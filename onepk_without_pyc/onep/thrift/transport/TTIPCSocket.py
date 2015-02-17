# 2015.02.05 17:23:14 IST
import socket
import logging
from thrift.transport.TSocket import TSocket
from thrift.transport.TTransport import TTransportException

class TTIPCSocket(TSocket):
    """TIPC Socket implementation"""

    ONEP_TIPC_PORT = 15003
    ONEP_TIPC_TIMOUT = 5

    def __init__(self, port = ONEP_TIPC_PORT):
        """Initialize a TTIPCSocket
        
            @param port(int)  The (TIPC) port to connect to.
            """
        TSocket.__init__(self, port=port)
        self.setTimeout(TTIPCSocket.ONEP_TIPC_TIMOUT * 1000.0)



    def open(self):
        """Open a TIPC Socket"""
        try:
            srvaddr = (socket.TIPC_ADDR_NAME,
             self.port,
             5,
             0)
            self.handle = socket.socket(socket.AF_TIPC, socket.SOCK_STREAM)
        except Exception as e:
            logging.error('TIPC is not supported: ' + e.__str__())
            raise e
        try:
            self.handle.settimeout(None)
            self.handle.connect(srvaddr)
        except socket.error as e:
            message = 'Could not connect to TIPC:%d' % self.port
            raise TTransportException(type=TTransportException.NOT_OPEN, message=message)




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:23:14 IST
