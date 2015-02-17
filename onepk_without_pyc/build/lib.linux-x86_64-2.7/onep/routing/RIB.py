# 2015.02.05 17:20:03 IST
from onep.core.util.Enum import enum
from onep.routing.L3UnicastScope import L3UnicastScope
from onep.routing.L3UnicastRouteRange import L3UnicastRouteRange
from onep.routing.L3UnicastRIBFilter import L3UnicastRIBFilter
from onep.routing.L3UnicastRoute import L3UnicastRoute
from Shared.ttypes import ExceptionIDL
from onep.core.util.OnepConstants import OnepConstants
from onep.core.exception.OnepIllegalArgumentException import OnepIllegalArgumentException
from onep.core.exception.OnepRemoteProcedureException import OnepRemoteProcedureException
from onep.core.exception.OnepConnectionException import OnepConnectionException
from onep.core.exception.OnepException import OnepException
from onep.routing.RIBRouteStateListener import RIBRouteStateListener
from onep.thrift.Thrift import TException
from onep.interfaces import NetworkPrefix
import logging

class RIB(object):
    """RIB class represents service provided
    by RIB (Routing Information Base).
    """

    RouteState = enum('UP', 'DOWN', 'UNKNOWN')
    TRIGER_INITIAL_WALK = 1
    _parent_rss = None

    def __init__(self, parent_rss):
        """
        Constructor for RIB
        """
        self._parent_rss = parent_rss
        self.log = logging.getLogger('onep.' + __name__)



    def get_route_list(self, scope, filter, range):
        """
        Gets the RIB routes from the network element for the specified scope,
        filter and range. This method will make remote procedure call and 
        response time may be long.
        
        Only routes which satisfy the filter and range are retrieved. This 
        method may not return all the number of routes as specified in the 
        range count per invocation. The platform controls the maximum number 
        of routes returned per invocation. To retrieve all the routes matching 
        the criteria, the application may have to call the method multiple 
        times, adjusting the start prefix and the type in the range argument 
        accordingly, until a list of size 0 is returned.
        
        Also, to prevent connection timeout when getting a long list of routes, 
        application should increase the timeout by calling the following method 
        before connecting to a network element
        #NetworkApplicaiton.set_default_socket_timeout(300)
        
        @param scope: Indicates which table in the RIB to retrieve route from.
        @type scope: L{L3unicastScope<onep.routing.L3unicastScope>}
        
        @param filter: Specifies characteristic of a route must match for it to
        be retrieved. Use default filter (instantiated with default constructor) 
        if no filtering is needed.the same as if a filter with all default values 
        passed in.
        @type filter: L{L3UnicastRIBFilter<onep.routing.L3UnicastRIBFilter>}
        
        @param range: Specifies range of route to be retrieved. Use default 
        range (instantiated with default constructor) if no range matching
        is needed.
        @type range: L{L3UnicastRouteRange<onep.routing.L3UnicastRouteRange>}
        """
        scope_idl = None
        if isinstance(scope, L3UnicastScope):
            scope_idl = scope._to_idl()
        if scope_idl == None:
            raise OnepIllegalArgumentException('scope', 'invalid')
        filter_idl = None
        if isinstance(filter, L3UnicastRIBFilter):
            filter_idl = filter._to_idl()
        if filter_idl == None:
            raise OnepIllegalArgumentException('filter', 'invalid')
        range_idl = None
        if isinstance(range, L3UnicastRouteRange):
            range_idl = range._to_idl()
        if range_idl == None:
            raise OnepIllegalArgumentException('range', 'invalid')
        try:
            route_idl_list = self._parent_rss._routing_client.Routing_L3UcastGetRibRouteListIDL(self._parent_rss.network_element.session_handle._id, scope_idl, filter_idl, range_idl)
            if route_idl_list == None or len(route_idl_list) == 0:
                print 'route list is null'
                return list()
            else:
                route_list = list()
                for route_idl in route_idl_list:
                    if route_idl != None:
                        route_list.append(L3UnicastRoute._from_idl(route_idl, self._parent_rss.network_element))

                return route_list
        except ExceptionIDL as e:
            if e.code == OnepConstants.ERR_NO_DATA:
                return list()
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e)



    def add_route_state_listener(self, route_state_listener, scope, filter, flag, client_data):
        """
        Adds a route state listener to the RIB object.
        
        @param route_state_listener: 
        The RouteStateListener object that handles the events.
        @type route_state_listener: 
        L{RIBRouteStateListener<onep.routing.RIBRouteStateListener>}
        
        @param scope:
        Indicates which table in the RIB to retrieve route from.
        @type scope: L{L3UnicastScope<onep.routing.L3UnicastScope>}
        
        @param filter:
        Specifies characteristic of a route must match for it to
        be retrieved
        @type filter: L{L3UnicastRIBFilter<onep.routing.L3UnicastRIBFilter>}
        
        @param client_data:
        The client data associated with the listener. This
        client data will be part of input parameters when the
        handleEvent method in the listener is invoked.
        @type client_data: C{str}
        
        @param flag:
        Additional request when the listener is installed.
        If TRIGER_INITIAL_WALK is set, triggers an initial walk of the
        RIB and reports an UP event to the application for each route that
        matches rib_filter. The TRIGER_INITIAL_WALK flag is supported only
        on network elements that run IOS Classic or IOS-XE.
        On IOS-XR and NXOS, TRIGER_INITIAL_WALK is ignored;
        an initial walk is always performed.
        @type flag : C{int}
        
        @return: 
        EventHandle, a numeric ID associated with this event
        registration. The eventHandle is used to unregister
        the listener using the removeRouteStateListener method.
        If registration fails, -1 is returned.
        @rtype: C{int}
        
        @raise OnepIllegalArgumentException:
        The exception is thrown when scope, filter or range  is invalid
        
        @raise OnepConnectionException:
        The exception is thrown when connection 
        to the network element has failed.
        
        @raise OnepRemoteProcedureException:
        The exception is thrown when an error has occurred in the 
        remote procedure call made to a network element
        
        @raise OnepException:
        The exception is thrown when an internal error occurs       
        """
        if route_state_listener == None:
            raise OnepIllegalArgumentException('routeStateListener', 'null')
        if not isinstance(route_state_listener, RIBRouteStateListener):
            OnepIllegalArgumentException('routeStateListener', 'invalid')
        scope_idl = None
        if isinstance(scope, (L3UnicastScope,)):
            scope_idl = scope._to_idl()
        if scope_idl == None:
            raise OnepIllegalArgumentException('scope', 'invalid')
        filter_idl = None
        if isinstance(filter, (L3UnicastRIBFilter,)):
            if scope.afi == L3UnicastScope.AFIType.IPV6 and filter.subnet.address == '0.0.0.0' and filter.subnet.prefix_length == 0:
                filter.subnet = NetworkPrefix('0::0', 0)
            filter_idl = filter._to_idl()
        if filter_idl == None:
            raise OnepIllegalArgumentException('filter', 'invalid')
        try:
            event_prop = self._parent_rss._routing_client.L3UcastRibRouteEvent_registerIDL(self._parent_rss.network_element.session_handle._id, scope_idl, filter_idl, flag)
            if event_prop != None:
                self._parent_rss.network_element.event_manager.add_listener(event_prop.eventHandle, route_state_listener, client_data)
                self.log.debug('Registered RIBRoute listener with event handle : ' + str(event_prop.eventHandle))
                return event_prop.eventHandle
            raise OnepException('Internal error while registering the Listener')
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e)



    def remove_route_state_listener(self, eventHandle):
        """Removes the RouteStateListener listener object. This method will
        remove the listener associated with the specified eventHandle and also 
        remove the corresponding registered event on the RIB.
        
        @param eventHandle: Registered event identifier
        @type eventHandle: C{int}
        
        @raise OnepIllegalArgumentException: The exception is thrown when 
        eventHandle is not valid or is unregistered already.
        
        @raise OnepRemoteProcedureException: The exception is thrown when 
        an error has occurred in the remote procedure call made to a network 
        element
        
        @raise OnepConnectionException: The exception is thrown when connection 
        to a network element has failed.
        """
        self._parent_rss.network_element.event_manager.remove_listener(eventHandle)




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:20:03 IST
