# 2015.02.05 17:18:26 IST
import re
import logging
import socket
import onep.core.util.socket_imp
from array import array
from onep.core.util.OnepArgumentTypeValidate import validate, validate_none
from onep.core.util.Enum import enum
from onep.core.util.OnepConstants import OnepConstants
from onep.core.exception.OnepIllegalArgumentException import OnepIllegalArgumentException
from onep.core.exception.OnepRemoteProcedureException import OnepRemoteProcedureException
from onep.core.exception.OnepConnectionException import OnepConnectionException
from onep.core.exception.OnepException import OnepException, OnepConflictException
from onep.thrift.Thrift import TException
from Shared.ttypes import NetworkAddressIDL, ExceptionIDL, InterfaceFilterIDL
from onep.CdpIDL import CdpIDL
from onep.NetworkInterfaceIDL import NetworkInterfacesIDL
from onep.interfaces.InterfaceConfig import InterfaceConfig, TunnelInterfaceConfig, InterfaceConfigSpeed, InterfaceConfigDuplex, InterfaceConfigFlowControl, InterfaceConfigAutoNeg
from onep.interfaces.InterfaceProperty import InterfaceProperty
from onep.interfaces.InterfaceStatistics import InterfaceStatistics
from onep.interfaces.InterfaceStatisticsFilter import InterfaceStatisticsFilter
from onep.interfaces.InterfaceStatus import InterfaceStatus
from onep.interfaces.NetworkPrefix import NetworkPrefix
from onep.interfaces.Vlan import Vlan
from onep.interfaces.InterfaceStateListener import InterfaceStateListener
from onep.interfaces.InterfaceStatisticsListener import InterfaceStatisticsListener
from onep.cdp.CDPListener import CDPListener
try:
    from onep.routing.vrf import Vrf
    from onep.vty.VtyProxy import VtyProxy
except ImportError:
    pass
from onep.core.util.HostIpCheck import HostIpCheck
from onep.core.util import deprecated

