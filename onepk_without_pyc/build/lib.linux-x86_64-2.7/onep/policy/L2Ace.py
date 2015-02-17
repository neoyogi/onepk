# 2015.02.05 17:19:23 IST
from onep.element.NetworkElement import NetworkElement
from array import array
from onep.PolicyIDL.ttypes import L2AceParam_IDL
from onep.core.exception.OnepIllegalArgumentException import OnepIllegalArgumentException
from onep.core.exception.OnepConnectionException import OnepConnectionException
from onep.core.exception.OnepRemoteProcedureException import OnepRemoteProcedureException
from Shared.ttypes import ExceptionIDL
from onep.thrift.Thrift import TException
import logging
from ctypes import c_int, c_uint

class L2Ace(object):
    """ L2 Access Control Element (ACE) Class.
    
        It defines a set of attributes for matching a packet.
        One or more ACEs may be added to an Access Control List (ACL).
        
        @undocumented: sequence
        """


    def _set_sequence(self, sequence):
        try:
            self._validate_sequence(sequence)
        except OnepIllegalArgumentException as e:
            raise e
        self._sequence = sequence



    def _get_sequence(self):
        return self._sequence


    _doc = '\n    Sequence number denotes position of L2 Access Control Element(ACE) in the L2 Access Control List(ACL).\n\n    Raises: OnepIllegalArgumentException - If sequence number is invalid.\n\n    @type: C{int}\n    '
    sequence = property(_get_sequence, _set_sequence, None, _doc)

    def _set_permit(self, permit):
        try:
            self._validate_permit(permit)
        except OnepIllegalArgumentException as e:
            raise e
        self._permit = permit



    def _get_permit(self):
        return self._permit


    _doc = '\n    Permit/Deny for L2 Access Control Element(ACE).\n\n    Set TRUE for permit.\n\n    Set FALSE for deny.\n\n    Raises: OnepIllegalArgumentException - If permit is invalid.\n\n    @type: C{bool}\n    '
    permit = property(_get_permit, _set_permit, None, _doc)

    def _set_src_mac(self, addr):
        try:
            self._validate_mac(addr, 'Source')
        except OnepIllegalArgumentException as e:
            raise e
        (pos, self._src_mac,) = self._convert_to_thrift_array(addr)
        if self._src_mac == None:
            raise OnepIllegalArgumentException('Mac address byte:' + str(pos) + ' is not set to valid(0x00 <= Byte <= 0xFF) byte range')



    def _get_src_mac(self):
        (pos, src_mac_array,) = self._thrift_to_hex_array(self._src_mac)
        return src_mac_array


    _doc = '\n    Source mac address.\n\n    List or Array of length six represents mac address.\n\n    List position or an array index represents single byte of mac address.\n\n    Raises: OnepIllegalArgumentException - If source mac address is invalid.\n\n    @type: C{list} or C{array}\n    '
    src_mac = property(_get_src_mac, _set_src_mac, None, _doc)

    def _set_src_mac_mask(self, mask):
        try:
            self._validate_mac_mask(mask, 'Source')
        except OnepIllegalArgumentException as e:
            raise e
        (pos, self._src_mac_mask,) = self._convert_to_thrift_array(mask)
        if self._src_mac_mask == None:
            raise OnepIllegalArgumentException('Mac address mask byte:' + str(pos) + ' is not set to valid(0x00 <= Byte <= 0xFF) byte range')



    def _get_src_mac_mask(self):
        (pos, src_mac_mask_array,) = self._thrift_to_hex_array(self._src_mac_mask)
        return src_mac_mask_array


    _doc = '\n    Source mac address mask.\n\n    Raises: OnepIllegalArgumentException - If source mac address mask is invalid.\n\n    @type: C{list} or C{array}\n    '
    src_mac_mask = property(_get_src_mac_mask, _set_src_mac_mask, None, _doc)

    def _set_dst_mac(self, addr):
        try:
            self._validate_mac(addr, 'Destination')
        except OnepIllegalArgumentException as e:
            raise e
        (pos, self._dst_mac,) = self._convert_to_thrift_array(addr)
        if self._dst_mac == None:
            raise OnepIllegalArgumentException('Mac address byte:' + str(pos) + ' is not set to valid(0x00 <= Byte <= 0xFF) byte range')



    def _get_dst_mac(self):
        (pos, dst_mac_array,) = self._thrift_to_hex_array(self._dst_mac)
        return dst_mac_array


    _doc = '\n    Destination mac address.\n\n    List or Array of length six represents mac address.\n\n    List position or an array index represents single byte of mac address.\n\n    Raises: OnepIllegalArgumentException - If destination mac address is invalid.\n\n    @type: C{list} or C{array}\n    '
    dst_mac = property(_get_dst_mac, _set_dst_mac, None, _doc)

    def _set_dst_mac_mask(self, mask):
        try:
            self._validate_mac_mask(mask, 'Destination')
        except OnepIllegalArgumentException as e:
            raise e
        (pos, self._dst_mac_mask,) = self._convert_to_thrift_array(mask)
        if self._dst_mac_mask == None:
            raise OnepIllegalArgumentException('Mac address mask byte:' + str(pos) + ' is not set to valid(0x00 <= Byte <= 0xFF) byte range')



    def _get_dst_mac_mask(self):
        (pos, dst_mac_mask_array,) = self._thrift_to_hex_array(self._dst_mac_mask)
        return dst_mac_mask_array


    _doc = '\n    Destination mac address mask.\n\n    Raises: OnepIllegalArgumentException - If destination mac address mask is invalid.\n\n    @type: C{list} or C{array}\n    '
    dst_mac_mask = property(_get_dst_mac_mask, _set_dst_mac_mask, None, _doc)

    def _thrift_to_hex_array(self, mac_address):
        if mac_address == None:
            return (0, None)
        mac_hex_array = list()
        item_pos = 0
        for item in mac_address:
            item_pos += 1
            if item > 127 or item < -128:
                return (item_pos, None)
            if item < 0:
                mac_hex_array.append(hex(item + 256))
            else:
                mac_hex_array.append(hex(item))

        return (0, mac_hex_array)



    def _convert_to_thrift_array(self, mac_address):
        mac_thrift_array = list()
        item_pos = 0
        for item in mac_address:
            item_pos += 1
            if item > 255 or item < 0:
                return (item_pos, None)
            if item > 127:
                mac_thrift_array.append(item - 256)
            else:
                mac_thrift_array.append(item)

        return (0, mac_thrift_array)



    def _thrift_to_hex_string(self, mac_array):
        hex_str = str()
        for i in mac_array:
            if i < 0:
                hex_str += str(hex(i + 256))
            else:
                hex_str += str(hex(i))
            hex_str += ' '

        return hex_str



    def _validate_mac(self, addr, src_dst):
        if addr == None:
            raise OnepIllegalArgumentException(src_dst + ' Mac address', 'None')
        if not isinstance(addr, list) and not isinstance(addr, array):
            raise OnepIllegalArgumentException(src_dst + ' Mac address is not of type list or array')
        if len(addr) != 6:
            raise OnepIllegalArgumentException('Invalid ' + src_dst + ' mac address length')



    def _validate_mac_mask(self, mask, src_dst):
        if mask == None:
            raise OnepIllegalArgumentException(src_dst + ' Mac address mask', 'None')
        if not isinstance(mask, list) and not isinstance(mask, array):
            raise OnepIllegalArgumentException(src_dst + ' Mac address mask is not of type list or array')
        if len(mask) != 6:
            raise OnepIllegalArgumentException('Invalid ' + src_dst + ' mac address mask length')



    def _validate_sequence(self, sequence):
        if sequence == None:
            raise OnepIllegalArgumentException('Sequence number', 'None')
        if not isinstance(sequence, (int, long)):
            raise OnepIllegalArgumentException('Sequence number is not of type int')
        if sequence < 0:
            raise OnepIllegalArgumentException('Sequence number', 'negative')



    def _validate_permit(self, permit):
        if permit == None:
            raise OnepIllegalArgumentException('permit', 'None')
        if not isinstance(permit, bool):
            raise OnepIllegalArgumentException('permit is not of type bool')



    def __init__(self, sequence, permit):
        """ Constructor of class L2Ace.
        
                Instantiate a new L2 Access Control Element(ACE)::
                    ACE Properties are initialized as follows:
                    Source Mac address:           0x00:0x00:0x00:0x00:0x00:0x00
                    Source Mac address mask:      0xff:0xff:0xff:0xff:0xff:0xff
                    Destination Mac address:      0x00:0x00:0x00:0x00:0x00:0x00
                    Destination Mac address mask: 0xff:0xff:0xff:0xff:0xff:0xff
        
                @param sequence: Position of L2 ACE in the L2 Access Control List(ACL).
                @type sequence: C{int}
                @param permit: pass TRUE for permit, pass FALSE for deny.
                @type permit: C{bool}
        
                @raise OnepIllegalArgumentException: If sequence number or permit is invalid.
                """
        self.log = logging.getLogger(__name__)
        try:
            self.sequence = sequence
            self.permit = permit
        except OnepIllegalArgumentException as e:
            raise e
        self._acl = None
        self._ace_handle = 0
        self._src_mac = [0,
         0,
         0,
         0,
         0,
         0]
        self._dst_mac = [0,
         0,
         0,
         0,
         0,
         0]
        self._src_mac_mask = [-1,
         -1,
         -1,
         -1,
         -1,
         -1]
        self._dst_mac_mask = [-1,
         -1,
         -1,
         -1,
         -1,
         -1]



    def _add_to_l2_acl(self, acl):
        """
        """
        if self._acl != None:
            raise OnepIllegalArgumentException('ace is already added to acl')
        try:
            self._validate_sequence(self._sequence)
            self._validate_permit(self._permit)
            self._validate_mac(self._src_mac, 'Source')
            self._validate_mac_mask(self._src_mac_mask, 'Source')
            self._validate_mac(self._dst_mac, 'Destination')
            self._validate_mac_mask(self._dst_mac_mask, 'Destination')
        except OnepIllegalArgumentException as e:
            raise e
        self.log.info('Basic Validation of all L2-ace parameters completed.')
        self._acl = acl
        ace_param = L2AceParam_IDL(c_int(self._sequence).value, self._permit, self._src_mac, self._src_mac_mask, self._dst_mac, self._dst_mac_mask)
        self.log.info('Successfully created L2-ace parameters through idl call L2AceParam_IDL')
        try:
            self._ace_handle = acl._acl_client.addL2Ace_IDL(acl._acl_handle, ace_param)
            self.log.info('Returned from addL2Ace_IDL idl call to add a L2-ace in L2-acl')
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e.message, e)



    def _remove_from_l2_acl(self, acl):
        """
        """
        try:
            self._ace_handle = acl._acl_client.deleteAce_IDL(acl._acl_handle, self._ace_handle)
            self.log.info('Returned from deleteAce_IDL idl call to remove a L2-ace from L2-acl')
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e.message, e)
        self._acl = None



    def __str__(self):
        """ Returns a string representation of the L2 Access Control Element(ACE) instance.
        
                @rtype: C{str}
                @return: String representation of the L2 ACE.
                """
        sb = '\nL2 ACE [ ' + str(self._ace_handle) + ' ]\n'
        sb += '\tSequence Num : ' + str(self._sequence) + '\n'
        sb += '\tPermit       : ' + str(self._permit) + '\n'
        sb += '\tSrc MAC      : ' + self._thrift_to_hex_string(self._src_mac) + '\n'
        sb += '\tSrc MAC mask : ' + self._thrift_to_hex_string(self._src_mac_mask) + '\n'
        sb += '\tDst MAC      : ' + self._thrift_to_hex_string(self._dst_mac) + '\n'
        sb += '\tDst MAC mask : ' + self._thrift_to_hex_string(self._dst_mac_mask) + '\n'
        return sb




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:19:24 IST
