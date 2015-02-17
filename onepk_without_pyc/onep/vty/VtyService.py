# 2015.02.05 17:23:20 IST
from Shared.ttypes import ExceptionIDL
from onep.thrift.Thrift import TException
import time
from onep.core.exception.OnepConnectionException import OnepConnectionException
from onep.core.exception.OnepIllegalArgumentException import OnepIllegalArgumentException
from onep.core.exception.OnepRemoteProcedureException import OnepRemoteProcedureException
from onep.core.util.Enum import enum
from onep.core.exception.OnepException import OnepException
from onep.vty.VtyListener import VtyListener
import logging
from onep.NetCmdExecutionIDL.NetCmdExecutionIDL import Client

class OnepVtyNotClosed(IOError):
    pass

class VtyService(object):
    """
        The VtyService class represents a vty on a network element i.e. a cisco device.
    
        VTY Service Set hides the commands executed through it.
        To view the commands executed through VTY, enable CLI logs as follows.
    
        On NXOS, use vty.write("debug cli parser-detail") in your application, future onep_vty_write() will have the CLI logs in the response.
        Use vty.write("no debug cli parser-detail") to turn off CLI log or simply reopen vty session.
    
        On IOS, use the following command to view CLI logs on the Router.
        "show history all"
    
        On XR, use the following command to view CLI logs on the Router.
        "show cli history detail"
    
        """


    def __init__(self, element):
        """
                Constructor
        
                @raise OnepIllegalArgumentException
                            The exception is thrown when the input argument is invalid
                @raise OnepConnectionException:
                            The exception is thrown when the connection to a network element
                            has failed.
                @raise OnepRemoteProcedureException:
                            The exception is thrown when an error has occurred in the
                            remote procedure call made to a network element.
                @raise OnepException:
                            The exception is thrown when the server returns an invalid CPU
                            sampling interval value.
        
                @param  element: The Network Element on which to open the vty
        
                """
        self._max_response = 0
        self.timeout = 0
        self.typeahead = ''
        self.p_state = None
        self.exec_handle = 0
        self.data_available = False
        self.state = self.OnepVtyState.ONEP_VTY_STATE_DISCONNECTED
        VtyService.log = logging.getLogger(__name__)
        self.log.debug('Initializing Vty Service')
        if element == None:
            raise OnepIllegalArgumentException('element')
        if not element.is_connected():
            raise OnepConnectionException('Network Element must be connected to open a VTY')
        self.element = element
        self.api_client = Client(element.api_protocol)
        try:
            self.exec_handle = self.api_client.ExecutionCmd_newIDL(element.session_handle._id)
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e.message, e)
        self.cli_result = str()
        self.listener = VtyService.Listener()
        element.event_manager.add_vty_listener(self.exec_handle, self.listener, self)



    @property
    def max_response(self):
        """
        The maximum response byte length. Responses truncated to this length.
        Zero is unlimited
        """
        return self._max_response



    @max_response.setter
    def max_response(self, max):
        if max < 0:
            raise OnepIllegalArgumentException('max_response must be greater than zero')
        self._max_response = max



    @property
    def timeout(self):
        """The maximum length to wait for a Network Element response in seconds"""
        return self._timeout



    @timeout.setter
    def timeout(self, time_out):
        if time_out < 0:
            raise OnepIllegalArgumentException('timeout must be greater than zero')
        self._timeout = time_out



    def open(self):
        """
                Open a vty on the network element with the default cmd interpreter - no control messages
                @note: On XR, "aaa authorization eventmanager default local" must be configured
                    in config mode, otherwise open() will fail to get a valid handle.
                    Also, the device should have "hostname <whatever-hostname>" config.
                    aaa authorization commands default <group | none>" is recommended to config prior to use.
        
                @raise OnepConnectionException:
                            The exception is thrown when the connection to a network element
                            has failed.
                @raise OnepRemoteProcedureException:
                            The exception is thrown when an error has occurred in the
                            remote procedure call made to a network element.
                @raise OnepException:
                            The exception is thrown when the server returns an invalid CPU
                            sampling interval value.
        
                """
        if self.is_open():
            raise OnepException('VTY is already opened')
        try:
            self.api_client.ExecutionCmd_openIDL(self.element.session_handle._id, self.exec_handle)
            elapsedTime = 0
            while not self.data_available:
                if self.timeout > 0 and elapsedTime >= self.timeout * 100:
                    break
                elapsedTime += 1
                time.sleep(0.01)

            if not self.data_available:
                raise OnepException('VTY Open timed out')
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e.message, e)
        self.data_available = False
        self.log.debug('open: open compelete')



    def set_output_format(self, format):
        """
        Set the output format for vty
        This API can only be used before the vty is opened.
        It will raise an exception if vty is already open.
        
        @param format: The vty output format to be set on the network element
        @type format: L{OnepVtyOutputFormat<onep.vty.VtyService.OnepVtyOutputFormat>}
        @raise OnepConnectionException:
                    The exception is thrown when the connection to a network element
                    has failed.
        @raise OnepRemoteProcedureException:
                    The exception is thrown when an error has occurred in the
                    remote procedure call made to a network element.
        @raise OnepException:
                    The exception is thrown when the vty is already open and this 
                    API is called.
        """
        if not VtyService.OnepVtyOutputFormat._is_valid(format):
            raise OnepIllegalArgumentException("The input parameter 'format' is invalid.")
        if self.state is not self.OnepVtyState.ONEP_VTY_STATE_DISCONNECTED:
            raise OnepException('VTY is already open. Please, close it before changing the output format.')
        try:
            self.api_client.ExecutionCmd_setOutputFormatIDL(self.element.session_handle._id, self.exec_handle, format)
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e.message, e)



    def write(self, s):
        """
                Write a String to a vty on the network element
        
                @raise OnepConnectionException:
                            The exception is thrown when the connection to a network element
                            has failed.
                @raise OnepRemoteProcedureException:
                            The exception is thrown when an error has occurred in the
                            remote procedure call made to a network element.
                @raise OnepException:
                            The exception is thrown when the server returns an invalid CPU
                            sampling interval value.
        
                @param  s: The String to write to the vty
        
                @return: The interpreted result from the Network Element
        
                """
        if self.state == self.OnepVtyState.ONEP_VTY_STATE_DISCONNECTED or self.state == self.OnepVtyState.ONEP_VTY_STATE_IDLE_TIMEOUT:
            raise OnepConnectionException('VTY must be connected to write')
        if not s:
            raise OnepIllegalArgumentException('Input command string is null or empty.')
        try:
            self.data_available = False
            self.cli_result = ''
            self.api_client.ExecutionCmd_writeIDL(self.element.session_handle._id, self.exec_handle, s, self.typeahead, self._max_response)
            elapsedTime = 0
            while not self.data_available:
                if self.timeout > 0 and elapsedTime >= self.timeout * 100:
                    break
                elapsedTime += 1
                time.sleep(0.01)

            if not self.data_available:
                self.api_client.ExecutionCmd_stopIDL(self.element.session_handle._id, self.exec_handle)
                raise OnepException('VTY Write timed out')
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e.message, e)
        self.data_available = False
        return self.cli_result



    def write_0(self, s, typeahead):
        """
                Write a String to a vty on the network element with a typeahead list
        
                @raise OnepConnectionException:
                            The exception is thrown when the connection to a network element
                            has failed.
                @raise OnepRemoteProcedureException:
                            The exception is thrown when an error has occurred in the
                            remote procedure call made to a network element.
                @raise OnepException:
                            The exception is thrown when the server returns an invalid CPU
                            sampling interval value.
        
                @param  s: The String to write to the vty
                @param  typeAhead: The list of strings to type ahead of running the command
        
                @return: The interpreted result from the Network Element
        
                """
        if typeahead:
            self.typeahead = typeahead
        else:
            self.typeahead = ''
        return self.write(s)



    def close(self):
        """
                Close a vty.
        
                @raise OnepConnectionException:
                            The exception is thrown when the connection to a network element
                            has failed.
                @raise OnepRemoteProcedureException:
                            The exception is thrown when an error has occurred in the
                            remote procedure call made to a network element.
                @raise OnepException:
                            The exception is thrown when the server returns an invalid CPU
                            sampling interval value.
        
                """
        if self.state == self.OnepVtyState.ONEP_VTY_STATE_DISCONNECTED or self.state == self.OnepVtyState.ONEP_VTY_STATE_IDLE_TIMEOUT:
            raise OnepException('VTY is already closed')
        try:
            self.api_client.ExecutionCmd_closeIDL(self.element.session_handle._id, self.exec_handle)
        except TException as e:
            raise OnepConnectionException(e.message, e)
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        self.state = self.OnepVtyState.ONEP_VTY_STATE_DISCONNECTED



    def cancel(self):
        """
                Cancel command execution.
        
                @raise OnepConnectionException:
                            The exception is thrown when the connection to a network element
                            has failed.
                @raise OnepRemoteProcedureException:
                            The exception is thrown when an error has occurred in the
                            remote procedure call made to a network element.
                @raise OnepException:
                            The exception is thrown when the server returns an invalid CPU
                            sampling interval value.
        
                """
        if self.state == self.OnepVtyState.ONEP_VTY_STATE_DISCONNECTED or self.state == self.OnepVtyState.ONEP_VTY_STATE_IDLE_TIMEOUT:
            return 
        try:
            self.api_client.ExecutionCmd_stopIDL(self.element.session_handle._id, self.exec_handle)
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e.message, e)



    class Listener(VtyListener):
        """
                For internal use
        
                """


        def handleEvent(self, event, clientData):
            """
            """
            clientData.state = event.state
            clientData.cli_result = event.data
            clientData.data_available = True




    class CmdResults(object):
        """
                cmdResults is the collection of command results associated with the VTY and last command run
        
                """


        def __init__(self, inputLine, parseReturnCode, errorLocation):
            """
                        Constructor
            
                        @param input_line: The command line to be interpreted
                        @param parse_return_code: The return code of the parser for this command line
                        @param error_location: The position in the command line where an error was detected by the parser
            
                        """
            self.input_line = inputLine
            self.parse_return_code = parseReturnCode
            self.error_location = errorLocation




    class ParserState(object):
        """
                ParserState is used to determine what went wrong with a command block.
        
                It includes the command lines, individual parser return codes, and error postions in the input.
        
                """


        def __init__(self, prompt, overallRC, results):
            """
                        Constructor for parserState class
            
                        @param prompt:
                            The prompt of the parser at the time of command interpretation
                        @param overallRC:
                            The overall return code of the parser for this command set
                        @param results:
                            The list of parser results and errors line by line
            
                        """
            self.prompt = prompt
            self.overallRC = overallRC
            self.results = results




    def get_parser_state(self):
        """
                Returns the state of the parser after the last command interpretation.
        
                @raise OnepConnectionException:
                            The exception is thrown when the connection to a network element
                            has failed.
                @raise OnepRemoteProcedureException:
                            The exception is thrown when an error has occurred in the
                            remote procedure call made to a network element.
                @raise OnepException:
                            The exception is thrown when the server returns an invalid CPU
                            sampling interval value.
        
                @return: The parser state
        
                """
        if self.state == VtyService.OnepVtyState.ONEP_VTY_STATE_DISCONNECTED or self.state == VtyService.OnepVtyState.ONEP_VTY_STATE_IDLE_TIMEOUT:
            raise OnepConnectionException('VTY must be connected to retrieve parser state')
        try:
            execState = self.api_client.ExecutionCmd_stateGetIDL(self.element.session_handle._id, self.exec_handle)
            lst = []
            for result in execState.cmdResults:
                cmdIDL = self.CmdResults(result.inputLine, result.parseReturnCode, result.errorLocation)
                lst.append(cmdIDL)

            self.p_state = VtyService.ParserState(execState.prompt, execState.overallReturnCode, lst)
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e.message, e)
        return self.p_state



    def is_open(self):
        """
                Returns true if a connected vty exists between the network element and application.
        
                """
        if self.state == VtyService.OnepVtyState.ONEP_VTY_STATE_CONNECTED:
            return True
        else:
            return False



    def _set_idle_timeout(self, timeout):
        """
                Set VTY idle timeout - zero is infinite
        
                Throws OnepVtyNotClosed if VTY service is still open
        
                """
        if self.is_open():
            raise OnepVtyNotClosed('Vty Service must be closed to set idle timeout')
        try:
            self.api_client.ExecutionCmd_setIdleTimeoutIDL(self.element.session_handle._id, int(timeout))
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e.message, e)



    def destroy(self):
        """
                Done with VtyService instance so destroy it
        
                Throws OnepVtyNotClosed if VTY service is still open
        
                """
        if self.is_open():
            raise OnepVtyNotClosed('Vty Service must be closed before destroy')
        self.api_client.ExecutionCmd_destroyIDL(self.element.session_handle._id, self.exec_handle)



VtyService.OnepVtyState = enum('ONEP_VTY_STATE_DISCONNECTED', 'ONEP_VTY_STATE_CONNECTING', 'ONEP_VTY_STATE_CONNECTED', 'ONEP_VTY_STATE_IDLE_TIMEOUT', 'ONEP_VTY_STATE_INVALID')
VtyService.OnepVtyCmdInterp = enum('ONEP_VTY_CMD_IOS_SH', 'ONEP_VTY_CMD_TCL')
VtyService.OnepVtyOutputFormat = enum('ONEP_VTY_OUTPUT_FORMAT_TLV', 'ONEP_VTY_OUTPUT_FORMAT_TEXT', 'ONEP_VTY_OUTPUT_FORMAT_XML')
VtyService.log = None

# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:23:20 IST
