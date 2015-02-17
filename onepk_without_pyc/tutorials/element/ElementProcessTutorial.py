#!/usr/bin/env python

# 
# * Copyright (c) 2010-2013 by Cisco syss, Inc.
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
# package: tutorials.element
import logging
from BaseTutorial import BaseTutorial
from onep.element import NetworkElement, NetworkApplication

logger = logging.getLogger('onep:ElementProcessTutorial')
logger.setLevel(logging.INFO)


class ElementProcessTutorial(BaseTutorial):
    """
    The ElementProcessTutorial demonstrates the abilities like connecting to a Network Element, 
    reading process information of the network element and getting an attributes of a Network processes.
    
    @author The onePK Team (onepk-feedback@cisco.com)
    """
    
    def get_element_process_attributes(self, process_list):
        """
        Prints all the attributes of Process while iterating over the Process List of the network element.
        
        @param process_list
        """
        for element_process in process_list:
            
            logger.info(element_process)
            
            """Get allocated memory of the Element Process of a Network Element"""
            #  START SNIPPET: get_ne_process_alloc_mem
            logger.info("Allocated Memory - %s", element_process.allocatedMemory)
            #  END SNIPPET: get_ne_process_alloc_mem
            
            """Get CPU utilization of the Element Process of a Network Element"""
            #  START SNIPPET: get_ne_process_cpuutil
            logger.info("CPU utilization - %s", element_process.cpuUsage)
            #  END SNIPPET: get_ne_process_cpuutil
            
            """Get freed memory of the Element Process of a Network Element"""              
            #  START SNIPPET: get_ne_process_freemem
            logger.info("Freed Memory - %s", element_process.freedMemory)
            #  END SNIPPET: get_ne_process_freemem
            
            """Get Process ID of the Element Process of a Network Element"""
            #  START SNIPPET: get_ne_process_pid
            logger.info("Process ID - %s", element_process.processID)
            #  END SNIPPET: get_ne_process_pid
            
            """Get Process Name of the Element Process of a Network Element"""
            #  START SNIPPET: get_ne_process_pname
            logger.info("Process Name - %s", element_process.processName)
            #  END SNIPPET: get_ne_process_pname
            
            """Get used memory of the Element Process of a Network Element"""
            #  START SNIPPET: get_ne_process_usedmem
            logger.info("Used Memory - %s", element_process.heldMemory)
            #  END SNIPPET: get_ne_process_usedmem
            
if __name__ == '__main__':
    """
    Invokes the tutorial via the command line. This main method attempts to use arguments from the command line.
    """
    import sys
    tutorial = ElementProcessTutorial(sys.argv)
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
        #  START SNIPPET: get_ne_process
        process_list = tutorial.get_network_element().get_process_list()
        #  END SNIPPET: get_ne_process
        tutorial.get_element_process_attributes(process_list)
    except Exception as e:
        tutorial.disconnect()
        logger.error(str(e))
    tutorial.disconnect()
    sys.exit(0)
