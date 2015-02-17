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
The goal of the BaseTutorial is to show how to create an application and connect to a network element to obtain a
session handle. The BaseTutorial provides base class functions for reading test properties, parsing command line
properties, and network element connectivity.

@author The onePK Team (onepk-feedback@cisco.com)

"""
from onep.element.NetworkApplication import NetworkApplication
from onep.interfaces import InterfaceStatus
from onep.element import SessionConfig
from onep.interfaces import NetworkInterface

import getopt
import sys
import getpass
import onep.interfaces.InterfaceFilter
import os
import socket
from onep.core.util import tlspinning
#  START SNIPPET: createLogger
import logging
logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger('onep:BaseTutorial')
logger.setLevel(logging.INFO)
#  END SNIPPET: createLogger

class BaseTutorial(object):
    #  START SNIPPET: variables
    element_hostname = None
    username = None
    password = None
    transport = "tls"
    network_element = None
    session_handle = None
    root_cert_path = None
    client_cert_path = None
    client_key_path = None
    key_passphrase = None
    tls_pinning_file = None
    
    args = None
    #  END SNIPPET: variables

    def __init__(self, args):
        """
        Instantiates the Logger instance using the classname of the implementing class.
        """
        self.args = args

    def connect(self, applicationName):
        """
        Obtains a NetworkApplication instance, sets the name to applicationName,
        gets a network element for the hostname or address in the command line
        arguments or tutorial.properties file and then tries to connect to the
        Network Element with the username and password supplied, or from the
        tutorial.properties file.
        
        @param applicationName: The NetworkApplication name is set to this value.
        @return True if the connection succeeded without exception, else false.
        @throws OnepException
        """
        
        #  START SNIPPET: init_myapp
        network_application = NetworkApplication.get_instance()
        #  END SNIPPET: init_myapp
        
        #  START SNIPPET: name_myapp   
        network_application.name = applicationName
        #  END SNIPPET: name_myapp
        
        #  START SNIPPET: get_ne_opt1
        self.network_element = network_application.get_network_element(self.element_hostname)
        #  END SNIPPET: get_ne_opt1
        if self.network_element == None:
            logger.error("Failed to get network element")
            sys.exit(1)

        logger.info("We have a NetworkElement : " + self.network_element.__str__())
        
        #  START SNIPPET: connect
        session_config = SessionConfig(SessionConfig.SessionTransportMode.TLS) #default is TLS
        if self.transport.lower() == "tipc" or self.transport == "2":
            session_config = SessionConfig(SessionConfig.SessionTransportMode.TIPC)

        #Set all the TLS properties in session_config
        session_config.ca_certs = self.root_cert_path
        session_config.keyfile = self.client_key_path
        session_config.certfile = self.client_cert_path
        session_config.set_tls_pinning(self.tls_pinning_file, PinningHandler(self.tls_pinning_file))

        self.session_handle = self.network_element.connect(self.username, self.password, session_config)
        #  END SNIPPET: connect
        
        if self.session_handle == None:
            #  START SNIPPET: loggerError
            logger.error("Failed to connect to NetworkElement - ")
            #  END SNIPPET: loggerError
            return False
        logger.info("Successful connection to NetworkElement - " )
        return True

    def disconnect(self):
        """
        Disconnects the application from the Network Element.
        
        @return True if the disconnect succeeded without an exception, else false if the application failed to disconnect
        from the Network Element.
        """
        try:
            if self.network_element.is_connected():
                self.network_element.disconnect()
        except Exception, e:
            logger.error("Failed to disconnect from Network Element")
            logger.error(e)
            return False
        return True

    def get_element_hostname(self):
        """
        Gets the IP address or hostname of the Network Element we are interested in.
        
        @return The element_hostname.        
        """
        return self.element_hostname


    #  START SNIPPET: getLogger
    def get_logger(self):
        """
        Implements the logger, which sends all enabled log messages.
        
        @return The logger.
        """
        return self.logger
    #  END SNIPPET: getLogger
    

    def get_network_element(self):
        """
        Gets the NetworkElement that is being connected to by the application.
        
        @return The NetworkElement that is being connected to by the application.
        """
        return self.network_element

    def get_session_handle(self):
        """
        Gets the session_handle that identifies the connection to this Network Element.
        
        @return The session_handle that identifies the connection to this NetworkElement.
        """
        return self.session_handle

    def get_username(self):
        """
        Gets the username on whose behalf the connection will be made. The username is specified via the command line or
        in the tutorial.properties file.
        
        @return The username that is specified via the command line or in the tutorial.properties file.
        """
        return self.username
    
    def get_password(self):
        """
        Gets the password with which connection will be made. The password is specified via the command line or
        in the tutorial.properties file.
        
        @return The password that is specified via the command line or in the tutorial.properties file.
        """
         
        return self.password
    
    def get_transport(self):
        """
        Gets the transport mode with which connection will be made. The transport is specified via the command line or
        in the tutorial.properties file.
        
        @return The transport that is specified via the command line or in the tutorial.properties file.
        """
        return self.transport
    
    def get_usage(self):
        return " Usage: -a <address or FQDN> [-t <transport>] [-C <client cert file>] \n [-K <client private key file>] \n [-R <root certificates file>] \n [-P <tls pinning file>]"

    def parse_command_line(self, skip_login_for_tipc=True):
        """
        Parse the command line options.

        @param args  The args string passed into the main(...) method.
        
        @return true if parsing the command line succeeds, false otherwise.
        """
        try:
            opts, args = getopt.getopt(self.args[1:],"ha:t:R:C:K:P:",["hostname=","transport=", "rootcert=", "clientcert=", "key=", "tlspinningfile="])
        except getopt.GetoptError as err:
            print str(err)
            logger.info(self.get_usage())
            sys.exit(2)
        
        """
         * options:
         *       -a, --hostname <network element address or FQDN>
         *       -t, --transport <transport type> default is tls
         *       -C, --clientcert <client certificate file>
         *       -K, --clientkey <client private key file>
         *       -R, --rootcert <root certificates file>
         *       -P, --pinfile <tls pinning file>
        """     
        for option, arg in opts:
            if option == '-h':
                logger.info(self.get_usage())
                sys.exit()
            elif option in ("-a", "--hostname"):
                self.element_hostname = arg
            elif option in ("-t", "--transport"):
                self.transport = arg
            elif option in ("-R", "--rootcert"):
                self.root_cert_path = arg
            elif option in ("-C", "--clientcert"):
                self.client_cert_path = arg
            elif option in ("-K", "--key"):
                self.client_key_path = arg
            elif option in ("-P", "--pinfile"):
                self.tls_pinning_file = arg
        
        if self.element_hostname == None:
            logger.error(self.get_usage())
            return False

        if self.transport != "tipc" or not skip_login_for_tipc:
            self.username = raw_input('Enter Username : ')
            self.password = getpass.getpass('Enter Password : ')
            if self.username == None or self.password == None:
                logger.error("Username and password are required.")
                return False
        
        return True

    def set_element_hostname(self, element_hostname):
        """
        """
        self.element_hostname = element_hostname

    def set_logger(self, logger):
        """
        """
        self.logger = logger

    def set_network_element(self, network_element):
        """
        """        
        self.network_element = network_element

    def set_password(self, password):
        """
        """        
        self.password = password

    def set_session_handle(self, session_handle):
        """
        """        
        self.session_handle = session_handle

    def set_username(self, username):
        """
        """        
        self.username = username

    def get_all_interfaces(self):
        """
        """        
        interfaceList = None
        try:
            interfaceList = self.network_element.get_interface_list(onep.interfaces.InterfaceFilter())
        except Exception, e:
            logger.error(e)
        return interfaceList

    def get_an_interface(self, address_required = True):
        """
          Gets an Ethernet interface which is not the interface that the application is connected to.
          If address_required is true looks for interface which has IP address set. 
        """
        interfaceList = None
        networkInterface = None
        try:
            interfaceList = self.network_element.get_interface_list(onep.interfaces.InterfaceFilter())
            elemAddress = socket.gethostbyname(self.network_element.host_address)
            for networkInterface in interfaceList:
                if networkInterface.interface_type == NetworkInterface.InterfaceTypes.ONEP_IF_TYPE_ETHERNET:
                    addresses = networkInterface.get_address_list()
                    if (addresses or not address_required) and elemAddress not in addresses:
                        return networkInterface
        except Exception, e:
            logger.error(e)
        logger.info('No interface with IP address present.')
        return None
 

    def get_an_up_interface(self):
        """
          Get an interface which has its LINK status as UP
        """
        interfaceList = None
        networkInterface = None
        try:
            interfaceList = self.network_element.get_interface_list(onep.interfaces.InterfaceFilter())
            for networkInterface in interfaceList:
                if networkInterface.get_status().link == InterfaceStatus.InterfaceState.ONEP_IF_STATE_OPER_UP:
                    return networkInterface                          
        except Exception, e:
            logger.error(e)
        return None 
    
class PinningHandler(tlspinning.TLSUnverifiedElementHandler):
    
    def __init__(self, pinning_file):
        self.pinning_file = pinning_file
        
    def handle_verify(self, host,hashtype, finger_print, changed):
        """
        Callback to the app to determine whether to add a host to pinning DB
        Upon receipt of a certificate which fails to match based on server-name or
        IP address, and for which there is no match in the pinning database,
        this callback asks the application whether to accept the
        connection and/or whether to add the server to the pinning database. 
        By default, the connection will be terminated and the pinning db will
        remain unchanged.
        """
        if  changed:
            msg = "\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n"
            msg +="WARNING: THE CERTIFICATE PRESENTED BY REMOTE HOST '%s'\n IS DIFFERENT FROM THE ONE PREVIOUSLY ACCEPTED" %(host)
            msg +="\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
        else:
            msg = "WARNING: Certificate presented by remote host '%s' is not verified."%(host)

        msg += "\n\nThe %s fingerprint sent by the remote host(%s) is:\n%s" %(hashtype, host, finger_print)
        msg += "\n\nYou MUST verify the certificate on remote host before proceeding! \n"
        msg += "\nChoose from following options:"

        if self.pinning_file:
            prompt = "\nAccept and Pin (p), Accept Once (o), Reject (r) (default) :"
        else:
            prompt = "\nAccept Once (o), Reject (r) (default) :"
        sys.stdout.write(msg)
        self.decision = raw_input(prompt)
        
        while True:
            if not self.decision or self.decision.lower() == 'r':
                return tlspinning.DecisionType.REJECT
            elif self.decision.lower() == 'p' and self.pinning_file:
                return tlspinning.DecisionType.ACCEPT_AND_PIN
            elif self.decision.lower() == 'o':
                return tlspinning.DecisionType.ACCEPT_ONCE
            else:
                self.decision = raw_input(prompt)
    

        
if __name__ == '__main__':
    tutorial = BaseTutorial(sys.argv)
    
    logger.info("Reading arguments...")
    if not tutorial.parse_command_line():
        logger.error("Error in parsing arguments")
        sys.exit(1)
    
    logger.info("Connecting to Network Element...")
    #try:
    tutorial.connect("BaseTutorial")
    #except Exception, e:
        #logger.error("Error in connecting to network element - %s", e)
    #logger.error(e)
        
    tutorial.disconnect()
    logger.info("Done.")
    
