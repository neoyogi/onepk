__author__ = 'yogesh'
from onep.element import SessionConfig
from onep.element.NetworkApplication import NetworkApplication
import argparse
import logging, os, sys
import ConfigParser


class onepbase(object):
    element_hostname = None
    username = None
    password = None
    transport = "tls"
    network_element = None
    session_handle = None
    root_cert_path = None
    application_name = None
    parser = None
    properties_config = None
    properties = dict()
    loglevel = None

    def __init__(self):
        self.parse_arguments()
        self.set_loggers("onep")
        self.setConfigProperties(property_file="properties.conf")
        self.connection_status = self.connect(self.application_name)
        if self.connection_status is False:
            sys.exit(-1)
        self.logNetworkElementStatus()
        self.logSessionProperties()
        self.logSessionStatistics()

    def setConfigProperties(self,property_file):
        config = ConfigParser.ConfigParser()
        try:
            config.read(property_file)
        except IOError as e:
            print e.message
            raise IOError("Failed to open the config file "+property_file)
        self.properties["eventQueueSize"] = int(config.get("SessionConfig","eventQueueSize"))
        self.properties["eventThreadPool"] = int(config.get("SessionConfig","eventThreadPool"))
        self.properties["eventDropMode"] = int(config.get("SessionConfig","eventDropMode"))
        self.properties["keepAliveIdleTime"] = int(config.get("SessionConfig","keepAliveIdleTime"))
        self.properties["keepAliveInterval"] = int(config.get("SessionConfig","keepAliveInterval"))
        self.properties["keepAliveRetryCount"] = int(config.get("SessionConfig","keepAliveRetryCount"))
        self.properties["reconnectTimer"] = int(config.get("SessionConfig","reconnectTimer"))

    def set_loggers(self,*args):
        if self.loglevel == "DEBUG":
            loggerlevel = logging.DEBUG
        elif self.loglevel == "WARNING":
            loggerlevel = logging.WARNING
        elif self.loglevel == "ERROR":
            loggerlevel = logging.ERROR
        elif self.loglevel == "INFO":
            loggerlevel = logging.INFO
        elif self.loglevel == "DEBUG":
            loggerlevel = logging.DEBUG
        else:
            loggerlevel = logging.NOTSET

        format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        logging.basicConfig(format=format)
        for logs in args:
            self.logger = logging.getLogger(logs)
        self.logger.setLevel(loggerlevel)
        logFileHandler = logging.FileHandler(os.path.basename(__file__).strip(".py").strip(".pyc")+".log")
        self.logger.addHandler(logFileHandler)

    def parse_arguments(self):
        self.parser = argparse.ArgumentParser(description="One PK App")
        self.parser.add_argument("-H","--hostname", dest="hostname", required=True, help="Hostname / IP address to connect")
        self.parser.add_argument("-u","--user", dest="username",required=True, help="Username configured on the router")
        self.parser.add_argument("-p","--password", dest="password",required=True, help="Password for the specified user")
        self.parser.add_argument("-c","--certificate",dest="certificate", required = True, help="Certificate / PEM key to use")
        self.parser.add_argument("-a","--appname", dest="appname", required=True, help="Application name")
        self.parser.add_argument("-f","--propertyfile",dest="propfile",required=False,default="properties.conf",help="Properties config file")
        self.parser.add_argument("-l","--loglevel", dest="loglevel", required=False, help="Log levels: CRITICAL | ERROR | WARNING | INFO | DEBUG | NOTSET", default="INFO")

        argvalues = self.parser.parse_args()
        self.element_hostname = argvalues.hostname
        self.username = argvalues.username
        self.password = argvalues.password
        self.root_cert_path = argvalues.certificate
        self.application_name = argvalues.appname
        self.properties_config = argvalues.propfile
        self.loglevel = argvalues.loglevel

    def connect(self, application_name, **kwargs):
        network_application = NetworkApplication.get_instance()
        network_application.name = application_name
        self.network_element = network_application.get_network_element(self.element_hostname)
        if self.network_element is None:
            self.logger.error("Failed to get network element")
            sys.exit(1)
        self.logger.info("We have a NetworkElement : " + self.network_element.__str__())

        session_config = SessionConfig(SessionConfig.SessionTransportMode.TLS) #default is TLS

        session_config.eventQueueSize = self.properties["eventQueueSize"]
        session_config.eventThreadPool = self.properties["eventThreadPool"]
        session_config.eventDropMode = self.properties["eventDropMode"]
        session_config.keepAliveIdleTime = self.properties["keepAliveIdleTime"]
        session_config._keepAliveInterval = self.properties["keepAliveInterval"]
        session_config.keepAliveRetryCount = self.properties["keepAliveRetryCount"]
        session_config.reconnectTimer = self.properties["reconnectTimer"]

        session_config.ca_certs = self.root_cert_path

        self.session_handle = self.network_element.connect(self.username, self.password, session_config)
        if self.session_handle is None:
            logging.error("Failed to connect to the network element")
            return False

        logging.info("successful in connecting to the network element")
        return True

    def logSessionProperties(self):
        sessionproperty = self.session_handle.sessionProp
        self.logger.info("*"*10+ "START :Session Properties" + "*"*10)
        self.logger.info("Port: " + str(sessionproperty.port))
        self.logger.info("EventQueueSize: " + str(sessionproperty.eventQueueSize))
        self.logger.info("EventThreadPool: " + str(sessionproperty.eventThreadPool))
        self.logger.info("EventDropMode: " + str(sessionproperty.eventDropMode))
        self.logger.info("ReconnectTimer: " + str(sessionproperty.reconnectTimer))
        self.logger.info("TransportMode: " + str(sessionproperty.transportMode))
        self.logger.info("*"*10+ "END :Session Properties" + "*"*10)

    def logSessionStatistics(self):
        statistics = self.session_handle.sessionStat
        self.logger.info("*"*10+ "START :Session Statistics" + "*"*10)
        self.logger.info("Events Total: %s", statistics.eventTotalCount)
        self.logger.info("\nEvents Dropped: %s", statistics.eventDropCount)
        self.logger.info("*"*10+ "END :Session Statistics" + "*"*10)

    def disconnect(self):
        try:
            if self.network_element.is_connected():
                self.network_element.disconnect()
        except Exception as e:
            self.logger.error("Failed to disconnect from Network Element")
            self.logger.error(e)
            return False
        return True

    def logNetworkElementStatus(self):
        self.logger.info("*"*10+ "START :NETWORK ELEMENT STATUS" + "*"*10)
        self.logger.info("System name: " + str(self.network_element.properties.sys_name))
        self.logger.info("System uptime: " + str(self.network_element.properties.sys_uptime))
        self.logger.info("Total system memory: "+ str(self.network_element.total_system_memory))
        self.logger.info("Free system memory: " + str(self.network_element.free_system_memory))
        self.logger.info("system CPU utilization: " + str(self.network_element.system_cpu_utilization))
        self.logger.info("System connect time: "+str(self.network_element.get_connect_time()))
        self.logger.info("System disconnect time: "+str(self.network_element.get_disconnect_time()))
        self.logger.info("*"*10+ "END :NETWORK ELEMENT STATUS" + "*"*10)

if __name__ == "__main__":
    x = onepbase()
    x.disconnect()