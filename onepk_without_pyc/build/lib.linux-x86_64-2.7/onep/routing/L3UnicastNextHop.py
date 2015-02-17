# 2015.02.05 17:20:04 IST
from onep.routing.NextHop import NextHop
from onep.routing.L3UnicastScope import L3UnicastScope
from onep.core.util.Enum import enum
from onep.interfaces.NetworkInterface import NetworkInterface
from onep.RoutingIDL.ttypes import RouteNextHopIDL
from onep.RoutingIDL.ttypes import L3UcastRouteNextHopIDL
from onep.RoutingEventIDL.ttypes import L3UcastRouteNextHopOutIDL
from onep.core.exception.OnepIllegalArgumentException import OnepIllegalArgumentException
import logging
from onep.core.util.HostIpCheck import HostIpCheck
from ctypes import c_int

class L3UnicastNextHop(NextHop):
    """NextHop class represents a next hop of route, and support
    both IPv4 and IPv6.
    """

    _network_interface = None
    _address = None
    _scope = None
    _error_code = None
    _metric = None
    _route_tag = None
    log = logging.getLogger('onep.' + __name__)
    NextHopType = enum('DEFAULT', 'REPAIR')

    def __init__0(self, network_interface, address, metric):
        super(L3UnicastNextHop, self).__init__()
        if network_interface == None and address == None:
            raise OnepIllegalArgumentException('networkInterface and address invalid')
        if network_interface and not isinstance(network_interface, NetworkInterface):
            raise OnepIllegalArgumentException('networkInterface invalid')
        if address and not HostIpCheck(address).is_ipaddress():
            raise OnepIllegalArgumentException('address invalid')
        if metric is not None and not isinstance(metric, int):
            raise OnepIllegalArgumentException('metric invalid')
        self._network_interface = network_interface
        self._address = address
        self._scope = L3UnicastScope()
        self._metric = metric



    def __init__(self, network_interface, address, scope = None, error_code = None, metric = None):
        """Constructor. 
        This constructor can be used for convenience when the Scope is not 
        required, for example, when the route operation is REMOVE.
        
        @param network_interface: The network interface in the next hop to set.
        @type network_interface: L{NetworkInterface<onep.interfaces.NetworkInterface>}
        @param address: The address in the next hop to set.
        @type address: C{str}
        @param scope: The the next hop scope to set.
        @type scope: L{L3UnicastScope<onep.routing.L3UnicastScope>}
        @raise OnepIllegalArgumentException:
        The exception is thrown when both networkInterface and
        address are not valid.
        """
        if scope is None and error_code is None:
            self.__init__0(network_interface, address, metric)
        elif error_code is None:
            super(L3UnicastNextHop, self).__init__()
            if network_interface == None and address == None:
                raise OnepIllegalArgumentException('networkInterface and address invalid')
            if network_interface and not isinstance(network_interface, NetworkInterface):
                raise OnepIllegalArgumentException('networkInterface invalid')
            if address and not HostIpCheck(address).is_ipaddress():
                raise OnepIllegalArgumentException('address invalid')
            if metric is not None and not isinstance(metric, int):
                raise OnepIllegalArgumentException('invalid metric')
            self._network_interface = network_interface
            self._address = address
            self._scope = scope
            self._metric = metric
        else:
            self.__init__1(network_interface, address, scope, error_code, metric)



    def __init__1(self, network_interface, address, scope, errorCode, metric):
        super(L3UnicastNextHop, self).__init__()
        self._network_interface = network_interface
        self._address = address
        self._scope = scope
        self._error_code = errorCode
        self._metric = metric



    def _get_network_interface(self):
        return self._network_interface



    def _set_network_interface(self, network_interface):
        if network_interface is None or not isinstance(network_interface, NetworkInterface):
            raise OnepIllegalArgumentException('Not a valid Interface')
        self._network_interface = network_interface


    _doc = '\n    The network interface in the next hop\n    \n    @type: L{NetworkInterface<onep.interfaces.NetworkInterface>}\n    @raise OnepIllegalArgumentException: if interface not valid\n    '
    network_interface = property(_get_network_interface, _set_network_interface, None, _doc)

    def _get_address(self):
        return self._address



    def _set_address(self, address):
        if address is None or not HostIpCheck(address).is_ipaddress():
            raise OnepIllegalArgumentException('address invalid')
        self._address = address


    _doc = '\n    The address in the next hop\n    \n    @type: C{str}\n    @raise OnepIllegalArgumentException: if address not valid\n    '
    address = property(_get_address, _set_address, None, _doc)

    def _get_metric(self):
        return self._metric



    def _set_metric(self, metric):
        if metric is not None and not isinstance(metric, int):
            raise OnepIllegalArgumentException('metric invalid')
        self._metric = metric


    _doc = '\n    The metric in the next hop. If a route has multiple next hops,\n    the metric can help a router to pick the best next hop to use.\n    Larger values indicate higher preference.\n    \n    @type: C{int}\n    @raise OnepIllegalArgumentException: if metric not valid\n    '
    metric = property(_get_metric, _set_metric, None, _doc)

    def _get_route_tag(self):
        return self._route_tag



    def _set_route_tag(self, route_tag):
        if route_tag is None:
            self._route_tag = route_tag
        elif isinstance(route_tag, (int, long)) and -1 < route_tag and route_tag < 4294967296L:
            self._route_tag = c_int(route_tag).value
        else:
            raise OnepIllegalArgumentException('route_tag is invalid. It should be in unsigned 32-bit integer range.')


    _doc = '\n    The route tag in the next hop. The route tag can be used by\n    routing protocols on the router in conjunction with routing\n    policies to decide which routes to advertise to other routers.\n    \n    @type: C{int}\n    @raise OnepIllegalArgumentException: if route tag not valid\n    '
    route_tag = property(_get_route_tag, _set_route_tag, None, _doc)

    def __str__(self):
        """
        Gets the string representation of the object
        @return: The string representation of the object.
        """
        nh_str = 'L3UnicastNextHop['
        nh_str += 'Address:' + self.address + ','
        nh_str += 'Interface:'
        if self.network_interface is None:
            nh_str += 'None,'
        else:
            nh_str += self.network_interface.name + ','
        nh_str += 'ErrorCode:' + str(self.error_code) + ','
        nh_str += 'RouteTag:' + str(self.route_tag) + ','
        nh_str += 'Metric:' + str(self.metric) + ']'
        return nh_str



    def _to_idl(self):
        addr_idl = None
        if self._address != None:
            addr_idl = NetworkInterface._convert_to_networkaddressidl(self._address)
        if self._network_interface == None:
            network_interface_name = None
            network_interface_handle = 0
            network_interface_type = 0
        else:
            network_interface_name = self._network_interface.name
            network_interface_handle = self._network_interface.xos_handle
            network_interface_type = self._network_interface.interface_type
        if self._metric is not None:
            nh_metric = self._metric
        else:
            nh_metric = 0
        nh_idl = RouteNextHopIDL(network_interface_name, addr_idl, network_interface_handle, network_interface_type, 0, nh_metric, self._route_tag)
        self.log.info('Creating RouteNextHopIDL')
        scope_idl = None
        if self._scope != None and isinstance(self._scope, (L3UnicastScope,)):
            scope_idl = self._scope._to_idl()
        l3nh_idl = L3UcastRouteNextHopIDL(nh_idl, 0, scope_idl)
        self.log.info('Creating L3UcastRouteNextHopIDL')
        return l3nh_idl



    @staticmethod
    def _from_idl(nh_idl, ne):
        if nh_idl == None:
            return 
        addr = None
        if nh_idl.nextHop and nh_idl.nextHop.address != None:
            if isinstance(nh_idl, L3UcastRouteNextHopIDL):
                addr = NetworkInterface._convert_to_inetaddress(nh_idl.nextHop.address)
            elif isinstance(nh_idl, L3UcastRouteNextHopOutIDL):
                addr = nh_idl.nextHop.address.addr
        scp = L3UnicastScope._from_idl(nh_idl.scope)
        ni = None
        try:
            ni = NetworkInterface(ne, nh_idl.nextHop.name, nh_idl.nextHop.interfaceType, nh_idl.nextHop.xosHandle)
        except OnepIllegalArgumentException as e:
            L3UnicastNextHop.log.debug('failed to convert NetworkInterface ' + e)
        L3UnicastNextHop.log.debug('Creating L3UcastRouteNextHop from IDL')
        l3nh = L3UnicastNextHop(ni, addr, scp, nh_idl.nextHop.ec, nh_idl.nextHop.metric)
        if nh_idl.nextHop.route_tag is not None:
            l3nh._route_tag = nh_idl.nextHop.route_tag
        return l3nh




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:20:04 IST
