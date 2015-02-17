# 2015.02.05 17:22:58 IST
from onep.core.util.Enum import enum

class Route(object):
    """
    This abstract class is the parent class of L3UnicastRoute and
    in the future for L3MulticastRoute, L2UnicastRoute,
    L2MulticastRoute, etc.
    
    All common fields among these derived class will be defined in this
    class.
    """

    RouteErrorCode = enum('NONE', 'SUCCESS', 'PARTIAL_SUCCESS', 'EAGAIN', 'FAILURE', 'MAX')


# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:22:58 IST
