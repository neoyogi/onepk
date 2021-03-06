# 2015.02.05 17:21:22 IST
from onep.core.event.EventListener import EventListener
from abc import abstractmethod

class InterfaceStateListener(EventListener):
    """
    The listener interface for receiving InterfaceState events. The class that is
    interested in processing an InterfaceState event should implement this
    interface.         
    """


    @abstractmethod
    def handle_event(self, event, client_data):
        """
           Invoked when an event is received from the network element.
        
           @param event:
               An event object which indicates that an event occurred 
               in a network element.
           @type event: L{InterfaceStateEvent<interfaces.InterfaceStateEvent.InterfaceStateEvent>}
           @param client_data:
               The client_data is an object that was passed in when
               application called an API to add/register the event listener. 
               The application is responsible for casting the input client_data
               to the appropriate class before using it.
                   
           """
        pass




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:21:22 IST
