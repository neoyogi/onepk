# 2015.02.05 17:21:17 IST
from onep.element.NetworkElement import NetworkElement
from onep.core.exception.OnepException import OnepException
from onep.core.exception.OnepIllegalArgumentException import OnepIllegalArgumentException
from onep.core.exception.OnepConnectionException import OnepConnectionException
from onep.core.exception.OnepRemoteProcedureException import OnepRemoteProcedureException
from Shared.ttypes import ExceptionIDL
from onep.thrift.Thrift import TException
from onep.SanetIDL.SanetIDL import Client
from onep.SanetIDL.SanetIDL import SanetSessionListIDL
from onep.aaa.Attribute import Attribute
from onep.AaaIDL.AaaIDL import AttrFormat_e
from onep.AaaIDL.AaaIDL import Attribute_IDL
from onep.aaa.OnepAAAAttributeType import OnepAAAAttributeType
from onep.aaa.IntAttribute import IntAttribute
from onep.aaa.StringAttribute import StringAttribute
from onep.aaa.BinaryAttribute import BinaryAttribute
from onep.aaa.AddressAttribute import AddressAttribute
from onep.core.util.Enum import isValidEnum
import logging
log = logging.getLogger(__name__)

def _validate_element(element):
    if element == None:
        raise OnepIllegalArgumentException('element', 'None')
    if not isinstance(element, NetworkElement):
        raise OnepIllegalArgumentException('element is not of type NetworkElement')



def _validate_parent(parent):
    if parent == None:
        raise OnepIllegalArgumentException('parent', 'None')
    if not isinstance(parent, Identity):
        raise OnepIllegalArgumentException('parent is not of type Identity')



def _validate_session(session):
    if session == None:
        raise OnepIllegalArgumentException('session', 'None')
    if not isinstance(session, IdentitySession):
        raise OnepIllegalArgumentException('session is not of type IdentitySession')



def _from_idl(attr_idl, network_element):
    """For internal use only"""
    if attr_idl == None:
        return 
    attr = None
    attrName = None
    if not network_element.is_connected():
        log.debug('Application is not connected to network element ' + network_element.host_address)
        return 
    if network_element.session_handle == None:
        log.debug('Application is not connected to network element ' + network_element.host_address)
        return 
    format = attr_idl.format
    attr_type = attr_idl.type
    if not isValidEnum(OnepAAAAttributeType, attr_type):
        raise OnepException('Error in attr type ' + str(attr_type))
    if attr_idl.type == OnepAAAAttributeType.ONEP_AAA_AT_APP_ATTR:
        app_attr_value = attr_idl.str_value
        if app_attr_value.startswith('"') and app_attr_value.endswith('"'):
            app_attr_value = app_attr_value.substring[1:-1]
        app_value = app_attr_value.split(':')
        if len(app_value) < 3:
            raise OnepException('Invalid app attribute format ' + str(app_value))
        attrName = app_value[0]
        try:
            if app_value[1].lower() == 'string':
                attr = StringAttribute(attr_type, attrName, app_value[2])
            else:
                attr = IntAttribute(attr_type, attrName, int(app_value[2]))
        except OnepIllegalArgumentException as e:
            raise OnepException('Error adding a Application attribute type ' + str(app_value), e)
    else:
        result = {AttrFormat_e.AAA_TYPE_FORMAT_ULONG: lambda _type, _idl: IntAttribute(_type, None, _idl.ulong_value),
         AttrFormat_e.AAA_TYPE_FORMAT_STRING: lambda _type, _idl: StringAttribute(_type, None, _idl.str_value),
         AttrFormat_e.AAA_TYPE_FORMAT_BINARY: lambda _type, _idl: BinaryAttribute(_type, None, _idl.binary_value),
         AttrFormat_e.AAA_TYPE_FORMAT_IP_ADDR: lambda _type, _idl: BinaryAttribute(_type, None, _idl.binary_value),
         AttrFormat_e.AAA_TYPE_FORMAT_IPV6_ADDR: lambda _type, _idl: BinaryAttribute(_type, None, _idl.binary_value)}
        attr = result[format](attr_type, attr_idl)
        if attr == None:
            raise OnepException('Unsupported Attribute Format')
    return attr



def _from_idl_list(attrIdlList, network_element):
    """For internal use only"""
    if attrIdlList == None:
        return 
    attrList = []
    for attr_idl in attrIdlList:
        attr = _from_idl(attr_idl, network_element)
        if attr != None:
            attrList.append(attr)

    return attrList



