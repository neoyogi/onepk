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
 This tutorial shows how to access and manipulate the interfaces addresses of a Network Element.
 As a example to show how setAddress works, this tutorial gets an interface and sets the interface
 address to the first address in the address list for the interface.
 Note that it is not recommended to set the address to an arbitrary value,
 as that may lead to loss of connectivity.
 @author The onePK Team (onepk-feedback@cisco.com)
"""

import logging
from BaseTutorial import BaseTutorial
from onep.core.util import OnepConstants
from onep.core.util import HostIpCheck

OnepAddressScopeType = OnepConstants.OnepAddressScopeType
logger = logging.getLogger('onep:InterfaceAddressTutorial')
logger.setLevel(logging.INFO)

class InterfaceAddressTutorial(BaseTutorial):

    """
     Gets all addresses for all interfaces and logs them.
    """
    # START SNIPPET: interfaceAddresses
    def logInterfaceAddresses(self, networkInterfaces):
        print "\nPrinting interface address..."
        addresses = None
        for networkInterface in networkInterfaces:
            addresses = networkInterface.get_address_list()
            for address in addresses:
                if address != None:
                    print "Interface - " + networkInterface.name + "\tAddress:" + address
    #END SNIPPET: interfaceAddresses
    
    """
     Gets all prefixes for all interfaces and logs them.
    """
    #START SNIPPET: interfacePrefixes                     
    def logInterfacePrefixes(self, networkInterfaces):
        print "\nPrinting interface prefix..."
        prefixes = None
        for networkInterface in networkInterfaces:
            prefixes = networkInterface.get_prefix_list()
            for prefix in prefixes:
                if prefix != None:
                    print "Interface - " + networkInterface.name + "\tPrefix:" + str(prefix.prefix_length)
    #END SNIPPET: interfacePrefixes
    
    """
      * Gets an interface and sets the interface address to the first address in the address list for the interface.
      * Note that it is not recommended to set the address to an arbitrary value, as that may lead to loss of
      * connectivity.
      * @throws OnepException
      *             If there is an error.
    """
    #START SNIPPET: setInterfaceAddress
    def setInterfaceIPAddress(self, networkInterface):
        if networkInterface == None:
            logger.error("No interfaces are available.")
            return None
        setPrefix = 24;
        setAddr = None
        
        prefixes = networkInterface.get_prefix_list()
	for prefix in prefixes:
		if prefix:
			setPrefix = prefix.prefix_length
			setAddr = prefix.address
			if HostIpCheck(setAddr).is_ipv4():
				print "\nSetting IPv4 address of interface " + networkInterface.name
				networkInterface.set_address(1,OnepAddressScopeType.ONEP_ADDRESS_IPv4_PRIMARY,setAddr,setPrefix)
				print "Successfully set the IP address of interface " + networkInterface.name 
				print " to " + setAddr + " prefix " + str(setPrefix)
			break
    #END SNIPPET: setInterfaceAddress
                                   
if __name__ == '__main__':
    """
        Invokes the tutorial via the command line. This main method attempts to use arguments from the command line.
    """
    import sys
    tutorial = InterfaceAddressTutorial(sys.argv)
    logger.info("Reading arguments...")
    if not tutorial.parse_command_line():
        logger.error("Error in parsing arguments")
        sys.exit(1)
    try:
        logger.info("Connecting to Network Element...")
        if not tutorial.connect("InterfaceAddressTutorial"):
            logger.error("Error in connecting to network element")
            sys.exit(1)
 
        print "Connected to network element " + tutorial.get_element_hostname()
        
        tutorial.logInterfaceAddresses(tutorial.get_all_interfaces())
        tutorial.logInterfacePrefixes(tutorial.get_all_interfaces())
        tutorial.setInterfaceIPAddress(tutorial.get_an_interface())       
    except Exception, e:
            print e
    print "Disconnecting from the Network Element"
    tutorial.disconnect()
    sys.exit(0)
