# 2015.02.05 17:20:02 IST
from onep.thrift.Thrift import TException
from onep.core.exception.OnepConnectionException import OnepConnectionException
from onep.core.exception.OnepException import OnepException
from onep.core.exception.OnepRemoteProcedureException import OnepRemoteProcedureException
from Shared.ttypes import ExceptionIDL
from onep.routing.L3UnicastRoute import L3UnicastRoute
from onep.routing.L3UnicastRouteOperation import L3UnicastRouteOperation
from onep.core.exception.OnepIllegalArgumentException import OnepIllegalArgumentException
from onep.routing.L3UnicastScope import L3UnicastScope
from onep.core.util.Enum import enum
import logging
from onep.core.util.HostIpCheck import HostIpCheck as ipchk
try:
    from onep.vty.VtyProxy import VtyProxy
except ImportError:
    pass
from onep.routing.RouteOperation import RouteOperation
from onep.core.util.HostIpCheck import HostIpCheck

class AppRouteTable(object):
    """
    This class represents an application route table. It provides application
    the ability to add, remove and replace route from the application route 
    table. The following services are provided:
    
    Add, replace and remove route from the application route table.Get 
    notification when the added application route is promoted or demoted 
    in the RIB.
    
    Depending on platform, the application route table could do extra check 
    before adding the route to the RIB. For example, route may be added to the 
    RIB when the next hop is resolvable.
    
    Once the application accept and return success for the operation, the 
    application is responsible to keep the state of the routes consistent 
    across HA switchover.
    
    The route added will not be visible in the configuration. But the added 
    route would be visible in routing related show commands.
    The show output will be able to tell which application added the route.
    The added route are redistributable.
    
    If a listener is registered, the application route table will provide 
    notification when an application route gets promoted or demoted in the RIB.
    
    Currently, only add/delete/update route operations are supported.
    
    @undocumented: __init__
    """

    RouteState = enum('PROMOTE', 'DEMOTE')
    TRIGER_INITIAL_WALK = 1
    _parent_rss = None
    _async_queue_size = 100

    def __init__(self, parentRSS):
        """
        Constructor. For internal use only
        """
        self._parent_rss = parentRSS
        self.log = logging.getLogger(__name__)



    def update_routes(self, scope, opList):
        """
                Update a route. It is a synchronous API.
                It is used to add, delete and replace single route in the 
                Application Route Table. The type of operation is indicated 
                by RouteOperationType parameter.
        
                For route addition: If the route do not exist, create route 
                with the provided next hops. If the route already exist in 
                the table, any new next hop specified is added to the route. 
                Duplicated next hop is ignored.
        
                For route replace: If the route do not exist, it act like 
                route addition operation. If the route already exist in the table, 
                the all the old next hops are removed and new next hops specified 
                are added to the route.
        
                For route deletion: Next hop specified will be removed. 
                If no next hop is specified, then all next hops are removed. 
                The route will be removed when no more next hops exist.
         
                Return error if the scope and route is not consistent.
        
                This method will make remote procedure call and 
                response time may be long.  
        
                @param scope: Indicate which table in the Application Route Table
                to send the route operation too.
                @type scope: L{L3UnicastScope<onep.routing.L3UnicastScope>}
                
                @param opList: The list of route operation. If API succeeds,
                per route per next hop status are returned and could be accessed 
                using Route.error_code and NextHop.eror_code
                @type opList: C{list} of 
                L{L3UnicastRouteOperation<onep.routing.L3UnicastRouteOperation>}
                
                @return: A list of the route operation. This list is a copy of the 
                routes in the input parameter, with error code for each route added.
                @rtype: C{list} of 
                L{L3UnicastRouteOperation<onep.routing.L3UnicastRouteOperation>}
                
                @raise OnepIllegalArgumentException: This exception is thrown 
                if the scope and route are not consistent
                
                @raise OnepConnectionException: The exception is thrown when connection
                to the network element has failed.
                
                @raise OnepRemoteProcedureException: The exception is thrown when an 
                error has occurred in the remote procedure call made to a network 
                element
                """
        if opList == None or len(opList) == 0:
            return 
        scopeIdl = None
        if isinstance(scope, L3UnicastScope):
            scopeIdl = scope._to_idl()
        if scopeIdl == None:
            raise OnepIllegalArgumentException('scope', 'invalid')
        opListIdl = list()
        for rop in opList:
            if rop != None and isinstance(rop, (L3UnicastRouteOperation,)):
                opListIdl.append(rop._to_idl())

        try:
            opIdlList = self._parent_rss._routing_client.Routing_L3UcastARTUpdateRoutesIDL(self._parent_rss.network_element.session_handle._id, scopeIdl, opListIdl)
            self.log.info('Returning from Routing_L3UcastARTUpdateRoutesIDL')
            opListOut = list()
            for opIdl in opIdlList:
                if opIdl != None:
                    opListOut.append(L3UnicastRouteOperation(opIdl.opType, L3UnicastRoute._from_idl(opIdl.route, self._parent_rss.network_element), True))

            return opListOut
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e)



    def async_update_routes(self, scope, op_list, listener, client_data):
        """
        Asynchronously update a route. It is an asynchronous API that
        will return immediately and the application provided listener
        will be invoked when the all the route update requests are
        processed by the network element.
        
        It is used to add, delete and replace single route in the
        Application Route Table. The type of operation is indicated
        by RouteOperationType parameter.
        
        For route addition: If the route do not exist, create route
        with the provided next hops. If the route already exist in
        the table, any new next hop specified is added to the route
        Duplicated next hop is ignored.
        
        For route replace: If the route do not exist, it act like 
        route addition operation. If the route already exist in the table,
        the all the old next hops are removed and new next hops specified
        are added to the route.
        
        If no next hop is specified, then all next hops are removed.
        The route will be removed when no more next hops exist.
        
        Return error if the scope and route is not consistent.
        
        This method will make remote procedure call and
        response time may be long.
        
        @param scope: Indicate which table in the Application Route Table
        to send the route operation too.
        @type scope: L{Scope<onep.routing.Scope>}
        
        @param op_list: The list of route operation. If API succeeds,
        per route per next hop status are returned and could be accessed 
        using Route.error_code and NextHop.error_code
        @type op_list: C{list} of L{L3UnicastRouteOperation<onep.routing.L3UnicastRouteOperation>}
        
        @param listener: The UpdateRouteResponseListener object that handles the events.
        @type listener: L{UpdateRouteResponseListener<onep.routing.UpdateRouteResponse>}
        
        @param client_data: The client data associated with the listener. This 
        client data will be part of input parameters when the
        handleEvent method in the listener is invoked.
        
        @return: An identifier for this asynchronous update request.
        Could be used to monitor the status or cancel the request. 
        @rtype: C{int}
        
        @raise OnepIllegalArgumentException: This exception is thrown 
        if the scope and route are not consistent
        
        @raise OnepConnectionException: The exception is thrown when connection
        to the network element has failed.
        
        @raise OnepRemoteProcedureException: The exception is thrown when an 
        error has occurred in the remote procedure call made to a network 
        element
        """
        if op_list == None or len(op_list) == 0:
            raise OnepIllegalArgumentException('opList', 'empty')
        scope_idl = None
        if isinstance(scope, L3UnicastScope):
            scope_idl = scope._to_idl()
        if scope_idl == None:
            raise OnepIllegalArgumentException('scope', 'Invalid')
        op_list_idl = list()
        for rop in op_list:
            if rop != None and isinstance(rop, L3UnicastRouteOperation):
                op_list_idl.append(rop._to_idl())

        try:
            event_prop = self._parent_rss._routing_client.Routing_L3UcastARTUpdateRoutesAsyncIDL(self._parent_rss.network_element.session_handle._id, scope_idl, op_list_idl)
            self.log.debug('Done calling Routing_L3UcastARTUpdateRoutesAsyncIDL')
            if event_prop != None:
                self._parent_rss.network_element.event_manager.add_listener(event_prop.eventHandle, listener, client_data)
                self.log.debug('Registered UpdateResponseListener with handle' + str(event_prop.eventHandle))
                self._parent_rss.network_element.event_manager.register_dedicated_queue(event_prop.eventHandle, self._async_queue_size)
                return event_prop.eventHandle
            raise OnepException('Internal error while registering the Listener')
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e)



    def add_route_state_listener(self, routeStateListener, scope, flags, clientData):
        """
                Adds a route state listener to the ART object.
                
                @param routeStateListener: The RouteStateListener object that 
                handles the events. 
                @type routeStateListener: L{ARTRouteStateListener<onep.routing.ARTRouteStateListener>}
                
                @param scope: Indicate which table in the Application Route Table get
                notification from.
                @type scope: L{L3UnicastScope<onep.routing.L3UnicastScope>}
               
                @param flags: Additional flags to be passed to listener. 
                This argument is reserved for future use and ignored at present.
                @type flags: C{int}
        
                @param clientData: The client data associated with the listener. This
                client data will be part of input parameters when the
                handleEvent method in the listener is invoked.
                
                @return: EventHandle, a numeric ID associated with this event
                registration. The eventHandle is used to unregister
                the listener using the remove_route_state_listener method
                If registration fails, -1 is returned.        
                @rtype: C{int}
                
                @raise OnepIllegalArgumentException: The exception is thrown when the 
                listener or other parameters is not valid.
                
                @raise OnepConnectionException: The exception is thrown when 
                connection to a network element has failed.
                
                @raise OnepRemoteProcedureException: The exception is thrown when 
                an error has occurred in the remote procedure call made to a
                network element
                """
        if routeStateListener == None:
            raise OnepIllegalArgumentException('routeStateListener', 'null')
        scopeIdl = None
        if isinstance(scope, (L3UnicastScope,)):
            scopeIdl = scope._to_idl()
        if scopeIdl == None:
            raise OnepIllegalArgumentException('scope', 'invalid')
        try:
            eventProp = self._parent_rss._routing_client.L3UcastARTEvent_registerIDL(self._parent_rss.network_element.session_handle._id, scopeIdl)
            self.log.info('Returning from L3UcastARTEvent_registerIDL ')
            if eventProp != None:
                self._parent_rss.network_element.event_manager.add_listener(eventProp.eventHandle, routeStateListener, clientData)
                self.log.debug('Registered ARTRouteStateListener listener, eventHandle=' + str(eventProp.eventHandle))
                return eventProp.eventHandle
            raise OnepException('Internal error while registering the Listener')
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e)



    def remove_route_state_listener(self, eventHandle):
        """
        Removes the RouteStateListener listener object. This method will 
        remove the listener associated with the specified eventHandle and 
        also remove the corresponding registered event on the route table.
        
        @param eventHandle: Registered event identifier.  
        @type eventHandle: C{int}
        
        @raise OnepIllegalArgumentException: The exception is thrown when 
        eventHandle is not valid or is unregistered already.
        
        @raise OnepRemoteProcedureException: The exception is thrown when 
        an error has occurred in the remote procedure call made to a 
        network element
        
        @raise OnepConnectionException: The exception is thrown when connection 
        to a network element has failed.
        """
        self._parent_rss.network_element.event_manager.remove_listener(eventHandle)



    def add_replay_route_event_listener(self, listener, scope, client_data):
        """
        Adds a replay route event listener to the RIB object.
        
        @param listener: The ReplayRouteEventListener object that 
        handles the events. 
        @type listener: L{ReplayRouteEventListener<onep.routing.ReplayRouteEventListener>}
        
        @param scope: Indicate which table in the Application Route Table get
        notification from.
        @type scope: L{L3UnicastScope<onep.routing.L3UnicastScope>}
        
        @param client_data: The client data associated with the listener. This
        client data will be part of input parameters when the
        handleEvent method in the listener is invoked.
        
        @return: EventHandle, a numeric ID associated with this event
        registration. The eventHandle is used to unregister
        the listener using the remove_route_state_listener method
        If registration fails, -1 is returned.        
        @rtype: C{int}
        
        @raise OnepIllegalArgumentException: The exception is thrown when the 
        listener or other parameters is not valid.
        
        @raise OnepConnectionException: The exception is thrown when 
        connection to a network element has failed.
        
        @raise OnepRemoteProcedureException: The exception is thrown when 
        an error has occurred in the remote procedure call made to a
        network element
        """
        if listener == None:
            raise OnepIllegalArgumentException('ReplayRouteEventListener', 'null')
        scopeIdl = None
        if isinstance(scope, (L3UnicastScope,)):
            scopeIdl = scope._to_idl()
        if scopeIdl == None:
            raise OnepIllegalArgumentException('scope', 'invalid')
        try:
            eventProp = self._parent_rss._routing_client.RoutingReplayRouteEvent_registerIDL(self._parent_rss.network_element.session_handle._id, scopeIdl)
            self.log.info('Returning from RoutingReplayRouteEvent_registerIDL ')
            if eventProp != None:
                self._parent_rss.network_element.event_manager.add_listener(eventProp.eventHandle, listener, client_data)
                self.log.debug('Registered ReplayRouteEventListener listener, eventHandle=' + str(eventProp.eventHandle))
                return eventProp.eventHandle
            raise OnepException('Internal error while registering the Listener')
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e)



    def remove_replay_route_event_listener(self, eventHandle):
        """
        Removes the ReplayRouteEventListener listener object. This method will 
        remove the listener associated with the specified eventHandle and 
        also remove the corresponding registered event on the route table.
        
        @param eventHandle: Registered event identifier.  
        @type eventHandle: C{int}
        
        @raise OnepIllegalArgumentException: The exception is thrown when 
        eventHandle is not valid or is unregistered already.
        
        @raise OnepRemoteProcedureException: The exception is thrown when 
        an error has occurred in the remote procedure call made to a 
        network element
        
        @raise OnepConnectionException: The exception is thrown when connection 
        to a network element has failed.
        """
        self._parent_rss.network_element.event_manager.remove_listener(eventHandle)




