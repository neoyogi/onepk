# 2015.02.05 17:22:18 IST
from onep.element.NetworkElement import NetworkElement
from onep.core.util.Enum import *
from onep.PolicyIDL.PolicyIDL import Client
from onep.policy.Acl import Acl
from onep.policy.L2Ace import L2Ace
from onep.core.exception.OnepIllegalArgumentException import OnepIllegalArgumentException
from onep.core.exception.OnepConnectionException import OnepConnectionException
from onep.core.exception.OnepRemoteProcedureException import OnepRemoteProcedureException
from Shared.ttypes import ExceptionIDL
from onep.thrift.Thrift import TException
import logging

class L2Acl(Acl):
    """ L2 Access Control List (ACL) Class.
    
        It is a list of L2 Access Control Elements(ACE) that define attributes for matching a packet.
        
        @undocumented: l2_ace_list
        """

    OnepLifetime = enum('ONEP_TRANSIENT', 'ONEP_PERSISTENT')

    def _get_ace_list(self):
        return self._l2_ace_list


    _doc = '\n    The list of L2 Access Control Element(ACE) instance objects.\n\n    L2 ACE object is added in the list when it is added to L2 ACL.\n\n    L2 ACE object is removed from the list when it is removed form L2 ACL.\n\n    @type: C{list}\n    '
    l2_ace_list = property(_get_ace_list, None, None, _doc)

    def _validate_ace(self, ace):
        if ace == None:
            raise OnepIllegalArgumentException('ace', 'None')
        if not isinstance(ace, L2Ace):
            raise OnepIllegalArgumentException('Passed ace argument is not of type L2Ace')



    def _validate_lifetime(self, lifetime):
        if lifetime == None:
            raise OnepIllegalArgumentException('lifetime', 'None')
        if not (lifetime == self.OnepLifetime.ONEP_TRANSIENT or lifetime == self.OnepLifetime.ONEP_PERSISTENT):
            raise OnepIllegalArgumentException('lifetime is invalid')



    def __init__(self, element, lifetime):
        """ Constructor of class L2Acl.
        
                Instantiate a new L2 Access Control List(ACL).
        
                @param element: Network Element instance.
                @type element: L{NetworkElement<onep.element.NetworkElement.NetworkElement>}
        
                @param lifetime: Life time of L2 Acl.
                @type lifetime: L{OnepLifetime<OnepLifetime>}
        
                @raise OnepIllegalArgumentException: If element or lifetime is invalid.
                @raise OnepRemoteProcedureException: If error occurs when remote procedure call is made to network element.
                @raise OnepConnectionException: If connection to network element fails.
                """
        self.log = logging.getLogger('onep.' + __name__)
        super(L2Acl, self).__init__(element)
        try:
            self._validate_lifetime(lifetime)
        except OnepIllegalArgumentException as e:
            raise e
        self._l2_ace_list = list()
        self._lifetime = lifetime
        self._acl_client = Client(element.api_protocol)
        try:
            self._acl_handle = self._acl_client.createAcl_IDL(element.session_handle._id, self._ONEP_L2ACL, self._lifetime, 0)
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e.message, e)
        self._element._l2_acl_list.append(self)



    def delete_acl(self):
        """ Delete L2 Access Control List(ACL).
        
                Attempt to delete L2-ACL which is already applied to the network interface raises exception.
        
                @raise OnepRemoteProcedureException: If error occurs when remote procedure call is made to network element.
                @raise OnepConnectionException: If connection to network element fails.
                """
        try:
            self._acl_client.deleteAcl_IDL(self._element.session_handle._id, self._acl_handle)
            self.log.info('Returned from deleteAcl_IDL idl call to delete L2-acl')
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e.message, e)
        if self in self._element._l2_acl_list:
            self._element._l2_acl_list.remove(self)



    def add_ace(self, ace):
        """ Add a L2 Access Control Element(ACE) to the L2 Access Control List(ACL).
        
                Already added L2-ACE cannot be added in the same L2-ACL again.
        
                @param ace: L2 ACE instance to be added in L2 ACL.
                @type ace: L{L2Ace<onep.policy.L2Ace.L2Ace>}
        
                @raise OnepIllegalArgumentException: If ace is invalid.
                @raise OnepRemoteProcedureException: If error occurs when remote procedure call is made to network element.
                @raise OnepConnectionException: If connection to network element fails.
                """
        try:
            self._validate_ace(ace)
            ace._add_to_l2_acl(self)
        except OnepIllegalArgumentException as e:
            raise e
        except OnepRemoteProcedureException as e:
            raise e
        except OnepConnectionException as e:
            raise e
        self._l2_ace_list.append(ace)



    def remove_ace(self, ace):
        """ Remove a L2 Access Control Element(ACE) from L2 Access Control List(ACL).
        
                Attempt to remove an ace which is not added to the L2 ACL raises no exception.
        
                @param ace: L2 ACE instance to be removed from L2 ACL.
                @type ace: L{L2Ace<onep.policy.L2Ace.L2Ace>}
        
                @raise OnepIllegalArgumentException: If ace is invalid.
                @raise OnepRemoteProcedureException: If error occurs when remote procedure call is made to network element.
                @raise OnepConnectionException: If connection to network element fails.
                """
        try:
            self._validate_ace(ace)
        except OnepIllegalArgumentException as e:
            raise e
        if ace in self._l2_ace_list:
            self._l2_ace_list.remove(ace)
            try:
                ace._remove_from_l2_acl(self)
            except OnepRemoteProcedureException as e:
                raise e
            except OnepConnectionException as e:
                raise e



    def __str__(self):
        """ Returns a string representation of the L2 Access Control List(ACL) instance.
        
                @rtype: C{str}
                @return: String representation of the L2 ACL object.
                """
        sb = '\nL2 ACL [ ' + str(self._acl_handle) + ' ]\n'
        sb += '\tACEs         : ' + str(len(self._l2_ace_list)) + '\n'
        return sb




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:22:19 IST
