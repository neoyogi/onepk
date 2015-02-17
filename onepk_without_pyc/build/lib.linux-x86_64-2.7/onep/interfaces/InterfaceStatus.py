# 2015.02.05 17:18:29 IST
from onep.core.util.Enum import enum

class InterfaceStatus(object):
    """ 
    Class which handles provides information about status of the interface
    
    @ivar interface_name:
        The name of the interface
    @type interface_name: C{str}
    
    @ivar link:
        The link status of the interface.
    @type link: L{InterfaceState<interfaces.InterfaceStatus.InterfaceStatus.InterfaceState>}
    
    @ivar lineproto:
        The lineproto state of the interface.
    @type lineproto:  L{InterfaceState<interfaces.InterfaceStatus.InterfaceStatus.InterfaceState>}  
    
    """

    InterfaceStateEventType = enum('ONEP_IF_STATE_EVENT_LINK', 'ONEP_IF_STATE_EVENT_LINEPROTO', 'ONEP_IF_STATE_EVENT_ANY')
    InterfaceState = enum(ONEP_IF_STATE_ADMIN_DOWN=1, ONEP_IF_STATE_OPER_DOWN=2, ONEP_IF_STATE_OPER_UP=3)
    InterfaceVLANEventType = enum('ONEP_IF_VLAN_EVENT_ADD', 'ONEP_IF_VLAN_EVENT_DELETE', 'ONEP_IF_VLAN_EVENT_ANY')
    InterfaceVRFEventType = enum('ONEP_IF_VRF_EVENT_LINEPROTO', 'ONEP_IF_VRF_EVENT_LINK')
    interface_name = None
    link = InterfaceState.ONEP_IF_STATE_ADMIN_DOWN
    lineproto = InterfaceState.ONEP_IF_STATE_ADMIN_DOWN

    def __init__(self, link, lineproto, interface_name):
        """
        Constructor of InterfaceStatus class.
        """
        self.link = link
        self.lineproto = lineproto
        self.interface_name = interface_name



    def __str__(self):
        """
        Obtain string representation of the Interface Status object.
        """
        sb = ''
        sb += '\nInterfaceStatus [ ' + self.interface_name + ' ]\n'
        sb += '\tLinkState        : ' + str(self.InterfaceState.enumval(self.link)) + '\n'
        sb += '\tLineProtoState   : ' + str(self.InterfaceState.enumval(self.lineproto)) + '\n'
        return sb




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:18:29 IST
