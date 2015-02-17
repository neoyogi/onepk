# 2015.02.05 17:21:22 IST
from onep.core.event.EventFilter import EventFilter
from onep.core.exception.OnepIllegalArgumentException import OnepIllegalArgumentException
from onep.interfaces.InterfaceConfig import InterfaceConfig
from onep.interfaces.NetworkInterface import NetworkInterface

class InterfaceVrfFilter(EventFilter):
    """
    This class implements the EventFilter abstract class for filtering Vrf 
    event according to the specified criteria. 
    
    A Filter can be used to provide fine-tuned control over which Vrf events to listen to.
    
    @undocumented: interface
    @undocumented: interface_type
    @undocumented: vrf_name
    @undocumented: encap
    @undocumented: __init__
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


    _doc = '\n    The Network Interface set in the filter.\n    \n    A specific interface if mentioned overrides the interface_type property, \n    and the given interface will be matched exactly.\n    \n    If the interface parameter is None then it indicates no specific interface, \n    the interface_type will determine the match.   \n    \n    @type: L{NetworkInterface<onep.interfaces.NetworkInterface.NetworkInterface>}\n    '
    interface = property(_get_interface, _set_interface, None, _doc)

    def _get_type(self):
        return self._intf_type



    def _set_type(self, intf_type):
        if intf_type == None:
            self._intf_type = NetworkInterface.InterfaceTypes.ONEP_IF_TYPE_ANY
        else:
            self._check_parameter('interface_type', intf_type, NetworkInterface.InterfaceTypes)
            self._intf_type = intf_type


    _doc = '\n    The type of Network Interface the filter should match\n    \n    A specific interface if mentioned overrides the interface_type property, \n    and the given interface will be matched exactly.\n    \n    If the interface parameter is None then it indicates no specific interface, \n    the interface_type will determine the match. \n    \n    If the type is also set to ONEP_IF_TYPE_ANY, all the interfaces\n    on the network element will match. \n    \n    Raises: OnepIllegalArgumentException - if interface_type is assigned invalid value\n    \n    @type: L{InterfaceTypes<onep.interfaces.NetworkInterface.NetworkInterface.InterfaceTypes>}\n    '
    interface_type = property(_get_type, _set_type, None, _doc)

    def _get_name(self):
        return self._name



    def _set_name(self, name):
        self._name = name


    _doc = '\n    The name of the VRF.\n    @type: C{str}\n    \n    '
    vrf_name = property(_get_name, _set_name, None, _doc)

    def _get_encap(self):
        return self._encap_type



    def _set_encap(self, encap_type):
        if encap_type == None:
            self._encap_type = InterfaceConfig.Encap.ONEP_IF_ENCAP_ANY
        else:
            self._check_parameter('Encap_type', encap_type, InterfaceConfig.Encap)
            self._encap_type = encap_type


    _doc = '\n    The type of Encapsulation the Filter should match.\n    \n    If the encapsulation type is also set to ONEP_IF_ENCAP_ANY, all encapsulations will be matched.\n    \n    Raises: OnepIllegalArgumentException - if interface_type is assigned invalid value\n    \n    @type : L{Encap<onep.interfaces.InterfaceConfig.InterfaceConfig.Encap>}\n    '
    encap = property(_get_encap, _set_encap, None, _doc)

    def __init__(self, interface = None, interface_type = None, vrf_name = None, encap = None):
        """   
        Constructs an instance of InterfaceVrfFilter.
        If no parameters are provided it returns an empty interface filter that 
        will match all the interfaces on the network element.
        
        @param interface:
               Specific interface to be monitored. The value can be set to None to
               indicate any interface. When not None, this attribute
               supersedes any other settings in the filter. The default value is None
        @type interface:  L{NetworkInterface<onep.interfaces.NetworkInterface.NetworkInterface>}
        @param interface_type:
               Type of interfaces to be monitored. This parameter is
               ineffective if the interface parameter is set to a non-None value.
               The default value will be set to (InterfaceTypes.ONEP_IF_TYPE_ANY) if None is passed.
        @type interface_type:L{InterfaceTypes<onep.interfaces.NetworkInterface.NetworkInterface.InterfaceTypes>} 
        @param vrf_name:
               Specifies the name of the vrf
        @type vrf_name: C{str}
        @param encap:
                Specifies the encapsulation type to be monitored. If it is set to null, 
                it means any type. Note that this parameter has no effect in current release.
        @type encap: L{Encap<onep.interfaces.InterfaceConfig.InterfaceConfig.Encap>}
         
        @return: L{InterfaceVrfFilter<onep.interfaces.InterfaceVrfFilter.InterfaceVrfFilter>}
        """
        super(InterfaceVrfFilter, self).__init__()
        self.interface = interface
        self.interface_type = interface_type
        self.vrf_name = vrf_name
        self.encap = encap




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:21:22 IST
