# 2015.02.05 17:17:57 IST
import logging
from onep.core.event.EventFilter import EventFilter
from onep.cdp.CDPEvent import CDPEvent

class CDPFilter(EventFilter):
    """
        Implements the EventFilter abstract class for filtering CDP events.
    
        Implements the EventFilter abstract class for filtering CDP
        events according to the specified criteria.
    
        @ivar notify_type:
        CDP Event Notification type
        @type notify_type: L{CDPEventNotifyType<onep.cdp.CDPEvent.CDPEvent.CDPEventNotifyType>}
            
        """


    def __init__(self):
        """
                Constructs a CDPFilter object without specifying criteria. and expression
        
                """
        super(CDPFilter, self).__init__()
        self.notify_type = CDPEvent.CDPEventNotifyType.ONEP_CDP_ALL




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:17:57 IST
