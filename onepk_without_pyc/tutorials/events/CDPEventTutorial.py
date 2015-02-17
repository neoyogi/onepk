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
# package: tutorials.events

"""
 The goal of this tutorial is to add a CDP (Cisco Discovery Protocol) listener and to process
 the CDP event occurred on a NetworkElement object.

 @author The onePK Team (onepk-feedback@cisco.com)
"""

import sys
import logging
from   time import sleep
import onep.element.NetworkElement
from   onep.cdp import CDPFilter
from   onep.cdp import CDPListener
from   onep.cdp import CDPEvent
from   onep.interfaces import InterfaceFilter
from   BaseTutorial import BaseTutorial

logger = logging.getLogger('onep:CDPEventTutorial')
logger.setLevel(logging.ERROR)

"""
  Implements an CDPListener that logs the String representation of the CDPEvent received.
  The listener is constructed with a name so that different listener instances can
  differentiate their logged output. 
"""
#  START SNIPPET: ExampleNeCDPListener
class ExampleNeCDPListener(CDPListener):
    
    name = str()

    def __init__(self, name):        
        super(ExampleNeCDPListener, self).__init__()
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
        print "NetworkInterface = " + str(event.intf)
        print "neighbor  = " + str(event.device_id)
        print "platform = " + event.platform
        print "version = " + event.version
        print "capabilitites = " + event.capabilities
        print "---------------------------\n"

#  END SNIPPET: ExampleNeCDPListener

"""
Invokes the tutorial
"""
class CDPEventTutorial(BaseTutorial):
    
    TEN_SEC = 10

if __name__ == '__main__':
    """
    Invokes the tutorial via the command line. This main method attempts to use arguments from the command line.
    """
    tutorial = CDPEventTutorial(sys.argv)
    logger.info("Reading arguments ...")
    if not tutorial.parse_command_line():
        logger.error("Error in parsing arguments")
        sys.exit(1)
    try:
        logger.info("Connecting to Network Element...")
        if not tutorial.connect("CDPEventTutorial"):
            logger.error("Error in connecting to network element")
            sys.exit(1)

        print "Connected to Network Element " + str(tutorial.get_element_hostname())
        #  START SNIPPET: addCDPListenerOnNe
        cdpListener = ExampleNeCDPListener("CDP Tutorial")
        cdpFilter = CDPFilter()
        cdpFilter.notifyType = CDPEvent.CDPEventNotifyType.ONEP_CDP_ALL
        ifFilter = InterfaceFilter()
        clientData = None
        network_element = tutorial.get_network_element()
        print "Adding CDP listener to network element"
        event_handle = network_element.add_cdp_listener(cdpListener, ifFilter, cdpFilter, clientData)
        #  END SNIPPET: addCDPListenerOnNe
        print "Waiting for a CDP event to occur"
        sleep(tutorial.TEN_SEC)
        #
        # Remove the  event listener
        #
        print 'Removing the event listener...'
        #  START SNIPPET: removeCDPListenerOnNe
        network_element.remove_cdp_listener(event_handle)
        #  END SNIPPET: removeCDPListenerOnNe
    except Exception as e:
        print e
    finally:
        tutorial.disconnect()
        # disconnect network element
        sys.exit(0)
