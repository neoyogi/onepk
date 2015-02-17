# 2015.02.05 17:22:48 IST
from abc import *
from onep.interfaces.NetworkInterface import NetworkInterface
import socket
import onep.core.util.socket_imp
from onep.core.util.Enum import *
from onep.core.util.OnepArgumentTypeValidate import *
from onep.core.exception.OnepIllegalArgumentException import OnepIllegalArgumentException
from onep.core.exception.OnepConnectionException import OnepConnectionException
from onep.core.exception.OnepRemoteProcedureException import OnepRemoteProcedureException
from onep.core.util.OnepConstants import OnepConstants
from Shared.ttypes import ExceptionIDL
from onep.thrift.Thrift import TException
from onep.PolicyBulkIDL.ttypes import MatchIDL
from onep.PolicyBulkIDL.ttypes import MatchPktLenIDL
from onep.PolicyBulkIDL.ttypes import MatchL2CosIDL
from onep.PolicyBulkIDL.ttypes import MatchQosGroupIDL
from onep.PolicyBulkIDL.ttypes import MatchApplicationIDL
from onep.PolicyBulkIDL.ttypes import MatchIcmpIDL
from onep.PolicyBulkIDL.ttypes import MatchEtypeIDL
from onep.PolicyBulkIDL.ttypes import MatchTtlIDL
from onep.PolicyBulkIDL.ttypes import MatchDscpIDL
from onep.PolicyBulkIDL.ttypes import MatchMplsExpIDL
from onep.PolicyBulkIDL.ttypes import MatchInterfaceIDL
from onep.PolicyBulkIDL.ttypes import MatchTcpPortIDL
from onep.PolicyBulkIDL.ttypes import MatchRtpPortIDL
from onep.PolicyBulkIDL.ttypes import MatchTcpFlagsIDL
from onep.PolicyBulkIDL.ttypes import MatchVlanIDL
from onep.PolicyBulkIDL.ttypes import MatchAclIDL
from onep.PolicyBulkIDL.ttypes import MatchMacAddressIDL
from onep.PolicyBulkIDL.ttypes import MatchIpAddressIDL
from onep.PolicyBulkIDL.ttypes import MatchProtocolIDL
import logging
from ctypes import c_byte, c_short, c_ushort
from onep.core.util.HostIpCheck import HostIpCheck
from onep.core.util import deprecated
Direction = enum('SOURCE', 'DESTINATION')
MatchOperator = enum('MATCH_OPERATOR_AND', 'MATCH_OPERATOR_OR', 'MATCH_OPERATOR_NOT')
MatchType = enum(MATCH_NONE=0, MATCH_ACL=1, MATCH_IP_DSCP=2, MATCH_FR_DE=3, MATCH_FR_DLCI=4, MATCH_INTERFACE=5, MATCH_L2_COS=6, MATCH_DST_MAC_ADDRESS=7, MATCH_SRC_MAC_ADDRESS=8, MATCH_MPLS_EXP=9, MATCH_PKT_LEN=10, MATCH_QOS_GROUP=11, MATCH_PROTOCOL=12, MATCH_RTP_PORT=13, MATCH_VLAN=14, MATCH_VRF=15, MATCH_DST_IP_ADDRESS=16, MATCH_SRC_IP_ADDRESS=17, MATCH_DST_TCP_PORT=18, MATCH_SRC_TCP_PORT=19, MATCH_IP_PROTOCOL=20, MATCH_ETYPE=21, MATCH_IP_TOS=22, MATCH_MPLS_LABEL=23, MATCH_IN_PHYSICAL_PORT=24, MATCH_METADATA=25, MATCH_ICMPV4_TYPE=26, MATCH_ICMPV4_CODE=27, MATCH_ICMPV6_TYPE=28, MATCH_ICMPV6_CODE=29, MATCH_IPV6_SRC=30, MATCH_IPV6_DST=31, MATCH_IPV6_FLABEL=32, MATCH_IPV6_ND_TARGET=33, MATCH_IPV6_ND_SLL=34, MATCH_IPV6_ND_TLL=35, MATCH_MPLS_BOS=36, MATCH_PBB_ISID=37, MATCH_TUNNEL_ID=38, MATCH_IPV6_EXTHDR=39, MATCH_ARP_SPA=40, MATCH_ARP_TPA=41, MATCH_ARP_SHA=42, MATCH_ARP_THA=43, MATCH_PMAP=44, MATCH_APPLICATION=45, MATCH_TCP_FLAGS=46, MATCH_IP_TTL=47, MATCH_MPLS_TC=48, MATCH_IPV6_FLOW_LABEL=49, MATCH_LAST=50)
_map_external_match = {0: 0,
 1: 1,
 2: 2,
 3: 3,
 4: 4,
 5: 5,
 6: 6,
 7: 7,
 8: 7,
 9: 8,
 10: 9,
 11: 10,
 12: 11,
 20: 11,
 45: 12,
 13: 13,
 14: 14,
 21: 15,
 16: 16,
 17: 16,
 18: 17,
 19: 17,
 46: 18,
 26: 19,
 27: 19,
 28: 19,
 29: 19,
 30: 16,
 31: 16,
 47: 21}

