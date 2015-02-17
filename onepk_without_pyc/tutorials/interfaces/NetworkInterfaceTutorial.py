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
# 
 The goal of this tutorial is to show how to access Interfaces(ports/links), and their properties from a
 onePK-enabled Network Element.
 
  @author The onePK Team (onepk-feedback@cisco.com)
"""
import logging
from BaseTutorial import BaseTutorial
from onep.interfaces import InterfaceFilter
from onep.interfaces import NetworkInterface

InterfaceTypes = NetworkInterface.InterfaceTypes
logger = logging.getLogger('onep:NetworkInterfaceTutorial')
logger.setLevel(logging.INFO)

class NetworkInterfaceTutorial(BaseTutorial):
    
    def logInterfaceAddresses(self, networkInterfaces):
        addresses = None
        for networkInterface in networkInterfaces:
            addresses = networkInterface.get_address_list()
            for address in addresses:
                if address != None:
                    print "Interface - " + networkInterface.name + "\tAddress:" + address
                    
if __name__ == '__main__':
    """
        Invokes the tutorial via the command line. This main method attempts to use arguments from the command line.
    """
    import sys
    tutorial = NetworkInterfaceTutorial(sys.argv)
    logger.info("Reading arguments...")
    if not tutorial.parse_command_line():
        logger.error("Error in parsing arguments")
        sys.exit(1)

    try:
        if not tutorial.connect("NetworkInterfaceTutorial"):
            sys.exit(1)
        
        print "Connected to Network Element " + str(tutorial.get_element_hostname())
        
        network_element = tutorial.get_network_element()
        #  Get all Interfaces 
        networkInterfaces = network_element.get_interface_list(InterfaceFilter())
        print "\nPrinting all interfaces..."
        for networkInterface in networkInterfaces:
            print  "\t" + networkInterface.__str__()
                
        #  Get Ethernet Interfaces
        #START SNIPPET: getEthernetInterfaces
        filter = InterfaceFilter(None,InterfaceTypes.ONEP_IF_TYPE_ETHERNET) 
        networkInterfaces = network_element.get_interface_list(filter)
        print "\nPrinting all Ethernet interfaces..."
        for networkInterface in networkInterfaces:
            print "\t" + networkInterface.__str__()
        #END SNIPPET: getEthernetInterfaces
        
        #  Get Hardware properties of an interface 
        print "\nPrinting hardware properties of an interface..."
        #START SNIPPET: getInterfaceHardwareProperties
        intf = tutorial.get_an_interface()
        if intf == None:
            logger.error("No interfaces are available.")
            sys.exit(1)
        intfProperty = NetworkInterface.get_property(intf)
        print "\t" + intf.name + "\t Port" + str(intfProperty.port) + "\t Slot" + str(intfProperty.slot)
        #END SNIPPET: getInterfaceHardwareProperties
        
        #  Get Ethernet Interface status 
        print "\nStatus of an interface..."
        #START SNIPPET: getInterfaceStatus
        print "\t Interface " + intf.name + " status is " + str(intf.get_status())
        #END SNIPPET: getInterfaceStatus
        
        #  Get VRF (Virtual Routing Forwarding) name associated with the network interface 
        #print "\nVRF (Virtual Routing Forwarding) name associated of an interface..."
        #print "\t Interface " + intf.name + " VRF name is " + str(intf.get_vrf_name())        
        
        #  Get all interface config data 
        #print "\nPrinting all interfaces config data..."
        #START SNIPPET: getInterfaceConfigurations
	#NOT supported
        #for networkInterface in networkInterfaces:
        #    intfConfig = NetworkInterface.get_config(networkInterface)
        #    print "\t" + intfConfig.display_name
        #END SNIPPET: getInterfaceConfigurations 
        
        #  Get all parent interfaces
        print "\nPrinting all Parent interfaces..."
        #START SNIPPET: getParentInterfaces
        for networkInterface in networkInterfaces:
            parentIntf = networkInterface.get_parent()
            print "\t" + parentIntf.__str__()
        #END SNIPPET: getParentInterfaces
        
        #  Get all sub interfaces for all parent interfaces
        print "\nPrinting all subinterfaces..."
        #START SNIPPET: getSubInterfaces
        for networkInterface in networkInterfaces:
            parentIntf = networkInterface.get_parent()
            subIntfList = parentIntf.get_subinterface_list()
            for subIntf in subIntfList:
                print "\t" + subIntf.__str__()
        #END SNIPPET: getSubInterfaces
         
    except Exception, e:
        print e
    finally:
        print "Disconnecting from the Network Element"
        tutorial.disconnect()
        sys.exit(0)


