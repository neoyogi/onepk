#!/usr/bin/env python

# 
#  Copyright (c) 2010-2013, Cisco Systems, Inc.
#
#  THIS SAMPLE CODE IS PROVIDED "AS IS" WITHOUT ANY EXPRESS OR IMPLIED WARRANTY
#  BY CISCO SOLELY FOR THE PURPOSE of PROVIDING PROGRAMMING EXAMPLES.
#  CISCO SHALL NOT BE HELD LIABLE FOR ANY USE OF THE SAMPLE CODE IN ANY
#  APPLICATION.
#
#  Redistribution and use of the sample code, with or without
#  modification, are permitted provided that the following conditions
#  are met:
#  Redistributions of source code must retain the above disclaimer.
#
#  
"""
Session Tutorial
 
This tutorial is intended for application developers who need to specify configuration parameters for
connections made between onePK applications and network elements.
 
In onePK, a session represents an authenticated channel of communication
between an application and a network element. This tutorial shows
how to configure a session, how to get the properties and statistics of a
session.
@author The onePK Team (onepk-feedback@cisco.com)
"""
import logging
from BaseTutorial import BaseTutorial
from onep.element import NetworkElement
from onep.element import NetworkApplication
from onep.element import SessionConfig
from onep.element import SessionHandle
from onep.element import SessionStatistics
from onep.element import SessionProperty
from onep.element import ConnectionListener
from onep.core.exception import OnepException
from onep.core.util import tlspinning

logger = logging.getLogger('onep:SessionTutorial')
logger.setLevel(logging.INFO)

