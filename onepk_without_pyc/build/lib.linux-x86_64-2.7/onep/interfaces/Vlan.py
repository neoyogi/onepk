# 2015.02.05 17:18:28 IST
import logging
from onep.VlanIDL import VlanIDL
from onep.VlanIDL.ttypes import VlanParam_IDL
from Shared.ttypes import ExceptionIDL
from onep.core.util.Enum import enum
from onep.core.util.OnepConstants import OnepConstants
from onep.core.exception.OnepRemoteProcedureException import OnepRemoteProcedureException
from onep.core.exception.OnepIllegalArgumentException import OnepIllegalArgumentException
from onep.core.util.OnepArgumentTypeValidate import validate

class Vlan(object):
    """
    The VLAN class represents the information about the interface 
    VLAN encapsulation type and the associated tags.
    
    @undocumented: __init__
    @undocumented: from_idl
    @undocumented: from_out_idl
    @undocumented: first_tag
    @undocumented: second_tag
    @undocumented: encap
    """

    VLANEncapType = enum('NONE', 'DOT1Q', 'QINQ', 'QINANY')

    class Tag(object):
        """
        This class represent a VLAN tag, where:
        The most significant 16-bits is the Protocol Identifier (TPID).
        The next 3-bits represents Priority Code Point (PCP).
        The next 1-bit represents canonical format (CFI).
        The final 12-bits represents the VLAN ID (VID).
        
        @ivar raw_tag: The VLAN tag
        @type raw_tag: C{int}
        
        @ivar tpid: he 16-bits value representing the TPID in the tag
        @type tpid: C{int}
        
        @ivar pcp: The 3-bits value representing Priority Code Point(PCP) in the tag
        @type pcp: C{int}
        
        @ivar cfi: The 1-bits value representing canonical format (CFI) in the tag
        @type cfi: C{int}
        
        @ivar vid: The 12-bits value representing the VLAN id (VID) in the tag
        @type vid: C{int}
        
        @undocumented: __init__
        
        """


        def __init__(self, raw_tag):
            self.raw_tag = raw_tag
            self.pcp = raw_tag & 7
            self.tpid = raw_tag & 65535L
            self.cfi = raw_tag & 1
            self.vid = raw_tag & 4095




    def __init__(self, encap, first_tag, second_tag):
        self.encap = encap
        self.first_tag = self.Tag(first_tag)
        self.second_tag = self.Tag(second_tag)



    @classmethod
    def from_idl(self, vlanIdl):
        vlan = Vlan(vlanIdl.encapType, vlanIdl.vlanTag1, vlanIdl.vlanTag2)
        return vlan



    def from_out_idl(self, vlanIdl):
        vlan = Vlan(vlanIdl.encapType, vlanIdl.vlanTag1, vlanIdl.vlanTag2)
        return vlan




