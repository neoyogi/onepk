# 2015.02.05 17:18:19 IST
import logging
from onep.thrift.Thrift import TException
from Shared.ttypes import ExceptionIDL
from onep.core.event.EventObject import EventObject
from onep.core.util.OnepConstants import OnepConstants
import onep.SyncEventReplyIDL

class CLIEvent(EventObject):
    """
       An event that indicates that a CLI event occurred in a network element.
       
       A CLI event occurs when input is entered on the network element console that
       matches a given regular expression pattern.
    
       """

    apiClient = None

    def __init__(self, element, eventHandle, tty, count, sync, msg):
        """
        Constructor - used internally
        
        """
        super(CLIEvent, self).__init__(element, eventHandle, OnepConstants.EVENT_TYPE_CLI)
        self.event_handle = eventHandle
        self.message = msg
        self.msg_count = count
        self.tty = tty
        self.sync = sync



    def do_event(self, ne):
        """
                This method specifies what action to do when an event is processed.
                
                For CLIEvent, the action is invoking the client's event
                listener.
                
                @param ne:
                    The source of the event. For CLIEvent, the source in an
                    instance of NetworkElement.
        
                """
        logging.debug('CLI.doEvent: eventHandle' + str(self.event_handle) + ' msgCount = ' + str(self.msg_count) + ' sync = ' + str(self.sync) + ' sync = ' + str(self.tty) + ' message = ' + self.message)
        targetListener = ne.event_manager.get_event_listener(self.event_handle)
        clienData = ne.event_manager.get_event_listener_client_data(self.event_handle)
        if targetListener != None:
            if self.sync > 0:
                rc = targetListener.handle_sync_event(self, clienData)
                try:
                    self.apiClient = SyncEventReplyIDL.Client(ne.api_protocol)
                    self.apiClient.CLISyncEvent_ResponseIDL(ne.session_handle._id, rc, targetListener.get_sync_reply())
                except ExceptionIDL as e:
                    self.log.debug('CLI.doEvent: eventHandle = ' + str(eventHandle) + ' failed to reply to synchronous event')
                except TException as e:
                    self.log.debug('CLI.doEvent: eventHandle = ' + str(eventHandle) + ' failed to reply to synchronous event')
            else:
                targetListener.handle_event(self, clienData)




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:18:19 IST