class NetworkInterface(object):
    """ 
        This class represents a NetworkInterface. It is used for both physical and logical interfaces.
    
        @cvar name:
        The name of the network Interface.        
        @type name: C{str}
        
        @cvar xos_handle:
        The Network Interface Handle
        @type xos_handle: C{int}
        
        @cvar interface_type:
        The type of the network Interface
        @type interface_type: L{InterfaceTypes<interfaces.NetworkInterface.NetworkInterface.InterfaceTypes>}
    
        @cvar network_element:
        The source network element to which the interface belongs
        @type network_element: L{NetworkElement<onep.element.NetworkElement.NetworkElement>}
        
        @undocumented: get_vlan
        @undocumented: get_vrf_name
        @undocumented: set_load_interval
        @undocumented: set_switchport_mode
        """

    InterfaceTypes = enum('ONEP_IF_TYPE_UNSUPPORTED', 'ONEP_IF_TYPE_ANY', 'ONEP_IF_TYPE_NULL', 'ONEP_IF_TYPE_LOOPBACK', 'ONEP_IF_TYPE_ETHERNET', 'ONEP_IF_TYPE_ETHER_CHANNEL', 'ONEP_IF_TYPE_GIGABIT_ETHERNET', 'ONEP_IF_TYPE_SERIAL', 'ONEP_IF_TYPE_TUNNEL', 'ONEP_IF_TYPE_P2P', 'ONEP_IF_TYPE_MULTI_LINK', 'ONEP_IF_TYPE_TE', 'ONEP_IF_TYPE_PSEUDOWIRE', 'ONEP_IF_TYPE_WIRELESS', 'ONEP_IF_TYPE_ATM', 'ONEP_IF_TYPE_FRAME_RELAY', 'ONEP_IF_TYPE_VLAN', 'ONEP_IF_TYPE_PPP', 'ONEP_IF_TYPE_MLP_BUNDLE', 'ONEP_IF_TYPE_POS', 'ONEP_IF_TYPE_POS_CHANNEL', 'ONEP_IF_TYPE_NATIVE_VLAN', 'ONEP_IF_TYPE_HDLC', 'ONEP_IF_TYPE_EFP', 'ONEP_IF_TYPE_BVI', 'ONEP_IF_TYPE_INTERFLEX_LEFT', 'ONEP_IF_TYPE_INTERFLEX_RIGHT', 'ONEP_IF_TYPE_PSEUDOWIRE_HE', 'ONEP_IF_TYPE_SUB_INTERFACE', 'ONEP_IF_TYPE_MANAGEMENT')
    IANAType = {'ONEP_IF_IANA_TYPE_ANY': 0,
     'ONEP_IF_IANA_TYPE_OTHER': 1,
     'ONEP_IF_IANA_TYPE_LOOPBACK': 24,
     'ONEP_IF_IANA_TYPE_ETHERNET': 6,
     'ONEP_IF_IANA_TYPE_ETHER_CHANNEL': 161,
     'ONEP_IF_IANA_TYPE_GIGABIT_ETHERNET': 6,
     'ONEP_IF_IANA_TYPE_SERIAL': 22,
     'ONEP_IF_IANA_TYPE_TUNNEL': 132,
     'ONEP_IF_IANA_TYPE_P2P': 23,
     'ONEP_IF_IANA_TYPE_MULTI_LINK': 121,
     'ONEP_IF_IANA_TYPE_TE': 200,
     'ONEP_IF_IANA_TYPE_PSEUDOWIRE': 246,
     'ONEP_IF_IANA_TYPE_WIRELESS': 157,
     'ONEP_IF_IANA_TYPE_ATM': 37,
     'ONEP_IF_IANA_TYPE_FRAME_RELAY': 32,
     'ONEP_IF_IANA_TYPE_VLAN': 136,
     'ONEP_IF_IANA_TYPE_PPP': 23,
     'ONEP_IF_IANA_TYPE_MLP_BUNDLE': 121,
     'ONEP_IF_IANA_TYPE_POS': 171,
     'ONEP_IF_IANA_TYPE_CHANNEL': 70,
     'ONEP_IF_IANA_TYPE_HDLC': 118,
     'ONEP_IF_IANA_TYPE_EFP': 135,
     'ONEP_IF_IANA_TYPE_BVI': 209}
    interfaceTypeMap = {InterfaceTypes.ONEP_IF_TYPE_NULL: IANAType['ONEP_IF_IANA_TYPE_OTHER'],
     InterfaceTypes.ONEP_IF_TYPE_LOOPBACK: IANAType['ONEP_IF_IANA_TYPE_LOOPBACK'],
     InterfaceTypes.ONEP_IF_TYPE_ETHERNET: IANAType['ONEP_IF_IANA_TYPE_ETHERNET'],
     InterfaceTypes.ONEP_IF_TYPE_ETHER_CHANNEL: IANAType['ONEP_IF_IANA_TYPE_ETHER_CHANNEL'],
     InterfaceTypes.ONEP_IF_TYPE_GIGABIT_ETHERNET: IANAType['ONEP_IF_IANA_TYPE_ETHERNET'],
     InterfaceTypes.ONEP_IF_TYPE_SERIAL: IANAType['ONEP_IF_IANA_TYPE_SERIAL'],
     InterfaceTypes.ONEP_IF_TYPE_TUNNEL: IANAType['ONEP_IF_IANA_TYPE_TUNNEL'],
     InterfaceTypes.ONEP_IF_TYPE_P2P: IANAType['ONEP_IF_IANA_TYPE_P2P'],
     InterfaceTypes.ONEP_IF_TYPE_MULTI_LINK: IANAType['ONEP_IF_IANA_TYPE_MULTI_LINK'],
     InterfaceTypes.ONEP_IF_TYPE_TE: IANAType['ONEP_IF_IANA_TYPE_TE'],
     InterfaceTypes.ONEP_IF_TYPE_PSEUDOWIRE: IANAType['ONEP_IF_IANA_TYPE_PSEUDOWIRE'],
     InterfaceTypes.ONEP_IF_TYPE_WIRELESS: IANAType['ONEP_IF_IANA_TYPE_WIRELESS'],
     InterfaceTypes.ONEP_IF_TYPE_ATM: IANAType['ONEP_IF_IANA_TYPE_ATM'],
     InterfaceTypes.ONEP_IF_TYPE_FRAME_RELAY: IANAType['ONEP_IF_IANA_TYPE_FRAME_RELAY'],
     InterfaceTypes.ONEP_IF_TYPE_VLAN: IANAType['ONEP_IF_IANA_TYPE_VLAN'],
     InterfaceTypes.ONEP_IF_TYPE_PPP: IANAType['ONEP_IF_IANA_TYPE_PPP'],
     InterfaceTypes.ONEP_IF_TYPE_MLP_BUNDLE: IANAType['ONEP_IF_IANA_TYPE_MLP_BUNDLE'],
     InterfaceTypes.ONEP_IF_TYPE_POS: IANAType['ONEP_IF_IANA_TYPE_POS'],
     InterfaceTypes.ONEP_IF_TYPE_POS_CHANNEL: IANAType['ONEP_IF_IANA_TYPE_CHANNEL'],
     InterfaceTypes.ONEP_IF_TYPE_NATIVE_VLAN: IANAType['ONEP_IF_IANA_TYPE_OTHER'],
     InterfaceTypes.ONEP_IF_TYPE_HDLC: IANAType['ONEP_IF_IANA_TYPE_HDLC'],
     InterfaceTypes.ONEP_IF_TYPE_EFP: IANAType['ONEP_IF_IANA_TYPE_EFP'],
     InterfaceTypes.ONEP_IF_TYPE_BVI: IANAType['ONEP_IF_IANA_TYPE_BVI'],
     InterfaceTypes.ONEP_IF_TYPE_PSEUDOWIRE_HE: IANAType['ONEP_IF_IANA_TYPE_OTHER'],
     InterfaceTypes.ONEP_IF_TYPE_ANY: IANAType['ONEP_IF_IANA_TYPE_ANY']}
    ONEP_IF_ALL_HANDLES = -1
    _name = 'unknown'
    _xos_handle = 0
    _interface_type = InterfaceTypes.ONEP_IF_TYPE_UNSUPPORTED
    _network_element = None
    _property = None
    cdp_client = None
    _api_client = None
    _stats_list = None
    _log = logging.getLogger(__name__)

    @property
    def name(self):
        return self._name



    @property
    def interface_type(self):
        return self._interface_type



    @property
    def network_element(self):
        return self._network_element



    @property
    def xos_handle(self):
        return self._xos_handle



    def __init__(self, element, name, type_, xoshandle):
        """
        Constructor of NetworkInterface class.
        """
        self._network_element = element
        if element != None:
            self._api_client = NetworkInterfacesIDL.Client(element.api_protocol)
        self._interface_type = type_
        self._xos_handle = xoshandle
        self._name = name
        self._vty = None



    def __str__(self):
        """  The str() method returns the string representation of the NetworkInterface instance."""
        sb = ''
        sb += '\nNetworkInterface [ ' + self.name + ' ]\n'
        if self.network_element != None:
            sb += str(self.network_element) + '\n'
        sb += '\tType             : ' + str(self.InterfaceTypes.enumval(self.interface_type)) + '\n'
        if self._property != None:
            sb += '\tSlot             : %d' % self._property.slot + '\n'
            sb += '\tPort             : %d' % self._property.port + '\n'
        return sb



    def __eq__(self, other):
        """        
        Two interface Objects are equal if they have the same network interface unique id and
        have the same NetworkElement parent Object.
        
        @param other: L{NetworkInterface<interfaces.NetworkInterface.NetworkInterface>}
        @rtype: C{bool}                  
        """
        if other == None:
            return False
        if not isinstance(other, type(self)):
            return False
        return self.xos_handle == other.xos_handle and self.network_element == other.network_element



    def _interface_IANA_type(self):
        return self.interfaceTypeMap[self._interface_type]


    IANA_type = property(_interface_IANA_type)

    @classmethod
    def get_interface_instance_by_type(self, element, name, type, xoshandle):
        """
                Return an instantiated Network Interface class according to type
        
                """
        (base, dot, sub,) = name.partition('.')
        if type == self.InterfaceTypes.ONEP_IF_TYPE_TUNNEL:
            return TunnelInterface(element, name, type, xoshandle)
        if type == self.InterfaceTypes.ONEP_IF_TYPE_LOOPBACK:
            return LoopbackInterface(element, name, type, xoshandle)
        if len(sub) > 0 and sub.isdigit():
            return SubInterface(element, name, type, xoshandle)
        return NetworkInterface(element, name, type, xoshandle)



    def equals(self, other):
        """
        Checks if two NetworkInterface Objects are equal or not.
        
        Two interface Objects are equal if they have the same network interface unique id and
        have the same NetworkElement parent Object.
        
        @param other: L{NetworkInterface<interfaces.NetworkInterface.NetworkInterface>}
        @rtype: C{bool}    
        @raise OnepIllegalArgumentException: 
            This exception is thrown if input parameter is not specified or 
            if it is not a NetworkInterface object.                
        """
        validate(other, type(self))
        validate_none(other, 'Network Interface to be compared')
        ni = other
        return self.xos_handle == ni.xos_handle and self.network_element == ni.network_element



    def get_statistics(self):
        """ Returns the NetworkInterface Statistics after querying the router.
        
        @rtype: L{InterfaceStatistics<interfaces.InterfaceStatistics.InterfaceStatistics>}
        
        @raise OnepRemoteProcedureException: System failure to serve the request, please check error
                message for more details.
        @raise OnepConnectionException : Transport error, may need to reset the connection, please 
                check the error message for more details.    
        """
        try:
            stats_idl = self._api_client.NetworkInterface_getStatisticsIDL(self.xos_handle)
            self._log.info('Returned from idl call to retrieve Interface Statistics')
            if_stats = InterfaceStatistics(stats_idl)
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as t:
            raise OnepConnectionException(t.message, t)
        return if_stats



    def _get_statistics_ultra(self):
        """Internal API for Ultra. It gets the non-cumulative stats 
        from the time clear_statistics() was called.
        """
        if not self._stats_list:
            return self.get_statistics()
        else:
            return InterfaceStatistics([ self._subtract_stat_idls(new_stat, cached_stat) for (new_stat, cached_stat,) in zip(self.get_statistics().stats_list, self._stats_list) ])



    def _subtract_stat_idls(self, stat_idl1, stat_idl2):
        stat_idl1.stats = stat_idl1.stats - stat_idl2.stats
        return stat_idl1



    def get_property(self):
        """ Gets the hardware property of the NetworkInterface.
        
           The property is only retrieved once from the NetworkElement. It is hard
           property of the interface which do not change during life of the session.
           
           @rtype: L{InterfaceProperty<interfaces.InterfaceProperty.InterfaceProperty>}
           
           @raise OnepRemoteProcedureException: System failure to serve the request, please check error
                   message for more details.
           @raise OnepConnectionException : Transport error, may need to reset the connection, please 
                   check the error message for more details.    
           """
        if self._property == None:
            try:
                property_idl = self._api_client.NetworkInterface_getPropertyIDL(self.xos_handle)
                self._log.info('Returned from idl call to retrieve Interface Property')
                self._property = InterfaceProperty(property_idl.slot, property_idl.port, property_idl.speed, property_idl.shortname, property_idl.subif_id)
            except ExceptionIDL as e:
                raise OnepRemoteProcedureException(e)
            except TException as t:
                raise OnepConnectionException(t.message, t)
        return self._property



    def get_status(self):
        """ Gets the snapshot status of the NetworkInterface.
        
           The status is a snapshot of the current condition of the NetworkInterface
           attributes. The status is retrieved on demand on every invocation.
            
           @rtype: L{InterfaceStatus<interfaces.InterfaceStatus.InterfaceStatus>}
            
           @raise OnepRemoteProcedureException: System failure to serve the request, please check error
                   message for more details.
           @raise OnepConnectionException : Transport error, may need to reset the connection, please 
                   check the error message for more details.    
           """
        try:
            status_idl = self._api_client.NetworkInterface_getStatusIDL(self.xos_handle)
            self._log.info('Returned from idl call to retrieve Interface Status')
            status = InterfaceStatus(status_idl.link, status_idl.lineproto, self.name)
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as t:
            raise OnepConnectionException(t.message, t)
        return status



    @classmethod
    def _int2hex(cls, int_list):
        cls._log.info('Converting mac-address from integer to hex format')
        hex_string = ''
        for t in int_list:
            if t < 0:
                t += 256
            hex_string += '%02x ' % t

        hex_string = hex_string.strip()
        hex_string = re.sub('\\s', '.', hex_string)
        return hex_string



    def _chk_vty(self):
        if not self._vty:
            try:
                self._vty = VtyProxy(self._network_element)
            except NameError:
                from onep.vty.VtyProxy import VtyProxy
                self._vty = VtyProxy(self._network_element)



    def get_config(self):
        """ Gets the configuration of the NetworkInterface.
        
        The software property comes from the configuration of the NetworkInterface, which might be changed 
        during its session of life via configuration. The configuration is refreshed on every invocation.
        
        @rtype: L{InterfaceConfiguration<interfaces.InterfaceConfig.InterfaceConfig>}
        
        @raise OnepRemoteProcedureException: System failure to serve the request, please check error
                message for more details.
        @raise OnepConnectionException : Transport error, may need to reset the connection, please 
                check the error message for more details.    
        """
        try:
            config_idl = self._api_client.NetworkInterface_getConfigIDL(self.xos_handle)
            self._log.info('Returned from idl call to retrieve Interface Configuration')
            mac_addr = self._int2hex(config_idl.macaddr)
            self._log.info('Converted mac-address to hex format successfully %s', mac_addr)
            speed = None
            if config_idl.speedIDL:
                speed = InterfaceConfigSpeed(config_idl.speedIDL.capability, config_idl.speedIDL.configured, config_idl.speedIDL.operational)
            duplex_conf = None
            if config_idl.duplexIDL:
                duplex_conf = InterfaceConfigDuplex(config_idl.duplexIDL.configured, config_idl.duplexIDL.operational)
            flow_control = None
            if config_idl.fcIDL:
                flow_control = InterfaceConfigFlowControl(config_idl.fcIDL.input_configured, config_idl.fcIDL.input_operational, config_idl.fcIDL.output_configured, config_idl.fcIDL.output_operational)
            auto_neg = None
            if config_idl.autoNegIDL:
                auto_neg = InterfaceConfigAutoNeg(config_idl.autoNegIDL.configured, config_idl.autoNegIDL.operational)
            vrf_name = None
            try:
                vrf_name = self.get_vrf_name()
            except OnepRemoteProcedureException as e:
                pass
            config = InterfaceConfig(config_idl.encap, config_idl.mode, config_idl.mtu, config_idl.rx, config_idl.tx, config_idl.snmp, config_idl.layer2, config_idl.displayName, mac_addr, config_idl.descr, config_idl.ipRedirect, config_idl.ipUnreachable, config_idl.ipProxyArp, config_idl.ipUnicastReversePath, vrf_name, speed, config_idl.duplex, duplex_conf, config_idl.fwdClassID, flow_control, auto_neg)
            config.iphelper = []
            if config_idl.ipHelperAddr:
                for helper in config_idl.ipHelperAddr:
                    config.iphelper.append(self._convert_to_inetaddress(helper))

            self._log.info('InterfaceConfig object created successfully %s', config.__str__())
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as t:
            raise OnepConnectionException(t.message, t)
        return config



    def get_subinterface_list(self):
        """ Gets all the sub-interfaces attached to this network interface if any. 
        
        For instance eth0:1 will be a sub-interface to eth0.
        If no subinterfaces under the interface, the interface itself is returned. 
        
        
        @returns: A dictionary with all the available sub-interfaces keyed by sub-interface name.
        @rtype: C{dictionary}
        @raise OnepRemoteProcedureException: System failure to serve the request, please check error
                message for more details.
        @raise OnepConnectionException : Transport error, may need to reset the connection, please 
                check the error message for more details.    
        """
        sub_interfaces_dict = {}
        try:
            subInterfacesList_idl = self._api_client.NetworkInterface_getSubInterfaceIDL(self.xos_handle)
            self._log.info('Returned from idl call to retrieve Sub Interface List')
            for subinterface in subInterfacesList_idl:
                intf = NetworkInterface(self.network_element, subinterface.name, subinterface.type, subinterface.xosHandle)
                sub_interfaces_dict[subinterface.name] = intf

            self._log.info('Created Dictionary consisting of sub-interfaces')
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as t:
            raise OnepConnectionException(t.message, t)
        return sub_interfaces_dict



    def get_parent(self):
        """ Gets the parent NetworkInterface of this interface if this is a
        sub-interface, or None if it is a physical (non virtual) interface or has
        no parent.
        
        @rtype: L{NetworkInterface<interfaces.NetworkInterface.NetworkInterface>}
        @return: The NetworkInterface this interface is attached to.
        
        @raise OnepRemoteProcedureException: System failure to serve the request, please check error
                message for more details.
        @raise OnepConnectionException : Transport error, may need to reset the connection, please 
                check the error message for more details.    
        """
        try:
            parent_idl = self._api_client.NetworkInterface_getParentIDL(self.xos_handle)
            self._log.info('Returned from idl call to retrieve Parent Interface')
            if parent_idl != None:
                parent_interface = NetworkInterface(self.network_element, parent_idl.name, parent_idl.type, parent_idl.xosHandle)
                self._log.debug('parent Interface Created %s', parent_interface.__str__())
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as t:
            raise OnepConnectionException(t.message, t)
        return parent_interface



    def get_vrf_name(self):
        """
        Gets the VRF (Virtual Routing Forwarding) name associated with the network interface.
        
        @rtype: C{str}
        @raise OnepRemoteProcedureException: System failure to serve the request, please check error
                        message for more details.
        @raise OnepConnectionException : Transport error, may need to reset the connection, please 
                        check the error message for more details.
        """
        try:
            vrf = self._api_client.NetworkInterface_getVrfIDL(self.xos_handle)
            self._log.info('Retreived VRF name')
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e.message, e)
        return vrf



    def get_vlan(self):
        """
            Gets the Layer 3 VLAN information of the network interface.
            This method obtains the Layer 3 VLAN information such as encapsulation 
            and tags. 
            
            @rtype: L{Vlan<onep.interfaces.Vlan.Vlan>}
            @raise OnepRemoteProcedureException: System failure to serve the request, please check error
                            message for more details.
            @raise OnepConnectionException : Transport error, may need to reset the connection, please 
                            check the error message for more details.
        
            """
        try:
            vlan_idl = self._api_client.NetworkInterface_getVlanIDL(self.xos_handle)
            vlan = Vlan.from_idl(vlan_idl)
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e.message, e)
        return vlan



    def set_vlan(self, param):
        """ the parameter has key 'encap-type', 'vlan-tag1', and optional 'vlan-tag2'
        """
        self._log.info('set_vlan ')
        self._chk_vty()
        vlan_tag1 = vlan_tag2 = None
        encap_type = 'DOT1Q'
        if param.has_key('vlan-tag1'):
            vlan_tag1 = param['vlan-tag1']
        if param.has_key('vlan-tag2'):
            vlan_tag2 = param['vlan-tag2']
        if param.has_key('encap-type'):
            encap_type = param['encap-type']
        cli = 'interface %s\n' % self.name + 'encap dot1q %s' % vlan_tag1
        if vlan_tag2 and encap_type == 'QINQ':
            cli += ' second-dot1q ' + str(vlan_tag2)
        ret = self._vty.config(cli)
        if 'Configuration of multiple subinterfaces of the same main' in ret:
            (head, tmp, detail,) = ret.partition('%')
            raise OnepConflictException(detail)



    def remove_vlan(self):
        self._log.info('remove_vlan')
        self._chk_vty()
        lines = _get_section_config(self, self.name)
        if lines:
            line = [ line for line in lines.splitlines() if line.lstrip().startswith('encapsulation dot1Q ') ]
            if line:
                cli = 'interface %s\n' % self.name + 'no ' + line[0]
                self._vty.config(cli)


    doc_vlan = '\n        subinterface dot1q vlan tag\n        '
    vlan = property(get_vlan, set_vlan, remove_vlan, doc_vlan)

    @classmethod
    def get_empty_interface(cls):
        """ Creates dummy interface that matches any interface to be used in Interface filter.
        
        This is equivalent of empty interface object.
        
        @rtype: L{NetworkInterface<interfaces.NetworkInterface.NetworkInterface>} 
        """
        cls._log.info('Returning an empty Interface')
        return NetworkInterface(None, 'unknown', cls.InterfaceTypes.ONEP_IF_TYPE_ANY, cls.ONEP_IF_ALL_HANDLES)



    def set_mtu(self, mtu):
        """ Sets MTU for an interface.
        
        @param mtu: 
            The MTU value which should be set on the interface.Must be of integer type.
        @type mtu: C{int} 
        @raise OnepRemoteProcedureException: System failure to serve the request, please check error
                message for more details.
        @raise OnepConnectionException : Transport error, may need to reset the connection, please 
                check the error message for more details.     
        @raise OnepIllegalArgumentException : This exception is thrown if input parameter is not specified or if 
                it is not of type integer.
        """
        validate_none(mtu, 'MTU')
        validate(mtu, int)
        try:
            self._api_client.NetworkInterface_setMTUIDL(self.xos_handle, mtu)
            self._log.info('Returned from idl call to set MTU to %d', mtu)
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as t:
            raise OnepConnectionException(t.message, t)



    def set_description(self, description):
        """ Sets the interface description.
        
        @param description: 
            The interface description. Must be of string type.
        @type description: C{str} 
        @raise OnepRemoteProcedureException: System failure to serve the request, please check error
                message for more details.
        @raise OnepConnectionException : Transport error, may need to reset the connection, please 
                check the error message for more details.     
        @raise OnepIllegalArgumentException : This exception is thrown if input parameter is not specified or if 
                it is not of type integer.
        """
        validate_none(description, 'description')
        validate(description, str)
        if len(description) >= OnepConstants.INTERFACE_DESCRIPTION_SIZE:
            description = description[:(OnepConstants.INTERFACE_DESCRIPTION_SIZE - 1)]
        try:
            self._api_client.NetworkInterface_setDescriptionIDL(self.xos_handle, description)
            self._log.info('Returned from idl call to set description to %s', description)
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as t:
            raise OnepConnectionException(t.message, t)



    def set_bw(self, bw):
        """ Sets the interface Bandwidth.
        
        @param bw: 
            The Bandwidth value which should be set on the interface.Must be of integer type.
        @type bw: C{int} 
        @raise OnepRemoteProcedureException: System failure to serve the request, please check error
                message for more details.
        @raise OnepConnectionException : Transport error, may need to reset the connection, please 
                check the error message for more details.     
        @raise OnepIllegalArgumentException : This exception is thrown if input parameter is not specified or if 
                it is not of type integer.
        """
        validate_none(bw, 'bw')
        validate(bw, int)
        try:
            self._api_client.NetworkInterface_setBwIDL(self.xos_handle, bw)
            self._log.info('Returned from idl call to set bw to %d', bw)
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as t:
            raise OnepConnectionException(t.message, t)



    def set_encapsulation(self, encapsulation):
        """ Sets the interface encapsulation
        
        @param encapsulation: 
            The interface encapsulation
        @type encapsulation: L{InterfaceConfig.Encap<interfaces.InterfaceConfig.Encap>}
        @raise OnepRemoteProcedureException: System failure to serve the request, please check error
                message for more details.
        @raise OnepConnectionException : Transport error, may need to reset the connection, please 
                check the error message for more details.     
        @raise OnepIllegalArgumentException : This exception is thrown if input parameter is not specified or if 
                it is not of type integer.
        """
        validate_none(encapsulation, 'encapsulation')
        validate(encapsulation, int)
        try:
            self._api_client.NetworkInterface_setEncapIDL(self.xos_handle, encapsulation)
            self._log.info('Returned from idl call to set encapsulation to %d', encapsulation)
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as t:
            raise OnepConnectionException(t.message, t)



    def set_switchport_mode(self, mode):
        """ Sets the interface switchport mode
        
        @param mode:
            The interface switchport mode.
        @type mode: L{InterfaceConfig.SwitchportMode<interfaces.InterfaceConfig.SwitchportMode>}
        @raise OnepRemoteProcedureException: System failure to serve the request, please check error
                message for more details.
        @raise OnepConnectionException : Transport error, may need to reset the connection, please 
                check the error message for more details.     
        @raise OnepIllegalArgumentException : This exception is thrown if input parameter is not specified or if 
                it is not of type integer.
        """
        validate_none(mode, 'switchport_mode')
        validate(mode, int)
        try:
            self._api_client.NetworkInterface_setSwitchportModeIDL(self.xos_handle, mode)
            self._log.info('Returned from idl call to set switchport mode to %d', mode)
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as t:
            raise OnepConnectionException(t.message, t)



    def shut_down(self, shutdown):
        """ Sets interface admin state to down or up.
        
        This method is equivalent of configuration command to shutdown an interface. 
        
        Applications can set the shutdown value to TRUE to administratively shutdown the interface.
        
        Applications can set the shutdown value to FALSE to administratively bring the interface up.
        
        @param shutdown: 
             Value indicating if it is a shutdown/bringup operation. 1  to shutdown the interface and 0 to bring up the interface
        @type shutdown: C{int}
        @raise OnepRemoteProcedureException: System failure to serve the request, please check error
                message for more details.
        @raise OnepConnectionException : Transport error, may need to reset the connection, please 
                check the error message for more details.     
        @raise OnepIllegalArgumentException : This exception is thrown if input parameter is not specified or if 
                it is not of type integer.
        """
        validate_none(shutdown, 'Shutdown ')
        if shutdown != 1 and shutdown != 0:
            raise OnepIllegalArgumentException('shutdown', 'invalid')
        try:
            self._api_client.NetworkInterface_setInterfaceShutdownIDL(self.xos_handle, shutdown)
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as t:
            raise OnepConnectionException(t.message, t)
        self._log.info('Interface %s admin status set to %s', self.name, shutdown)



    @deprecated()
    def clear_statistics(self):
        """ Clears statistics for the given Interface.
        
        @raise OnepRemoteProcedureException: System failure to serve the request, please check error
                message for more details.
        @raise OnepConnectionException : Transport error, may need to reset the connection, please 
                check the error message for more details.
        @deprecated: Deprecated with SDK release 1.2.1
        """
        try:
            self._stats_list = self.get_statistics().stats_list
            self._api_client.NetworkInterface_clearStatisticsIDL(self.xos_handle)
            self._log.info('Returned from idl call to clear Interface Statistics')
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as t:
            raise OnepConnectionException(t.message, t)



    def set_load_interval(self, interval):
        """ Sets load interval value on the interface.
        
        This method is used to change the length of time for which data is used to compute 
        load statistics. Use this method to modify the value of load-interval interface configuration.
        
        The load-interval is default set to 300 (5 min). The number is approximation 
        of rate per second. The value is a multiple of 30, from 30 to 600 (30, 60, 90, 120, 
        and so forth). If a value of zero is specified then, the value is set to default value.
        
        The load-interval value is used for measurements of load averages of tx_rate_pps, 
        tx_rate_bps,rx_rate_pps and rx_rate_bps.
         
        
        @param interval: Interval Value of load-interval to be set. 
        @type interval: C{int}
        @raise OnepRemoteProcedureException: System failure to serve the request, please check error
                message for more details.
        @raise OnepConnectionException : Transport error, may need to reset the connection, please 
                check the error message for more details.     
        @raise OnepIllegalArgumentException : This exception is thrown if input parameter is not specified or if 
                it is not of type integer.
        """
        validate_none(interval, 'Interval')
        validate(interval, int)
        try:
            self._api_client.NetworkInterface_setLoadIntervalIDL(self.xos_handle, interval)
            self._log.info('Returned from idl call to set Interface Load Interval to %d', interval)
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as t:
            raise OnepConnectionException(t.message, t)



    def get_location(self):
        """
        Gets a Location object associated with the network interface. The Location
        object can be used to access all types of location information.
        
        @return: The Location object for the network interface, or None if there is
                no location information available.
        
        @raise OnepConnectionException:
                    The exception is thrown when the connection to a network element
                    has failed.
        @raise OnepRemoteProcedureException:
                    The exception is thrown when an error has occurred in the
                    remote procedure call made to a network element.
        """
        from onep.location import location
        if self.network_element and (self.network_element.session_handle == None or self.network_element.session_handle._id == 0):
            raise OnepConnectionException('Session is disconnected')
        locIdl = None
        try:
            locIdl = self.network_element.location_client.Location_getLocationIDL(location.LocationHandleType.LocInterfaceHandle, self._xos_handle)
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e.message, e)
        if locIdl != None:
            loc = location.fromIDL(locIdl)
            loc._set_element_interface_attachment(self)
            return loc
        else:
            return 



    def set_location(self, loc):
        """
        Sets location information for the network interface.
        
        Sets location information for the network interface with the information in
        the input Location parameter.
        
        @param loc: The location information to be associated with the network
                   interface.
        @type loc: L{Location<onep.location.location.Location>}
                   
        @raise OnepIllegalArgumentException:
                    The exception is thrown if the location object is invalid.
        @raise OnepConnectionException:
                    The exception is thrown when the connection to a network element
                    has failed.
        @raise OnepRemoteProcedureException:
                    The exception is thrown when an error has occurred in the
                    remote procedure call made to a network element.
        """
        from onep.location import location
        if loc == None:
            raise OnepIllegalArgumentException('loc', 'None')
        if not self.network_element or self.network_element.session_handle == None or self.network_element.session_handle._id == 0:
            raise OnepConnectionException('Session is disconnected')
        try:
            self.network_element.location_client.Location_setLocationIDL(location.LocationHandleType.LocInterfaceHandle, self._xos_handle, loc.toIDL())
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e.message, e)



    @classmethod
    def _af_check(cls, inet_addr):
        try:
            socket.inet_pton(socket.AF_INET, inet_addr)
            return 1
        except socket.error:
            try:
                socket.inet_pton(socket.AF_INET6, inet_addr)
                return 2
            except socket.error:
                raise OnepIllegalArgumentException('Address passed ', 'invalid')



    @classmethod
    def _convert_to_networkaddressidl(cls, inet_addr):
        if inet_addr == None:
            inet_addr = ''
        byte_array = array('B', inet_addr)
        byte_array.append(0)
        if inet_addr == '':
            family = 0
        else:
            family = cls._af_check(inet_addr)
        na_idl = NetworkAddressIDL(family, byte_array)
        return na_idl



    def set_address(self, set, scope, addr, prefix_len):
        """ Sets or Unset IP address on the interface.
          
          This API can be used to set either an IPv4 or IPv6 address on the Interface. 
          The API also allows one to specify the scope of the address being configured.  
        
          Following operations can be done with the API.
              1. Set IPv4 primary address (only one allowed on an interface). 
                   set_address(1, OnepAddressScopeType.ONEP_ADDRESS_IPv4_PRIMARY, addr, prefix).
              2. Set IPv4 secondary address (multiple allowed on an interface). 
                   set_address(1, OnepAddressScopeType.ONEP_ADDRESS_IPv4_SECONDARY, addr, prefix). 
              3. Unset IPv4 primary address (the correct address must be specified).
                   set_address(0, OnepAddressScopeType.ONEP_ADDRESS_IPv4_PRIMARY, addr, prefix). 
              4. Unset IPv4 secondary address (the correct address must be specified).
                   set_address(0, OnepAddressScopeType.ONEP_ADDRESS_IPv4_SECONDARY, addr, prefix). 
              5. Unset IPv4 addresses (both primary and secondary).
                   set_address(0, OnepAddressScopeType.ONEP_ADDRESS_IPv4_ALL, None, 0). 
              6. Set IPv6 link-local address (only one allowed on an interface).
                   set_address(1, OnepAddressScopeType.ONEP_ADDRESS_IPv6_LINK_LOCAL, addr, prefix).
              7. Set IPv6 address in EUI-64 format (multiple allowed on an interface).
                   set_address(1, OnepAddressScopeType.ONEP_ADDRESS_IPv6_EUI64, addr, prefix).
              8. Set IPv6 uni-cast or site-local address (multiple allowed on an interface). 
                   set_address(1, OnepAddressScopeType.ONEP_ADDRESS_IPv6_GLOBAL, addr, prefix).
              9. Unset IPv6 link-local address (set default link-local). 
                   set_address(0, OnepAddressScopeType.ONEP_ADDRESS_IPv6_LINK_LOCAL, addr, 0). 
              10. Unset IPv6 address of EUI-64 format.
                   set_address(0, OnepAddressScopeType.ONEP_ADDRESS_IPv6_EUI64, addr, prefix).
              11. Unset IPv6 uni-cast or site-local address .
                   set_address(0, OnepAddressScopeType.ONEP_ADDRESS_IPv6_GLOBAL, addr, prefix).
              12. Unset all IPv6 addresses. 
                   set_address(0, ONEP_ADDRESS_IPv6_ALL, None, 0).
          
          @param set: Integer value indicating if it is a set/unset operation.
                  1 to set the address adn 0 to unset the address
          @type set: C{int}
          @param scope: Indicates the scope of the address.
          @type scope: L{OnepAddressScopeType<core.util.OnepConstants.OnepConstants.OnepAddressScopeType>}
          @param addr: The IP address to be set on the interface. This argument is ignored 
                  for unset operation for scope types ONEP_ADDRESS_V4_ALL, ONEP_ADDRESS_V6_ALL,
                  and ONEP_ADDRESS_V4_PRIMARY.
          @type addr: C{str}
          @param prefix_len: Value of prefix length (representing the mask) for the set/unset 
                  IP address operation. This argument is ignored for unset operation for 
                  scope types ONEP_ADDRESS_V4_ALL, ONEP_ADDRESS_V6_ALL and ONEP_ADDRESS_V4_PRIMARY.
          @type prefix_len: C{int} 
          @raise OnepRemoteProcedureException: System failure to serve the request, please check error
                  message for more details.
          @raise OnepConnectionException : Transport error, may need to reset the connection, please 
                  check the error message for more details.     
          @raise OnepIllegalArgumentException : This exception is thrown if input parameter is not specified or if 
                  it is not of correct type.
          """
        validate_none(scope, 'Scope')
        validate_none(set, 'Set')
        validate_none(prefix_len, 'PrefixLen')
        validate(prefix_len, int)
        if set != 1 and set != 0:
            raise OnepIllegalArgumentException('set', 'invalid')
        self._log.info('Basic Validation of set,scope and prefix_len parameters completed.')
        if set == 1:
            validate_none(addr, 'Addr')
            if scope == OnepConstants.OnepAddressScopeType.ONEP_ADDRESS_IPv4_ALL or scope == OnepConstants.OnepAddressScopeType.ONEP_ADDRESS_IPv6_ALL:
                self._log.info('Scope value is set to %s while setting address which is invalid', OnepConstants.OnepAddressScopeType.enumval(scope))
                raise OnepIllegalArgumentException('scope', 'invalid')
        elif addr == None:
            if scope == OnepConstants.OnepAddressScopeType.ONEP_ADDRESS_IPv4_SECONDARY or scope == OnepConstants.OnepAddressScopeType.ONEP_ADDRESS_IPv4_PRIMARY or scope == OnepConstants.OnepAddressScopeType.ONEP_ADDRESS_IPv6_EUI64 or scope == OnepConstants.OnepAddressScopeType.ONEP_ADDRESS_IPv6_GLOBAL or scope == OnepConstants.OnepAddressScopeType.ONEP_ADDRESS_IPv6_LINK_LOCAL:
                self._log.info('Address is None but scope value is set which is invalid')
                raise OnepIllegalArgumentException('scope', 'invalid. Address set for ' + OnepConstants.OnepAddressScopeType.enumval(scope))
        if set == 0 and scope == OnepConstants.OnepAddressScopeType.ONEP_ADDRESS_IPv4_ALL or scope == OnepConstants.OnepAddressScopeType.ONEP_ADDRESS_IPv6_ALL:
            addr_idl = self._convert_to_networkaddressidl(None)
        else:
            addr_idl = self._convert_to_networkaddressidl(addr)
        self._log.info('NetworkAddressIDL created successfully')
        try:
            self._api_client.NetworkInterface_setAddressIDL(self.xos_handle, set, scope, addr_idl, prefix_len)
            self._log.info('Returned from idl call to set Interface Address')
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as t:
            raise OnepConnectionException(t.message, t)



    def set_iphelper(self, ipaddress, vrf = None, set = True):
        """     
                Enable UDP forwarding to specified address 
        
                Throws on error
                    OnepIllegalArgumentException - Invalid IP address 
        
                Keyword arguments
                ipaddress -- string  - IP address of host for forwarding operation
                vrf       -- Vrf class - Virtual Route Forwarding
                set       -- boolean - True = set forwarding, False = stop forwarding
        
                """
        if not HostIpCheck(ipaddress).is_ipaddress():
            self._log.error('Invalid IP address %s', ipaddress)
            raise OnepIllegalArgumentException('Invalid IP address %s' % ipaddress)
        if vrf:
            try:
                from onep.routing.vrf import Vrf
                validate(vrf, Vrf)
                if not vrf.name:
                    vrf.name = ''
                vrf = vrf.name
            except:
                vrf = ''
        else:
            vrf = ''
        if set:
            self._log.info('Enable %s UDP forwarding to %s', self._name, ipaddress)
            try:
                self._api_client.NetworkInterface_setIpHelperIDL(self.xos_handle, self._convert_to_networkaddressidl(ipaddress), vrf, True)
            except ExceptionIDL as e:
                raise OnepException('set_iphelper', e)
        else:
            self._log.info('Disable %s UDP forwarding to %s', self._name, ipaddress)
            try:
                self._api_client.NetworkInterface_setIpHelperIDL(self.xos_handle, self._convert_to_networkaddressidl(ipaddress), vrf, False)
            except ExceptionIDL as e:
                raise OnepException('set_iphelper', e)



    def set_proxy_arp(self, set):
        """     
                Turn on/off ARP proxy
        
                Keyword argument
                set -- boolean - True = turn on ARP proxy, False = turn off ARP proxy
        
                """
        try:
            self._api_client.NetworkInterface_setIpProxyArpIDL(self.xos_handle, int(set))
        except ExceptionIDL as e:
            raise OnepException('set_proxy_arp', e)



    def set_ip_unreachable(self, set):
        """     
                Turn on/off IP unreachable
        
                Keyword argument
                set -- boolean - True = turn on IP unreachable, False = turn off IP unreachable
        
                """
        try:
            self._api_client.NetworkInterface_setIpUnreachableIDL(self.xos_handle, int(set))
        except ExceptionIDL as e:
            raise OnepException('set_ip_unreachable', e)



    def set_ip_redirect(self, set):
        """     
                Turn on/off IP redirect
        
                Keyword argument
                set -- boolean - True = turn on IP redirect, False = turn off IP redirect
        
                """
        try:
            self._api_client.NetworkInterface_setIpRedirectIDL(self.xos_handle, int(set))
        except ExceptionIDL as e:
            raise OnepException('set_ip_redirect', e)



    def set_ip_unicast_reverse_path(self, set, access_list = None):
        """     
                Turn on/off IP Unicast Reverse Path
        
                Keyword arguments
                set -- boolean - True = turn on IP reverse path, False = turn off IP reverse path
                access_list -- string - name of access list for reverse path
        
                """
        try:
            if access_list is None:
                access_list = ''
            self._api_client.NetworkInterface_setIpUnicastReversePathIDL(self.xos_handle, access_list, int(set))
        except ExceptionIDL as e:
            raise OnepException('set_ip_unicast_reverse_path', e)



    def set_vrf_forwarding(self, vrf, set = True):
        self._chk_vty()
        try:
            from onep.routing.vrf import Vrf
        except:
            return 
        if not isinstance(vrf, Vrf):
            raise OnepIllegalArgumentException('Must pass in Vrf class')
        if set:
            self._log.info('Enable %s vrf forwarding to %s', self._name, vrf.name)
            cli = 'interface %s\nvrf forwarding %s' % (self._name, vrf.name)
            self._vty.config(cli)
        else:
            self._log.info('Disable %s vrf forwarding to %s', self._name, vrf.name)
            cli = 'interface %s\nno vrf forwarding %s' % (self._name, vrf.name)
            self._vty.config(cli)



    def get_address_list(self):
        """ Gets a list of IP addresses (IPv4 or IPv6) associated with this
           
              @rtype: C{list}
              @return: A list of ip addresses as strings.
        
              @raise OnepRemoteProcedureException: System failure to serve the request, please check error
                      message for more details.
              @raise OnepConnectionException : Transport error, may need to reset the connection, please 
                      check the error message for more details.     
              """
        addr_list = []
        try:
            na_list = self._api_client.NetworkInterface_getAddressListIDL(self.xos_handle)
            self._log.info('Returned from idl call to retrieve Interface Address List')
            if na_list != None:
                for na in na_list:
                    inet_addr = self._convert_to_inetaddress(na)
                    if inet_addr != None:
                        inet_addr = inet_addr.strip('\x00')
                        addr_list.append(inet_addr)

        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as t:
            raise OnepConnectionException(t.message, t)
        return addr_list



    @classmethod
    def _convert_to_inetaddress(cls, na_idl):
        arr = na_idl.addr
        inet_addr = ''
        for l in arr:
            if l == 0:
                break
            inet_addr += str(chr(l))

        return inet_addr



    def get_prefix_list(self):
        """ Gets a list of IP prefixes (IPv4 or IPv6 address and its mask) 
              associated with this Interface. 
           
              The Interfaces IP prefixes are returned as list of NetworkPrefix objects.
              The NetworkPrefix object contains the InetAddress object representing the IPv4 or IPv6 
              address and an integer for the prefix length.
        
              @rtype: C{list}
              @return: A list of NetworkPrefix objects.
              
              @raise OnepRemoteProcedureException: System failure to serve the request, please check error
                      message for more details.
              @raise OnepConnectionException : Transport error, may need to reset the connection, please 
                      check the error message for more details.     
              """
        prefix_list = []
        try:
            npiList = self._api_client.NetworkInterface_getPrefixListIDL(self.xos_handle)
            self._log.info('Returned from idl call to get Interface Prefix List')
            if npiList != None:
                for npIdl in npiList:
                    inet_addr = self._convert_to_inetaddress(npIdl.addr)
                    len = npIdl.prefix_len
                    if inet_addr != None:
                        inet_addr = inet_addr.strip('\x00')
                        np = NetworkPrefix(inet_addr, len)
                        prefix_list.append(np)

        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as t:
            raise OnepConnectionException(t.message, t)
        return prefix_list



    def get_sub_interface_by_id(self, sub_if_id):
        """
                Return a NetworkInterface class representing the sub-interface object matching the ID
        
                @param sub_if_id: sub-interface ID
                @type sub_if_id: L{InterfaceTypes<onep.interfaces.NetworkInterface.InterfaceTypes>}
        
                @rtype: L{NetworkInterface<onep.interfaces.NetworkInterface>}
                @return NetworkInterface class
        
                """
        try:
            if not isinstance(sub_if_id, int) or sub_if_id < 0:
                raise OnepIllegalArgumentException('Invalid sub-interface ID')
            subidl = self._api_client.NetworkInterface_getSubInterfaceByIdIDL(self.xos_handle, self._interface_type, sub_if_id)
            return NetworkInterface(self.network_element, subidl.name, subidl.type, subidl.xosHandle)
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as t:
            raise OnepConnectionException(t.message, t)



    def add_state_listener(self, interface_state_listener, state_event_type, client_data):
        """ Adds a Interface up/down state listener to NetworkElement Object.
        
        @param interface_state_listener: Instance of InterfaceStateListener class.
        @type interface_state_listener: L{InterfaceStateListener<interfaces.InterfaceStateListener.InterfaceStateListener>}
        @param state_event_type: Specify what type of event is of interest.
        @type state_event_type:  L{InterfaceStateEvent<interfaces.InterfaceStatus.InterfaceStatus.InterfaceStateEventType>}.
        @param client_data: The client data associated with the listener. This client data 
              will be part of input parameters when the handleEvent method  in the 
              listener is invoked.
         
        @rtype: C{int} 
        @return: event_handle, Numeric ID associated with this event registration. The event_handle 
             is used to unregister the listener using the remove_state_listener method.
        
        @raise OnepRemoteProcedureException: System failure to serve the request, please check error
                message for more details.
        @raise OnepConnectionException : Transport error, may need to reset the connection, please 
                check the error message for more details.     
        @raise OnepIllegalArgumentException : This exception is thrown if input parameter is not specified or if 
                it is not of correct type.
        """
        validate_none(interface_state_listener, 'interface_state_listener')
        validate_none(state_event_type, 'state_event_type')
        validate(interface_state_listener, InterfaceStateListener)
        self._log.info('Basic validation of input parameters is complete')
        if state_event_type < 0 or state_event_type > 2:
            raise OnepIllegalArgumentException('state_event_type', 'Invalid value')
        from onep.interfaces.InterfaceFilter import InterfaceFilter
        filter = InterfaceFilter(self, self.interface_type)
        event_prop = None
        try:
            interface_type = filter.interface_type
            event_prop = self._api_client.InterfaceStateEvent_registerIDL(self.network_element.session_handle._id, filter.interface.xos_handle, interface_type, state_event_type, 0, 0)
            self._log.info('Returned from idl call to Register the Interface State Listener for %s interface', self.name)
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as t:
            raise OnepConnectionException(t.message, t)
        if event_prop != None:
            self.network_element.event_manager.add_listener(event_prop.eventHandle, interface_state_listener, client_data)
            self._log.info('Added Interface State Listener to event Manager')
        return event_prop.eventHandle



    def remove_state_listener(self, event_handle):
        """ Remove Interface up/down state listener from NetworkElement Object.
        
        @param event_handle: Numeric ID which was returned when listener was added to detect the event.
        @type event_handle: C{int}  
        @raise OnepRemoteProcedureException: System failure to serve the request, please check error
                message for more details.
        @raise OnepConnectionException : Transport error, may need to reset the connection, please 
                check the error message for more details.     
        @raise OnepIllegalArgumentException : This exception is thrown if input parameter is not specified or if 
                it is not of type C{int}.
        """
        if event_handle == None:
            raise OnepIllegalArgumentException('event_handle', 'None')
        self.network_element.event_manager.remove_listener(event_handle)
        self._log.info('Removed listener for Interface State events for %s interface', self.name)



    def add_statistics_listener(self, interface_statistics_listener, filter, client_data):
        """  Subscribes to Interface statistics change events.
        
        @param interface_statistics_listener: Instance of InterfaceStatisticsListener class.
        @type interface_statistics_listener:  L{InterfaceStatisticsListener<interfaces.InterfaceStatisticsListener.InterfaceStatisticsListener>}
        @param filter: Specify criteria of interesting interface statistics events. 
        @type filter: L{InterfaceStatisticsFilter<interfaces.InterfaceStatisticsFilter.InterfaceStatisticsFilter>}
        @param client_data: The client data associated with the listener. This client data 
               will be part of input parameters when the handleEvent method  in the 
               listener is invoked.
          
        @rtype: C{int}
        @return: event_handle, Numeric ID associated with this event registration. The event_handle 
              is used to unregister the listener using the remove_statistics_listener method.
         
        @raise OnepRemoteProcedureException: System failure to serve the request, please check error
                message for more details.
        @raise OnepConnectionException : Transport error, may need to reset the connection, please 
                check the error message for more details.     
        @raise OnepIllegalArgumentException : This exception is thrown if input parameter is not specified or if 
                it is not of correct type.
        """
        validate_none(interface_statistics_listener, 'interface_statistics_listener')
        validate_none(filter, 'filter')
        validate(interface_statistics_listener, InterfaceStatisticsListener)
        self._log.info('Basic validation of input parameters is complete')
        if filter.exit_combination == OnepConstants.OnepCombinationType.ONEP_COMBINATION_AND and (filter.exit_op == OnepConstants.OnepOperatorType.ONEP_OP_NONE or not filter.exit_value or filter.exit_time.sec == 0 and filter.exit_time.msec == 0):
            self._log.info('When exit_combination is set to  ONEP_COMBINATION_AND then exit_op,exit_value and exit_time must be set as well ')
            raise OnepIllegalArgumentException('filter', 'When exit_combination is ONEP_COMBINATION_AND , ' + 'exit_op, exit_value and exit_time must exist')
        if filter.exit_combination == OnepConstants.OnepCombinationType.ONEP_COMBINATION_OR and (filter.exit_op == OnepConstants.OnepOperatorType.ONEP_OP_NONE or not filter.is_exit_value_set) and filter.exit_time.sec == 0 and filter.exit_time.msec == 0:
            self._log.info('When exit_combination is set to ONEP_COMBINATION_OR then (exit_op and exit_value) or exit_time must be set as well ')
            raise OnepIllegalArgumentException('filter', 'When exit_combination is OR, ' + '(exit_op and exit_value) or exit_time must exist')
        if filter.average_factor > 0 and filter.entry_type != InterfaceStatisticsFilter.InterfaceStatisticsType.ONEP_INTERFACE_STATISTICS_TYPE_RATE:
            self._log.info('When average_factor is set then entry_type must be set to ONEP_INTERFACE_STATISTICS_TYPE_RATE')
            raise OnepIllegalArgumentException('filter', 'When average_factor is specified, ' + 'entry_type must be ONEP_INTERFACE_STATISTICS_TYPE_RATE')
        if filter.average_factor > 0 and filter.is_exit_value_set and filter.exit_type != InterfaceStatisticsFilter.InterfaceStatisticsType.ONEP_INTERFACE_STATISTICS_TYPE_RATE:
            self._log.info('When average_factor is set and exit_value is also set then exit_type must be set to ONEP_INTERFACE_STATISTICS_TYPE_RATE')
            raise OnepIllegalArgumentException('filter', 'When average_factor is specified and exit_value is set then, ' + 'exit_type must be ONEP_INTERFACE_STATISTICS_TYPE_RATE ')
        event_prop = None
        try:
            if filter.is_exit_value_set:
                is_exit_value_set = True
            else:
                is_exit_value_set = False
            if filter.exit_event:
                exit_event = True
            else:
                exit_event = False
            event_prop = self._api_client.InterfaceStatisticsEvent_registerIDL(self.network_element.session_handle._id, self.xos_handle, filter.parameter, filter.poll_interval.sec, filter.poll_interval.msec, filter.entry_value, filter.entry_op, filter.entry_type, is_exit_value_set, filter.exit_value, filter.exit_op, filter.exit_type, filter.exit_combination, filter.exit_time.sec, filter.exit_time.msec, exit_event, filter.average_factor, 0, 0)
            self._log.info('Returned from idl call to Register the Interface Statistics Listener for %s interface', self.name)
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e.message, e)
        if event_prop != None:
            self.network_element.event_manager.add_listener(event_prop.eventHandle, interface_statistics_listener, client_data)
        return event_prop.eventHandle



    def remove_statistics_listener(self, event_handle):
        """ Remove Interface statistics change events listeners.
        
        @param event_handle: Numeric ID which was returned when listener was added to detect the event.
        @type event_handle: C{int}
        @raise OnepRemoteProcedureException: System failure to serve the request, please check error
                message for more details.
        @raise OnepConnectionException : Transport error, may need to reset the connection, please 
                check the error message for more details.     
        @raise OnepIllegalArgumentException : This exception is thrown if input parameter is not specified or if 
                it is not of type integer.
        """
        if event_handle == None:
            raise OnepIllegalArgumentException('event_handle', 'None')
        self.network_element.event_manager.remove_listener(event_handle)
        self._log.info('Removed listener for Interface Statistics events for %s interface', self.name)



    def add_cdp_listener(self, cdp_listener, filter, client_data):
        """  Subscribes to CDP events.
        
        @param cdp_listener: Instance of CDPListener class.
        @type cdp_listener: L{CDPListener<cdp.CDPListener.CDPListener>}
        @param filter: Specify criteria of interesting CDP events. 
        @type filter: L{CDPFilter<cdp.CDPFilter.CDPFilter>}
        @param client_data: The client data associated with the listener. This client data 
               will be part of input parameters when the handleEvent method  in the 
               listener is invoked.
          
        @rtype: C{int}
        @return: event_handle, Numeric ID associated with this event registration. The event_handle 
              is used to unregister the listener using the remove_cdp_listener method.
         
        @raise OnepRemoteProcedureException: System failure to serve the request, please check error
                message for more details.
        @raise OnepConnectionException : Transport error, may need to reset the connection, please 
                check the error message for more details.     
        @raise OnepIllegalArgumentException : This exception is thrown if input parameter is not specified or if 
                it is not of correct type.
        """
        validate_none(cdp_listener, 'cdp_listener')
        validate_none(filter, 'filter')
        validate(cdp_listener, CDPListener)
        self._log.info('Basic validation of input parameters is complete')
        event_prop = None
        if_filter_idl = InterfaceFilterIDL(self.interface_type, self.xos_handle)
        self._log.info('InterfaceFilterIDL created for this interface')
        if self.cdp_client == None:
            self._log.info('cdp_client created for this interface')
            self.cdp_client = CdpIDL.Client(self.network_element.api_protocol)
        try:
            event_prop = self.cdp_client.CDPEvent_registerIDL(self.network_element.session_handle._id, filter.notify_type, if_filter_idl)
            self._log.info('Returned from idl call to Register the CDP Event Listener for %s interface', self.name)
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e.message, e)
        if event_prop != None:
            self.network_element.event_manager.add_listener(event_prop.eventHandle, cdp_listener, client_data)
            self._log.info('Registered CDP Listener with event handle')
            return event_prop.eventHandle



    def remove_cdp_listener(self, event_handle):
        """ Remove CDP events listeners.
        
        @param event_handle: Numeric ID which was returned when listener was added to detect the event.
        @type event_handle: C{int}
        @raise OnepRemoteProcedureException: System failure to serve the request, please check error
                message for more details.
        @raise OnepConnectionException : Transport error, may need to reset the connection, please 
                check the error message for more details.     
        @raise OnepIllegalArgumentException : This exception is thrown if input parameter is not specified or if 
                it is not of type integer.
        """
        if event_handle == None:
            raise OnepIllegalArgumentException('event_handle', 'None')
        self.network_element.event_manager.remove_listener(event_handle)
        self._log.info('Removed listener for CDP events for %s interface', self.name)




