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
 This tutorial shows how a onePK application can obtain network interface statistics
 via two different methods: either polling for statistics or
 by registering a "listener" to retrieve statistics from an interface
 only when the data crosses a certain threshold.

 @author The onePK Team (onepk-feedback@cisco.com)  
"""

import logging
from BaseTutorial import BaseTutorial
import sys
import time
from onep.interfaces import NetworkInterface
from onep.core.util import  OnepConstants
OnepOperatorType = OnepConstants.OnepOperatorType
from onep.interfaces import InterfaceStatistics
from onep.interfaces import InterfaceStatisticsFilter
from onep.interfaces import InterfaceStatus
from onep.interfaces import InterfaceStatisticsListener

InterfaceStateEventType = InterfaceStatus.InterfaceStateEventType
InterfaceState = InterfaceStatus.InterfaceState
InterfaceStatisticsParameter = InterfaceStatistics.InterfaceStatisticsParameter
_InterfaceStatisticsType = InterfaceStatisticsFilter.InterfaceStatisticsType

OnepAddressScopeType = OnepConstants.OnepAddressScopeType
logger = logging.getLogger('onep:InterfaceStatisticsTutorial')
logger.setLevel(logging.INFO)
InterfaceTypes = NetworkInterface.InterfaceTypes

"""
 Implements an InterfaceStatisticsListener that logs the String representation of the InterfaceStatisticsEvent
 received. The listener is constructed with a name so that different listener instances can differentiate their
 logged output.
"""
#START SNIPPET: ExampleInterfaceStatisticsListener
class MyInterfaceStatisticsListener(InterfaceStatisticsListener):
    name = str()

    def __init__(self, name):        
        super(MyInterfaceStatisticsListener, self).__init__()
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
            print self.name + " has received statistics change event - from Event Handler "
            if InterfaceStatisticsParameter.ONEP_IF_STAT_RX_PKTS_BCAST == event.parameter:
                print "\tchange in ONEP_IF_STAT_RX_PKTS_BCAST value on interface " + event.interface.name
#END SNIPPET: ExampleInterfaceStatisticsListener

"""
 Following class invokes the tutorial 
"""            
class InterfaceStatisticsTutorial(BaseTutorial):
    
    TEN_SEC = 10
    POLL_SLEEP = 10
    POLL_LOOP = 3
    
    """
      Gets statistics from NetworkInterfaces on a periodic basis, that is, using a poll loop.
      @throws OnepException
                  If there is a error.
      @throws InterruptedException
                  If there is an interruption when sleeping between polls.
    """
    #START SNIPPET: pollStatistics
    def pollStatistics(self, networkInterface):    
        print "\nPolling for network interface stats..."
        statistics = None
        i = 0
        try:
            while i < self.POLL_LOOP:                 
                statistics = networkInterface.get_statistics()
                print "-------- " + networkInterface.name+ " ----------"
                print "Number of broadcast packets received by the interface.: " + str(statistics.receive_broadcast)
                print "CRC Errors:" + str(statistics.in_error_crc)
                print "Receive Rate (in BPS): " + str(statistics.receive_rate_bps)
                print "Received multicast packets: " + str(statistics.receive_multicast)
                i += 1
                if i < self.POLL_LOOP:
                    time.sleep(self.POLL_SLEEP)
        except Exception as e:
            print e
        print "\nDone polling for network interface stats"
    #END SNIPPET: pollStatistics
 
if __name__ == '__main__':
    """
        Invokes the tutorial via the command line. This main method attempts to use arguments from the command line.
    """
    tutorial = InterfaceStatisticsTutorial(sys.argv)
    logger.info("Reading arguments ...")
    if not tutorial.parse_command_line():
        logger.error("Error in parsing arguments")
        sys.exit(1)
    try:
        logger.info("Connecting to Network Element...")
        if not tutorial.connect("InterfaceStatisticsTutorial"):
            logger.error("Error in connecting to network element")
            sys.exit(1)

        print "Connected to Network Element " + str(tutorial.get_element_hostname())
        
        #START SNIPPET: registerStatisticsListenerOnInterfaces
        #Add interface stats listener to interface
        statsFilter = None
        statsFilter = InterfaceStatisticsFilter(
                InterfaceStatisticsParameter.ONEP_IF_STAT_RX_PKTS_BCAST, #parameter to monitor
                OnepOperatorType.ONEP_OP_GE, #Greater than or Equal to
                0, #value to trigger the event
                _InterfaceStatisticsType.ONEP_INTERFACE_STATISTICS_TYPE_VALUE)
        
        listener = MyInterfaceStatisticsListener("Interface Statistics Tutorial")       
        networkInterface = tutorial.get_an_interface()
        networkelement = tutorial.get_network_element()
        #networkInterface = networkelement.get_interface_by_name('Ethernet1/3')
        if networkInterface == None:
            logger.error("No interfaces are available.")
            sys.exit(1)
        
        #Polling statistics on network interface
        tutorial.pollStatistics(networkInterface)
        
        print "\nAdding statistics change listener on interface " + networkInterface.name
        evtHandle = networkInterface.add_statistics_listener(listener, statsFilter, 'Stats Event')
        #END SNIPPET: registerStatisticsListenerOnInterfaces
        print "\nWaiting for statistics changes to occur..."
        time.sleep(tutorial.TEN_SEC)                

        print "\nRemoving event listener"
        #START SNIPPET: removeStatisticsListenerOnInterfaces
        networkInterface.remove_statistics_listener(evtHandle)
        #END SNIPPET: removeStatisticsListenerOnInterfaces
        
    except Exception as e:
        print e
    finally:
        print "\nDisconnecting from the Network Element"
        tutorial.disconnect()
        sys.exit(0)


                        
