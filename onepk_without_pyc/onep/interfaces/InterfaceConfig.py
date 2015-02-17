# 2015.02.05 17:21:22 IST
"""
@undocumented: InterfaceConfigSpeed
@undocumented: InterfaceConfigDuplex
@undocumented: InterfaceConfigFlowControl
@undocumented: InterfaceConfigAutoNeg
"""
from onep.core.util.Enum import enum

class InterfaceConfig(object):
    """
     This class represents the configuration (software property) of the network
     interface.
    
     The configuration might be changed during the life of the session. Hence, it
     is refreshed if the last accessed time has aged out.
     
     @ivar islayer2:
         Indicates if this a Layer-2 Interface
     @type islayer2: C{bool}
     
     @ivar display_name:
         The name of the interface.
     @type display_name: C{str}
     
     @ivar description:
         The description of the interface.
     @type description: C{str} 
     
     @ivar tx_bandwidth:
         The interface transmit bandwidth
     @type tx_bandwidth: C{int}
     
     @ivar rx_bandwidth:
         The interface receive bandwidth
     @type rx_bandwidth: C{int}
     
     @ivar mtu:
         The MTU value of the interface
     @type mtu: C{int}
     
     @ivar mac_address:
         The MAC address of the interface
     @type mac_address: C{str}
     
     @ivar undir_mode:
         Gets the unidirectional mode,
     @type undir_mode: L{UnidirMode<interfaces.InterfaceConfig.InterfaceConfig.UnidirMode>}
     
     @ivar encap:
            The interface encapsulation type.
     @type encap: L{Encap<interfaces.InterfaceConfig.InterfaceConfig.Encap>}
    
     @ivar snmp_index:
         The interface Simple Network Management Protocol (SNMP) index
     @type snmp_index: C{int}
     
     @undocumented: __init__
     @undocumented: DuplexMode
     @undocumented: speed
     @undocumented: duplex
     @undocumented: duplex_conf
     @undocumented: fwd_class_id
     @undocumented: flow_control
     @undocumented: auto_neg
     """

    Encap = enum('ONEP_IF_ENCAP_NULL', 'ONEP_IF_ENCAP_ANY', 'ONEP_IF_ENCAP_UNKNOWN', 'ONEP_IF_ENCAP_ARPA', 'ONEP_IF_ENCAP_LOOP', 'ONEP_IF_ENCAP_DOT1Q', 'ONEP_IF_ENCAP_ATM', 'ONEP_IF_ENCAP_SNAP', 'ONEP_IF_ENCAP_HDLC', 'ONEP_IF_ENCAP_PPP', 'ONEP_IF_ENCAP_ETHER', 'ONEP_IF_ENCAP_GRE', 'ONEP_IF_ENCAP_MPLS')
    UnidirMode = enum('ONEP_IF_UNIDIR_MODE_OFF', 'ONEP_IF_UNIDIR_MODE_SEND_ONLY', 'ONEP_IF_UNIDIR_MODE_RECV_ONLY', 'ONEP_IF_UNIDIR_MODE_NOT_SUPPORTED')
    DuplexMode = enum('ONEP_IF_HALF_DUPLEX', 'ONEP_IF_FULL_DUPLEX', 'ONEP_IF_AUTO_DUPLEX', 'ONEP_IF_DUPLEX_NOT_SUPPORTED')
    SwitchportMode = enum('ONEP_IF_SWITCHPORT', 'ONEP_IF_SWITCHPORT_MODE_ACCESS', 'ONEP_IF_SWITCHPORT_MODE_DOT1Q_TUNNEL', 'ONEP_IF_SWITCHPORT_MODE_TRUNK', 'ONEP_IF_SWITCHPORT_MODE_NOT_SUPPORTED')

    def __init__(self, encap, unidir_mode, mtu, rx_bandwidth, tx_bandwidth, snmp_index, islayer2, display_name, mac_address, description, ip_redirect, ip_unreachable, ip_proxy_arp, ip_unicast_reverse_path, vrf, speed = None, duplex = None, duplex_conf = None, fwdClassID = None, flow_control = None, auto_neg = None):
        """
        Constructor of InterfaceConfig class.
        """
        self.encap = encap
        self.unidir_mode = unidir_mode
        self.mtu = mtu
        self.rx_bandwidth = rx_bandwidth
        self.tx_bandwidth = tx_bandwidth
        self.snmp_index = snmp_index
        self.islayer2 = islayer2
        self.display_name = display_name
        self.mac_address = mac_address
        self.description = description
        self.iphelper = []
        self.ip_redirect = bool(ip_redirect)
        self.ip_unreachable = bool(ip_unreachable)
        self.ip_proxy_arp = bool(ip_proxy_arp)
        self.ip_unicast_reverse_path = bool(ip_unicast_reverse_path)
        self.vrf = vrf
        self.speed = speed
        self.duplex = duplex
        self.duplex_conf = duplex_conf
        self.fwd_class_id = fwdClassID
        self.flow_control = flow_control
        self.auto_neg = auto_neg



    def __str__(self):
        """ Returns the configuration in string format. """
        tmp = 'Interface Configuration'
        tmp += '\n Interface Name: ' + str(self.display_name)
        tmp += '\n MAC Address: ' + str(self.mac_address)
        tmp += '\n Rx Bandwidth: ' + str(self.rx_bandwidth)
        tmp += '\n Tx Bandwidth: ' + str(self.tx_bandwidth)
        tmp += '\n MTU: ' + str(self.mtu)
        tmp += '\n SNMP Index: ' + str(self.snmp_index)
        tmp += '\n Layer2: ' + str(self.islayer2)
        tmp += '\n Encapsulation: ' + str(self.Encap.enumval(self.encap))
        tmp += '\n Mode: ' + str(self.UnidirMode.enumval(self.unidir_mode))
        tmp += '\n Description: ' + str(self.description)
        tmp += '\n IP helper-addresses: ' + str(self.iphelper)
        tmp += '\n IP redirect: ' + str(self.ip_redirect)
        tmp += '\n IP unreachable: ' + str(self.ip_unreachable)
        tmp += '\n IP proxy ARP: ' + str(self.ip_proxy_arp)
        tmp += '\n IP unicast reverse path: ' + str(self.ip_unicast_reverse_path)
        tmp += '\n Virtual Route Forwarding: %s' % str(self.vrf)
        return tmp




