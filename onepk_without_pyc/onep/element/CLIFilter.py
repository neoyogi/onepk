# 2015.02.05 17:21:11 IST
from core.event.EventFilter import EventFilter
from onep.core.exception.OnepIllegalArgumentException import OnepIllegalArgumentException

class CLIFilter(EventFilter):
    """
        Implements the EventFilter abstract class for filtering a CLI event
        
        Implements the EventFilter abstract class for filtering a CLI event
        according to the specified criteria.
     
        A Filter can be used to provide fine-tuned control over which events to
        listen to.
    
        """


    def __init__(self, pattern):
        """
        Constructs a CLIFilter with specified regular expression pattern,
        
        Using a pattern string filter to perform CLI message pattern matching. 
        Specifying a pattern parameter is mandatory in order to register for events.
        
        @param pattern:
                   Sets the pattern string used by the filter. It is a regular
                   expression used to perform CLI message pattern matching.
        """
        super(CLIFilter, self).__init__()
        self.occurs = 1
        self._skip = 0
        self._sync = 0
        self.timeoutRC = 0
        self.periodMsec = 0
        self.pattern = pattern



    def get_skip(self):
        return self._skip



    def set_skip(self, skip):
        if skip < 0:
            raise OnepIllegalArgumentException('Skip value can not be negative.')
        if self._sync > 0 and skip > 0:
            raise OnepIllegalArgumentException('Both skip and sync value cannot be true.')
        self._skip = skip


    skip = property(get_skip, set_skip)

    def get_sync(self):
        return self._sync



    def set_sync(self, sync):
        if sync < 0:
            raise OnepIllegalArgumentException('Skip value can not be negative.')
        if self._skip > 0 and sync > 0:
            raise OnepIllegalArgumentException('Both skip and sync value cannot be true.')
        self._sync = sync


    sync = property(get_sync, set_sync)


# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:21:11 IST
