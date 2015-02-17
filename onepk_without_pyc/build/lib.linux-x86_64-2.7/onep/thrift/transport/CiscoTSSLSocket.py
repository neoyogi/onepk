# 2015.02.05 17:20:19 IST
import hashlib
import os
import ssl
import socket
import logging
from onep.core.exception import OnepIllegalArgumentException
from onep.thrift.transport.TSSLSocket import TSSLSocket
from onep.thrift.transport.TTransport import TTransportException
from onep.core.util import enum, HostIpCheck, tlspinning
CertificateMatchType = enum(DNS_NAME=0, COMMON_NAME=1, IP_ADDRESS=2, UNSTRUCTURED_ADDRESS=3)

class CiscoTSSLSocket(TSSLSocket):

    def __init__(self, host = 'localhost', port = 9090, validate = True, keyfile = None, certfile = None, ca_certs = None, unix_socket = None, pinning_file = None, unverified_handler = None, accept_once = []):
        if not isinstance(accept_once, list):
            raise OnepIllegalArgumentException('accept_once must be a list but it', str(accept_once))
        self.log = logging.getLogger(__name__)
        if validate and accept_once:
            validate = False
        if validate and ca_certs is None:
            validate = False
            self.ssl_exception = 'No CA certificates were given so the network element could not be verified.'
        else:
            self.ssl_exception = None
        TSSLSocket.__init__(self, host, port, validate, ca_certs, unix_socket)
        self.certfile = certfile
        self.keyfile = keyfile
        self.pinning_file = pinning_file
        self.unverified_handler = unverified_handler
        self.accept_once = accept_once
        if validate:
            if certfile and not os.access(certfile, os.R_OK):
                raise IOError('Client Certificate certfile file "%s" is not readable, cannot validate SSL certificates.' % certfile)
            if keyfile and not os.access(keyfile, os.R_OK):
                raise IOError('Client keyfile file "%s" is not readable, cannot validate SSL certificates.' % keyfile)



    def open(self):
        try:
            res0 = self._resolveAddr()
            for res in res0:
                (sock_family, sock_type,) = res[0:2]
                ip_port = res[4]
                plain_sock = socket.socket(sock_family, sock_type)
                try:
                    self.handle = ssl.wrap_socket(plain_sock, keyfile=self.keyfile, certfile=self.certfile, ssl_version=self.SSL_VERSION, do_handshake_on_connect=True, ca_certs=self.ca_certs, cert_reqs=self.cert_reqs)
                except ssl.SSLError as e:
                    message = 'SSLError: Error in certificate or key file(s): %s' % e
                    raise TTransportException(type=TTransportException.NOT_OPEN, message=message)
                self.handle.settimeout(self._timeout)
                try:
                    self.handle.connect(ip_port)
                except ssl.SSLError as e:
                    if self.validate:
                        self.handle.close()
                        self.validate = False
                        self.cert_reqs = ssl.CERT_NONE
                        self.ssl_exception = e
                        return self.open()
                    raise e
                except socket.error as e:
                    if res is not res0[-1]:
                        continue
                    else:
                        raise e
                break

        except socket.error as e:
            if self._unix_socket:
                message = 'Could not connect to secure socket %s' % self._unix_socket
            else:
                message = 'Could not connect to %s:%d' % (self.host, self.port)
            raise TTransportException(type=TTransportException.NOT_OPEN, message=message)
        if self.validate:
            self._validate_cert()
        elif self.ssl_exception is not None:
            self._do_pinning(self.handle.getpeercert(True), self.ssl_exception)
        elif self.accept_once:
            if self.handle.getpeercert(True) in self.accept_once:
                return 
            self.handle.close()
            self.validate = True
            self.cert_reqs = ssl.CERT_REQUIRED
            return self.open()



    def _validate_ip_addrs(self, addrs, type):
        self.log.debug('ip addr: %s self.host %s' % (addrs, self.host))
        for addr in addrs:
            if HostIpCheck(str(addr)) == HostIpCheck(self.host):
                self.is_valid = True
                return 

        self.log.warn('Host name we connected to "%s" doesn\'t match certificate provided ip address "%s"' % (self.host, addrs))
        if type == CertificateMatchType.UNSTRUCTURED_ADDRESS:
            field = 'unstructuredAddress'
        else:
            field = 'subjectAltName'
        e = TTransportException(type=TTransportException.UNKNOWN, message='Host name we connected to "%s" doesn\'t match certificate provided "%s %s"' % (self.host, field, addrs))
        self._do_pinning(self.handle.getpeercert(True), e)



    def _validate_names(self, names, type):
        self.log.debug('host: %s self.host %s' % (names, self.host))
        for name in names:
            if name.lower() == self.host.lower():
                self.is_valid = True
                return 

        if type == CertificateMatchType.COMMON_NAME:
            field = 'commonName'
        else:
            field = 'subjectAltName'
        self.log.warn('Host name we connected to "%s" doesn\'t match certificate provided dns names: %s' % (self.host, names))
        e = TTransportException(type=TTransportException.UNKNOWN, message='Host name we connected to "%s" doesn\'t match certificate provided %s: %s' % (self.host, field, names))
        self._do_pinning(self.handle.getpeercert(True), e)



    def _get_fields(self):
        dns_names = []
        ip_addrs = []
        common_names = []
        unstructured_addrs = []
        if 'subjectAltName' in self.peercert:
            fields = self.peercert['subjectAltName']
            for item in fields:
                if not isinstance(item, tuple) or len(item) < 2:
                    continue
                (cert_key, cert_value,) = item[0:2]
                if cert_key == 'DNS':
                    dns_names.append(cert_value)
                if cert_key == 'IP Address':
                    ip_addrs.append(cert_value)

        if 'subject' in self.peercert:
            fields = self.peercert['subject']
            for field in fields:
                for item in field:
                    if not isinstance(item, tuple) or len(item) < 2:
                        continue
                    (cert_key, cert_value,) = item[0:2]
                    if cert_key == 'commonName':
                        common_names.append(cert_value)
                    if cert_key == 'unstructuredAddress':
                        unstructured_addrs.append(cert_value)


        return [dns_names,
         ip_addrs,
         common_names,
         unstructured_addrs]



    def _validate_cert(self):
        """
        Internal method to validate the peer's SSL certificate.
        raises OnepCertificateException if the certificate fails validation.
        """
        cert = self.handle.getpeercert()
        self.peercert = cert
        self.log.debug('cert: %s' % cert)
        dns_names = []
        ip_addrs = []
        common_names = []
        unstructured_addrs = []
        (dns_names, ip_addrs, common_names, unstructured_addrs,) = self._get_fields()
        if HostIpCheck(self.host).is_ipaddress():
            if len(ip_addrs) > 0:
                self._validate_ip_addrs(ip_addrs, CertificateMatchType.IP_ADDRESS)
            elif len(unstructured_addrs) > 0:
                self._validate_ip_addrs(unstructured_addrs, CertificateMatchType.UNSTRUCTURED_ADDRESS)
            else:
                self.log.warn('Certificate provided neither ip address nor unstructured address')
                e = TTransportException(type=TTransportException.UNKNOWN, message='Certificate provided neither ip address nor unstructured address')
                self._do_pinning(self.handle.getpeercert(True), e)
        elif len(dns_names) > 0:
            self._validate_names(dns_names, CertificateMatchType.DNS_NAME)
        elif len(common_names) > 0:
            self._validate_names(common_names, CertificateMatchType.COMMON_NAME)
        else:
            self.log.warn('Certificate provided neither dns name nor common name')
            e = TTransportException(type=TTransportException.UNKNOWN, message='Certificate provided neither dns name nor common name')
            self._do_pinning(self.handle.getpeercert(True), e)



    def _do_pinning(self, cert, cause):
        if cert is None:
            self.log.error('TLS pinning was attempted but there was no certificate to pin.')
            raise TTransportException(type=TTransportException.NOT_OPEN, message=str(cause))
        try:
            entry = tlspinning._get_entry(self.pinning_file, self.host)
        except:
            entry = None
        hash_type = None
        fingerprint = None
        changed = False
        if entry is not None:
            hash_type = entry[1]
            try:
                md = CiscoTSSLSocket._hashtypes[hash_type]()
            except KeyError:
                self.log.warn("The entry '%s' in the pinning file '%s' could not be used." % (entry[0], self.pinning_file))
                entry = None
            else:
                md.update(cert)
                hexdigest = md.hexdigest().upper()
                fingerprint = ':'.join((hexdigest[i:(i + 2)] for i in range(0, len(hexdigest), 2)))
                if entry[2].upper() == fingerprint:
                    return 
                changed = True
        if entry is None:
            hash_type = 'SHA-1'
            md = hashlib.sha1()
            md.update(cert)
            hexdigest = md.hexdigest().upper()
            fingerprint = ':'.join((hexdigest[i:(i + 2)] for i in range(0, len(hexdigest), 2)))
        decision = tlspinning.DecisionType.REJECT
        if self.unverified_handler is not None:
            decision = self.unverified_handler.handle_verify(self.host, hash_type, fingerprint, changed)
        if decision == tlspinning.DecisionType.ACCEPT_AND_PIN:
            if self.pinning_file:
                try:
                    tlspinning._update_entry(self.pinning_file, (self.host, hash_type, fingerprint))
                except Exception as e:
                    self.log.error("Failed to pin '%s' to pinning file '%s':  %s" % (self.host, self.pinning_file, e))
            else:
                self.log.error("No pinning file was given so '%s' could not be pinned." % self.host)
            self.accept_once.append(cert)
            return 
        if decision == tlspinning.DecisionType.ACCEPT_ONCE:
            self.accept_once.append(cert)
            return 
        raise TTransportException(type=TTransportException.UNKNOWN, message=str(cause))


    _hashtypes = {'MD5': hashlib.md5,
     'SHA-1': hashlib.sha1,
     'SHA-256': hashlib.sha256,
     'SHA-512': hashlib.sha512}


# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:20:19 IST
