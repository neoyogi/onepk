# 2015.02.05 17:21:08 IST
import os.path
import sys
onep_path = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir))
if onep_path not in sys.path:
    sys.path.insert(0, onep_path)
from thrift.transport import TTransport
from onep.thrift.Thrift import *
from onep.thrift.transport.TTransport import *
from onep.thrift.transport.TSocket import TSocket
from onep.thrift.transport.CiscoTSSLSocket import CiscoTSSLSocket
from onep.thrift.transport.TTIPCSocket import TTIPCSocket
from onep.thrift.protocol.TBinaryProtocol import TBinaryProtocolAccelerated
from onep.core.util.OnepArgumentTypeValidate import validate
try:
    from onep.thrift.protocol import fastbinary
except:
    fastbinary = None
from onep.NetworkElementIDL import *
from onep.Constants.constants import ONEP_VERSION_MAJOR, ONEP_VERSION_MINOR, ONEP_VERSION_MAINTENANCE
from onep.NetworkElementIDL.ttypes import InterfaceCreateDeleteFilterIDL
from onep.NetworkElementIDL.ttypes import VmCredentialIDL
import onep.NetworkInterfaceIDL.NetworkInterfacesIDL
import onep.SystemStatusIDL.SystemStatusIDL
import onep.DiscoveryIDL.DiscoveryIDL
import onep.LocationIDL.LocationIDL
import onep.PolicyIDL.PolicyIDL
from onep.ApplmgmtDataIDL import ApplmgmtDataIDL
from onep.CdpIDL.CdpIDL import Client
from onep.VlanIDL import VlanIDL
from onep.VlanIDL.ttypes import VlanParam_IDL
from Shared.ttypes import ExceptionIDL, InterfaceFilterIDL, OnepVersionIDL
from onep.core.util.OnepConstants import OnepConstants
from onep.core.util.Enum import enum
from onep.core.event.EventManager import EventManager
from onep.core.exception.OnepException import OnepException
from onep.core.exception.OnepRemoteProcedureException import OnepRemoteProcedureException
from onep.core.exception.OnepIllegalArgumentException import OnepIllegalArgumentException
from onep.core.exception.OnepConnectionException import OnepConnectionException
from onep.core.exception.OnepDuplicateElementException import OnepDuplicateElementException
from onep.core.util import Version
from onep.element.SessionConfig import SessionConfig
from onep.element.ElementProperty import ElementProperty
from onep.element.SessionHandle import SessionHandle
from onep.element.NetworkApplication import NetworkApplication
from onep.element.FRU import FRU
from onep.interfaces.NetworkInterface import NetworkInterface
from onep.interfaces.InterfaceConfig import InterfaceConfig
from onep.interfaces.InterfaceStatus import InterfaceStatus
from onep.location import location
import re
try:
    from onep.vty.VtyProxy import VtyProxy
except ImportError:
    pass
import logging
from time import time
try:
    from onep.container.csdata import InterfaceMap
except ImportError:
    pass
from ctypes import c_byte

class OnepInterfaceException(ValueError):
    pass

class OnepVMcredentialException(IOError):
    pass

