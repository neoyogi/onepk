# 2015.02.05 17:18:06 IST
import threading
import collections
import Queue
import pdb
from onep.thrift.Thrift import *
from onep.thrift.Thrift import TProcessor
from onep.thrift.transport import TTransport
from onep.thrift.transport import TSocket
from onep.thrift.protocol import TBinaryProtocol, TProtocol
from onep.thrift.transport.TTransport import TTransportException
import logging
from Shared.ttypes import ExceptionIDL
from onep.core.exception.OnepConnectionException import OnepConnectionException
from onep.core.exception.OnepRemoteProcedureException import OnepRemoteProcedureException
from onep.core.exception.OnepIllegalArgumentException import OnepIllegalArgumentException
from onep.core.exception.OnepRemoteProcedureException import OnepRemoteProcedureException
from onep.core.exception.OnepConnectionException import OnepConnectionException
from onep.core.exception.OnepException import OnepException
from onep.core.util.OnepConstants import OnepConstants
from onep.core.util.OnepStatus import *
from onep.core.event.EventDispatcher import EventDispatcher
from onep.core.event.KeepaliveMonitor import KeepaliveMonitor
from onep.element.SessionProperty import SessionProperty
from onep.element.SessionConfig import SessionConfig
from onep.element.SyslogEvent import SyslogEvent
from onep.element.OIREvent import OIREvent
from onep.element.OIRFilter import OIRFilter
from onep.element.CLIEvent import CLIEvent
from onep.element.ApplEvent import ApplEvent
from onep.applmgmt.ApplicationCliData import ApplicationCliData
from onep.interfaces.NetworkInterface import NetworkInterface
from onep.interfaces.InterfaceStateEvent import InterfaceStateEvent
from onep.interfaces.InterfaceStatisticsEvent import InterfaceStatisticsEvent
from onep.interfaces.InterfaceCreateDeleteEvent import InterfaceCreateDeleteEvent
from onep.interfaces.InterfaceAddressChangeEvent import InterfaceAddressChangeEvent
from onep.interfaces.interfacestatspoll import InterfaceStatisticsPollEvent
from onep.interfaces.InterfaceMtuEvent import InterfaceMtuEvent
from onep.interfaces.InterfaceBandwidthEvent import InterfaceBandwidthEvent
from onep.interfaces.InterfaceVlanEvent import InterfaceVlanEvent
from onep.interfaces.InterfaceVrfEvent import InterfaceVrfEvent
from onep.interfaces.NetworkPrefix import NetworkPrefix
from onep.routing.L3UnicastScope import *
from onep.routing.L3UnicastNextHop import L3UnicastNextHop
from onep.routing.L3UnicastRoute import *
from onep.routing.Route import *
from onep.location import location
import onep.NetworkEventIDL.NetworkEventIDL
import onep.TopologyEventIDL.TopologyEventIDL
import onep.LocationEventIDL.LocationEventIDL
import onep.RoutingEventIDL.RoutingEventIDL
from onep.vty.VtyListener import VtyListener
from onep.vty.VtyData import VtyData
from onep.cdp.CDPEvent import CDPEvent
from onep.ContainerServicesEventIDL import ContainerServicesEventIDL
try:
    from onep.container.csevent import *
except ImportError:
    from onep.ContainerServicesIDL.ttypes import *
    from onep.ContainerServicesEventIDL.ttypes import *
from onep.policyservice.policymap import PolicySubmitEvent
from onep.policyservice.policymap import PolicyActivateEvent
from onep.policyservice.policymap import PolicyStatsEvent
from onep.policyservice.classmap import ClassEvent
from onep.PolicyEventIDL import PolicyEventIDL

