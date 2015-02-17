# 2015.02.05 17:23:00 IST
from onep.RoutingIDL.ttypes import L3UcastRouteRangeIDL
from Shared.ttypes import NetworkPrefixIDL
from onep.routing.RouteRange import RouteRange
from onep.interfaces.NetworkInterface import NetworkInterface
from onep.interfaces.NetworkPrefix import NetworkPrefix
from onep.core.exception.OnepIllegalArgumentException import OnepIllegalArgumentException
from onep.core.util.Enum import isValidEnum

class L3UnicastRouteRange(RouteRange):
    """
    L3UnicastRouteRange class represents the range tuple
    (Start L3 Unicast Prefix, Range Type, Count)
    used for filtering.
    """


    def __init__(self, start_prefix, range_type, count):
        """
                Create the range tuple (Start L3 Unicast Prefix, Range Type, Count)
                used for filtering.
        
                If range type is EQUAL_OR_LARGER, then the range indicates Count
                routes starting with the prefix equal or lexically larger than
                Start Prefix.
        
                If range type is ROUTING_ROUTE_RANGE_LARGER, then the filter
                indicates Count routes starting with the prefix lexically
                larger than Start Prefix.
        
                If count is 0, it is treated as no count limit and all routes
                matching the (Start L3 Unicast Prefix, Range Type) are included.
        
                @param start_prefix:
                        The starting prefix reference of the range.
                @type start_prefix: L{NetworkPrefix<onep.interfaces.NetworkPrefix>}
                @param range_type:
                        Indicate if the range include the start prefix.
                @type range_type: L{RouteRange.RangeType<onep.routing.RouteRange>}
                @param count:
                           Maximum number of route the range should cover.
                           A count of 0 means no limit.
                @type count: C{int}
                """
        super(L3UnicastRouteRange, self).__init__()
        if not isinstance(start_prefix, NetworkPrefix):
            raise OnepIllegalArgumentException('start_prefix', 'Invalid type')
        if not isValidEnum(RouteRange.RangeType, range_type):
            raise OnepIllegalArgumentException('range_type', 'Invalid type')
        if count < 0 or not isinstance(count, int):
            raise OnepIllegalArgumentException('count', 'Invalid type')
        self._start_prefix = start_prefix
        self._range_type = range_type
        self._count = count



    def _get_start_prefix(self):
        return self._start_prefix



    def _set_start_prefix(self, start_prefix):
        if start_prefix is None or not isinstance(start_prefix, NetworkPrefix):
            raise OnepIllegalArgumentException('start_prefix', 'Invalid type')
        self._start_prefix = start_prefix


    _doc = 'starting prefix reference of the range to set\n\n    @type: L{NetworkPrefix<onep.interfaces.NetworkPrefix>}\n    @raise OnepIllegalArgumentException: If network prefix is invalid\n    '
    start_prefix = property(_get_start_prefix, _set_start_prefix, None, _doc)

    def _get_range_type(self):
        return self._range_type



    def _set_range_type(self, range_type):
        if not isValidEnum(RouteRange.RangeType, range_type):
            raise OnepIllegalArgumentException('range_type', 'Invalid type')
        self._range_type = range_type


    _doc = 'range_type indicating if the range include the\n    start prefix.\n\n    @type: L{RouteRange.RangeType<onep.routing.RouteRange>}\n    @raise OnepIllegalArgumentException: If range_type is invalid\n    '
    range_type = property(_get_range_type, _set_range_type, None, _doc)

    def _get_count(self):
        return self._count



    def _set_count(self, count):
        if count < 0 or not isinstance(count, int):
            raise OnepIllegalArgumentException('count', 'Invalid type')
        self._count = count


    _doc = 'maximum number of route the range should cover\n\n    @type: C{int}\n    @raise OnepIllegalArgumentException: If count is invalid\n    '
    count = property(_get_count, _set_count, None, _doc)

    def _to_idl(self):
        prefix_idl = None
        addr_idl = None
        if self._start_prefix is not None:
            addr_idl = NetworkInterface._convert_to_networkaddressidl(self._start_prefix.address)
            prefix_idl = NetworkPrefixIDL(self._start_prefix.prefix_length, addr_idl)
        return L3UcastRouteRangeIDL(self._range_type, self._count, prefix_idl)




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:23:00 IST