class Identity(object):
    """
    Session Aware Network (aka. Identity) Service Set is a set of API that allows 
    application programs to access information about the network sessions.
    
    A network session is identified by a set of AAA attributes (user-name,
    IP-address, MAC-address, etc). The Identity service set API will provide
    capability to add, update, delete and query network session based on a
    combination of query attributes. These API will provide an interface to
    applications interested in accessing network session information
    that matches certain criteria.
    
    """


    def __init__(self, element):
        """
        @param element:
            The network element from which to access 
            the Identity service. The element must be 
            connected before using this constructor to get 
                       
        @throws OnepIllegalArgumentException
            The exception is thrown when any of input parameter is 
            invalid.
        @throws OnepConnectionException
            The exception is thrown when the network element 
            is not connected.
        """
        self.log = logging.getLogger(__name__)
        self._ne = element
        _validate_element(self._ne)
        self._identity_client = Client(element.api_protocol)
        if self._identity_client == None:
            raise OnepConnectionException('Unable to create identity client instance')



    def add_session(self, attr_list):
        """
        Adds a session record to the database and updates it with the 
        attribute values. Note that "mac-addr" must be specified in
        the AAA attributes when adding a session. 
         
        @param attr_ist: List of AAA attributes to be stored in the record.
        
        @return an IdentitySession object representing the session record 
        in the database of the network element; None is returned 
        if the method failed to add a session.
                 
        @throws OnepIllegalArgumentException
            The exception is thrown when any of input parameter is 
            invalid.
        @throws OnepConnectionException
            The exception is thrown when the network element 
            is not connected.
        @throws OnepRemoteProcedureException
            The exception is thrown when an error has 
            occurred in the remote procedure call made to the 
            network element or the session cannot be created.
        """
        if attr_list == None:
            raise OnepIllegalArgumentException('attr_list', 'None')
        if self._ne == None or self._ne.session_handle == None:
            raise OnepConnectionException()
        attr_id_list = Attribute.toIDLList(attr_list, self._ne)
        try:
            session_label = self._identity_client.Sanet_Set_Attributes_IDL(self._ne.session_handle.id, -1, attr_id_list, 0)
            if session_label == -1:
                return 
            else:
                return IdentitySession(self, self._ne, session_label)
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e)



    def delete_session(self, session):
        """
        Deletes the session record from the database.
        
        @param session:
            The session that needs to be deleted. 
            
        @throws OnepIllegalArgumentException
            The exception is thrown when any of input parameter is 
            invalid.
        @throws OnepConnectionException
            The exception is thrown when the network element 
            is not connected.
        @throws OnepRemoteProcedureException
            The exception is thrown when an error has 
            occurred in the remote procedure call made to the 
            network element.
        """
        _validate_session(session)
        session.delete_session()



    def find_session_by_attributes(self, match_list, retrieve_list = None):
        """
        Finds sessions matching the attributes specified in match_list. 
        The attributes associated with each of the found sessions will be
        retrieved and returned as the values of the dictionary.
        
        If the optional retrieve_list is None, all attributes will be retrieved. 
        If the retrieve_list is not null, only a subset of the attributes listed 
        in the retrieve_list will be retrieved. 
        
        @param match_list:
            The attributes and their corresponding values in the match_list 
            specifies the sessions that match these attributes.
        @param retrieve_list:
            The retrieve_list specifies a list of attribute to be retrieved. 
            If it is None or missing, all attributes will be retrieved; otherwise 
            only a subset of the attributes listed in the retrieve_list
            will be retrieved.
                    
        @return A dictionary that contains Identity sessions as keys and list of Attribute
            as corresponding values. 
                
        @throws OnepIllegalArgumentException
            The exception is thrown when any of input parameter is 
            invalid.
        @throws OnepConnectionException
            The exception is thrown when the network element 
            is not connected.
        @throws OnepRemoteProcedureException
            The exception is thrown when an error has 
            occurred in the remote procedure call made to the 
            network element.
        """
        if self._ne == None or self._ne.session_handle == None:
            raise OnepConnectionException()
        match_idl_list = Attribute.toIDLList(match_list, self._ne)
        if match_idl_list == None:
            match_idl_list = []
        retrieve_id_list = Attribute.toIDLList(retrieve_list, self._ne)
        try:
            if retrieve_list == None:
                ss_id_list = self._identity_client.Sanet_Find_By_Attributes_IDL(self._ne.session_handle.id, match_idl_list)
            else:
                ss_id_list = self._identity_client.Sanet_Find_By_Attributes_With_Reqd_List_IDL(self._ne.session_handle.id, match_idl_list, retrieve_id_list)
            if ss_id_list == None:
                return 
            else:
                ss_map = {}
                for ss_idl in ss_id_list:
                    if ss_idl == None:
                        continue
                    ss = IdentitySession(self, self._ne, ss_idl.sessionNum)
                    attr_list = _from_idl_list(ss_idl.attr_list, self._ne)
                    ss_map[ss] = attr_list

                return ss_map
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e.getCode(), e.getText(), e)
        except TException as e:
            raise OnepConnectionException(e.getMessage(), e)



    def delete_session_by_attributes(self, match_list, enforce_multi_delete = False):
        """
            Deletes sessions matching the attributes specified in match_list. 
            The attributes and their corresponding values in the match_list need to be 
            specified in order to find the sessions that match these attributes. 
        
            If multiple sessions are found and the enforce_multi_delete parameter 
            is True, then all found sessions will be deleted. If multiple sessions 
            are found but the enforce_multi_delete parameter is False, then none of the 
            found sessions will be deleted.
        
            @param match_list:
                The attributes and their corresponding values in the match_list 
                specifies the sessions that match these attributes.
            @param enforce_multi_delete:
                This parameter determines whether to proceed with the deletion when 
                multiple sessions are found. If the  parameter is true, 
                then all found sessions will be deleted. Otherwise, none of the 
                found sessions will be deleted.
                           
            @throws OnepIllegalArgumentException
                The exception is thrown when any of input parameter is 
                invalid.
            @throws OnepConnectionException
                The exception is thrown when the network element 
                is not connected.
            @throws OnepRemoteProcedureException
                The exception is thrown when an error has 
                occurred in the remote procedure call made to the 
                network element.
            """
        if self._ne == None or self._ne.session_handle == None:
            raise OnepConnectionException()
        match_id_list = Attribute.toIDLList(match_list, self._ne)
        if match_id_list == None:
            match_id_list = []
        try:
            self._identity_client.Sanet_Delete_Session_By_Attrs_IDL(self._ne.session_handle.id, match_id_list, 1 if enforce_multi_delete else 0)
            return 
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e)