class StaticRouteTable(AppRouteTable):
    """
        This class represents the static route table. It provides application
        the ability to add and remove static routes.
    
        """


    def __init__(self, parentRSS):
        super(StaticRouteTable, self).__init__(parentRSS)
        self.vty = VtyProxy(parentRSS._network_element)



    def update_routes(self, scope, opList):
        """     
                Add or remove static routes
        
                @param scope: Indicate which table in the Static Route Table
                to send the route operation too.
                @type scope: L{L3UnicastScope<onep.routing.L3UnicastScope>}
                
                @param opList: The list of route operation. If API succeeds,
                per route per next hop status are returned and could be accessed 
                using Route.error_code and NextHop.eror_code
                @type opList: C{list} of 
                L{L3UnicastRouteOperation<onep.routing.L3UnicastRouteOperation>}
                
                @return: A dictionary of the route operation which contains a copy of the  
                routes in the input parameter, with 'SUCCESS', 'FAIL', or 'NOT_SUPPORTED'
                @rtype: dictionary of 
                L{L3UnicastRouteOperation<onep.routing.L3UnicastRouteOperation> : 'SUCCESS'}
                
                @raise OnepIllegalArgumentException: This exception is thrown  
                if the scope and route are not consistent
                
                @raise OnepConnectionException: The exception is thrown when connection
                to the network element has failed. 
                
                @raise OnepRemoteProcedureException: The exception is thrown when an 
                error has occurred in the remote procedure call made to a network 
                element 
        
                """
        if opList == None or len(opList) == 0:
            return 
        oplistout = {}
        for rop in opList:
            if rop != None:
                vrf = scope._vrf
                address = rop.route.prefix.address
                mask = ipchk.len2mask(rop.route.prefix.prefix_length)
                if rop.route.next_hop_list:
                    next_hop = rop.route.next_hop_list[0].address
                    interface = rop.route.next_hop_list[0].network_interface
                    metric = rop.route.next_hop_list[0].metric
                else:
                    next_hop = interface = metric = None
                op = rop.op_type
                if vrf:
                    cli = 'ip route vrf %s %s %s ' % (vrf, address, mask)
                else:
                    cli = 'ip route %s %s ' % (address, mask)
                if interface:
                    cli = cli + interface.name + ' '
                if next_hop:
                    cli = cli + ' ' + next_hop + ' '
                if metric:
                    cli = cli + str(metric)
                if rop.op_type == RouteOperation.RouteOperationType.ADD:
                    try:
                        ret = self.vty.config(cli)
                        if ret.find('Inconsistent address and mask') > 0:
                            oplistout[rop] = 'FAIL'
                        else:
                            oplistout[rop] = 'SUCCESS'
                    except:
                        oplistout[rop] = 'FAIL'
                if rop.op_type == RouteOperation.RouteOperationType.REMOVE:
                    try:
                        self.vty.no_config(cli)
                        oplistout[rop] = 'SUCCESS'
                    except:
                        oplistout[rop] = 'FAIL'
                if rop.op_type == RouteOperation.RouteOperationType.REPLACE:
                    oplistout[rop] = 'NOT_SUPPORTED'

        return oplistout



    def get_static_route_list(self):
        """
                Return a dictionary of manually configured static routes
        
                Keys
                ----
                destination -- string - destination IP address
                mask        -- int - prefix length
                metric      -- int - administrative distance
                next_hop    -- string - next hop IP address
                interface   -- string - outgoing interface
                router      -- string - next hop router
        
                """
        routes = self.vty.show('run | inc ip route').splitlines()
        retlist = []
        for item in routes:
            items = item.split()
            rts = {}
            if items[2] == 'vrf':
                rts['vrf'] = items[3]
                items = items[:2] + items[4:]
            rts['destination'] = items[2]
            rts['mask'] = HostIpCheck.mask2len(items[3])
            if HostIpCheck(items[4]).is_ipaddress():
                rts['next_hop'] = items[4]
                rts['interface'] = None
            else:
                rts['next_hop'] = None
                rts['interface'] = items[4]
            rts['metric'] = None
            rts['router'] = None
            if len(items) > 5:
                if HostIpCheck(items[5]).is_ipaddress():
                    rts['router'] = items[5]
                    if len(items) > 6:
                        rts['metric'] = int(items[6])
                else:
                    rts['metric'] = int(items[5])
            retlist.append(rts)

        return retlist




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:20:03 IST
