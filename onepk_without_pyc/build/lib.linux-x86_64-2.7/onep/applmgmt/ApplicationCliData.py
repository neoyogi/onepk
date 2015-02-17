# 2015.02.05 17:17:54 IST
import logging
from onep.core.event.AsyncMsg import AsyncMsg
from onep.core.util.Enum import enum
from onep.core.exception.OnepConnectionException import OnepConnectionException
from onep.core.exception.OnepIllegalArgumentException import OnepIllegalArgumentException
from onep.core.exception.OnepRemoteProcedureException import OnepRemoteProcedureException
from onep.ApplmgmtDataIDL import ApplmgmtDataIDL
from Shared.ttypes import ExceptionIDL
from thrift.Thrift import TException
_onep_async_msg_type = AsyncMsg.OnepAsyncMsgType

class ApplicationCliData(AsyncMsg):
    """
    The application managed data information returned by the network element 
    when a configuration is applied to application data on the network element, 
    or a show application data is invoked through the CLI.
    
    @ivar data_name: The name of the data variable
    @type data_name: C{str}
    
    @ivar data_value: The value of the data variable
    @type data_value: C{str}  
    """

    OnepAppCLIDataType = enum('ONEP_APP_CLI_TYPE_CONFIG', 'ONEP_APP_CLI_TYPE_EXEC')

    def __init__(self, element, data_name, data_val, type):
        """
        Constructor for ApplicationCliData class.
        """
        super(ApplicationCliData, self).__init__(element, _onep_async_msg_type.ONEP_ASYNC_MESSAGE_TYPE_APICALL)
        self.log = logging.getLogger(__name__)
        self.data_name = data_name
        self.data_value = data_val
        self.cli_type = type
        self._api_client = ApplmgmtDataIDL.Client(element.api_protocol)



    def _set_show_data(self, element, data_name, data_value):
        if data_name == None:
            raise OnepIllegalArgumentException('dataName', 'None')
        try:
            self._api_client.ApplManagedData_setShowDataIDL(element.session_handle._id, data_name, data_value)
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e.message, e)



    def do_event(self, network_element):
        if network_element == None:
            return 
        if self.cli_type == self.OnepAppCLIDataType.ONEP_APP_CLI_TYPE_CONFIG:
            self.log.debug('Message for CLI type: ONEP_APP_CLI_TYPE_CONFIG')
            target_listener = network_element.get_application_config_cli_listener()
            client_data = network_element.get_application_config_cli_client_data()
            if target_listener != None:
                target_listener.handle_event(self, client_data)
        else:
            self.log.debug('Message for CLI type: ONEP_APP_CLI_TYPE_EXEC')
            target_listener = network_element.get_application_exec_cli_listener()
            client_data = network_element.get_application_exec_cli_client_data()
            if target_listener != None:
                show_data_value = target_listener.handle_event(self, client_data)
                if not isinstance(show_data_value, str):
                    raise TypeError('Expected str from %s.handle_event. %s received.' % (type(target_listener), type(show_data_value)))
                try:
                    self._set_show_data(network_element, self.data_name, show_data_value)
                except OnepRemoteProcedureException as e:
                    self.log.error('Show CLI data dispatch failed with message: ' + e.message)
                except OnepIllegalArgumentException as e:
                    self.log.error('Show CLI data dispatch failed with message: ' + e.message)
                except OnepConnectionException as e:
                    self.log.error('Show CLI data dispatch failed with message: ' + e.message)




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:17:54 IST
