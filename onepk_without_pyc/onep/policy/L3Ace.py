# 2015.02.05 17:22:19 IST
import socket
import onep.core.util.socket_imp
from onep.core.util.Enum import *
from onep.core.util import HostIpCheck
from onep.PolicyIDL.PolicyIDL import *
from onep.core.util.OnepConstants import OnepConstants
from onep.core.exception.OnepIllegalArgumentException import OnepIllegalArgumentException
from onep.core.exception.OnepConnectionException import OnepConnectionException
from onep.core.exception import OnepRemoteProcedureException
from onep.core.exception import OnepNotSupportedException
from Shared.ttypes import ExceptionIDL
from onep.thrift.Thrift import TException
import logging
from ctypes import c_byte, c_ubyte, c_short, c_int, c_uint

class L3Ace(object):
    """ L3 Access Control Element (ACE) Class.
    
        It defines a set of attributes for matching a packet.
        One or more ACEs may be added to an Access Control List (ACL).
        
        @undocumented: get_match
        @undocumented: sequence
        @undocumented: get_log_flag
        @undocumented: ttl
        @undocumented: set_icmp
        """

    AceFlag = enum(IP_ACE_PREC_PRESENT=1, IP_ACE_TOS_PRESENT=2, IP_ACE_DSCP_PRESENT=4, IP_ACE_FRAG_PRESENT=8, IP_ACE_LOG_PRESENT=16, IP_ACE_LOG_INPUT_PRESENT=32, IP_ACE_COPY_ACTION=64, IP_ACE_DIVERT_ACTION=128, IP_ACE_ETHERTYPE_PRESENT=256, IP_ACE_VLAN_PRESENT=512, IP_ACE_IN_INTF_PRESENT=1024, IP_ACE_L2COS_PRESENT=2048, IP_ACE_REDIRECT_ACTION=4096, IP_ACE_SET_VLAN_ACTION=8192, IP_ACE_STRIP_VLAN_ACTION=16384, IP_ACE_MAC_REWRITE_ACTION=32768, IP_ACE_MATCHMAC_PRESENT=65536, IP_ACE_TTL_PRESENT=131072)
    PortOperator = enum('ONEP_OPER_ANY', 'ONEP_OPER_LT', 'ONEP_OPER_GT', 'ONEP_OPER_EQ', 'ONEP_OPER_NEQ', 'ONEP_OPER_RANGE', 'ONEP_OPER_ONEBYTE', 'ONEP_OPER_TWOBYTE')
    TcpFlags = enum(ONEP_TCP_FIN=1, ONEP_TCP_SYN=2, ONEP_TCP_RST=4, ONEP_TCP_PSH=8, ONEP_TCP_ACK=16, ONEP_TCP_URG=32)
    TcpFlagMatch = enum(ONEP_MATCH_ANY=1, ONEP_MATCH_ALL=2)
    log_flag = enum(ONEP_ACL_LOG_UNUSED=0, ONEP_ACL_LOG_NORMAL=1, ONEP_ACL_LOG_INPUT=2)

    def __init__(self, sequence, permit):
        """ Instantiate a new Access Control Element.
        
                It initialises L3 Access Control Element(ACE) properties as follows::
                    src_port_oper: PortOperator.ONEP_OPER_ANY
                    dst_port_oper: PortOperator.ONEP_OPER_ANY
                    protocol: 256 
                    ttl: 0
        
                @param sequence: Position of L3 ACE in the L3 Access Control List(ACL).
                @type sequence: C{int}
                @param permit: pass TRUE for permit, pass FALSE for deny.
                @type permit: C{bool}
        
                @raise OnepIllegalArgumentException: If sequence number or permit is invalid.
                """
        self.log = logging.getLogger(__name__)
        self._acl = None
        self._ace_handle = 0
        self.sequence = sequence
        self.permit = permit
        self._src_port_oper = self.PortOperator.ONEP_OPER_ANY
        self._dst_port_oper = self.PortOperator.ONEP_OPER_ANY
        self._src_prefix = '0.0.0.0'
        self._src_prefix_len = None
        self._dst_prefix = '0.0.0.0'
        self._dst_prefix_len = None
        self._tcp_flag_match = 0
        self._tcp_flag_mask = 0
        self._tcp_flag_value = 0
        self._ttl = 0
        self._flags = 0
        self._dscp = 0
        self._dscp_v2 = 0
        self._src_port1 = 0
        self._src_port2 = 0
        self._dst_port1 = 0
        self._dst_port2 = 0
        self._protocol = 256
        self.icmp_type = 0
        self.icmp_code = 0



    def _set_sequence(self, sequence):
        self._validate_sequence(sequence)
        self._sequence = sequence



    def _get_sequence(self):
        return self._sequence


    _doc = '\n    Sequence number denotes position of L3 Access Control Element(ACE) in the L3 Access Control List(ACL).\n\n    Raises: OnepIllegalArgumentException - If sequence number is invalid.\n\n    @type: C{int}\n    '
    sequence = property(_get_sequence, _set_sequence, None, _doc)

    def _set_permit(self, permit):
        try:
            self._validate_permit(permit)
        except OnepIllegalArgumentException as e:
            raise e
        self._permit = permit



    def _get_permit(self):
        return self._permit


    _doc = ' Permit/Deny for L3 Access Control Element(ACE).\n\n    Set TRUE for permit.\n\n    Set FALSE for deny.\n\n    Raises: OnepIllegalArgumentException - If permit is invalid.\n\n    @type: C{bool}\n    '
    permit = property(_get_permit, _set_permit, None, _doc)

    def _set_src_prefix(self, prefix):
        self._validate_prefix(prefix, 'Source')
        self._src_prefix = prefix



    def _get_src_prefix(self):
        return self._src_prefix


    _doc = ' Source IP address to be matched.\n\n    Raises: OnepIllegalArgumentException - If ip address is invalid.\n\n    @type: C{str}\n    '
    src_prefix = property(_get_src_prefix, _set_src_prefix, None, _doc)

    def _set_src_prefix_len(self, prefix_len):
        self._validate_prefix_len(prefix_len, 'Source')
        self._src_prefix_len = prefix_len



    def _get_src_prefix_len(self):
        return self._src_prefix_len


    _doc = ' Source prefix length.\n\n    Raises: OnepIllegalArgumentException - If prefix length is invalid.\n\n    @type: C{int}\n    '
    src_prefix_len = property(_get_src_prefix_len, _set_src_prefix_len, None, _doc)

    def _set_dst_prefix(self, prefix):
        self._validate_prefix(prefix, 'Destination')
        self._dst_prefix = prefix



    def _get_dst_prefix(self):
        return self._dst_prefix


    _doc = ' Destination IP address to be matched.\n\n    Raises: OnepIllegalArgumentException - If ip address is invalid.\n\n    @type: C{str}\n    '
    dst_prefix = property(_get_dst_prefix, _set_dst_prefix, None, _doc)

    def _set_dst_prefix_len(self, prefix_len):
        self._validate_prefix_len(prefix_len, 'Destination')
        self._dst_prefix_len = prefix_len



    def _get_dst_prefix_len(self):
        return self._dst_prefix_len


    _doc = ' Destination prefix length.\n\n    Raises: OnepIllegalArgumentException - If prefix length is invalid.\n\n    @type: C{int}\n    '
    dst_prefix_len = property(_get_dst_prefix_len, _set_dst_prefix_len, None, _doc)

    def _set_protocol(self, protocol):
        if protocol == None:
            raise OnepIllegalArgumentException('protocol', 'None')
        if not isinstance(protocol, int):
            raise OnepIllegalArgumentException('protocol is not of type int')
        if protocol < 0 or protocol > 256:
            raise OnepIllegalArgumentException('protocol is out of range')
        self._protocol = protocol



    def _get_protocol(self):
        return self._protocol


    _doc = ' Protocol value.\n\n    Protocol value must be a number between 0 and 256.\n\n    256 = All protocols\n\n    6 =  TCP\n\n    Raises: OnepIllegalArgumentException - If protocol value is invalid.\n\n    @type: C{int}\n    '
    protocol = property(_get_protocol, _set_protocol, None, _doc)

    def _set_src_port_oper(self, operator):
        self._validate_port_operator(operator, 'Source')
        if operator == self.PortOperator.ONEP_OPER_RANGE:
            raise OnepIllegalArgumentException('Cannot set the port operator to ONEP_OPER_RANGE. Use set_src_port_range API if you want the port operator to be range.')
        self._src_port_oper = operator



    def _get_src_port_oper(self):
        return self._src_port_oper


    _doc = ' Operator for source port matching. \n    This property cannot be set to ONEP_OPER_RANGE.\n\n    Raises: OnepIllegalArgumentException - If operator value is invalid.\n\n    @type: L{PortOperator<PortOperator>}\n    '
    src_port_oper = property(_get_src_port_oper, _set_src_port_oper, None, _doc)

    def _set_src_port1(self, port):
        self._validate_port(port, 'Source')
        if self._src_port_oper == self.PortOperator.ONEP_OPER_RANGE:
            raise OnepIllegalArgumentException('Cannot set src_port1 when port operator is ONEP_OPER_RANGE. For range operator use set_src_port_range or change the operator.')
        self._src_port1 = port



    def _get_src_port1(self):
        return self._src_port1


    _doc = ' TCP/UDP source port. \n    Cannot set this property when the src_port_oper is ONEP_OPER_RANGE.\n\n    Raises: OnepIllegalArgumentException - If port value is invalid.\n\n    @type: C{int}\n    '
    src_port1 = property(_get_src_port1, _set_src_port1, None, _doc)

    def _set_dst_port_oper(self, operator):
        self._validate_port_operator(operator, 'Destination')
        if operator == self.PortOperator.ONEP_OPER_RANGE:
            raise OnepIllegalArgumentException('Cannot set the port operator to ONEP_OPER_RANGE. Use set_dst_port_range API if you want the port operator to be range.')
        self._dst_port_oper = operator



    def _get_dst_port_oper(self):
        return self._dst_port_oper


    _doc = ' Operator for destination port matching. \n    This property cannot be set to ONEP_OPER_RANGE.\n\n    Raises: OnepIllegalArgumentException - If operator value is invalid.\n\n    @type: L{PortOperator<PortOperator>}\n    '
    dst_port_oper = property(_get_dst_port_oper, _set_dst_port_oper, None, _doc)

    def _set_dst_port1(self, port):
        self._validate_port(port, 'Destination')
        if self._dst_port_oper == self.PortOperator.ONEP_OPER_RANGE:
            raise OnepIllegalArgumentException('Cannot set dst_port1 when port operator is ONEP_OPER_RANGE. For range operator use set_dst_port_range or change the operator.')
        self._dst_port1 = port



    def _get_dst_port1(self):
        return self._dst_port1


    _doc = ' TCP/UDP destination port. \n    Cannot set this property when the dst_port_oper is ONEP_OPER_RANGE.\n\n    Raises: OnepIllegalArgumentException - If port value is invalid.\n\n    @type: C{int}\n    '
    dst_port1 = property(_get_dst_port1, _set_dst_port1, None, _doc)

    def _set_ttl(self, ttl):
        self._validate_ttl(ttl)
        self._ttl = ttl
        self._flags |= self.AceFlag.IP_ACE_TTL_PRESENT



    def _get_ttl(self):
        if self._flags & self.AceFlag.IP_ACE_TTL_PRESENT:
            return self._ttl
        raise OnepNotSupportedException('Invalid request.')


    _doc = ' Time to Live (TTL).\n\n    Raises: OnepIllegalArgumentException - If ttl value is invalid.\n\n    @type: C{int}\n    '
    ttl = property(_get_ttl, _set_ttl, None, _doc)
    _AF_INET = 1
    _AF_INET6 = 2

    def _af_check(self, ip):
        try:
            socket.inet_pton(socket.AF_INET, ip)
            return self._AF_INET
        except socket.error:
            try:
                socket.inet_pton(socket.AF_INET6, ip)
                return self._AF_INET6
            except socket.error:
                return -1



    def _port_operator_in_range(self, operator):
        if operator != self.PortOperator.ONEP_OPER_ANY and operator != self.PortOperator.ONEP_OPER_LT and operator != self.PortOperator.ONEP_OPER_GT and operator != self.PortOperator.ONEP_OPER_EQ and operator != self.PortOperator.ONEP_OPER_NEQ and operator != self.PortOperator.ONEP_OPER_RANGE:
            return False
        else:
            return True



    def _validate_sequence(self, sequence):
        if sequence == None:
            raise OnepIllegalArgumentException('sequence number', 'None')
        if not isinstance(sequence, (int, long)):
            raise OnepIllegalArgumentException('sequence number', str(sequence))
        if sequence < 0:
            raise OnepIllegalArgumentException('sequence', 'negative')



    def _validate_permit(self, permit):
        if permit == None:
            raise OnepIllegalArgumentException('permit', 'None')
        if not isinstance(permit, bool):
            raise OnepIllegalArgumentException('permit is not of type bool')



    def _validate_prefix(self, prefix, src_dst):
        if prefix == None:
            raise OnepIllegalArgumentException(src_dst + ' prefix', 'None')
        if not isinstance(prefix, str):
            raise OnepIllegalArgumentException(src_dst + ' prefix is not of type str')
        addr_type = self._af_check(prefix)
        if addr_type == -1:
            raise OnepIllegalArgumentException(src_dst + ' prefix is set to invalid address')



    def _validate_prefix_len(self, prefix_len, src_dst, is_IPv4 = False):
        if prefix_len == None:
            return 
        if not isinstance(prefix_len, int):
            raise OnepIllegalArgumentException(src_dst + ' prefix length is not of type int')
        if prefix_len < 0:
            raise OnepIllegalArgumentException(src_dst + ' prefix length is negative')
        if is_IPv4 and prefix_len > 32:
            raise OnepIllegalArgumentException(src_dst + ' prefix length is beyond the IPv4 prefix range.')
        if prefix_len > 128:
            raise OnepIllegalArgumentException(src_dst + ' prefix length is beyond the IPv6 prefix range.')



    def _validate_port(self, port, src_dst):
        if port == None:
            raise OnepIllegalArgumentException(src_dst + ' port', 'None')
        if not isinstance(port, int):
            raise OnepIllegalArgumentException(src_dst + ' port is not of type int')
        if port < 0:
            raise OnepIllegalArgumentException(src_dst + ' port < 0')
        if port > 65535:
            raise OnepIllegalArgumentException(src_dst + ' port > 65535')



    def _validate_port_operator(self, operator, src_dst):
        if operator == None:
            raise OnepIllegalArgumentException(src_dst + ' port operator', 'None')
        if self._port_operator_in_range(operator) == False:
            raise OnepIllegalArgumentException(src_dst + ' port operator is invalid')



    def _validate_port_range(self, port1, port2, src_dst):
        if port1 == None:
            raise OnepIllegalArgumentException(src_dst + ' port1', 'None')
        if port2 == None:
            raise OnepIllegalArgumentException(src_dst + ' port2', 'None')
        if not isinstance(port1, int):
            raise OnepIllegalArgumentException(src_dst + ' port1 is not of type int')
        if not isinstance(port2, int):
            raise OnepIllegalArgumentException(src_dst + ' port2 is not of type int')
        if port1 < 0:
            raise OnepIllegalArgumentException(src_dst + ' port1 < 0')
        if port1 > 65535:
            raise OnepIllegalArgumentException(src_dst + ' port1 > 65535')
        if port2 < 0:
            raise OnepIllegalArgumentException(src_dst + ' port2 < 0')
        if port2 > 65535:
            raise OnepIllegalArgumentException(src_dst + ' port2 > 65535')
        if port1 > port2:
            raise OnepIllegalArgumentException(src_dst + ' start range > end range')



    def _validate_ttl(self, ttl):
        if ttl == None:
            raise OnepIllegalArgumentException('ttl', 'None')
        if not isinstance(ttl, int):
            raise OnepIllegalArgumentException('ttl is not of type int')
        if ttl < 0:
            raise OnepIllegalArgumentException('ttl is set to negative value')
        if ttl > 255:
            raise OnepIllegalArgumentException('ttl cannot be set to a value greater than 255')



    def _check_proto(self):
        """ generated source for method checkProto """
        if self._protocol < 0:
            return 1
        else:
            return 0



    def set_src_prefix_any(self):
        """ Set source prefix to any.
        
                It sets following two properties:
        
                src_prefix: "0.0.0.0"
        
                src_prefix_len: 0
        
                @type: C{int}
                """
        self._src_prefix = '0.0.0.0'
        self._src_prefix_len = 0



    def set_dst_prefix_any(self):
        """ Set destination prefix to any.
        
                It sets following two properties:
        
                dst_prefix: "0.0.0.0"
        
                dst_prefix_len: 0
        
                @type: C{int}
                """
        self._dst_prefix = '0.0.0.0'
        self._dst_prefix_len = 0



    def set_src_port_range(self, port1, port2):
        """ Set TCP/UDP source port range.
        
                @param port1: Source port range lower bound.
                @type port1: C{int}
                @param port2: Source port range upper bound.
                @type port2: C{int}
        
                @raise OnepIllegalArgumentException: If port value is invalid.
                """
        self._validate_port_range(port1, port2, 'Source')
        self._src_port1 = port1
        self._src_port2 = port2
        self._src_port_oper = self.PortOperator.ONEP_OPER_RANGE



    def get_src_port_range(self):
        """ Get TCP/UDP source port lower,upper bound.
        
                @return: Returns source port lower,upper bound.
        
                @rtype: (C{int},C{int})
                """
        return (self._src_port1, self._src_port2)



    def set_dst_port_range(self, port1, port2):
        """ Set TCP/UDP destination port range.
        
                @param port1: Destination port range lower bound.
                @type port1: C{int}
                @param port2: Destination port range upper bound.
                @type port2: C{int}
        
                @raise OnepIllegalArgumentException: If port value is invalid.
                """
        self._validate_port_range(port1, port2, 'Destination')
        self._dst_port1 = port1
        self._dst_port2 = port2
        self._dst_port_oper = self.PortOperator.ONEP_OPER_RANGE



    def get_dst_port_range(self):
        """ Get TCP/UDP destination port lower,upper bound.
        
                @return: Returns destination port lower,upper bound.
        
                @rtype: (C{int},C{int})
                """
        return (self._dst_port1, self._dst_port2)



    def _validate_tcp_flag(self, tcp_flag):
        if tcp_flag != self.TcpFlags.ONEP_TCP_FIN and tcp_flag != self.TcpFlags.ONEP_TCP_SYN and tcp_flag != self.TcpFlags.ONEP_TCP_RST and tcp_flag != self.TcpFlags.ONEP_TCP_PSH and tcp_flag != self.TcpFlags.ONEP_TCP_ACK and tcp_flag != self.TcpFlags.ONEP_TCP_URG:
            return False
        else:
            return True



    def set_tcp_flags(self, value, mask, match):
        """ Set TCP flags. A match bit field value, mask and a match type are used to set up the matching of TCP flags.
        
                The mask field selects which flags are to be used in the match.
        
                The match type determines the combination of selected TCP flags that will cause a match, i.e., either all TCP flags
                must match the selected flag values, or any one of the TCP flags must match the selected flag values.
        
                For example to match on all TCP flag bits being FIN = 1, SYN = 1, PSH = 0, ACK = 0 ::
                    value = [TcpFlags.ONEP_TCP_FIN, TcpFlags.ONEP_TCP_SYN]
                    mask  = [TcpFlags.ONEP_TCP_FIN, TcpFlags.ONEP_TCP_SYN, TcpFlags.ONEP_TCP_PSH, TcpFlags.ONEP_TCP_ACK]
                    match = [TcpFlagMatch.ONEP_MATCH_ALL]
                    Note: PSH and ACK are not passed in 'value' as all tcp flags have 0 bit value by default.
        
                @param value: pass list of tcp flags for which bit value 1 is to be matched.
                @type value: C{list}
                @param mask: list of tcp flags are to be used in the match.
                @type mask: C{list}
                @param match: all or any one of the tcp flags must match selected flag values.
                @type match: C{list}
        
                @raise OnepIllegalArgumentException: If value,mask or match is invalid.
                """
        if self._protocol != 6:
            raise OnepIllegalArgumentException('protocol != TCP')
        if value == None:
            raise OnepIllegalArgumentException('value', 'none')
        if mask == None:
            raise OnepIllegalArgumentException('mask', 'none')
        if match == None:
            raise OnepIllegalArgumentException('match', 'none')
        if not isinstance(value, list):
            raise OnepIllegalArgumentException('value is not of type list')
        if not isinstance(mask, list):
            raise OnepIllegalArgumentException('mask is not of type list')
        if match != self.TcpFlagMatch.ONEP_MATCH_ANY and match != self.TcpFlagMatch.ONEP_MATCH_ALL:
            raise OnepIllegalArgumentException('match is invalid')
        i = 0
        for val in value:
            i += 1
            if self._validate_tcp_flag(val) == False:
                raise OnepIllegalArgumentException('Element ' + str(i) + " in 'value' list is not valid tcpflag")
            self._tcp_flag_value = self._tcp_flag_value | val

        i = 0
        for msk in mask:
            i += 1
            if self._validate_tcp_flag(msk) == False:
                raise OnepIllegalArgumentException('Element ' + str(i) + " in 'mask' list is not valid tcpflag")
            self._tcp_flag_mask = self._tcp_flag_mask | msk

        self._tcp_flag_match = match



    def _validate_dscp(self, dscp):
        if dscp is None:
            raise OnepIllegalArgumentException('No DSCP value')
        if not OnepConstants.OnepDscp._is_valid(dscp):
            raise OnepIllegalArgumentException('Invalid DSCP')



    def set_dscp(self, dscp):
        """ Set the value of the DSCP field.
        
                @param dscp: dscp value.
                @type dscp: C{int}
        
                @raise OnepIllegalArgumentException: If value,mask or match is invalid.
                """
        self._validate_dscp(dscp)
        self._dscp_v2 = dscp << 2 & 252
        self._flags |= self.AceFlag.IP_ACE_DSCP_PRESENT


    _ONEBYTE = 6
    _TWOBYTE = 7

    def set_icmp(self, type, code):
        if type > 255 or type < 0:
            raise OnepIllegalArgumentException('Invalid ICMP type')
        if code < 0:
            raise OnepIllegalArgumentException('Invalid ICMP code')
        if code > 255:
            if code != 65535:
                raise OnepIllegalArgumentException('Invalid ICMP code')
        if code == 65535:
            self._dst_port_oper = self._ONEBYTE
        else:
            self._dst_port_oper = self._TWOBYTE
        self._protocol = 1
        self._dst_port1 = type
        self._dst_port2 = code



    def _validate_log_flag(self, log_flag):
        if log_flag == None:
            raise OnepIllegalArgumentException('log_flag', 'None')
        if log_flag != self.log_flag.ONEP_ACL_LOG_NORMAL and log_flag != self.log_flag.ONEP_ACL_LOG_INPUT and log_flag != self.log_flag.ONEP_ACL_LOG_UNUSED:
            raise OnepIllegalArgumentException('log_flag is invalid')



    def set_log_flag(self, log_flag):
        """ Set Log Flag.
        
                Set the value of the Log flags.
        
                @param log_flag: normal=1, input=2, or unused=0
                @type log_flag: L{log_flag<log_flag>}
        
                @raise OnepIllegalArgumentException: If log_flag is invalid.
                """
        log_flag = int(log_flag)
        self._validate_log_flag(log_flag)
        if log_flag == self.log_flag.ONEP_ACL_LOG_NORMAL:
            self._flags |= self.AceFlag.IP_ACE_LOG_PRESENT
        if log_flag == self.log_flag.ONEP_ACL_LOG_INPUT:
            self._flags |= self.AceFlag.IP_ACE_LOG_INPUT_PRESENT
        if log_flag == self.log_flag.ONEP_ACL_LOG_UNUSED:
            self._flags &= ~self.AceFlag.IP_ACE_LOG_PRESENT
            self._flags &= ~self.AceFlag.IP_ACE_LOG_INPUT_PRESENT



    def get_log_flag(self):
        """
                Returns log flag settings
        
                log_flag.ONEP_ACL_LOG_NORMAL and/or
                log_flag.ONEP_ACL_LOG_INPUT
        
                log_flag.ONEP_ACL_LOG_UNUSED
        
                @return: Log Flags
                @rtype: C{int}
        
                """
        log_flag = self.log_flag.ONEP_ACL_LOG_UNUSED
        if self._flags & self.AceFlag.IP_ACE_LOG_PRESENT:
            log_flag |= self.log_flag.ONEP_ACL_LOG_NORMAL
        if self._flags & self.AceFlag.IP_ACE_LOG_INPUT_PRESENT:
            log_flag |= self.log_flag.ONEP_ACL_LOG_INPUT
        return log_flag



    def get_match(self):
        """ Get ACE match count.
        
                Get the count of matches for this ACE.
        
                @return: Count Match.
                @rtype: C{int}
        
                @raise OnepRemoteProcedureException: If error occurs when remote procedure call is made to network element.
                @raise OnepConnectionException: If connection to network element fails.
                """
        count = 0
        try:
            if self._acl._acl_header:
                self.log.debug('Get named ACE match count')
                count = self._acl._acl_client.getNamedAceMatch_IDL(self._acl._acl_header.name, self._acl._acl_handle, c_int(self._sequence).value, self._acl._acl_header.lifetime, self._acl._acl_header.addrFamily)
            else:
                self.log.debug('Get ACE match count')
                count = self._acl._acl_client.getAceMatch_IDL(self._acl._acl_handle, self._ace_handle)
            self.log.debug('Returned ace match count %s', str(count))
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e.message, e)
        return count



    def _add_to_acl(self, acl):
        """
        """
        self._validate_prefix(self.src_prefix, 'Source')
        self._validate_prefix_len(self.src_prefix_len, 'Source', HostIpCheck(self.src_prefix).is_ipv4())
        self._validate_prefix(self.dst_prefix, 'Destination')
        self._validate_prefix_len(self.dst_prefix_len, 'Destination', HostIpCheck(self.dst_prefix).is_ipv4())
        src_addr_type = self._af_check(self.src_prefix)
        if src_addr_type == self._AF_INET:
            if self.src_prefix_len > 32:
                raise OnepIllegalArgumentException('Source prefix length for AF_INET source prefix > 32')
            elif self.src_prefix_len == None:
                self.src_prefix_len = 32
            src_prefix_af = OnepConstants.OnepAddressFamilyType.ONEP_AF_INET
        elif src_addr_type == self._AF_INET6:
            if self.src_prefix_len > 128:
                raise OnepIllegalArgumentException('Source prefix length for AF_INET6 source prefix > 128')
            elif self.src_prefix_len == None:
                self.src_prefix_len = 128
            src_prefix_af = OnepConstants.OnepAddressFamilyType.ONEP_AF_INET6
        else:
            raise OnepIllegalArgumentException('Invalid Source prefix Address')
        dst_addr_type = self._af_check(self._dst_prefix)
        if dst_addr_type == self._AF_INET:
            if self.dst_prefix_len > 32:
                raise OnepIllegalArgumentException('Destination prefix length for AF_INET destination prefix > 32')
            elif self.dst_prefix_len == None:
                self.dst_prefix_len = 32
            dst_prefix_af = OnepConstants.OnepAddressFamilyType.ONEP_AF_INET
        elif dst_addr_type == self._AF_INET6:
            if self.dst_prefix_len > 128:
                raise OnepIllegalArgumentException('Destination prefix length for AF_INET6 destination prefix > 128')
            elif self.dst_prefix_len == None:
                self.dst_prefix_len = 128
            dst_prefix_af = OnepConstants.OnepAddressFamilyType.ONEP_AF_INET6
        else:
            raise OnepIllegalArgumentException('Invalid Destination prefix Address')
        if self.dst_prefix_len == 0:
            dst_prefix_af = src_prefix_af
        if self.src_prefix_len == 0:
            src_prefix_af = dst_prefix_af
        if not src_prefix_af == dst_prefix_af:
            raise OnepIllegalArgumentException('Source prefix address family and Destination prefix address family are not same.')
        if self.src_prefix_len != 0 and src_prefix_af != acl._afi:
            raise OnepIllegalArgumentException('L3-Ace address family  not same as L3-Acl address family')
        if self.dst_prefix_len != 0 and dst_prefix_af != acl._afi:
            raise OnepIllegalArgumentException('L3-Ace address family not same as L3-Acl address family')
        if not self._acl == None:
            raise OnepIllegalArgumentException('L3 Access Control Element(ACE) already added to L3 Access Control List(ACL)')
        self.log.info('Basic Validation of all L3-ace parameters completed.')
        self._acl = acl
        ace_param = L3AceParam_IDL(c_int(self._sequence).value, self.permit, src_prefix_af, self.src_prefix, self.src_prefix_len, self.dst_prefix, self.dst_prefix_len, self.protocol, self.src_port_oper, c_short(self.src_port1).value, c_short(self._src_port2).value, self.dst_port_oper, c_short(self.dst_port1).value, c_short(self._dst_port2).value, self._tcp_flag_value, self._tcp_flag_mask, self._tcp_flag_match, self._dscp, self._flags, self._ttl, acl._app_id, acl._app_id, self._dscp_v2)
        self.log.info('Successfully created L3-ace parameters through idl call L3AceParam_IDL')
        if acl._acl_header:
            try:
                self.log.debug('Added named ACE to ACL')
                self._ace_handle = acl._acl_client.addNamedL3Ace_IDL(acl._acl_header.name, acl._acl_handle, acl._acl_header.lifetime, acl._acl_header.addrFamily, ace_param)
                self.log.info('Returned from addNamedL3Ace_IDL idl call to add a L3-ace in L3-acl')
            except ExceptionIDL as e:
                raise OnepRemoteProcedureException(e)
            except TException as e:
                raise OnepConnectionException(e.message, e)
        else:
            try:
                self.log.debug('Added ACE to ACL')
                self._ace_handle = acl._acl_client.addL3Ace_IDL(acl._acl_handle, ace_param)
                self.log.info('Returned from addL3Ace_IDL idl call to add a L3-ace in L3-acl')
            except ExceptionIDL as e:
                raise OnepRemoteProcedureException(e)
            except TException as e:
                raise OnepConnectionException(e.message, e)



    def _remove_from_acl(self, acl):
        """
        """
        if acl._acl_header:
            try:
                self.log.debug('Delete named ACE=%d from ACL' % self._sequence)
                self._ace_handle = acl._acl_client.deleteNamedAce_IDL(acl._acl_header.name, acl._acl_handle, c_int(self._sequence).value, acl._acl_header.lifetime, acl._acl_header.addrFamily)
                self.log.info('Returned from deleteNamedAce_IDL idl call to remove a L3-ace from L3-acl')
            except ExceptionIDL as e:
                raise OnepRemoteProcedureException(e)
            except TException as e:
                raise OnepConnectionException(e.message, e)
        else:
            try:
                self.log.debug('Deleted ACE from ACL')
                self._ace_handle = acl._acl_client.deleteAce_IDL(acl._acl_handle, self._ace_handle)
                self.log.info('Returned from deleteAce_IDL idl call to remove a L3-ace from L3-acl')
            except ExceptionIDL as e:
                raise OnepRemoteProcedureException(e)
            except TException as e:
                raise OnepConnectionException(e.message, e)
        self._acl = None



    def __str__(self):
        """ Returns a string representation of the L2 Access Control Element(ACE) instance.
        
                @rtype: C{str}
                @return: String representation of the L2 ACE object.
                """
        sb = '\nL3 ACE [ ' + str(self._ace_handle) + ' ]\n'
        sb += '\tSequence Num : ' + str(self._sequence) + '\n'
        sb += '\tPermit       : ' + str(self._permit) + '\n'
        sb += '\tProtocol     : ' + str(self._protocol) + '\n'
        if self._src_prefix != None:
            sb += '\tSource       : ' + str(self._src_prefix) + '/' + str(self._src_prefix_len) + '\n'
        else:
            sb += '\tSource       : any\n'
        if self._dst_prefix != None:
            sb += '\tDestination  : ' + str(self._dst_prefix) + '/' + str(self._dst_prefix_len) + '\n'
        else:
            sb += '\tDestination  : any\n'
        sb += '\tSrc Port     : ' + self.PortOperator.enumval(self._src_port_oper) + ' ' + str(self._src_port1)
        if self._src_port_oper == self.PortOperator.ONEP_OPER_RANGE:
            sb += ' ' + str(self._src_port2) + '\n'
        else:
            sb += '\n'
        sb += '\tDst Port     : ' + self.PortOperator.enumval(self._dst_port_oper) + ' ' + str(self._dst_port1)
        if self._dst_port_oper == self.PortOperator.ONEP_OPER_RANGE:
            sb += ' ' + str(self._dst_port2) + '\n'
        else:
            sb += '\n'
        if self._flags & self.AceFlag.IP_ACE_DSCP_PRESENT == self.AceFlag.IP_ACE_DSCP_PRESENT:
            sb += '\tDSCP         : ' + str(self._dscp_v2 >> 2) + '\n'
        return sb




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:22:19 IST
