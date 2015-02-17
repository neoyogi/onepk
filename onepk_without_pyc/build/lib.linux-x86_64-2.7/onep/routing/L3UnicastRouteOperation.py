# 2015.02.05 17:20:04 IST
from onep.core.exception.OnepIllegalArgumentException import OnepIllegalArgumentException
from onep.routing.RouteOperation import *
from onep.RoutingIDL.ttypes import L3UcastRouteAppRouteTableOpIDL
import logging

class L3UnicastRouteOperation(RouteOperation):
    """
    This class represents the operation to be performed on a route.
    """

    _route = None

    def __init__(self, opType, route, noCheck = None):
        """ Constructor for L3UnicastRouteOperation
        @param opType: The operation type
        @type opType: L{Enum<onep.core.util.Enum>}
        
        @param route: The route for the operation
        @type route : L{L3UnicastRoute<onep.routing.L3UnicastRoute>}
        @raise OnepIllegalArgumentException: This exception is thrown if opType
        route or nextHopList is invalid
        """
        if noCheck == None:
            self.__init__1(opType, route)
        else:
            self.__init__0(opType, route, noCheck)
        self.log = logging.getLogger('onep.' + __name__)



    def __init__0(self, opType, route, noCheck):
        super(L3UnicastRouteOperation, self).__init__(opType)
        self._route = route



    def __init__1(self, opType, route):
        super(L3UnicastRouteOperation, self).__init__(opType)
        if opType == None:
            raise OnepIllegalArgumentException('opType', 'null')
        if not isinstance(opType, int) or opType < RouteOperation.RouteOperationType.ADD or opType > RouteOperation.RouteOperationType.REPLACE:
            raise OnepIllegalArgumentException('opType', 'invalid')
        if route is None:
            raise OnepIllegalArgumentException('route', 'null')
        if opType is RouteOperation.RouteOperationType.ADD or opType is RouteOperation.RouteOperationType.REPLACE:
            if not self._valid_next_hop_list(route):
                raise OnepIllegalArgumentException('nextHopList', 'invalid')
        self._route = route



    def _valid_next_hop_list(self, route):
        """
        Internal Use only
        """
        if route == None or route.next_hop_list == None:
            return False
        for hop in route.next_hop_list:
            if hop == None:
                return False

        return True



    def _get_route(self):
        return self._route


    _doc = 'The route for the operation.\n    @type: L{L3UnicastRoute<onep.routing.L3UnicastRoute>}\n    '
    route = property(_get_route, None, None, _doc)

    def _to_idl(self):
        """ Convert to L3UcastRouteAppRouteTableOpIDL. For internal use only. """
        self.log.info('calling L3UcastRouteAppRouteTableOpIDL')
        return L3UcastRouteAppRouteTableOpIDL(self._op_type, None if self._route == None else self._route._to_idl())




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:20:04 IST
