# 2015.02.05 17:21:22 IST
from onep.core.event.EventFilter import EventFilter
from onep.core.exception.OnepIllegalArgumentException import OnepIllegalArgumentException
from onep.interfaces.NetworkInterface import NetworkInterface
from onep.interfaces.InterfaceConfig import InterfaceConfig

class InterfaceCreateDeleteFilter(EventFilter):
    """
    This class implements the EventFilter abstract class for filtering an
    interface create/delete event according to the specified criteria.
    
    A filter can be used to provide fine-tuned control over which events to listen
    to.
    
    If a specific interface is set in the filter, the rest of the criteria are ignored.
    
    If a specific interface is not set, the 'include_subinterfaces' property will be ignored. 
    """

    _interface = None
    _interface_type = NetworkInterface.InterfaceTypes.ONEP_IF_TYPE_ANY
    _encap = InterfaceConfig.Encap.ONEP_IF_ENCAP_ANY
    _include_subinterfaces = False

    def _check_parameter(self, param_name, parameter, enum = None):
        if parameter == None:
            raise OnepIllegalArgumentException(param_name, 'None')
        if enum:
            if not enum._is_valid(parameter):
                raise OnepIllegalArgumentException(param_name, 'Invalid Value')



    def _get_interface(self):
        return self._interface



    def _set_interface(self, interface):
        if interface and isinstance(interface, NetworkInterface):
            self._interface = interface
        else:
            self._interface = None


    _doc = '\n    The network Interface. \n    The Network Interface object can be obtained from \n    L{<onep.element.NetworkElement.NetworkElement.get_interface_by_name>} API.\n    If the network interface is set to None, the application will receive address change \n    notifications for all the interfaces on the network element.\n    @type: L{NetworkInterface<interfaces.NetworkInterface.NetworkInterface>} \n    '
    interface = property(_get_interface, _set_interface, None, _doc)

    def _get_include_subinterfaces(self):
        return self._include_subinterfaces



    def _set_include_subinterfaces(self, val):
        if isinstance(val, bool):
            self._include_subinterfaces = val
        else:
            raise OnepIllegalArgumentException('include_subinterfaces', 'Invalid value')


    _doc = '\n    Specifies whether the subinterfaces of a given interface set in this filter also should be monitored.\n    This parameter applies only if interface property is explicitly set. it is set to False by default.\n    \n    Raises: OnepIllegalArgumentException - if include_subinterfaces is assigned None or invalid value\n    \n    @type: bool\n    '
    include_subinterfaces = property(_get_include_subinterfaces, _set_include_subinterfaces, None, _doc)

    def _get_interface_type(self):
        return self._interface_type



    def _set_interface_type(self, intf_type):
        self._check_parameter('interface_type', intf_type, NetworkInterface.InterfaceTypes)
        self._interface_type = intf_type


    _doc = '\n    The NetworkInterface type set in this filter.\n    If an Interface Create Delete event occurs and the type of interface in the filter matches that\n    of the event then a notification will be sent to the application.\n    \n    Raises: OnepIllegalArgumentException - if interface_type is assigned None or invalid value\n    \n    @type: L{InterfaceTypes<interfaces.NetworkInterface.NetworkInterface.InterfaceTypes>} \n    '
    interface_type = property(_get_interface_type, _set_interface_type, None, _doc)

    def _get_encap(self):
        return self._encap



    def _set_encap(self, encap):
        self._check_parameter('encap', encap, InterfaceConfig.Encap)
        self._encap = encap


    _doc = '\n    The encapsulation set in this filter.\n    If an Interface Create Delete event occurs and the type of encapsulation in the filter matches that\n    of the event then a notification will be sent to the application.\n    \n    Raises: OnepIllegalArgumentException - if encap is assigned None or invalid value\n    \n    @type: L{Encap<onep.interfaces.InterfaceConfig.InterfaceConfig.Encap>}\n    '
    encap = property(_get_encap, _set_encap, None, _doc)

    def __init__(self):
        """
        The default constructor does not set any filter on the interface address
        change notifications. The application will receive notifications for all
        interface create delete events. 
        
        The application can add filters using the interface, encap, interface_type and
         include_subinterfaces properties.
        """
        super(InterfaceCreateDeleteFilter, self).__init__()




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:21:22 IST
