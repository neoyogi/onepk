# 2015.02.05 17:18:06 IST
from onep.core.event.AsyncMsg import AsyncMsg
OnepAsyncMsgType = AsyncMsg.OnepAsyncMsgType

class EventObject(AsyncMsg):
    """
        This abstract class is meant to be implemented by any class acting as an
        event object.
    
        @ivar event_handle: A unique ID to identify which event listener should 
            receive the event.
        @type event_handle: C{int}
        @ivar event_type : The type of the event.
        @type event_type: C{int}
        """


    def __init__(self, element, eventHandle, event_type):
        """
                Constructor for EventObject class.
        
                @param eventHandle: A unique ID to identify which event listener
                    should receive the event .
                @type eventHandle: C{int}
                @param event_type: The type of the event.
                @type event_type: C{int}
                    
                """
        super(EventObject, self).__init__(element, OnepAsyncMsgType.ONEP_ASYNC_MESSAGE_TYPE_EVENT)
        self.event_handle = eventHandle
        self.event_type = event_type




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:18:06 IST
