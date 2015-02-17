# 2015.02.05 17:20:03 IST
from onep.core.exception.OnepConnectionException import OnepConnectionException
from onep.core.exception.OnepIllegalArgumentException import OnepIllegalArgumentException
from onep.RoutingIDL import RoutingIDL
from onep.routing.RIB import RIB
from onep.routing.AppRouteTable import AppRouteTable
from onep.routing.AppRouteTable import StaticRouteTable
from onep.core.util.Enum import enum
from Shared.ttypes import ExceptionIDL
from onep.thrift.Thrift import TException
from onep.core.exception.OnepException import OnepException
from onep.core.exception.OnepRemoteProcedureException import OnepRemoteProcedureException
import logging

class Routing(object):
    """ 
        Routing class represents the entry point of Routing Service.To access the 
        Routing Service API, the application instantiates a Routing object that's 
        associated with a NetworkElement. 
    
        Warning: This Sample Code Has Not Been Verified
        Example:
    
        def example() :
       
                # Get the network element and connect to it.
               ne = element.NetworkElement.NetworkElement("10.1.1.4","dolph")
               handle = ne.connect("cisco", "cisco")
               
               # Get a Routing instance that's associated with the network element. 
               routing = Routing.get_instance(ne)
               
               # Get RIB information and print the list of layer 3 unicast routes.
        
              rib = routing.rib
              scope = L3UnicastScope("", AFIType.IPV4, SAFIType.UNICAST, "")
              prefix = None
              filter = L3UnicastRIBFilter()
              range = L3UnicastRouteRange(
                              prefix, 
                              RouteRange.RangeType.EQUAL_OR_LARGER,
                              10)
              routeList = rib.get_route_list(scope, filter, range)
              for route in routeList :
                   if (isinstance (route,L3UnicastRoute) :
                       print route              
    
               # Add a listener to receive route state change events.
               # When events arrive, listener.handleEvent() will be invoked.
               listener = MyRouteListener()    
               eventHandle = rib.add_route_state_listener(
                             listener, 
                              scope, 
                              filter, 
                              RIB.TRIGER_INITIAL_WALK, 
                              None)
    
              # Get the instance of AppRouteTable in Routing object.
              art = routing.get_app_route_table()
              
              
              # Create a new route and change its administrative distance 
              # to make it more trusted. 
              scope = L3UnicastScope("", AFIType.IPV4, SAFIType.UNICAST, "")
              destNetwork = NetworkPrefix("192.168.200.0", 24)
              
              # Wrong address for the interface, see what happen.
               nextHop = L3UnicastNextHop(
                              ne.get_interface_by_name("Ethernet1/0"),
                              "192.168.99.77",
                              scope)
              nextHopList = set()
              nextHopList.add(nextHop)
              aRoute = L3UnicastRoute(destNetwork, nextHopList)
              aRoute.admin_distance = 1
              
              # Now update the app route table with this route.
              op = L3UnicastRouteOperation(RouteOperationType.REPLACE, aRoute);
              opList = list()
              opList.append(op);
              resultList = art.update_routes(scope, opList);  
    
           # Implement a RIBRouteStateListener.
           class MyRouteListener (RIBRouteStateListener) : 
                def handleEvent(event, clientData) :
                   print "Scope: " + event.scope
                   print "Route: " + event.route  
            Warning: This Sample Code Has Not Been Verified
        """

    RoutingServiceType = enum('RIB', 'ART', 'ALL')
    _network_element = None
    _app_route_table = None
    static_route_table = None
    _routing_instance_map = dict()
    _routing_client = None
    _rib = None

    def __init__(self, networkElement):
        """ Constructor. For internal use only.
        @param networkElement: The target network element which routing service
        is associate with..
        @type networkElement: L{NetworkElement<onep.element.NetworkElement>}
        
        @raise OnepConnectionException: The exception is thrown when 
        the network element is not connectted.
        """
        super(Routing, self).__init__()
        if not networkElement.is_connected():
            self._routing_client = None
            raise OnepConnectionException()
        self._network_element = networkElement
        self._rib = RIB(self)
        self._app_route_table = AppRouteTable(self)
        self.static_route_table = StaticRouteTable(self)
        if self._routing_client == None:
            self._routing_client = RoutingIDL.Client(networkElement.api_protocol)
            if self._routing_client == None:
                raise OnepConnectionException('Unable to create Routing client instance')
        self.log = logging.getLogger('onep.' + __name__)



    @staticmethod
    def get_instance(networkElement):
        """
        Create a Routing instance based on the provided NetworkElement.
        This static method follows factory pattern to guarantee only one instance
        of Routing will be created for each NetworkElement.
        
        @param networkElement: The network element which the Routing instance
        is associate with..
        @type networkElement: L{NetworkElement<onep.element.NetworkElement>}
        
        @raise OnepConnectionException: The exception is thrown when the 
        network element is not connected.
        """
        if networkElement == None or not networkElement.is_connected():
            raise OnepConnectionException()
        if not networkElement.routing:
            networkElement.routing = Routing(networkElement)
        return networkElement.routing



    def _get_network_element(self):
        return self._network_element


    _doc = '\n    Gets the NetworkElement object where this Routing instance belongs to\n    @type : L{NetworkElement<onep.element.NetworkElement}\n    '
    network_element = property(_get_network_element, None, None, _doc)

    def _get_rib(self):
        return self._rib


    _doc = '\n    Gets the RIB object in this Routing service\n    @type: L{RIB<onep.routing.RIB>}\n    '
    rib = property(_get_rib, None, None, _doc)

    def _get_app_route_table(self):
        return self._app_route_table


    _doc = '\n    Gets the AppRouteTable object in this Routing service.\n    @type: L{AppRouteTable<onep.routing.AppRouteTable>}\n    '
    app_route_table = property(_get_app_route_table, None, None, _doc)

    def add_service_status_listener(self, listener, client_data):
        """
                Adds a routing service status listener.
                
                @param listener: The RoutingServiceStatusListener object that handles the events.
                @type listener: L{RoutingServiceStatusListener<onep.routing.RoutingServiceStatusListener>}
                
                @param client_data: The client data associated with the listener. This 
                client data will be part of input parameters when the handleEvent method 
                in the listener is invoked.
                
                @return event_handle: a numeric ID associated with this event registration. 
                The eventHandle is used to unregister the listener using the remove listener method.
                If registration fails, -1 is returned.
                @rtype: C{int}
                
                @raise OnepIllegalArgumentException: The exception is thrown when scope, 
                filter or range is invalid
                
                @raise OnepConnectionException: The exception is thrown when connection to the 
                network element has failed.
        
                @raise OnepRemoteProcedureException: The exception is thrown when an error has
                occurred in the remote procedure call made to a network element
                
                @raise OnepException: This occurs when an internal exception occurs
                """
        if listener == None:
            raise OnepIllegalArgumentException('listener', 'null')
        try:
            event_prop = self._routing_client.RoutingServiceStatusEvent_registerIDL(self._network_element.session_handle._id)
            if event_prop != None:
                self._network_element.event_manager.add_listener(event_prop.eventHandle, listener, client_data)
                self.log.debug('Registered Service status listener with event handle : ' + str(event_prop.eventHandle))
                return event_prop.eventHandle
            raise OnepException('Internal error while registering the Listener')
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e)



    def remove_service_status_listener(self, event_handle):
        """
        Removes the RoutingServiceStatusListener listener object. This method will 
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
        self._parent_rss.network_element.event_manager.remove_listener(event_handle)




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:20:03 IST
