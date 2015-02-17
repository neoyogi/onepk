#!/usr/bin/env python

# Copyright (c) 2010-2013 by Cisco syss, Inc.
# 
# THIS SAMPLE CODE IS PROVIDED "AS IS" WITHOUT ANY EXPRESS OR IMPLIED WARRANTY
# BY CISCO SOLELY FOR THE PURPOSE of PROVIDING PROGRAMMING EXAMPLES.
# CISCO SHALL NOT BE HELD LIABLE FOR ANY USE OF THE SAMPLE CODE IN ANY
# APPLICATION.
# 
# Redistribution and use of the sample code, with or without
# modification, are permitted provided that the following conditions
# are met:
# Redistributions of source code must retain the above disclaimer.
# 
import logging
import time
from BaseTutorial import BaseTutorial
from onep.interfaces import NetworkPrefix
from onep.routing import ARTRouteStateListener
from onep.routing import AppRouteTable
from onep.routing import L3UnicastNextHop
from onep.routing import L3UnicastRIBFilter
from onep.routing import L3UnicastRoute
from onep.routing import L3UnicastRouteOperation
from onep.routing import L3UnicastRouteRange
from onep.routing import L3UnicastScope
from onep.routing import RIB
from onep.routing import RIBRouteStateEvent
from onep.routing import RIBRouteStateListener
from onep.routing import ReplayRouteEventListener
from onep.routing import RouteRange
from onep.routing import Routing
from onep.routing import UpdateRouteResponseListener

logger = logging.getLogger('onep:ARTTutorial')
logger.setLevel(logging.INFO)

class ARTTutorial(BaseTutorial):
    """
    This tutorial shows how to create Routing Service Set object, how to read ART routes, 
    update application routes, add listeners for route up and down events in the ART, 
    and add listeners for application routes.

    @author The onePK Team (onepk-feedback@cisco.com)
    """

    def get_app_route_table(self):
        """
        Gets the Application Route Table generated by this application.
        
        @return AppRouteTable for this application
        
        @throws OnepConnectionException 
        """
        
        #  START SNIPPET: getAppRouteTable
        #  Create a Routing object for the network element.
        routing = Routing.get_instance(tutorial.get_network_element())
        
        #  Get the instance of application route table.
        approutetable = routing.get_app_route_table()
        return approutetable
        #  END SNIPPET: getAppRouteTable

    def addRoutes(self, approutetable):
        """
        Adds custom application routes to the network element.
        
        @param approutetable: application route table to be updated
        
        @throws OnepConnectionException
        @throws OnepIllegalArgumentException
        @throws OnepRemoteProcedureException
        @throws UnknownHostException
        """
            
        #  START SNIPPET: addRoutes
        eth_interface = tutorial.get_an_interface()
        if eth_interface == None:
            logger.error("Could not find a suitable interface to add routes to.")
            return
        logger.info(eth_interface)
        
        route_scope = L3UnicastScope("", L3UnicastScope.AFIType.IPV4 , L3UnicastScope.SAFIType.UNICAST, "")
        
        #aL3UnicastNextHopList = HashSet()
        aL3UnicastNextHopList = list()
        aL3UnicastNextHop = L3UnicastNextHop(eth_interface, "10.1.1.24")
        aL3UnicastNextHopList.append(aL3UnicastNextHop)
        aL3UnicastNextHopList.append(L3UnicastNextHop(eth_interface, "10.1.1.25"))
        
        destNetworkPrefix = NetworkPrefix("160.10.0.0", 16)

        aRoute = L3UnicastRoute(destNetworkPrefix, aL3UnicastNextHopList)
        aRoute.admin_distance = 1
        #  Now update the app route table with this route.
        routeOperation = L3UnicastRouteOperation(0, aRoute)
        
        routeOperationList = list()
        routeOperationList.append(routeOperation)
        mylist = approutetable.update_routes(route_scope, routeOperationList)
        logger.info(mylist)
        #  END SNIPPET: addRoutes

    def remove_art_route_listener(self, approutetable, eventHandler):
        """
        Removes the Application Routing Table listener.
    
        @param approutetable
               ART associated with the listener.
        @param eventHandler
               associated with the ART to be removed.
        @throws OnepException
               If there is an error.
        """
        #  START SNIPPET: removeARTRouteListener
        #  Remove Application Route listener.
        approutetable.remove_route_state_listener(eventHandler)
        #  END SNIPPET: removeARTRouteListener

#  START SNIPPET: ExampleARTRouteListener
class ExampleARTRouteListener (ARTRouteStateListener):
    def handle_event(self,event,clientData):
        logger.info("\n\n\nEntering handle event for my ART Listener")
        scope_A = event.scope
        route_A = event.route
        try:
            logger.info(scope_A)
            state_A =  event.state
            logger.info("State is :")
            logger.info(AppRouteTable.RouteState.enumval(state_A))

            logger.info(route_A)
            nexthoplist = route_A.next_hop_list
            for next_hop in nexthoplist:
                try:
                    ni = next_hop.network_interface
                    na = next_hop.address
                except OnepRemoteProcedureException,e:
                    logger.info("N/A: " + e)
                except OnepConnectionException, e:
                    logger.info(str(e))
                except OnepIllegalArgumentException, e:
                    logger.info(e)
                else:
                    logger.info("Next hop ip address is " + na)
                    if ni is not None:
                        logger.info(ni.name)
        except (OnepIllegalArgumentException, OnepRemoteProcedureException, OnepConnectionException) ,e:    
            logger.info(e)
            logger.info("Exiting gracefully")
#  END SNIPPET: ExampleARTRouteListener


if __name__ == '__main__':
    """
    Invokes the tutorial via the command line. This main method attempts to use arguments from the command line.
    """
    import sys
    tutorial = ARTTutorial(sys.argv)
    logger.info("Reading arguments...")
    if not tutorial.parse_command_line():
        logger.error("Error in parsing arguments")
        sys.exit(1)
    try:
        logger.info("Connecting to Network Element...")
        if not tutorial.connect("ARTTutorial"):
            logger.error("Error in connecting to network element")
            sys.exit(1)
        logger.info("Done")
        
        #  Create a Application Routing Table.
        logger.info("Getting a Routing Instance...")
        routing = Routing.get_instance(tutorial.get_network_element())
        
        logger.info("Getting a Application Route Table...")
        approutetable = routing.app_route_table
        
        #  Add a ART listener to listen for changes in the ART.
        logger.info("Adding ART Listener...")
        #  START SNIPPET: addARTRouteListener
        aL3UnicastScope = L3UnicastScope("", L3UnicastScope.AFIType.IPV4 , 
                                            L3UnicastScope.SAFIType.UNICAST, 
                                            "")
        #  Add a listener to receive route state change events. When events arrive, listener.handleEvent() will be invoked.
        artRouteListener = ExampleARTRouteListener()
        aARTEventHandler = approutetable.add_route_state_listener(
                    artRouteListener, 
                    aL3UnicastScope, 
                    0,
                    None)
        logger.info("aARTEventHandler : ")
        logger.info(str(aARTEventHandler))
        #  END SNIPPET: addARTRouteListener

        #  Add custom application routes.
        logger.info("Adding Routes...")
        tutorial.addRoutes(approutetable)
        
        #  Removes the ART Listener.
        logger.info("Removing ART route Listener...")
        tutorial.remove_art_route_listener(approutetable, aARTEventHandler)
        
    except Exception, e:
        logger.error(str(e))
    tutorial.disconnect()
    sys.exit(0)