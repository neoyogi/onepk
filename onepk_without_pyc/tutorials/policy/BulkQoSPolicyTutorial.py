#!/usr/bin/env python

# Copyright (c) 2010-2013 by Cisco syss, Inc.
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
# package: tutorials.routing
import logging
from BaseTutorial import BaseTutorial
from onep.policyservice import bulk
from onep.policyservice import match
from onep.policyservice import caps
from onep.policyservice.target import Target
from onep.policyservice import action
from onep.policyservice import StorageType
from onep.core.util import OnepConstants
from onep.interfaces import InterfaceFilter
from onep.interfaces import NetworkInterface

logger = logging.getLogger('onep:BulkQoSPolicyTutorial')
logger.setLevel(logging.INFO)

# 
#  * This tutorial show how a onePK application creates a QoS Policy on a Network Element. 
#  * The QoS Policy object is a top-level object in a hierarchy of objects that define class, 
#  * filter and action objects that are used to apply QoS policy to interface targets. 
#  * The Policy object is associated with a target (or interface).
#  * 
#  * @author The onePK Team (onepk-feedback@cisco.com)
#  * 
#  
class BulkQoSPolicyTutorial(BaseTutorial):
    """
    This tutorial show how a onePK application creates a Bulk QoS Policy on a Network Element. 
    """
    
    #  START SNIPPET: BULK_QOS_VARIABLES
    MIN_PACKET_LENGTH = 250
    MAX_PACKET_LENGTH = 500
    
    class_map1 = None
    classMap1Handle = None
    bulkService = None
    policyQuery = None
    policyCapabilities = None
    policy_map1 = None
    policyMap1Handle = None
    entry1 = None
    entry2 = None
    entry3 = None
    #  END SNIPPET: BULK_QOS_VARIABLES
    
    def create_policy_map(self):
        bulkService = bulk.BulkService(tutorial.network_element)
        #START SNIPPET: createPolicymap
        for tbl in caps.get_table_capabilities(tutorial.network_element):
            if match.MatchType.MATCH_IP_DSCP in tbl.matches and \
               action.ActionType.SET_DSCP in tbl.actions:
                self.policy_map1 = bulkService.create_policy(tbl.type, tutorial.network_element)
                if tbl.persistent:
                    self.policy_map1.storage_type = StorageType.PERSISTENT
                #END SNIPPET: createPolicymap
        
                #START SNIPPET: createPolicymapEntry
                self.entry1 = self.policy_map1.create_entry(self.class_map1)
                #END SNIPPET: createPolicymapEntry
                action_mark1 = action.Mark(action.ActionType.SET_DSCP, 7)
                #START SNIPPET: addPolicymapEntryMatch
                self.entry1.add_action(action_mark1)
                #END SNIPPET: addPolicymapEntryMatch
                #START SNIPPET: getPolicyMapResult
                logger.info("Submitting policy map...")
                bulkService.submit_policy_map(self.policy_map1)
                logger.info("After Create policy map: Result Text = "
                            + self.policy_map1.result_text)
                policyMap1Handle = self.policy_map1.handle
                logger.info("PMapHandle - " + str(policyMap1Handle) + "\n")
                #END SNIPPET: getPolicyMapResult
                break

    def create_class_map(self):
        bulkService = bulk.BulkService(tutorial.network_element)
        #START SNIPPET: createCapability
        for tbl in caps.get_table_capabilities(tutorial.network_element):
            if match.MatchType.MATCH_IP_DSCP in tbl.matches:
                logger.info("TABLE NAME "+ tbl.name + "\n")
                #END SNIPPET: createCapability
                #START SNIPPET: createClassmap
                self.class_map1 = bulkService.create_class(tbl.type, tutorial.network_element)
                if tbl.persistent:
                    self.class_map1.storage_type = StorageType.PERSISTENT
                self.class_map1.match_all = True
                #END SNIPPET: createClassmap        
           
                #START SNIPPET: classmapAddMatch
                self.class_map1.add_match(match.DSCP(OnepConstants.OnepDscp.ONEP_DSCP_EF))
                #END SNIPPET: classmapAddMatch
                
                logger.info("Submitting ClassMap...");
                #START SNIPPET: getClassMapResult
                bulkService.submit_class_map(self.class_map1)
                logger.info("After Create class map: Result Text = " 
                            + self.class_map1.result_text)
                classMap1Handle = self.class_map1.handle
                logger.info("CMapHandle - " + str(classMap1Handle) + "\n")
                #END SNIPPET: getClassMapResult
                break
    
    def apply_target(self):
        intf = tutorial.get_an_interface(address_required=False)
        if intf is None:
            raise Exception('No interface available for use.')
        
        logger.info("Creating Target on interface : %s",intf.name);
        #START SNIPPET: createTarget
        t1 = Target(intf, Target.TargetLocation.HARDWARE_DEFINED_INPUT)
        #END SNIPPET: createTarget
        
        logger.info("Creating activationHolder...");
        #START SNIPPET: addPolicyToTarget
        self.activationHolder = bulkService.create_activation_holder(self.policy_map1, t1)
        #END SNIPPET: addPolicyToTarget
        
        logger.info("Activating policy...");
        #START SNIPPET: getTargetPolicyResult
        bulkService.activate_policy(self.activationHolder)
        logger.info("Result Text: " + self.policy_map1.result_text)
        #END SNIPPET: getTargetPolicyResult
        
    
    def clean_up(self):
        #START SNIPPET: removeBulkQOS
        if not self.policy_map1==None:
            logger.info("\nDeactivating policy")
            bulkService.deactivate_policy(self.activationHolder)
            logger.info("Deleting policy map")
            bulkService.delete_policy_map(self.policy_map1)
        if not self.class_map1==None:  
            logger.info("Deleting class map1")
            bulkService.delete_class_map(self.class_map1)
        #END SNIPPET: removeBulkQOS

if __name__ == '__main__':
    import sys
    tutorial = BulkQoSPolicyTutorial(sys.argv)
    logger.info("Reading arguments...")
    if not tutorial.parse_command_line():
        logger.error("Error in parsing arguments")
        sys.exit(1)
    try:
        logger.info("Connecting to Network Element...")
        if not tutorial.connect("BulkQoSPolicyTutorial"):
            logger.error("Error in connecting to network element")
            sys.exit(1)
        logger.info("Done")
        
        """create bulkservice"""
        #START SNIPPET: createBulkService
        bulkService = bulk.BulkService(tutorial.network_element)
        #END SNIPPET: createBulkService
                
        """create class map"""
        tutorial.create_class_map()
        
        """create policy map"""
        tutorial.create_policy_map()
        
        """Apply to target"""
        tutorial.apply_target()
        
        raw_input('\nPolicy created\nContinue to clean up? <enter> : ')
        
        """clean up the maps"""
        tutorial.clean_up()
        
    except Exception, e:
        tutorial.disconnect()
        logger.error(str(e))
    tutorial.disconnect()
    sys.exit(0)

