# 2015.02.05 17:20:20 IST
import os
import socket
import ssl
from thrift.transport import TSocket
from thrift.transport.TTransport import TTransportException

class TSSLSocket(TSocket.TSocket):
    """
      SSL implementation of client-side TSocket
    
      This class creates outbound sockets wrapped using the
      python standard ssl module for encrypted connections.
      
      The protocol used is set using the class variable
      SSL_VERSION, which must be one of ssl.PROTOCOL_* and
      defaults to  ssl.PROTOCOL_TLSv1 for greatest security.
      """

    SSL_VERSION = ssl.PROTOCOL_TLSv1

    def __init__(self, host = 'localhost', port = 9090, validate = True, ca_certs = None, unix_socket = None):
        """
        @param validate: Set to False to disable SSL certificate validation entirely.
        @type validate: bool
        @param ca_certs: Filename to the Certificate Authority pem file, possibly a
        file downloaded from: http://curl.haxx.se/ca/cacert.pem  This is passed to
        the ssl_wrap function as the 'ca_certs' parameter.
        @type ca_certs: str
        
        Raises an IOError exception if validate is True and the ca_certs file is
        None, not present or unreadable.
        """
        self.validate = validate
        self.is_valid = False
        self.peercert = None
        if not validate:
            self.cert_reqs = ssl.CERT_NONE
        else:
            self.cert_reqs = ssl.CERT_REQUIRED
        self.ca_certs = ca_certs
        if validate:
            if ca_certs is None or not os.access(ca_certs, os.R_OK):
                raise IOError('Certificate Authority ca_certs file "%s" is not readable, cannot validate SSL certificates.' % ca_certs)
        TSocket.TSocket.__init__(self, host, port, unix_socket)



    def open(self):
        try:
            res0 = self._resolveAddr()
            for res in res0:
                (sock_family, sock_type,) = res[0:2]
                ip_port = res[4]
                plain_sock = socket.socket(sock_family, sock_type)
                self.handle = ssl.wrap_socket(plain_sock, ssl_version=self.SSL_VERSION, do_handshake_on_connect=True, ca_certs=self.ca_certs, cert_reqs=self.cert_reqs)
                self.handle.settimeout(self._timeout)
                try:
                    self.handle.connect(ip_port)
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



    def _validate_cert(self):
        """internal method to validate the peer's SSL certificate, and to check the
        commonName of the certificate to ensure it matches the hostname we
        used to make this connection.  Does not support subjectAltName records
        in certificates.
        
        raises TTransportException if the certificate fails validation."""
        cert = self.handle.getpeercert()
        self.peercert = cert
        if 'subject' not in cert:
            raise TTransportException(type=TTransportException.NOT_OPEN, message='No SSL certificate found from %s:%s' % (self.host, self.port))
        fields = cert['subject']
        for field in fields:
            if not isinstance(field, tuple):
                continue
            cert_pair = field[0]
            if len(cert_pair) < 2:
                continue
            (cert_key, cert_value,) = cert_pair[0:2]
            if cert_key != 'commonName':
                continue
            certhost = cert_value
            if certhost == self.host:
                self.is_valid = True
                return 
            raise TTransportException(type=TTransportException.UNKNOWN, message='Host name we connected to "%s" doesn\'t match certificate provided commonName "%s"' % (self.host, certhost))

        raise TTransportException(type=TTransportException.UNKNOWN, message='Could not validate SSL certificate from host "%s".  Cert=%s' % (self.host, cert))




class TSSLServerSocket(TSocket.TServerSocket):
    """
      SSL implementation of TServerSocket
    
      This uses the ssl module's wrap_socket() method to provide SSL
      negotiated encryption.
      """

    SSL_VERSION = ssl.PROTOCOL_TLSv1

    def __init__(self, host = None, port = 9090, certfile = 'cert.pem', unix_socket = None):
        """Initialize a TSSLServerSocket
        
        @param certfile: The filename of the server certificate file, defaults to cert.pem
        @type certfile: str
        @param host: The hostname or IP to bind the listen socket to, i.e. 'localhost' for only allowing
        local network connections. Pass None to bind to all interfaces.
        @type host: str
        @param port: The port to listen on for inbound connections.
        @type port: int
        """
        self.setCertfile(certfile)
        TSocket.TServerSocket.__init__(self, host, port)



    def setCertfile(self, certfile):
        """Set or change the server certificate file used to wrap new connections.
        
        @param certfile: The filename of the server certificate, i.e. '/etc/certs/server.pem'
        @type certfile: str
        
        Raises an IOError exception if the certfile is not present or unreadable.
        """
        if not os.access(certfile, os.R_OK):
            raise IOError('No such certfile found: %s' % certfile)
        self.certfile = certfile



    def accept(self):
        (plain_client, addr,) = self.handle.accept()
        try:
            client = ssl.wrap_socket(plain_client, certfile=self.certfile, server_side=True, ssl_version=self.SSL_VERSION)
        except ssl.SSLError as ssl_exc:
            plain_client.close()
            return None
        result = TSocket.TSocket()
        result.setHandle(client)
        return result




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:20:21 IST
