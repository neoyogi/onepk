# 2015.02.05 17:21:12 IST
from onep.core.event.EventListener import EventListener

class CLIListener(EventListener):
    """
    A listener for receiving CLI events. 
    
    The class that is interested in processing a CLI event should 
    implement this interface.
    
    """


    def handle_event(self, event, clientData):
        """
           Invoked when an async CLI  event is received from the network element
        
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



    def handle_sync_event(self, event, clientData):
        """
           Invoked when a sync CLI  event is received from the network element
        
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



    def get_sync_reply(self):
        pass




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:21:12 IST
