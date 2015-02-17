# 2015.02.05 17:20:23 IST
from onep.core.event.EventListener import EventListener
from abc import abstractmethod

class TopologyListener(EventListener):
    """
    The listener interface for receiving Topology events. The class that is
    interested in processing a Topology event should implement this interface.
    """


    @abstractmethod
    def handle_event(self, event, clientData):
        """
        Invoked when the a Topology event is received from the network element.
        
        @param event: An event object which indicates that an event occurred
        in a network element
        @type event: L{TopologyEvent<src.topology.TopologyEvent>}
        
        @param clientData: The clientData is an object that was passed in when
        application called an API to add/register the event listener.
        The application is responsible for casting the input clientData
        to the appropriate class before using it.
        """
        pass




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:20:23 IST