class EventManager(threading.Thread):
    """
        This class is for internal use only
    
        """


    def __init__(self, networkElement, protocol):
        """
            For internal use only
        
            """
        super(EventManager, self).__init__()
        self.log = logging.getLogger(__name__)
        if networkElement != None and networkElement.session_handle != None and networkElement.session_handle.sessionProp != None:
            self.sessionProp = networkElement.session_handle.sessionProp
        else:
            self.sessionProp = SessionProperty(SessionConfig(None), networkElement)
        self.element = networkElement
        self.element_evt_processor = onep.NetworkEventIDL.NetworkEventIDL.Processor(self)
        self.topology_evt_processor = onep.TopologyEventIDL.TopologyEventIDL.Processor(self)
        self.location_evt_processor = onep.LocationEventIDL.LocationEventIDL.Processor(self)
        self.routing_evt_processor = onep.RoutingEventIDL.RoutingEventIDL.Processor(self)
        self.bulk_evt_processor = PolicyEventIDL.Processor(self)
        self.cs_evt_processor = ContainerServicesEventIDL.Processor(self)
        self.event_queue = collections.deque(maxlen=self.sessionProp.eventQueueSize)
        self.dedicated_event_queue_map = None
        self.dedicated_dispatcher_map = None
        self.listener_map = {}
        self.listener_client_data_map = {}
        self.vty_listener_map = {}
        self.vty_listener_client_data_map = {}
        self.bulk_listener_map = {}
        self.evt_protocol = None
        self.dispatchers = []
        self.terminated = False
        self.ka_monitor = None
        self.event_id = 200
        self.start_listeners(protocol)



    def start_listeners(self, protocol):
        """
            For internal use only
        
            """
        self.evt_protocol = protocol
        nThreads = self.sessionProp.eventThreadPool
        self.dispatchers = [None] * nThreads
        i = 0
        while i < nThreads:
            self.dispatchers[i] = EventDispatcher()
            self.dispatchers[i].element = self.element
            self.dispatchers[i].event_queue = self.event_queue
            self.dispatchers[i].start()
            i += 1

        if self.ka_monitor != None:
            logging.debug('Dangling KeepAlive timer found active. Terminating it to start new.')
            self.ka_monitor.stop_monitor()
            self.ka_monitor = None
        self.ka_monitor = KeepaliveMonitor(self.element)
        self.daemon = True
        self.start()



    def add_keepalive(self):
        if self.ka_monitor == None:
            logging.debug('Starting KeepAlive timer.')
            self.ka_monitor = KeepaliveMonitor(self.element)



    def remove_keepalive(self):
        if self.ka_monitor != None:
            logging.debug('Terminating KeepAlive timer.')
            self.ka_monitor.stop_monitor()
            self.ka_monitor = None



    def run(self):
        """
            For internal use only
        
            """
        try:
            try:
                while not self.terminated:
                    try:
                        (name, type, seqid,) = self.evt_protocol.readMessageBegin()
                    except Exception as e:
                        if self.terminated:
                            self.log.debug('Exception after PL initiated disconnect ' + str(e))
                            break
                        else:
                            raise 
                    if not self.terminated:
                        if name in self.topology_evt_processor._processMap:
                            result = self.topology_evt_processor._processMap[name](self.topology_evt_processor, seqid, self.evt_protocol, self.evt_protocol)
                        elif name in self.location_evt_processor._processMap:
                            result = self.location_evt_processor._processMap[name](self.location_evt_processor, seqid, self.evt_protocol, self.evt_protocol)
                        elif name in self.routing_evt_processor._processMap:
                            result = self.routing_evt_processor._processMap[name](self.routing_evt_processor, seqid, self.evt_protocol, self.evt_protocol)
                        elif name in self.element_evt_processor._processMap:
                            result = self.element_evt_processor._processMap[name](self.element_evt_processor, seqid, self.evt_protocol, self.evt_protocol)
                        elif name in self.cs_evt_processor._processMap:
                            result = self.cs_evt_processor._processMap[name](self.cs_evt_processor, seqid, self.evt_protocol, self.evt_protocol)
                        elif name in self.bulk_evt_processor._processMap:
                            result = self.bulk_evt_processor._processMap[name](self.bulk_evt_processor, seqid, self.evt_protocol, self.evt_protocol)
                        else:
                            self.evt_protocol.skip(TType.STRUCT)
                            self.evt_protocol.readMessageEnd()
                            x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % name)
                            self.evt_protocol.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
                            x.write(self.evt_protocol)
                            self.evt_protocol.writeMessageEnd()
                            self.evt_protocol.trans.flush()
                    self.log.debug('Event Manager Message: ' + name)

            except TTransportException as e:
                if not self.terminated:
                    self.log.error('Event channel listener error')
                else:
                    self.log.debug('Exiting event channel listener thread')
            except TException as e:
                if not self.terminated:
                    self.log.error('Event channel listener error')
                else:
                    self.log.debug('Exiting event channel listener thread')
        except ExceptionIDL as e:
            self.log.debug('Event channel terminated')
            if not self.terminated:
                self.log.error('Event channel listener error')
                raise e
        finally:
            if not self.terminated:
                self.element.disconnect('EventManager triggered disconnect')



    def get_event_listener(self, eventHandle):
        """
            For internal use only
        
            """
        return self.listener_map[eventHandle]



    def get_event_listener_client_data(self, eventHandle):
        """
            For internal use only
        
            """
        return self.listener_client_data_map[eventHandle]



    def get_vty_event_listener(self, execHandle):
        """
            For internal use only
        
            """
        return self.vty_listener_map[execHandle]



    def get_vty_event_listener_client_data(self, execHandle):
        """
            For internal use only
        
            """
        return self.vty_listener_client_data_map[execHandle]



    def add_listener(self, eventHandle, listener, clientData):
        """
            For internal use only
        
            """
        self.listener_map[eventHandle] = listener
        self.listener_client_data_map[eventHandle] = clientData



    def add_vty_listener(self, execHandle, listener, clientData):
        """
            For internal use only
        
            """
        self.vty_listener_map[execHandle] = listener
        self.vty_listener_client_data_map[execHandle] = clientData



    def selective_queue_flush(self, queue, event_handle):
        """
                For internal use only
        
                """
        self.log.debug('Selective flush of event ' + str(event_handle))
        [ queue.remove(obj) for obj in list(queue) if obj.event_handle == event_handle ]



    def remove_listener(self, eventHandle):
        """
            For internal use only
        
            """
        if eventHandle == None or eventHandle not in self.listener_map or eventHandle not in self.listener_client_data_map or self.listener_map[eventHandle] == None:
            raise OnepIllegalArgumentException('eventHandle', str(eventHandle))
        self.request_event_unregister(eventHandle)
        self.selective_queue_flush(self.event_queue, eventHandle)
        self.listener_map[eventHandle] = None
        self.listener_client_data_map[eventHandle] = None



    def remove_vty_listener(self, execHandle):
        """
            For internal use only
        
            """
        self.vty_listener_map[execHandle] = None
        self.vty_listener_client_data_map[execHandle] = None



    def request_event_unregister(self, eventHandle):
        """
            For internal use only
        
            """
        try:
            self.element.api_client.Event_unregisterIDL(self.element.session_handle._id, eventHandle)
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e.message, e)



    def OnepEvent_applEventIDL(self, sessionHandle, eventHandle, applID, type_, data1, data2, data3, data4):
        """
            For internal use only
        
            """
        self.log.debug('Application EventIDL: session Handle = ' + str(sessionHandle) + ' eventHandle = ' + str(eventHandle) + ' applID = ' + str(applID) + ' type = ' + str(type_))
        if self.terminated:
            return 
        event = ApplEvent(self.element, applID, type_, data1, data2, data3, data4, eventHandle)
        self.enque(event)



    def OnepEvent_configNotificationIDL(self, sessionHandle, cfgDataName, cfgDataValue):
        """
            For internal use only
        
            """
        self.log.debug('configNotificationIDL: session Handle = ' + str(sessionHandle) + ' cfgDataName = ' + str(cfgDataName) + ' cfgDataValue = ' + str(cfgDataValue))
        if self.terminated:
            return 
        if self.element == None or self.element.config_listener == None:
            return 
        event = ApplicationCliData(self.element, cfgDataName, cfgDataValue, ApplicationCliData.OnepAppCLIDataType.ONEP_APP_CLI_TYPE_CONFIG)
        self.enque(event)



    def OnepEvent_showDataIDL(self, sessionHandle, showDataName):
        """
            For internal use only
        
            """
        self.log.debug('showDataIDL: session Handle = ' + str(sessionHandle) + ' show_data_name = ' + str(showDataName))
        if self.terminated:
            return 
        if self.element == None or self.element.exec_listener == None:
            return 
        cliData = ApplicationCliData(self.element, showDataName, '', ApplicationCliData.OnepAppCLIDataType.ONEP_APP_CLI_TYPE_EXEC)
        self.enque(cliData)



    def OnepEvent_syslogEventIDL(self, sessionHandle, eventHandle, msgCount, priority, message):
        """
            For internal use only
        
            """
        self.log.debug('syslogEventIDL: session Handle = ' + str(sessionHandle) + ' eventHandle = ' + str(eventHandle) + ' msgCount = ' + str(msgCount) + ' priority = ' + str(priority) + ' message  = ' + message)
        if self.terminated:
            return 
        event = SyslogEvent(self.element, eventHandle, msgCount, priority, message)
        self.enque(event)



    def OnepEvent_oirEventIDL(self, sessionHandle, eventHandle, slot, oirType):
        """
            For internal use only
        
            """
        self.log.debug('oirEventIDL: session Handle = ' + str(sessionHandle) + ' eventHandle = ' + str(eventHandle) + ' slot = ' + str(slot) + ' oirType = ' + str(oirType))
        if self.terminated:
            return 
        try:
            event = OIREvent(self.element, eventHandle, slot, OIRFilter.OIRType.enumval(oirType))
            self.enque(event)
        except OnepIllegalArgumentException as e:
            self.log.error('AL to PL enum conversion failed')



    def OnepEvent_cliEventIDL(self, sessionHandle, eventHandle, msgCount, tty, errorCode, sync, message):
        """
            For internal use only
        
            """
        self.log.debug('cli EventIDL: session Handle = ' + str(sessionHandle) + ' eventHandle = ' + str(eventHandle) + ' msgCount = ' + str(msgCount) + ' tty = ' + str(tty) + ' errorCode =' + str(errorCode) + 'sync = ' + str(sync) + ' message  = ' + message)
        if self.terminated:
            return 
        event = CLIEvent(self.element, eventHandle, tty, msgCount, sync, message)
        self.enque(event)



    def OnepEvent_cdpEventIDL(self, sessionHandle, eventHandle, xosHandle, name, type_, notifyType, neighborName, holdTime, mgmtDomain, platform, version, capabilities, addresses, neighborIntfName):
        """
            For internal use only
        
            """
        self.log.debug('cdp EventIDL: session Handle = ' + str(sessionHandle) + ' eventHandle = ' + str(eventHandle) + ' NetworkInterface = ' + str(name) + ' notifyType = ' + str(notifyType) + ' neighbor  = ' + str(neighborName) + 'hold time = ' + str(holdTime) + 'vtp domain = ' + str(mgmtDomain) + 'platform = ' + str(platform) + 'version = ' + str(version) + 'capabilitites = ' + str(capabilities) + 'neighborIntfName = ' + str(neighborIntfName))
        if self.terminated:
            return 
        event = None
        try:
            interface = NetworkInterface(self.element, name, type_, xosHandle)
            event = CDPEvent(self.element, eventHandle, interface, notifyType, neighborName, holdTime, mgmtDomain, platform, version, capabilities, addresses, neighborIntfName)
            self.enque(event)
        except OnepIllegalArgumentException as e:
            self.log.error('AL to PL enum conversion failed : ' + str(e.message))



    def OnepEvent_InterfaceStatisticsPollEventIDL(self, sessionHandle, eventHandle, intfXosHandle, intfName, intfType, intfstats):
        """
            For internal use only
        
            """
        if self.terminated:
            return 
        try:
            self.log.debug('InterfaceStatisticsPollEvent: session Handle = ' + str(sessionHandle) + ' eventHandle = ' + str(eventHandle) + ' interface name = ' + str(intfName) + ' intefaceType = ' + str(intfType) + ' xos Handle = ' + str(intfXosHandle))
            ni = NetworkInterface(self.element, intfName, intfType, intfXosHandle)
            event = InterfaceStatisticsPollEvent(self.element, eventHandle, ni, intfstats)
            self.enque(event)
        except OnepIllegalArgumentException as e:
            self.log.error('AL to PL conversion failed')



    def OnepEvent_InterfaceAddrChangeEventIDL(self, sessionHandle, eventHandle, intfXosHandle, intfName, intfType, oldAddress, newAddress, oldPrefix, newPrefix):
        """
            For internal use only
        
            """
        if self.terminated:
            return 
        try:
            if oldPrefix == None or newPrefix == None:
                oaddr_string = oldAddress
                naddr_string = newAddress
                oldPrefixLen = 0
                newPrefixLen = 0
            else:
                oaddr_string = oldPrefix.addr
                naddr_string = newPrefix.addr
                oldPrefixLen = oldPrefix.prefix_len
                newPrefixLen = newPrefix.prefix_len
            self.log.debug('InterfaceAddressChangeEventIDL: session Handle = ' + str(sessionHandle) + ' eventHandle = ' + str(eventHandle) + ' interface name = ' + str(intfName) + ' intefaceType = ' + str(intfType) + ' xos Handle = ' + str(intfXosHandle) + ' oldAddress = ' + str(oaddr_string) + ' newAddress = ' + str(naddr_string))
            ni = NetworkInterface(self.element, intfName, intfType, intfXosHandle)
            event = InterfaceAddressChangeEvent(self.element, eventHandle, ni, oaddr_string, naddr_string, oldPrefixLen, newPrefixLen)
            self.enque(event)
        except OnepIllegalArgumentException as e:
            self.log.error('AL to PL enum conversion failed')



    def OnepEvent_InterfaceCTXEnableDisableEventIDL(self, sessionHandle, eventHandle, intfXosHandle, intfName, intfType, oprType):
        """
            For internal use only
        
            """
        pass



    def OnepEvent_InterfaceMtuEventIDL(self, sessionHandle, eventHandle, xosHandle, intfType, intfName, mtu):
        """
        For internal use only
        
        """
        msg = 'InterfaceMtuEventIDL: session Handle = ' + str(sessionHandle) + ' eventHandle = ' + str(eventHandle)
        msg += ' xosHandle = ' + str(xosHandle) + ' intfType= ' + str(intfType)
        msg += ' shortName = ' + str(intfName) + ' mtu = ' + str(mtu)
        self.log.debug(msg)
        if self.terminated:
            return 
        try:
            ni = NetworkInterface(self.element, intfName, intfType, xosHandle)
            event = InterfaceMtuEvent(self.element, eventHandle, ni, mtu)
            self.enque(event)
        except OnepIllegalArgumentException as e:
            self.log.error('AL to PL enum conversion failed')



    def OnepEvent_InterfaceVrfEventIDL(self, sessionHandle, eventHandle, xosHandle, intfType, intfName, vrf, vrfEventType):
        """
        For internal use only
        
        """
        msg = 'InterfaceVrfEventIDL: session Handle = ' + str(sessionHandle) + ' eventHandle = ' + str(eventHandle)
        msg += ' xosHandle = ' + str(xosHandle) + ' intfType= ' + str(intfType)
        msg += ' shortName = ' + intfName + ' vrf = ' + str(vrf)
        msg += ' vrfEventType= ' + str(vrfEventType)
        self.log.debug(msg)
        if self.terminated:
            return 
        try:
            ni = NetworkInterface(self.element, intfName, intfType, xosHandle)
            event = InterfaceVrfEvent(self.element, eventHandle, ni, vrfEventType)
            self.enque(event)
        except OnepIllegalArgumentException as e:
            self.log.error('AL to PL enum conversion failed')



    def OnepEvent_InterfaceVlanEventIDL(self, sessionHandle, eventHandle, xosHandle, intfType, intfName, vlan, vlanEventType):
        """
        For internal use only
        
        """
        msg = 'InterfaceVlanEventIDL: session Handle = ' + str(sessionHandle) + ' eventHandle = ' + str(eventHandle)
        msg += ' xosHandle = ' + str(xosHandle) + ' intfType= ' + str(intfType)
        msg += ' shortName = ' + intfName + ' vlanEventType = ' + str(vlanEventType)
        self.log.debug(msg)
        if self.terminated:
            return 
        try:
            ni = NetworkInterface(self.element, intfName, intfType, xosHandle)
            event = InterfaceVlanEvent(self.element, eventHandle, ni, vlanEventType, vlan)
            self.enque(event)
        except OnepIllegalArgumentException as e:
            self.log.error('AL to PL enum conversion failed')



    def OnepEvent_InterfaceBandwidthEventIDL(self, sessionHandle, eventHandle, xosHandle, intfType, intfName, bandwidth, is_tx = None):
        """
        For internal use only
        
        """
        msg = 'InterfaceBandwidthEventIDL: session Handle = ' + str(sessionHandle) + ' eventHandle = ' + str(eventHandle)
        msg += ' xosHandle = ' + str(xosHandle) + ' intfType= ' + str(intfType)
        msg += ' shortName = ' + intfName + ' Bandwidth = ' + str(bandwidth) + ' Is TX = ' + str(is_tx)
        self.log.debug(msg)
        if self.terminated:
            return 
        try:
            ni = NetworkInterface(self.element, intfName, intfType, xosHandle)
            event = InterfaceBandwidthEvent(self.element, eventHandle, ni, bandwidth, is_tx)
            self.enque(event)
        except OnepIllegalArgumentException as e:
            self.log.error('AL to PL enum conversion failed')



    def OnepEvent_InterfaceCreateDeleteEventIDL(self, sessionHandle, eventHandle, intfXosHandle, intfName, intfType, isCreated, isOir):
        """
            For internal use only
        
            """
        self.log.debug('InterfaceCreateDeleteEventIDL: session Handle = ' + str(sessionHandle) + ' eventHandle = ' + str(eventHandle) + ' interface name = ' + str(intfName) + ' intefaceType' + str(intfType) + ' xos Handle = ' + str(intfXosHandle) + ' isCreated =' + str(isCreated))
        if self.terminated:
            return 
        try:
            ni = NetworkInterface(self.element, intfName, intfType, intfXosHandle)
            event = InterfaceCreateDeleteEvent(self.element, eventHandle, ni, isCreated, isOir)
            self.enque(event)
        except OnepIllegalArgumentException as e:
            self.log.error('AL to PL enum conversion failed')



    def OnepEvent_appLogLevelChangeIDL(self, sessionHandle, level, dummy):
        """
            For internal use only
        
            """
        pass



    def OnepEvent_InterfaceStateEventIDL(self, sessionHandle, eventHandle, xosHandle, intfType, stateType, intfState, shortName, link = None, lineproto = None):
        """
            For internal use only
        
            """
        tmp = 'Interface State change event received:\n event Handle  ' + str(eventHandle)
        tmp += '\n xos handle = ' + str(xosHandle) + '\n interface type = ' + str(intfType)
        tmp += '\n event type = ' + str(stateType) + '\n interface state type = ' + str(intfState)
        tmp += '\n short name = ' + str(shortName)
        tmp += '\n link state type = ' + str(link) + '\n lineproto state type = ' + str(lineproto)
        self.log.debug(tmp)
        try:
            ni = NetworkInterface(self.element, shortName, intfType, xosHandle)
            event = InterfaceStateEvent(self.element, eventHandle, ni, stateType, intfState, link, lineproto)
            self.enque(event)
        except Exception as e1:
            self.log.error('AL to PL enum conversion failed')



    def OnepEvent_InterfaceStatisticsEventIDL(self, sessionHandle, eventHandle, xosHandle, intfType, parameter, isIncrement, isExitEvent, value, deltaValue, shortName):
        """
            For internal use only
        
            """
        tmp = 'Interface Statistics change event received:\n event Handle  ' + str(eventHandle)
        tmp += '\n xos handle = ' + str(xosHandle) + '\n interface type = ' + str(intfType)
        tmp += '\n short name = ' + str(shortName) + ' isIncrement ' + str(isIncrement) + ' value  ' + str(value)
        tmp += '\ndeltaValue' + str(deltaValue) + '\nisExitevent ' + str(isExitEvent)
        self.log.debug(tmp)
        ni = NetworkInterface(self.element, shortName, intfType, xosHandle)
        event = InterfaceStatisticsEvent(self.element, eventHandle, ni, parameter, isIncrement, value, deltaValue, isExitEvent)
        self.enque(event)



    def OnepEvent_srvcDiscoveryEventIDL(self, sessionHandle, eventHandle, discoveryType, ssName, ssState, ssVersion, ipAddress):
        """
            For internal use only
        
            """
        from onep.discovery.DiscoveryEvent import DiscoveryEvent
        try:
            self.log.debug('Service stat change event received: event Handle = ' + str(eventHandle) + ' discovery type: ' + str(discoveryType) + ' ssName : ' + str(ssName) + ' ssState: ' + str(ssState) + ' ssVersion: ' + str(ssVersion) + ' ipAddress: ' + str(ipAddress))
            inetAddr = None
            try:
                if ipAddress is not None:
                    inetAddr = ipAddress.addr
            except Exception as e:
                self.log.warning('Unknown host')
            event = DiscoveryEvent(self.element, eventHandle, discoveryType, ssName, ssState, ssVersion, inetAddr)
            self.enque(event)
        except OnepException as e1:
            self.log.error('AL to PL enum conversion failed')



    def OnepEvent_locationChangeEventIDL(self, sessionHandle, eventHandle, subtype, changer, locationHandle):
        """
            For internal use only
        
            """
        self.log.debug('locationChangeEventIDL: session Handle = ' + str(sessionHandle) + ' eventHandle = ' + str(eventHandle) + ' locationHandle = ' + str(locationHandle))
        if self.terminated:
            return 
        event = location.LocationChangeEvent(self.element, eventHandle, location.Location._get_location_by_id(locationHandle), location.Location._convert_subtype_bitmast_to_list(subtype), changer)
        self.enque(event)



    def OnepEvent_vtyEventIDL(self, sessionHandle, execHandle, state, msgType, data):
        """
            For internal use only
        
            """
        self.log.debug('OnepEvent_vtyEventIDL: session Handle = ' + str(sessionHandle) + ' execHandle = ' + str(execHandle) + ' state = ' + str(state) + ' msgType = ' + str(msgType) + ' data = ' + data)
        if self.terminated:
            return 
        if self.get_vty_event_listener(execHandle) == None:
            return 
        event = VtyData(self.element, execHandle, state, msgType, data)
        self.enque(event)



    def OnepEvent_keepaliveHeartbeatIDL(self, sessionHandle):
        """
            For internal use only
        
            """
        self.log.debug('OnepEvent_keepaliveHeartbeatIDL: session Handle = ' + str(sessionHandle))
        self.ka_monitor.update_heatbeat_time()



    def OnepEvent_capStrIDL(self, sessionHandle, cap_name, cap_value):
        """
            For internal use only
        
            """
        self.log.debug('OnepEvent_capStringIDL: session Handle = ' + str(sessionHandle))



    def OnepEvent_capIntIDL(self, sessionHandle, cap_name, capabilty_value):
        """
            For internal use only
        
            """
        self.log.debug('OnepEvent_capIntIDL: session Handle = ' + str(sessionHandle))



    def OnepEvent_TopologyChangeEventIDL(self, session_id, event_handle, topology_key, event_type, outconfig, edge_idl_list):
        """
            For internal use only
        
            """
        from onep.topology.TopologyEvent import TopologyEvent
        from onep.topology.Node import Node
        from onep.topology.NodeConnector import NodeConnector
        from onep.topology.TopologyClass import TopologyClass
        from onep.topology.Edge import Edge
        dbg_buf = 'OnepEvent_TopologyChangeEventIDL: session Handle = ' + str(session_id) + ' eventHandle = ' + str(event_handle) + ' TopologyKey = ' + str(topology_key) + ' eventType = ' + str(event_type)
        self.log.debug(dbg_buf)
        if self.terminated:
            return 
        type_list = TopologyEvent.convert_type_bitmip_to_list(event_type)
        edge_list = []
        tpl_type = outconfig.Type
        node_type = Node.NodeType.INVALID_NODE_TYPE
        conn_type = NodeConnector.NodeConnectorType.ONEP_INVALID_CONNECTOR_TYPE
        if tpl_type == TopologyClass.TopologyType.CDP:
            node_type = Node.NodeType.CDP_NODE
            conn_type = NodeConnector.NodeConnectorType.ONEP_CDP_CONNECTOR
        for edge_idl in edge_idl_list:
            if edge_idl != None:
                edge_list.append(Edge._from_out_idl(edge_idl, node_type, conn_type))

        event = TopologyEvent(self.element, event_handle, topology_key, type_list, edge_list)
        self.enque(event)



    def OnepEvent_ContainerSrvChangeEventIDL(self, sessionHandle, eventtype, adding, mask, macid, addr):
        """
            For internal use only
        
            """
        self.log.debug('ContainerEventChangeIDL: session Handle = ' + str(sessionHandle) + ' eventtype = ' + str(eventtype) + ' adding = ' + str(adding))
        if self.terminated or self.element is None:
            return 
        try:
            event = ContainerDataEvent(self.element, sessionHandle, eventtype, adding, mask, macid, addr)
            self.enque(event)
        except:
            self.log.debug('Unable to get container event changes.')



    def OnepEvent_ContainerSrv_ext_send_guest_updateIDL(self, sessionHandle, eventtype, update_info):
        if self.terminated or self.element is None:
            return 
        try:
            event = ContainerUpdateEvent(self.element, sessionHandle, eventtype, update_info)
            self.enque(event)
        except:
            self.log.debug('Unable to send guest update.')



    def OnepEvent_ContainerSrvInfoRequestIDL(self, sessionHandle, eventtype, transactionID, macid, extrainfo):
        """
            For internal use only
        
            """
        self.log.debug('Container Info Request IDL: session Handle = ' + str(sessionHandle) + ' event type = ' + str(eventtype) + ' transaction ID = ' + str(transactionID))
        if self.terminated or self.element == None:
            return 
        try:
            event = ContainerRequestEvent(self.element, sessionHandle, eventtype, transactionID, macid, extrainfo)
            self.enque(event)
        except:
            self.log.debug('Unable to provide container service request.')



    def OnepEvent_L3UcastRibRouteEventIDL(self, base, ribState):
        """
            For internal use only
        
            """
        from onep.routing.RIBRouteStateEvent import RIBRouteStateEvent
        if base == None:
            return 
        sessionHandle = base.sessionHandle
        eventHandle = base.eventHandle
        protocol = base.protocol
        safi = L3UnicastScope.SAFIType.UNICAST
        afi = 0
        if base.prefix != None and base.prefix.addr != None:
            afi = base.prefix.addr.family
        metric = base.metric
        distance = base.distance
        prefix = 0
        if base.prefix != None:
            prefix = base.prefix.prefix_len
        network = None
        if base.prefix != None and base.prefix.addr != None:
            network = base.prefix.addr.addr
        topoName = base.topoName
        vrfName = base.vrfName
        tagName = base.tagName
        if self.terminated:
            return 
        scope = None
        try:
            scope = L3UnicastScope(vrfName, afi, safi, topoName)
        except OnepIllegalArgumentException as e1:
            scope = None
        destNetwok = NetworkPrefix(network, prefix)
        nhList = set()
        if base.hopList != None:
            for nh_idl in base.hopList:
                nh = L3UnicastNextHop._from_idl(nh_idl, self.element)
                if nh != None:
                    nhList.add(nh)

        route = L3UnicastRoute(destNetwok, nhList, protocol, tagName, L3UnicastRoute.RouteType.NONE, distance, metric, Route.RouteErrorCode.NONE)
        event = RIBRouteStateEvent(self.element, eventHandle, scope, route, ribState)
        self.enque(event)



    def OnepEvent_L3UcastARTRouteEventIDL(self, base, artState):
        """
            For internal use only
        
            """
        from onep.routing.ARTRouteStateEvent import ARTRouteStateEvent
        if base == None:
            return 
        sessionHandle = base.sessionHandle
        eventHandle = base.eventHandle
        protocol = base.protocol
        safi = L3UnicastScope.SAFIType.UNICAST
        afi = 0
        if base.prefix != None and base.prefix.addr != None:
            afi = base.prefix.addr.family
        metric = base.metric
        distance = base.distance
        prefix = 0
        if base.prefix != None:
            prefix = base.prefix.prefix_len
        network = None
        if base.prefix != None and base.prefix.addr != None:
            network = base.prefix.addr.addr
        topoName = base.topoName
        vrfName = base.vrfName
        tagName = base.tagName
        if self.terminated:
            return 
        scope = None
        try:
            scope = L3UnicastScope(vrfName, afi, safi, topoName)
        except OnepIllegalArgumentException as e1:
            scope = None
        destNetwok = NetworkPrefix(network, prefix)
        nhList = set()
        if base.hopList != None:
            for nh_idl in base.hopList:
                nh = L3UnicastNextHop._from_idl(nh_idl, self.element)
                if nh != None:
                    nhList.add(nh)

        route = L3UnicastRoute(destNetwok, nhList, protocol, tagName, L3UnicastRoute.RouteType.NONE, distance, metric, Route.RouteErrorCode.NONE)
        event = ARTRouteStateEvent(self.element, eventHandle, scope, route, artState)
        self.enque(event)



    def AsyncMsg_L3UcastARTRouteUpdateAsyncIDL(self, base, scope_idl, op_idl_list, status):
        """
        For internal use only
        """
        from onep.routing.L3UnicastRouteOperation import L3UnicastRouteOperation
        from onep.routing.UpdateRouteResponse import UpdateRouteResponse
        if self.terminated:
            return OnepConstants.ERR_EVENTQ_FULL
        scope = L3UnicastScope._from_idl(scope_idl)
        op_list_out = list()
        for op_idl in op_idl_list:
            if op_idl != None:
                try:
                    route_op = L3UnicastRouteOperation(op_idl.opType, L3UnicastRoute._from_idl(op_idl.route, self.element), True)
                    op_list_out.append(route_op)
                except OnepIllegalArgumentException as e:
                    self.log.debug('Adding L3 unicast route operation failed')

        event = UpdateRouteResponse(self.element, base.asyncHandle, scope, op_list_out, status)
        return self.enque_dedicated(event, base.asyncHandle)



    def OnepEvent_RoutingServiceStatusEventIDL(self, session_handle, event_handle, routing_service, status):
        from onep.routing.RoutingServiceStatusEvent import RoutingServiceStatusEvent
        debug_msg = 'Session Handle ' + str(session_handle) + 'Event Handle' + str(event_handle) + 'Routing Service' + str(routing_service) + 'Status' + str(status)
        self.log.debug(debug_msg)
        if self.terminated:
            return 
        if status == 0:
            status_ = False
        else:
            status_ = True
        event = RoutingServiceStatusEvent(self.element, event_handle, routing_service, status_)
        self.enque(event)



    def OnepEvent_RoutingReplayRouteEventIDL(self, session_handle, event_handle, afi, safi, vrf_name, topo_name):
        from onep.routing.ReplayRouteEvent import ReplayRouteEvent
        debug_msg = 'OnepEvent_RoutingServiceStatusEventIDL: session Handle' + str(session_handle) + 'eventHandle' + str(event_handle) + 'afi' + str(afi) + 'safi' + str(safi) + 'vrfname' + vrf_name + 'toponame' + topo_name
        self.log.debug(debug_msg)
        if self.terminated:
            return 
        event = ReplayRouteEvent(self.element, event_handle, afi, safi, vrf_name, topo_name)
        self.enque(event)



    def Policy_submitPmapBulkAsyncRspIDL(self, base, result, type, reslist):
        """
                Internal use only
        
                Converts IDL classes to public classes for event listeners to use
        
                """
        self.log.debug('pmap bulk async submit event = ' + str(base) + ' ' + str(result) + ' ' + str(type) + ' ' + str(reslist))
        if self.terminated:
            return 
        event = PolicySubmitEvent(self.element, base, result, type, reslist)
        self.enque(event)



    def Policy_submitCmapBulkAsyncRspIDL(self, base, result, type, reslist):
        """
                Internal use only
        
                Converts IDL classes to public classes for event listeners to use
        
                """
        self.log.debug('cmap bulk async event = ' + str(base) + ' ' + str(result) + ' ' + str(type) + ' ' + str(reslist))
        if self.terminated:
            self.log.debug('cmap bulk async event terminated')
            return 
        event = ClassEvent(self.element, base, result, type, reslist)
        self.enque(event)



    def Policy_submitActivateBulkAsyncRspIDL(self, base, result, type, reslist):
        """
                Internal use only
        
                Converts IDL classes to public classes for event listeners to use
        
                """
        self.log.debug('pmap bulk async activate event = ' + str(base) + ' ' + str(result) + ' ' + str(type) + ' ' + str(reslist))
        if self.terminated:
            self.log.debug('pmap bulk async activate event terminated')
            return 
        event = PolicyActivateEvent(self.element, base, result, type, reslist)
        self.enque(event)



    def Policy_StatisticsEventIDL(self, session_handle, event_handle, statresult):
        """
                Internal use only
        
                Converts IDL classes to public classes for event listeners to use
        
                """
        self.log.debug('cmap bulk async stat event = ' + str(session_handle) + '' + str(event_handle))
        if self.terminated:
            self.log.debug('pmap bulk async statistics event terminated')
        event = PolicyStatsEvent(self.element, session_handle, event_handle, statresult)
        self.enque(event)



    def enque(self, event):
        """
            For internal use only
        
            """
        if self.terminated:
            self.log.warn('Event ' + ' received after the session has been terminated, ignoring it.')
            return 
        self.ka_monitor.update_heatbeat_time()
        self.element.session_handle.sessionStat.incrementEventTotalCount()
        if len(self.event_queue) == self.event_queue.maxlen:
            self.element.session_handle.sessionStat.incrementEventDropCount()
            if self.sessionProp.eventDropMode == SessionConfig.OnepEventDropMode.ONEP_EVENT_DROP_NEW:
                return 
        try:
            self.event_queue.append(event)
        except Exception as e:
            self.terminated = True



    def enque_dedicated(self, event, async_handle):
        """
        This is a special form of enque method. The event will be put 
        on the dedicated queue specific for the asyncHandle instead 
        of the global queue
        
        @param event: Event to be queued
        @type event: L{AsyncMsg<onep.core.event.AsyncMsg>}
        
        @param async_handle: The async handle to create the queue for
        @type async_handle: C{int}
        """
        if self.terminated:
            self.log.debug('Event ' + ' received after the session has been terminated, ignoring it.')
            return OnepConstants.FAIL
        self.ka_monitor.update_heatbeat_time()
        if self.dedicated_event_queue_map == None:
            self.log.debug('Dedicated queue map %d empty' % async_handle)
            return OnepStatus.ONEP_EOK_EVENTQ_FULL
        dedicated_queue = self.dedicated_event_queue_map.get(async_handle)
        if dedicated_queue == None:
            self.log.debug('Dedicated queue %d missing' % async_handle)
            return OnepStatus.ONEP_EOK_EVENTQ_FULL
        if len(dedicated_queue) == dedicated_queue.maxlen:
            self.log.debug('Dedicated queue %d full' % async_handle)
            return OnepConstants.ERR_EVENTQ_FULL
        self.log.debug('Dedicated queue %d enque event' % async_handle)
        dedicated_queue.append(event)



    def register_dedicated_queue(self, async_handle, qsize):
        """
        Register a dedicated queue for this asyncHandle
        
        @param async_handle: The handle to create the queue for
        @type async_handle: C{int}
        
        @param qsize: The size of the queue
        @type qsize: C{int}
        """
        self.log.debug('Dedicated queue %d size %d registered' % (async_handle, qsize))
        if self.dedicated_event_queue_map == None:
            self.dedicated_event_queue_map = {}
        dedicated_queue = self.dedicated_event_queue_map.get(async_handle, None)
        if dedicated_queue != None:
            self.dedicated_event_queue_map[async_handle] = None
            self.dedicated_event_queue_map[async_handle] = collections.deque(maxlen=qsize)
        else:
            dedicated_queue = collections.deque(maxlen=qsize)
            self.dedicated_event_queue_map[async_handle] = dedicated_queue
        if self.dedicated_dispatcher_map == None:
            self.dedicated_dispatcher_map = {}
        dispatcher = EventDispatcher()
        dispatcher.event_queue = dedicated_queue
        dispatcher.element = self.element
        self.dedicated_dispatcher_map[async_handle] = dispatcher
        dispatcher.start()



    def deregister_dedicated_queue(self, async_handle):
        """
        Deregister dedicated queue for this async handle
        
        @param async_handle: The asyncHandle for this queue
        @type async_handle: C{int}
        """
        if self.dedicated_event_queue_map == None:
            self.log.debug('deregister dedicated queue %d missing' % async_handle)
            return 
        dedicated_queue = self.dedicated_event_queue_map.get(async_handle, None)
        if dedicated_queue != None:
            self.log.debug('deregister dedicated queue %d' % async_handle)
            self.dedicated_event_queue_map[async_handle] = None
        dispatcher_map = self.dedicated_dispatcher_map.get(async_handle, None)
        if dispatcher_map != None:
            dispatcher_map.interrupt()
        self.dedicated_dispatcher_map.pop(async_handle, None)



    def notify_sender(self, async_handle):
        session_handle = self.element.session_handle._id
        status = -1
        try:
            status = self.element.api_client.AsyncMsg_notifySenderIDL(session_handle, async_handle)
            return status
        except Shared.ttypes.ExceptionIDL as e:
            self.log.debug('Ignored calling AsyncMsg_notifySenderIDL')
        except TException as e:
            self.log.debug('Ignored calling AsyncMsg_notifySenderIDL')
        return status



    def terminate(self):
        """
            For internal use only
        
            """
        self.terminated = True
        for d in self.dispatchers:
            d.interrupt()

        if self.dedicated_dispatcher_map != None:
            for d in self.dedicated_dispatcher_map.values():
                d.interrupt()

        if self.ka_monitor != None:
            self.ka_monitor.stop_monitor()
            self.ka_monitor = None




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:18:07 IST
