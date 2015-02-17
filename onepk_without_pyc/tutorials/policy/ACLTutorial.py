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
  This tutorial shows how a Connected Application can create an Access Control List in a Network Element.
  It shows how to create an L3 ACL, and create an L3 ACE with TCP protocol.
  The ACE will then be added to the ACL which will be applied an interface.
  In this example the first interface connected to the network element will be used.
  Results could be verified on the network element using the following commands:
   #show ip access-list dynamic
   #show ip interface <interface_name> | include access 
  
  package: tutorials.policy

"""

import sys
import getopt, getpass
from BaseTutorial import BaseTutorial
from onep.core.util import OnepConstants
from onep.policy import Acl, L3Acl, L3Ace

import logging
logger = logging.getLogger('onepACLTutorial')
logger.setLevel(logging.ERROR)

class ACLTutorial(BaseTutorial):
    
    TWENTY_SEC = 20
    SEQUENCE_NUMBER = 10

    def parse_command_line_acl(self):
        
        #super(ApplicationManagementTutorial, self).parse_command_line(args)
        base_usage_msg = tutorial.get_usage()
        usage_message_applmgmt = base_usage_msg + '\n [-i <interface>]'
        try:
            opts, args = getopt.getopt(self.args[1:],"ha:i:t:R:C:K:P:",["hostname=","interface=","transport=", "rootcert=", "clientcert=", "key=", "tlspinningfile="])
        except getopt.GetoptError as err:
            print str(err)
            logger.info(usage_message_applmgmt)
            sys.exit()
        for option, arg in opts:
            if option == '-h':
                logger.info(usage_message_applmgmt)
                sys.exit()
            elif option in ("-a", "--hostname"):
                tutorial.element_hostname = arg
            elif option in ("-t", "--transport"):
                tutorial.transport = arg
            elif option in ("-i", "--interface"):
                tutorial.interface_name = arg
            elif option in ("-R", "--rootcert"):
                tutorial.root_cert_path = arg
            elif option in ("-C", "--clientcert"):
                tutorial.client_cert_path = arg
            elif option in ("-K", "--key"):
                tutorial.client_key_path = arg
            elif option in ("-P", "--pinfile"):
                tutorial.tls_pinning_file = arg
        tutorial.username = raw_input('Enter Username : ')
        tutorial.password = getpass.getpass('Enter Password : ')
        
        if(tutorial.element_hostname is None or tutorial.username is None or tutorial.password is None):
            logger.error(usage_message_applmgmt)
            return False
        return True

if __name__ == '__main__':
    """
    Invokes the tutorial via the command line. This main method attempts to use arguments from the command line.
    """
    tutorial = ACLTutorial(sys.argv)
    tutorial.interface_name = None
    tutorial.network_interface = None
    logger.info("Reading arguments ...")
    if not tutorial.parse_command_line_acl():
        logger.error("Error in parsing arguments")
        sys.exit(1)
    try:
        logger.info("Connecting to Network Element...")
        if not tutorial.connect("ACLTutorial"):
            logger.error("Error in connecting to network element")
            sys.exit(1)

        print "Connected to Network Element " + str(tutorial.get_element_hostname())  
        
        networkElement = tutorial.get_network_element()      

        # START SNIPPET: createAcl
        #  Create a L3 IPv4 Access Control List
        l3_acl = L3Acl(networkElement, OnepConstants.OnepAddressFamilyType.ONEP_AF_INET, 0)
        # END SNIPPET: createAcl

        #  Create Access Control Element
        # START SNIPPET: createAccessControlElement
        # Creates a new Access Control Element w/ Sequence Number 10 and this will "permit" the following conditions.
        l3_ace = L3Ace(tutorial.SEQUENCE_NUMBER, True)
        # Protocol value must be a number between 0 and 256.
        # 256 = All protocols   6 =  TCP
        l3_ace.protocol = 6
        
        value = [l3_ace.TcpFlags.ONEP_TCP_URG, 
                     l3_ace.TcpFlags.ONEP_TCP_SYN]
        mask  = [l3_ace.TcpFlags.ONEP_TCP_FIN, 
                 l3_ace.TcpFlags.ONEP_TCP_SYN, 
                 l3_ace.TcpFlags.ONEP_TCP_PSH, 
                 l3_ace.TcpFlags.ONEP_TCP_ACK]
        match = l3_ace.TcpFlagMatch.ONEP_MATCH_ALL  
        
        l3_ace.set_tcp_flags(value, mask, match)
        # Permit any source prefix
        l3_ace.set_src_prefix_any()
        # Permit any destination prefix
        l3_ace.set_dst_prefix_any()            
        # Set the value of the DSCP field        
        l3_ace.set_dscp(OnepConstants.OnepDscp.ONEP_DSCP_CS1)
        # Log the Access Control Element    
        l3_ace.set_log_flag(l3_ace.log_flag.ONEP_ACL_LOG_NORMAL)
        #END SNIPPET: createAccessControlElement
        
        #  START SNIPPET: addACEtoACL
        #  Add Access Control Element to Access Control List
        l3_acl.add_ace(l3_ace)
        #  END SNIPPET: addACEtoACL
        
        #  Apply Access Control Element to Interface  
        print '\n', str(l3_ace)
        if tutorial.interface_name:
            try:
                print 'trying to get interface ' + str(tutorial.interface_name)
                tutorial.network_interface = tutorial.get_network_element().get_interface_by_name(tutorial.interface_name)
            except Exception as e:
                logger.error('Could not get interface ' + str(tutorial.interface_name))
                raise e
        if tutorial.network_interface is None:
            print 'Getting an interface'
            tutorial.network_interface = tutorial.get_an_interface(address_required = False)
        if tutorial.network_interface is None:
            logger.error("Could not apply ACL to an interface")
            sys.exit(1)
        
        # START SNIPPET: applyAcl
        l3_acl.apply_to_interface(tutorial.network_interface, Acl.Direction.ONEP_DIRECTION_IN)
        #  END SNIPPET: applyAcl
        
        print "Applied ACL to interface = " + tutorial.network_interface.name
        print str(l3_acl)
        print "Verify on network element that the ACL has been successfully applied."
        
        raw_input('Enter to continue and remove the ACL')
        print "\nRemoving ACL from interface..."
        #  START SNIPPET: removeAcl
        #  Remove Access Control Element from ACL.
        l3_acl.remove_ace(l3_ace)
        #  Remove ACL from interface. 
        l3_acl.delete_acl()
        #  END SNIPPET: removeAcl
    except Exception as e:
        print e
    finally:
        print "Disconnecting from the Network Element"
        tutorial.disconnect()
        sys.exit(0)