class Match(object):
    """
        The Match class is an abstract class that represents a match specified in the class map.
        
        There may be one or more Match objects in a ClassMap object or directly in an Entry object
        of a PolicyMap object (referred to as an inline class).  There are different types
        of Match objects that specify details of each match criteria to be matched.  The different
        types of Match are specified by different classes extended from Match.
    
        ***DEPRECATED***
        MatchType in Match class is deprecated
        Please use match.MatchType
        ****************
    
        """

    __metaclass__ = ABCMeta
    _internal_match_type = enum(MATCH_NONE=0, MATCH_ACL=1, MATCH_IP_DSCP=2, MATCH_FR_DE=3, MATCH_FR_DLCI=4, MATCH_INTERFACE=5, MATCH_L2_COS=6, MATCH_MAC_ADDRESS=7, MATCH_MPLS_EXP=8, MATCH_PKT_LEN=9, MATCH_QOS_GROUP=10, MATCH_PROTOCOL=11, MATCH_APPLICATION=12, MATCH_RTP_PORT=13, MATCH_VLAN=14, MATCH_ETYPE=15, MATCH_IP_ADDRESS=16, MATCH_TCP_PORT=17, MATCH_TCP_FLAGS=18, MATCH_ICMP=19, MATCH_IP_TOS=20, MATCH_IP_TTL=21)
    _map_internal_match = {0: MatchType.MATCH_NONE,
     1: MatchType.MATCH_ACL,
     2: MatchType.MATCH_IP_DSCP,
     3: MatchType.MATCH_FR_DE,
     4: MatchType.MATCH_FR_DLCI,
     5: MatchType.MATCH_INTERFACE,
     6: MatchType.MATCH_L2_COS,
     8: MatchType.MATCH_MPLS_EXP,
     9: MatchType.MATCH_PKT_LEN,
     10: MatchType.MATCH_QOS_GROUP,
     11: MatchType.MATCH_IP_PROTOCOL,
     12: MatchType.MATCH_APPLICATION,
     13: MatchType.MATCH_RTP_PORT,
     14: MatchType.MATCH_VLAN,
     15: MatchType.MATCH_ETYPE,
     18: MatchType.MATCH_TCP_FLAGS,
     20: MatchType.MATCH_IP_TOS,
     21: MatchType.MATCH_IP_TTL}
    MatchOpCode = enum('CREATE', 'MOD', 'DEL', 'ADD', 'REM')
    MatchType = MatchType

    def __init__(self, match_type):
        """ Constructs Match.
        """
        self._match_type = match_type
        self._sense = 1
        self._op_code = Match.MatchOpCode.CREATE
        self._handle = 0
        self.dependent_match = None
        self.log = logging.getLogger(__name__)



    def check_match_support(self, capable_matches):
        """  
                Check to see if class match is supported on network element
        
                @param capable_matches: list of MatchType from network element
                @type capable_matches: L{MatchType<match.MatchType>}
        
                @return: Returns True if supported False if not
                @rtype: C{bool}
        
                """
        self.log.debug('MATCH CAPS ' + str(capable_matches))
        m_type = None
        if hasattr(self, '_external_type'):
            m_type = self._external_type
            self.log.debug('external type ' + MatchType.enumval(m_type))
        else:
            m_type = self._map_internal_match[self._match_type]
            self.log.debug('external type mapped ' + MatchType.enumval(m_type))
        return m_type in capable_matches



    def get_match_type(self):
        """  
                Return MatchType of match class
        
                @return: Return MatchType of match
                @rtype: {MatchType<match.MatchType>}
        
                """
        if hasattr(self, '_external_type'):
            return self._external_type
        else:
            return self._map_internal_match[self._match_type]



    @property
    def match_type(self):
        return self._match_type



    def set_negate(self, sense_value):
        """ Sets whether this is a "match not" statement. 
        
        @param sense_value: Pass in true if it is match not. Otherwise pass in false.
        @type sense_value: C{bool}
        """
        try:
            validate(sense_value, bool)
        except OnepIllegalArgumentException as e:
            raise e
        self._sense = int(sense_value)



    @classmethod
    def _to_idl_list(cls, inst_list):
        """
        """
        idl_list = []
        for inst in inst_list:
            idl_list.append(inst._to_idl())

        return idl_list



    @classmethod
    def _from_idl_list(cls, idl_list, element):
        """
        """
        idl_list = list()
        for idl in idl_list:
            if idl.matchType == cls._internal_match_type.MATCH_ACL:
                idl_list.append(ACL._from_idl(idl, element))
            elif idl.matchType == cls._internal_match_type.MATCH_IP_DSCP:
                idl_list.append(DSCP._from_idl(idl))
            elif idl.matchType == cls._internal_match_type.MATCH_FR_DE:
                pass
            elif idl.matchType == cls._internal_match_type.MATCH_FR_DLCI:
                pass
            elif idl.matchType == cls._internal_match_type.MATCH_INTERFACE:
                idl_list.append(InputInterface._from_idl(idl, element))
            elif idl.matchType == cls._internal_match_type.MATCH_L2_COS:
                idl_list.append(L2CoS._from_idl(idl))
            elif idl.matchType == cls._internal_match_type.MATCH_MAC_ADDRESS:
                idl_list.append(MACAddress._from_idl(idl))
            elif idl.matchType == cls._internal_match_type.MATCH_MPLS_EXP:
                idl_list.append(MPLSExperimental._from_idl(idl))
            elif idl.matchType == cls._internal_match_type.MATCH_PKT_LEN:
                idl_list.append(PacketLength._from_idl(idl))
            elif idl.matchType == cls._internal_match_type.MATCH_QOS_GROUP:
                idl_list.append(QOSGroup._from_idl(idl))
            elif idl.matchType == cls._internal_match_type.MATCH_PROTOCOL:
                idl_list.append(IpProtocol._from_idl(idl))
            elif idl.matchType == cls._internal_match_type.MATCH_RTP_PORT:
                idl_list.append(RTPPort._from_idl(idl))
            elif idl.matchType == cls._internal_match_type.MATCH_VLAN:
                idl_list.append(VLAN._from_idl(idl))
            elif idl.matchType == cls._internal_match_type.MATCH_ETYPE:
                idl_list.append(EtherType._from_idl(idl))
            elif idl.matchType == cls._internal_match_type.MATCH_IP_ADDRESS:
                idl_list.append(IPAddress._from_idl(idl))
            elif idl.matchType == cls._internal_match_type.MATCH_TCP_PORT:
                idl_list.append(Port._from_idl(idl))
            elif idl.matchType == cls._internal_match_type.MATCH_TCP_FLAGS:
                idl_list.append(TCPFlags._from_idl(idl))
            elif idl.matchType == cls._internal_match_type.MATCH_ICMP:
                idl_list.append(ICMP._from_idl(idl))
            elif idl.matchType == cls._internal_match_type.MATCH_IP_TOS:
                pass
            elif idl.matchType == cls._internal_match_type.MATCH_IP_TTL:
                idl_list.append(TTL._from_idl(idl))

        return idl_list




class PacketLength(Match):
    """ PacketLength Class.
    
    Packet Length Math. This specifies the Layer 3 packet length in the IP header as match criterion in a classmap.
    
    @undocumented: min
    MatchOperator: max
    """


    def _get_min(self):
        return self._min


    _doc_min = ' Minimum packet length.\n    \n    @type: C{int}\n    '
    min = property(_get_min, None, None, _doc_min)

    def _get_max(self):
        return self._max


    _doc_max = ' Maximum packet length.\n    \n    @type: C{int}\n    '
    max = property(_get_max, None, None, _doc_max)

    def __init__(self, min, max):
        """ Constructs a packet length match.
        
        @param min: Minimum packet length.
        @type min: C{int}
        @param max: Maximum packet length.
        @type max: C{int} 
        
        @raise OnepIllegalArgumentException: If any of constructor parameter is invalid.
        """
        super(PacketLength, self).__init__(self._internal_match_type.MATCH_PKT_LEN)
        validate(min, int)
        validate(max, int)
        if min > max:
            raise OnepIllegalArgumentException('min > max')
        self._min = min
        self._max = max



    def __eq__(self, obj):
        """
        """
        try:
            validate(obj, PacketLength)
        except OnepIllegalArgumentException as e:
            return False
        if self is obj:
            return True
        else:
            if self._min == obj._min and self._max == obj._max:
                return True
            return False



    def _to_idl(self):
        """
        """
        idl = MatchIDL(0, 0, 0, 0, 0)
        idl.matchType = self._match_type
        idl.pktLenMatch = MatchPktLenIDL(self._sense, self._min, self._max)
        idl.opCode = self._op_code
        return idl



    @classmethod
    def _from_idl(cls, idl):
        """
        """
        if idl == None:
            return 
        mt = PacketLength(idl.pktLenMatch.min, idl.pktLenMatch.max)
        mt.set_negate(False if idl.pktLenMatch.sense == 0 else True)
        mt._handle = idl.matchHandle
        return mt




