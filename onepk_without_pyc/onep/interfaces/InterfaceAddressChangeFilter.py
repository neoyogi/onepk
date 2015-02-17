# 2015.02.05 17:21:21 IST
from onep.core.event.EventFilter import EventFilter
from onep.core.util.OnepConstants import OnepConstants
from onep.core.exception.OnepIllegalArgumentException import OnepIllegalArgumentException
from onep.interfaces.NetworkInterface import NetworkInterface

class InterfaceAddressChangeFilter(EventFilter):
    """   
        This class implements the EventFilter abstract class for filtering an
        interface address change event according to the specified criteria.
        
        Changing interface address involves two operations, first where the existing
        ip address is released and second when new address is applied to interface.
        These two events will happen in quick succession if the user changed the primary
        address, otherwise, individual events may occur well apart from each other as 
        and when the user removes the address and assigns new address respectively.
        
        A Filter can be used to provide fine grain control over what events to listen
        to Address Change events.
        
    
       """

    _family = OnepConstants.OnepAddressFamilyType.ONEP_AF_ANY
    _interface = None

    def _get_address_family(self):
        return self._family



    def _set_address_family(self, family):
        if (family < 0 or family > 3) and family is not None:
            raise OnepIllegalArgumentException('The address family being set is invalid')
        if family == None:
            self._family = OnepConstants.OnepAddressFamilyType.ONEP_AF_ANY
        else:
            self._family = family


    _doc = '\n    The family parameter used by the filter.\n    If the family is set to None, then the application will receive notifications for all the address families.\n    \n    Raises: OnepIllegalArgumentException - if address_family is assigned invalid value\n    \n    @type:  L{OnepAddressFamilyType<onep.core.util.OnepConstants.OnepConstants.OnepAddressFamilyType>}\n    '
    address_family = property(_get_address_family, _set_address_family, None, _doc)

    def _get_interface(self):
        return self._interface



    def _set_interface(self, interface):
        if interface and isinstance(interface, NetworkInterface):
            self._interface = interface
        else:
            self._interface = None


    _doc = '\n    The network Interface. \n    The Network Interface object can be obtained from \n    L{<onep.element.NetworkElement.NetworkElement.get_interface_by_name>} API.\n    If the network interface is set to None, the application will receive address change \n    notifications for all the interfaces on the network element.\n    \n    @type: L{NetworkInterface<interfaces.NetworkInterface.NetworkInterface>} \n    '
    interface = property(_get_interface, _set_interface, None, _doc)

    def __init__(self):
        """ 
        The default InterfaceAddressChangeFilter constructor without specifying 
        any filter criteria.
        
        The default constructor does not set any filter on the interface address change
        notifications. The application will receive notifications for all address changes
        on all network interfaces. The application can add additional filters using the
        interface and address_family properties.        
        """
        super(InterfaceAddressChangeFilter, self).__init__()




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:21:21 IST
