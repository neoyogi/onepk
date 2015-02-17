# 2015.02.05 17:18:27 IST
from onep.core.event.EventObject import EventObject
from onep.core.util.OnepConstants import OnepConstants
import logging

class InterfaceMtuEvent(EventObject):
    """
    An event which indicates that a MTU event occurred in 
    a network interface.
    
    @ivar interface:
        The network interface whose MTU changed.
    @type interface: L{NetworkInterface<onep.interfaces.NetworkInterface.NetworkInterface>} 
    
    @ivar mtu:
        The new MTU.
    @type mtu: C{int}
       
    """

    interface = None
    mtu = 0

    def __init__(self, element, event_handle, net_intf, mtu):
        super(InterfaceMtuEvent, self).__init__(element, event_handle, OnepConstants.EVENT_TYPE_VLAN)
        self.log = logging.getLogger(__name__)
        self.interface = net_intf
        self.mtu = mtu



    def do_event(self, network_element):
        """
        Internal Use Only
        """
        msg = 'InterfaceMTUEvent.do_event: event_handle = ' + str(self.event_handle) + ' New MTU: ' + str(self.mtu)
        self.log.debug(msg)
        target_listener = network_element.event_manager.get_event_listener(self.event_handle)
        client_data = network_element.event_manager.get_event_listener_client_data(self.event_handle)
        if target_listener != None:
            target_listener.handle_event(self, client_data)




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:18:27 IST
