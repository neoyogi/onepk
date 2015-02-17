# 2015.02.05 17:21:22 IST
from onep.core.event.EventObject import EventObject
from onep.core.util.OnepConstants import OnepConstants
from onep.core.event.EventListener import EventListener
from onep.core.event.EventFilter import EventFilter
from onep.core.exception.OnepIllegalArgumentException import OnepIllegalArgumentException
from onep.interfaces.NetworkInterface import NetworkInterface
from abc import abstractmethod
import logging

class InterfaceStatisticsPollEvent(EventObject):
    """
    An event indicating that an interface statistics poll event occurred in a network element.
    
    @ivar interface:
        The network interface
    @type interface: L{NetworkInterface<interfaces.NetworkInterface.NetworkInterface>} 
    
    @ivar network_element:
        The Network Element at which the event is generated.
    @type network_element: L{NetworkElement<onep.element.NetworkElement.NetworkElement>}
    
    @ivar stat:
        The collected statistics
    @type stat: L{InterfaceStatistics<interfaces.InterfaceStatistics.InterfaceStatistics>} 
       
    """


    def __init__(self, element, event_handle, interf, stat):
        """
        Constructor of InterfaceStatisticsPollEvent class.
        """
        super(InterfaceStatisticsPollEvent, self).__init__(element, event_handle, OnepConstants.EVENT_TYPE_INTERFACE_STATISTICS_POLL)
        self.network_element = element
        self.interface = interf
        self.stat = stat
        self.log = logging.getLogger(__name__)



    def do_event(self, network_element):
        """
        This method specifies what action to do when an event is processed 
        in the event queue. For InterfaceStatisticsPollEvent, the action is 
        invoking client's event listener.
        
        @param network_element:
            The Network Element at which the event is generated.
        @type network_element: L{NetworkElement<onep.element.NetworkElement.NetworkElement>}
        """
        msg = 'InterfaceStatisticsPollEvent: eventHandle = ' + str(self.event_handle)
        msg += ' Stats : ' + str(self.stat)
        self.log.debug(msg)
        target_listener = network_element.event_manager.get_event_listener(self.event_handle)
        client_data = network_element.event_manager.get_event_listener_client_data(self.event_handle)
        if target_listener != None:
            target_listener.handle_event(self, client_data)




class InterfaceStatisticsPollFilter(EventFilter):
    """   
        This class implements the EventFilter abstract class for filtering an
        interface Statistics Poll event according to the specified criteria.
        
        A Filter can be used to provide fine grain control over what events to listen
        to Statistics Poll events.
        
        @ivar interface:
            The NetworkInterface to poll events from
        @type interface: L{NetworkInterface<interfaces.NetworkInterface.NetworkInterface>} 
        
        @ivar interval:
            The interval (in seconds) during which the statistics data is polled
        @type interval: C{long}
    
       """


    def _get_interface(self):
        return self._interface



    def _set_interface(self, interface):
        if interface and isinstance(interface, NetworkInterface):
            self._interface = interface
        else:
            self._interface = None


    _doc = '\n    The network Interface. \n    The Network Interface object can be obtained from \n    L{<onep.element.NetworkElement.NetworkElement.get_interface_by_name>} API.\n    \n    @type: L{NetworkInterface<interfaces.NetworkInterface.NetworkInterface>} \n    '
    interface = property(_get_interface, _set_interface, None, _doc)

    def __init__(self, interface, interval):
        """ 
        The InterfaceStatisticsPollFilter constructor 
        
        @param interface:
            The NetworkInterface to poll events from
        @type interface: L{NetworkInterface<interfaces.NetworkInterface.NetworkInterface>} 
        
        @param interval:
            The interval (in seconds) during which the statistics data is polled
        @type interval: C{long}
        """
        super(InterfaceStatisticsPollFilter, self).__init__()
        self._interface = interface
        self.interval = interval




class InterfaceStatisticsPollListener(EventListener):
    """
    The listener interface for receiving interface statistics poll events.
    
    The class that is interested in processing a InterfaceStatisticsPoll event
    should implement this interface.
    """


    @abstractmethod
    def handle_event(self, event, client_data):
        """
        Invoked when an event is received from the network element.
        
        @param event: An event object which indicates that an event occurred in a network element. 
        @type event:   L{InterfaceStatisticsPollEvent<interfaces.InterfaceStatisticsPollEvent.InterfaceStatisticsPollEvent>}
        
        @param client_data: The client_data is an object that was passed in when
                   the application called an API to add/register the event listener. 
                   The application is responsible for casting the input client_data
                   to the appropriate class before using it. 
        """
        pass




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:21:22 IST
