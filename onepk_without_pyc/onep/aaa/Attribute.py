# 2015.02.05 17:20:33 IST
from onep.thrift.Thrift import TException
import core.exception.OnepConnectionException
import core.exception.OnepException
import core.exception.OnepIllegalArgumentException
import core.exception.OnepRemoteProcedureException
from core.util.HostIpCheck import HostIpCheck
import element.NetworkElement
from onep.AaaIDL.AaaIDL import AttrFormat_e
from onep.AaaIDL.AaaIDL import Attribute_IDL
from onep.aaa.OnepAAAAttributeType import OnepAAAAttributeType
import logging

class Attribute(object):
    """
        The Attribute class stores the AAA attributes defined for a user.
        An attributes list can consist of the following attributes:
        - Any Standard IETF attribute
        - Any Vendor Specific Attribute defined by Vendors such as Cisco, Microsoft, etc. and Standards Bodies such as 3GPP2, WiMAX Forum, etc.
        - allowed-action - Cisco's custom attribute (specifically defined for ConnectedApps) for action- based authorization
        - app-attr - Cisco's custom attribute (specifically defined for ConnectedApps) for any application- defined attribute name value pair
    
        The two new attributes allowed-action and app-attr will be
        stored in the AAA User's Authorization Profile on the AAA Server.
        - Attribute allowed-action - use this attribute to specify
                names of Application-specific actions that a user is
                authorized to perform.
    
                Format - The format for this attribute setting on AAA server is
                    cisco-avpair = "allowed-action=&lt;appname&gt;:&lt;action-name&gt;"
    
                Examples
                    cisco-avpair = "allowed-action=appname:action-name1"
                    cisco-avpair = "allowed-action=appname:action-name2"
    
                The {@link aaa.User#authenticate(java.util.List)} method can be used
                to check if the action a user is attempting to perform matches
                the action-name listed in the user's profile on the AAA server.
    
        - Attribute app-attr - use this attribute
                for any application-specific parameter.
                One possible use is to leverage AAA for Application-specific
                configuration parameters or properties.
    
                Format - The format for this attribute setting on AAA server is
                     cisco avpair = "app-attr=&lt;avpair-name&gt;:&lt;avpair-format&gt;:&lt;avpair-value&gt;"
    
                Examples
                    cisco-avpair = "app-attr=attrname1:type:attrvalue1"
                    cisco-avpair = "app-attr=attrname2:type:attrvalue2"
    
               Currently String and Integer are supported for the type.
        """


    def __init__(self, type_, name):
        """
        Create a AAA Attribute that has the specified type.
        This constructor creates an Attribute with the given Attribute type and name.
        The Application-specific attributes are keyed on attribute names, hence the name parameters are
        required parameters for application-specific attributes.
        @raise OnepIllegalArgumentException: if name is null for application
        """
        Attribute.log = logging.getLogger(__name__)
        if type_ == None:
            raise OnepIllegalArgumentException('The type_ parameter is None')
        if type_ == OnepAAAAttributeType.ONEP_AAA_AT_APP_ATTR and name == None:
            raise OnepIllegalArgumentException('The name parameter is None')
        self.type_ = type_
        self.name = name



    def toIDL(self, network_element):
        """For internal use only"""
        format = None
        attrIDL = None
        byteList = []
        from onep.aaa.IntAttribute import IntAttribute
        from onep.aaa.StringAttribute import StringAttribute
        from onep.aaa.BinaryAttribute import BinaryAttribute
        from onep.aaa.AddressAttribute import AddressAttribute
        if isinstance(self, IntAttribute):
            format = AttrFormat_e.AAA_TYPE_FORMAT_ULONG
            if self.type_ == OnepAAAAttributeType.ONEP_AAA_AT_APP_ATTR:
                value = self.name + ':uint32:' + str(self.long_value)
                attrIDL = Attribute_IDL(self.type_, AttrFormat_e.AAA_TYPE_FORMAT_STRING, value, 0, byteList)
            else:
                attrIDL = Attribute_IDL(self.type_, format, '', self.long_value, byteList)
        elif isinstance(self, StringAttribute):
            format = AttrFormat_e.AAA_TYPE_FORMAT_STRING
            if self.type_ == OnepAAAAttributeType.ONEP_AAA_AT_APP_ATTR:
                value = self.name + ':string:' + self.str_value
                attrIDL = Attribute_IDL(self.type_, AttrFormat_e.AAA_TYPE_FORMAT_STRING, value, 0, byteList)
            elif self.type_ == OnepAAAAttributeType.ONEP_AAA_AT_ALLOWED_ACTION:
                value = network_element.appname + ':string:' + self.str_value
                attrIDL = Attribute_IDL(self.type_, AttrFormat_e.AAA_TYPE_FORMAT_STRING, value, 0, byteList)
            attrIDL = Attribute_IDL(self.type_, format, self.str_value, 0, byteList)
        elif isinstance(self, BinaryAttribute):
            format = AttrFormat_e.AAA_TYPE_FORMAT_BINARY
            byteList = self.binary_data
            attrIDL = Attribute_IDL(self.type_, format, '', 0, byteList)
        elif isinstance(self, AddressAttribute):
            try:
                if HostIpCheck(self.address).is_ipv4():
                    format = AttrFormat_e.AAA_TYPE_FORMAT_IP_ADDR
                if HostIpCheck(self.address).is_ipv6():
                    format = AttrFormat_e.AAA_TYPE_FORMAT_IPV6_ADDR
                attrIDL = Attribute_IDL(self.type_, format, self.address, 0, byteList)
            except OnepException as e:
                self.log.error('Error retrieving InetAddress from Attribute list')
        else:
            self.log.error('Invalid attribute type')
        return attrIDL



    @classmethod
    def toIDLList(cls, attrList, network_element):
        """For internal use only"""
        if attrList == None:
            return []
        attrIdlList = []
        for attr in attrList:
            attrIdl = attr.toIDL(network_element)
            if attrIdl != None:
                attrIdlList.append(attrIdl)

        return attrIdlList



    @classmethod
    def fromIDL(cls, attrIDL, network_element):
        """For internal use only"""
        if attrIDL == None:
            return 
        attr = None
        attrName = None
        format = AttrFormat_e()
        if not network_element.is_connected():
            cls.log.debug('Application is not connected to network element ' + network_element.host_address)
            return 
        if network_element.session_handle == None:
            cls.log.debug('Application is not connected to network element ' + network_element.host_address)
            return 
        format = attrIDL.format
        try:
            attrType = attrIDL.type
        except OnepIllegalArgumentException as e1:
            cls.log.error('Error adding attribute type ' + str(attrIDL.type) + ' to list, possible enum mismatch')
            return 
        if attrIDL.type == OnepAAAAttributeType.ONEP_AAA_AT_APP_ATTR:
            appAttrValue = attrIDL.str_value
            if appAttrValue.startswith('"') and appAttrValue.endswith('"'):
                appAttrValue = appAttrValue.substring[1:-1]
            appValue = appAttrValue.split(':')
            if len(appValue) < 3:
                cls.log.error('Invalid app attribute format')
                return 
            attrName = appValue[0]
            try:
                if appValue[1].lower() == 'string':
                    attr = StringAttribute(attrType, attrName, appValue[2])
                else:
                    attr = IntAttribute(attrType, attrName, int(appValue[2]))
            except OnepIllegalArgumentException as e:
                cls.log.error('Error adding a Application attribute type ' + str(appValue))
                return 
        elif format == AttrFormat_e.AAA_TYPE_FORMAT_ULONG:
            try:
                attr = IntAttribute(attrType, None, attrIDL.ulong_value)
            except OnepIllegalArgumentException as e:
                cls.log.error('Error adding  attribute type ' + str(attrType))
                return 
        elif format == AttrFormat_e.AAA_TYPE_FORMAT_STRING:
            try:
                attr = StringAttribute(attrType, None, attrIDL.str_value)
            except OnepIllegalArgumentException as e:
                cls.log.error('Error adding  attribute type ' + str(attrType))
                return 
        elif format == AttrFormat_e.AAA_TYPE_FORMAT_BINARY:
            try:
                attr = BinaryAttribute(attrType, None, attrIDL.binary_value)
            except OnepIllegalArgumentException as e:
                cls.log.error('Error adding  attribute type ' + str(attrType))
                return 
        else:
            try:
                attr = AddressAttribute(attrType, None, str_value)
            except UnknownHostException as e:
                cls.log.error('Error translating IP address ' + str(e))
                return 
            except OnepIllegalArgumentException as e:
                cls.log.error('Error adding  attribute type ' + str(attrType))
                return 
        return attr



    @classmethod
    def fromIDLList(cls, attrIdlList, network_element):
        """For internal use only"""
        if attrIdlList == None:
            return 
        attrList = []
        for attrIdl in attrIdlList:
            if attr != None:
                attrList.append(attr)

        return attrList



Attribute.log = None

# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:20:33 IST
