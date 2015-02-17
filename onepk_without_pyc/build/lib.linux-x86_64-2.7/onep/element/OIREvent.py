# 2015.02.05 17:18:18 IST
from onep.core.event.EventObject import EventObject
from onep.core.util import OnepConstants
from onep.element.OIRFilter import OIRFilter
import logging

class OIREvent(EventObject):
    """
    Represents an event which indicates that an online insertion and removal event
    
    """

    log = logging.getLogger('onep.' + __name__)

    def __init__(self, element, eventHandle, slot, oirType):
        """
        Constructor for the OIREvent class.
         
        @param eventHandle:
           Event handle is a unique ID to identify which event listener
           should receive the event.
        @param slot:
           Slot in which the OIR event came in on.
        @param oirType:
           Type of OIR event.
        """
        super(OIREvent, self).__init__(element, eventHandle, OnepConstants.EVENT_TYPE_OIR)
        self.event_handle = eventHandle
        self.slot = slot
        self.oir_type = oirType



    def do_event(self, ne):
        """
        Specifies what action to do when a event is processed.
        
        For OIREvent, the action is invoking client's event
        listener.
        
        @param ne:
                   The source of the event. For OIREvent, the source in an
                   instance of NetworkElement.
        """
        self.log.debug('OIREvent.do_event: event_handle = ' + str(self.event_handle) + ' Slot = ' + str(self.slot) + ' OIR Type = ' + str(self.oir_type))
        targetListener = ne.event_manager.get_event_listener(self.event_handle)
        clienData = ne.event_manager.get_event_listener_client_data(self.event_handle)
        if targetListener != None:
            targetListener.handle_event(self, clienData)




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:18:18 IST