def _get_section_config(self, section_title):
    self._chk_vty()
    return self._vty.show('run | section %s' % section_title)



def _parse_tunnel_config(self, tunnel_cfg):
    lines = _get_section_config(self, self.name)
    line = [ line for line in lines.splitlines() if line.lstrip().startswith('tunnel source ') ]
    if line:
        tunnel_cfg.source_ip = line[0].split()[2]
    else:
        tunnel_cfg.source_ip = None
    line = [ line for line in lines.splitlines() if line.lstrip().startswith('tunnel destination ') ]
    if line:
        tunnel_cfg.dest_ip = line[0].split()[2]
    else:
        tunnel_cfg.dest_ip = None
    line = [ line for line in lines.splitlines() if line.lstrip().startswith('tunnel mode ipsec ') ]
    if line:
        mode = line[0].split()[3]
        tunnel_cfg.ipsec_mode = mode
    else:
        tunnel_cfg.ipsec_mode = None
    tunnel_cfg.ipsec_profile = None
    tunnel_cfg.ike_profile = None
    line = [ line for line in lines.splitlines() if line.lstrip().startswith('tunnel protection ipsec profile ') ]
    if line:
        tunnel_cfg.ipsec_profile = line[0].split()[4]
        if len(line[0].split()) > 5:
            tunnel_cfg.ike_profile = line[0].split()[6]
    tunnel_cfg.ip_address = None
    line = [ line for line in lines.splitlines() if line.lstrip().startswith('ip address ') ]
    if line:
        tunnel_cfg.ip_address = line[0].lstrip(' ip address ')
    else:
        line = [ line for line in lines.splitlines() if line.lstrip().startswith('ip unnumbered') ]
        if line:
            tunnel_cfg.ip_address = line[0].lstrip('ip unnumbered ')



