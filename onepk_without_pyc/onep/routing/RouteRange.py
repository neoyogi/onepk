# 2015.02.05 17:22:58 IST
from onep.core.util.Enum import enum

class RouteRange(object):
    """
    This abstract class is the parent class of L3UnicastRouteRange and 
    in the future for L3MulticastRouteRange, L2UnicastRouteRange,
    L2MulticastRouteRange, etc.
    
    All common fields among these derived class will be defined in this 
    class.      
    """

    RangeType = enum('EQUAL_OR_LARGER', 'LARGER')
    _start_prefix = None
    _range_type = int()
    _count = long()


# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:22:58 IST
