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
 The goal of this tutorial is to add a CDP (Cisco Discovery Protocol)
 listener on a Network interface. As a CDP-configured network interface
 sends periodic messages to a multicast address, they are sent to the registered onePK
 application through a callback mechanism.

@author The onePK Team (onepk-feedback@cisco.com)
"""

import logging
from BaseTutorial import BaseTutorial
import sys
from time import sleep
from onep.cdp import CDPFilter
from onep.cdp import CDPListener
from onep.cdp import CDPEvent

logger = logging.getLogger('onep:InterfaceCDPTutorial')
logger.setLevel(logging.ERROR)

"""
 Following class implements an CDPListener that logs the String representation of the CDPEvent received.
 The listener is constructed with a name so that different listener instances can
 differentiate their logged output.
 To trigger an event execute 'cdp enable' on one of the neighbor interfaces.
"""
#  START SNIPPET: ExampleInterfaceCDPListener
class ExampleInterfaceCDPListener(CDPListener):        
    name = str()
    
    def __init__(self, name):            
        super(ExampleInterfaceCDPListener, self).__init__()
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
        print "---------------------------"
        print CDPEvent.CDPEventNotifyType.enumval(event.notify_type)
        print "---------------------------"
        print "NetworkInterface = " + event.intf
        print "neighbor  = " + str(event.device_id)
        print "platform = " + event.platform
        print "version = " + event.version
        print "capabilitites = " + event.capabilities
        print "---------------------------\n"

#  END SNIPPET: ExampleInterfaceCDPListener


"""
 Following class invokes the tutorial 
"""
class InterfaceCDPTutorial(BaseTutorial):    
    TEN_SEC = 10

if __name__ == '__main__':
    """
    Invokes the tutorial via the command line. This main method attempts to use arguments from the command line.
    """
    tutorial = InterfaceCDPTutorial(sys.argv)
    logger.info("Reading arguments ...")
    if not tutorial.parse_command_line():
        logger.error("Error in parsing arguments")
        sys.exit(1)
    try:
        logger.info("Connecting to Network Element...")
        if not tutorial.connect("InterfaceCDPTutorial"):
            logger.error("Error in connecting to network element")
            sys.exit(1)

        print "Connected to Network Element " + str(tutorial.get_element_hostname())
        
        #  START SNIPPET: registerCDPListenerOnInterfaces
        cdpFilter = CDPFilter()
        cdpFilter.notifyType = CDPEvent.CDPEventNotifyType.ONEP_CDP_ALL
        clientData = "CDP Event"
        event_handle = None
        interface = tutorial.get_an_interface()
        if interface == None:
            logger.error("No interfaces are available.")
            sys.exit(1)
        print "Adding CDP event listener on interface " + interface.name
        cdpListener = ExampleInterfaceCDPListener("Interface CDP listener")
        event_handle = interface.add_cdp_listener(cdpListener, cdpFilter, clientData)
        #  END SNIPPET: registerCDPListenerOnInterfaces
        print "Waiting for CDP event to occur"
        sleep(tutorial.TEN_SEC)
        print "Removing CDP event listener"
        #  START SNIPPET: removeCDPListenerOnInterfaces
        interface.remove_cdp_listener(event_handle)
        #  END SNIPPET: removeCDPListenerOnInterfaces        
    except Exception as e:
        print e
    finally:
        print "Disconnecting from the Network Element"
        tutorial.disconnect()
        sys.exit(0)


