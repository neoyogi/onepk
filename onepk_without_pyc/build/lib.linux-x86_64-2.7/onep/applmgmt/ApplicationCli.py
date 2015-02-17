# 2015.02.05 17:17:54 IST
import logging
from onep.core.exception.OnepConnectionException import OnepConnectionException
from onep.core.exception.OnepIllegalArgumentException import OnepIllegalArgumentException
from onep.core.exception.OnepRemoteProcedureException import OnepRemoteProcedureException
from onep.ApplmgmtDataIDL import ApplmgmtDataIDL
from Shared.ttypes import ExceptionIDL
from thrift.Thrift import TException

class ApplicationCli:
    """
    The ApplmgmtData class represents application managed data that reside 
    in the network element.
    
    """


    def __init__(self, element, version, instance, config_domain):
        """
        Constructor for ApplicationCli.
        
        @param element:
            The network element to which the application CLI will be applied.
        @type element: L{NetworkElement<onep.element.NetworkElement.NetworkElement>} 
        @param version: 
            The CLI version which the application will use.
        @type version: C{str}
        @param instance: 
            The instance identifier which the application will use.
        @type instance: C{str}
        @param config_domain: 
            The configuration domain identifier which the application will use. This must be supplied 
            for end-node hosted applications.  If application is running in a container, 
            the container name will be used.
        @type config_domain: C{str}
        
        @raise OnepRemoteProcedureException: System failure to serve the request, please check error
                message for more details.
        @raise OnepConnectionException: Transport error, may need to reset the connection, please 
                check the error message for more details.     
        @raise OnepIllegalArgumentException: This exception is thrown if input parameter is None.
        """
        if element == None:
            raise OnepIllegalArgumentException('element', 'None')
        if version == None:
            raise OnepIllegalArgumentException('version', 'None')
        if instance == None:
            raise OnepIllegalArgumentException('instance', 'None')
        if config_domain == None:
            raise OnepIllegalArgumentException('config_domain', 'None')
        self.log = logging.getLogger(__name__)
        self.element = element
        self.version = version
        self.instance = instance
        self.config_domain = config_domain
        self.element.set_appl_managed_data(self)
        self._api_client = ApplmgmtDataIDL.Client(element.api_protocol)
        try:
            val = self._api_client.ApplManagedData_setConfigIDL(element.session_handle._id, self.version, self.instance, self.config_domain)
            self.log.debug('ApplManagedData_setConfigIDL returns: ' + str(val))
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e.message, e)



    def get_config(self, data_name):
        """
        Retrieve the configuration for the given application data managed by Network Element CLI
        interface.
        
        @param data_name:
            The name of the variable whose value needs to be retrieved.
        @return:  A string containing the value of the data
        @rtype: C{str}
        
        @raises OnepRemoteProcedureException: The exception is raised to when an error occurs in the IPC mechanism.
        @raises OnepConnectionException: The exception is raised when connection to a network element failed.
        """
        try:
            val = self._api_client.ApplManagedData_getConfigIDL(self.element.session_handle._id, data_name)
            return val
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e.message, e)



    def set_config_listener(self, listener, client_data):
        """
        Sets the ApplicationConfigCliListener for the network element. 
        
        The ApplicationConfigCliListener will be invoked when the application-defined 
        configuration commands are applied on the network element.
        
        Note: The listener is singular that is, if a listener has been set before, 
        the new listener will replace the previous one.
        
        @param listener: Instance of ApplicationConfigCliListener
        @type listener: L{ApplicationConfigCliListener<onep.applmgmt.ApplicationConfigCliListener.ApplicationConfigCliListener>}
         
        @raises OnepIllegalArgumentException: The exception is raised to when the event listener is invalid.
        """
        if listener == None:
            raise OnepIllegalArgumentException('listener', 'None')
        self.element.set_application_config_cli_listener(listener, client_data)



    def get_config_listener(self):
        """    
        Gets the ApplmgmtConfigEvent listener for the network element. 
        @return: The ApplmgmtConfigEvent listener.
        @rtype: L{ApplicationConfigCliListener<onep.applmgmt.ApplicationConfigCliListener.ApplicationConfigCliListener>}
        
        """
        return self.element.get_application_config_cli_listener()



    def set_exec_listener(self, listener, client_data):
        """
        Sets the ApplicationExecCliListener for application's show data action.
         
        The listener is invoked when the network administrator issues 
        a show CLI for the application data.
        
        Note: The listener is singular that is, if a listener has been set before, 
        the new listener will replace the previous one.
        
        @param listener: Instance of ApplicationExecCliListener 
        @type listener: L{ApplicationExecCliListener<onep.applmgmt.ApplicationExecCliListener.ApplicationExecCliListener>}
        @raises OnepIllegalArgumentException: The exception is raised when the event listener is None
        """
        if listener == None:
            raise OnepIllegalArgumentException('listener', 'None')
        self.element.set_application_exec_cli_listener(listener, client_data)



    def get_exec_listener(self):
        """
        Get a ApplmgmtShowEvent listener to the network element.
         
        @return: The ApplmgmtExecCliEvent listener.
        @rtype: L{ApplicationExecCliListener<onep.applmgmt.ApplicationExecCliListener.ApplicationExecCliListener>} 
        """
        return self.element.get_application_exec_cli_listener()




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:17:54 IST
