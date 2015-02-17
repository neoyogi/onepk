# 2015.02.05 17:21:22 IST
from onep.core.event.EventObject import EventObject
from onep.core.util.OnepConstants import OnepConstants
import logging

class InterfaceBandwidthEvent(EventObject):
    """
    An event which indicates that a Bandwidth change event occurred in 
    a network interface.
    
    @ivar interface:
        The network interface whose Bandwidth changed.
    @type interface: L{NetworkInterface<onep.interfaces.NetworkInterface.NetworkInterface>} 
    
    @ivar bandwidth:
        The new Bandwidth.
    @type bandwidth: C{int}
       
    @ivar is_tx:
        The bandwidth is tx
    @type is_tx: C{bool}
       
    """


    def __init__(self, element, event_handle, net_intf, bandwidth, is_tx):
        super(InterfaceBandwidthEvent, self).__init__(element, event_handle, OnepConstants.EVENT_TYPE_VLAN)
        self.log = logging.getLogger(__name__)
        self.interface = net_intf
        self.bandwidth = bandwidth
        self.is_tx = True if is_tx else False



    def do_event(self, network_element):
        """
        Internal Use Only
        """
        msg = 'InterfaceBandwidthEvent.do_event: event_handle = ' + str(self.event_handle) + ' New Bandwidth: ' + str(self.bandwidth)
        self.log.debug(msg)
        target_listener = network_element.event_manager.get_event_listener(self.event_handle)
        client_data = network_element.event_manager.get_event_listener_client_data(self.event_handle)
        if target_listener != None:
            target_listener.handle_event(self, client_data)




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:21:22 IST
