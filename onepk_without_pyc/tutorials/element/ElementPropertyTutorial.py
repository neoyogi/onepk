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
from onep.element import NetworkElement

logger = logging.getLogger('onep:ElementPropertyTutorial')
logger.setLevel(logging.INFO)

class ElementPropertyTutorial(BaseTutorial):
    """
    The ElementPropertyTutorial demonstrates the abilities like connecting to a Network Element, 
    reading property information of the network element and getting an attributes of a Network property.
 
    @author The onePK Team (onepk-feedback@cisco.com)
    """
    # 
    
    # 	 
    def get_element_property_attributes(self, element_property):
        """
        Prints all the attributes of Property of a Network element.

        @param element_property
        @throws OnepRemoteProcedureException
        @throws OnepConnectionException
        """
         
        """Get Processor of the Element Property of a Network Element"""
        #  START SNIPPET: get_np_processor
        processor = element_property.processor
        #  END SNIPPET: get_np_processor
        logger.info("Processor - %s", processor)

        """Get PID of the Element Property of a Network Element"""
        #  START SNIPPET: get_np_pid
        product_id = element_property.product_id
        #  END SNIPPET: get_np_pid
        logger.info("Product Id - %s", product_id)

        """Get Serial Number of the Element Property of a Network Element"""
        #  START SNIPPET: get_np_sn
        serial_no = element_property.SerialNo
        #  END SNIPPET: get_np_sn
        logger.info("Serial Number - %s", serial_no)

        """Get Description of the Element Property of a Network Element"""
        #  START SNIPPET: get_np_desc
        sys_descr = element_property.sys_descr
        #  END SNIPPET: get_np_desc
        logger.info("sys Description - %s", sys_descr)

        """Get sys Name of the Element Property of a Network Element"""
        #  START SNIPPET: get_np_sysnm
        sys_name = element_property.sys_name
        #  END SNIPPET: get_np_sysnm
        logger.info("sys Name - %s", sys_name)

        """Get sys uptime of the Element Property of a Network Element"""
        #  START SNIPPET: get_np_sysuptime
        sys_uptime = element_property.sys_uptime
        #  END SNIPPET: get_np_sysuptime
        logger.info("sys Up time - %s", sys_uptime)


if __name__ == '__main__':
    """
    Invokes the tutorial via the command line. This main method attempts to use arguments from the command line.
    """
    import sys
    tutorial = ElementPropertyTutorial(sys.argv)
    logger.info("Reading arguments...")
    if not tutorial.parse_command_line():
        logger.error("Error in parsing arguments")
        sys.exit(1)
    try:
        logger.info("Connecting to Network Element...")
        if not tutorial.connect("ElementPropertyTutorial"):
            logger.error("Error in connecting to network element")
            sys.exit(1)
        logger.info("Done")
        #  START SNIPPET: get_ne_prop
        element_property = tutorial.get_network_element().properties
        tutorial.get_element_property_attributes(element_property)
        #  END SNIPPET: get_ne_prop
    except Exception, e:
        tutorial.disconnect()
        logger.error("Error in getting Process Attributes : %s", str(e))
    tutorial.disconnect()
    sys.exit(0)