class L2Cos(Match):
    """ L2Cos Class.
    
    L2 COS match. This matches a packet on the basis of a Layer 2 class of service (CoS)/Inter-Switch Link (ISL) marking.
    
    @undocumented: l2cos_list
    """


    def _get_l2cos_list(self):
        if len(self._l2cos_list) > 0:
            return self._l2cos_list


    _doc_l2cos_list = ' L2Cos List.\n    \n    @type: C{list}\n    '
    l2cos_list = property(_get_l2cos_list, None, None, _doc_l2cos_list)

    def __init__(self, *l2cos):
        """ Constructs a L2CoS match.
        
        The CoS is from 0 to 7.
        
        Ignores an invalid l2cos value in *l2cos, if present.
                    
        @param l2cos: List of specific IEEE 802.1Q/ISL CoS value.
        @type l2cos: Variable length argument list of C{int}       
        
        @raise OnepIllegalArgumentException: If all l2cos values in *l2cos are invalid. 
        """
        super(L2Cos, self).__init__(self._internal_match_type.MATCH_L2_COS)
        self._l2cos_list = []
        for l2_cos in l2cos:
            if isinstance(l2_cos, int):
                if l2_cos >= 0 and l2_cos <= 7:
                    self._l2cos_list.append(l2_cos)
                else:
                    raise OnepIllegalArgumentException('L2 COS must be between 0 - 7')

        if len(self._l2cos_list) == 0:
            raise OnepIllegalArgumentException('No l2cos value is valid in l2cos.')



    def __eq__(self, obj):
        """
        """
        try:
            validate(obj, L2Cos)
        except OnepIllegalArgumentException as e:
            return False
        if self is obj:
            return True
        else:
            if self._l2cos_list == obj._l2cos_list:
                return True
            return False



    def _to_idl(self):
        """
        """
        idl = MatchIDL(0, 0, 0, 0, 0)
        idl.matchType = self._match_type
        idl.l2cosMatch = MatchL2CosIDL(self._sense, self._l2cos_list)
        idl.opCode = self._op_code
        return idl



    @classmethod
    def _from_idl(cls, idl):
        """
        """
        if idl == None:
            return 
        mt = L2Cos(idl.l2cosMatch.l2cos)
        mt.set_negate(False if idl.l2cosMatch.sense == 0 else True)
        mt._handle = idl.matchHandle
        return mt




class DSCP(Match):
    """ DSCP class.
    
    Match on DSCP. This identifies one or more differentiated service code point (DSCP), 
    Assured Forwarding (AF), and Class Selector (CS) values as a match criterion.
    
    @undocumented: dscp_byte_array
    """


    def _get_dscp_byte_array(self):
        if len(self._dscp_byte_array) > 0:
            return self._dscp_byte_array


    _doc_dscp_byte_array = ' DSCP List.\n    \n    @type: C{bytearray}\n    '
    dscp_byte_array = property(_get_dscp_byte_array, None, None, _doc_dscp_byte_array)

    def __init__(self, *dscps):
        """ Constructs a DSCP match.
        
        Ignores an invalid dscp value in *dscps, if present.
                    
        @param dscps: List of dscp value.
        @type dscps: Variable length argument list of C{int}       
        
        @raise OnepIllegalArgumentException: If all dscp values in *dscps are invalid. 
        """
        super(DSCP, self).__init__(self._internal_match_type.MATCH_IP_DSCP)
        if isinstance(dscps[0], bytearray):
            self._dscp_byte_array = dscps[0]
        else:
            self._dscp_byte_array = bytearray()
            for dscp in dscps:
                if isinstance(dscp, int):
                    if dscp < 0 or dscp > 63:
                        raise OnepIllegalArgumentException('DSCP must be 0 to 63')
                    self._dscp_byte_array.append(dscp)

        if len(self._dscp_byte_array) == 0:
            raise OnepIllegalArgumentException('No dscp value is valid in dscps.')



    def __eq__(self, obj):
        """
        """
        try:
            validate(obj, DSCP)
        except OnepIllegalArgumentException as e:
            return False
        if self is obj:
            return True
        else:
            if self._dscp_byte_array == obj._dscp_byte_array:
                return True
            return False



    def _to_idl(self):
        """
        """
        idl = MatchIDL(0, 0, 0, 0, 0)
        idl.matchType = self._match_type
        idl.dscpMatch = MatchDscpIDL(self._sense, self._dscp_byte_array)
        idl.opCode = self._op_code
        return idl



    @classmethod
    def _from_idl(cls, idl):
        """
        """
        if idl == None:
            return 
        temp_dscp_bytearray = bytearray()
        for dscp_val in idl.dscpMatch.dscp:
            temp_dscp_bytearray.append(dscp_val)

        mt = DSCP(temp_dscp_bytearray)
        mt.set_negate(False if idl.dscpMatch.sense == 0 else True)
        mt._handle = idl.matchHandle
        return mt




class VLAN(Match):
    """ VLAN class.
    
    Match on top most VLAN ID. This matches and classifies traffic on the basis of 
    the virtual local area network (VLAN) identification number.
    
    @undocumented: vlan_list
    """


    def _get_vlan_list(self):
        if len(self._vlan_list) > 0:
            return self._vlan_list


    _doc_vlan_list = ' VLAN Id List.\n    \n    @type: C{list}\n    '
    vlan_list = property(_get_vlan_list, None, None, _doc_vlan_list)

    def __init__(self, *vlan_ids):
        """ Constructs a VLAN match.
        
        Valid vlan id number must be in the range of 1 to 4095.
        
        Ignores an invalid vlan id value in *vlan_ids, if present.
                    
        @param vlan_ids: List of specific IEEE 802.1Q/ISL CoS value.
        @type vlan_ids: Variable length argument list of C{int}       
        
        @raise OnepIllegalArgumentException: If all vlan id in *vlan_ids are invalid.
        """
        super(VLAN, self).__init__(self._internal_match_type.MATCH_VLAN)
        if isinstance(vlan_ids[0], list):
            self._vlan_list = vlan_ids[0]
        else:
            self._vlan_list = list()
            for vlan in vlan_ids:
                if isinstance(vlan, int):
                    if vlan >= 1 and vlan <= 4095:
                        self._vlan_list.append(vlan)

        if len(self._vlan_list) == 0:
            raise OnepIllegalArgumentException('No vlan id value is valid in vlan_ids.')



    def __eq__(self, obj):
        """
        """
        try:
            validate(obj, VLAN)
        except OnepIllegalArgumentException as e:
            return False
        if self is obj:
            return True
        else:
            if self._vlan_list == obj._vlan_list:
                return True
            return False



    def _to_idl(self):
        """
        """
        idl = MatchIDL(0, 0, 0, 0, 0)
        idl.matchType = self._match_type
        idl.vlanMatch = MatchVlanIDL(self._sense, self._vlan_list)
        idl.opCode = self._op_code
        return idl



    @classmethod
    def _from_idl(cls, idl):
        """
        """
        if idl == None:
            return 
        mt = VLAN(idl.vlanMatch.vlan)
        mt.set_negate(False if idl.vlanMatch.sense == 0 else True)
        mt._handle = idl.matchHandle
        return mt




