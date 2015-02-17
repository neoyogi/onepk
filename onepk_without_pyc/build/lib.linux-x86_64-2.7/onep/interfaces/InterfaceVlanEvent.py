# 2015.02.05 17:18:29 IST
import logging
from onep.core.event.EventObject import EventObject
from onep.core.util.OnepConstants import OnepConstants
from onep.interfaces.InterfaceStatus import InterfaceStatus

class InterfaceVlanEvent(EventObject):
    """
    An event which indicates that a Vlan change event occurred in 
    a network interface.
    
    @undocumented: interface
    @undocumented: vlan
    @undocumented: vlan_event_type
    """

    interface = None
    vlan = None
    vlan_event_type = 0

    def __init__(self, element, event_handle, net_intf, vlan_event_type, vlan):
        super(InterfaceVlanEvent, self).__init__(element, event_handle, OnepConstants.EVENT_TYPE_VLAN)
        self.log = logging.getLogger(__name__)
        self.interface = net_intf
        self.vlan = vlan
        self.vlan_event_type = vlan_event_type



    def do_event(self, network_element):
        """
        Internal Use Only
        """
        msg = 'InterfaceVlanEvent.do_event: event_handle = ' + str(self.event_handle) + ' Vlan: ' + str(self.vlan)
        msg += ' Vlan event type :' + InterfaceStatus.InterfaceVLANEventType.enumval(self.vlan_event_type)
        self.log.debug(msg)
        target_listener = network_element.event_manager.get_event_listener(self.event_handle)
        client_data = network_element.event_manager.get_event_listener_client_data(self.event_handle)
        if target_listener != None:
            target_listener.handle_event(self, client_data)




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:18:29 IST
