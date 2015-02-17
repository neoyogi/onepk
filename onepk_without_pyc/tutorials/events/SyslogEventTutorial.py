#!/usr/bin/env python

# Copyright (c) 2010-2013 by Cisco Systems, Inc.
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

"""
  The SyslogEventsTutorial creates an example SyslogListener that logs the String representation of the SyslogEvents
  received from the Network Element. The listener is constructed with a name so that different listener instances can 
  differentiate their logged output.
"""
import sys
import logging
import onep.element.NetworkElement

from time import sleep
from onep.element import SyslogListener
from onep.element import SyslogEvent
from onep.element import SyslogFilter
from onep.core.util import OnepConstants
from BaseTutorial import BaseTutorial

logger = logging.getLogger('onep:SyslogEventTutorial')
logger.setLevel(logging.ERROR)

"""
 This is an example Syslog Listener event handler class
"""    
#  START SNIPPET: ExampleSyslogListener
class ExampleSyslogListener(SyslogListener):    
    name = str()
    
    """
      Creates an Example Syslog Event Listener.
      @param name
            Identifies the instance.
    """
    def __init__(self, name):        
        super(ExampleSyslogListener, self).__init__()
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
        print self.name + " has received SysLog Event\n"
        print "Message        = " + event.message
        print "Message Count  = " + str(event.msg_count)
        print "Priority       = " + onep.element.NetworkElement.OnepSyslogSeverity.enumval(event.priority)
        print "---------------------------\n"
    #  END SNIPPET: ExampleSyslogListener

"""
Invokes the tutorial
"""
class SyslogEventTutorial(BaseTutorial):
    
    TEN_SEC = 10

if __name__ == '__main__':
    """
    Invokes the tutorial via the command line. This main method attempts to use arguments from the command line.
    """
    tutorial = SyslogEventTutorial(sys.argv)
    logger.info("Reading arguments ...")
    if not tutorial.parse_command_line():
        logger.error("Error in parsing arguments")
        sys.exit(1)
    try:
        logger.info("Connecting to Network Element...")
        if not tutorial.connect("SyslogEventTutorial"):
            logger.error("Error in connecting to network element")
            sys.exit(1)

        print "Connected to Network Element " + str(tutorial.get_element_hostname())
        
        #  START SNIPPET: addSyslogListener
        syslogListener = ExampleSyslogListener("Syslog Tutorial")
        syslogFilter = SyslogFilter('Interface')
        syslogFilter.periodMsec = 1000
        syslogFilter.priority = onep.element.NetworkElement.OnepSyslogSeverity.ONEP_SYSLOG_NOTICE
        clientData = None
        network_element = tutorial.get_network_element()
        #
        # Add a syslog event listener
        #
        print 'Adding a Syslog event listener'
        eventHandle = network_element.add_syslog_listener(syslogListener, syslogFilter, clientData)
        #  END SNIPPET: addSyslogListener
        interface = tutorial.get_an_interface()
        if interface == None:
            logger.error("No interfaces are available.")
            sys.exit(1)
        
        print "\nTo trigger a Syslog event "
        print "shutting down interface " + interface.name
        interface.shut_down(1)
        sleep(tutorial.TEN_SEC)
        print "bring up interface " + interface.name
        interface.shut_down(0)
        sleep(tutorial.TEN_SEC)
        
        #
        # Remove the  event listener
        #
        print 'Removing the event listener...'
        network_element.remove_syslog_listener(eventHandle)
    except Exception as e:        
        print e       
    finally:
        print "Disconnecting from the Network Element"
        tutorial.disconnect()
        sys.exit(0)
