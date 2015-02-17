# 2015.02.05 17:20:30 IST
from onep.core.event.EventListener import EventListener

class VtyListener(EventListener):
    """
        The listener interface for receiving vty events. The class that is
        interested in processing a vty event should implement this interface.
    
        """


    def handleEvent(self, event, clientData):
        """
                Invoked when the a vty event is received from the network element.
        
                Keyword argument:
                event
                    An event object which indicates that an event occurred 
                    in a network element.
                clientData
                    The clientData is an object that was passed in when
                    application called an API to add/register the event listener. 
                    It is application's responsibility to cast the input clientData
                    to appropriate class before using it.
        
                """
        pass




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:20:30 IST