class TunnelInterface(NetworkInterface):
    """
        Tunnel Interface
    
        """

    IPSEC_MODE_IPV4 = 1
    IPSEC_MODE_IPV6 = 2
    _ipsec_mode = {IPSEC_MODE_IPV4: 'ipv4',
     IPSEC_MODE_IPV6: 'ipv6',
     'ipv4': IPSEC_MODE_IPV4,
     'ipv6': IPSEC_MODE_IPV6}

    def __init__(self, element, name = None, type = None, xoshandle = None, tunnel_id = None):
        """
                Tunnel Interface class constructor.
        
                    Keyword arguments:
                    element   -- NetworkElement class - must be connected to element
                    name      -- string - interface name -              Default: 'Tunnel'
                    type      -- NetworkInterface.Interfacetype -       Default: TUNNEL
                    xoshandle -- int - ID for managing API calls to IOS Default: None
                    tunnel_id -- int - Tunnel interface number          Default: None
        
                """
        if not name and not tunnel_id:
            self._log.error('Must supply name or tunnel ID')
            OnepIllegalAt = rgumentException('Must supply name or tunnel ID')
        if tunnel_id:
            self.tunnel_id = tunnel_id
        else:
            self.tunnel_id = re.findall('\\d+', name)[0]
        if not name:
            name = 'Tunnel' + str(tunnel_id)
        type = NetworkInterface.InterfaceTypes.ONEP_IF_TYPE_TUNNEL
        NetworkInterface.__init__(self, element, name, type, xoshandle)



    def get_config(self):
        self._chk_vty()
        cfg = super(TunnelInterface, self).get_config()
        tunnel_cfg = TunnelInterfaceConfig(cfg.encap, cfg.unidir_mode, cfg.mtu, cfg.rx_bandwidth, cfg.tx_bandwidth, cfg.snmp_index, cfg.islayer2, cfg.display_name, cfg.mac_address, cfg.description, None, None, None, None, cfg.vrf, self.tunnel_id, cfg.speed, cfg.duplex, cfg.duplex_conf, cfg.fwd_class_id, cfg.flow_control, cfg.auto_neg)
        _parse_tunnel_config(self, tunnel_cfg)
        self._log.info('TunnelConfig object created successfully %s\n', tunnel_cfg.__str__())
        return tunnel_cfg



    def remove_tunnel_interface(self):
        self._chk_vty()
        self._vty.no_config('interface %s' % self.name)



    def _get_source_ip(self):
        """ Get tunnel source address 
        """
        lines = _get_section_config(self, self.name)
        line = [ line for line in lines.splitlines() if line.lstrip().startswith('tunnel source ') ]
        if line:
            src_ip = line[0].split()[2]
            if HostIpCheck(src_ip).is_ipaddress():
                return src_ip



    def _set_source_ip(self, src_ip):
        """ Set Tunnel source address
        """
        self._chk_vty()
        if not HostIpCheck(src_ip).is_ipaddress():
            self._log.error('Tunnel source IP %s invalid', str(src_ip))
            raise OnepIllegalArgumentException('Tunnel source IP %s invalid' % str(src_ip))
        self._vty.config('int %s\ntunnel source %s' % (self.name, src_ip))



    def _del_source_ip(self):
        self._chk_vty()
        self._vty.config('int %s\nno tunnel source' % self.name)


    _doc_source_ip = '\n        Tunnel source IP \n\n        '
    tunnel_source_ip = property(_get_source_ip, _set_source_ip, _del_source_ip, _doc_source_ip)

    def _get_source_intf(self):
        """  Get tunnel source interface-name
        """
        lines = _get_section_config(self, self.name)
        line = [ line for line in lines.splitlines() if line.lstrip().startswith('tunnel source ') ]
        if line:
            addr_or_name = line[0].split()[2]
            if not re.match('[1-9]\\d{0, 2}(\\.\\d{1, 3}){3}', addr_or_name):
                return addr_or_name



    def _set_source_intf(self, intf_name):
        """ set the tunnel source to an interface
        """
        self._chk_vty()
        self._vty.config('int %s\ntunnel source %s' % (self.name, intf_name))



    def _del_source_intf(self):
        self._chk_vty()
        self._vty.config('int %s\nno tunnel source' % self.name)


    _doc_source_intf = '\n        Tunnel source interface\n        '
    tunnel_source_intf = property(_get_source_intf, _set_source_intf, _del_source_intf, _doc_source_intf)

    def _get_dest_ip(self):
        lines = _get_section_config(self, self.name)
        line = [ line for line in lines.splitlines() if line.lstrip().startswith('tunnel destination ') ]
        if line:
            return line[0].split()[2]
        else:
            return None



    def _set_dest_ip(self, dest_ip):
        self._chk_vty()
        if not HostIpCheck(dest_ip).is_ipaddress():
            self._log.error('Tunnel destination IP %s invalid', str(dest_ip))
            raise OnepIllegalArgumentException('Tunnel destination IP %s invalid' % str(dest_ip))
        self._vty.config('int %s\ntunnel destination %s' % (self.name, dest_ip))



    def _del_dest_ip(self):
        self._chk_vty()
        self._vty.config('int %s\nno tunnel destination' % self.name)


    _doc_dest_ip = '\n        Tunnel destination IP\n\n        '
    tunnel_destination_ip = property(_get_dest_ip, _set_dest_ip, _del_dest_ip, _doc_dest_ip)

    def _get_ipsec_mode(self):
        lines = _get_section_config(self, self.name)
        line = [ line for line in lines.splitlines() if line.lstrip().startswith('tunnel mode ipsec ') ]
        if line:
            return line[0].split()[3]



    def _set_ipsec_mode(self, mode):
        self._chk_vty()
        self._vty.config('int %s\ntunnel mode ipsec %s' % (self.name, self._ipsec_mode[mode]))



    def _del_ipsec_mode(self):
        self._chk_vty()
        self._vty.config('int %s\nno tunnel mode' % self.name)


    _doc_ipsec_mode = '\n        Tunnel IPsec mode\n\n        '
    ipsec_mode = property(_get_ipsec_mode, _set_ipsec_mode, _del_ipsec_mode, _doc_ipsec_mode)

    def _get_ipsec_profile(self):
        """
        It is getting the ipsec profile name
        """
        lines = _get_section_config(self, self.name)
        line = [ line for line in lines.splitlines() if line.lstrip().startswith('tunnel protection ipsec profile ') ]
        if not line:
            return None
        return line[0].split()[4]



    def _set_ipsec_profile(self, profile_name):
        """
        The same line can have ipsec-profile as well as ike profile.
        """
        self._log.info('set_ipsec_profile')
        lines = _get_section_config(self, self.name)
        line = [ line for line in lines.splitlines() if line.lstrip().startswith('tunnel protection ipsec profile') ]
        if not line or len(line[0].split()) == 5:
            cli = 'int %s\n tunnel protection ipsec profile %s' % (self.name, profile_name)
        elif len(line[0].split()) == 7:
            (head, pat, tail,) = line[0].partition(' isakmp-profile ')
            cli = 'int %s\n tunnel protection ipsec profile ' % self.name + profile_name + pat + tail
        self._vty.config(cli)



    def _del_ipsec_profile(self):
        """ remove the association of this tunnel to the ipsec-profile. 
        """
        lines = _get_section_config(self, self.name)
        line = [ line for line in lines.splitlines() if line.lstrip().startswith('tunnel protection ipsec profile') ]
        if line:
            line = line[0]
            if len(line.split()) == 5:
                cli = 'int %s\n' % self.name + 'no ' + line
            else:
                (head, pat, tail,) = line.partition(' isakmp-profile ')
                cli = 'int %s\n' % self.name + 'tunnel protection ipsec profile default isakmp-profile ' + tail
            self._vty.config(cli)


    _doc_ipsec_profile = '\n        ipsec profile name \n\n        '
    ipsec_profile = property(_get_ipsec_profile, _set_ipsec_profile, _del_ipsec_profile, _doc_ipsec_profile)

    def _get_ike_profile(self):
        """ get the ike profile name from tunnel 
        """
        self._log.info('get_ike_profile')
        lines = _get_section_config(self, self.name)
        line = [ line for line in lines.splitlines() if line.lstrip().startswith('tunnel protection ipsec profile') ]
        line = line[0]
        if line and len(line.split()) > 5:
            return line.split()[6]
        else:
            return None



    def _set_ike_profile(self, ike_profile_name):
        """ associate tunnel with this ike_profile
        """
        self._log.info('set_ike_profile')
        lines = _get_section_config(self, self.name)
        line = [ line for line in lines.splitlines() if line.lstrip().startswith('tunnel protection ipsec profile') ]
        if len(line) == 0:
            cli = 'int %s\n' % self.name + 'tunnel protection ipsec profile default isakmp %s' % ike_profile_name
        else:
            line = line[0]
            (line, tmp, old,) = line.partition('isakmp-profile')
            line += ' isakmp-profile  %s ' % ike_profile_name
            cli = 'int %s\n' % self.name + line
        self._vty.config(cli)



    def _del_ike_profile(self):
        """ remove the association of the tunnel and the ike profile
        """
        lines = _get_section_config(self, self.name)
        line = [ line for line in lines.splitlines() if line.lstrip().startswith('tunnel protection ipsec profile ') ]
        if line:
            line = line[0]
            if len(line.split()) > 6:
                (head, tmp, tail,) = line.partition(' isakmp-profile ')
                cli = 'int %s\n' % self.name + head
                self._vty.config(cli)


    _doc_ike_profile = '\n        The ike profile name associate with the tunnel\n        '
    ike_profile = property(_get_ike_profile, _set_ike_profile, _del_ike_profile, _doc_ike_profile)

    def _get_mtu(self):
        self._chk_vty()
        ret = self._vty.show('ip interface %s' % self.name)
        for line in ret.splitlines():
            if line.find('MTU') > -1:
                mtu = line.split()[2]

        if mtu:
            return int(mtu)



    def _set_mtu(self, mtu_size):
        self._chk_vty()
        self._vty.config('int %s\nip mtu %s' % (self.name, mtu_size))



    def _del_mtu(self):
        self._chk_vty()
        self._vty.config('int %s\nno ip mtu' % self.name)


    _doc_mtu = ' \n               MTU attribute \n               '
    mtu = property(_get_mtu, _set_mtu, _del_mtu, _doc_mtu)

    def get_address_list(self):
        """ Gets a list of IP addresses (IPv4 or IPv6) associated with this
           
              @rtype: C{list} 
              @return: A list of ip addresses as strings.
        
              @raise OnepRemoteProcedureException: System failure to serve the request, please check error
                      message for more details.
              @raise OnepConnectionException : Transport error, may need to reset the connection, please  
                      check the error message for more details.     
              """
        addr_list = []
        self._chk_vty()
        ret = self._vty.show('run | section %s' % self.name).splitlines()
        if ret:
            addr_list = [ line.split()[2] for line in ret if line.lstrip().startswith('ip address') ]
        return addr_list



    def _get_ip_address(self):
        """  Get the ip address of the tunnel,
        """
        self._log.info('get_ip_address')
        lines = _get_section_config(self, self.name)
        line = [ line for line in lines.splitlines() if line.lstrip().startswith('ip address ') ]
        if line:
            address_mask = line[0].lstrip(' ip address')
            return address_mask



    def _set_ip_address(self, param):
        """ setting the tunne ip address           
        """
        self._log.info('set_ip_address')
        addr = param['addr']
        prefix_len = param['prefix']
        if param.has_key('scope'):
            scope = param['scope']
        else:
            scope = None
        if not HostIpCheck(addr).is_ipaddress():
            self._log.error('Tunnel IP %s invalid', str(addr))
            raise OnepIllegalArgumentException('Tunnel IP %s invalid' % str(addr))
        if scope is None:
            scope = OnepConstants.OnepAddressScopeType.ONEP_ADDRESS_IPv4_PRIMARY
        if self.name.lower().startswith('tunnel'):
            self.set_address(1, scope, addr, prefix_len)
        else:
            self_address_mask = self.ip_address
            if self_address_mask and self_address_mask.split()[0] == addr:
                return 
            self._chk_vty()
            all_ip_address = self._vty.show('run | include ip address')
            if addr in all_ip_address:
                raise OnepException('Duplicate IP address %s' % addr)
            else:
                cli = 'interface %s\nip address %s %s' % (self.name, addr, HostIpCheck.len2mask(prefix_len))
                self._vty.config(cli)



    def _del_ip_address(self):
        self._chk_vty()
        cli = 'int %s\n' % self.name + 'no ip address'
        self._vty.config(cli)


    _doc_ip_address = '\n        Tunnel ip address, \n        '
    ip_address = property(_get_ip_address, _set_ip_address, _del_ip_address, _doc_ip_address)

    def _get_ip_unnumbered(self):
        """  Get ip unnumber <interface>
        """
        self._log.info('get_ip_unnumbered')
        lines = _get_section_config(self, self.name)
        line = [ line for line in lines.splitlines() if line.lstrip().startswith('ip unnumbered ') ]
        if line:
            return line[0].split()[2]



    def _set_ip_unnumbered(self, name):
        """ config ip unnumbered <interface>
        """
        self._log.info('set_ip_unnumbered')
        cli = 'int %s\n' % self.name + 'ip unnumbered %s' % name
        self._chk_vty()
        self._vty.config(cli)



    def _del_ip_unnumbered(self):
        self._chk_vty()
        cli = 'int %s\n' % self.name + 'no ip unnumbered'
        self._vty.config(cli)


    _doc_ip_unnumbered = '\n        Tunnel ip unnumbered to a local interface\n        '
    ip_unnumbered = property(_get_ip_unnumbered, _set_ip_unnumbered, _del_ip_unnumbered, _doc_ip_unnumbered)


