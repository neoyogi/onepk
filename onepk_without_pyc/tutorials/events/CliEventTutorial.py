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
  CLI event tutorial demonstrate how to add a CLI event listener on a network element.
  It also demonstrates how to handle a CLI event and alter its default behavior.
  
  @author The onePK Team (onepk-feedback@cisco.com)  
"""

import sys
import logging
from   time import sleep
import onep.element.NetworkElement
from   onep.element import CLIListener
from   onep.element import CLIEvent
from   onep.element import CLIFilter
from   onep.core.util import OnepConstants
from BaseTutorial import BaseTutorial

logger = logging.getLogger('onep:CliEventTutorial')
logger.setLevel(logging.ERROR)

"""
 This is an example CLI event Listener that will handle the CLI event.
   
"""
#  START SNIPPET: ExampleCliListener
class ExampleCliListener(CLIListener):
    
    name = ''

    """
      Creates an Example CLI Event Listener.
      @param name
            Identifies the instance.
    """
    def __init__(self, name):        
        super(ExampleCliListener, self).__init__()
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
    def handle_event(self,event,clientData):
        print "---------------------------"
        print "CLI Event: handle_event\n"
        print " eventHandle" + str(event.event_handle)
        print " msgCount = " + str(event.msg_count)
        print " sync = " + str(event.sync)
        print " sync = " + str(event.tty)
        print " message = " + event.message
        print "---------------------------\n"
    
    """
      Invoked when a sync event is received from a network element.
      @param event
                 An event object that indicates that an event has occurred in a network element.
      @param clientData
                 The clientData is an object that is passed in when the application calls an API to add/register
                 the event listener. The application is responsible for casting the input clientData to the
                 appropriate class before using it.
    """     
    def handle_sync_event(self,event,clientData):
        print "---------------------------"
        print "CLI Event: handle_sync_event\n"
        print " eventHandle" + str(event.event_handle)
        print " msgCount = " + str(event.msg_count)
        print " sync = " + str(event.sync)
        print " sync = " + str(event.tty)
        print " message = " + event.message
        print "---------------------------\n"
    def get_sync_reply(self):
        print "---------------------------"
        print "CLI Event: get_sync_reply\n"
        print "---------------------------\n"
#  END SNIPPET: ExampleCliListener

"""
Invokes the tutorial
"""
class CliEventTutorial(BaseTutorial):
    
    TEN_SEC = 10

if __name__ == '__main__':
    """
    Invokes the tutorial via the command line. This main method attempts to use arguments from the command line.
    """
    tutorial = CliEventTutorial(sys.argv)
    logger.info("Reading arguments ...")
    if not tutorial.parse_command_line():
        logger.error("Error in parsing arguments")
        sys.exit(1)
    try:
        logger.info("Connecting to Network Element...")
        if not tutorial.connect("CliEventTutorial"):
            logger.error("Error in connecting to network element")
            sys.exit(1)

        print "Connected to Network Element " + str(tutorial.get_element_hostname())
        
        #  START SNIPPET: addCliEventListener
        cliListener = ExampleCliListener("CLI event listener")
        cliFilter = CLIFilter('clock')
        clientData = None          
        network_element = tutorial.get_network_element()
        #
        # Add a CLI event listener
        #
        print "Adding a CLI event listener'"
        eventHandle = network_element.add_cli_listener(cliListener, cliFilter, clientData)
        print "To verify please enter 'show clock' command on the connected device"
        #  END SNIPPET: addCliEventListener
        #  invoke 'show location' CLI on the connected network element 
        sleep(tutorial.TEN_SEC)
        #  Removes the CliEventListener from the Network Element. 
        print "Removing the CLI event listener"
        #  START SNIPPET: removeCliEventListener
        network_element.remove_cli_listener(eventHandle)
        #  END SNIPPET: removeCliEventListener
    except Exception as e:
        print e
    finally:
        tutorial.disconnect()
        # disconnect network element
        sys.exit(0)
