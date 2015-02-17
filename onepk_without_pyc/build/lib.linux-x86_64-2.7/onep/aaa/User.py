# 2015.02.05 17:17:49 IST
from onep.thrift.Thrift import TException
from onep.core.exception.OnepConnectionException import OnepConnectionException
from onep.core.exception.OnepException import OnepException
from onep.core.exception.OnepIllegalArgumentException import OnepIllegalArgumentException
from onep.core.exception.OnepRemoteProcedureException import OnepRemoteProcedureException
import onep.element.NetworkElement
from onep.interfaces.NetworkInterface import NetworkInterface
from onep.aaa.Attribute import Attribute
from onep.aaa.AddressAttribute import AddressAttribute
from onep.aaa.OnepAAAAttributeType import OnepAAAAttributeType
from onep.aaa.BinaryAttribute import BinaryAttribute
from onep.aaa.IntAttribute import IntAttribute
from onep.aaa.StringAttribute import StringAttribute
from onep.aaa.Server import Server
from onep.AaaIDL import AaaIDL
from onep.AaaIDL.AaaIDL import AttrFormat_e
from onep.AaaIDL.AaaIDL import Attribute_IDL
from Shared.ttypes import ExceptionIDL
from onep.core.util.Enum import enum
import logging

class User(object):
    """
        AAA User class.
    
        A AAA User is associated with the following entities:
            - Network Element which is used to access AAA services for the AAA User
            - AAA Server that was used for the last AAA service. The server is characterized by its address and the AAA Protocol type (onep_aaa_protocol_e). One or more AAA servers are configured on the Network Element. Based on the availability,one of the configured server is used for accessing the AAA service
            - AAA Attribute List that contains the Authorization Profile associated with the AAA User that was downloaded from the AAA Server. An attribute list can also be included while sending a service request to the AAA Server.
    
        @undocumented: AttrListToIDL
        """

    OnepAAAAcctAction = enum('ONEP_AAA_ACCT_ACTION_START', 'ONEP_AAA_ACCT_ACTION_STOP', 'ONEP_AAA_ACCT_ACTION_UPDATE')

    def __init__(self, ne, username, password):
        """
        Create a User instance.
        @param ne: Network Element which is used to access AAA server.
        @param username: User name.
        @param password: User password.
        @raise OnepIllegalArgumentException: if username, password or network element is null
        @raise OnepException: if application is not connected to network element
        """
        self.server = None
        self.userID = 0
        self.is_auto_acct_enabled = False
        self.attr_original = []
        self.auth_profile = []
        User.log = logging.getLogger(__name__)
        if ne == None:
            raise OnepIllegalArgumentException('ne')
        if username == None:
            raise OnepIllegalArgumentException('username')
        if password == None:
            raise OnepIllegalArgumentException('password')
        if not ne.is_connected():
            raise OnepException('Application is not connected to ' + ne.host_address)
        self.network_element = ne
        self.username = username
        self.password = password
        self.user_client = AaaIDL.Client(ne.api_protocol)



    def set_network_element(self, network_element):
        """
                Set the network element to be used for the AAA Service.
        
                This method updates the Network Element to be used to access the AAA Service for an existing AAA User instance.
                It overwrites the Network Element that was set in the call to User(NetworkElement,String,String).
                If auto-accounting is enabled for the user and if an accounting session is active
                between the existing Network Element and the AAA Server, then this API will result
                into sending an Accounting-Stop over the accounting session.
                Auto-accounting session will not be initiated from the new Network Element
                until the AAA User is authenticated on the new Network Element and the Authorization Profile has auto-accounting enabled.
                @param network_element: the Network Element to set
                @raise OnepIllegalArgumentException: if the network element is null
                """
        if network_element == None:
            raise OnepIllegalArgumentException('network_element')
        if not network_element.is_connected():
            raise OnepException('Application is not connected to ' + network_element.host_address)
        self.network_element = network_element
        self.user_client = AaaIDL.Client(network_element.api_protocol)
        if self.is_auto_acct_enabled:
            self.send_accounting_record(self.OnepAAAAcctAction.ONEP_AAA_ACCT_ACTION_STOP, [])
            self.is_auto_acct_enabled = False



    def authenticate(self, list_):
        """
                Authenticate a user using the AAA Service on the Network Element.
        
                This method authenticates a user (i.e. an instance of AAA User)
                using the AAA Service on the Network Element associated with the user
                set while creating the AAA User instance
                or updated using set_network_element(NetworkElement).
        
                On successful authentication the following will happen:
                    - The user's authorization profile configured on the AAA server is
                    returned as a AAA Attribute List instance.
                    - Accounting is turned on for the user, if the AAA Server
                    administrator has enabled auto-accounting for this user by
                    configuring Cisco VSA "auto-acct=enable" in the user's authorization
                    profile.
        
                The AAA User Authorization Profile is realized using a list of L{onep.aaa.Attribute}
                structure, which is cached locally in the AAA User instance.
        
                Change of Authorization functionality is not available,
                so if the AAA admin changes the user's profile on the AAA server after
                the user was successfully authenticated, the new profile will not
                be reflected in this object unless the Application calls
                authenticate() again to refresh the Authorization Profile.
        
                Note:
                Accounting, if enabled, is turned off when the AAA User instance
                is removed using remove_user() or if the AAA User's
                Network Element attachment is changed using
                set_network_element(NetworkElement) API
        
                Note:
                The AAA Server that was used to service this request
                can be retrieved from self.server
        
                Note:
                The "allowed-action" attribute is not returned in the authorization
                profile. Use is_action_authorized(String) to read the
                value of this attribute set in the authorization profile configured
                on the AAA server.
        
                Example:
        
                >>> attrs = user.authenticate(None)
                >>> for attr in attrs:
                        print str(attr)
        
                @return: List of Attributes containing the authorization profile for the user.
                If no authorization profile is configured on AAA server, the list is a size of 0.
                @raise OnepConnectionException:
                The exception is thrown when connection to a network element has failed
                @raise OnepRemoteProcedureException:
                The exception is thrown when error has occurred in the remote-
                procedure call made to a network element
                """
        attrType = None
        attr = None
        attrName = None
        format = AttrFormat_e()
        idlList = self.AttrListToIDL(list_)
        try:
            self._validate_element_connection()
        except OnepException:
            raise 
        try:
            result = self.user_client.authenticate_IDL(self.network_element.session_handle._id, self.username, self.password, idlList)
            self.userID = result.aaa_user_id
            self.is_auto_acct_enabled = True if result.auto_acct_enabled != 0 else False
            try:
                address = NetworkInterface._convert_to_inetaddress(result.server.address)
                self.server = Server(address, Server.OnepAAAProtocol.enumval(result.server.aaa_protocol))
            except OnepIllegalArgumentException as e2:
                self.log.error('User authenticate: error retrieving server information')
            for attrIDL in result.author_profile:
                skipResultList = False
                attr = None
                attrName = None
                format = attrIDL.format
                try:
                    attrType = attrIDL.type
                except OnepIllegalArgumentException as e1:
                    self.log.error('Error adding attribute type ' + str(attrIDL.type) + ' to list, possible enum mismatch')
                    continue
                if attrIDL.type == OnepAAAAttributeType.ONEP_AAA_AT_ALLOWED_APP or attrIDL.type == OnepAAAAttributeType.ONEP_AAA_AT_ALLOWED_ACTION or attrIDL.type == OnepAAAAttributeType.ONEP_AAA_AT_AUTO_ACCT:
                    skipResultList = True
                if attrIDL.type == OnepAAAAttributeType.ONEP_AAA_AT_APP_ATTR:
                    appAttrValue = attrIDL.str_value
                    if appAttrValue.startswith('"') and appAttrValue.endswith('"'):
                        appAttrValue = appAttrValue.substring[1:-1]
                    appValue = appAttrValue.split(':')
                    if len(appValue) < 3:
                        self.log.error('Invalid app attribute format')
                        continue
                    attrName = appValue[0]
                    try:
                        if appValue[1].lower() == 'string':
                            attr = StringAttribute(attrType, attrName, appValue[2])
                        else:
                            attr = IntAttribute(attrType, attrName, int(appValue[2]))
                    except OnepIllegalArgumentException as e:
                        self.log.error('Error adding a Application attribute type ' + str(appValue))
                        continue
                elif format == AttrFormat_e.AAA_TYPE_FORMAT_ULONG:
                    try:
                        attr = IntAttribute(attrType, None, attrIDL.ulong_value)
                    except OnepIllegalArgumentException as e:
                        self.log.error('Error adding  attribute type ' + str(attrType))
                        continue
                elif format == AttrFormat_e.AAA_TYPE_FORMAT_STRING:
                    try:
                        attr = StringAttribute(attrType, None, attrIDL.str_value)
                    except OnepIllegalArgumentException as e:
                        self.log.error('Error adding  attribute type ' + str(attrType))
                        continue
                elif format == AttrFormat_e.AAA_TYPE_FORMAT_BINARY:
                    try:
                        attr = BinaryAttribute(attrType, None, attrIDL.binary_value)
                    except OnepIllegalArgumentException as e:
                        self.log.error('Error adding  attribute type ' + str(attrType))
                        continue
                else:
                    try:
                        attr = AddressAttribute(attrType, None, attrIDL.str_value)
                    except OnepIllegalArgumentException as e:
                        self.log.error('Error adding  attribute type ' + str(attrType))
                        continue
                self.attr_original.append(attr)
                if not skipResultList:
                    self.auth_profile.append(attr)

        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(arg_cause=e)
        return self.auth_profile



    def is_action_authorized(self, action):
        """
                Verify if action is authorized for user.
        
                This method verifies whether a particular action is authorized for a
                user. The action-name string must exactly match one of the action-names
                in the user's profile on the AAA Server. The search space is limited to
                actions listed for the application that invoked
                L{authenticate}. Action-names are case-sensitive.
        
                @param action: Action name
                @return: True if action is authorized, False otherwise.
                @raise OnepException: if action is not present in the attribute list returned by {@link #authenticate} API
                """
        if self.attr_original == None:
            raise OnepException('User authorization profile does not exist ')
        if action == None:
            raise OnepIllegalArgumentException('action')
        for attr in self.attr_original:
            if attr.type_ != OnepAAAAttributeType.ONEP_AAA_AT_ALLOWED_ACTION:
                continue
            actionStr = attr.str_value.split(':')
            if len(actionStr) < 2:
                self.log.error('Invalid Allowed Action attribute format')
                continue
            if actionStr[1].lower() == action.lower():
                return True

        return False



    def send_accounting_record(self, action, accntRecord):
        """
                Send an accounting record for a user using AAA Service on the Network Element.
        
                This method is used for sending an accounting record to the AAA
                (Accounting) Server.
        
                Note: This method must not be used to send Accounting 
                messages if auto-accounting is enabled for the AAA User.
                Note: If auto-accounting is enabled for a user then this API will
                not be allowed to be executed.
                Note: The AAA Server that was used to service this request
                can be retrieved by calling L{authenticate}
        
                @param action:  Accounting action type L{OnepAAAAcctAction}, START,
                STOP,or UPDATE.
                @param accntRecord: Attribute list containing Application-specific
                attributes (including byte/packet counters as per RFC2866) to be
                included in the accounting records. This argument can be
                specified as None if there are no Application-specific attributes
                to be sent.
                @raise OnepConnectionException:
                The exception is thrown when connection to a network element has failed.
                @raise OnepRemoteProcedureException:
                The exception is thrown when error has occurred in the remote-
                procedure call made to a network element.
                @raise OnepConnectionException:
                The exception is thrown when connection to a network element has failed
                @raise OnepIllegalArgumentException: if accntRecord is null.
                """
        try:
            self._validate_element_connection()
        except OnepException:
            raise 
        if self.is_auto_acct_enabled:
            raise OnepException('Auto accounting is already enabled')
        idlList = self.AttrListToIDL(accntRecord)
        try:
            acctResult = self.user_client.account_IDL(self.userID, action, idlList)
            self.userID = acctResult.aaa_user_id
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(arg_cause=e)



    def AttrListToIDL(self, attrList):
        attrIDLList = []
        if attrList == None:
            return attrIDLList
        for attr in attrList:
            attrIDLList.append(attr.toIDL(self.network_element))

        return attrIDLList



    def remove_user(self):
        """
                Remove the user record maintained by ONEP Infrastructure.
        
                This API removes all the information that is maintained by
                ONEP session infrastructure for the given user. If accounting has started
                for the given user, an accounting STOP request is sent to the AAA server.
        
                Note: The API below does not remove user records from the AAA server,
                nor does it invalidate the existing user instance.
        
                The application can reuse the existing User instance to re-authenticate with the AAA Server.
        
                @raise OnepConnectionException:
                The exception is thrown when connection to a network element has failed.
        
                @raise OnepRemoteProcedureException:
                The exception is thrown when an error has occurred in the remote
                procedure call made to a network element.
        
                @raise OnepException:
                The exception is thrown when the removal of user session fails.
                """
        if self.userID == 0:
            self.log.debug('User session does not exist')
            return 
        try:
            self._validate_element_connection()
        except OnepException:
            raise 
        try:
            if self.user_client.deallocate_aaa_user_IDL(self.userID, 1 if self.is_auto_acct_enabled else 0) == 0:
                raise OnepException('Error removing user ' + self.username)
            self.is_auto_acct_enabled = False
            self.attr_original = None
            self.userID = 0
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(arg_cause=e)



    def _validate_element_connection(self):
        if not self.network_element.is_connected():
            raise OnepException('Application is not connected to network element ' + self.network_element.host_address)
        if self.network_element.session_handle is None:
            raise OnepException('Application is not connected to network element ' + self.network_element.host_address)
        if self.user_client._iprot is not self.network_element.api_protocol:
            self.user_client = AaaIDL.Client(self.network_element.api_protocol)



User.log = None

# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:17:50 IST
