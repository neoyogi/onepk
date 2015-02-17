#!/usr/bin/env python

# 
#  * Copyright (c) 2010-2013, Cisco Systems, Inc.
#  *
#  * THIS SAMPLE CODE IS PROVIDED "AS IS" WITHOUT ANY EXPRESS OR IMPLIED WARRANTY
#  * BY CISCO SOLELY FOR THE PURPOSE of PROVIDING PROGRAMMING EXAMPLES.
#  * CISCO SHALL NOT BE HELD LIABLE FOR ANY USE OF THE SAMPLE CODE IN ANY
#  * APPLICATION.
#  *
#  * Redistribution and use of the sample code, with or without
#  * modification, are permitted provided that the following conditions
#  * are met:
#  * Redistributions of source code must retain the above disclaimer.
#  *
#  
"""
This tutorial gets and displays the list of onePK Service Sets
available on the target network device.

@author The onePK Team (onepk-feedback@cisco.com)

"""
import logging
from BaseTutorial import BaseTutorial
from onep.element import NetworkElement
from onep.discovery import ServiceSetDescription

logger = logging.getLogger('onep:DiscoveringOnePKServiceSetsTutorial')
logger.setLevel(logging.INFO)
 
class DiscoveringOnePKServiceSetsTutorial(BaseTutorial):
    
    '''
    Obtain and log the Service Sets.
    
    @throws OnepException
        If there is an error.
    '''   
    def get_service_set_discovery_list(self):
        
        #  START SNIPPET: getServiceSetDiscoveryList
        sdList = tutorial.get_network_element().discover_service_set_list()
        if sdList == None or len(sdList) == 0:
            logger.info("Empty Service Set Description list")
        else:
            for sd in sdList:
                logger.info("NetworkElement IPAddress = %s ", sd.network_element.host_address)
                services = sd.service_set_list
                if services != None:
                    for serviceName in services:
                        logger.info("Service Name: %s ", ServiceSetDescription.ServiceSetName.enumval(serviceName) )
                        logger.info("Versions: %s", services.get(serviceName))
        #  END SNIPPET: getServiceSetDiscoveryList


if __name__ == '__main__':
    import sys
    tutorial = DiscoveringOnePKServiceSetsTutorial(sys.argv)
    #tutorial.parseOptions(args)
    #tutorial.showAuthenticationDialog()
    if not tutorial.parse_command_line():
        logger.error("Error in parsing arguments")
        sys.exit(1)
    try:
        logger.info("Connecting to Network Element...")
        if not tutorial.connect("ServiceDiscoveryTutorial"):
            logger.error("Error in connecting to network element")
            sys.exit(1)
        tutorial.get_service_set_discovery_list()
    except Exception as e:
        tutorial.disconnect()
        logger.error(e)
    finally:
        tutorial.disconnect()
        sys.exit(0)
    