class VtemplateInterface(object):
    """
            Vtemplate is a container, 
            there are many types of vtemplates, 
    
            interface Virtual-Template2 type tunnel ---- tunel
            interface Virtual-Template3  ---------------serial 
         
        """


    def __init__(self, element, name = None):
        if name:
            self.name = name
        self._network_element = element
        self._vty = None



    def _chk_vty(self):
        if not self._vty:
            try:
                self._vty = VtyProxy(self._network_element)
            except NameError:
                from onep.vty.VtyProxy import VtyProxy
                self._vty = VtyProxy(self._network_element)



    def add_vtemplate(self, name, type):
        self._chk_vty()
        ret = self._vty.show('run | include interface %s' % name)
        if ret and name in ret.split():
            raise OnepException('%s interface already configured' % name)
        if type == NetworkInterface.InterfaceTypes.ONEP_IF_TYPE_TUNNEL:
            if name.startswith('Virtual-Template'):
                if 'type tunnel' not in name:
                    name += ' type tunnel'
        self.name = name
        self._vty.config('interface %s' % name)
        self.interface = TunnelInterface(self._network_element, name=self.name)



    def get_all_vtemplates(self, filter):
        list = self._network_element.get_interface_list(filter)
        vtemplates = [ item for item in list if item.name.startswith('Virtual-Template') ]
        return vtemplates




class LoopbackInterface(NetworkInterface):
    pass

class SubInterface(NetworkInterface):
    pass

# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:18:27 IST
