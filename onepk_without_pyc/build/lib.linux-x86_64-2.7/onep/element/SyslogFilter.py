# 2015.02.05 17:18:19 IST
import logging
from onep.core.event.EventFilter import EventFilter
from onep.core.util.OnepConstants import OnepConstants
from onep.core.exception.OnepIllegalArgumentException import OnepIllegalArgumentException

class SyslogFilter(EventFilter):
    """
        Implements the EventFilter abstract class for filtering a syslog event
        
        Implements the EventFilter abstract class for filtering a syslog event
        according to the specified criteria.
     
        A Filter can be used to provide fine-tuned control over which events to
        listen to.
    
        """


    def __init__(self, pattern):
        """
                Constructs a SyslogFilter object with the specified text pattern
                
                @param pattern: the regular expression text matching pattern
        
                """
        super(SyslogFilter, self).__init__()
        self.pattern = pattern
        self.occurs = 1
        self.priority = OnepConstants.EVENT_MIN_PRIORITY
        self.periodMsec = 0




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:18:19 IST