class MPLSExperimental(Match):
    """ MPLSExperimental class.
    
    MPLS Experimental tag match. This configure a class map to use the specified value or 
    values of the experimental (EXP) field as a match criteria.
    
    @undocumented: mpls_experimental_list
    """


    def _get_mpls_experimental_list(self):
        if len(self._mpls_exp_list) > 0:
            return self._mpls_exp_list


    _doc_mpls_experimental_list = ' MPLS Experimental List.\n    \n    @type: C{list}\n    '
    mpls_experimental_list = property(_get_mpls_experimental_list, None, None, _doc_mpls_experimental_list)

    def __init__(self, *mpls_exps):
        """ Constructs a MPLS Experimental match.
        
        Valid range of mpls value is 0 to 7.
        
        Ignores an invalid mpls value in *mpls_exps, if present.
                    
        @param mpls_exps: List of mpls value.
        @type mpls_exps: Variable length argument list of C{int}       
        
        @raise OnepIllegalArgumentException: If all mpls values in *mpls_exps are invalid.         
        """
        super(MPLSExperimental, self).__init__(self._internal_match_type.MATCH_MPLS_EXP)
        if isinstance(mpls_exps[0], list):
            self._mpls_exp_list = mpls_exps[0]
        else:
            self._mpls_exp_list = list()
            for mpls in mpls_exps:
                if isinstance(mpls, int):
                    if mpls >= 0 and mpls <= 7:
                        self._mpls_exp_list.append(mpls)

        if len(self._mpls_exp_list) == 0:
            raise OnepIllegalArgumentException('No mpls value is valid in mpls_exps.')



    def __eq__(self, obj):
        """
        """
        try:
            validate(obj, MPLSExperimental)
        except OnepIllegalArgumentException as e:
            return False
        if self is obj:
            return True
        else:
            if self._mpls_exp_list == obj._mpls_exp_list:
                return True
            return False



    def _to_idl(self):
        """
        """
        idl = MatchIDL(0, 0, 0, 0, 0)
        idl.matchType = self._match_type
        idl.mplsExpMatch = MatchMplsExpIDL(self._sense, self._mpls_exp_list)
        idl.opCode = self._op_code
        return idl



    @classmethod
    def _from_idl(cls, idl):
        """
        """
        if idl == None:
            return 
        temp_mpls_bytearray = bytearray()
        mt = MPLSExperimental(idl.mplsExpMatch.mplsExp)
        mt.set_negate(False if idl.mplsExpMatch.sense == 0 else True)
        mt._handle = idl.matchHandle
        return mt




class QOSGroup(Match):
    """ QOSGroup class.
    
    This identifies a specific quality of service (QoS) group value as a match criterion.
    
    @undocumented: group
    """


    def _get_group(self):
        return self._group


    _doc_group = ' Qos group value.\n     \n    @type: C{int}\n    '
    group = property(_get_group, None, None, _doc_group)

    def __init__(self, group):
        """ Constructs a QOSGroup match.
            
            @param group: Qos group value.
            @type group: C{int}
        
            @raise OnepIllegalArgumentException: If group is invalid.        
            """
        super(QOSGroup, self).__init__(self._internal_match_type.MATCH_QOS_GROUP)
        validate(group, int)
        self._group = group



    def __eq__(self, obj):
        """
        """
        try:
            validate(obj, QOSGroup)
        except OnepIllegalArgumentException as e:
            return False
        if self is obj:
            return True
        else:
            if self._group == obj._group:
                return True
            return False



    def _to_idl(self):
        """
        """
        idl = MatchIDL(0, 0, 0, 0, 0)
        idl.matchType = self._match_type
        idl.qosGroupMatch = MatchQosGroupIDL(self._sense, self._group)
        idl.opCode = self._op_code
        return idl



    @classmethod
    def _from_idl(cls, idl):
        """
        """
        if idl == None:
            return 
        mt = QOSGroup(idl.qosGroupMatch.group)
        mt.set_negate(False if idl.qosGroupMatch.sense == 0 else True)
        mt._handle = idl.matchHandle
        return mt




class Application(Match):
    """ Application class.
    
    Match on Protocol. This configures the match criterion for a class map on the basis of a specified protocol.
    """


    def _get_protocol(self):
        return self._protocol


    _doc_protocol = ' Protocol value.\n    \n    @type: C{str}    \n    '
    protocol = property(_get_protocol, None, None, _doc_protocol)

    def _get_sub_protocol(self):
        return self._sub_protocol


    _doc_sub_protocol = ' Subprotocol value.\n    \n    @type: C{str}\n    '
    sub_protocol = property(_get_sub_protocol, None, None, _doc_sub_protocol)

    def _get_param(self):
        return self._param


    _doc_param = ' Parameter value.\n    \n    @type: C{str}    \n    '
    param = property(_get_param, None, None, _doc_param)

    def __init__(self, protocol, subprotocol = None, param = None):
        """ Constructs an Application match.
        
        'subprotocol' and 'param' are optional parameters.
        
        @param protocol: protocol.
        @type protocol: C{str}
        @param subprotocol: sub-protocol.
        @type subprotocol: C{str}
        @param param: parameter.
        @type param: C{str}
        
        @raise OnepIllegalArgumentException: If any of constructor parameter is invalid.
        """
        super(Application, self).__init__(self._internal_match_type.MATCH_APPLICATION)
        try:
            if protocol == None or len(protocol) == 0:
                raise OnepIllegalArgumentException('protocol', 'None/Empty')
            if subprotocol == None:
                self._sub_protocol = str('')
            elif len(subprotocol) == 0:
                raise OnepIllegalArgumentException('subprotocol', 'empty')
            else:
                validate(subprotocol, str)
                self._sub_protocol = subprotocol
            if param == None:
                self._param = str('')
            elif len(param) == 0:
                raise OnepIllegalArgumentException('param', 'empty')
            else:
                validate(param, str)
                self._param = param
            validate(protocol, str)
            self._protocol = protocol
        except OnepIllegalArgumentException as e:
            raise e



    def __eq__(self, obj):
        """
        """
        try:
            validate(obj, Application)
        except OnepIllegalArgumentException as e:
            return False
        if self is obj:
            return True
        else:
            if self._protocol == obj._protocol and self._sub_protocol == obj._sub_protocol and self._param == obj._param:
                return True
            return False



    def _to_idl(self):
        """
        """
        idl = MatchIDL(0, 0, 0, 0, 0)
        idl.matchType = self._match_type
        idl.appMatch = MatchApplicationIDL(self._sense, self._protocol, self._sub_protocol, self._param)
        idl.opCode = self._op_code
        return idl



    @classmethod
    def _from_idl(cls, idl):
        """                            
        """
        if idl == None:
            return 
        mt = Application(idl.appMatch.protocol, idl.appMatch.subProtocol, idl.appMatch.param)
        mt.set_negate(False if idl.qosGroupMatch.sense == 0 else True)
        mt._handle = idl.matchHandle
        return mt