class SessionTutorial(BaseTutorial):
    
    @classmethod
    def createSessionConfig(self, mode):
        """
        Creates an instance of SessionConfig with the given transport mode and
        sets the reconnect timer to one minute. All other attributes are set to
        their default values.

        When connecting to a network element, the caller may optionally provide a
        SessionConfig that contains the desired configuration for the resulting
        session. When creating the SessionConfig, the only required attribute is
        the transport mode. TLS is the transport mode used for the end node
        hosting model. TIPC (sometimes referred to as LOCAL) may be used in
        process and blade hosting models. All other attributes are optional,
        and will take on their default values if not explicitly set. To
        demonstrate reconnecting to the session, the reconnect timer will be set
        to one minute.

        @param mode The transport mode used by the connection.
        @return a SessionConfig instance.
        """
        
        #  START SNIPPET: create_session_config
        #  Construct a SessionConfig instance with the given transport mode. 
        config = SessionConfig(mode)
        #  Set the reconnect timer to one minute. 
        config.reconnectTimer = 60
        #  The session attributes below this point are set to their default
        #  values.
        #          
        #  Set the port to connect to on the network element.
        #  TLS      15002
        #  TIPC     N/A
        #          
        if mode.lower() == "tls":
            config.port = config.DEFAULT_PORT
            config.transportMode = SessionConfig.SessionTransportMode.TLS
            config.ca_certs = tutorial.root_cert_path
            config.keyfile = tutorial.client_key_path
            config.certfile = tutorial.client_cert_path
        else:
            #  Not required for TIPC.
            pass
        #  Set the event queue size of the session. 
        config.eventQueueSize = config.DEFAULT_EVENT_QUEUE_SIZE
        #  Set the event thread pool size of the session. 
        config.eventThreadPool = config.DEFAULT_THREADPOOL_SIZE
        #  Set the event drop mode of the session. 
        config.eventDropMode = config.DEFAULT_EVENT_DROP_MODE
        #  Set the keepalive attributes of the session. 
        #  Idle time in seconds 
        config.keepAliveIdleTime = config.DEFAULT_KEEPALIVE_IDLE_TIME
        #  Interval between keepalives in seconds 
        config.keepAliveInterval = config.DEFAULT_KEEPALIVE_INTERVAL
        #  Number of keepalives 
        config.keepAliveRetryCount = config.DEFAULT_KEEPALIVE_RETRY_COUNT
        #  END SNIPPET: create_session_config
        config.set_tls_pinning(tutorial.tls_pinning_file, PinningHandler(tutorial.tls_pinning_file))
        return config

    def connectWithConfig(self, applicationName, config):
        """
        Initializes the network application. Then, gets the network element and
        connects to it with the given session configuration.

        @param applicationName  The unique name of this application.
        @param config           Configuration options instance.
        @return SessionHandle   The handle of the connected session, or
                                null if there was an error.
        @throws OnepException   If there was an error in executing a onePK
                                call.
        """
        
        #  Get the NetworkApplication instance. 
        networkApplication = NetworkApplication.get_instance()
        #  Set the name of the application to applicationName. 
        networkApplication.name = applicationName
        #  Get the network element's address or hostname passed in from the
        #  command line or the properties file.
        #          
        element_hostname = tutorial.get_element_hostname()
        #  Get the NetworkElement instance at the given hostname. 
        networkElement = networkApplication.get_network_element(element_hostname)
        logger.info("Got a NetworkElement - %s ", networkElement)
        #  Set the network element for this tutorial. 
        tutorial.set_network_element(networkElement)
        #  Connect to the element using the given session configuration. If no
        #  configuration is specified by the caller (i.e. null is used), the
        #  session will take on the default values.
        #          
        #  START SNIPPET: onep_element_connect
        handle = networkElement.connect(tutorial.get_username(), tutorial.get_password(), config)
        #  END SNIPPET: onep_element_connect
        logger.info("Successfully connected to NetworkElement - %s", tutorial.get_network_element())
        return handle

    def printSessionProperties(self, config,handle):
        """
        Prints the session properties to the logger.

        @param handle  The handle to the session to print the properties
                       for.
        """
        
        #  START SNIPPET: print_session_properties
        #  Get the property instance for this session using the
        #  session handle.
        # 
        property = handle.sessionProp
       
        #  Get the port number the session is connected on. 
        logger.info("Port: " + str(property.port))
        #  Get the event queue size of the session. 
        logger.info("EventQueueSize: " + str(property.eventQueueSize))
        #  Get the event thread pool size of the session. 
        logger.info("EventThreadPool: " + str(property.eventThreadPool))
        #  Get the event drop mode of the session. 
        logger.info("EventDropMode: " + str(property.eventDropMode))
        #  Get the reconnect timer of the session in seconds. 
        logger.info("ReconnectTimer: " + str(property.reconnectTimer))
        #  Get the transport mode of the session. 
        logger.info("TransportMode: " + str(property.transportMode))
        #  END SNIPPET: print_session_properties

    def printSessionStatistics(self, handle):
        
        #  START SNIPPET: print_session_statistics
        #  Get the statistics instance for this session using the
        #  session handle.
        #          
        statistics = handle.sessionStat
        #  Get the count of events received and dropped. 
        logger.info("Events Total: %s", statistics.eventTotalCount)
        logger.info("\nEvents Dropped: %s", statistics.eventDropCount)
        #  END SNIPPET: print_session_statistics

    def simulate_disconnect(self):
        '''
        Internal function for testing tutorial reconnect

        '''
        self.get_network_element()._reconnect_waiting = True
        self.get_network_element().disconnect()


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
        @param host: String containing either the FQDN or 
        a text version of the IP address
        @param hashtype: If there was a host name with a non-matching 
        certificate, this will be the hash-type from that entry. 
        If there was no entry, this will be created  as "SHA-1".
        @param finger_print: Fingerprint text created from the certificate. 
        This will be a series of hex bytes separated by 
        colons of the form "A1:B2:C3:..."
        @changed: changed is TRUE if there was an existing entry in the database
        but the certificate does not match. FALSE indicates that there was
        no entry in the database for this host.
        @return: ACCEPT_AND_PIN if onep should both accept
        the connection and add the entry to the pinning database.
        ACCEPT_ONCE if onep should only accept the connection 
        but not add the entry to the pinning database.
        REJECT if onep should neither accept the connection 
        nor add the entry to the pinning database.
        """
#  START SNIPPET: pin_handler
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
#  END SNIPPET: pin_handler

class TutorialReconnectListener(ConnectionListener):
    '''
    Build a listener class to react to application connection
    events.  The connection listener will be registered directly
    to the instantiated NetworkElement class.

    In this example we have setup a log to send messages to the
    application logger.  We have also added a maximum reconnect
    retry count and a flag to tell the listener when the application
    wants to exit without a reconnect attempt.

    '''
# START SNIPPET: reconnect
    log = logging.getLogger('onep:SessionTutorial')
    log.setLevel(logging.INFO)
    retry = 3
    app_terminate = False

    def handle_event(self, event, data):

        self.log.info("\n********* CONNECT LISTENER *******")
        self.log.info('Received connection event %s',
                      event.elem.OnepSessionState.enumval(event.state))

        if self.app_terminate:
            self.log.info("\n********* TUTORIAL TERMINATED *******")
            return

        if event.state == event.elem.OnepSessionState.ONEP_STATE_DISCONNECTED:
            if not self.retry:
                self.log.info("\n********* RECONNECT RETRY MAX FOR %d *******" % data['id'])
                event.elem.set_connection_listener(None, None)
                return
            try:
                self.log.info("\n********* RECONNECT SESSION %d *******" % data['id'])
                event.elem.reconnect(data['user'], data['pwd'],
                                     data['id'], data['sess'])
            except Exception as e:
                self.retry -= 1
                self.log.info("\n********* RECONNECT FAILED SESSION %d*******" %data['id'])
                self.log.info("\n********* %s *******" % str(e))
# END SNIPPET: reconnect
            
if __name__ == '__main__':
    import sys
    tutorial = SessionTutorial(sys.argv)
    #  Parse arguments from command line or properties file. 
    if not tutorial.parse_command_line():
        logger.error("Error in parsing arguments")
        sys.exit(1)
        
    #  Create a session configuration with transport mode socket. 
    config = tutorial.createSessionConfig(tutorial.get_transport())
    logger.info("\n********* INITIALIZE AND CONNECT *******")
    #  Connect to the network element using the given configuration. 
    originalSessionHandle = None
    try:
        originalSessionHandle = tutorial.connectWithConfig("Session Tutorial", config)
    except OnepException as e:
        logger.error("Failed to connect to element.", e)

    #  Upon a successful connection, a session is established and a handle
    #  is returned in the form of a SessionHandle. When a session is in the
    #  connected state, its configuration cannot be modified. The session
    #  handle may be used to query information about the session. Here, we
    #  use it to get the session's ID, which will be needed when we want to
    #  reconnect to the session.
    #          
    #  START SNIPPET: onep_session_handle_get_id
    sessionID = originalSessionHandle._id
    #  END SNIPPET: onep_session_handle_get_id
    logger.info("Connected to network element with session ID: " + str(sessionID))
    logger.info("\n********* PRINT SESSION PROPERTIES *******")
    tutorial.printSessionProperties(config,originalSessionHandle)
    logger.info("\n********* PRINT SESSION STATISTICS *******")
    tutorial.printSessionStatistics(originalSessionHandle)
    logger.info("\n********* SETUP CONNECT LISTENER *******")
    # START SNIPPET: reconnect_setup
    con_listener = TutorialReconnectListener()
    tutorial.get_network_element().set_connection_listener(con_listener,
                                                           {'user': tutorial.get_username(),
                                                            'pwd': tutorial.get_password(),
                                                            'id': sessionID,
                                                            'sess' : config})
    # END SNIPPET: reconnect_setup
    logger.info("\n********* SIMULATE INTERRUPTION OF CONNECTION *******")
    tutorial.simulate_disconnect()
    logger.info("\n********* DISCONNECT AND CLEAN UP *******\n\n")
    con_listener.app_terminate = True
    tutorial.disconnect()


