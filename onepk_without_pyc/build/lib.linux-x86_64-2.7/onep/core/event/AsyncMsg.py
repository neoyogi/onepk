# 2015.02.05 17:18:07 IST
from onep.core.util.Enum import enum

class AsyncMsg(object):
    """
        This abstract class is meant to be implemented by a any class acting as a
        event object.
    
        """


    def __init__(self, element, msgType):
        """
                Constructor for AsyncMsg class.
        
                Keyword argument:
                eventHandle
                    Event ID is a unique ID to identify which event listener
                    should receive the event .
                type
                    Event type, for example OnepConstants.EVENT_TYPE_SYSLOG
                    represent a syslog event type.
        
                """
        self.src_ne = element
        self.msg_type = msgType



    def do_event(self, source):
        """
                This method must be implemented by substantial class to specify what
                action to do when a event is processed in the event queue. Typically an
                action would be invoking client's event listener.
        
                Keyword argument:
                source
                    The source of the event. For example, the source of a syslog
                    event would be a NetworkElement object.
        
                """
        pass


    OnepAsyncMsgType = enum('ONEP_ASYNC_MESSAGE_TYPE_APICALL', 'ONEP_ASYNC_MESSAGE_TYPE_EVENT')


# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:18:07 IST