class EtherType(Match):
    """ EtherType class.
    
    Ether type match.
    
    @undocumented: ether_type
    """


    def _get_ether_type(self):
        return self._ether_type


    _doc_ether_type = ' Ether Type.\n     \n    @type: C{int}\n    '
    ether_type = property(_get_ether_type, None, None, _doc_ether_type)

    def __init__(self, etype):
        """ Constructs  an EtherType match.
            
            @param etype: Ether Type.
            @type etype: C{int}
        
            @raise OnepIllegalArgumentException: If etype is invalid.
            """
        super(EtherType, self).__init__(self._internal_match_type.MATCH_ETYPE)
        try:
            validate(etype, int)
        except OnepIllegalArgumentException as e:
            raise e
        self._ether_type = etype



    def __eq__(self, obj):
        """
        """
        try:
            validate(obj, EtherType)
        except OnepIllegalArgumentException as e:
            return False
        if self is obj:
            return True
        else:
            if self._ether_type == obj._ether_type:
                return True
            return False



    def _to_idl(self):
        """
        """
        idl = MatchIDL(0, 0, 0, 0, 0)
        idl.matchType = self._match_type
        idl.etypeMatch = MatchEtypeIDL(self._sense, self._ether_type)
        idl.opCode = self._op_code
        return idl



    @classmethod
    def _from_idl(cls, idl):
        """
        """
        if idl == None:
            return 
        mt = EtherType(idl.etypeMatch.etype)
        mt.set_negate(False if idl.etypeMatch.sense == 0 else True)
        mt._handle = idl.matchHandle
        return mt




class InputInterface(Match):
    """ InputInterface Class.
    
    Matches on input interface.
    
    This configures the class map to use the specified input interface as a match criterion.
    
    @undocumented: network_interface
    """


    def _get_network_interface(self):
        return self._nif


    _doc_network_interface = ' Input network interface to match on.\n    \n    @type: L{NetworkInterface<onep.policy.NetworkInterface.NetworkInterface>}    \n    '
    network_interface = property(_get_network_interface, None, None, _doc_network_interface)

    def __init__(self, nif):
        """ Constructs an input interface match.
        
        @param nif: Network Interface instance
        @type nif: L{NetworkInterface<onep.interfaces.NetworkInterface.NetworkInterface>}
        
        @raise OnepIllegalArgumentException: If nif is invalid.            
        """
        try:
            validate(nif, NetworkInterface)
        except OnepIllegalArgumentException as e:
            raise e
        super(InputInterface, self).__init__(self._internal_match_type.MATCH_INTERFACE)
        self._nif = nif



    def __eq__(self, obj):
        """
        """
        try:
            validate(obj, InputInterface)
        except OnepIllegalArgumentException as e:
            return False
        if self is obj:
            return True
        else:
            if self._nif == obj._nif:
                return True
            return False



    def _to_idl(self):
        """
        """
        idl = MatchIDL(0, 0, 0, 0, 0)
        idl.matchType = self._match_type
        idl.ifcMatch = MatchInterfaceIDL(self._sense, self._nif.xos_handle)
        idl.opCode = self._op_code
        return idl



    def _from_idl(cls, idl, element):
        """
        """
        if idl == None:
            return 
        nif_obj = NetworkInterface(element, None, NetworkInterface.InterfaceTypes.ONEP_IF_TYPE_ANY, idl.ifcMatch.ifHandle)
        mi = InputInterface(nif_obj)
        mi.set_negate(False if idl.ifcMatch.sense == 0 else True)
        mi._handle = idl.matchHandle
        return mi




class ICMP(Match):
    """
        ICMP match class.
    
        Assign ICMP type, ICMP code, or both.
        Use class variable ICMPV4 or ICMPV6 for Protocol parameter.
    
        """


    def __init__(self, icmp_type = 0, icmp_code = 0, protocol = None):
        """
                @param icmp_type: ICMP type.
                @type icmp_type: C{int}
        
                @param icmp_code: ICMP code.
                @type icmp_code: C{int} 
        
                @param protocol: ICMP.ICMPV4 or ICMP.ICMPV6
                @type protocol: C{int}
        
                @raise OnepIllegalArgumentException: Constructor parameter is invalid.        
        
                """
        validate(icmp_type, int)
        validate(icmp_code, int)
        if protocol != self.IPV4 and protocol != self.IPV6:
            raise OnepIllegalArgumentException('Invalid protocol', str(protocol))
        self._external_type = None
        if icmp_type:
            if icmp_type < 0 or icmp_type > 255:
                raise OnepIllegalArgumentException('Invalid icmp_type')
            self._external_type = self._icmp_type_map[protocol, 1]
        if icmp_code:
            if icmp_code < 0 or icmp_code > 255:
                raise OnepIllegalArgumentException('Invalid icmp_code')
            if not self._external_type:
                self._external_type = self._icmp_type_map[protocol, 0]
        super(ICMP, self).__init__(self._internal_match_type.MATCH_ICMP)
        self.protocol = protocol
        self.type = icmp_type
        self.code = icmp_code


    IPV4 = 1
    IPV6 = 58
    _icmp_type_map = {(IPV4, 0): MatchType.MATCH_ICMPV4_CODE,
     (IPV4, 1): MatchType.MATCH_ICMPV4_TYPE,
     (IPV6, 0): MatchType.MATCH_ICMPV6_CODE,
     (IPV6, 1): MatchType.MATCH_ICMPV6_TYPE}

    def _to_idl(self):
        idl = MatchIDL(0, 0, 0, 0, 0)
        idl.matchType = self._match_type
        idl.icmpMatch = MatchIcmpIDL(self._sense, self.type, self.code, self.protocol)
        idl.opCode = self._op_code
        return idl



    @classmethod
    def _from_idl(cls, idl):
        if idl == None:
            return 
        mt = ICMP(idl.icmpMatch.type, idl.icmpMatch.code, idl.icmpMatch.protocol)
        mt.set_negate(bool(idl.icmpMatch.sense))
        mt._handle = idl.matchHandle
        return mt



    def __eq__(self, obj):
        if not isinstance(obj, ICMP):
            return False
        return self.type == obj.type and self.code == obj.code and self.protocol == obj.protocol



    def __str__(self):
        return '\n            ICMP action %s\n            type %d\n            code %d\n            ' % (MatchType.enumval(self._external_type), self.type, self.code)




