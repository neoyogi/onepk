# 2015.02.05 17:21:07 IST
from onep.core.event.EventFilter import EventFilter
from onep.core.exception.OnepIllegalArgumentException import OnepIllegalArgumentException
from onep.discovery.ServiceSetDescription import *

class DiscoveryFilter(EventFilter):
    """
    The DiscoveryFilter class represents the specifications needed to register 
    for a service set discovery event from the root network element and/or its 
    neighbors.
    
    The application has to be connected to the root network element to receive
    service state change notifications from the root network element and its 
    neighbors. The application can use the default constructor to define the 
    service discovery filter or can refine the filter by selectively setting 
    fields of interest in the service discovery filter object. When the default
    service set discovery filter is used, the application receives all service 
    set change notifications for all the service sets on root network element 
    and its directly connected neighbors. The service set discovery filter can 
    also be defined for the filter events based on additional criteria such as 
    the network element IP address, service set name, version, and service set 
    state.
    
    The DiscoveryFilter is passed into the 
    L{add_discovery_listener<onep.element.NetworkElement>} method. A single 
    DiscoveryFilter object can be used in multiple calls 
    
    See L{DiscoveryListener<onep.discovery.DiscoveryListener>} 
    """

    DiscoveryType = enum('ONEP_DISCOVERY_ALL', 'ONEP_DISCOVERY_LOCAL', 'ONEP_DISCOVERY_NEIGHBOR')
    ServiceSetState = enum('ONEP_SERVICE_SET_STATE_ALL', 'ONEP_SERVICE_SET_ENABLED', 'ONEP_SERVICE_SET_DISABLED')
    _name = ServiceSetDescription.ServiceSetName.ONEP_SERVICE_SET_ALL
    _state = ServiceSetState.ONEP_SERVICE_SET_STATE_ALL
    _discovery_type = DiscoveryType.ONEP_DISCOVERY_ALL

    def __init__(self):
        """
        The default ServiceDiscoveryFilter constructor without specifying
        any filter criteria.
        
        Default constructor does not set any filter on the service discovery 
        notifications, and the application will receive all service change 
        notifications from the root NE and its neighbors
        """
        super(DiscoveryFilter, self).__init__()



    def _get_state(self):
        return self._state



    def _set_state(self, state):
        if state == None:
            self._state = self.ServiceSetState.ONEP_SERVICE_SET_STATE_ALL
        elif not isinstance(state, int) or state < self.ServiceSetState.ONEP_SERVICE_SET_STATE_ALL or state > self.ServiceSetState.ONEP_SERVICE_SET_DISABLED:
            raise OnepIllegalArgumentException('state', 'invalid')
        self._state = state


    _doc = '\n    Gets the new service set state.\n    \n    The application can define the service set state for which it wants to \n    receive notifications. If the service set state is set to null, the \n    application will receive notifications for all service state\n    changes\n    \n    @type : L{enum<onep.core.util.Enum>}\n    '
    state = property(_get_state, _set_state, None, _doc)

    def _set_name(self, name):
        if name == None:
            self._name = ServiceSetDescription.ServiceSetName.ONEP_SERVICE_SET_ALL
        elif not ServiceSetDescription.ServiceSetName._is_valid(name):
            raise OnepIllegalArgumentException('name', 'invalid')
        self._name = name



    def _get_name(self):
        return self._name


    _doc = 'the name of the service for the filter.\n    \n    The application can refine the filter to receive notifications when the \n    service state changes for only a particular service set. If \n    ServiceSetName is set to null, the application will receive service state \n    change notifications for all the services.\n    \n    @type: L{Enum<core.util.Enum>}\n    '
    name = property(_get_name, _set_name, None, _doc)

    def _set_type(self, discoveryType):
        if discoveryType == None:
            self._discovery_type = self.DiscoveryType.ONEP_DISCOVERY_ALL
        elif not self.DiscoveryType._is_valid(discoveryType):
            raise OnepIllegalArgumentException('discoveryType', 'invalid')
        self._discovery_type = discoveryType



    def _get_type(self):
        return self._discovery_type


    _doc = '\n    type of service set discovery.\n    \n    The application can define the kind of service set discovery, either \n    local or neighbor discovery or both. If the discovery type is null, \n    both local and neighbor service set discovery takes place.\n    \n    @type: L{Enum<onep.core.util.Enum>}\n    '
    type = property(_get_type, _set_type, None, _doc)


# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:21:08 IST
