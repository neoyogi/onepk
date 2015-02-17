# 2015.02.05 17:22:19 IST
from onep.element.NetworkElement import NetworkElement
from onep.core.util.Enum import *
from onep.PolicyIDL.PolicyIDL import Client
from onep.interfaces.NetworkInterface import NetworkInterface
from onep.core.exception.OnepException import OnepException
from onep.core.exception.OnepIllegalArgumentException import OnepIllegalArgumentException
from onep.core.exception.OnepConnectionException import OnepConnectionException
from onep.core.exception.OnepRemoteProcedureException import OnepRemoteProcedureException
from Shared.ttypes import ExceptionIDL
from onep.thrift.Thrift import TException
from onep.interfaces.InterfaceFilter import InterfaceFilter
import logging
AclType = enum('ONEP_ACL_L2', 'ONEP_ACL_L3')
AclFilter = enum('ONEP_ACL_FILTER_ANY', 'ONEP_ACL_FILTER_L2', 'ONEP_ACL_FILTER_L3')
Direction = enum('ONEP_DIRECTION_IN', 'ONEP_DIRECTION_OUT', 'ONEP_DIRECTION_BOTH')

def _validate_element(element):
    if element == None:
        raise OnepIllegalArgumentException('element', 'None')
    if not isinstance(element, NetworkElement):
        raise OnepIllegalArgumentException('element is not of type NetworkElement')



def _validate_acl_type(acl_type):
    if acl_type == None:
        raise OnepIllegalArgumentException('acl_type', 'None')
    if acl_type != AclType.ONEP_ACL_L2 and acl_type != AclType.ONEP_ACL_L3:
        raise OnepIllegalArgumentException('acl_type is invalid')



def _validate_acl_name(acl_name):
    if acl_name == None:
        raise OnepIllegalArgumentException('acl_name', 'None')
    if not isinstance(acl_name, str):
        raise OnepIllegalArgumentException('acl_name is not of type str')



def _validate_acl_filter(acl_filter):
    try:
        AclFilter.enumval(acl_filter)
    except OnepIllegalEnumException:
        raise OnepIllegalArgumentException('Acl filter type', str(acl_filter))



class Acl(object):
    """ Access Control List (ACL) Class.
    
    It is a list of Access Control Elements(ACE) that define attributes for matching a packet.
    
    @undocumented: get_name
    """

    _ONEP_L2ACL = 0
    _ONEP_L3ACL = 1
    AclType = enum('ONEP_ACL_L2', 'ONEP_ACL_L3')
    Direction = enum('ONEP_DIRECTION_IN', 'ONEP_DIRECTION_OUT', 'ONEP_DIRECTION_BOTH')

    def _validate_nif_and_dir(self, nif, nif_direction):
        if nif == None:
            raise OnepIllegalArgumentException('nif', 'None')
        if not isinstance(nif, NetworkInterface):
            raise OnepIllegalArgumentException('nif is not of type NetworkInterface')
        if nif_direction == None:
            raise OnepIllegalArgumentException('nif_direction', 'None')
        if nif_direction != self.Direction.ONEP_DIRECTION_IN and nif_direction != self.Direction.ONEP_DIRECTION_OUT and nif_direction != self.Direction.ONEP_DIRECTION_BOTH:
            raise OnepIllegalArgumentException('Invalid nif_direction')



    def __init__(self, element):
        """ Constructor of class Acl.
         
                    Instantiate a new Access Control List.
                
                    @param element: Network Element instance.
                    @type element: L{NetworkElement<onep.element.NetworkElement.NetworkElement>}
        
                    @raise OnepIllegalArgumentException: If element is invalid.
                    """
        self.log = logging.getLogger(__name__)
        if element == None:
            raise OnepIllegalArgumentException('element', 'None')
        if not isinstance(element, NetworkElement):
            raise OnepIllegalArgumentException('Constructor argument element is not of type NetworkElement')
        self._element = element
        self._nif_acl_info = []
        self._api_transport = None
        self._evt_transport = None
        self._api_protocol = None
        self._evt_protocol = None
        self._acl_client = None
        self._acl_handle = 0
        self._acl_name = None
        self._acl_header = None



    @property
    def _acl_header(self):
        return None



    @_acl_header.setter
    def _acl_header(self, val):
        pass



    def get_name(self):
        return ''



    def apply_to_interface(self, nif, nif_direction):
        """ Apply an ACL to the Interface.
        
        ACL is applied to network interface in inbound,outbound or in both direction.
        
        @param nif: Network Interface instance.
        @type nif: L{NetworkInterface<onep.interfaces.NetworkInterface.NetworkInterface>}
        
        @param nif_direction: Direction inbound,outbound or both.
        @type nif_direction: L{Direction}
        
        @raise OnepIllegalArgumentException: If nif or direction is invalid.
        @raise OnepRemoteProcedureException: If error occurs when remote procedure call is made to network element.
        @raise OnepConnectionException: If connection to network element fails.
        """
        try:
            self._validate_nif_and_dir(nif, nif_direction)
            if self._acl_header:
                self._acl_client.applyNamedAclToInterface_IDL(self._acl_header.name, self._acl_header.type, nif.xos_handle, nif_direction, self._acl_header.addrFamily)
            else:
                self._acl_client.applyAclToInterface_IDL(self._acl_handle, nif.xos_handle, nif_direction)
            self.log.info('Returned from applyAclToInterface_IDL idl call to apply acl to interface')
        except OnepIllegalArgumentException as e:
            raise e
        except ExceptionIDL as e:
            raise OnepException('apply_to_interface', e)
        except TException as e:
            raise OnepConnectionException(e.message, e)
        nif_tuple = (nif, self.Direction.enumval(nif_direction))
        if nif_tuple not in self._nif_acl_info:
            self._nif_acl_info.append(nif_tuple)



    def remove_from_interface(self, nif, nif_direction):
        """ Remove an ACl from the Interface.
            
            ACL is removed from network interface.
            
            @param nif: Network Interface instance.
            @type nif: L{NetworkInterface<onep.interfaces.NetworkInterface.NetworkInterface>}
            
            @param nif_direction: Direction Enum.
            @type nif_direction: L{Direction}
        
            @raise OnepIllegalArgumentException: If nif or directin is invalid.
            @raise OnepRemoteProcedureException: If error occurs when remote procedure call is made to network element.
            @raise OnepConnectionException: If connection to network element fails.
            """
        try:
            self._validate_nif_and_dir(nif, nif_direction)
            if self._acl_header:
                self._acl_client.removeNamedAclFromInterface_IDL(self._acl_header.name, self._acl_header.type, nif.xos_handle, nif_direction, self._acl_header.addrFamily)
            else:
                self._acl_client.removeAclFromInterface_IDL(self._acl_handle, nif.xos_handle, nif_direction)
            self.log.info('Returned from removeAclFromInterface_IDL idl call to remove acl to interface')
        except OnepIllegalArgumentException as e:
            raise e
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e.message, e)
        nif_tuple = (nif, self.Direction.enumval(nif_direction))
        if nif_tuple in self._nif_acl_info:
            self._nif_acl_info.remove(nif_tuple)



    def __str__(self):
        """ Returns a string representation of the Acl object instance. 
        
        @rtype: C{str}
        @return: String representation of the Acl object.
        """
        sb = '\nACL [ ' + str(self._acl_handle) + ' ]\n'
        return sb




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:22:19 IST
