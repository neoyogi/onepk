# 2015.02.05 17:21:22 IST
import logging
from onep.core.event.EventObject import EventObject
from onep.core.util.OnepConstants import OnepConstants
from onep.interfaces.InterfaceStatus import InterfaceStatus

class InterfaceVrfEvent(EventObject):
    """
    An event which indicates that a Vrf event occurred on   
    a network interface.
    
    
    
    @undocumented: interface
    @undocumented: vrf_event_type
    @undocumented: do_event
    @undocumented: __init__
    """

    interface = None
    vrf_event_type = 0

    def __init__(self, element, event_handle, net_intf, vrf_event_type):
        super(InterfaceVrfEvent, self).__init__(element, event_handle, OnepConstants.EVENT_TYPE_VLAN)
        self.log = logging.getLogger(__name__)
        self.interface = net_intf
        self.vrf_event_type = vrf_event_type



    def do_event(self, network_element):
        """
        Internal Use Only
        """
        msg = 'InterfaceVrfEvent.do_event: event_handle = ' + str(self.event_handle) + ' Vrf event: ' + InterfaceStatus.InterfaceVRFEventType.enumval(self.vrf_event_type)
        self.log.debug(msg)
        target_listener = network_element.event_manager.get_event_listener(self.event_handle)
        client_data = network_element.event_manager.get_event_listener_client_data(self.event_handle)
        if target_listener != None:
            target_listener.handle_event(self, client_data)




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:21:22 IST
