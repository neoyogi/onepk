# 2015.02.05 17:18:26 IST
import logging
from onep.core.util.OnepConstants import OnepConstants
from onep.core.event.EventObject import EventObject
from onep.interfaces.InterfaceStatus import InterfaceStatus

class InterfaceStateEvent(EventObject):
    """
    An event that indicates that an interface changed its line or administrative state
    up/down.
    @ivar interface:
        The network interface instance on which this event occurred
    @type interface: L{NetworkInterface<interfaces.NetworkInterface.NetworkInterface>} 
    
    @ivar state_event_type:
        The type of state change: line protocol or administrative status.
    @type state_event_type: L{InterfaceStateEventType<onep.interfaces.InterfaceStatus.InterfaceStatus.InterfaceStateEventType>}
    
    @ivar interface_state: 
        The current state of the interface conveyed by event: up or down.
    @type interface_state: L{InterfaceState<onep.interfaces.InterfaceStatus.InterfaceStatus.InterfaceState>}
    
    @ivar link: 
        The current state of the link conveyed by event: up or down.
    @type interface_state: L{InterfaceState<onep.interfaces.InterfaceStatus.InterfaceStatus.InterfaceState>}
    
    @ivar lineProto: 
        The current state of the line protocol conveyed by event: up or down.
    @type interface_state: L{InterfaceState<onep.interfaces.InterfaceStatus.InterfaceStatus.InterfaceState>}
    
    @see: L{add_interface_state_listener<onep.element.NetworkElement.NetworkElement.add_interface_state_listener>}
    @see: L{add_state_listener<onep.interfaces.NetworkInterface.NetworkInterface.add_state_listener>}
    """


    def __init__(self, elem, event_handle, ni, event_type, state, link, lineProto):
        """
        Constructor of InterfaceStateEvent class.
        """
        super(InterfaceStateEvent, self).__init__(elem, event_handle, OnepConstants.EVENT_TYPE_INTERFACE_STATE)
        self.interface = ni
        self.state_event_type = event_type
        self.interface_state = state
        self.link = link
        self.lineProto = lineProto
        self.log = logging.getLogger(__name__)



    def do_event(self, network_element):
        """
        This method specifies what action to do when a event is processed in the
        event queue. 
        
        @param element:
            The Network Element at which the event is generated.
        @type element: L{NetworkElement<onep.element.NetworkElement.NetworkElement>}
        """
        msg = 'Interface State Event: event_handle = ' + str(self.event_handle)
        msg += ' Interface: ' + self.interface.name
        msg += ' State Event Type = ' + InterfaceStatus.InterfaceStateEventType.enumval(self.state_event_type)
        msg += ' Interface state = ' + InterfaceStatus.InterfaceState.enumval(self.interface_state)
        if self.link:
            msg += ' Link state = ' + InterfaceStatus.InterfaceState.enumval(self.link)
        if self.lineProto:
            msg += ' Line Protoco state = ' + InterfaceStatus.InterfaceState.enumval(self.lineProto)
        self.log.debug(msg)
        target_listener = network_element.event_manager.get_event_listener(self.event_handle)
        client_data = network_element.event_manager.get_event_listener_client_data(self.event_handle)
        if target_listener != None:
            target_listener.handle_event(self, client_data)




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:18:26 IST
