# 2015.02.05 17:18:27 IST
from onep.core.event.EventListener import EventListener

class InterfaceVlanListener(EventListener):
    """
    The listener interface for receiving interface VLAN change events.
    The class that is interested in processing an interface VLAN change 
    event should implement this interface.
    Listener will be notified when the interface VLAN is changed.  
    """


    def handle_event(self, event, client_data):
        """
        Invoked when an VLAN change event is received from the network element.
        
        @param event: An event object which indicates that an VLAN Change event occurred in a network element. 
        @type event:   L{InterfaceVlanEvent<interfaces.InterfaceVlanEvent.InterfaceVlanEvent>}
        
        @param client_data: The client_data is an object that was passed in when
                   the application called an API to add/register the event listener. 
                   The application is responsible for casting the input client_data
                   to the appropriate class before using it. 
        """
        pass




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:18:27 IST
