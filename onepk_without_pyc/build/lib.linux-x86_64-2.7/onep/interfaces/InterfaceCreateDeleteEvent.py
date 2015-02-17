# 2015.02.05 17:18:25 IST
from onep.core.event.EventObject import EventObject
from onep.core.util.OnepConstants import OnepConstants
import logging

class InterfaceCreateDeleteEvent(EventObject):
    """ 
    An event which indicates that an an interface creation or deletion event is received.
    
    @ivar interface:
        The Network interface from which the event came from.
    @type interface: L{NetworkInterface<interfaces.NetworkInterface.NetworkInterface>}
    
    @ivar is_oir:
        Specifies the create/delete event was an online insertion and removal (OIR) create/delete event or a
        regular create/delete.
    @type is_oir: C{bool} 
    
    @ivar is_created:
        Checks to determine if the interface was added or deleted.
    @type is_created: C{bool}
    
    """

    interface = None
    is_oir = False
    is_created = False

    def __init__(self, element, eventHandle, intf, created, oir):
        """
        Constructor of InterfaceCreateDeleteEvent class.
        """
        super(InterfaceCreateDeleteEvent, self).__init__(element, eventHandle, OnepConstants.EVENT_TYPE_IF_ADDRCHANGE)
        self.interface = intf
        self.is_oir = oir
        self.is_created = created
        self.log = logging.getLogger(__name__)



    def do_event(self, network_element):
        """
           This method specifies what action to do when a event is processed in the
           event queue. For InterfaceCreateDeleteEvent, the action is invoking
           the client's event listener.
        
           @param element:
               The Network Element at which the event is generated.
           @type element: L{NetworkElement<onep.element.NetworkElement.NetworkElement>}
           """
        msg = 'InterfaceAddressChange.do_event: event_handle = ' + str(self.event_handle) + str(self.interface)
        self.log.debug(msg)
        target_listener = network_element.event_manager.get_event_listener(self.event_handle)
        client_data = network_element.event_manager.get_event_listener_client_data(self.event_handle)
        if target_listener != None:
            target_listener.handle_event(self, client_data)




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:18:25 IST
