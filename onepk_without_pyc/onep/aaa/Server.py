# 2015.02.05 17:20:34 IST
import onep.core.exception.OnepIllegalArgumentException
from onep.core.util.Enum import enum

class Server(object):
    """
    Server class describes the AAA Server that is used for user
    authentication. Each server is characterized by its IP Address
    and the AAA protocol.
    """

    OnepAAAProtocol = enum('ONEP_AAA_PROTOCOL_RADIUS', 'ONEP_AAA_PROTOCOL_TACACSPLUS', 'ONEP_AAA_PROTOCOL_LOCAL')

    def __init__(self, address, protocol):
        """AAA server constructor, used internally"""
        self.address = address
        self.protocol = protocol




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:20:34 IST