class VlanConfig(object):
    """
        Vlan configuration class for setting up 802.1Q VLAN encapsulation
    
        @undocumented: __init__
        @undocumented: create_vlan
        @undocumented: delete_vlan
        @undocumented: set_vlan_state
        @undocumented: set_vlan_admin_state
        @undocumented: set_vlan_name
        @undocumented: add_interface_to_vlan
        @undocumented: remove_interface_from_vlan
    
        """


    def __init__(self, ne):
        self.log = logging.getLogger(__name__)
        self.element = ne
        self.client = VlanIDL.Client(ne.api_protocol)
        self.handle = ne.session_handle._id



    def _validate_vlan(self, vlan):
        if not isinstance(vlan, int):
            raise OnepIllegalArgumentException('VLAN id must be integer')
        if vlan not in range(1, 4095):
            raise OnepIllegalArgumentException('VLAN id out of range %d' % id)



    def _validate_vlan_name(self, name):
        if not isinstance(name, str):
            raise OnepIllegalArgumentException('VLAN name not string')
        if len(name) > 64:
            raise OnepIllegalArgumentException('VLAN name over 64 characters')



    def create_vlan(self, vlan):
        """
                Create VLAN encapsulation ID
        
                @param vlan - dict
        
                       Keys    Values
                       ----    ------
                       id   -- int - VLAN ID - range <1-4095>
                       name -- string - VLAN name (maximum 64 characters) : Optional
        
                @raise OnepIllegalArgumentException:
                The exception is thrown when any of the arguments is invalid.
                @raise OnepConnectionException:
                The exception is thrown when the connection to a network element 
                has failed. 
                @raise OnepRemoteProcedureException:
                The exception is thrown when an error has occurred in the
                remote procedure call made to a network element.
        
                """
        validate(vlan, dict)
        self._validate_vlan(vlan['id'])
        name = ''
        if vlan.has_key('name') and vlan['name']:
            self._validate_vlan_name(vlan['name'])
            name = vlan['name']
        vlan_idl = VlanParam_IDL(vlan['id'], 0, name, 0, 0)
        try:
            self.log.debug(str(vlan_idl))
            self.client.createVlan_IDL(self.handle, vlan_idl)
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)



    def delete_vlan(self, id):
        """
                Remove VLAN encapsulation ID
        
                @param id -- int - VLAN ID - range <1-4095>
        
                @raise OnepIllegalArgumentException:
                The exception is thrown when any of the arguments is invalid.
                @raise OnepConnectionException:
                The exception is thrown when the connection to a network element 
                has failed. 
                @raise OnepRemoteProcedureException:
                The exception is thrown when an error has occurred in the
                remote procedure call made to a network element.
        
                """
        self._validate_vlan(id)
        try:
            self.log.debug('remove vlan %d' % id)
            self.client.deleteVlan_IDL(self.handle, id)
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)



    def set_vlan_state(self, id, state):
        """
                Set VLAN state
        
                @param id -- int - VLAN ID - range <1-4095>
        
                @param state -- OnepConstants.VlanState
                                    ACTIVE (default)
                                    SUSPEND
        
                @raise OnepIllegalArgumentException:
                The exception is thrown when any of the arguments is invalid.
                @raise OnepConnectionException:
                The exception is thrown when the connection to a network element 
                has failed. 
                @raise OnepRemoteProcedureException:
                The exception is thrown when an error has occurred in the
                remote procedure call made to a network element.
        
                """
        self._validate_vlan(id)
        if state != OnepConstants.VlanState.ACTIVE and state != OnepConstants.VlanState.SUSPEND:
            raise OnepIllegalArgumentException('VLAN state invalid')
        try:
            self.log.debug('set vlan state %d' % state)
            self.client.setVlanState_IDL(self.handle, id, state)
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)



    def set_vlan_admin_state(self, id, shutdown):
        """
                Set VLAN adminstrative state
        
                @param id -- int - VLAN ID - range <1-4095>
        
                @param shutdown -- boolean (True is default)
        
                @raise OnepIllegalArgumentException:
                The exception is thrown when any of the arguments is invalid.
                @raise OnepConnectionException:
                The exception is thrown when the connection to a network element 
                has failed. 
                @raise OnepRemoteProcedureException:
                The exception is thrown when an error has occurred in the
                remote procedure call made to a network element.
        
                """
        self._validate_vlan(id)
        if not isinstance(shutdown, bool):
            raise OnepIllegalArgumentException('VLAN admin state is boolean')
        try:
            self.log.debug('vlan shutdown %s' % str(shutdown))
            self.client.setVlanAdminState_IDL(self.handle, id, int(shutdown))
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)



    def set_vlan_name(self, id, name):
        """
                Set VLAN name
        
                @param id -- int - VLAN ID - range <1-4095>
        
                @param name -- string VLAN text name
        
                @raise OnepIllegalArgumentException:
                The exception is thrown when any of the arguments is invalid.
                @raise OnepConnectionException:
                The exception is thrown when the connection to a network element 
                has failed. 
                @raise OnepRemoteProcedureException:
                The exception is thrown when an error has occurred in the
                remote procedure call made to a network element.
        
                """
        self._validate_vlan(id)
        self._validate_vlan_name(name)
        try:
            self.log.debug('set vlan name %s', name)
            self.client.setVlanName_IDL(self.handle, id, name)
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)



    def add_interface_to_vlan(self, id, intf):
        """
                Add VLAN encapsuation to an interface
        
                @param id -- int - VLAN ID - range <1-4095>
        
                @param intf -- NetworkInterface class
        
                @raise OnepIllegalArgumentException:
                The exception is thrown when any of the arguments is invalid.
                @raise OnepConnectionException:
                The exception is thrown when the connection to a network element 
                has failed. 
                @raise OnepRemoteProcedureException:
                The exception is thrown when an error has occurred in the
                remote procedure call made to a network element.
        
                """
        self._validate_vlan(id)
        if not hasattr(intf, 'xos_handle'):
            raise OnepIllegalArgumentException('not interface object')
        try:
            self.log.debug('add %s to vlan %d' % (intf.name, id))
            self.client.setIntfVlan_IDL(self.handle, intf.xos_handle, id)
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)



    def remove_interface_from_vlan(self, id, intf):
        """
                Remove VLAN encapsuation from an interface
        
                @param id -- int - VLAN ID - range <1-4095>
        
                @param intf -- NetworkInterface class
        
                @raise OnepIllegalArgumentException:
                The exception is thrown when any of the arguments is invalid.
                @raise OnepConnectionException:
                The exception is thrown when the connection to a network element 
                has failed. 
                @raise OnepRemoteProcedureException:
                The exception is thrown when an error has occurred in the
                remote procedure call made to a network element.
        
                """
        self._validate_vlan(id)
        if not hasattr(intf, 'xos_handle'):
            raise OnepIllegalArgumentException('not interface object')
        try:
            self.log.debug('remove %s from vlan %d' % (intf.name, id))
            self.client.removeIntfFromVlan_IDL(self.handle, intf.xos_handle, id)
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:18:28 IST
