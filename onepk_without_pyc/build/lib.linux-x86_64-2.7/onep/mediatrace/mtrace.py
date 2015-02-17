# 2015.02.05 17:18:42 IST
import logging
import ctypes
from onep.core.util import enum, HostIpCheck
from onep.core.exception import OnepIllegalArgumentException
from onep.core.exception import OnepRemoteProcedureException
from Shared.ttypes import ExceptionIDL
from onep.PathTraceIDL import PathTraceIDL
from onep.PathTraceIDL.ttypes import PathSpecIDL
from onep.PathTraceIDL.ttypes import PathTraceGraphIDL
from onep.PathTraceIDL.ttypes import PathTraceRequestIDL
from onep.interfaces import NetworkInterface
Protocol = enum(TCP=6, UDP=17)
ProfileType = enum('ECHO', 'CPU', 'INTERFACE', 'MEMORY', 'PERFMON')
RouteStatus = enum('PENDING', 'OK', 'NO_MEM', 'NO_OPER_COMP', 'CONNECTING_TIMEOUT', 'ESESCREATE1', 'ESESCREATE2', 'ESESCOMM', 'ETIMEOUT', 'NO_SUCH_PROFILE', 'TOO_MANY_PROFILE', 'EROUTECHG', 'EABORT_ROUTECHG', 'EINCOMPLETEHOP', 'ENOROUTE', 'ESESDOWN', 'RESP_NULL_PTR', 'RESP_SNMP_FAILURE', 'FNFV9_DECODE_FAILED', 'DVMC_REGISTRATION_FAILED', 'DVMC_MON_OBJ_BUILD_FAILED', 'DVMC_MONITOR_START_FAILED', 'DVMC_MONITOR_STOP_FAILED', 'DVMC_DATA_COLLECTION_FAILED', 'DVMC_DATA_NO_RECORD', 'PROF_PROT_MISMATCH', 'PROF_NOT_ATTACHED', 'FAIL', 'UNKNOWN')
TraceRouteStatus = enum('UNKNOWN', 'IN_PROGRESS', 'COMPLETE', 'ERROR', 'TIMEOUT', 'NO_MATCH')
NodeType = enum('MT', 'TR')
NodeStatus = enum('FAIL', 'OK', 'SYSTEM_NO_MEM', 'SYSTEM_RESP_NULL_PTR', 'SYSTEM_RESP_SNMP_FAILURE', 'PERFMON_CLIENT_INVALID', 'PERFMON_CLIENT_EXIST', 'PERFMON_MOBJ_ACTIVE', 'PERFMON_MOBJ_INVALID', 'PERFMON_PATH_INVALID', 'PERFMON_IF_INVALID', 'PERFMON_FSPEC_INVALID', 'PERFMON_FSPEC_FAIL', 'PERFMON_ROBJ_INVALID', 'PERFMON_ROBJ_EXIST', 'PERFMON_ROBJ_CREATE_FAIL', 'PERFMON_FNF_DECODE_FAIL', 'PERFMON_FNF_NOMSG', 'PERFMON_FNF_ENCODE_FAIL', 'PERFMON_FNF_ENCODE_OPT_FAIL', 'PERFMON_XML_NOMSG', 'PERFMON_XML_FAIL', 'PERFMON_XML_KEY_UNKNOWN', 'PERFMON_RPT_NO_RECORD', 'PERFMON_RPT_BUF_SHORT', 'PERFMON_RPT_XFORM_FAIL', 'PERFMON_PARAM_INVALID', 'PERFMON_RESOURCE_EXHAUSTED', 'PERFMON_MULTI_MON_EXCEEDED', 'PERFMON_FLOW_OVERLAP', 'PERFMON_INTERNAL_ERROR')

def _validate_ip(ip_addr):
    if not HostIpCheck(ip_addr).is_ipaddress():
        raise OnepIllegalArgumentException('Invalid IP address ' + str(ip_addr))
    return ip_addr



