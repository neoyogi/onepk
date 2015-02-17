# 2015.02.05 17:21:23 IST
from onep.core.event.EventObject import EventObject
from onep.core.util.OnepConstants import OnepConstants
import logging

class InterfaceAddressChangeEvent(EventObject):
    """
    An event indicating that an interface address change event occurred in a network element.
    @ivar interface:
        The network interface whose address changed.
    @type interface: L{NetworkInterface<interfaces.NetworkInterface.NetworkInterface>} 
    
    @ivar old_addr:
        The old address.
    @type old_addr: C{str}
    
    @ivar new_addr:
        The new address.
    @type new_addr: C{str}
       
    """

    interface = None
    old_addr = None
    new_addr = None

    def __init__(self, element, event_handle, interf, oldaddr, newaddr, old_prefix_len, new_prefix_len):
        """
        Constructor of InterfaceAddressChangeEvent class.
        """
        super(InterfaceAddressChangeEvent, self).__init__(element, event_handle, OnepConstants.EVENT_TYPE_IF_ADDRCHANGE)
        self.interface = interf
        self.old_addr = oldaddr
        self.new_addr = newaddr
        self.old_prefix_len = old_prefix_len
        self.new_prefix_len = new_prefix_len
        self.log = logging.getLogger(__name__)



    def do_event(self, network_element):
        """
        This method specifies what action to do when an event is processed 
        in the event queue. For InterfaceAddressChangeEvent, the action is 
        invoking client's event listener.
        
        @param element:
            The Network Element at which the event is generated.
        @type element: L{NetworkElement<onep.element.NetworkElement.NetworkElement>}
        """
        msg = 'InterfaceAddressChangeEvent: eventHandle = ' + str(self.event_handle)
        msg += ' Old Address : ' + str(self.old_addr)
        msg += ' New Address: ' + str(self.new_addr)
        self.log.debug(msg)
        target_listener = network_element.event_manager.get_event_listener(self.event_handle)
        client_data = network_element.event_manager.get_event_listener_client_data(self.event_handle)
        if target_listener != None:
            target_listener.handle_event(self, client_data)




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:21:23 IST