class IdentitySession(object):
    """
    IdentitySession represents a session record in the database in 
    a network element. 
    """


    @property
    def session_label(self):
        return self._session_label



    def __init__(self, parent, element, session_label):
        self.log = logging.getLogger(__name__)
        self._ne = element
        self._session_label = session_label
        self._parent = parent
        _validate_element(self._ne)
        _validate_parent(self._parent)



    def update_session_attributes(self, attr_list):
        """
             Updates the attributes of the session record in database. 
        
             The method will fail if the session record hasn't been created previously using 
             add_session(). Only the attributes passed in will be updated while retaining 
             the older values for other attributes, if any. 
             
             @param attr_list List of attributes that needed to be updated.
             
             @throws OnepIllegalArgumentException
                 The exception is thrown when any of input parameter is 
                 invalid.
             @throws OnepConnectionException
                 The exception is thrown when the network element 
                 is not connected.
             @throws OnepRemoteProcedureException
                 The exception is thrown when an error has 
                 occurred in the remote procedure call made to the 
                 network element.        
             """
        if attr_list == None:
            raise OnepIllegalArgumentException('attr_list', 'null')
        if self._ne == None or self._ne.session_handle == None:
            raise OnepConnectionException()
        attr_idl_list = Attribute.toIDLList(attr_list, self._ne)
        try:
            self._parent._identity_client.Sanet_Set_Attributes_IDL(self._ne.session_handle.id, self._session_label, attr_idl_list, 1)
            return 
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e)



    def fetch_session_attributes(self, retrieve_list = None):
        """ 
            Retrieves the attributes from a session record in database. 
            
            @param retrieve_list
                The retrieve_list specifies a list of Attribute to be retrieved. 
                If the optional retrieve_list is None or an empty list, 
                all attributes will be retrieved. 
                If the retrieve_list is not null, only a subset of 
                the attributes listed in the retrieveList will be retrieved.
                    
            @return the list of attributes retrieved.
        
            @throws OnepIllegalArgumentException
                The exception is thrown when any of input parameter is 
                invalid.
            @throws OnepConnectionException
                The exception is thrown when the network element 
                is not connected.
            @throws OnepRemoteProcedureException
                The exception is thrown when an error has 
                occurred in the remote procedure call made to the 
                network element.
            """
        if self._ne == None or self._ne.session_handle == None:
            raise OnepConnectionException()
        retrieve_id_list = Attribute.toIDLList(retrieve_list, self._ne)
        try:
            result_list = self._parent._identity_client.Sanet_Get_Attributes_IDL(self._ne.session_handle.id, self._session_label, retrieve_id_list)
            return result_list
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e.getCode(), e.getText(), e)
        except TException as e:
            raise OnepConnectionException(e.getMessage(), e)



    def delete_session(self):
        """
        Deletes the session record from the database.
        
        @throws OnepIllegalArgumentException
            The exception is thrown when any of input parameter is 
            invalid.
        @throws OnepConnectionException
            The exception is thrown when the network element 
            is not connected.
        @throws OnepRemoteProcedureException
            The exception is thrown when an error has 
            occurred in the remote procedure call made to the 
            network element.
        """
        if self._ne == None or self._ne.session_handle() == None:
            raise OnepConnectionException()
        try:
            self._parent._identity_client.Sanet_Delete_Session_IDL(self._ne.session_handle.id, self._session_label)
            self._session_label = -1
            return 
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e)




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:21:17 IST
