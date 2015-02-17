#! /usr/bin/env python

# *------------------------------------------------------------------
# * sample.py  
# *
# * Cisco ONE-P Python SDK
# *
# * Copyright (c) 2011-2014 by Cisco Systems, Inc.
# * All rights reserved.
# *------------------------------------------------------------------
# *

import logging
import getopt
import sys
import getpass
from onep.element import NetworkElement
from onep.element import SessionConfig

logging.basicConfig(level=logging.WARNING)

element_address = None
username = None
password = None
transport = "tls"
network_element = None
session_handle = None
root_cert_path = None
client_cert_path = None
client_key_path = None

# Must have a Cisco network device capable of communicating
# with ONE-P APIs.  Network Element must also have onep
# configured with the socket transport and have the correct
# onep services activated.  A network interface must be
# configured with a valid IP address and pingable.

def parse_command_line(args):
    """
    Parse the command line options. If the required argument "-a" for element address or FQDN is not provided,
    this method displays the proper usage information and calls sys.exit(1).

    @param args  The args string passed into the main(...) method.
    
    @return true if parsing the command line succeeds, false otherwise.
    """
    try:
        opts, args = getopt.getopt(args[1:],"ha:t:R:C:K:",["address=","transport=", "rootcert=", "clientcert=", "key="])
    except getopt.GetoptError as err:
        print str(err)
        logger.info(get_usage())
        sys.exit(2)
    
    """
     * options:
     *       -a, --address <network element address or FQDN>
     *       -t, --transport <transport type> default is tls
     *       -C, --clientcert <client certificate file>
     *       -K, --clientkey <client private key file>
     *       -R, --rootcert <root certificates file>
    """     
    for option, arg in opts:
        if option == '-h':
            logger.info(get_usage())
            sys.exit()
        elif option in ("-a", "--address"):
            global element_address
            element_address = arg
        elif option in ("-t", "--transport"):
            global transport
            transport = arg
        elif option in ("-R", "--rootcert"):
            global root_cert_path
            root_cert_path = arg
        elif option in ("-C", "--clientcert"):
            global client_cert_path
            client_cert_path = arg
        elif option in ("-K", "--key"):
            global client_key_path
            client_key_path = arg
    global username
    username = raw_input('Enter Username : ')
    global password
    password = getpass.getpass('Enter Password : ')
    
    if(element_address==None):
        logger.error(get_usage())
        return False
    
    return True
    
def get_usage():
        return " Usage: -a <address or FQDN> [-t <transport>] [-C <client cert file>] \n [-K <client private key file>] \n [-R <root certificates file>]"

def sampleapp():
    appname = raw_input('Enter name of application : ')

    session_config = SessionConfig(SessionConfig.SessionTransportMode.TLS) #default is TLS
    if transport.lower() == "tipc" or transport == 2:
        session_config = SessionConfig(SessionConfig.SessionTransportMode.TIPC)

    session_config.ca_certs = root_cert_path
    session_config.certfile = client_cert_path
    session_config.keyfile = client_key_path
    
    ne = NetworkElement(element_address, appname)
    con = ne.connect(username, password, session_config)
    print 'Connected to host'
    
    print "System Name:            ", ne.properties.sys_name
    print "System Uptime:          ", ne.properties.sys_uptime
    print "Total System Memory:    ", ne.total_system_memory
    print "Free System Memory:     ", ne.free_system_memory
    print "System CPU Utilization: ", ne.system_cpu_utilization, "%\n"
    print "System Connect Time:    ", ne.get_connect_time()
    print "System Disconnect Time:  ", ne.get_disconnect_time()
    print "System __str__ Method:  ", ne
    print "Host Content String:\n",   ne.properties.content_string
    
    ne.disconnect()

if __name__=='__main__':
    logger = logging.getLogger('onep')
    logger.setLevel(logging.INFO)
    if not parse_command_line(sys.argv):
        logger.error("Error in parsing arguments")
        sys.exit(1)
    sampleapp()
