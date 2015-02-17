# 2015.02.05 17:22:59 IST
from onep.routing.Route import *
from onep.interfaces.NetworkPrefix import NetworkPrefix
from onep.interfaces.NetworkInterface import NetworkInterface
from onep.RoutingIDL.ttypes import RouteIDL
from onep.RoutingIDL.ttypes import L3UcastRouteIDL
from Shared.ttypes import NetworkPrefixIDL
from onep.RoutingEventIDL.ttypes import L3UcastRouteOutIDL
from onep.routing.L3UnicastNextHop import L3UnicastNextHop
from onep.core.exception.OnepIllegalArgumentException import OnepIllegalArgumentException
import logging

class L3UnicastRoute(Route):
    """
    This clase represents a layer 3 unicast route.
    """

    OwnerType = enum('NONE', 'APP', 'CONNECTED', 'STATIC', 'BGP', 'MOBILE', 'RIP', 'OSPF', 'ISIS', 'EIGRP', 'IGRP2', 'OSPFV3', 'ODR', 'HSRP', 'NHRP', 'LISP', 'NEMO', 'ND', 'RPL', 'LOCAL', 'MAX')
    RouteType = enum('NONE', 'OSPF_INTRA', 'OSPF_INTER', 'OSPF_EXTERN1', 'OSPF_EXTERN2', 'OSPF_NSSA1', 'OSPF_NSSA2', 'BGP_INT', 'BGP_EXT', 'BGP_LOC', 'BGP_ANY', 'ISIS_SUM', 'ISIS_L1', 'ISIS_L2', 'ISIS_L1_IA', 'IGRP2_INT', 'IGRP2_EXT', 'MAX')
    _DEFAULT_ADMIN_DISTANCE = 0
    _prefix = None
    _next_hop_list = set()
    _admin_distance = long()
    _route_type = RouteType.NONE
    _owner_type = OwnerType.NONE
    _owner_tag = ''
    _metric = 0
    _error_code = Route.RouteErrorCode.NONE

    def __init__0(self, prefix):
        super(L3UnicastRoute, self).__init__()
        if prefix and not isinstance(prefix, NetworkPrefix):
            raise OnepIllegalArgumentException('prefix', 'invalid')
        self._prefix = prefix
        self._next_hop_list = None
        self._admin_distance = self._DEFAULT_ADMIN_DISTANCE



    def __init__1(self, prefix, next_hop_list):
        super(L3UnicastRoute, self).__init__()
        if prefix and not isinstance(prefix, NetworkPrefix):
            raise OnepIllegalArgumentException('prefix', 'invalid')
        self._prefix = prefix
        self._next_hop_list = next_hop_list
        self._admin_distance = self._DEFAULT_ADMIN_DISTANCE



    def __init__(self, prefix, next_hop_list = None, owner_type = None, owner_tag = None, route_type = None, admin_distance = None, metric = 0, error_code = 0):
        """
        Constructor that provides convenience 
        can be called with only prefix 
        or prefix and Next hop list 
          
        @param prefix :Prefix of the destination network in the route.
        @type prefix: L{NetworkPrefix<onep.interfaces.NetworkPrefix>}
        @param next_hop_list: The list of next hop of the route.
                               Note that the list is in the form of "set"
                               to ensure duplicate hops in the list.
        @type next_hop_list: C{list}         
        """
        if owner_type is None and owner_tag is None and route_type is None and admin_distance is None and metric == 0 and error_code == 0:
            if next_hop_list is None:
                self.__init__0(prefix)
            else:
                self.__init__1(prefix, next_hop_list)
        else:
            self.__init__2(prefix, next_hop_list, owner_type, owner_tag, route_type, admin_distance, metric, error_code)
        self.log = logging.getLogger('onep.' + __name__)



    def __init__2(self, prefix, next_hop_list, owner_type, owner_tag, route_type, admin_distance, metric, error_code):
        super(L3UnicastRoute, self).__init__()
        self._prefix = prefix
        self._next_hop_list = next_hop_list
        if metric == None:
            metric = 0
        if error_code == None:
            error_code = Route.RouteErrorCode.NONE
        if admin_distance == None:
            self._admin_distance = self._DEFAULT_ADMIN_DISTANCE
        else:
            self._admin_distance = admin_distance
        self._owner_type = owner_type
        if owner_tag is None:
            self._owner_tag = ''
        else:
            self._owner_tag = owner_tag
        self._route_type = route_type
        self._metric = metric
        self._error_code = error_code



    def _get_prefix(self):
        return self._prefix



    def _set_prefix(self, prefix_):
        if not prefix_ or not isinstance(prefix_, NetworkPrefix):
            raise OnepIllegalArgumentException('prefix', 'invalid')
        self._prefix = prefix_


    _doc = 'prefix of the destination network in the route.\n    @type: L{NetworkPrefix<onep.interfaces.Networkprefix>}\n    @raise OnepIllegalArgumentException: If invalid prefix\n    '
    prefix = property(_get_prefix, _set_prefix, None, _doc)

    def _get_owner_type(self):
        return self._owner_type


    _doc = 'Gets the owner type of the route.\n    @type : C{int}\n    '
    owner_type = property(_get_owner_type, None, None, _doc)

    def _get_owner_tag(self):
        return self._owner_tag


    _doc = 'Gets the tag of the route owner.\n    @type: C{str}\n    '
    owner_tag = property(_get_owner_tag, None, None, _doc)

    def _get_route_type(self):
        return self._route_type


    _doc = 'Gets the type of the route.\n    @type : C{int}\n    '
    route_type = property(_get_route_type, None, None, _doc)

    def _get_next_hop_list(self):
        return self._next_hop_list



    def _set_next_hop_list(self, hop_list):
        if hop_list and not isinstance(hop_list, list):
            raise OnepIllegalArgumentException('next_hop_list', 'invalid')
        self._next_hop_list = hop_list


    _doc = ' Sets the list of next hop of the route.\n    Note that the list is in the form of "set" to ensure\n    no duplicate hops in the list.\n        \n    The following example shows how to append a next hop to the route:\n        \n    hop_list = route.next_hop_list\n    route.next_hop_list = hop_list.append(new_hop) \n          \n    @type: C{list} of L{L3UnicastNextHop<onep.routing.L3UnicastNextHop>}            \n    '
    next_hop_list = property(_get_next_hop_list, _set_next_hop_list, None, _doc)

    def _get_admin_distance(self):
        return self._admin_distance



    def _set_admin_distance(self, admin_dist):
        if admin_dist <= 0 or admin_dist >= 255:
            raise OnepIllegalArgumentException('adminDistance', 'Invalid')
        self._admin_distance = admin_dist


    _doc = 'The administrative distance of the route.\n    @type: C{int}\n    @raise OnepIllegalArgumentException: If admin distance invalid\n    '
    admin_distance = property(_get_admin_distance, _set_admin_distance, None, _doc)

    def _get_metric(self):
        return self._metric


    _doc = 'The metric of the route.\n    @type: C{int}\n    '
    metric = property(_get_metric, None, None, _doc)

    def _get_error_code(self):
        return self._error_code


    _doc = 'The route error code.\n    @type: C{int}\n    '
    error_code = property(_get_error_code, None, None, _doc)

    def __str__(self):
        """
        Gets the string representation of the  object
        @return: The string representation of the object.
        """
        return 'L3UnicastRoute[' + 'address:' + self.prefix.address + '/' + str(self.prefix.prefix_length) + ',' + 'ownerType:' + self.OwnerType.enumval(self.owner_type) + ',' + 'ownerTag:' + self.owner_tag + ',' + 'routeType:' + self.RouteType.enumval(self.route_type) + ',' + 'adminDistance:' + str(self.admin_distance) + ',' + 'metric:' + str(self.metric) + ',' + 'errorCode:' + str(self.error_code) + ']'



    def _to_idl(self):
        prefix_idl = None
        if self._prefix != None:
            addr_idl = NetworkInterface._convert_to_networkaddressidl(self._prefix.address)
            prefix_idl = NetworkPrefixIDL(self._prefix.prefix_length, addr_idl)
            self.log.info('Creating NetworkprefixIDL')
        r_idl = RouteIDL(0, 0, 0)
        r_idl.adminDistance = self._admin_distance
        r_idl.metric = self._metric
        hop_id_list = list()
        if self._next_hop_list != None:
            for hop in self._next_hop_list:
                if hop != None:
                    hop_id_list.append(hop._to_idl())

        self.log.info('Creating L3UcastRouteIDL')
        if self._route_type == None:
            self._route_type = 0
        if self._owner_type == None:
            self._owner_type = 0
        return L3UcastRouteIDL(r_idl, self._route_type, self._owner_type, self._owner_tag, prefix_idl, hop_id_list)



    @staticmethod
    def _from_idl(route_idl, ne):
        if route_idl == None:
            return 
        nh_set = set()
        for nh_idl in route_idl.hopList:
            if nh_idl != None:
                nh_set.add(L3UnicastNextHop._from_idl(nh_idl, ne))

        prefix = None
        addr = None
        if route_idl.prefix != None and route_idl.prefix.addr != None:
            if isinstance(route_idl, L3UcastRouteIDL):
                addr = NetworkInterface._convert_to_inetaddress(route_idl.prefix.addr)
            elif isinstance(route_idl, L3UcastRouteOutIDL):
                addr = route_idl.prefix.addr.addr
            prefix = NetworkPrefix(addr, route_idl.prefix.prefix_len)
        return L3UnicastRoute(prefix, nh_set, route_idl.ownerType, route_idl.tag, route_idl.l3UcastRouteType, route_idl.route.adminDistance, route_idl.route.metric, route_idl.route.ec)




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:22:59 IST
