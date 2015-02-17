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
from onep.core.exception import OnepNoDataException

logger = logging.getLogger('FRUTutorial`')
logger.setLevel(logging.INFO)

class FRUTutorial(BaseTutorial):
    """
    The FRUTutorial demonstrates the abilities like connecting to a Network Element, 
    reading FRU list of the network element and getting an attributes of FRU.
 
    @author The onePK Team (onepk-feedback@cisco.com)
    """
    
    def get_fru_attributes(self, fruList):
        """
        Prints all the attributes of FRU while iterating over the FRU List of the network element.
        
        @param fruList
        """
        for fru in fruList:
            # FRU Details
            logger.info("\n\nFRU Details :")
            # FRU alarm type
            #  START SNIPPET: get_fru_alarm
            logger.info("FRU alarm type - " + fru.alarm_type)
            #  END SNIPPET: get_fru_alarm
            
            # FRU Firmware Version
            #  START SNIPPET: get_fru_fw
            logger.info("FRU Firmware Version - " + fru.fw_version)
            #  END SNIPPET: get_fru_fw
            
            # FRU Hardware Version
            #  START SNIPPET: get_fru_hw
            logger.info("FRU Hardware Version - " + fru.hw_version)
            #  END SNIPPET: get_fru_hw
            
            # FRU Part Number
            #  START SNIPPET: get_fru_pn
            logger.info("FRU Part Number - " + fru.part_no)
            #  END SNIPPET: get_fru_pn
            
            # FRU product Identifier (PID)
            #  START SNIPPET: get_fru_pid
            logger.info("FRU product Identifier (PID) - " + fru.product_id )
            #  END SNIPPET: get_fru_pid
            
            # FRU Serial Number (SN)
            #  START SNIPPET: get_fru_sn
            logger.info("FRU Serial Number (SN) - " + fru.serial_no)
            #  END SNIPPET: get_fru_sn
            
            # FRU slot number
            #  START SNIPPET: get_fru_slot
            logger.info("FRU slot number - " + str(fru.slot))
            #  END SNIPPET: get_fru_slot
            
            # FRU Software Version
            #  START SNIPPET: get_fru_sw
            logger.info("FRU Software Version - " + fru.sw_version)
            #  END SNIPPET: get_fru_sw

if __name__ == '__main__':
    import sys
    tutorial = FRUTutorial(sys.argv)
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
        #  START SNIPPET: get_ne_fru_list
        fru_list = tutorial.get_network_element().get_fru_list()
        #  END SNIPPET: get_ne_fru_list
        tutorial.get_fru_attributes(fru_list)
    except OnepNoDataException, e:
        print "\n    This Network Element has no FRU items to display\n"
    except Exception, e:
        tutorial.disconnect()
        logger.error("Error in getting Process Attributes : %s", str(e))
    tutorial.disconnect()
    sys.exit(0)