class TTL(Match):
    """ TTL class.
    
    Match on TTL.
    
    @undocumented: ttl
    @undocumented: mask
    """


    def _get_ttl(self):
        return self._ttl


    _doc_ttl = ' TTL value.\n     \n    @type: C{int}\n    '
    ttl = property(_get_ttl, None, None, _doc_ttl)

    def _get_mask(self):
        return self._mask


    _doc_mask = ' Mask value.\n     \n    @type: C{int}\n    '
    mask = property(_get_mask, None, None, _doc_mask)

    def __init__(self, ttl, mask):
        """ Construct a TTL match.
        
        @param ttl: TTL.
        @type ttl: C{int} 
        @param mask: Mask.
        @type mask: C{int}
        
        @raise OnepIllegalArgumentException: If any of constructor parameter is invalid.
        """
        super(TTL, self).__init__(self._internal_match_type.MATCH_IP_TTL)
        try:
            validate(ttl, int)
            validate(mask, int)
        except OnepIllegalArgumentException as e:
            raise e
        self._ttl = ttl
        self._mask = mask



    def __eq__(self, obj):
        """
        """
        try:
            validate(obj, TTL)
        except OnepIllegalArgumentException as e:
            return False
        if self is obj:
            return True
        else:
            if self._ttl == obj._ttl and self._mask == obj._mask:
                return True
            return False



    def _to_idl(self):
        """
        """
        idl = MatchIDL(0, 0, 0, 0, 0)
        idl.matchType = self._match_type
        idl.ttlMatch = MatchTtlIDL(self._sense, self._ttl, self._mask)
        idl.opCode = self._op_code
        return idl



    @classmethod
    def _from_idl(cls, idl):
        """
        """
        if idl == None:
            return 
        mt = TTL(idl.ttlMatch.ttl, idl.ttlMatch.mask)
        mt.set_negate(False if idl.ttlMatch.sense == 0 else True)
        mt._handle = idl.matchHandle
        return mt




class Port(Match):
    """
        Match on a port or port range.
        
        port_direction - match.Direction enum
        protocol - Port.Protocol enum
        port1 - start port range
        port2 - end port range (default is value of port1)
    
        """


    def __init__(self, port_direction, protocol, port1, port2 = None):
        """
                Constructs a port or port range match.
                
                @param port_direction: Either source or destination port.
                @type port_direction: L{Direction<match.Direction>}
        
                @param protocol: Port.Protocol enum
                @type protocol: L{type<match.Port.Protocol>}
        
                @param port1: start port range
                @type port1: C{int} 
        
                @param port2: end port range (default is value of port1)
                @type port2: C{int} 
                
                @raise OnepIllegalArgumentException: If any of constructor parameter is invalid.
        
                """
        if not isinstance(port1, int) or port1 > 65535 or port1 < 0:
            raise OnepIllegalArgumentException('port1 invalid ' + str(port1))
        if port2:
            if not isinstance(port2, int) or port2 > 65535 or port2 < 0:
                raise OnepIllegalArgumentException('port2 invalid ' + str(port2))
        else:
            port2 = port1
        if not Direction._is_valid(port_direction):
            raise OnepIllegalArgumentException('port_direction ' + str(port_direction) + ' is invalid.')
        if not self.Protocol._is_valid(protocol):
            raise OnepIllegalArgumentException('protocol ' + str(protocol) + ' is invalid.')
        super(Port, self).__init__(self._internal_match_type.MATCH_TCP_PORT)
        if port_direction == Direction.SOURCE:
            self._external_type = MatchType.MATCH_SRC_TCP_PORT
        else:
            self._external_type = MatchType.MATCH_DST_TCP_PORT
        self.direction = port_direction
        self.protocol = protocol
        self.port1 = port1
        self.port2 = port2
        self.dependent_match = IpProtocol(protocol)


    Protocol = enum(TCP=6, UDP=17, SCTP=132)

    def __eq__(self, obj):
        if not isinstance(self, Port):
            return False
        return self.direction == obj.direction and self.protocol == obj.protocol and self.port1 == obj.port1 and self.port2 == obj.port2



    def _to_idl(self):
        """
        """
        idl = MatchIDL(0, 0, 0, 0, 0)
        idl.matchType = self._match_type
        idl.tcpPortMatch = MatchTcpPortIDL(self._sense, self.direction, 1, c_short(self.port1).value, c_short(self.port2).value)
        idl.opCode = self._op_code
        return idl



    @classmethod
    def _from_idl(cls, idl):
        """
        """
        if idl == None:
            return 
        mt = Port(idl.tcpPortMatch.srcDst, idl.tcpPortMatch.oper, c_ushort(idl.tcpPortMatch.port1).value, c_ushort(idl.tcpPortMatch.port2).value)
        mt.set_negate(False if idl.tcpPortMatch.sense == 0 else True)
        mt._handle = idl.matchHandle
        return mt




class TCPPort(Port):
    """
        TCPPort class is deprecated.  Please use Port class.
    
        @deprecated: Deprecated with SDK release 1.2.2
    
        """


    @deprecated(Port)
    def __init__(self, port_direction, protocol, port1, port2 = None):
        super(TCPPort, self).__init__(port_direction, protocol, port1, port2)




class RTPPort(Match):
    """ RTPPort class.
    
    RTP Port match.
    """


    def _get_port1(self):
        return self._port1


    _doc_port1 = ' Port1.\n     \n    @type: C{int}\n    '
    port1 = property(_get_port1, None, None, _doc_port1)

    def _get_port2(self):
        return self._port2


    _doc_port2 = ' Port2.\n     \n    @type: C{int}\n    '
    port2 = property(_get_port2, None, None, _doc_port2)

    def __init__(self, port1, port2):
        """ Constructs a Protocol match.
        
        @param port1: Port number 1.
        @type port1: C{int}
        @param port2: Port number 2.
        @type port2: C{int} 
        
        @raise OnepIllegalArgumentException: If any of constructor parameter is invalid.
        """
        try:
            validate(port1, int)
            validate(port2, int)
        except OnepIllegalArgumentException as e:
            raise e
        super(RTPPort, self).__init__(self._internal_match_type.MATCH_RTP_PORT)
        self._port1 = port1
        self._port2 = port2



    def __eq__(self, obj):
        """
        """
        try:
            validate(obj, RTPPort)
        except OnepIllegalArgumentException as e:
            return False
        if self is obj:
            return True
        else:
            if self._port1 == obj._port1 and self._port2 == obj._port2:
                return True
            return False



    def _to_idl(self):
        """
        """
        idl = MatchIDL(0, 0, 0, 0, 0)
        idl.matchType = self._match_type
        idl.rtpPortMatch = MatchRtpPortIDL(self._sense, self._port1, self._port2)
        idl.opCode = self._op_code
        return idl



    @classmethod
    def _from_idl(cls, idl):
        """
        """
        if idl == None:
            return 
        mt = RTPPort(idl.rtpPortMatch.port1, idl.rtpPortMatch.port2)
        mt.set_negate(False if idl.rtpPortMatch.sense == 0 else True)
        mt._handle = idl.matchHandle
        return mt