class NetworkElement(object):
    """
    The NetworkElement class represents the hardware that hosts the network OS.
    
    It provides network services to a oneP application. The class provides 
    access to the network services offered by  network element through a session
    The session is managed by the class. Each application can have one and only
    one session to a network element, however an application may connect to as
    many network elements as it can maintain connections to.
    
    @ivar appname: Name of the oneP application.
    @type appname: C{str}
    
    @ivar host_address: The host IP address.
    @type host_address: C{str}
    
    @ivar state: The current state of the session.
    @type state: L{OnepSessionState<onep.element.NetworkElement.OnepSessionState>}
    
    @ivar username: Username used for the session authentication.
    @type username: C{str}
    
    @ivar password: Password used for the session authentication.
    @type password: C{str}
    
    @ivar session_handle: A numeric ID associated with the session.
    @type session_handle: L{SessionHandle<onep.element.SessionHandle.SessionHandle>}
    
    @ivar connect_time: The time when connection established to the Network Element.
    @type connect_time: C{float}
    
    @ivar disconnect_time: The time when disconnected from the Network Element.
    @type disconnect_time: C{float}
    
    @ivar disconnect_msg: The message sent to Network Element while disconnecting.
    @type disconnect_msg: C{str}
    
    @ivar properties: Provides the static properties of the NetworkElement.
    @type properties: L{ElementProperty<onep.element.ElementProperty.ElementProperty>}
    
    @ivar port: The port to connect to.
    @type port: C{int}
    
    @ivar appl_managed_data: The application managed data.
    
    @ivar interfaces: All the network interfaces in dictionary form.
    @type interfaces: C{dict}
    
    @undocumented: add_vlan_listener
    @undocumented: remove_vlan_listener
    @undocumented: remove_vrf_listener
    @undocumented: get_vlan_list
    @undocumented: publish_connection_event
    @undocumented: connect_
    @undocumented: set_application_config_cli_listener
    @undocumented: set_application_exec_cli_listener
    @undocumented: set_appl_managed_data
    @undocumented: get_application_exec_cli_listener
    @undocumented: get_application_exec_cli_client_data
    @undocumented: get_application_config_cli_listener
    @undocumented: get_application_config_cli_client_data
    @undocumented: get_connect_time
    @undocumented: get_disconnect_time
    @undocumented: get_reconnect_timer
    
    """


    def __init__(self, host_address = '127.0.0.1', appname = 'noname'):
        """
        Constructor of NetworkElement
        
        @param host_address: The host IP address
        @param appname: The application name
        
        """
        NetworkElement.log = logging.getLogger(__name__)
        self.appname = appname
        self.host_address = host_address
        if not self.host_address:
            self.host_address = '127.0.0.1'
        self.state = self.OnepSessionState.ONEP_STATE_DISCONNECTED
        self.username = None
        self.password = None
        self.session_handle = None
        self.connect_time = None
        self.disconnect_time = None
        self.disconnect_msg = ''
        logging.basicConfig()
        self._vty = None
        self._vty_service = None
        self.routing = None
        self._reconnect_waiting = False
        self._conn_event_listener = None
        self._conn_event_listener_data = None
        self._cpu_sampling_interval = 0
        self.api_transport = None
        self.evt_transport = None
        self.api_protocol = None
        self.evt_protocol = None
        self.api_client = None
        self.evt_client = None
        self.intf_client = None
        self.system_client = None
        self.cdp_client = None
        self.discovery_client = None
        self.location_client = None
        self.vlan_client = None
        self.event_manager = None
        self.policy_client = None
        self.applmgmt_client = None
        self.properties = None
        self.port = OnepConstants.ONEP_PORT
        self.appl_managed_data = None
        self.interfaces = None
        self.parent = None
        self.policy_list = {}
        self._l2_acl_list = list()
        self._l3_acl_list = list()
        self.config_listener = None
        self.exec_listener = None
        self.config_client_data = None
        self.exec_client_data = None



    def __enter__(self):
        return self



    @property
    def license(self):
        """ 
                Licensing of Network Element - 
                [PID of the license identifiers : Version ID : Serial number]
        
                """
        if self.properties:
            return str(self.properties.product_id) + ':' + str(self.properties.version_id) + ':' + str(self.properties.SerialNo)



    def __exit__(self, type, val, tb):
        self.disconnect()



    def _get_cpu_sampling_interval(self):
        return self._cpu_sampling_interval



    def _set_cpu_sampling_interval(self, sampling_interval):
        validate(sampling_interval, int)
        if sampling_interval < 0:
            raise OnepIllegalArgumentException('cpu_sampling_interval can not be less then 0')
        self._cpu_sampling_interval = sampling_interval


    cpu_sampling_interval = property(_get_cpu_sampling_interval, _set_cpu_sampling_interval)

    def _chk_vty(self):
        if not self._vty:
            try:
                self._vty = VtyProxy(self)
            except NameError:
                from vty.VtyProxy import VtyProxy
                self._vty = VtyProxy(self)



    def add_logical_interface(self, if_id, type, parent_intf = None):
        """
                Add a logical interface to network element.
                Raises OnepInterfaceException
                           - interface already exists
                           - logical interface type not supported
        
                Keyword argument:
                if_id -- int  - Logical interface number, subintf_id if it is subinterface
                type  -- enum - NetworkInterface.InterfaceTypes
                parent_intf --NetworkInterface--  base interface 
                """
        name = None
        if type == NetworkInterface.InterfaceTypes.ONEP_IF_TYPE_LOOPBACK:
            name = 'Loopback' + str(if_id)
        if type == NetworkInterface.InterfaceTypes.ONEP_IF_TYPE_TUNNEL:
            name = 'Tunnel' + str(if_id)
        if parent_intf:
            name = parent_intf.name + '.' + str(if_id)
        if not name:
            raise OnepInterfaceException('Logical interface type %d not supported' % type)
        self._chk_vty()
        ret = self._vty.show('run | include interface %s' % name)
        if ret and name in ret.split():
            tmp = [ line for line in ret.splitlines() if line.lstrip().startswith('interface %s' % name) ]
            if tmp:
                raise OnepInterfaceException('%s interface already configured' % name)
        self._vty.config('interface %s' % name)



    def remove_logical_interface(self, if_obj):
        """
                Remove a logical interface to network element.
                Raises OnepInterfaceException
                           - Removal of interface type not supported
                           - Interface not configured
        
                Keyword argument:
                if_obj - interface class
        
                """
        (base, dot, subif_id,) = if_obj.name.partition('.')
        is_subinterface = len(subif_id) > 0 and subif_id.isdigit()
        if if_obj._interface_type != NetworkInterface.InterfaceTypes.ONEP_IF_TYPE_LOOPBACK and not is_subinterface and if_obj._interface_type != NetworkInterface.InterfaceTypes.ONEP_IF_TYPE_TUNNEL:
            raise OnepInterfaceException('Interface type %d cannot be removed' % if_obj._interface_type)
        self._chk_vty()
        ret = self._vty.show('run | include interface %s' % if_obj.name)
        if ret and if_obj.name not in ret.split():
            raise OnepInterfaceException('Interface %s not configured on element' % if_obj.name)
        self._vty.config('no interface %s' % if_obj.name)



    def is_connected(self):
        """
        Returns true if a connected session exists between the network element
        and the application.
        
        """
        if self.state == self.OnepSessionState.ONEP_STATE_CONNECTED:
            return True
        else:
            return False



    def publish_connection_event(self, msg):
        """  
            For internal use only 
        
            """
        if self._conn_event_listener:
            self.log.debug('Sending out %s notification' % self.OnepSessionState.enumval(self.state))
            from onep.element.ConnectionEvent import ConnectionEvent
            event = ConnectionEvent(self, self.state)
            self._conn_event_listener.handle_event(event, self._conn_event_data)



    def set_connection_listener(self, listener, clientData = None):
        """
        Sets a connection listener.
        
        Registers a connection state change listener callback for the
        connect/disconnect state change event.
        
        @param listener: The listener to be registered for connection, that is,
        the listener that will be invoked when the event is triggered.
        To deregister, the listener passes None listener. 
        Any setting of the connection listener overrides the previous setting.
        @param clientData: The client data associated with the listener.
        This client data is part of the input parameters when the handleEvent
        method in the listener is invoked.
        
        """
        self.log.debug('Adding connection event listener')
        self._conn_event_listener = listener
        self._conn_event_data = clientData



    def add_interface_state_listener(self, interfaceStateListener, ifFilter, stateEventType, clientData):
        """
        Adds an Interface up/down state listener to the NetworkElement object.
        
        @raise OnepIllegalArgumentException:
        The eventHandle is used to unregister the listener using the
        remove_interface_state_listener method.
        @raise OnepConnectionException:
        If the interfaceStateListener/ifFilter is None.
        @raise OnepRemoteProcedureException:
        The exception is thrown when an error has occurred in the
        remote procedure call made to a network element.
        @raise OnepException:
        The exception is thrown when an internal error occurs.
        
        @param interfaceStateListener: Class that implements the event handler.
        @param ifFilter: InterfaceFilter class to specify match criteria for interfaces to monitor.
        @param stateEventType: InterfaceStatus.InterfaceStateEventType class to specify the type of event that is interesting--up/down/both.
        @param clientData: The client data associated with the listener. This client data
        is part of the input parameters used when the handleEvent method
        in the listener is invoked.
        
        @return: The eventHandle
        
        """
        if interfaceStateListener == None:
            raise OnepIllegalArgumentException('interfaceStateListener', 'None')
        if ifFilter == None:
            raise OnepIllegalArgumentException('ifFilter', 'None')
        xosHandle = NetworkInterface.ONEP_IF_ALL_HANDLES
        type_ = NetworkInterface.InterfaceTypes.ONEP_IF_TYPE_ANY
        if None != ifFilter.interface:
            xosHandle = ifFilter.interface.xos_handle
            type_ = ifFilter.interface_type
        else:
            type_ = ifFilter.interface_type
        eventProp = None
        try:
            eventProp = self.intf_client.InterfaceStateEvent_registerIDL(self.session_handle._id, xosHandle, type_, stateEventType, 0, 0)
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e.message, e)
        if eventProp != None:
            self.event_manager.add_listener(eventProp.eventHandle, interfaceStateListener, clientData)
            self.log.debug('Registered Interface Statistics listener with event handle : ' + str(eventProp.eventHandle))
        else:
            raise OnepException('Internal error while registering the Listener')
        return eventProp.eventHandle



    def remove_interface_state_listener(self, eventHandle):
        """
        Removes the interface event listener.
        
        This method removes the listener associated with the specified
        eventHandle and also removes the corresponding registered event on the
        NetworkElement.
        
        @raise OnepIllegalArgumentException:
        The exception is thrown when the eventHandle is not valid or
        unregistered already.
        @raise OnepConnectionException:
        The exception is thrown when the connection to a network element
        has failed.
        @raise OnepRemoteProcedureException:
        The exception is thrown when an error has occurred in the
        remote procedure call made to a network element.
        @raise OnepException:
        The exception is thrown when an internal error occurs.
        
        @param eventHandle: Registered event identifier.
        
        """
        self.event_manager.remove_listener(eventHandle)



    def add_syslog_listener(self, syslogListener, syslogFilter, clientData):
        """
        Adds a syslog listener to the NetworkElement object.
        
        Multiple listeners can be associated with an instance of NetworkElement.
        
        @raise OnepIllegalArgumentException:
        The exception is thrown when syslogListener or filter is not
        valid
        @raise OnepConnectionException:
        The exception is thrown when the connection to a network element
        has failed.
        @raise OnepRemoteProcedureException:
        The exception is thrown when an error has occurred in the
        remote procedure call made to a network element.
        @raise OnepException:
        The exception is thrown when an internal error occurs.
        
        @param syslogListener: The SyslogListener object that handles the events.
        @param syslogFilter: The SyslogFilter to specify criteria of interested syslog
        events.
        @param clientData: The client data associated with the listener. This client data
        is part of the input parameters when the handleEvent method
        in the listener is invoked.
        
        @return: EventHandle, a numeric ID associated with this event
        registration. The eventHandle is used to unregister the listener
        using the removeSyslogListener method. If registration fails, -1
        is returned.
        
        """
        self.log.debug('Registering for Syslog events')
        if self.session_handle == None or self.session_handle._id == 0:
            raise OnepConnectionException('Session is disconnected')
        if syslogListener == None:
            raise OnepIllegalArgumentException('syslogListener', 'None')
        if syslogFilter == None:
            raise OnepIllegalArgumentException('syslogFilter', 'None')
        if syslogFilter.occurs < 1 or syslogFilter.occurs > OnepConstants.EVENT_MAX_OCCURS:
            raise OnepIllegalArgumentException('syslogFilter occurs', 'not within range (1 to ' + OnepConstants.EVENT_MAX_OCCURS + ' )')
        if syslogFilter.priority < OnepConstants.EVENT_MIN_PRIORITY or syslogFilter.priority > OnepConstants.EVENT_MAX_PRIORITY:
            raise OnepIllegalArgumentException('syslogFilter priority', 'out of range')
        if syslogFilter.periodMsec < 0:
            raise OnepIllegalArgumentException('syslogFilter period', 'out of range')
        if self.session_handle == None or self.session_handle._id == 0:
            raise OnepConnectionException('Session is disconnected')
        eventProp = None
        try:
            eventProp = self.api_client.SyslogEvent_registerIDL(self.session_handle._id, syslogFilter.pattern, syslogFilter.occurs, syslogFilter.priority, int(syslogFilter.periodMsec / 1000), int(syslogFilter.periodMsec % 1000), 0, 0)
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        try:
            if eventProp != None:
                self.event_manager.add_listener(eventProp.eventHandle, syslogListener, clientData)
                self.log.debug('Registered Syslog listener with event handle : ' + str(eventProp.eventHandle))
                return eventProp.eventHandle
            raise OnepException('Internal error while registering the Listener')
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e.message, e)



    def remove_syslog_listener(self, eventHandle):
        """
        Removes the Syslog event listener
        
        This method removes the listener associated with the specified
        eventHandle and also removes the corresponding registered event on the
        NetworkElement
        
        @raise OnepIllegalArgumentException:
        The exception is thrown when eventHandle is not valid or is
        unregistered already.
        @raise OnepConnectionException:
        The exception is thrown when the connection to a network element
        has failed.
        @raise OnepRemoteProcedureException:
        The exception is thrown when an error has occurred in the
        remote procedure call made to a network element.
        @raise OnepException:
        The exception is thrown when an internal error occurs.
        
        @param eventHandle: Registered event identifier
        
        """
        self.event_manager.remove_listener(eventHandle)



    def add_oir_listener(self, OIRListener, OIRFilter, clientData):
        """
        Adds an Online Insertion and Removal(OIR) listener
        
        Multiple listeners can be associated with an instance of NetworkElement.
        
        @raise OnepIllegalArgumentException:
        The exception is thrown when OIRListener or filter is not valid.
        @raise OnepConnectionException:
        The exception is thrown when the connection to a network element
        has failed.
        @raise OnepRemoteProcedureException:
        The exception is thrown when an error has occurred in the
        remote procedure call made to a network element.
        @raise OnepException:
        The exception is thrown when an internal error occurs.
        
        @param OIRListener: The OIRListener object that handles the events.
        @param OIRFilter: The OIRFilter to specify criteria of interested OIR events.
        @param clientData: The client data associated with the listener. This client data
        is part of the input parameters used when the handleEvent method
        in the listener is invoked.
        @param syslogListener: The SyslogListener object that handles the events.
        @param syslogFilter: The SyslogFilter to specify criteria of interested syslog
        events.
        @param clientData: The client data associated with the listener. This client data
        is part of the input parameters when the handleEvent method
        in the listener is invoked.
        
        @return: EventHandle, a numeric ID associated with this event registration.
        The eventHandle is used to unregister the listener using the 
        removeOIRListener method. If registration fails, -1 is returned.
        
        """
        self.log.debug('Registering for OIR events')
        if self.session_handle == None or self.session_handle._id == 0:
            raise OnepConnectionException('Session is disconnected')
        if OIRListener == None:
            raise OnepIllegalArgumentException('OIRListener', 'None')
        if OIRFilter == None:
            raise OnepIllegalArgumentException('OIRFilter', 'None')
        eventProp = None
        try:
            eventProp = self.api_client.OIREvent_registerIDL(self.session_handle._id, OIRFilter.oir_type)
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        try:
            if eventProp != None:
                self.event_manager.add_listener(eventProp.eventHandle, OIRListener, clientData)
                self.log.debug('Registered OIR listener with event handle : ' + str(eventProp.eventHandle))
                return eventProp.eventHandle
            raise OnepException('Internal error while registering the Listener')
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e.message, e)



    def remove_oir_listener(self, eventHandle):
        """
        Removes the Online Insertion and Removal(OIR) event listener. 
        
        This method removes the listener associated with the specified
        eventHandle and also removes the corresponding registered event on
        the NetworkElement.
        
        @raise OnepIllegalArgumentException:
        The exception is thrown when the eventHandle is not valid or is
        unregistered already.
        @raise OnepConnectionException:
        The exception is thrown when the connection to a network element
        has failed.
        @raise OnepRemoteProcedureException:
        The exception is thrown when an error has occurred in the
        remote procedure call made to a network element.
        @raise OnepException:
        The exception is thrown when an internal error occurs.
        
        @param eventHandle: Registered event identifier.
        
        """
        self.event_manager.remove_listener(eventHandle)



    def add_cli_listener(self, CLIListener, CLIFilter, clientData):
        """
                Adds a CLI listener to the NetworkElement object
                
                Multiple listeners can be associated with an instance of NetworkElement
                
                @raise OnepIllegalArgumentException:
                The exception is thrown when the eventHandle is not valid or
                unregistered already.
                @raise OnepConnectionException:
                The exception is thrown when the connection to a network element
                has failed.
                @raise OnepRemoteProcedureException:
                The exception is thrown when an error has occurred in the
                remote procedure call made to a network element.
                @raise OnepException:
                The exception is thrown when an internal error occurs.
                
                @param CLIListener: The CLIListener object that handles the events.
                @param filter: The CLIFilter to specify criteria of interested CLI events.
                @param  clientData: The client data associated with the listener. This client data
                is part of the input parameters used when the handleEvent method
                in the listener is invoked.
                
                @return:
                EventHandle, a numeric ID associated with this event
                registration. The eventHandle is used to unregister the listener
                using the remove listener method. If registration fails, -1 is
                returned.
        
                """
        if CLIListener == None:
            raise OnepIllegalArgumentException('CLIListener', 'None')
        if CLIFilter == None:
            raise OnepIllegalArgumentException('CLIFilter', 'None')
        if CLIFilter.occurs < 1 or CLIFilter.occurs > OnepConstants.EVENT_MAX_OCCURS:
            raise OnepIllegalArgumentException('CLIFilter occurs', 'not within range (1 to ' + OnepConstants.EVENT_MAX_OCCURS + ' )')
        if CLIFilter.periodMsec < 0:
            raise OnepIllegalArgumentException('CLIFilter period', 'out of range')
        if self.session_handle == None or self.session_handle._id == 0:
            raise OnepConnectionException('Session is disconnected')
        eventProp = None
        try:
            eventProp = self.api_client.CLIEvent_registerIDL(self.session_handle._id, CLIFilter.occurs, CLIFilter.skip, CLIFilter.sync, CLIFilter.timeoutRC, int(CLIFilter.periodMsec / 1000), int(CLIFilter.periodMsec % 1000), CLIFilter.pattern, 0, 0)
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        try:
            if eventProp != None:
                self.event_manager.add_listener(eventProp.eventHandle, CLIListener, clientData)
                self.log.debug('Registered CLI listener with event handle : ' + str(eventProp.eventHandle))
                return eventProp.eventHandle
            raise OnepException('Internal error while registering the Listener')
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e.message, e)



    def remove_cli_listener(self, eventHandle):
        """
        Removes the CLI event listener.
        
        This method will remove the listener associated with the specified
        eventHandle and also remove thecorresponding registered event on the
        NetworkElement.
        
        @raise OnepIllegalArgumentException:
        xxx
        @raise OnepConnectionException:
        The exception is thrown when the connection to a network element
        has failed.
        @raise OnepRemoteProcedureException:
        The exception is thrown when an error has occurred in the
        remote procedure call made to a network element.
        @raise OnepException:
        The exception is thrown when an internal error occurs.
        
        @param  eventHandle: Registered event identifier.
        
        """
        self.event_manager.remove_listener(eventHandle)



    def add_cdp_listener(self, cdpListener, ifFilter, cdpFilter, clientData):
        """
        Adds a (Cisco Discovery Protocol) CDP listener
        
        Multiple listeners can be associated with an instance of
        NetworkElement. The event is generated when changes in the CDP table match
        specified filter criteria on the network element.
        
        @raise OnepIllegalArgumentException:
        The exception is thrown when cdpListener or ifFilter or
        cdpFilter is not valid
        @raise OnepConnectionException:
        The exception is thrown when the connection to a network element
        has failed.
        @raise OnepRemoteProcedureException:
        The exception is thrown when an error has occurred in the
        remote procedure call made to a network element.
        @raise OnepException:
        The exception is thrown when an internal error occurs.
        
        @param  cdpListener: The CDPListener object that handles the events.
        @param  ifFilter: The InterfaceFilter to specify interface list subset.
        @param  cdpFilter: The CDPFilter to specify criteria of interested CDP events.
        @param  clientData: The client data associated with the listener. This client data
        will be part of input parameters when the handleEvent method
        in the listener is invoked.
        
        @return: EventHandle, a numeric ID associated with this event
        registration. The eventHandle is used to unregister the listener
        using the remove listener method. If registration fails, -1 is
        returned.
        
        """
        if cdpListener == None:
            raise OnepIllegalArgumentException('cdpListener', 'None')
        if ifFilter == None:
            raise OnepIllegalArgumentException('ifFilter', 'None')
        if cdpFilter == None:
            raise OnepIllegalArgumentException('cdpFilter', 'None')
        ifFilterIdl = InterfaceFilterIDL()
        ifFilterIdl.interfaceType = ifFilter.interface_type
        if ifFilter.interface == None:
            ifFilterIdl.interfaceXOSHandle = NetworkInterface.ONEP_IF_ALL_HANDLES
        else:
            ifFilterIdl.interfaceXOSHandle = ifFilter.interface.xos_handle
        if self.session_handle == None or self.session_handle._id == 0:
            raise OnepConnectionException('Session is disconnected')
        if self.cdp_client == None:
            self.cdp_client = onep.CdpIDL.CdpIDL.Client(self.api_protocol)
        eventProp = None
        try:
            eventProp = self.cdp_client.CDPEvent_registerIDL(self.session_handle._id, cdpFilter.notify_type, ifFilterIdl)
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        try:
            if eventProp != None:
                self.event_manager.add_listener(eventProp.eventHandle, cdpListener, clientData)
                self.log.debug('Registered CDP Listner with event handle ' + str(eventProp.eventHandle))
                return eventProp.eventHandle
            raise OnepException('Could not register for CDP Event')
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e.message, e)



    def remove_cdp_listener(self, eventHandle):
        """
        Removes the CDP event listener.
        
        This method will remove the listener
        associated with the specified event_handle and also remove the
        corresponding registered event on the NetworkElement.
        
        
        @raise OnepIllegalArgumentException:
        The exception is thrown when the event_handle is not valid or
        is already unregistered.
        @raise OnepConnectionException:
        The exception is thrown when the connection to a network element
        has failed.
        @raise OnepRemoteProcedureException:
        The exception is thrown when an error has occurred in the
        remote procedure call made to a network element.
        @raise OnepException:
        The exception is thrown when an internal error occurs.
        
        @param  eventHandle: Registered event identifier.
                
        """
        self.event_manager.remove_listener(eventHandle)



    def add_interface_address_change_listener(self, listener, ac_filter, client_data):
        """
                Adds an Interface Address Change listener
                
                Multiple listeners can be associated with an instance of NetworkElement.
                
                @raise OnepIllegalArgumentException:
                The exception is thrown any of the listener or filter
                parameters are null or invalid.
                @raise OnepConnectionException:
                The exception is thrown when the connection to a network element
                has failed.
                @raise OnepRemoteProcedureException:
                The exception is thrown when an error has occurred in the
                remote procedure call made to a network element.
                @raise OnepException:
                The exception is thrown when an internal error occurs.
                
                @param  listener: The InterfaceAddressChangeListener object that handles the
                events.
                @param  acFilter: The InterfaceAddressChangeFilter to specify criteria of
                interested InterfaceAddressChange events.
                
                @param  clientData: The client data associated with the listener. This client data
                will be part of input parameters used when the handleEvent method
                in the listener is invoked.
                
                @return: EventHandle, a numeric ID associated with this event
                registration. The eventHandle is used to unregister the listener
                using the removeInterfaceAddressChangeListener method. If
                registration fails, -1 is returned.
        
                """
        self.log.debug('Registering for InterfaceAddressChange events')
        if self.session_handle == None or self.session_handle._id == 0:
            raise OnepConnectionException('Session is disconnected')
        if listener == None:
            raise OnepIllegalArgumentException('InterfaceAddressChangeListener', 'None')
        if ac_filter == None:
            raise OnepIllegalArgumentException('InterfaceAddressChangeFilter', 'None')
        if_filter_idl = InterfaceFilterIDL()
        if ac_filter.interface == None:
            if_filter_idl.interfaceXOSHandle = NetworkInterface.ONEP_IF_ALL_HANDLES
            if_filter_idl.interfaceType = NetworkInterface.InterfaceTypes.ONEP_IF_TYPE_ANY
        else:
            if_filter_idl.interfaceXOSHandle = ac_filter.interface.xos_handle
            if_filter_idl.interfaceType = ac_filter.interface.interface_type
        try:
            event_prop = self.api_client.InterfaceAddrChangeEvent_registerIDL(self.session_handle._id, ac_filter.address_family, if_filter_idl)
            if event_prop != None:
                self.event_manager.add_listener(event_prop.eventHandle, listener, client_data)
                self.log.debug('Registered Interface Address Change listener with event handle : ' + str(event_prop.eventHandle))
                return event_prop.eventHandle
            raise OnepException('Internal error while registering the InterfaceAddressChange Listener')
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e.message, e)



    def remove_interface_address_change_listener(self, eventHandle):
        """
        Removes the Interface Address Change event listener.  
        
        This method removes the listener associated with the specified eventHandle
        and also removes the corresponding registered event on the NetworkElement.
        
        @raise OnepIllegalArgumentException:
        The exception is thrown when eventHandle is not valid or is
        unregistered already.
        @raise OnepConnectionException:
        The exception is thrown when the connection to a network element
        has failed.
        @raise OnepRemoteProcedureException:
        The exception is thrown when an error has occurred in the
        remote procedure call made to a network element.
        @raise OnepException:
        The exception is thrown when an internal error occurs.
        
        @param  eventHandle: Registered event identifier.
        
        @return: EventHandle, a numeric ID associated with this event
        registration.
        
        """
        self.event_manager.remove_listener(eventHandle)



    def add_interface_create_delete_listener(self, listener, if_filter, client_data):
        """
                Adds an Interface Create/Delete event listener
                
                Multiple listeners can be associated with an instance of NetworkElement.
                
                
                @raise OnepIllegalArgumentException:
                The exception is thrown if any of the listener or filter
                parameters are null or invalid.
                @raise OnepConnectionException:
                The exception is thrown when the connection to a network element
                has failed.
                @raise OnepRemoteProcedureException:
                The exception is thrown when an error has occurred in the
                remote procedure call made to a network element.
                @raise OnepException:
                The exception is thrown when an internal error occurs.
                
                @param  listener: The InterfaceCreateDeleteListener object that handles the
                events.
                @param  if_filter: The InterfaceCreateDeleteFilter to specify interface list subset.
                @param  clientData: The client data associated with the listener. This client data
                is part of the input parameters used when the handleEvent method
                in the listener is invoked.
                
                @return: EventHandle, a numeric ID associated with this event
                registration. The eventHandle is used to unregister the listener
                using the removeInterfaceCreateDeleteListener method. If
                registration fails, -1 is returned.
        
                """
        self.log.debug('Registering for InterfaceCreateDelete events')
        if self.session_handle == None or self.session_handle._id == 0:
            raise OnepConnectionException('Session is disconnected')
        if listener == None:
            raise OnepIllegalArgumentException('InterfaceCreateDeleteListener', 'None')
        if if_filter == None:
            raise OnepIllegalArgumentException('if_filter', 'None')
        elif if_filter.interface_type == None:
            raise OnepIllegalArgumentException('Filters property interface_type', 'None')
        elif if_filter.encap == None:
            raise OnepIllegalArgumentException('if_filter encap', 'None')
        elif if_filter.interface == None and if_filter.include_subinterfaces == True:
            self.log.debug('if_filter.interface is set to None and ' + 'if_filter.includeSubinterface is set to true. ' + 'This setting will listen to all interfaces including subinterfaces.')
        filter_idl = InterfaceCreateDeleteFilterIDL()
        filter_idl.interfaceType = if_filter.interface_type
        filter_idl.encap = if_filter.encap
        if if_filter.include_subinterfaces:
            filter_idl.includeSubinterfaces = 1
        else:
            filter_idl.includeSubinterfaces = 0
        if if_filter.interface == None:
            filter_idl.interfaceXOSHandle = NetworkInterface.ONEP_IF_ALL_HANDLES
        else:
            filter_idl.interfaceXOSHandle = if_filter.interface.xos_handle
            filter_idl.encap = InterfaceConfig.Encap.ONEP_IF_ENCAP_ANY
            filter_idl.interfaceType = NetworkInterface.InterfaceTypes.ONEP_IF_TYPE_ANY
        try:
            event_prop = self.api_client.InterfaceCreateDeleteEvent_registerIDL(self.session_handle._id, filter_idl)
            if event_prop != None:
                self.event_manager.add_listener(event_prop.eventHandle, listener, client_data)
                self.log.debug('Registered Interface CreateDelete listener with event handle : ' + str(event_prop.eventHandle))
                return event_prop.eventHandle
            raise OnepException('Internal error while registering the Listener')
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e.message, e)



    def remove_interface_create_delete_listener(self, event_handle):
        """
        Removes the Interface Create/Delete event listener
        
        This method removes the listener associated with the specified event_handle
        and also removes the corresponding registered event on the NetworkElement.
        
        @param  event_handle: Registered event identifier.
         
        @raise OnepIllegalArgumentException:
        The exception is thrown when event_handle is not valid or is
        unregistered already.
        @raise OnepConnectionException:
        The exception is thrown when the connection to a network element
        has failed.
        @raise OnepRemoteProcedureException:
        The exception is thrown when an error has occurred in the
        remote procedure call made to a network element.
        @raise OnepException:
        The exception is thrown when an internal error occurs.        
        """
        self.event_manager.remove_listener(event_handle)



    def add_mtu_listener(self, listener, filter, client_data):
        """
        Adds a MTU change listener to  the network interface.
        
        @param listener: 
             The InterfaceMtuListener object that handles the events.
        @type listener: L{InterfaceMtuListener<onep.interfaces.InterfaceMtuListener.InterfaceMtuListener>} 
        @param filter: 
             The InterfaceMtuFilter to specify criteria of the interested Interface.
             events.
        @type filter: L{InterfaceMtuFilter<onep.interfaces.InterfaceMtuFilter.InterfaceMtuFilter>}
        @param client_data:
             The client data associated with the listener. This client data 
             will be part of input parameters when the handleEvent method 
             in the listener is invoked.
        @return eventHandle: Numeric ID associated with this event registration.
          The eventHandle is used to unregister the listener using the
          removeInterfaceStateListener method.
        
        @raise OnepRemoteProcedureException: System failure to serve the request, please check error
                message for more details.
        @raise OnepConnectionException : Transport error, may need to reset the connection, please 
                check the error message for more details.     
        @raise OnepIllegalArgumentException : This exception is thrown if input parameter is not specified or if 
                it is not of type integer.
        """
        self.log.debug('Registering for Interface MTU change events')
        if self.session_handle == None or self.session_handle._id == 0:
            raise OnepConnectionException('Session is disconnected')
        if listener == None:
            raise OnepIllegalArgumentException('listener', 'None')
        xos_handle = NetworkInterface.ONEP_IF_ALL_HANDLES
        type = NetworkInterface.InterfaceTypes.ONEP_IF_TYPE_ANY
        if filter.interface != None:
            xos_handle = filter.interface.xos_handle
            type = filter.interface.interface_type
        else:
            type = filter.interface_type
        try:
            ni_api_client = onep.NetworkInterfaceIDL.NetworkInterfacesIDL.Client(self.api_protocol)
            event_prop = ni_api_client.InterfaceMtuEvent_registerIDL(self.session_handle._id, xos_handle, type)
            if event_prop != None:
                self.event_manager.add_listener(event_prop.eventHandle, listener, client_data)
                self.log.debug('Registered Interface MTU listener with event handle : ' + str(event_prop.eventHandle))
                return event_prop.eventHandle
            raise OnepException('Internal error while registering the Listener')
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e.message, e)



    def remove_mtu_listener(self, event_handle):
        """
          Removes the MTU event listener. This method will remove the listener associated 
          with the given event_handle.
        
          @param event_handle:
                   Registered event identifier.
          @type event_handle: C{int} 
          @raise OnepRemoteProcedureException: System failure to serve the request, please check error
                  message for more details.
          @raise OnepConnectionException : Transport error, may need to reset the connection, please 
                  check the error message for more details.     
          @raise OnepIllegalArgumentException : This exception is thrown if input parameter is not specified or if 
                  it is not of type integer.
          """
        self.event_manager.remove_listener(event_handle)



    def add_bandwidth_listener(self, listener, filter, client_data):
        """
        Adds a Bandwidth change listener to  the network interface.
        
        @param listener:
             The InterfaceBandwidthListener object that handles the events.
        @type listener: L{InterfaceBandwidthListener<onep.interfaces.InterfaceBandwidthListener.InterfaceBandwidthListener>} 
        @param filter:
             The InterfaceFilter to specify criteria of the interested Interface 
             events.
        @type filter: L{InterfaceFilter<onep.interfaces.InterfaceFilter.InterfaceFilter>}
        @param client_data:
             The client data associated with the listener. This client data 
             will be part of input parameters when the handleEvent method 
             in the listener is invoked.
        @return eventHandle: Numeric ID associated with this event registration.
          The eventHandle is used to unregister the listener using the
          removeInterfaceStateListener method.
        
        @raise OnepRemoteProcedureException: System failure to serve the request, please check error
                message for more details.
        @raise OnepConnectionException : Transport error, may need to reset the connection, please 
                check the error message for more details.     
        @raise OnepIllegalArgumentException : This exception is thrown if input parameter is not specified or if 
                it is not of type integer.
        """
        self.log.debug('Registering for Interface Bandwidth change events')
        if self.session_handle == None or self.session_handle._id == 0:
            raise OnepConnectionException('Session is disconnected')
        if listener == None:
            raise OnepIllegalArgumentException('listener', 'None')
        xos_handle = NetworkInterface.ONEP_IF_ALL_HANDLES
        type = NetworkInterface.InterfaceTypes.ONEP_IF_TYPE_ANY
        if filter.interface != None:
            xos_handle = filter.interface.xos_handle
            type = filter.interface.interface_type
        else:
            type = filter.interface_type
        try:
            ni_api_client = onep.NetworkInterfaceIDL.NetworkInterfacesIDL.Client(self.api_protocol)
            event_prop = ni_api_client.InterfaceBandwidthEvent_registerIDL(self.session_handle._id, xos_handle, type)
            if event_prop != None:
                self.event_manager.add_listener(event_prop.eventHandle, listener, client_data)
                self.log.debug('Registered Interface Bandwidth listener with event handle : ' + str(event_prop.eventHandle))
                return event_prop.eventHandle
            raise OnepException('Internal error while registering the Listener')
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e.message, e)



    def remove_bandwidth_listener(self, event_handle):
        """
          Removes the Bandwidth event listener. This method will remove the listener associated 
          with the given event_handle.
        
          @param event_handle:
                   Registered event identifier.
          @type event_handle: C{int} 
          @raise OnepRemoteProcedureException: System failure to serve the request, please check error
                  message for more details.
          @raise OnepConnectionException : Transport error, may need to reset the connection, please 
                  check the error message for more details.     
          @raise OnepIllegalArgumentException : This exception is thrown if input parameter is not specified or if 
                  it is not of type integer.
          """
        self.event_manager.remove_listener(event_handle)



    def add_vrf_listener(self, listener, filter, client_data):
        """
        Adds a VRF change listener to  the network interface.
        
        @param listener:
             The InterfaceVrfListener object that handles the events.
        @type listener: L{InterfaceVrfListener<onep.interfaces.InterfaceVrfListener.InterfaceVrfListener>} 
        @param filter: 
             The InterfaceVrfFilter to specify criteria of the interested VRF 
             events.
        @type filter: L{InterfaceVrfFilter<onep.interfaces.InterfaceVrfFilter.InterfaceVrfFilter>}
        @param client_data: 
             The client data associated with the listener. This client data 
             will be part of input parameters when the handleEvent method 
             in the listener is invoked.
        @return eventHandle: Numeric ID associated with this event registration.
          The eventHandle is used to unregister the listener using the
          removeInterfaceStateListener method.
        
        @raise OnepRemoteProcedureException: System failure to serve the request, please check error
                message for more details.
        @raise OnepConnectionException : Transport error, may need to reset the connection, please 
                check the error message for more details.     
        @raise OnepIllegalArgumentException : This exception is thrown if input parameter is not specified or if 
                it is not of type integer.
        """
        if listener == None:
            raise OnepIllegalArgumentException('listener', 'None')
        if filter == None:
            raise OnepIllegalArgumentException('filter', 'None')
        xos_handle = NetworkInterface.ONEP_IF_ALL_HANDLES
        if_type = NetworkInterface.InterfaceTypes.ONEP_IF_TYPE_ANY
        if filter.interface != None:
            xos_handle = filter.interface.xos_handle
            type = filter.interface.interface_type
        else:
            type = filter.interface_type
        try:
            ni_api_client = onep.NetworkInterfaceIDL.NetworkInterfacesIDL.Client(self.api_protocol)
            event_prop = ni_api_client.InterfaceVrfEvent_registerIDL(self.session_handle._id, xos_handle, if_type, filter.vrf_name)
            if event_prop != None:
                self.event_manager.add_listener(event_prop.eventHandle, listener, client_data)
                self.log.debug('Registered Interface Vrf listener with event handle : ' + str(event_prop.eventHandle))
                return event_prop.eventHandle
            raise OnepException('Internal error while registering the Listener')
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e.message, e)



    def remove_vrf_listener(self, event_handle):
        """
          Removes the VRF event listener. This method will remove the listener associated 
          with the given eventHandle.
        
          @param event_handle:
                   Registered event identifier.
          @type event_handle: C{int} 
          @raise OnepRemoteProcedureException: System failure to serve the request, please check error
                  message for more details.
          @raise OnepConnectionException : Transport error, may need to reset the connection, please 
                  check the error message for more details.     
          @raise OnepIllegalArgumentException : This exception is thrown if input parameter is not specified or if 
                  it is not of type integer.
          """
        self.event_manager.remove_listener(event_handle)



    def add_vlan_listener(self, listener, filter, client_data):
        """
        Adds a VLAN change listener to  the network interface.
        
        @param listener:
             The InterfaceVlanListener object that handles the events.
        @type listener: L{InterfaceVlanListener<onep.interfaces.InterfaceVlanListener.InterfaceVlanListener>} 
        @param filter:
             The InterfaceVlanFilter to specify criteria of the interested VLAN 
             events.
        @type filter: L{InterfaceVlanFilter<onep.interfaces.InterfaceVlanFilter.InterfaceVlanFilter>}
        @param client_data:
             The client data associated with the listener. This client data 
             will be part of input parameters when the handleEvent method 
             in the listener is invoked.
        @return eventHandle: Numeric ID associated with this event registration.
          The eventHandle is used to unregister the listener using the
          removeInterfaceStateListener method.
        
        @raise OnepRemoteProcedureException: System failure to serve the request, please check error
                message for more details.
        @raise OnepConnectionException : Transport error, may need to reset the connection, please 
                check the error message for more details.     
        @raise OnepIllegalArgumentException : This exception is thrown if input parameter is not specified or if 
                it is not of type integer.
        """
        if listener == None:
            raise OnepIllegalArgumentException('listener', 'None')
        xos_handle = NetworkInterface.ONEP_IF_ALL_HANDLES
        if_type = NetworkInterface.InterfaceTypes.ONEP_IF_TYPE_ANY
        vlan_event_type = InterfaceStatus.InterfaceVLANEventType.ONEP_IF_VLAN_EVENT_ANY
        if filter.interface != None:
            xos_handle = filter.interface.xos_handle
            type = filter.interface.interface_type
        else:
            type = filter.interface_type
        if filter.vlan_event_type != None:
            vlan_event_type = filter.vlan_event_type
        try:
            ni_api_client = onep.NetworkInterfaceIDL.NetworkInterfacesIDL.Client(self.api_protocol)
            event_prop = ni_api_client.InterfaceVlanEvent_registerIDL(self.session_handle._id, xos_handle, if_type, vlan_event_type)
            if event_prop != None:
                self.event_manager.add_listener(event_prop.eventHandle, listener, client_data)
                self.log.debug('Registered Interface Vlan event listener with event handle : ' + str(event_prop.eventHandle))
                return event_prop.eventHandle
            raise OnepException('Internal error while registering the Listener')
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e.message, e)



    def remove_vlan_listener(self, event_handle):
        """
          Removes the VLAN event listener. This method will remove the listener associated 
          with the given eventHandle.
        
          @param event_handle:
                   Registered event identifier.
          @type event_handle: C{int} 
          @raise OnepRemoteProcedureException: System failure to serve the request, please check error
                  message for more details.
          @raise OnepConnectionException : Transport error, may need to reset the connection, please 
                  check the error message for more details.     
          @raise OnepIllegalArgumentException : This exception is thrown if input parameter is not specified or if 
                  it is not of type integer.
          """
        self.event_manager.remove_listener(event_handle)



    def add_appl_listener(self, applListener, AppFilter, clientData):
        """
                Adds an application listener to the NetworkElement object
                
                Multiple listeners can be associated with an instance of NetworkElement.
                The application-specific event allows applications to publish 
                application-specific events. If an application is registered for the 
                event type, it receives a callback notification when the specified 
                event is published and also matches the specified filter.
                
                @raise OnepIllegalArgumentException:
                The exception is thrown when applListener or filter is not
                valid.
                @raise OnepConnectionException:
                The exception is thrown when the connection to a network element
                has failed.
                @raise OnepRemoteProcedureException:
                The exception is thrown when an error has occurred in the
                remote procedure call made to a network element.
                @raise OnepException:
                The exception is thrown when an internal error occurs.
                
                @param  applListener: The ApplListener object that handles the events.
                @param  AppFilter: The ApplFilter used to specify criteria of interested application
                events.
                @param  clientData: The client data associated with the listener. This client data
                is part of the input parameters when the handleEvent method
                in the listener is invoked.
                
                @return: EventHandle, a numeric ID associated with this event
                registration. The eventHandle is used to unregister the listener
                using the removeSyslogListener method. If registration fails, -1
                is returned.
        
                """
        if applListener == None:
            raise OnepIllegalArgumentException('applListener', 'None')
        if AppFilter == None:
            raise OnepIllegalArgumentException('AppFilter', 'None')
        if self.session_handle == None or self.session_handle._id == 0:
            raise OnepConnectionException('Session is disconnected')
        eventProp = None
        try:
            eventProp = self.api_client.ApplEvent_registerIDL(self.session_handle._id, AppFilter.applID, AppFilter.applType, 0, 0)
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        try:
            if eventProp != None:
                self.event_manager.add_listener(eventProp.eventHandle, applListener, clientData)
                return eventProp.eventHandle
            raise OnepException('Could not register for Application Event')
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e.message, e)



    def remove_appl_listener(self, eventHandle):
        """
                Removes the application event listener
                
                This method removes the listener associated with the specified
                eventHandle and also removes the corresponding registered event
                on the NetworkElement.
                
                @raise OnepIllegalArgumentException:
                The exception is thrown when the eventHandle is not valid.
                @raise OnepConnectionException:
                The exception is thrown when the connection to a network element
                has failed.
                @raise OnepRemoteProcedureException:
                The exception is thrown when an error has occurred in the
                remote procedure call made to a network element.
                @raise OnepException:
                The exception is thrown when an internal error occurs.
                
                @param  eventHandle: Registered event identifier.
                
                @return: EventHandle, a numeric ID associated with this event
                registration.
        
                """
        self.event_manager.remove_listener(eventHandle)



    def publish_appl_event(self, pubEvent):
        """
        Publishes an application event to the abstraction layer
        
        This method publishes an application event to the abstraction layer.
        
        @raise OnepIllegalArgumentException:
        The exception is thrown when the pubEvent is not valid.
        @raise OnepConnectionException:
        The exception is thrown when the connection to a network element
        has failed.
        @raise OnepRemoteProcedureException:
        The exception is thrown when an error has occurred in the
        remote procedure call made to a network element.
        @raise OnepException:
        The exception is thrown when an internal error occurs.
        
        @param  pubEvent: The event to publish.
                
        """
        if pubEvent == None:
            return 
        if self.session_handle == None or self.session_handle._id == 0:
            raise OnepConnectionException('Session is disconnected')
        try:
            self.api_client.ApplEvent_publishIDL(self.session_handle._id, pubEvent.applID, pubEvent.applType, pubEvent.applData[1], pubEvent.applData[2], pubEvent.applData[3], pubEvent.applData[4])
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e.message, e)
        except OnepIllegalArgumentException as e:
            pass



    def reconnect(self, username, password, session_id, session_config):
        """
                Reconnects to the disconnected session.
                
                Provides the ability to reconnect back to the network element after the
                session is disconnected by the application via the disconnect method, or
                abnormally due to connection failure. If the application has specified the
                reconnect timer during the connect attempt to the network element, it
                can reconnect to the original session if reconnection is made
                within the reconnect timeout window, if the sessionId is the same as the
                original session, and if the reauthentication is successful. With successful
                reconnection, the same SessionHandle is returned.
        
                If any failure occurs during the reconnection attempt, NULL SessionHandle is
                returned along with the exception detailing the reason. If the reconnect
                timer expires and no reconnection attempt is successfully made to the
                network element, the session resource in the network element is
                released.
        
                null SessionHandle is returned in the following cases:
                  - If the sessionId argument passed does not match the unique ID of
                  the disconnected session on the network element.
                  - If the disconnected session does not have a reconnect timer specified
                  during the connect() attempt.
                  - If reauthentication using username and password has failed.
                  - If any failure occurred during the reconnect attempt.
                
                @raise OnepIllegalArgumentException:
                The exception is thrown when any of the arguments is invalid.
                @raise OnepConnectionException:
                The exception is thrown when reconnection fails.
                @raise OnepRemoteProcedureException:
                The exception is thrown when an error has occurred in the
                remote procedure call made to a network element.
                @raise OnepDuplicateElementException:
                If the application is connected to the NetworkElement using
                one IP address, and then attempts to connect to the
                NetworkElement using another IP address, this exception will
                be thrown.
                @raise OnepException:
                The exception is thrown when an internal error occurs.
                
                @param  username: Mandatory username used for the session authentication. It
                should not be greater than OnepConstants.MAX_USERNAME_LEN
                characters in length.
                @type username: C{str}
                
                @param  password: Mandatory password used for the session authentication. It
                should not be greater than OnepConstants.MAX_PASSWORD_LEN
                characters in length.
                @type password: C{str}
                
                @param  session_id: The unique ID of the disconnected SessionHandle.
                @type session_id: C{int} 
                
                @param  session_config: session_config contains attributes for reconnecting to network
                element.
                @type session_config: L{SessionConfig<onep.element.SessionConfig.SessionConfig>}
                
                @return: A SessionHandle, if authenticated session is successfully
                established. null, if reconnect or reauthentication attempt
                failed.
        
                """
        self.log.info('Reconnecting session id: ' + str(session_id))
        validate(session_config, SessionConfig)
        validate(session_id, int)
        if not session_id:
            raise OnepIllegalArgumentException('session_id', '0')
        self.session_handle = SessionHandle(session_id, self, session_config)
        self.state = self.OnepSessionState.ONEP_STATE_RECONNECTING
        if self._conn_event_listener:
            self.publish_connection_event('Connected event')
        self._reconnect_waiting = False
        return self.connect_(username, password, session_config, True)



    def connect(self, username, password, session_config = None):
        """
                Connects to the network element using default session configuration.
                
                This method provides the ability to connect to the network element, if it
                is not currently connected. With successful connection and authentication
                to the network element, a SessionHandle is returned. If any failure
                occurs during the connection attempt, an exception detailing the reason
                will be raised. The default SessionConfig is used during establishment
                of the connection.
                
                Authentication is required in order to access the NetworkElement.
                Password authentication is used. The username and password needs to be
                configured in the network element and to be authenticated using network
                element configured authentication mechanism (that is, locally, RADIUS, and
                TACACS+)
                
                
                Note: Each network element has a configurable session limit that allows
                the rate limit on accessing the network element. This limit is
                configurable via CLI (session maximum) in the network element. The range
                is 1 to100. Default maximum session is 10.
                
                @raise OnepIllegalArgumentException:
                The exception is thrown when any of the arguments is invalid.
                @raise OnepConnectionException:
                The exception is thrown when connection fails.
                @raise OnepRemoteProcedureException:
                The exception is thrown when an error has occurred in the
                remote procedure call made to a network element.
                @raise OnepDuplicateElementException:
                If the application is connected to the NetworkElement using
                one IP address, and then it attempts to connect to the
                NetworkElement using a different IP address, this exception will
                be thrown.
                @raise OnepException:
                The exception is thrown when an internal error occurs.
                
                @param  username: Mandatory username used for the session authentication. It
                should not be greater than OnepConstants.MAX_USERNAME_LEN
                characters in length.
                @type username: C{str}
                
                @param  password: Mandatory password used for the session authentication. It
                should not be greater than OnepConstants.MAX_PASSWORD_LEN
                characters in length.
                @type password: C{str}
                
                @param  session_config: session_config contains attributes for connecting to network
                element. Default: None
                @type session_config: L{SessionConfig<onep.element.SessionConfig.SessionConfig>}
                
                @return: A SessionHandle, if the authenticated session is successfully
                established.
        
                """
        if not session_config:
            session_config = SessionConfig(None)
        return self.connect_(username, password, session_config, False)



    def connect_1(self, username, password, session_config):
        """
        Connects to the network element with the specified session configuration.
        
        This method is deprecated and replaced by connect
        
        This method provides the ability to connect to the network element, if it
        is not currently connected. With successful connection and authentication
        to the network element, a SessionHandle is returned. If any failure
        occurs during the connecting attempt, NULL SessionHandle is returned
        along with the exception detailing the reason. The default SessionConfig
        is used during connection establishment.
        
        Authentication is required in order to access the NetworkElement.
        Password authentication is used. The username and password needs to be
        configured in the network element and to be authenticated using network
        element configured authentication mechanism (i.e. locally, RADIUS, and
        TACACS+)
        
        Note. Optionally, application can set a reconnect timer in seconds via
        SessionConfig class. The timer is used in the network element side to
        keep the session information intact upon detection of application is
        unreachable (that is link is down or disconnected).
        
        If application is able to reconnect to the network element within the
        timeout window, the existing session context will be restored and used.
        If no reconnect timer is specified, the existing session information on
        the network element is released upon detection of unreachable of
        application.
        
        If application uses connect method to network element where the exited
        session still have reconnect timer running, the timer will be canceled.
        A new session establishment will be attempted.
        
        @raise OnepIllegalArgumentException:
        The exception is thrown when any of the arguments is invalid.
        @raise OnepConnectionException:
        The exception is thrown when connection fails.
        @raise OnepRemoteProcedureException:
        The exception is thrown when an error has occurred in the
        remote procedure call made to a network element.
        @raise OnepDuplicateElementException:
        If the application is connected to the NetworkElement using
        one IP address, and then it attempts to connect to the
        NetworkElement using a different IP address, this exception will
        be thrown.
        @raise OnepException:
        The exception is thrown when an internal error occurs.
        
        @param  username: Mandatory username used for the session authentication. It
        should not be greater than OnepConstants.MAX_USERNAME_LEN
        characters in length.
        
        @param  password: Mandatory password used for the session authentication. It
        should not be greater than OnepConstants.MAX_PASSWORD_LEN
        characters in length.
        
        @param  sessionConfig: sessionConfig contains attributes for connecting to network
        element.
        
        @return: A SessionHandle, if authenticated session is successfully
        established. Otherwise, null is returned.
        
        """
        self.log.warning("'connect_1' method is deprecated please use 'connect'")
        return self.connect_(username, password, session_config, False)



    def _get_vm_credentials(self, session):
        """
                Internal method to retrieve the virtual machine credentials from a container
                when making a TIPC connection.
        
                @return: Internal VM credential structure
        
                """
        try:
            f1 = open(session.vm_credential_file)
            creds = f1.read()
            vm_id = [ item[6:].lstrip().rstrip() for item in creds.splitlines() if item.startswith('VM-ID:') ]
            dn_id = [ item[10:].lstrip().rstrip() for item in creds.splitlines() if item.startswith('DOMAIN-ID:') ]
            dnid_bytes = None
            vmcred = [1, 0, 0]
            total_length = 0
            if dn_id:
                vmcred.append(1)
                dnid_bytes = int(dn_id[0])
                vmcred.append(2)
                if dnid_bytes > 255:
                    vmcred.append(c_byte(int(hex(dnid_bytes)[:(len(hex(dnid_bytes)) - 2)])).value)
                    vmcred.append(c_byte(int(hex(dnid_bytes)[(len(hex(dnid_bytes)) - 2):])).value)
                else:
                    vmcred.append(0)
                    vmcred.append(c_byte(dnid_bytes).value)
                total_length = 4
            if vm_id:
                vmcred.append(2)
                vmid_str = vm_id[0]
                vmcred.append(len(vmid_str))
                for c in vmid_str:
                    vmcred.append(ord(c))

                total_length += len(vmid_str) + 2
                if total_length > 255:
                    vmcred[1] = c_byte(int(hex(total_length)[:(len(hex(total_length)) - 2)], base=16)).value
                    vmcred[2] = c_byte(int(hex(total_length)[(len(hex(total_length)) - 2):], base=16)).value
                else:
                    vmcred[2] = c_byte(total_length).value
                session.vm_credential = VmCredentialIDL(vmcred)
            else:
                raise OnepVMcredentialException('%s data file invalid format\n' % (session.vm_credential_file, str(creds)))
        except IOError as e:
            if e.errno == 2:
                vmcred = [2,
                 0,
                 8,
                 2,
                 6]
                eobc = InterfaceMap().get_eobcmac()
                for bt in eobc.split(':'):
                    vmcred.append(c_byte(int(bt, base=16)).value)

                session.vm_credential = VmCredentialIDL(vmcred)



    def connect_(self, username, password, session_config, reconnect):
        """
        For internal use only
        """
        if self.state == self.OnepSessionState.ONEP_STATE_CONNECTED and self.session_handle != None and self.session_handle._id != 0:
            self.log.info('Session already established, returning the same')
            return self.session_handle
        if session_config == None:
            session_config = SessionConfig(None)
        if username == None:
            username = ''
        if password == None:
            password = ''
        if session_config.transportMode == SessionConfig.SessionTransportMode.TIPC:
            if OnepConstants.MAX_USERNAME_LEN < len(username):
                raise OnepIllegalArgumentException('username', 'Exceeds limits')
            if OnepConstants.MAX_PASSWORD_LEN < len(password):
                raise OnepIllegalArgumentException('password', 'Exceeds limits')
        elif OnepConstants.MAX_USERNAME_LEN < len(username) or 0 >= len(username):
            raise OnepIllegalArgumentException('username', 'Exceeds limits')
        if OnepConstants.MAX_PASSWORD_LEN < len(password) or 0 >= len(password):
            raise OnepIllegalArgumentException('password', 'Exceeds limits')
        self.log.info('Connect called')
        prop = None
        self.port = session_config.port
        self.log.debug('self.port: %s' % self.port)
        try:
            if session_config.transportMode == SessionConfig.SessionTransportMode.SOCKET:
                self.api_transport = TSocket(self.host_address, self.port)
            elif session_config.transportMode == SessionConfig.SessionTransportMode.TIPC:
                self.api_transport = TTIPCSocket()
                if not session_config.vm_credential:
                    self._get_vm_credentials(session_config)
                self.log.debug('self.port: ' + str(self.port))
            else:
                accept_once = []
                if session_config.ca_certs is None:
                    self.log.info('No CA certs given.')
                else:
                    self.log.info('Root cert from: %s' % session_config.ca_certs)
                self.api_transport = CiscoTSSLSocket(self.host_address, self.port, keyfile=session_config.keyfile, certfile=session_config.certfile, ca_certs=session_config.ca_certs, pinning_file=session_config.tls_pinning_file, unverified_handler=session_config.tls_unverified_element_handler, accept_once=accept_once)
            self.api_transport.setTimeout(session_config.read_write_timeout * 1000)
            self.api_transport = TBufferedTransport(self.api_transport)
            try:
                inSessionID = 0
                self.api_protocol = TBinaryProtocolAccelerated(self.api_transport)
                self.api_client = NetworkElementIDL.Client(self.api_protocol)
                if not self.api_transport.isOpen():
                    self.api_transport.open()
                if self.state == self.OnepSessionState.ONEP_STATE_RECONNECTING and self.session_handle != None and self.session_handle._id != 0:
                    self.log.info('Reconnect request for session Id: ' + str(self.session_handle._id))
                    inSessionID = self.session_handle._id
                self.state = self.OnepSessionState.ONEP_STATE_CONNECTING
                if self._conn_event_listener:
                    self.publish_connection_event('Connecting event')
                if None == self.appname:
                    if stack == None or len(stack):
                        self.appname = ''
                    elif None == main:
                        self.appname = ''
                    else:
                        self.appname = main.getClassName().substring(index)
                self.username = username
                self.password = password
                versionIdl = OnepVersionIDL(ONEP_VERSION_MAJOR, ONEP_VERSION_MINOR, ONEP_VERSION_MAINTENANCE)
                if inSessionID == None:
                    inSessionID = 0
                self.log.info('connectIDL: appname [' + self.appname + '] host_address[' + self.host_address + '] timer [' + str(session_config.reconnectTimer) + '] sessionid [' + str(inSessionID) + ']')
                try:
                    prop = self.api_client.NetworkElement_connectIDL(self.appname, self.host_address, username, password, session_config.reconnectTimer, inSessionID, versionIdl, session_config.keepAliveIdleTime, session_config.vm_credential)
                except TTransport.TTransportException as e:
                    if session_config.transportMode != SessionConfig.SessionTransportMode.TLS or isinstance(e, TTransport.TTransportException) and e.type != TTransport.TTransportException.END_OF_FILE:
                        raise e
                    self.api_transport.close()
                    self.api_transport = CiscoTSSLSocket(self.host_address, self.port, keyfile=session_config.keyfile, certfile=session_config.certfile, ca_certs=session_config.ca_certs, pinning_file=session_config.tls_pinning_file, unverified_handler=session_config.tls_unverified_element_handler, accept_once=accept_once)
                    self.api_transport.setTimeout(session_config.read_write_timeout * 1000)
                    self.api_transport = TBufferedTransport(self.api_transport)
                    self.api_protocol = TBinaryProtocolAccelerated(self.api_transport)
                    self.api_client = NetworkElementIDL.Client(self.api_protocol)
                    if not self.api_transport.isOpen():
                        self.api_transport.open()
                    prop = self.api_client.NetworkElement_connectIDL(self.appname, self.host_address, username, password, session_config.reconnectTimer, inSessionID, versionIdl, session_config.keepAliveIdleTime, session_config.vm_credential)
                self.properties = ElementProperty(self, prop)
                self._reconnect_waiting = False
            except ExceptionIDL as e:
                self.log.error('IDL Exception: ' + e.__str__())
                if e.code == OnepConstants.ERR_DUPLICATE:
                    raise OnepDuplicateElementException(self, e.message, e)
                else:
                    raise OnepConnectionException(self, e)
            except TException as e:
                self.log.error('Thrift exception: ' + e.__str__())
                raise OnepConnectionException(e.message, e)
            if session_config.transportMode == SessionConfig.SessionTransportMode.SOCKET:
                self.evt_transport = TSocket(self.host_address, self.port)
                self.evt_transport = TBufferedTransport(self.evt_transport)
            elif session_config.transportMode == SessionConfig.SessionTransportMode.TIPC:
                self.evt_transport = TTIPCSocket()
                self.evt_transport = TBufferedTransport(self.evt_transport)
            else:
                self.evt_transport = CiscoTSSLSocket(self.host_address, self.port, keyfile=session_config.keyfile, certfile=session_config.certfile, ca_certs=session_config.ca_certs, pinning_file=session_config.tls_pinning_file, unverified_handler=session_config.tls_unverified_element_handler, accept_once=accept_once)
                self.evt_transport = TBufferedTransport(self.evt_transport)
            try:
                self.evt_protocol = TBinaryProtocolAccelerated(self.evt_transport)
                self.evt_client = NetworkElementIDL.Client(self.evt_protocol)
                if not self.evt_transport.isOpen():
                    self.evt_transport.open()
                self.session_handle = SessionHandle(prop.sessionHandle, self, session_config)
                self.evt_client.NetworkElement_evtChannelIDL(self.session_handle._id)
                self.intf_client = onep.NetworkInterfaceIDL.NetworkInterfacesIDL.Client(self.api_protocol)
                self.system_client = onep.SystemStatusIDL.SystemStatusIDL.Client(self.api_protocol)
                self.discovery_client = onep.DiscoveryIDL.DiscoveryIDL.Client(self.api_protocol)
                self.location_client = onep.LocationIDL.LocationIDL.Client(self.api_protocol)
                self.policy_client = onep.PolicyIDL.PolicyIDL.Client(self.api_protocol)
                self.applmgmt_client = ApplmgmtDataIDL.Client(self.api_protocol)
            except ExceptionIDL as e:
                raise OnepConnectionException(e.message, e)
            except TTransportException as e:
                self.log.error('Transport exception: ' + str(e))
                raise OnepConnectionException(e.message, e)
            except TException as e:
                self.log.error('Thrift exception: ' + str(e))
                raise OnepConnectionException(e.message, e)
            if session_config.thread_stack_size != 0:
                import threading
                threading.stack_size(session_config.thread_stack_size)
            self.event_manager = EventManager(self, self.evt_protocol)
            self.state = self.OnepSessionState.ONEP_STATE_CONNECTED
            if self._conn_event_listener:
                self.publish_connection_event('Connected event')
            NetworkApplication.get_instance().increment_connected_count()
            self.connect_time = time()
            self.disconnect_time = None
        except OnepConnectionException as e:
            self.log.error('Could not connect to NetworkElement: ' + e.__str__())
            self.disconnect(e.message)
            raise e
        except TTransportException as e:
            self.log.error('Transport exception: ' + e)
            raise OnepConnectionException(e.message, e)
        self.log.info('Successfully established connection')
        return self.session_handle



    def disconnect(self, msg = ''):
        """
        Disonnect from a network element
        
        This method provides the ability to disconnect from the network element
        if the application is currently connected. When
        the application finishes the session, the session can be disconnected. This
        allows the network element resources to be freed on the network element, if no
        optional reconnect timer has been specified during the connect.
        
        @raise OnepIllegalArgumentException:
        The exception is thrown when any of the arguments is invalid.
        @raise OnepConnectionException:
        The exception is thrown when the connection to a network element
        has failed.
        @raise OnepRemoteProcedureException:
        The exception is thrown when an error has occurred in the
        remote procedure call made to a network element.
        @raise OnepException:
        The exception is thrown when an internal error occurs.
        
        @param  msg:
                
        """
        self.log.info('Disconnecting')
        if self.state == self.OnepSessionState.ONEP_STATE_DISCONNECTED:
            self.log.info('Session already disconnected')
            return 
        if self.event_manager != None:
            self.log.info('Signalling event channel for termination')
            self.event_manager.terminate()
        try:
            if not self._reconnect_waiting:
                disconnected = self.api_client.NetworkElement_disconnectIDL()
                self.log.info('Session disconnected ' + str(disconnected))
        except ExceptionIDL as e:
            self.log.error('IDL Exception: ' + str(e))
        except TException as e:
            self.log.error('Thrift exception: ' + str(e))
        if self.api_transport != None:
            self.api_transport.close()
        if self.evt_transport != None:
            self.evt_transport.close()
        self.log.info('Terminated API and Event channels')
        if self.session_handle != None:
            self.session_handle._id = 0
        self._vty = None
        self._vty_service = None
        self.routing = None
        self.connect_time = None
        self.disconnect_time = time()
        self.disconnect_msg = msg
        self.state = self.OnepSessionState.ONEP_STATE_DISCONNECTED
        self.log.info('Resources released, state set to %s' % self.OnepSessionState.enumval(self.state))
        NetworkApplication.get_instance().decrement_connected_count()
        if self._conn_event_listener:
            self.publish_connection_event(msg)
        self.log.info('Disconnect complete')



    def get_interface_dict(self, if_filter):
        """
        Gets the interfaces collection in dictionary form
        
        @raise OnepIllegalArgumentException:
        The exception is thrown when any of the arguments is invalid.
        @raise OnepConnectionException:
        The exception is thrown when the connection to a network element
        has failed.
        @raise OnepRemoteProcedureException:
        The exception is thrown when an error has occurred in the
        remote procedure call made to a network element.
        @raise OnepException:
        The exception is thrown when an internal error occurs.
        
        @param  if_filter: Specifications for selecting subset of interfaces.
        
        @return: All the network interfaces. The network
        interfaces includes both physical and logical ones.
        
        """
        if if_filter == None:
            raise OnepIllegalArgumentException('if_filter', 'None')
        if self.session_handle == None or self.session_handle._id == 0:
            raise OnepConnectionException('Session is disconnected')
        xosHandle = NetworkInterface.ONEP_IF_ALL_HANDLES
        type_ = if_filter.interface_type
        if if_filter.interface != None:
            xosHandle = if_filter.interface.xos_handle
            type_ = if_filter.interface.interface_type
        self.interfaces = {}
        try:
            list = self.intf_client.NetworkElement_getInterfaceListIDL(self.session_handle._id, xosHandle, int(type_), 0, 0)
            for ni in list:
                intf = NetworkInterface.get_interface_instance_by_type(self, ni.name, ni.type, ni.xosHandle)
                self.interfaces[ni.name] = intf

        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e.message, e)
        return self.interfaces



    def get_interface_list(self, if_filter):
        """
        Gets the list of interfaces
        
        @raise OnepIllegalArgumentException:
        The exception is thrown when any of the arguments is invalid.
        @raise OnepConnectionException:
        The exception is thrown when the connection to a network element
        has failed.
        @raise OnepRemoteProcedureException:
        The exception is thrown when an error has occurred in the
        remote procedure call made to a network element.
        @raise OnepException:
        The exception is thrown when an internal error occurs.
        
        @param  if_filter: Specifications for selecting subset of interfaces.
        
        @return: A list of all the network interfaces. The network
        interfaces includes both physical and logical ones.
        
        """
        map = self.get_interface_dict(if_filter)
        if None != map:
            return map.values()



    def get_interface_by_name(self, ifName):
        """
                Gets the NetworkInterface instance by the giving display name.
                This method returns a NetworkInterface instance on the specified
                NetworkElement by the giving display name.
                The name should be in the long display name format, for example,
                "Ethernet0/1".
                
                @raise OnepNoDataException:
                Interface does not exist on this element
                @raise OnepIllegalArgumentException:
                The exception is thrown when any of the arguments is invalid.
                @raise OnepConnectionException:
                The exception is thrown when the connection to a network element
                has failed.
                @raise OnepRemoteProcedureException:
                The exception is thrown when an error has occurred in the
                remote procedure call made to a network element.
                @raise OnepException:
                The exception is thrown when an internal error occurs.
                
                @param  ifName: Name of the network interface.
                
                @return: The NetworkInterface instance whose name matches the specified
                name.
        
                """
        if ifName == None or 0 == len(ifName):
            raise OnepIllegalArgumentException('ifName', 'None')
        if self.session_handle == None or self.session_handle._id == 0:
            raise OnepConnectionException('Session is disconnected')
        intf = None
        try:
            intf_item = self.intf_client.NetworkElement_getInterfaceByNameIDL(ifName)
            intf = NetworkInterface.get_interface_instance_by_type(self, intf_item.name, intf_item.type, intf_item.xosHandle)
        except ExceptionIDL as e:
            raise OnepException('get_interface_by_name', e)
        except TException as e:
            raise OnepConnectionException(e.text, e)
        return intf



    def get_vlan_list(self):
        """
                Return a list of configured VLANs with status
        
                @return dict:
                    Keys
                    ----
                    id -- int - VLAN ID
                    name -- string - VLAN text name
                    state -- OnepConstants.VlanState
                                 NONE
                                 ACTIVE
                                 SUSPEND
                                 NOT_CONFIG
                    shutdown -- boolean - True == Shutdown, False == No shutdown
        
                @raise OnepConnectionException:
                The exception is thrown when the connection to a network element 
                has failed. 
                @raise OnepRemoteProcedureException:
                The exception is thrown when an error has occurred in the
                remote procedure call made to a network element.
        
                """
        self.log.info('get vlan list')
        try:
            vlist = []
            if self.vlan_client == None:
                self.vlan_client = VlanIDL.Client(self.api_protocol)
            idllist = self.vlan_client.getAllVlans_IDL(self.session_handle._id)
            for vlan in idllist:
                vdict = {}
                vdict['id'] = vlan.vlanId
                vdict['name'] = vlan.vlanName
                vdict['state'] = OnepConstants.VlanState.enumval(vlan.vlanState)
                vdict['shutdown'] = bool(vlan.vlanAdminState)
                self.log.info(str(vdict))
                vlist.append(vdict)

            return vlist
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)



    def get_process_list(self):
        """
                Returns a list of ProcessIDL class.
                
                Gets the list of active processes in the NetworkElement and their
                respective CPU utilization and memory usage.
                
                The application can specify the time period for which it wants to
                retrieve the CPU utilization by setting the sampling interval.
                If the application does not set the
                sampling interval, the getProcessList() method retrieves CPU utilization
                for the most recent time period. However, if the application does set the
                sampling interval but the interval does not match any of the time period
                values supported by the platform, then the CPU utilization is retrieved
                for the most recent time period which is closest to the sampling
                interval. For example, if the Network Element supports CPU utilization
                for time periods 5 seconds, 60 seconds and 300 seconds, and the
                application sets the sampling interval as 100seconds, then the CPU
                utilization returned will be for the most recent time period closest to
                100 seconds, which is 60 seconds.
                
                If there is an error in receiving the cpu usage value, it will be set to -1. 
                
                @raise OnepIllegalArgumentException:
                Sampling interval is negative
                @raise OnepConnectionException:
                If the connection to the NE is dropped
                @raise OnepRemoteProcedureException:
                The exception is thrown when an error has occurred in the
                remote procedure call made to a network element.
                @raise OnepException:
                The exception is thrown when an internal error occurs.
                
                @return: The list of ElementProcess objects or a list of size 0 if there
                is an error or no process information can be retrieved.
        
                """
        if self.session_handle == None or self.session_handle._id == 0:
            raise OnepConnectionException('Session is disconnected')
        process = []
        try:
            processDetail = self.system_client.NetworkElement_getProcessIDL(self.session_handle._id, self.cpu_sampling_interval)
            self.cpu_sampling_interval = processDetail.samplingInterval
            process = processDetail.processList
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e.message, e)
        except OnepIllegalArgumentException as e:
            raise OnepException('Sampling interval is negative')
        for proc in process:
            try:
                proc.cpuUsage = float(proc.cpuUsage)
            except:
                proc.cpuUsage = -1

        return process



    def get_total_system_memory(self):
        """
                Gets the total system memory in bytes.
                
                @return: The total system memory in bytes.
                
                @raise OnepRemoteProcedureException:
                The exception is thrown when an error has occurred in the
                remote procedure call made to a network element.
                @raise OnepConnectionException:
                The exception is thrown when the connection to a network element
                has failed.
        
                """
        if self.session_handle == None or self.session_handle._id == 0:
            raise OnepConnectionException('Session is disconnected')
        try:
            return self.system_client.NetworkElement_getTotalSystemMemoryIDL(self.session_handle._id)
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e.message, e)


    total_system_memory = property(get_total_system_memory)

    def get_free_system_memory(self):
        """
        Gets the free system memory in bytes.
        
        @return: The system memory, that is, the amount of free memory in bytes.
        
        @raise OnepRemoteProcedureException:
                    The exception is thrown when an error has occurred in the
                    remote procedure call made to a network element.
        @raise OnepConnectionException:
                    The exception is thrown when the connection to a network element
                    has failed.
        
        """
        if self.session_handle == None or self.session_handle._id == 0:
            raise OnepConnectionException('Session is disconnected')
        try:
            return self.system_client.NetworkElement_getFreeSystemMemoryIDL(self.session_handle._id)
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e.message, e)


    free_system_memory = property(get_free_system_memory)

    def get_system_cpu_utilization(self):
        """
        Gets the total CPU utilization in percentage.
        
        The time period for which the CPU utilization is retrieved is determined
        by the sampling interval set through the
        {@link #setCPUSamplingInterval(int)} method. If no sampling interval is
        set, the CPU utilization is retrieved for the most recent time period
        supported by the platform. However, if the application does set the
        sampling interval, but interval does not match any of the time periods
        supported by the platform, the CPU utilization returned is for the most
        recent time period closest to the sampling interval.
        
        @return: the CPU usage The CPU utilization in percentage.
        @raise OnepConnectionException:
                    The exception is thrown when the connection to a network element
                    has failed.
        @raise OnepRemoteProcedureException:
                    The exception is thrown when an error has occurred in the
                    remote procedure call made to a network element.
        @raise OnepException:
                    The exception is thrown when the server returns an invalid CPU
                    sampling interval value.
        """
        if self.session_handle == None or self.session_handle._id == 0:
            raise OnepConnectionException('Session is disconnected')
        try:
            cpuIDL = self.system_client.NetworkElement_getSystemCPUUtilizationIDL(self.session_handle._id, self.cpu_sampling_interval)
            cpuUsage = cpuIDL.cpu_usage
            self.cpu_sampling_interval = cpuIDL.samplingInterval
            return cpuUsage
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e.message, e)
        except OnepIllegalArgumentException as e:
            raise OnepException('Sampling Interval is negative')


    system_cpu_utilization = property(get_system_cpu_utilization)

    def set_application_config_cli_listener(self, listener, client_data):
        """
        This method for internal use only
        """
        self.config_listener = listener
        self.config_client_data = client_data
        if listener == None:
            self.log.debug('UnRegistered ApplicationConfigCliListener')
        else:
            self.log.debug('Registered ApplicationConfigCliListener')



    def set_application_exec_cli_listener(self, listener, client_data):
        """
        This method for internal use only
        """
        self.exec_listener = listener
        self.exec_client_data = client_data
        if listener == None:
            self.log.debug('UnRegistered ApplicationExecCliListener')
        else:
            self.log.debug('Registered ApplicationExceCliListener')



    def set_appl_managed_data(self, app_data):
        """
        This method for internal use only
        """
        self.appl_managed_data = app_data



    def get_application_exec_cli_listener(self):
        """
        This method for internal use only
        """
        return self.exec_listener



    def get_application_exec_cli_client_data(self):
        """
        This method for internal use only
        """
        return self.exec_client_data



    def get_application_config_cli_listener(self):
        """
        This method for internal use only
        """
        return self.config_listener



    def get_application_config_cli_client_data(self):
        """
        This method for internal use only
        """
        return self.config_client_data



    def discover_service_set_list(self):
        """
                Discovers services available on the root network element and also on its neighbors that support onePK services.
                
                The application has to be connected to the root network element to 
                initiate service discovery. The discover_service_set_list method returns
                a list of L{ServiceSetDescription<src.discovery.ServiceSetDescription>} 
                containing the information on the service set that is available on the
                root network element and its neighbors. In cases where onePK-supported
                discovery protocol is not enabled on the root element, the 
                discover_service_set_list API returns service information only for the
                root element. The onePK application can use the information returned by
                L{ServiceSetDescription<src.discovery.ServiceSetDescription>} to identify 
                the network elements that support a given set of services, and initiate
                connection to those elements and invoke the service set APIs.
        
                The following sample code shows on how to obtain information on the
                services supported by the root NetworkElement and its neighbors:
                
                >>> sdList = elem.discover_service_set_list()
                >>> for sd in sdList:
                        #get network element
                        ne = sd.network_element
                        #get the services available on this Network Element
                        #Service Set name is the key, value is the string
                        #containing the enabled Service set version
                        services = sd.service_set_list
                        #Connect to the Neighboring 1P network element, which supports
                        #1.0 version of ONEP_BASE_SERVICE_SET
                                
                @return: list of ServiceSetDescription
                
                @raise OnepRemoteProcedureException: The exception is thrown when an 
                error has occurred in the remote procedure call made to a network 
                element.
                @raise OnepConnectionException: The exception is thrown when an error has 
                occurred in the remote procedure call made to a network element.
                @raise OnepException: The exception is thrown when an internal error 
                occurs.
                
                """
        from onep.discovery.ServiceSetDescription import ServiceSetDescription
        if self.session_handle == None or self.session_handle._id == 0:
            raise OnepConnectionException('Session is disconnected')
        sdList = list()
        sdIDLList = list()
        try:
            sdIDLList = self.discovery_client.NetworkElement_discoverServiceListIDL(self.session_handle._id)
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e.message, e)
        if sdIDLList == None:
            raise OnepException('Failed to retrieve service list')
        for sdIDL in sdIDLList:
            serviceMap = {}
            matchFound = False
            ipAddress = sdIDL.ipAddress
            key = sdIDL.serviceNameKey
            version = Version(sdIDL.version.major, sdIDL.version.minor, sdIDL.version.maint)
            if ipAddress == 'localhost':
                ipAddress = self.host_address
            for sd in sdList:
                if sd.network_element.host_address == ipAddress:
                    matchFound = True
                    serviceMap = sd.service_set_list
                    if key not in serviceMap:
                        serviceMap[key] = version
                    else:
                        continue
                        continue

            if not matchFound:
                if ipAddress == self.host_address:
                    ne = self
                else:
                    ne = NetworkElement(ipAddress, self.appname)
                serviceMap[key] = version
                sdList.append(ServiceSetDescription(ne, serviceMap))

        return sdList



    def add_discovery_listener(self, discoveryListener, discoveryFilter, clientData):
        """
        Adds a Service Set Discovery listener to the NetworkElement object.
        
        The application can add a Service Discovery listener to receive service 
        set state change notifications from the Network Element to which it is 
        directly connected (the root Network Element) and its neighbors. The 
        application can also define filter criteria based on Network Element, 
        service set name, and service set state.
        
        The application can use the notification received to either invoke the
        APIs of the enabled service sets, or cleanup the resources for the 
        disabled service sets. Multiple listeners can be associated with an 
        instance of NetworkElement.
        
        Note: The application will not receive notifications for Base service 
        set changes for Local discovery type. If the Base service set is disabled 
        on the root network element, the application will receive connection 
        notification if the application has registered for connection 
        notification. For remote discovery, the application will receive 
        notification on Base Service set state changes provided the application
        has registered for these change notifications.
        
        @param clientData: The client data associated with the listener. This 
        client data is part of the input parameters used when the handle_event 
        method in the listener is invoked.
        
        @param discoveryListener:  The DiscoveryListener object that handles 
        the events.
        @type discoveryListener: L{DiscoveryListener<src.discovery.DiscoveryListener>}
        
        @param discoveryFilter: The DiscoveryFilter to specify criteria of interested the 
        root Network Element and its ONEP neighbors.
        @type discoveryFilter : L{DiscoveryFilter<src.discovery.DiscoveryFilter>}
        
        @raise OnepIllegalArgumentException: The exception is thrown when 
        discoveryListener or filter are not valid
        @raise OnepConnectionException: The exception is thrown when the 
        connection to a network element has failed.
        @raise OnepRemoteProcedureException: The exception is thrown when an 
        error has occurred in the remote procedure call made to a network 
        element.
        @raise OnepException: The exception is thrown when an internal error 
        occurs.
        
        """
        if self.session_handle == None or self.session_handle._id == 0:
            raise OnepConnectionException('Session is disconnected')
        if discoveryListener == None:
            raise OnepIllegalArgumentException('discoveryListener', 'None')
        if discoveryFilter == None:
            raise OnepIllegalArgumentException('discoveryFilter', 'None')
        try:
            eventProp = self.discovery_client.SrvcDiscoveryEvent_registerIDL(self.session_handle._id, discoveryFilter.type, discoveryFilter.name, discoveryFilter.state)
            if eventProp != None:
                self.event_manager.add_listener(eventProp.eventHandle, discoveryListener, clientData)
                self.log.debug('Registered Discovery listener with event handle : ' + str(eventProp.eventHandle))
                return eventProp.eventHandle
            raise OnepException('Internal error while registering the Listener')
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e.message, e)



    def remove_discovery_listener(self, eventHandle):
        """
        Removes the given discovery listener.
        
        @param eventHandle: ID returned as part of
                   {@link #addDiscoveryListener(DiscoveryListener, DiscoveryFilter, Object)}
                   call.
        @raise OnepIllegalArgumentException:
                    The exception is thrown when eventHandle is not valid.
        @raise OnepConnectionException:
                    The exception is thrown when the connection to a network element
                    has failed.
        @raise OnepRemoteProcedureException:
                    The exception is thrown when an error has occurred in the
                    remote procedure call made to a network element.
        """
        self.event_manager.remove_listener(eventHandle)



    def get_connect_time(self):
        """
        This method for internal use only
        """
        if self.state == self.OnepSessionState.ONEP_STATE_CONNECTED:
            return self.connect_time
        else:
            return None



    def get_disconnect_time(self):
        """
        This method for internal use only
        """
        if self.state == self.OnepSessionState.ONEP_STATE_DISCONNECTED:
            return self.disconnect_time
        else:
            return None



    def __str__(self):
        """
        Gets a string representation of the NetworkElement.
        
        The toString method for the class NetworkElement returns the string
        representation of the NetworkElement object instance and the element
        properties.
        
        @return: A string representation of the NetworkElement object.
        """
        if self.host_address == None:
            addr = ''
        else:
            addr = self.host_address
        sb = '\nNetworkElement [ ' + addr + ' ]\n'
        if self.properties != None:
            sb += self.properties.content_string
        return sb.__str__()



    def get_reconnect_timer(self):
        """
        This method for internal use only
        """
        return self.session_handle.sessionProp.sessionConfig.reconnectTimer



    def get_location(self):
        """
        Gets a Location object associated with the network element. The Location
        object can be used to access all types of location information.
        
        @return: The Location object for the network element, or null if there is
                no location information available.
        
        @raise OnepConnectionException:
                    The exception is thrown when the connection to a network element
                    has failed.
        @raise OnepRemoteProcedureException:
                    The exception is thrown when an error has occurred in the
                    remote procedure call made to a network element.
        """
        if self.session_handle == None or self.session_handle._id == 0:
            raise OnepConnectionException('Session is disconnected')
        locIdl = None
        try:
            locIdl = self.location_client.Location_getLocationIDL(location.LocationHandleType.LocElementHandle, self.session_handle._id)
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e.message, e)
        if locIdl != None:
            loc = location.fromIDL(locIdl)
            loc._set_element_attachment(self)
            return loc
        else:
            return 



    def set_location(self, loc):
        """
        Sets location information for the network element.
        
        Sets location information for the network element with the information in
        the input Location parameter.
        
        @param loc: The location information to be associated with the network
                   element.
        @type loc: L{Location<onep.location.location.Location>}
        
        @raise OnepIllegalArgumentException:
                    The exception is thrown if the Location object is invalid.
        @raise OnepConnectionException:
                    The exception is thrown when the connection to a network element
                    has failed.
        @raise OnepRemoteProcedureException:
                    The exception is thrown when an error has occurred in the
                    remote procedure call made to a network element.
        """
        if loc == None:
            raise OnepIllegalArgumentException('loc', 'None')
        if self.session_handle == None or self.session_handle._id == 0:
            raise OnepConnectionException('Session is disconnected')
        try:
            self.location_client.Location_setLocationIDL(location.LocationHandleType.LocElementHandle, self.session_handle._id, loc.toIDL())
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e.message, e)



    def get_fru_list(self):
        """
        Returns the collection of the Field Replaceable Unit (FRU)
        
        @return: A collection of FRU on the network element, if it is available.
                Otherwise, NULL is returned.
        @raise OnepConnectionException:
                    The exception is thrown when the connection to a network element
                    has failed.
        @raise OnepRemoteProcedureException:
                    The exception is thrown when an error has occurred in the
                    remote procedure call made to a network element
        """
        if self.session_handle == None or self.session_handle._id == 0:
            raise OnepConnectionException('Session is disconnected')
        try:
            fru_idl_list = self.api_client.NetworkElement_getFruListIDL(self.session_handle._id)
            if fru_idl_list == None or len(fru_idl_list) == 0:
                return 
            else:
                fru_list = []
                for fru_idl in fru_idl_list:
                    fru = FRU(self, fru_idl.slot, fru_idl.alarm_type, fru_idl.product_id, fru_idl.serial_no, fru_idl.part_no, fru_idl.sw_version, fru_idl.fw_version, fru_idl.hw_version)
                    fru_list.append(fru)

                return fru_list
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e.message, e)



    def create_syslog_message(self, severity, message):
        """
                Creates a syslog message on the network element
        
                Creates a syslog message on the network element of specified:
                  - Severity and message body.  The facility is fixed at "onePK".  
                  - The mnemonic is the application name.
                
                @param severity:
                           The severity of the message. 
                @param message:
                           The body of the message.
                @raise OnepIllegalArgumentException:
                            The exception is thrown if the Location object is invalid.
                @raise OnepConnectionException:
                            The exception is thrown when the connection to a network element
                            has failed.
                @raise OnepRemoteProcedureException:
                            The exception is thrown when an error has occurred in the
                            remote procedure call made to a network element.
                """
        if message == None:
            raise OnepIllegalArgumentException('message', 'None')
        if self.session_handle == None or self.session_handle._id == 0:
            raise OnepConnectionException('Session is disconnected')
        try:
            self.api_client.NetworkElement_createSyslogMsgIDL(self.session_handle._id, severity, message)
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e.message, e)



    def delete_all_policies(self):
        """
        """
        try:
            self.policy_client.deleteAllPolicies_IDL(self.session_handle._id)
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e.message, e)



    def install_cli_ext(self, xsd_contents, config_domain, overwrite):
        """
        This method installs an Application Management Data XSD (ClI extension)
        on the network element.
        
        @param xsd_contents: The string-value containing the contents of the XSD to be installed.
        @type xsd_contents: C{str}
        
        @param config_domain: The configuration domain associated with the installation.
            If the application is in a container, this parameter is ignored, and the container name is used.
        @type config_domain: C{str}
        
        @param overwrite: If TRUE the existing XSD is overwritten and old data is migrated.
            If FALSE, this XSD is maintained as a separate version.
        @type overwrite: C{boolean}
        
        @raise OnepRemoteProcedureException: System failure to serve the request.
                Please check error message for more details.
        @raise OnepConnectionException: Transport error, may need to reset the connection.
                Please, check the error message for more details.     
        @raise OnepIllegalArgumentException: This exception is thrown if any input parameter is invalid.
        """
        validate(xsd_contents, str)
        validate(config_domain, str)
        validate(overwrite, bool)
        ovrwte = int(overwrite)
        try:
            self.applmgmt_client.ApplManagedData_installXsdIDL(self.session_handle._id, xsd_contents, config_domain, ovrwte)
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e.message, e)



    def uninstall_cli_ext(self, app_name, app_version, config_domain):
        """
        This method uninstalls a ClI extension on the specified network
        element.
        
        @param app_name: The string-value of the application name to be uninstalled. 
        @type app_name: C{str}
        
        @param app_version: The string-value of the application version to be uninstalled. 
        @type app_version: C{str}
        
        @param config_domain: The string-value of the configuration domain to be uninstalled.
        @type config_domain: C{str}
        
        @raise OnepRemoteProcedureException: System failure to serve the request.
                Please check error message for more details.
        @raise OnepConnectionException: Transport error, may need to reset the connection.
                Please check the error message for more details.     
        @raise OnepIllegalArgumentException: This exception is thrown if any input parameter is invalid.
        """
        validate(app_name, str)
        validate(app_version, str)
        validate(config_domain, str)
        try:
            self.applmgmt_client.ApplManagedData_uninstallXsdIDL(self.session_handle._id, app_name, app_version, config_domain)
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e.message, e)



    def is_xsd_installed(self, app_name, app_version, config_domain):
        """
        This method queries for a ClI extension on the specified network element.
         
        @param app_name: The string-value of the application name to be queried. 
        @type app_name: C{str}
        
        @param app_version: The string-value of the application version to be queried. 
        @type app_version: C{str}
        
        @param config_domain: The string-value of the configuration domain to be queried.
        @type config_domain: C{str}
        
        @raise OnepRemoteProcedureException: System failure to serve the request. 
                Please check error message for more details.
        @raise OnepConnectionException: Transport error, may need to reset the connection. 
                Please check the error message for more details.     
        @raise OnepIllegalArgumentException: This exception is thrown if any input parameter is invalid.
        """
        validate(app_name, str)
        validate(app_version, str)
        validate(config_domain, str)
        try:
            result = self.applmgmt_client.ApplManagedData_isXsdInstalledIDL(self.session_handle._id, app_name, app_version, config_domain)
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e.message, e)
        return bool(result)



NetworkElement.OnepSessionState = enum('ONEP_STATE_DISCONNECTED', 'ONEP_STATE_CONNECTING', 'ONEP_STATE_CONNECTED', 'ONEP_STATE_RECONNECTING')
NetworkElement.OnepSyslogSeverity = enum('ONEP_SYSLOG_EMERGENCY', 'ONEP_SYSLOG_ALERT', 'ONEP_SYSLOG_CRITICAL', 'ONEP_SYSLOG_ERROR', 'ONEP_SYSLOG_WARNING', 'ONEP_SYSLOG_NOTICE', 'ONEP_SYSLOG_INFO', 'ONEP_SYSLOG_DEBUG')
NetworkElement.log = None

# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:21:10 IST