class TunnelInterfaceConfig(InterfaceConfig):
    """     
        Tunnel interface for network element 
    
        """


    def __init__(self, encap, unidir_mode, mtu, rx_bandwidth, tx_bandwidth, snmp_index, islayer2, display_name, mac_address, description, ip_redirect, ip_unreachable, ip_proxy_arp, ip_unicast_reverse_path, vrf, tunnel_id = None, source_ip = None, dest_ip = None, ipsec_mode = None, ipsec_profile = None, ike_profile = None, speed = None, duplex = None, duplex_conf = None, fwdClassID = None, flow_control = None, auto_neg = None):
        self.tunnel_id = tunnel_id
        self.source_ip = source_ip
        self.dest_ip = dest_ip
        self.ipsec_mode = ipsec_mode
        self.ipsec_profile = ipsec_profile
        self.ike_profile = ike_profile
        self.vrf = vrf
        InterfaceConfig.__init__(self, encap, unidir_mode, mtu, rx_bandwidth, tx_bandwidth, snmp_index, islayer2, display_name, mac_address, description, ip_redirect, ip_unreachable, ip_proxy_arp, ip_unicast_reverse_path, vrf, speed, duplex, duplex_conf, fwdClassID, flow_control, auto_neg)



    def __str__(self):
        tmp = InterfaceConfig.__str__(self)
        tmp += '\n Tunnel ID: ' + str(self.tunnel_id)
        tmp += '\n Tunnel source: ' + str(self.source_ip)
        tmp += '\n Tunnel destination: ' + str(self.dest_ip)
        tmp += '\n Tunnel IPsec mode: ' + str(self.ipsec_mode)
        tmp += '\n Tunnel IPsec profile: ' + str(self.ipsec_profile)
        tmp += '\n Tunnel IKE profile: ' + str(self.ike_profile)
        tmp += '\n Virtual Route Forwarding: %s' % str(self.vrf)
        return tmp




class InterfaceConfigSpeed:
    """
    Speed configuration for the network element.
    """


    def __init__(self, capability, configured, operational):
        self._capability = capability
        self._configured = configured
        self._operational = operational



    def _get_capability(self):
        return _capability


    capability = property(_get_capability, None)

    def _get_configured(self):
        return _configured


    configured = property(_get_configured, None)

    def _get_operational(self):
        return _operational


    operational = property(_get_operational, None)

    def __str__(self):
        tmp = 'Interface Speed Config'
        tmp += '\n capability: ' + str(self._capability)
        tmp += '\n configured: ' + str(self._configured)
        tmp += '\n operational: ' + str(self._operational)
        return tmp




class InterfaceConfigDuplex:
    """
    Duplex configuration for the network element.
    """


    def __init__(self, configured, operational):
        self._configured = configured
        self._operational = operational



    def _get_configured(self):
        return _configured


    configured = property(_get_configured, None)

    def _get_operational(self):
        return _operational


    operational = property(_get_operational, None)

    def __str__(self):
        tmp = 'Interface Duplex Config'
        tmp += '\n configured: ' + InterfaceConfig.DuplexMode.enumval(self._configured)
        tmp += '\n operational: ' + InterfaceConfig.DuplexMode.enumval(self._operational)
        return tmp




class InterfaceConfigFlowControl:
    """
    Flow control configuration for the network element.
    """


    def __init__(self, ip_configured, ip_operational, op_configured, op_operational):
        self._ip_configured = ip_configured
        self._ip_operational = ip_operational
        self._op_configured = op_configured
        self._op_operational = op_operational



    def _get_ip_configured(self):
        return _ip_configured


    ip_configured = property(_get_ip_configured, None)

    def _get_ip_operational(self):
        return _ip_operational


    ip_operational = property(_get_ip_operational, None)

    def _get_op_configured(self):
        return _op_configured


    op_configured = property(_get_op_configured, None)

    def _get_op_operational(self):
        return _op_operational


    op_operational = property(_get_op_operational, None)

    def __str__(self):
        tmp = 'Interface Flow Control Config'
        tmp += '\n input_configured: ' + str(self._ip_configured)
        tmp += '\n input_operational: ' + str(self._ip_operational)
        tmp += '\n output_configured: ' + str(self._op_configured)
        tmp += '\n output_operational: ' + str(self._op_operational)
        return tmp




class InterfaceConfigAutoNeg:
    """
    Auto negotiation configuration for the network element.
    """


    def __init__(self, configured, operational):
        self._configured = configured
        self._operational = operational



    def _get_configured(self):
        return _configured


    configured = property(_get_configured, None)

    def _get_operational(self):
        return _operational


    operational = property(_get_operational, None)

    def __str__(self):
        tmp = 'Interface Auto Negotiation Config'
        tmp += '\n configured: ' + str(self._configured)
        tmp += '\n operational: ' + str(self._operational)
        return tmp




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:21:23 IST
