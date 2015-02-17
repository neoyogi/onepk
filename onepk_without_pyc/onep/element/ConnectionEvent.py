# 2015.02.05 17:21:10 IST
from onep.core.event.EventObject import EventObject
from core.util.OnepConstants import OnepConstants
from onep.element.NetworkElement import NetworkElement

class ConnectionEvent(object):
    """
    An event which indicates that a connection event occurred in a network element
    
    """

    state = NetworkElement.OnepSessionState.ONEP_STATE_DISCONNECTED

    def __init__(self, elem, state):
        """
           Constructor for the ConnectionEvent class.
        
           @param elem: The network element that triggers the event.
           @param state: State of the connection.
           """
        self.elem = elem
        self.state = state



    def doEvent(self, source):
        """
            This method specifies what action to do when a event is processed in the 
            event queue. 
        
            @param source: The source of the event.  
            """
        pass




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:21:10 IST
