# 2015.02.05 17:22:58 IST
from onep.routing.RIBFilter import RIBFilter
from onep.RoutingIDL.ttypes import L3UcastRibFilterIDL
from onep.routing.L3UnicastRoute import *
from onep.core.util.Enum import OnepIllegalEnumException

class L3UnicastRIBFilter(RIBFilter):
    """
    This class implements the RibFilter abstract class for filtering
    route state events according to the specified criteria.
    
    A Filter can be used to provide fine-tuned control over which events to listen
    to.
    """

    _owner_type = L3UnicastRoute.OwnerType.NONE
    _owner_tag = ''
    _subnet = None
    _log = logging.getLogger(__name__)

    def __init__0(self):
        super(L3UnicastRIBFilter, self).__init__()
        self._subnet = NetworkPrefix('0.0.0.0', 0)



    def __init__(self, owner_type = None, owner_tag = None, subnet = None):
        """
        Constructor for L3UnicastRIBFilter
        
        @param owner_type: The protocol type of the route ownerType. (default L3UnicastRoute.OwnerType.NONE)
        @type : C{int} refer ownerType in L{L3UnicastRoute<onep.routing.L3unicastRoute>}
        @param owner_tag: The owner tag associated with the route (default '')
        @type owner_tag: C{str}
        @param subnet: The subnet the route should match. 
            default 0.0.0.0/0 if IPv4 scope and 0::0/0 if IPv6 scope.
        @type subnet : L{NetworkPrefix<onep.interfaces.NetworkPrefix>}
        """
        if owner_type is None and owner_tag is None and subnet is None:
            self.__init__0()
        else:
            super(L3UnicastRIBFilter, self).__init__()
            if owner_type:
                if not isinstance(owner_type, int):
                    raise OnepIllegalArgumentException('ownerType', 'Invalid type')
                self.owner_type = owner_type
            if owner_tag:
                if not isinstance(owner_tag, str):
                    raise OnepIllegalArgumentException('ownerTag', 'Invalid type')
            self.owner_tag = owner_tag
            if subnet and not isinstance(subnet, NetworkPrefix):
                raise OnepIllegalArgumentException('subnet', 'Invalid type')
            self.subnet = subnet



    def _get_owner_type(self):
        return self._owner_type



    def _set_owner_type(self, owner_type):
        try:
            L3UnicastRoute.OwnerType.enumval(owner_type)
            self._owner_type = owner_type
        except OnepIllegalEnumException:
            raise OnepIllegalArgumentException('ownerType', str(owner_type))


    _doc = 'the protocol type of the route owner.\n    \n    @type: L{Enum<onep.core.util.Enum>}\n    @raise OnepIllegalArgumentException: If ownerType invalid \n    '
    owner_type = property(_get_owner_type, _set_owner_type, None, _doc)

    def _get_owner_tag(self):
        return self._owner_tag



    def _set_owner_tag(self, owner_tag):
        if owner_tag:
            if not isinstance(owner_tag, str):
                raise OnepIllegalArgumentException('ownerTag', 'Invalid type')
            self._owner_tag = owner_tag


    _doc = 'tag of the route owner.\n    @type: C{str}\n    @raise OnepIllegalArgumentException: If owner_tag is invalid\n    '
    owner_tag = property(_get_owner_tag, _set_owner_tag, None, _doc)

    def _get_subnet(self):
        return self._subnet



    def _set_subnet(self, subnet):
        if subnet is not None:
            if not isinstance(subnet, NetworkPrefix):
                raise OnepIllegalArgumentException('subnet', 'Invalid type')
            self._subnet = subnet


    _doc = 'subnet the route should match.\n    \n    @type: L{NetworkPrefix<onep.interfaces.NetworkPrefix>}\n    '
    subnet = property(_get_subnet, _set_subnet, None, _doc)

    def _to_idl(self):
        prefix_idl = None
        if self._subnet:
            addr_idl = NetworkInterface._convert_to_networkaddressidl(self._subnet.address)
            prefix_idl = NetworkPrefixIDL(self._subnet.prefix_length, addr_idl)
            self._log.info('Calling NetworkPrefixIDL')
        else:
            subnet0 = NetworkPrefix('0.0.0.0', 0)
            addr_idl = NetworkInterface._convert_to_networkaddressidl(subnet0.address)
            prefix_idl = NetworkPrefixIDL(subnet0.prefix_length, addr_idl)
            self._log.info('Calling NetworkPrefixIDL')
        return L3UcastRibFilterIDL(0 if self._owner_type is None else self._owner_type, self._owner_tag, prefix_idl, -1, -1, -1)




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:22:58 IST