def _validate_port(port_num):
    if port_num < 0 or port_num > 65535:
        raise OnepIllegalArgumentException('Invalid port number ' + str(port_num))
    return port_num



def trace_request(element, profile, path_spec, timeout):
    """
        Trace request allows applications to gather network device information along
        a path without addressing each device directly.
    
        @param element: NetworkElement class
        @type element: {NetworkElement<onep.element.NetworkElement>}
        @param profile: mtrace.ProfileType of trace
        @type profile: {ProfileType<onep.mediatrace.mtrace.ProfileType>}
        @param path_spec: PathSpecifier class
        @type path_spec: {PathSpecifier<onep.mediatrace.mtrace.PathSpecifier>}
        @param timeout: Timeout value of trace
        @type timeout: C{int}
    
        """
    if not ProfileType._is_valid(profile):
        raise OnepIllegalArgumentException('Invalid profile type ' + str(profile))
    if not isinstance(path_spec, PathSpecifier):
        raise OnepIllegalArgumentException('Invalid path spec ' + str(path_spec))
    if timeout < 0:
        raise OnepIllegalArgumentException('Invalid timeout ' + str(timeout))
    try:
        client = PathTraceIDL.Client(element.api_protocol)
        ptreq_idl = PathTraceRequestIDL(profile, timeout, path_spec._to_idl())
        graph_idl = client.PathTrace_executeRequestIDL(element.session_handle._id, ptreq_idl)
        return MediatraceRoute(graph_idl)
    except ExceptionIDL as e:
        return OnepRemoteProcedureException(e)



class PathSpecifier(object):
    """
        Class holding path specifications for trace to follow
    
        src_ip   - string - Valid IPv4 or IPv6 source address
        src_port - int - layer 4 source port number <0 - 65535>
        dst_ip   - string - Valid IPv4 or IPv6 destination address
        dst_port - int - layer 4 destination port number <0 - 65535>
        protocol - enum mtrace.Protocol - TCP or UDP
    
        """


    def __init__(self, src_ip, src_port, dst_ip, dst_port, protocol):
        """
                Constructor
        
                @ivar src_ip: Valid IPv4 or IPv6 source address
                @type src_ip: C{str}
                @ivar src_port: Layer 4 source port number <0 - 65535>
                @type src_port: C{int}
                @ivar dst_ip: Valid IPv4 or IPv6 destination address
                @type dst_ip: C{str}
                @ivar dst_port: Layer 4 destination port number <0 - 65535>
                @type src_port: C{int}
                @ivar protocol: enum mtrace.Protocol - TCP or UDP
                @type protocol: {Protocol<onep.mediatrace.mtrace.Protocol>}
        
                """
        self.src_ip = _validate_ip(src_ip)
        self.src_port = _validate_port(src_port)
        self.dst_ip = _validate_ip(dst_ip)
        self.dst_port = _validate_port(dst_port)
        if not Protocol._is_valid(protocol):
            raise OnepIllegalArgumentException('Invalid protocol type ' + str(protocol))
        self.protocol = protocol



    def _to_idl(self):
        return PathSpecIDL(self.src_port, self.dst_port, self.protocol, NetworkInterface._convert_to_networkaddressidl(self.src_ip), NetworkInterface._convert_to_networkaddressidl(self.dst_ip))



    def __str__(self):
        return '\n        PathSpecifier\n        -------------\n        source IP --------: %s\n        source port ------: %d\n        destination IP ---: %s\n        destination port -: %d\n        protocol ---------: %s\n        ' % (self.src_ip,
         ctypes.c_ushort(self.src_port).value,
         self.dst_ip,
         ctypes.c_ushort(self.dst_port).value,
         Protocol.enumval(self.protocol))




