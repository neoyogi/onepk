# 2015.02.05 17:23:20 IST
from onep.core.event.AsyncMsg import AsyncMsg
from onep.core.util.Enum import enum
import onep.NetworkEventIDL
from onep.vty.VtyProxy import VtyProxy
import logging

class VtyData(AsyncMsg):
    """
        The Vty data information returned by the Network Element when a command interpretation
        has completed, or the state of a Vty has changed.
    
        """


    def __init__(self, element, execHandle, state, msgType, data):
        """
                Constructor for VtyData class.
        
                Keyword argument:
                element -- The source network element.
                exec_handle -- Handle to Vty returned by Abstraction Layer
                state -- Current state of the Vty.
                msgType -- Type of message - data, state change, or error
                data -- data or error string
        
                """
        super(VtyData, self).__init__(element, AsyncMsg.OnepAsyncMsgType.ONEP_ASYNC_MESSAGE_TYPE_APICALL)
        self.exec_handle = execHandle
        self.state = state
        self.vty_msg_type = msgType
        self.data = data



    def do_event(self, source):
        """
                This method specifies what action to do when a event is processed in the 
                event queue. For Vty Event, the action is invoking client's
                event listener.
        
                Keyword argument:
                source -- The source of the event. For Vty Event, the source 
                        in an instance of NetworkElement.  
        
                """
        if source == None:
            return 
        logging.debug('VtyData.do_event: exec_handle = ' + str(self.exec_handle) + ' data = ' + self.data)
        ne = source
        targetListener = ne.event_manager.get_vty_event_listener(self.exec_handle)
        if targetListener != None:
            targetListener.handleEvent(self, ne.event_manager.get_vty_event_listener_client_data(self.exec_handle))



VtyData.OnepVtyMsgType = enum('ONEP_VTY_MSG_DATA', 'ONEP_VTY_MSG_STATE', 'ONE_VTY_MSG_ERROR')

# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:23:21 IST
