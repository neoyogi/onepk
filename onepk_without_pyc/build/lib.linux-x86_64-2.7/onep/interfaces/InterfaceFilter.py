# 2015.02.05 17:18:25 IST
from onep.core.event.EventFilter import EventFilter
from onep.core.exception.OnepIllegalArgumentException import OnepIllegalArgumentException
from onep.interfaces.NetworkInterface import NetworkInterface
import logging

class InterfaceFilter(EventFilter):
    """ 
    InterfaceFilter represents a subset of NetworkInterface on NetworkElement.
    The filter specifies the criteria to be matched against the NetworkInterfaceList
    so as to select the subset of interfaces matching the criteria.
    
    InterfaceFilter class can be used to specify subset of interface list for
    various operations like listing of network interfaces, or adding event
    listeners on the subset of interfaces.   
    """


    def _check_parameter(self, param_name, parameter, enum):
        if enum.toInteger(enum.enumval(parameter)) != parameter:
            raise OnepIllegalArgumentException(param_name, 'Invalid Value')
        if parameter == NetworkInterface.InterfaceTypes.ONEP_IF_TYPE_GIGABIT_ETHERNET:
            self.log.warning('interface_type ONEP_IF_TYPE_GIGABIT_ETHERNET is deprecated.Use ONEP_IF_TYPE_ETHERNET instead')



    def _get_interface(self):
        return self._interface



    def _set_interface(self, interface):
        if interface and isinstance(interface, NetworkInterface):
            self._interface = interface
        else:
            self._interface = None


    _doc = '\n    The Network Interface set in the filter.\n    \n    A specific interface if mentioned overrides the interface_type property, \n    and the given interface will be matched exactly.\n    \n    If the interface parameter is None then it indicates no specific interface, \n    the interface_type will determine the match.   \n    \n    @type: L{NetworkInterface<interfaces.NetworkInterface.NetworkInterface>}\n    '
    interface = property(_get_interface, _set_interface, None, _doc)

    def _get_type(self):
        return self._interface_type



    def _set_type(self, intf_type):
        if intf_type == None:
            self._interface_type = NetworkInterface.InterfaceTypes.ONEP_IF_TYPE_ANY
        else:
            self._check_parameter('interface_type', intf_type, NetworkInterface.InterfaceTypes)
            self._interface_type = intf_type


    _doc = '\n    The type of Network Interface the filter should match\n    \n    A specific interface if mentioned overrides the interface_type property, \n    and the given interface will be matched exactly.\n    \n    If the interface parameter is None then it indicates no specific interface, \n    the interface_type will determine the match. \n    \n    If the type is also set to ONEP_IF_TYPE_ANY, all the interfaces\n    on the network element will match. \n    \n    Raises: OnepIllegalArgumentException - if interface_type is assigned invalid value\n    \n    @type: L{InterfaceTypes<interfaces.NetworkInterface.NetworkInterface.InterfaceTypes>}\n    '
    interface_type = property(_get_type, _set_type, None, _doc)

    def __init__(self, interface = None, interface_type = NetworkInterface.InterfaceTypes.ONEP_IF_TYPE_ANY):
        """   
        Creates the interface filter for the given criteria in the parameters
        If no parameters are provided it returns an empty interface filter that 
        will match all the interfaces on the network element.
        
        @param interface:
               Specific interface to be matched. The value can be set to None to
               indicate no specific interface. When not None, this attribute
               supersedes any other settings in the filter. The default value is None
        @type interface:  L{NetworkInterface<interfaces.NetworkInterface.NetworkInterface>}
        @param interface_type:
               Type of interfaces to be filtered. This parameter is
               ineffective if the interface parameter is set to a non-None value.
               The default value will be set to (InterfaceTypes.ONEP_IF_TYPE_ANY) if None is passed.
        @type interface_type:L{InterfaceTypes<interfaces.NetworkInterface.NetworkInterface.InterfaceTypes>} 
        @return: L{InterfaceFilter Instance<interfaces.InterfaceFilter.InterfaceFilter>}
        """
        super(InterfaceFilter, self).__init__()
        self._interface = interface
        self.interface_type = interface_type
        self.log = logging.getLogger(__name__)




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:18:25 IST