class MediatraceRoute(object):
    """
        Read only class holding route information from results of trace
    
        route_index  - index of route information in chain
        profile      - mtrace.ProfileType enum
        route_status - mtrace.RouteStatus enum
        traceroute_status - mtrace.TraceRouteStatus enum
        nodes_successful - number of nodes successfully traced
        nodes_errored    - number of nodes with trace errors
        nodes_no_data    - number of nodes with no trace data
        non_mt_nodes     - number of nodes without mediatrace capability
        collection_timestamp - time node trace data was colledted
        last_route_change_timestamp - last route change time
        node_list - list of MediatraceNode classes
    
        """


    def __init__(self, idl):
        self.route_index = idl.route_index
        self.profile = idl.profile
        self.route_status = idl.route_status
        self.traceroute_status = idl.traceroute_status
        self.nodes_successful = idl.nodes_successful
        self.nodes_errored = idl.nodes_errored
        self.nodes_no_data = idl.nodes_no_data
        self.non_mt_nodes = idl.non_pt_nodes
        self.collection_timestamp = idl.collection_timestamp
        self.last_route_change_timestamp = idl.last_route_change_timestamp
        self.node_list = []
        for node in idl.node_list:
            self.node_list.append(MediatraceNode(node))




    def __str__(self):
        node_str = ''
        for node in self.node_list:
            node_str = node_str + str(node)

        return '\n        *-----------------*\n        | MediatraceRoute |\n        *-----------------*\n        route_index -------: %d\n        profile -----------: %s\n        route_status ------: %s\n        traceroute_status -: %s\n        nodes_successful --: %d\n        nodes_errored -----: %d\n        nodes_no_data -----: %d\n        non_mt_nodes ------: %d\n        collection_timestamp --------: %d\n        last_route_change_timestamp -: %d\n\n        %s\n        ' % (self.route_index,
         ProfileType.enumval(self.profile),
         RouteStatus.enumval(self.route_status),
         TraceRouteStatus.enumval(self.traceroute_status),
         self.nodes_successful,
         self.nodes_errored,
         self.nodes_no_data,
         self.non_mt_nodes,
         ctypes.c_ulonglong(self.collection_timestamp).value,
         ctypes.c_ulonglong(self.last_route_change_timestamp).value,
         node_str)




class EchoProfile(object):
    """
        Read only class containing ECHO profile information of a node in trace
    
        reachability_addr - reachable IP address of node in path
        ingress_intf_name - inbound interface name the trace took
        egress_intf_name  - outbound interface name the trace took
    
        """


    def __init__(self, idl):
        self.reachability_addr = NetworkInterface._convert_to_inetaddress(idl.EchoProfile.reachability_addr)
        self.ingress_intf_name = idl.EchoProfile.ingress_intf_name
        self.egress_intf_name = idl.EchoProfile.egress_intf_name



    def __str__(self):
        return '\n        *-------------*\n        | EchoProfile |\n        *-------------*\n        reachability_addr -: %s\n        ingress_intf_name -: %s\n        egress_intf_name --: %s\n        ' % (self.reachability_addr, self.ingress_intf_name, self.egress_intf_name)




class CPUProfile(object):
    """
        Read only class containing CPU profile information of a node in trace
    
        collection_timestamp - time CPU information was collected
        one_min_cpu_util     - one minute CPU utilization
        five_min_cpu_util    - one minute CPU utilization
    
        """


    def __init__(self, idl):
        self.collection_timestamp = idl.CPUProfile.collection_timestamp
        self.one_min_cpu_util = idl.CPUProfile.one_min_cpu_util
        self.five_min_cpu_util = idl.CPUProfile.five_min_cpu_util



    def __str__(self):
        return '\n        *------------*\n        | CPUProfile |\n        *------------*\n        collection_timestamp -: %d\n        one_min_cpu_util -----: %d\n        five_min_cpu_util ----: %d\n        ' % (ctypes.c_ulonglong(self.collection_timestamp).value, self.one_min_cpu_util, self.five_min_cpu_util)