class TCPFlags(Match):
    """ TCPFlags class.
    
    TCP flags match.
    
    @undocumented: value
    @undocumented: mask
    """


    def _get_value(self):
        return self._value


    _doc_value = ' TCP flags to be matched.\n     \n    @type: C{int}\n    '
    value = property(_get_value, None, None, _doc_value)

    def _get_mask(self):
        return self._mask


    _doc_mask = ' TCP flags mask.\n     \n    @type: C{int}\n    '
    mask = property(_get_mask, None, None, _doc_mask)

    def _get_operator(self):
        return self._operator


    _doc_operator = ' Logical AND, OR function.\n    \n    @type: L{MatchOperator<onep.policyservice.Match.MatchOperator>}\n    '
    operator = property(_get_operator, None, None, _doc_operator)

    def __init__(self, oper, value, mask):
        """ Constructs an TCPFlags match.
        
        @param oper: Logical AND, OR function.
        @type oper: L{MatchOperator<onep.policyservice.Match.MatchOperator>}
        @param value: TCP flags to be matched.
        @type value: C{int} 
        @param mask: TCP flags mask.
        @type mask: C{int} 
        
        @raise OnepIllegalArgumentException: If any of constructor parameter is invalid.
        """
        try:
            validate(mask, int)
            validate(value, int)
        except OnepIllegalArgumentException as e:
            raise e
        if not MatchOperator._is_valid(oper):
            raise OnepIllegalArgumentException('Passed oper parameter value ' + str(oper) + 'is invalid.')
        super(TCPFlags, self).__init__(self._internal_match_type.MATCH_TCP_FLAGS)
        self._operator = oper
        self._value = value
        self._mask = mask



    def __eq__(self, obj):
        """
        """
        try:
            validate(obj, TCPFlags)
        except OnepIllegalArgumentException as e:
            return False
        if self is obj:
            return True
        else:
            if self._operator == obj._operator and self._value == obj._value and obj._mask == obj._mask:
                return True
            return False



    def _to_idl(self):
        """
        """
        idl = MatchIDL(0, 0, 0, 0, 0)
        idl.matchType = self._match_type
        idl.tcpMatch = MatchTcpFlagsIDL(self._sense, self._value, self._mask, self._operator)
        idl.opCode = self._op_code
        return idl



    @classmethod
    def _from_idl(cls, idl):
        """
        """
        if idl == None:
            return 
        mt = TCPFlags(idl.tcpMatch.match, idl.tcpMatch.value, idl.tcpMatch.mask)
        mt.set_negate(False if idl.tcpMatch.sense == 0 else True)
        mt._handle = idl.matchHandle
        return mt




class ACL(Match):
    """ ACL class.
    
    ACL match. This configures the match criteria for a class map on the basis of the specified access control list (ACL).
    
    @undocumented: acl
    """


    def __init__(self, acl):
        """ Constructs an Access Control List(ACL) match.
        
        @param acl: L2 or L3 ACL object.
        @type acl: L{L2Acl<onep.policy.L2Acl.L2Acl>} or L{L3Acl<onep.policy.L3Acl.L3Acl>}
        
        @raise OnepIllegalArgumentException: If acl parameter is invalid.
        """
        super(ACL, self).__init__(self._internal_match_type.MATCH_ACL)
        self.acl = acl



    def __eq__(self, obj):
        """
        """
        try:
            validate(obj, ACL)
        except OnepIllegalArgumentException as e:
            return False
        if self is obj:
            return True
        else:
            if self.acl.get_name() == obj.acl.get_name():
                return True
            return False



    def _to_idl(self):
        """
        """
        idl = MatchIDL(0, 0, 0, 0, 0)
        idl.matchType = self._match_type
        idl.aclMatch = MatchAclIDL(self._sense, self.acl._acl_handle, self.acl.get_name())
        idl.opCode = self._op_code
        return idl



    @classmethod
    def _from_idl(cls, idl, element):
        """
        """
        if idl == None:
            return 
        mt = ACL(get_acl_by_name(element, idl.aclMatch.name, acl.AclType.ONEP_ACL_L3))
        mt.set_negate(False if idl.aclMatch.sense == 0 else True)
        mt._handle = idl.matchHandle
        return mt




class MACAddress(Match):
    """ MACAddress Class. 
    
    It uses source or destination MAC address as match criterion.
    
    @undocumented: mac_address
    @undocumented: mac_address_mask
    """


    def _get_mac_address(self):
        (pos, mac_addr_array,) = self._thrift_to_hex_array(self._mac_address)
        return mac_addr_array


    _doc_mac_address = ' MAC address.\n    \n    List or Array of length six represents mac address.\n    \n    List position or an array index represents single byte of mac address.\n    \n    @type: C{list} or C{array}\n    '
    mac_address = property(_get_mac_address, None, None, _doc_mac_address)

    def _get_mac_address_mask(self):
        (pos, mask_array,) = self._thrift_to_hex_array(self._mac_address_mask)
        return mask_array


    _doc_mac_address_mask = ' MAC address mask.\n    \n    List or Array of length six represents mac address mask.\n    \n    List position or an array index represents single byte of mac address mask.\n    \n    @type: C{list} or C{array}\n    '
    mac_address_mask = property(_get_mac_address_mask, None, None, _doc_mac_address_mask)

    def _get_direction(self):
        return self._src_dst


    _doc_direction = ' Direction source or destination.\n    \n    @type: L{Direction<onep.policyservice.Match.Direction>}\n    '
    direction = property(_get_direction, None, None, _doc_direction)

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



    def _validate_mac(self, addr, src_dst):
        if addr == None:
            raise OnepIllegalArgumentException(src_dst + ' Mac address', 'None')
        if not isinstance(addr, list) and not isinstance(addr, array):
            raise OnepIllegalArgumentException(src_dst + ' Mac address is not of type list or array')
        if len(addr) != 6:
            raise OnepIllegalArgumentException('Invalid ' + src_dst + ' mac address length')



    def _validate_mac_mask(self, mask, src_dst):
        if not isinstance(mask, list) and not isinstance(mask, array):
            raise OnepIllegalArgumentException(src_dst + ' Mac address mask is not of type list or array')
        if len(mask) != 6:
            raise OnepIllegalArgumentException('Invalid ' + src_dst + ' mac address mask length')



    def __init__(self, direction, mac_address, mask = None):
        """ Constructs a MAC address match with MAC address and mask.
                
                mask is optional parameter.
                
                List or Array of length six represents mac address.
                List position or an array index represents single byte of mac address.
            
                List or Array of length six represents mac address mask.
                List position or an array index represents single byte of mac address mask.
            
                @param direction: Source or Destination.
                @type direction: L{Direction<onep.policyservice.Match.Direction>}
                @param mac_address: MAC address.
                @type mac_address: C{list} or C{array}
                @param mask: MAC address mask.
                @type mask: C{list} or C{array}
                
                @raise OnepIllegalArgumentException: If any of constructor parameter is invalid.
        
                """
        if not Direction._is_valid(direction):
            raise OnepIllegalArgumentException('Invalid direction parameter.')
        if direction == Direction.SOURCE:
            direction_str = 'Source'
            self._external_type = MatchType.MATCH_SRC_MAC_ADDRESS
        else:
            direction_str = 'Destination'
            self._external_type = MatchType.MATCH_DST_MAC_ADDRESS
        super(MACAddress, self).__init__(self._internal_match_type.MATCH_MAC_ADDRESS)
        self._src_dst = direction
        self._validate_mac(mac_address, direction)
        (pos, self._mac_address,) = self._convert_to_thrift_array(mac_address)
        if self._mac_address == None:
            raise OnepIllegalArgumentException(direction_str + ' MAC address byte:' + str(pos) + ' is not set to valid(0x00 <= Byte <= 0xFF) byte range')
        if mask != None:
            self._validate_mac_mask(mask, direction)
            (pos, self._mac_address_mask,) = self._convert_to_thrift_array(mask)
            if self._mac_address_mask == None:
                raise OnepIllegalArgumentException(direction_str + ' MAC address mask byte:' + str(pos) + ' is not set to valid(0x00 <= Byte <= 0xFF) byte range')
        else:
            self._mac_address_mask = [0,
             0,
             0,
             0,
             0,
             0]



    def __eq__(self, obj):
        """
        """
        try:
            validate(obj, MACAddress)
        except OnepIllegalArgumentException as e:
            return False
        if self is obj:
            return True
        else:
            if self._src_dst == obj._src_dst and self._mac_address == obj._mac_address and self._mac_address_mask == obj._mac_address_mask:
                return True
            return False



    def _to_idl(self):
        """
        """
        idl = MatchIDL(0, 0, 0, 0, 0)
        idl.matchType = self._match_type
        idl.macAddressMatch = MatchMacAddressIDL(self._sense, self._src_dst, self._mac_address, self._mac_address_mask)
        idl.opCode = self._op_code
        return idl



    def _from_idl(cls, idl):
        """
        """
        if idl == None:
            return 
        ma = MACAddress(idl.macAddressMatch.type, idl.macAddressMatch.addr, idl.macAddressMatch.mask)
        ma.set_negate(False if idl.macAddressMatch.sense == 0 else True)
        ma._handle = idl.matchHandle
        return ma




