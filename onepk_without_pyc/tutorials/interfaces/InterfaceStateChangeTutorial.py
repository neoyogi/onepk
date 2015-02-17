#!/usr/bin/env python

# 
# * Copyright (c) 2010-2013 by Cisco Systems, Inc.
# *
# * THIS SAMPLE CODE IS PROVIDED "AS IS" WITHOUT ANY EXPRESS OR IMPLIED WARRANTY
# * BY CISCO SOLELY FOR THE PURPOSE of PROVIDING PROGRAMMING EXAMPLES.
# * CISCO SHALL NOT BE HELD LIABLE FOR ANY USE OF THE SAMPLE CODE IN ANY
# * APPLICATION.
# *
# * Redistribution and use of the sample code, with or without
# * modification, are permitted provided that the following conditions
# * are met:
# * Redistributions of source code must retain the above disclaimer.
# 
# package: tutorials.interfaces

""" 
 The goal of this tutorial is to show how to register for a state change event on the Network element.
 When the monitored state change happens on the Network element an event is triggered and the state
 change event handler is called. In this example the simply prints the state change details.

 @author The onePK Team (onepk-feedback@cisco.com)
"""

import logging
from BaseTutorial import BaseTutorial
import sys
import time
from onep.core.util import OnepConstants
import onep.interfaces.InterfaceFilter
from onep.interfaces import NetworkInterface
from onep.element import NetworkElement
from onep.interfaces import InterfaceStatus
from onep.interfaces import InterfaceStateListener
InterfaceStateEventType = InterfaceStatus.InterfaceStateEventType
InterfaceState = InterfaceStatus.InterfaceState

OnepAddressScopeType = OnepConstants.OnepAddressScopeType
logger = logging.getLogger('onep:InterfaceStateChangeTutorial')
logger.setLevel(logging.ERROR)
InterfaceTypes = NetworkInterface.InterfaceTypes

"""
 Following class implements an InterfaceStateListener that logs the String representation of the InterfaceStateEvents received.
 The listener is constructed with a name so that different listener instances can
 differentiate their logged output.
 To trigger an event change the status a connected interfaces.
"""
#START SNIPPET: ExampleInterfaceStateListener
class MyInterfaceStateListener(InterfaceStateListener):
    name = str()

    def __init__(self, name):        
        super(MyInterfaceStateListener, self).__init__()
        self.name = name
    
    """
      Invoked when an event is received from a network element.
      @param event
                 An event object that indicates that an event has occurred in a network element.
      @param clientData
                 The clientData is an object that is passed in when the application calls an API to add/register
                 the event listener. The application is responsible for casting the input clientData to the
                 appropriate class before using it.
    """     
    def handle_event(self, event, clientData):            
            print self.name + " has received state change event - from Event Handler " 
            print "Interface has state " + InterfaceState.enumval(event.interface_state) + "\n"
    #END SNIPPET: ExampleInterfaceStateListener

"""
 Following class invokes the tutorial 
"""
class InterfaceStateChangeTutorial(BaseTutorial):
    
    TEN_SEC = 10
    
    def stimulateShutDown(self, interface, val):
        interface.shut_down(val)

if __name__ == '__main__':
    """
        Invokes the tutorial via the command line. This main method attempts to use arguments from the command line.
    """
    tutorial = InterfaceStateChangeTutorial(sys.argv)
    logger.info("Reading arguments...")
    if not tutorial.parse_command_line():
        logger.error("Error in parsing arguments")
        sys.exit(1)
    try:
        logger.info("Connecting to Network Element...")
        if not tutorial.connect("InterfaceAddressTutorial"):
            logger.error("Error in connecting to network element")
            sys.exit(1)   
        
        print "Connected to Network Element " + str(tutorial.get_element_hostname())
        
        #START SNIPPET: registerStateChangeListenerOnElement
        elementStateListener = MyInterfaceStateListener("Network Element State Change")
        network_element = tutorial.get_network_element()
        ifFilter = onep.interfaces.InterfaceFilter()
        print "Adding Interface State Change event listener on network element " + tutorial.get_element_hostname()
        eventHandle1 = network_element.add_interface_state_listener(elementStateListener,ifFilter,InterfaceStateEventType.ONEP_IF_STATE_EVENT_LINK,'Client Data')
        #END SNIPPET: registerStateChangeListenerOnElement
        
        #START SNIPPET: registerStateChangeListenerOnInterfaces
        interfaceStateListener = MyInterfaceStateListener("Interface State Change")
        networkInterface = tutorial.get_an_interface()
        if networkInterface == None:
            logger.error("No interfaces are available.")
            sys.exit(1)
        print "Adding State Change event listener on interface " + networkInterface.name
        eventHandle2 = networkInterface.add_state_listener(interfaceStateListener,InterfaceStateEventType.ONEP_IF_STATE_EVENT_LINK,'Client Data')
        #END SNIPPET: registerStateChangeListenerOnInterfaces
        
        print "\nshutting down interface " + networkInterface.name
        networkInterface.shut_down(1)
        time.sleep(tutorial.TEN_SEC)
        print "bring up interface " + networkInterface.name
        networkInterface.shut_down(0)
        time.sleep(tutorial.TEN_SEC)
        
        print "Removing the registered state change listeners"
        #START SNIPPET: removeStateChangeListenerOnInterfaces
        networkInterface.remove_state_listener(eventHandle2)
        network_element.remove_interface_state_listener(eventHandle1)
        #END SNIPPET: removeStateChangeListenerOnInterfaces
    except Exception as e:
        print e
    finally:
        print "Disconnecting from the Network Element"
        tutorial.disconnect()
        sys.exit(0)

