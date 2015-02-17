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
# 
# package: tutorials.element
"""
 The NetworkElementTutorial demonstrates the abilities like connecting to a Network Element, getting an attributes of a Network Element.
 
 @author The onePK Team (onepk-feedback@cisco.com)

"""

import logging
from BaseTutorial import BaseTutorial
from onep.element import NetworkElement, NetworkApplication

logger = logging.getLogger('onep:NetworkElementTutorial')
logger.setLevel(logging.INFO)

class NetworkElementTutorial(BaseTutorial):
    
    def get_system_cpu_utilization(self, network_element):
        """
        Returns the Network Element CPU Utilization
        
        @param network_element
        
        @return
        
        @throws OnepConnectionException
        @throws OnepRemoteProcedureException
        @throws OnepException
        """
        logger.info("Total System CPU Utilization - %s", network_element.get_system_cpu_utilization())
        return network_element.get_system_cpu_utilization()

    def get_total_system_memory(self, network_element):
        """
        Returns the Network Element Total Memory
        
        @param network_element
        
        @return
        
        @throws OnepRemoteProcedureException
        @throws OnepConnectionException
        """
        logger.info("Total System Memory - %s", network_element.get_total_system_memory())
        return network_element.get_total_system_memory()

    def get_free_system_memory(self, network_element):
        """
        Returns the Network Element Free memory
        
        @param network_element
        
        @return
        
        @throws OnepRemoteProcedureException
        @throws OnepConnectionException
        """        
        logger.info("Free System Memory - %s", network_element.get_free_system_memory())
        return network_element.get_free_system_memory()

    def is_network_element_connected(self, network_element):
        """
        Checks if the network element is connected or not
        
        @param network_element
        
        @return
        """    
        logger.info("NetworkElement is connected - %s", network_element.is_connected())
        return network_element.is_connected()


if __name__ == '__main__':
    """
    Invokes the tutorial via the command line. This main method attempts to use arguments from the command line.
    """
    import sys
    tutorial = NetworkElementTutorial(sys.argv)
    logger.info("Reading arguments...")
    if not tutorial.parse_command_line():
        logger.error("Error in parsing arguments")
        sys.exit(1)
    try:
        logger.info("Connecting to Network Element...")
        if not tutorial.connect("NetworkElementTutorial"):
            logger.error("Error in connecting to network element")
            sys.exit(1)
        logger.info("Done")
        
        #  START SNIPPET: get_ne_parent
        parent = tutorial.network_element.parent
        logger.info("NetworkElement parent - %s", parent.name)
        #  END SNIPPET: get_ne_parent
        
        #  START SNIPPET: get_ne_tostring
        print tutorial.network_element.__str__()
        #  END SNIPPET: get_ne_tostring

        #Check if Network Element is connected
        #  START SNIPPET: ne_isconnected
        tutorial.is_network_element_connected(tutorial.get_network_element())
        #  END SNIPPET: ne_isconnected

        #Get Free System Memory of a Network Element
        #  START SNIPPET: get_ne_fsm
        tutorial.get_free_system_memory(tutorial.get_network_element())
        #  END SNIPPET: get_ne_fsm

        # Get Total System Memory of a Network Element
        #  START SNIPPET: get_ne_tsm
        tutorial.get_total_system_memory(tutorial.get_network_element())
        #  END SNIPPET: get_ne_tsm

        # Get Total CPU Utilization of a Network Element
        #  START SNIPPET: get_ne_cpuutil
        tutorial.get_system_cpu_utilization(tutorial.get_network_element())
        #  END SNIPPET: get_ne_cpuutil
    except Exception, e:
        #  START SNIPPET: disconnect_ne
        tutorial.disconnect()
        #  END SNIPPET: disconnect_ne
        logger.error(e.__str__())
    tutorial.disconnect()
    sys.exit(0)
