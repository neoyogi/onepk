# 2015.02.05 17:21:07 IST
from onep.core.event.EventListener import EventListener
from abc import abstractmethod

class DiscoveryListener(EventListener):
    """
    DiscoveryListener provides an interface to the application to define the 
    action that has to be taken when ONEP Service sets are enabled or 
    disabled. If the application wants to be notified of ONEP service set 
    state changes in the network element, it invokes the add_discovery_listener
    L{NetworkElement<onep.element.NetworkElement>} API to receive notification.
    
    See L{DiscoveryEvent<onep.discovery.DiscoveryEvent>}
    See L{DiscoveryFilter<onep.discovery.DiscoveryFilter>}
    
    The following code shows how to define and add service set discovery listener 
    to the network element.
    
    1. Implement the DiscoveryListener interface:
    
    class MyDiscoveryListener(DiscoveryListener):
        def handle_event(e, clientData):
        print "Following service sets changed" +
        e.description + "change in state" + 
        str(e.state)
        
    2. Add MyDiscoveryListener instance to NetworkElement:
    
    myDiscoveryListener = MyDiscoveryListener()
    filter = DiscoveryFilter()
    networkelement.add_discovery_listener(myDiscoveryListener, filter, clientData)
    
    Warning: This Sample Code Has Not Been Verified
    """


    @abstractmethod
    def handle_event(self, event, clientData):
        """
        Invoked when an event is received from the network element.
        
        @param event: An event object that indicates that an event occurred in
        a network element.
        @type event: L{DiscoveryEvent<onep.discovery.DiscoveryEvent>}
        
        @param clientData: The clientData is an object that was passed in when
        the application called an API to add/register the event listener. The
        application is responsible for casting the input clientData to the 
        appropriate class before using it.
        @type clientData: C{void}
        """
        pass




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:21:07 IST
