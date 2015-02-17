# 2015.02.05 17:21:11 IST

class SessionStatistics(object):
    """
    SessionStatistics represents statistical data of a live session (connection) 
    between a NetworkApplication and a single NetworkElement. 
    
    @undocumented: incrementEventTotalCount
    @undocumented: incrementEventDropCount
    """


    def __init__(self, ne):
        """
                constructor 
        
                Keyword argument:
                ne
                    The NetworkElement that associates with the SessionHandle.
        
                """
        self.eventTotalCount = 0
        self.eventDropCount = 0
        self.element = ne



    def clearEventCounters(self):
        """
                Clears the event total and drop counts. The method clears (resets) the
                event drop count and event total count.
        
                """
        self.eventTotalCount = 0
        self.eventDropCount = 0



    def incrementEventTotalCount(self):
        """
        This method is for internal use only.
        """
        self.eventTotalCount += 1



    def incrementEventDropCount(self):
        """
        This method is for internal use only.
        """
        self.eventDropCount += 1




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:21:11 IST
