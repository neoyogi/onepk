# 2015.02.05 17:18:18 IST
from core.event.EventListener import EventListener

class ApplListener(EventListener):
    """
    This interface represents a listener for receiving application events.
    
    The class that is interested in processing an application event should
    implement this interface.
    """


    def handle_event(self, event, clientData):
        """
           Invoked when the an event is received from the network element.
        
           @param event:
              An event object which indicates that an event occurred 
              in a network element.
           @param clientData:
              The clientData is an object that was passed in when
              application called an API to add/register the event listener. 
              The application is responsible for casting the input clientData
              to the appropriate class before using it.
                       
           """
        pass




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:18:18 IST
