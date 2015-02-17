# 2015.02.05 17:21:23 IST
from onep.core.event.EventFilter import EventFilter
from onep.core.exception.OnepIllegalArgumentException import OnepIllegalArgumentException
from onep.interfaces.NetworkInterface import NetworkInterface
from onep.interfaces.InterfaceFilter import InterfaceFilter
from onep.core.util import deprecated

class InterfaceBandwidthFilter(EventFilter):
    """
        This class implements the EventFilter abstract class for filtering Bandwidth 
        event according to the specified criteria. 
        
        A Filter can be used to provide fine-tuned control over which Bandwidth events to listen to.
           
        InterfaceBandwidthFilter is deprecated and replaced by onep.interfaces.InterfaceFilter
    
        If both the parameters, network interface and interface type are
        specified, network interface takes precedence over interface type.
        """


    def _check_parameter(self, param_name, parameter, enum):
        if enum.toInteger(enum.enumval(parameter)) != parameter:
            raise OnepIllegalArgumentException(param_name, 'Invalid Value')



    def _get_interface(self):
        return self._interface



    def _set_interface(self, interface):
        if interface and isinstance(interface, NetworkInterface):
            self._interface = interface
        else:
            self._interface = None


    _doc = '\n    The Network Interface set in the filter.\n    \n    An interface if specified overrides the interface_type property, \n    and the given interface will be matched exactly.\n    \n    If the interface parameter is None then it indicates no specific interface, \n    the interface_type will determine the match.   \n    \n    @type: L{NetworkInterface<onep.interfaces.NetworkInterface.NetworkInterface>}\n    '
    interface = property(_get_interface, _set_interface, None, _doc)

    def _get_type(self):
        return self._intf_type



    def _set_type(self, intf_type):
        if intf_type == None:
            self._intf_type = NetworkInterface.InterfaceTypes.ONEP_IF_TYPE_ANY
        else:
            self._check_parameter('interface_type', intf_type, NetworkInterface.InterfaceTypes)
            self._intf_type = intf_type


    _doc = '\n    The type of Network Interface the filter should match\n    \n    An interface if specified overrides the interface_type property, \n    and the given interface will be matched exactly.\n    \n    If the interface parameter is None then it indicates no specific interface, \n    the interface_type will determine the match. \n    \n    If the type is also set to ONEP_IF_TYPE_ANY, all the interfaces\n    on the network element will match. \n    \n    Raises: OnepIllegalArgumentException - if interface_type is assigned invalid value\n    \n    @type: L{InterfaceTypes<onep.interfaces.NetworkInterface.NetworkInterface.InterfaceTypes>}\n    '
    interface_type = property(_get_type, _set_type, None, _doc)

    @deprecated(InterfaceFilter)
    def __init__(self, interface = None, interface_type = None):
        """   
        Constructs an instance of InterfaceBandwidthFilter.
        
        If no parameters are provided it returns an empty interface filter that 
        will match all the interfaces on the network element.
        
        @param interface:
               Specific interface to be monitored. The value can be set to None to
               indicate any specific interface. When not None, this attribute
               supersedes any other settings in the filter. The default value is None
        @type interface:  L{NetworkInterface<onep.interfaces.NetworkInterface.NetworkInterface>}
        @param interface_type:
               Type of interfaces to be monitored. This parameter is
               ineffective if the interface parameter is set to a non-None value.
               The default value will be set to (InterfaceTypes.ONEP_IF_TYPE_ANY) if None is passed.
        @type interface_type:L{InterfaceTypes<onep.interfaces.NetworkInterface.NetworkInterface.InterfaceTypes>} 
        @return: L{InterfaceBandwidthFilter Instance<onep.interfaces.InterfaceBandwidthFilter.InterfaceBandwidthFilter>}
        """
        super(InterfaceBandwidthFilter, self).__init__()
        self.interface = interface
        self.interface_type = interface_type




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:21:23 IST