class InterfaceProfile(object):
    """
        Read only class containing INTERFACE profile information of a node in trace
    
        collection_timestamp - time INTERFACE information was collected
        octet_input_ingress  - inbound octet
        octet_output_egress  - outbound octet
        pkts_errored_ingress - inbound packet errors
        pkts_errored_egress  - outbound packet errors
        pkts_discarded_ingress - inbound packets discarded
        pkts_discarded_egress  - outbound packets discarded
        ingress_intf_speed     - interface speed inbound
        egress_intf_speed      - interface speed outbound
    
        """


    def __init__(self, idl):
        self.collection_timestamp = idl.IntfProfile.collection_timestamp
        self.octet_input_ingress = idl.IntfProfile.octet_input_ingress
        self.octet_output_egress = idl.IntfProfile.octet_output_egress
        self.pkts_errored_ingress = idl.IntfProfile.pkts_errored_ingress
        self.pkts_errored_egress = idl.IntfProfile.pkts_errored_egress
        self.pkts_discarded_ingress = idl.IntfProfile.pkts_discarded_ingress
        self.pkts_discarded_egress = idl.IntfProfile.pkts_discarded_egress
        self.ingress_intf_speed = idl.IntfProfile.ingress_intf_speed
        self.egress_intf_speed = idl.IntfProfile.egress_intf_speed



    def __str__(self):
        return '\n        *------------------*\n        | InterfaceProfile |\n        *------------------*\n        collection_timestamp ---: %d\n        octet_input_ingress ----: %d\n        octet_output_egress ----: %d\n        pkts_errored_ingress ---: %d\n        pkts_errored_egress ----: %d\n        pkts_discarded_ingress -: %d\n        pkts_discarded_egress --: %d\n        ingress_intf_speed -----: %d\n        egress_intf_speed ------: %d\n        ' % (ctypes.c_ulonglong(self.collection_timestamp).value,
         ctypes.c_uint(self.octet_input_ingress).value,
         ctypes.c_uint(self.octet_output_egress).value,
         ctypes.c_uint(self.pkts_errored_ingress).value,
         ctypes.c_uint(self.pkts_errored_egress).value,
         ctypes.c_uint(self.pkts_discarded_ingress).value,
         ctypes.c_uint(self.pkts_discarded_egress).value,
         ctypes.c_uint(self.ingress_intf_speed).value,
         ctypes.c_uint(self.egress_intf_speed).value)




class MemoryProfile(object):
    """
        Read only class containing MEMORY profile information of a node in trace
    
        collection_timestamp - time MEMORY information was collected
        proc_mem_util - memory in use by processes
    
        """


    def __init__(self, idl):
        self.collection_timestamp = idl.MemProfile.collection_timestamp
        self.proc_mem_util = idl.MemProfile.proc_mem_util



    def __str__(self):
        return '\n        *---------------*\n        | MemoryProfile |\n        *---------------*\n        collection_timestamp -: %d\n        proc_mem_util --------: %d\n        ' % (ctypes.c_ulonglong(self.collection_timestamp).value, self.proc_mem_util)