class IPAddress(Match):
    """
        IPAddress Class matches IPv6 or IPv4 addresses
    
        address    - IPv6 or IPv4 IP address
        prefix_len - address subnet mask
        direction  - match.Direction enum
    
        """

    _afi = OnepConstants.OnepAddressFamilyType.ONEP_AF_INET
    _mask = ''

    def __init__(self, address, prefix_len, direction):
        """
                @param address: IP address.
                @type address: C{str}
        
                @param prefix_len: Prefix Length.
                @type prefix_len: C{int} 
        
                @param direction: Direction.
                @type direction: L{Direction<match.Direction>}
                
                @raise OnepIllegalArgumentException: If any of constructor parameter is invalid.
        
                """
        if not Direction._is_valid(direction):
            raise OnepIllegalArgumentException('Invalid direction parameter.')
        if not HostIpCheck(address).is_ipaddress():
            raise OnepIllegalArgumentException(' ip address is invalid.')
        super(IPAddress, self).__init__(self._internal_match_type.MATCH_IP_ADDRESS)
        if direction == Direction.SOURCE:
            direction_str = 'Source'
            if HostIpCheck(address).is_ipv6():
                self._afi = OnepConstants.OnepAddressFamilyType.ONEP_AF_INET6
                self._external_type = MatchType.MATCH_IPV6_SRC
            else:
                self._external_type = MatchType.MATCH_SRC_IP_ADDRESS
        else:
            direction_str = 'Destination'
            if HostIpCheck(address).is_ipv6():
                self._afi = OnepConstants.OnepAddressFamilyType.ONEP_AF_INET6
                self._external_type = MatchType.MATCH_IPV6_DST
            else:
                self._external_type = MatchType.MATCH_DST_IP_ADDRESS
        self._validate_prefix_len(prefix_len)
        super(IPAddress, self).__init__(self._internal_match_type.MATCH_IP_ADDRESS)
        self.src_dst = direction
        self.address = address
        self.prefix_length = prefix_len
        if self._afi == OnepConstants.OnepAddressFamilyType.ONEP_AF_INET6:
            self._mask = HostIpCheck.len2mask6(prefix_len)
        else:
            self._mask = HostIpCheck.len2mask(prefix_len)



    def _validate_prefix_len(self, prefix_len):
        if prefix_len == None:
            raise OnepIllegalArgumentException(' prefix length', 'None')
        if not isinstance(prefix_len, int):
            raise OnepIllegalArgumentException(' prefix length is not of type int')
        if prefix_len < 0:
            raise OnepIllegalArgumentException(' prefix length is negative')
        if self._afi == OnepConstants.OnepAddressFamilyType.ONEP_AF_INET6 and prefix_len > 128 or self._afi == OnepConstants.OnepAddressFamilyType.ONEP_AF_INET and prefix_len > 32:
            raise OnepIllegalArgumentException(prefix_len, 'out of range')



    def _to_idl(self):
        idl = MatchIDL(0, 0, 0, 0, 0)
        idl.matchType = self._match_type
        idl.ipAddressMatch = MatchIpAddressIDL(self._sense, self.src_dst, self.src_dst, self._afi, NetworkInterface._convert_to_networkaddressidl(self.address).addr, NetworkInterface._convert_to_networkaddressidl(self._mask).addr, self.prefix_length)
        idl.opCode = self._op_code
        return idl



    def _from_idl(cls, idl):
        if idl == None:
            return 
        mi = IPAddress(idl.ipAddressMatch.addr, idl.ipAddressMatch.prefixlen, idl.ipAddressMatch.srcDst)
        mi.set_negate(bool(idl.ipAddressMatch.sense))
        mi._handle = idl.matchHandle
        return mi



    def __eq__(self, obj):
        if not isinstance(obj, IPAddress):
            return False
        return self.src_dst == obj.src_dst and self.address == obj.address and self.prefix_length == obj.prefix_length




class IpProtocol(Match):
    """ 
    IP Protocol class.
    
    Match IP protocol number
    
    @undocumented: protocol
    """

    protocol = None

    def __init__(self, protocol):
        """
        Constructs an IP Protocol match.
        
        @param protocol
        @type protocol: C{int}
        
        @raise OnepIllegalArgumentException: If any of constructor parameter is invalid.
        """
        if protocol < 0 or protocol > 254:
            raise OnepIllegalArgumentException('Must be between 0-254')
        try:
            validate(protocol, int)
        except OnepIllegalArgumentException as e:
            raise e
        super(IpProtocol, self).__init__(self._internal_match_type.MATCH_PROTOCOL)
        self.protocol = protocol



    def __eq__(self, obj):
        try:
            validate(obj, IpProtocol)
        except OnepIllegalArgumentException as e:
            return False
        if self is obj:
            return True
        else:
            if self.protocol == obj.protocol:
                return True
            return False



    def _to_idl(self):
        """
        """
        idl = MatchIDL(0, 0, 0, 0, 0)
        idl.matchType = self._match_type
        idl.protocolMatch = MatchProtocolIDL(self._sense, self.protocol)
        idl.opCode = self._op_code
        return idl



    @classmethod
    def _from_idl(cls, idl):
        """
        """
        if idl == None:
            return 
        mt = IpProtocol(idl.protocolMatch.protocol)
        mt.set_negate(False if idl.protocolMatch.sense == 0 else True)
        mt._handle = idl.matchHandle
        return mt




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:22:49 IST
