# 2015.02.05 17:23:14 IST
from TTransport import *
from cStringIO import StringIO
import urlparse
import httplib
import warnings
import socket

class THttpClient(TTransportBase):
    """Http implementation of TTransport base."""


    def __init__(self, uri_or_host, port = None, path = None):
        """THttpClient supports two different types constructor parameters.
        
            THttpClient(host, port, path) - deprecated
            THttpClient(uri)
        
            Only the second supports https."""
        if port is not None:
            warnings.warn("Please use the THttpClient('http://host:port/path') syntax", DeprecationWarning, stacklevel=2)
            self.host = uri_or_host
            self.port = port
            assert path
            self.path = path
            self.scheme = 'http'
        else:
            parsed = urlparse.urlparse(uri_or_host)
            self.scheme = parsed.scheme
            assert self.scheme in ('http', 'https')
            if self.scheme == 'http':
                self.port = parsed.port or httplib.HTTP_PORT
            elif self.scheme == 'https':
                self.port = parsed.port or httplib.HTTPS_PORT
            self.host = parsed.hostname
            self.path = parsed.path
            if parsed.query:
                self.path += '?%s' % parsed.query
        self.__wbuf = StringIO()
        self.__http = None
        self.__timeout = None



    def open(self):
        if self.scheme == 'http':
            self.__http = httplib.HTTP(self.host, self.port)
        else:
            self.__http = httplib.HTTPS(self.host, self.port)



    def close(self):
        self.__http.close()
        self.__http = None



    def isOpen(self):
        return self.__http != None



    def setTimeout(self, ms):
        if not hasattr(socket, 'getdefaulttimeout'):
            raise NotImplementedError
        if ms is None:
            self.__timeout = None
        else:
            self.__timeout = ms / 1000.0



    def read(self, sz):
        return self.__http.file.read(sz)



    def write(self, buf):
        self.__wbuf.write(buf)



    def __withTimeout(f):

        def _f(*args, **kwargs):
            orig_timeout = socket.getdefaulttimeout()
            socket.setdefaulttimeout(args[0].__timeout)
            result = f(*args, **kwargs)
            socket.setdefaulttimeout(orig_timeout)
            return result


        return _f



    def flush(self):
        if self.isOpen():
            self.close()
        self.open()
        data = self.__wbuf.getvalue()
        self.__wbuf = StringIO()
        self.__http.putrequest('POST', self.path)
        self.__http.putheader('Host', self.host)
        self.__http.putheader('Content-Type', 'application/x-thrift')
        self.__http.putheader('Content-Length', str(len(data)))
        self.__http.endheaders()
        self.__http.send(data)
        (self.code, self.message, self.headers,) = self.__http.getreply()


    if hasattr(socket, 'getdefaulttimeout'):
        flush = __withTimeout(flush)


# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:23:14 IST
