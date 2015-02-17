# 2015.02.05 17:21:23 IST
from onep.core.event.EventObject import EventObject
from onep.core.util.OnepConstants import OnepConstants
from onep.interfaces.InterfaceStatistics import InterfaceStatistics
import logging

class InterfaceStatisticsEvent(EventObject):
    """
        This class represents data related to statistical events detected on network interfaces.
        
        @ivar network_element:
            The network element.
        @type network_element: L{NetworkElement<onep.element.NetworkElement.NetworkElement>}
        
        @ivar interface:
            Gets the network interface on which this event occurred.
        @type interface: L{NetworkInterface<interfaces.NetworkInterface.NetworkInterface>} 
        
        @ivar parameter:
            Gets the parameter ID that triggered this event.
        @type parameter: L{InterfaceStatisticsParameter<onep.interfaces.InterfaceStatistics.InterfaceStatistics.InterfaceStatisticsParameter>}
        
        @ivar is_increment:
            Indicates whether this is an increment value event.
            This variable is applicable only in cases where ONEP_INTERFACE_STATISTICS_TYPE_INCREMENT is specified 
            in L{InterfaceStatisticsFilter<onep.interfaces.InterfaceStatisticsFilter.InterfaceStatisticsFilter>} criteria.
         @type is_increment: C{bool} 
        
        
        @ivar is_exit_event:
            Indicates whether this event is an exist event.
            This event is triggered due to an exit criteria match.
        @type is_exit_event: C{bool} 
        
        @ivar value:
            The incremental/decremental difference compared to the last event triggered or the absolute
            value of the parameter being monitored, depending on the interface statistics type specified in
            the registration. 
            
            For example, if ONEP_INTERFACE_STATISTICS_TYPE_INCREMENT was specified in 
            the InterfaceStatisticsFilter, the value returned will be the incremental/decremental difference.
        @type value: C{int}
    
        @ivar delta_value:
             Gets the change in value. If the type specified in event registration was
             ONEP_INTERFACE_STATISTICS_TYPE_RATE, the delta_value gets the
             difference between the current parameter value and the sample taken at
             the last poll interval. 
             
             Otherwise the return value is the difference
             between the current parameter value and the value taken when
             the event last triggered.
        @type delta_value: C{int}
        
        @ivar event_handle:
            Gets the numeric identifier that was assigned when a listener was added to detect this type of event.
        @type event_handle: C{int} 
        """

    network_element = None
    interface = None
    parameter = None
    value = 0
    delta_value = 0
    is_increment = False
    is_exit_event = False
    event_handle = None

    def __init__(self, elem, event_handle, ni, param, increment, value, delta, exit_event):
        """
        Constructor of InterfaceStatisticsEvent class.
        """
        super(InterfaceStatisticsEvent, self).__init__(elem, event_handle, OnepConstants.EVENT_TYPE_INTERFACE_STATISTICS)
        self.network_element = elem
        self.interface = ni
        self.parameter = param
        self.is_increment = increment
        self.value = value
        self.delta_value = delta
        self.is_exit_event = exit_event
        self.event_handle = event_handle
        self.log = logging.getLogger(__name__)



    def do_event(self, network_element):
        """
        This method specifies what action to do when a event is processed in the
        event queue. For InterfaceStatisticsEvent, the action is invoking
        client's event listener.
        
        @param element:
            The Network Element at which the event is generated.
        @type element: L{NetworkElement<onep.element.NetworkElement.NetworkElement>}
        """
        msg = 'Interface Statistics Event: event_handle = ' + str(self.event_handle)
        msg += ' Parameter = ' + InterfaceStatistics.InterfaceStatisticsParameter.enumval(self.parameter)
        msg += ' value = ' + str(self.value)
        self.log.debug(msg)
        target_listener = network_element.event_manager.get_event_listener(self.event_handle)
        client_data = network_element.event_manager.get_event_listener_client_data(self.event_handle)
        if target_listener != None:
            target_listener.handle_event(self, client_data)




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:21:23 IST
