# 2015.02.05 17:21:23 IST
from onep.core.event.EventListener import EventListener
from abc import abstractmethod

class InterfaceCreateDeleteListener(EventListener):
    """
    The listener interface for receiving interface create/delete events.
    The class that is interested in processing an interface create/delete 
    event should implement this interface.
    
    Listener will be notified as and when an interface creation or deletion 
    event is received. 
    
    The online insertion and removal (OIR) for physical ports are also 
    notified as interface create and delete events on logical interfaces 
    that have an associated physical interface. The application can glean 
    this info from the type of the interface
    
    Internal data structures allocated while creating an event are reused
    if the interface is deleted and created again. Hence, create event for
    interface is seen only the first time the interface gets created. 
    
    Delete event on the other hand is seen every time the interface is 
    deleted.
    """


    @abstractmethod
    def handle_event(self, event, client_data):
        """
         Invoked when an interface creation or deletion event is received. 
         
         The online insertion and removal (OIR) for physical ports are also 
         notified as interface create and delete events on logical interfaces 
         that have an associated physical interface. The application can glean 
         this info from the type of the interface
         
         @param event: An event object which indicates that an event occurred.
         @type event: L{InterfaceCreateDeleteEvent<interfaces.InterfaceCreateDeleteEvent.InterfaceCreateDeleteEvent>}
                    
         @param client_data:
                    The client_data is an object that was passed in when the
                    application called an API to add/register the event listener. 
                    It is application's responsibility to cast the input client_data
                    to appropriate class before using it.
        """
        pass




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:21:23 IST
