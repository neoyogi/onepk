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
AAA Tutorial

This tutorial demonstrates the onePK AAA (Authentication, Authorization,
and Accounting) Service Set. The AAA Service Set provides AAA client
functionality to onePK applications.

You will learn how to authenticate a user, how to read the user's
authorization attributes configured on the AAA server, and how to send
accounting requests to the AAA server.

@author The onePK Team (onepk-feedback@cisco.com)
"""

import logging
import sys
from BaseTutorial import BaseTutorial
from onep.aaa import Attribute
from onep.aaa import OnepAAAAttributeType
from onep.aaa import Server
from onep.aaa import StringAttribute
from onep.aaa import User
from onep.core.exception import OnepException

logger = logging.getLogger("onep:AAATutorial")
logger.setLevel(logging.INFO)

class AAATutorial(BaseTutorial): pass

if __name__ == '__main__':
    tutorial = AAATutorial(sys.argv)

    if not tutorial.parse_command_line(False):
        logger.error("Error in parsing arguments")
        sys.exit(1)

    logger.info("******* CONNECT *******")
    try:

        #  In order for a user to be granted application-specific
        #  authorization, the application name specified here must match the
        #  application name in the attributes configured on the AAA server. It
        #  is important to use a name that uniquely identifies the application.
        #  AAA service set APIs require an established connection to the
        #  network element.
        #  START SNIPPET: connect_network_element
        tutorial.connect("com.cisco.onep.tutorials.aaa.AAATutorial")
        #  END SNIPPET: connect_network_element
    except OnepException as e:
        logger.error(e)
        sys.exit(1)

    logger.info("******* AUTHENTICATE *******")
    try:

        #  Instantiate a User that holds a AAA user's attributes. The AAA user
        #  is associated with one network element, and the association can be
        #  changed using set_network_element(). The AAA user must authenticate
        #  to the AAA server prior to using other AAA services. During
        #  authentication, the application can supply an optional list of
        #  attributes if required by the AAA server.
        #  START SNIPPET: onep_aaa_user_new
        aaaUser = User(tutorial.network_element,
                       tutorial.username,
                       tutorial.password)
        #  END SNIPPET: onep_aaa_user_new
    except OnepException as e:
        logger.error(e)
        tutorial.disconnect()
        sys.exit(1)
    try:
        #  START SNIPPET: onep_aaa_user_authenticate
        #  Authenticate without supplying any additional attributes.
        aaaAttributeList = aaaUser.authenticate(None)
        #  END SNIPPET: onep_aaa_user_authenticate
    except OnepException as e:
        logger.error(e)
        tutorial.disconnect()
        sys.exit(1)

    logger.info("Successfully authenticated user: " + aaaUser.username)

    logger.info("******* GET AAA SERVER INFO *******")

    #  We can get information about the AAA server that served the last
    #  request using this property.
    #  START SNIPPET: onep_aaa_user_get_last_used_server
    server = aaaUser.server
    logger.info("IP address: " + server.address)
    logger.info("Protocol: " + server.protocol)
    #  END SNIPPET: onep_aaa_user_get_last_used_server

    logger.info("******* GET AUTHORIZATION PROFILE *******")
    if len(aaaAttributeList) > 0:
        #  Accounting records may be sent manually unless auto-accounting is
        #  enabled for the user.
        #  START SNIPPET: aaa_accounting_sta
        if aaaUser.is_auto_acct_enabled:
            logger.info("Auto-accounting is enabled.")
        else:
            logger.info("Auto-accounting is not enabled.")
            try:
                aaaUser.send_accounting_record(
                    User.OnepAAAAcctAction.ONEP_AAA_ACCT_ACTION_START, None)
            except OnepException as e:
                logger.error(e)
        #  END SNIPPET: aaa_accounting_sta

    #  Get an action from the user.
    print "Possible actions are: [ walk | run | custom ]"
    while True:
        nextLine = raw_input(
            'Enter an action, or "quit" to end the application: ')

        if nextLine.lower() == "quit" or nextLine.lower() == "exit":
            break

        #  The only action allowed by default is "walk".
        #  All others require authorization.
        if not nextLine == "walk":
            try:

                #  Allowed actions are returned separate from the
                #  authorization profile. Here, we check if the user is allowed
                #  to perform the requested action.
                #  START SNIPPET: onep_aaa_user_is_action_authorized
                if not aaaUser.is_action_authorized(nextLine):
                    print "You are not allowed to perform this action."
                    continue
                #  END SNIPPET: onep_aaa_user_is_action_authorized
            except OnepException as e:
                logger.error(e)
                break

            #  Authorization passed.
            #  If the AAA server is configured with app-specific attributes,
            #  we can get them from the authorization profile. Here, we read
            #  the app attribute "custom" from the attribute list.
            #  START SNIPPET: onep_aaa_attr_list_get_app_attr_string
            if nextLine == "custom":
                for attribute in aaaAttributeList:
                    if (attribute.type_ ==
                            OnepAAAAttributeType.ONEP_AAA_AT_APP_ATTR
                            and attribute.name == "aaa-tutorial-custom"
                            and isinstance(attribute, StringAttribute)):
                        #  Print the message for the custom action.
                        print "You " + attribute.str_value
                        break
                else:
                    print "Custom action not found."
                continue
            #  END SNIPPET: onep_aaa_attr_list_get_app_attr_string

        #  Print the message for a non-custom action.
        print "You " + nextLine

    print "Goodbye!"

    logger.info("******* DISCONNECT AND CLEAN UP *******")

    #  When auto-accounting is enabled, accounting stops when the application
    #  disconnects from the network element. Otherwise, the application can
    #  manually send a "stop" request.
    if len(aaaAttributeList) > 0 and not aaaUser.is_auto_acct_enabled:
        try:
            #  START SNIPPET: aaa_accounting_stop
            aaaUser.send_accounting_record(
                nepAAAAcctAction.ONEP_AAA_ACCT_ACTION_STOP, None)
            #  END SNIPPET: aaa_accounting_stop
        except OnepException as e:
            logger.error(e)

    tutorial.disconnect()
