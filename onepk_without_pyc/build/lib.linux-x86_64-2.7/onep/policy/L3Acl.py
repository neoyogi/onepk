# 2015.02.05 17:19:25 IST
from onep.element.NetworkElement import NetworkElement
from onep.core.util.Enum import *
from onep.core.util.OnepConstants import *
from onep.PolicyIDL.PolicyIDL import Client
from onep.policy.Acl import Acl
from onep.policy.Acl import AclType
from onep.policy.L3Ace import L3Ace
from onep.core.exception.OnepException import OnepException
from onep.core.exception.OnepIllegalArgumentException import OnepIllegalArgumentException
from onep.core.exception.OnepConnectionException import OnepConnectionException
from onep.core.exception.OnepRemoteProcedureException import OnepRemoteProcedureException
from onep.core.util.OnepStatus import OnepStatus
from Shared.ttypes import ExceptionIDL
from onep.thrift.Thrift import TException
import logging
from ctypes import c_uint

class L3Acl(Acl):
    """ L3 Access Control List(ACL) class.
    
    It is a list of L3 Access Control Elements(ACE) that define attributes for matching a packet.
    
    @undocumented: afi
    @undocumented: l3_ace_list
    """

    OnepLifetime = enum('ONEP_TRANSIENT', 'ONEP_PERSISTENT')

    def _get_afi(self):
        return self._afi


    _doc = '\n    Address Family of L3 Access Control List(ACL).\n    \n    Valid Address Family for L3 Acl: OnepAddressFamilyType.ONEP_AF_INET, OnepAddressFamilyType.ONEP_AF_INET6 \n    \n    @type: L{OnepAddressFamilyType<onep.core.util.OnepConstants.OnepConstants.OnepAddressFamilyType>}\n    '
    afi = property(_get_afi, None, None, _doc)

    def _validate_ace(self, ace):
        if ace == None:
            raise OnepIllegalArgumentException('ace', 'None')
        if not isinstance(ace, L3Ace):
            raise OnepIllegalArgumentException('Passed ace argument is not of type L3Ace')



    def _validate_afi(self, afi):
        if afi == None:
            raise OnepIllegalArgumentException('Address Family', 'None')
        if not (afi == OnepConstants.OnepAddressFamilyType.ONEP_AF_INET or afi == OnepConstants.OnepAddressFamilyType.ONEP_AF_INET6):
            raise OnepIllegalArgumentException('Invalid Address Family')



    def _validate_lifetime(self, lifetime):
        if lifetime == None:
            raise OnepIllegalArgumentException('lifetime', 'None')
        if not (lifetime == self.OnepLifetime.ONEP_TRANSIENT or lifetime == self.OnepLifetime.ONEP_PERSISTENT):
            raise OnepIllegalArgumentException('lifetime is invalid')



    def __init__(self, element, afi, lifetime, header = None):
        """ Constructor of class L3Acl.
        
           Instantiate a new L3 Access Control List(ACL).
           
           @param element: Network Element instance.
           @type element: L{NetworkElement<onep.element.NetworkElement.NetworkElement>}
           @param afi: Address Family. It can be OnepAddressFamilyType.ONEP_AF_INET or OnepAddressFamilyType.ONEP_AF_INET6
           @type afi: L{OnepAddressFamilyType<onep.core.util.OnepConstants.OnepConstants.OnepAddressFamilyType>}
           @param lifetime: Life time of L3 Acl.
           @type lifetime: L{OnepLifetime<OnepLifetime>}
           
           @raise OnepIllegalArgumentException: If element,address family or lifetime is invalid.
           @raise OnepRemoteProcedureException: If error occurs when remote procedure call is made to network element.
           @raise OnepConnectionException: If connection to network element fails.
           """
        self.log = logging.getLogger(__name__)
        super(L3Acl, self).__init__(element)
        self._l3_ace_list = []
        try:
            self._validate_afi(afi)
            self._validate_lifetime(lifetime)
        except OnepIllegalArgumentException as e:
            raise e
        self._afi = afi
        self._app_id = element.session_handle._id
        self._lifetime = lifetime
        self._acl_client = Client(element.api_protocol)
        if header:
            self._acl_header = header
            return 
        try:
            try:
                self._acl_handle = self._acl_client.createAcl_IDL(element.session_handle._id, self._ONEP_L3ACL, self._lifetime, afi)
                self.log.debug('Created ACL')
                self._element._l3_acl_list.append(self)
            except ExceptionIDL as e:
                raise OnepException('L3Acl init', e)
        except TException as e:
            raise OnepConnectionException(e.message, e)



    def delete_acl(self):
        """ Delete L3 Access Control List(ACL). 
        
        Attempt to delete L3-ACL which is already applied to the network interface raises exception.
        
        @raise OnepRemoteProcedureException: If error occurs when remote procedure call is made to network element.
        @raise OnepConnectionException: If connection to network element fails.
        """
        if self._acl_header:
            try:
                attached = self.get_applied_interfaces()
                for remove in attached:
                    self.log.debug('removing ACL from interface')
                    self.remove_from_interface(remove[0], remove[1])

                self.log.debug('Delete named ACL')
                self._acl_client.deleteNamedAcl_IDL(self._element.session_handle._id, self._acl_header.name, self._acl_handle, self._acl_header.lifetime, self._acl_header.addrFamily)
                self.log.info('Returned from deleteNamedAcl_IDL idl call to delete L3-acl')
            except ExceptionIDL as e:
                raise OnepRemoteProcedureException(e)
            except TException as e:
                raise OnepConnectionException(e.message, e)
        else:
            try:
                self.log.debug('Delete ACL')
                self._acl_client.deleteAcl_IDL(self._element.session_handle._id, self._acl_handle)
                self.log.info('Returned from deleteAcl_IDL idl call to delete L3-acl')
            except ExceptionIDL as e:
                raise OnepRemoteProcedureException(e)
            except TException as e:
                raise OnepConnectionException(e.message, e)
            if self in self._element._l3_acl_list:
                self._element._l3_acl_list.remove(self)



    def _duplicate_ace(self, ace, ace_list):
        """ 
        """
        for a in ace_list:
            if a._sequence == ace._sequence:
                return True

        return False



    def add_ace(self, ace):
        """ Add a L3 Access Control Element(ACE) to the L3 Access Control List(ACL).
                
        Already added L3-ACE cannot be added in the same L3-ACL again.
        
        @param ace: L3 ACE instance to be added in L3 ACL.
        @type ace: L{L3Ace<onep.policy.L3Ace.L3Ace>}
        
        @raise OnepIllegalArgumentException: If ace/ace parameter is invalid.
        @raise OnepRemoteProcedureException: If error occurs when remote procedure call is made to network element.
        @raise OnepConnectionException: If connection to network element fails.
        """
        try:
            self._validate_ace(ace)
        except OnepIllegalArgumentException as e:
            raise e
        if not ace._acl == None:
            raise OnepIllegalArgumentException('Ace already added to an Acl')
        if self._duplicate_ace(ace, self._l3_ace_list) != False:
            raise OnepIllegalArgumentException('Ace with same sequence number already exists in Acl')
        ret_val = ace._check_proto()
        if ret_val == 1:
            raise OnepIllegalArgumentException('Ace does not have valid protocol')
        try:
            ace._add_to_acl(self)
        except OnepIllegalArgumentException as e:
            raise e
        except OnepConnectionException as e:
            raise e
        except OnepRemoteProcedureException as e:
            raise e



    def remove_ace(self, ace):
        """ Remove a L3 Access Control Element(ACE) from L3 Access Control List(ACL).
                
        @param ace: L3 ACE instance to be removed from L3 ACL.
        @type ace: L{L3Ace<onep.policy.L3Ace.L3Ace>}
        
        @raise OnepIllegalArgumentException: If ace is invalid.
        @raise OnepRemoteProcedureException: If error occurs when remote procedure call is made to network element.
        @raise OnepConnectionException: If connection to network element fails. 
        """
        self._validate_ace(ace)
        ace._remove_from_acl(self)



    def __str__(self):
        """ Returns a string representation of the L3 Access Control List(ACL) instance. 
        
        @rtype: C{str}
        @return: String representation of the L3 ACL.
        """
        sb = '\nL3 ACL [ ' + str(self._acl_handle) + ' ]\n'
        sb += '\tAFI          : ' + OnepConstants.OnepAddressFamilyType.enumval(self._afi) + '\n'
        return sb




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:19:25 IST
