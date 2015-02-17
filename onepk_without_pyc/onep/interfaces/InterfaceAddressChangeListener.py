# 2015.02.05 17:21:19 IST
from onep.core.event.EventListener import EventListener
from abc import abstractmethod

class InterfaceAddressChangeListener(EventListener):
    """
    The listener interface for receiving interface address change events.
    The class that is interested in processing an interface address change 
    event should implement this interface.
    Listener will be notified when the interface address is changed.  
    
    Changing the interface address involves two events. 
    
    The first event is where the existing IP address is released. 
    
    The second is when a new address is applied to the interface.
    
    These two events will happen in quick succession if the user has changed 
    the address to a new address; otherwise, individual events may occur apart from 
    each other as and when the user removes the address and assigns the new address, respectively.
    """


    @abstractmethod
    def handle_event(self, event, client_data):
        """
        Invoked when an event is received from the network element.
        
        @param event: An event object which indicates that an Address Change event occurred in a network element. 
        @type event:   L{InterfaceAddressChangeEvent<interfaces.InterfaceAddressChangeEvent.InterfaceAddressChangeEvent>}
        
        @param client_data: The client_data is an object that was passed in when
                   the application called an API to add/register the event listener. 
                   The application is responsible for casting the input client_data
                   to the appropriate class before using it. 
        """
        pass




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:21:19 IST