class PerfmonProfile(object):
    """ 
        Read only class containing PERFMON profile information of a node in trace
    
        src_ip - source IP address of node in trace
        dst_ip - destination IP address of node in trace
        src_port - Layer 4 source port of node in trace
        dst_port - Layer 4 destination port of node in trace
        collection_timestamp - time performance information was collected
        loss_of_measurement_confidence - loss of measurement confidence
        media_stop_event_occured - media stop event occured
        ip_packet_drop_count - packet drop count
        ip_byte_count - bytes processed
        ip_packet_count - packets processed
        route_fwd_status - mtrace.RouteStatus enum
        ip_dscp - DSCP number
        ip_ttl - time to live of trace
        flow_count - number of flows processed
        flow_dirn - direction of flows
        protocol - mtrace.Protocol enum
    
        """


    def __init__(self, idl):
        self.src_ip = NetworkInterface._convert_to_inetaddress(idl.PerfMonProfile.src_ip)
        self.dst_ip = NetworkInterface._convert_to_inetaddress(idl.PerfMonProfile.dst_ip)
        self.src_port = idl.PerfMonProfile.src_port
        self.dst_port = idl.PerfMonProfile.dst_port
        self.collection_timestamp = idl.PerfMonProfile.collection_timestamp
        self.loss_of_measurement_confidence = idl.PerfMonProfile.loss_of_measurement_confidence
        self.media_stop_event_occured = idl.PerfMonProfile.media_stop_event_occured
        self.ip_packet_drop_count = idl.PerfMonProfile.ip_packet_drop_count
        self.ip_byte_count = idl.PerfMonProfile.ip_byte_count
        self.ip_packet_count = idl.PerfMonProfile.ip_packet_count
        self.ip_byte_rate = idl.PerfMonProfile.ip_byte_rate
        self.route_fwd_status = idl.PerfMonProfile.route_fwd_status
        self.ip_dscp = idl.PerfMonProfile.ip_dscp
        self.ip_ttl = idl.PerfMonProfile.ip_ttl
        self.flow_count = idl.PerfMonProfile.flow_count
        self.flow_dirn = idl.PerfMonProfile.flow_dirn
        self.protocol = idl.PerfMonProfile.protocol



    def __str__(self):
        return '\n        *----------------*\n        | PerfmonProfile |\n        *----------------*\n        src_ip ---: %s\n        dst_ip ---: %s\n        src_port -: %d\n        dst_port -: %d\n        collection_timestamp -----------: %d\n        loss_of_measurement_confidence -: %d\n        media_stop_event_occured -------: %d\n        ip_packet_drop_count -----------: %d\n        ip_byte_count ----: %d\n        ip_packet_count --: %d\n        ip_byte_rate -----: %d\n        route_fwd_status -: %s\n        ip_dscp ----------: %d\n        ip_ttl -----------: %d\n        flow_count -------: %d\n        flow_dirn --------: %d\n        protocol ---------: %d\n        ' % (self.src_ip,
         self.dst_ip,
         ctypes.c_ushort(self.src_port).value,
         ctypes.c_ushort(self.dst_port).value,
         ctypes.c_ulonglong(self.collection_timestamp).value,
         self.loss_of_measurement_confidence,
         self.media_stop_event_occured,
         ctypes.c_ulonglong(self.ip_packet_drop_count).value,
         ctypes.c_ulonglong(self.ip_byte_count).value,
         ctypes.c_ulonglong(self.ip_packet_count).value,
         ctypes.c_uint(self.ip_byte_rate).value,
         self.route_fwd_status,
         self.ip_dscp,
         self.ip_ttl,
         ctypes.c_uint(self.flow_count).value,
         self.flow_dirn,
         self.protocol)




class MediatraceNode(object):
    """
        Read only class containing basic information of a node in trace
    
        hostname    - node name
        node_type   - mtrace.NodeType enum
        ip_ttl      - time to live of trace
        rtt         - round trip time of trace
        node_status - mtrace.NodeStatus enum
        profiles    - profile class of trace
    
        """

    _prof_map = {ProfileType.ECHO: EchoProfile,
     ProfileType.CPU: CPUProfile,
     ProfileType.INTERFACE: InterfaceProfile,
     ProfileType.MEMORY: MemoryProfile,
     ProfileType.PERFMON: PerfmonProfile}

    def __init__(self, idl):
        self.hostname = idl.hostname
        self.node_type = idl.node_type
        self.node_index = idl.node_index
        self.ip_ttl = idl.ip_ttl
        self.rtt = idl.rtt
        self.node_status = idl.node_status
        self.profiles = self._prof_map[idl.Profiles.profile_type](idl.Profiles)



    def __str__(self):
        return '\n        *----------------*\n        | MediatraceNode |\n        *----------------*\n        hostname ----: %s\n        node_type ---: %s\n        node_index --: %d\n        ip_ttl ------: %d\n        rtt ---------: %d\n        node_status -: %s\n        %s\n        ' % (self.hostname,
         NodeType.enumval(self.node_type),
         self.node_index,
         self.ip_ttl,
         self.rtt,
         NodeStatus.enumval(self.node_status),
         str(self.profiles))




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:18:42 IST
