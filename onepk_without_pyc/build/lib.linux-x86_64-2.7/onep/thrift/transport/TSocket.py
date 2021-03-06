# 2015.02.05 17:20:22 IST
from TTransport import *
import os
import errno
import socket
import sys

class TSocketBase(TTransportBase):

    def _resolveAddr(self):
        if self._unix_socket is not None:
            return [(socket.AF_UNIX,
              socket.SOCK_STREAM,
              None,
              None,
              self._unix_socket)]
        else:
            return socket.getaddrinfo(self.host, self.port, socket.AF_UNSPEC, socket.SOCK_STREAM, 0, socket.AI_PASSIVE)



    def close(self):
        if self.handle:
            self.handle.close()
            self.handle = None




class TSocket(TSocketBase):
    """Socket implementation of TTransport base."""


    def __init__(self, host = 'localhost', port = 9090, unix_socket = None):
        """Initialize a TSocket
        
            @param host(str)  The host to connect to.
            @param port(int)  The (TCP) port to connect to.
            @param unix_socket(str)  The filename of a unix socket to connect to.
                                     (host and port will be ignored.)
            """
        self.host = host
        self.port = port
        self.handle = None
        self._unix_socket = unix_socket
        self._timeout = None



    def setHandle(self, h):
        self.handle = h



    def isOpen(self):
        return self.handle is not None



    def setTimeout(self, ms):
        if ms is None:
            self._timeout = None
        else:
            self._timeout = ms / 1000.0
        if self.handle is not None:
            self.handle.settimeout(self._timeout)



    def open(self):
        try:
            res0 = self._resolveAddr()
            for res in res0:
                self.handle = socket.socket(res[0], res[1])
                self.handle.settimeout(self._timeout)
                try:
                    self.handle.connect(res[4])
                except socket.error as e:
                    if res is not res0[-1]:
                        continue
                    else:
                        raise e
                break

        except socket.error as e:
            if self._unix_socket:
                message = 'Could not connect to socket %s' % self._unix_socket
            else:
                message = 'Could not connect to %s:%d' % (self.host, self.port)
            raise TTransportException(type=TTransportException.NOT_OPEN, message=message)



    def read(self, sz):
        try:
            buff = self.handle.recv(sz)
        except socket.error as e:
            if e.args[0] == errno.ECONNRESET and (sys.platform == 'darwin' or sys.platform.startswith('freebsd')):
                self.close()
                buff = ''
            else:
                raise 
        if len(buff) == 0:
            raise TTransportException(type=TTransportException.END_OF_FILE, message='TSocket read 0 bytes')
        return buff



    def write(self, buff):
        if not self.handle:
            raise TTransportException(type=TTransportException.NOT_OPEN, message='Transport not open')
        sent = 0
        have = len(buff)
        while sent < have:
            plus = self.handle.send(buff)
            if plus == 0:
                raise TTransportException(type=TTransportException.END_OF_FILE, message='TSocket sent 0 bytes')
            sent += plus
            buff = buff[plus:]




    def flush(self):
        pass




class TServerSocket(TSocketBase, TServerTransportBase):
    """Socket implementation of TServerTransport base."""


    def __init__(self, host = None, port = 9090, unix_socket = None):
        self.host = host
        self.port = port
        self._unix_socket = unix_socket
        self.handle = None



    def listen(self):
        res0 = self._resolveAddr()
        for res in res0:
            if res[0] is socket.AF_INET6 or res is res0[-1]:
                break

        if self._unix_socket:
            tmp = socket.socket(res[0], res[1])
            try:
                tmp.connect(res[4])
            except socket.error as err:
                (eno, message,) = err.args
                if eno == errno.ECONNREFUSED:
                    os.unlink(res[4])
        self.handle = socket.socket(res[0], res[1])
        self.handle.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        if hasattr(self.handle, 'settimeout'):
            self.handle.settimeout(None)
        self.handle.bind(res[4])
        self.handle.listen(128)



    def accept(self):
        (client, addr,) = self.handle.accept()
        result = TSocket()
        result.setHandle(client)
        return result




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:20:23 IST
