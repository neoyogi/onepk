#!/usr/bin/env python

# Copyright (c) 2010-2014 by Cisco Systems, Inc.
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
# package: tutorials.identity

import sys
import logging
from BaseTutorial import BaseTutorial
from onep.aaa import OnepAAAAttributeType, StringAttribute, IntAttribute
from onep.identity import Identity
from onep.core.exception import OnepNotSupportedException

logger = logging.getLogger('onep:IdentityTutorial')
logger.setLevel(logging.INFO)

class IdentityTutorial(BaseTutorial):
    """ create the attribute list """
    #  START SNIPPET: create_Attribute_list
    attribute_list1 = []
    attribute_list1.append(StringAttribute(
                        OnepAAAAttributeType.ONEP_AAA_AT_FORMATTED_CLID,
                        "mac-addr", "aa:bb:cc:dd:ee:11"))
    attribute_list1.append(StringAttribute(
                        OnepAAAAttributeType.ONEP_AAA_AT_USER_NAME,
                        "username", "test"))
    #  END SNIPPET: create_Attribute_list
    attribute_list1a = []
    attribute_list1a.append(StringAttribute(
                        OnepAAAAttributeType.ONEP_AAA_AT_USER_NAME,
                        "username", "test1a"))
    
    attribute_list2 = []
    
    attribute_list2.append(StringAttribute(
                        OnepAAAAttributeType.ONEP_AAA_AT_FORMATTED_CLID, 
                        "mac-addr", "aa:bb:cc:dd:ee:ab"))
    attribute_list2.append(StringAttribute(
                        OnepAAAAttributeType.ONEP_AAA_AT_USER_NAME,
                        "username", "test"))
    attribute_list2.append(IntAttribute(
                        OnepAAAAttributeType.ONEP_AAA_AT_INTERFACE,
                        "interface", 1))
    
    
if __name__ == "__main__":
    tutorial = IdentityTutorial(sys.argv)
    if not tutorial.parse_command_line():
        logger.error("Error in parsing arguments")
        sys.exit(1)
    
    tutorial.identity = None
    tutorial.identity_session1 = None
    tutorial.identity_session2 = None
    
    try:
        logger.info("Connecting to Network Element...")
        if not tutorial.connect("IdentityTutorial"):
            logger.error("Error in connecting to network element")
            sys.exit(1)
            
        """ Create an Identity instance for the network element """
        #  START SNIPPET: create_identity
        identity = Identity(tutorial.network_element)
        #  END SNIPPET: create_identity
        
        """ add the session to the network element """
        logger.info('adding session with attribute_list1')
        #  START SNIPPET: add_session
        tutorial.identity_session1 = tutorial.identity.add_session(IdentityTutorial.attribute_list1)
        if tutorial.identity_session1 is None:
            logger.error("Could not add the session.")
        else:
            logger.info("Session added. The session label is:" + str(tutorial.identity_session1.session_label))
        #  END SNIPPET: add_session
        
        logger.info('adding session with attribute_list2')
        tutorial.identity_session2 = tutorial.identity.add_session(IdentityTutorial.attribute_list2)
        if tutorial.identity_session2 is None:
            logger.error("Could not add the session.")
        else:
            logger.info("Session added. The session label is:" + str(tutorial.identity_session2.session_label))
                
        """ find a session matching the attributes """
        logger.info('Finding sessions matching attribute username test')
        #  START SNIPPET: find_session
        sessionMap = tutorial.identity.find_session_by_attributes([StringAttribute(
                                OnepAAAAttributeType.ONEP_AAA_AT_USER_NAME,
                                "username", "test")])
        logger.info('the sessions matching the attribute list are : ')
        for key in sessionMap.keys():
            logger.info(str(key.session_label))
        #  END SNIPPET: find_session
        
        """ update attributes of already existing session """
        logger.info('Updating identity_session1 attributes.')
        #  START SNIPPET: update_session
        tutorial.identity_session1.update_session_attributes(IdentityTutorial.attribute_list1a)
        #  END SNIPPET: update_session
        logger.info("update session completed")
        
        """ fetch the session attributes """
        logger.info('Fetching identity_session1 attributes.')
        #  START SNIPPET: fetch_session
        fetched_attribute_list = tutorial.identity_session1.fetch_session_attributes()
        logger.info('the session attributes are : ')
        for attribute in fetched_attribute_list:
            logger.info(OnepAAAAttributeType.enumval(attribute.type_)+': '+attribute.str_value)
        #  END SNIPPET: fetch_session
        
        
    except Exception as e:
        logger.error(str(e))
    finally:
        try:
            if tutorial.identity and tutorial.identity_session1:
                """ delete a session """
                logger.info('Deleting identity_session1')
                #  START SNIPPET: delete_session
                tutorial.identity.delete_session(tutorial.identity_session1)
                #  END SNIPPET: delete_session
                logger.info('identity_session1 deleted')
        except:
            pass
        try:
            if tutorial.identity and tutorial.identity_session2:
                """ delete session which matches the attributes """
                logger.info('deleting session matching attribute_list2')
                #  START SNIPPET: delete_by_attributes
                tutorial.identity.delete_session_by_attributes(tutorial.attribute_list2)
                #  END SNIPPET: delete_by_attributes
                logger.info('identity_session2 deleted')
        except:
            pass
        logger.info('disconnecting from the network element.')
        tutorial.disconnect()
        sys.exit(0)
