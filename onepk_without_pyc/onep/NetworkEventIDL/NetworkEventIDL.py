# 2015.02.05 17:21:50 IST
from thrift.Thrift import *
from ttypes import *
from thrift.Thrift import TProcessor
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
    from thrift.protocol import fastbinary
except:
    fastbinary = None

class Iface(object):

    def OnepEvent_keepaliveHeartbeatIDL(self, sessionHandle):
        """
        Parameters:
         - sessionHandle
        """
        pass



    def OnepEvent_applEventIDL(self, sessionHandle, eventHandle, applID, type, data1, data2, data3, data4):
        """
        Parameters:
         - sessionHandle
         - eventHandle
         - applID
         - type
         - data1
         - data2
         - data3
         - data4
        """
        pass



    def OnepEvent_appLogLevelChangeIDL(self, sessionHandle, level, dummy):
        """
        Parameters:
         - sessionHandle
         - level
         - dummy
        """
        pass



    def OnepEvent_configNotificationIDL(self, sessionHandle, cfg_data_name, cfg_data_value):
        """
        Parameters:
         - sessionHandle
         - cfg_data_name
         - cfg_data_value
        """
        pass



    def OnepEvent_showDataIDL(self, sessionHandle, show_data_name):
        """
        Parameters:
         - sessionHandle
         - show_data_name
        """
        pass



    def OnepEvent_cliEventIDL(self, sessionHandle, eventHandle, msgCount, tty, errorCode, sync, message):
        """
        Parameters:
         - sessionHandle
         - eventHandle
         - msgCount
         - tty
         - errorCode
         - sync
         - message
        """
        pass



    def OnepEvent_cdpEventIDL(self, sessionHandle, eventHandle, xosHandle, name, type, notifyType, neighborName, holdTime, mgmtDomain, platform, version, capabilities, addresses, neighborIntfName):
        """
        Parameters:
         - sessionHandle
         - eventHandle
         - xosHandle
         - name
         - type
         - notifyType
         - neighborName
         - holdTime
         - mgmtDomain
         - platform
         - version
         - capabilities
         - addresses
         - neighborIntfName
        """
        pass



    def OnepEvent_syslogEventIDL(self, sessionHandle, eventHandle, msgCount, priority, message):
        """
        Parameters:
         - sessionHandle
         - eventHandle
         - msgCount
         - priority
         - message
        """
        pass



    def OnepEvent_oirEventIDL(self, sessionHandle, eventHandle, slot, oirType):
        """
        Parameters:
         - sessionHandle
         - eventHandle
         - slot
         - oirType
        """
        pass



    def OnepEvent_InterfaceStateEventIDL(self, sessionHandle, eventHandle, xosHandle, intfType, stateEventType, intfState, shortName, link, lineproto):
        """
        Parameters:
         - sessionHandle
         - eventHandle
         - xosHandle
         - intfType
         - stateEventType
         - intfState
         - shortName
         - link
         - lineproto
        """
        pass



    def OnepEvent_InterfaceStatisticsEventIDL(self, sessionHandle, eventHandle, xosHandle, intfType, parameter, isIncrement, isExitEvent, value, deltaValue, shortName):
        """
        Parameters:
         - sessionHandle
         - eventHandle
         - xosHandle
         - intfType
         - parameter
         - isIncrement
         - isExitEvent
         - value
         - deltaValue
         - shortName
        """
        pass



    def OnepEvent_InterfaceAddrChangeEventIDL(self, sessionHandle, eventHandle, intfXosHandle, intfName, intfType, oldAddress, newAddress, oldPrefix, newPrefix):
        """
        Parameters:
         - sessionHandle
         - eventHandle
         - intfXosHandle
         - intfName
         - intfType
         - oldAddress
         - newAddress
         - oldPrefix
         - newPrefix
        """
        pass



    def OnepEvent_InterfaceCreateDeleteEventIDL(self, sessionHandle, eventHandle, intfXosHandle, intfName, intfType, isCreated, isOir):
        """
        Parameters:
         - sessionHandle
         - eventHandle
         - intfXosHandle
         - intfName
         - intfType
         - isCreated
         - isOir
        """
        pass



    def OnepEvent_InterfaceCTXEnableDisableEventIDL(self, sessionHandle, eventHandle, intfXosHandle, intfName, intfType, oprType):
        """
        Parameters:
         - sessionHandle
         - eventHandle
         - intfXosHandle
         - intfName
         - intfType
         - oprType
        """
        pass



    def OnepEvent_InterfaceStatisticsPollEventIDL(self, sessionHandle, eventHandle, intfXosHandle, intfName, intfType, intfstats):
        """
        Parameters:
         - sessionHandle
         - eventHandle
         - intfXosHandle
         - intfName
         - intfType
         - intfstats
        """
        pass



    def OnepEvent_srvcDiscoveryEventIDL(self, sessionHandle, eventHandle, discoveryType, ssId, ssState, veridl, neAddr):
        """
        Parameters:
         - sessionHandle
         - eventHandle
         - discoveryType
         - ssId
         - ssState
         - veridl
         - neAddr
        """
        pass



    def OnepEvent_vtyEventIDL(self, sessionHandle, execHandle, state, msgType, data):
        """
        Parameters:
         - sessionHandle
         - execHandle
         - state
         - msgType
         - data
        """
        pass



    def OnepEvent_capIntIDL(self, sessionHandle, capabilty_name, capabilty_value):
        """
        Parameters:
         - sessionHandle
         - capabilty_name
         - capabilty_value
        """
        pass



    def OnepEvent_capStrIDL(self, sessionHandle, capabilty_name, capabilty_value):
        """
        Parameters:
         - sessionHandle
         - capabilty_name
         - capabilty_value
        """
        pass



    def OnepEvent_ContainerSrvChangeEventIDL(self, sessionHandle, eventtype, adding, mask, MacID, Addr):
        """
        Parameters:
         - sessionHandle
         - eventtype
         - adding
         - mask
         - MacID
         - Addr
        """
        pass



    def OnepEvent_ContainerSrvInfoRequestIDL(self, sessionHandle, eventtype, transactionID, MacID, extrainfo):
        """
        Parameters:
         - sessionHandle
         - eventtype
         - transactionID
         - MacID
         - extrainfo
        """
        pass



    def OnepEvent_InterfaceMtuEventIDL(self, sessionHandle, eventHandle, xosHandle, intfType, shortName, mtu):
        """
        Parameters:
         - sessionHandle
         - eventHandle
         - xosHandle
         - intfType
         - shortName
         - mtu
        """
        pass



    def OnepEvent_InterfaceSpeedEventIDL(self, sessionHandle, eventHandle, xosHandle, intfType, shortName, speed, configType):
        """
        Parameters:
         - sessionHandle
         - eventHandle
         - xosHandle
         - intfType
         - shortName
         - speed
         - configType
        """
        pass



    def OnepEvent_InterfaceDuplexModeEventIDL(self, sessionHandle, eventHandle, xosHandle, intfType, shortName, duplexMode, configType):
        """
        Parameters:
         - sessionHandle
         - eventHandle
         - xosHandle
         - intfType
         - shortName
         - duplexMode
         - configType
        """
        pass



    def OnepEvent_InterfaceAutoNegotiateEventIDL(self, sessionHandle, eventHandle, xosHandle, intfType, shortName, autoNeg, configType):
        """
        Parameters:
         - sessionHandle
         - eventHandle
         - xosHandle
         - intfType
         - shortName
         - autoNeg
         - configType
        """
        pass



    def OnepEvent_InterfaceLayer2ModeEventIDL(self, sessionHandle, eventHandle, xosHandle, intfType, shortName, laye2Mode):
        """
        Parameters:
         - sessionHandle
         - eventHandle
         - xosHandle
         - intfType
         - shortName
         - laye2Mode
        """
        pass



    def OnepEvent_InterfaceFlowcontrolEventIDL(self, sessionHandle, eventHandle, xosHandle, intfType, shortName, inFlow, outFlow, configType):
        """
        Parameters:
         - sessionHandle
         - eventHandle
         - xosHandle
         - intfType
         - shortName
         - inFlow
         - outFlow
         - configType
        """
        pass



    def OnepEvent_InterfaceForwardClassIDEventIDL(self, sessionHandle, eventHandle, xosHandle, intfType, shortName, fwdClassID):
        """
        Parameters:
         - sessionHandle
         - eventHandle
         - xosHandle
         - intfType
         - shortName
         - fwdClassID
        """
        pass



    def OnepEvent_InterfaceBandwidthEventIDL(self, sessionHandle, eventHandle, xosHandle, intfType, shortName, bandwidth, is_tx):
        """
        Parameters:
         - sessionHandle
         - eventHandle
         - xosHandle
         - intfType
         - shortName
         - bandwidth
         - is_tx
        """
        pass



    def OnepEvent_InterfaceVlanEventIDL(self, sessionHandle, eventHandle, xosHandle, intfType, shortName, vlan, vlanEventType):
        """
        Parameters:
         - sessionHandle
         - eventHandle
         - xosHandle
         - intfType
         - shortName
         - vlan
         - vlanEventType
        """
        pass



    def OnepEvent_InterfaceVrfEventIDL(self, sessionHandle, eventHandle, xosHandle, intfType, shortName, vrf, vrfEventType):
        """
        Parameters:
         - sessionHandle
         - eventHandle
         - xosHandle
         - intfType
         - shortName
         - vrf
         - vrfEventType
        """
        pass



    def OnepEvent_HsrpStateEventIDL(self, sessionHandle, eventHandle, xosHandle, intfType, shortName, groupid, family, state):
        """
        Parameters:
         - sessionHandle
         - eventHandle
         - xosHandle
         - intfType
         - shortName
         - groupid
         - family
         - state
        """
        pass



    def OnepEvent_BDEventIDL(self, sessionHandle, eventHandle, type, id, name, xosHandle, intfType, shortName):
        """
        Parameters:
         - sessionHandle
         - eventHandle
         - type
         - id
         - name
         - xosHandle
         - intfType
         - shortName
        """
        pass



    def OnepEvent_BDServiceStatusEventIDL(self, sessionHandle, eventHandle, status, resync):
        """
        Parameters:
         - sessionHandle
         - eventHandle
         - status
         - resync
        """
        pass



    def OnepEvent_PortChannelEventIDL(self, sessionHandle, eventHandle, pcHandle, pcName, ifHandle, ifName, intfType, add):
        """
        Parameters:
         - sessionHandle
         - eventHandle
         - pcHandle
         - pcName
         - ifHandle
         - ifName
         - intfType
         - add
        """
        pass




class Client(Iface):

    def __init__(self, iprot, oprot = None):
        self._iprot = self._oprot = iprot
        if oprot != None:
            self._oprot = oprot
        self._seqid = 0



    def OnepEvent_keepaliveHeartbeatIDL(self, sessionHandle):
        """
        Parameters:
         - sessionHandle
        """
        self._oprot.rlock.acquire()
        try:
            self.send_OnepEvent_keepaliveHeartbeatIDL(sessionHandle)
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()



    def send_OnepEvent_keepaliveHeartbeatIDL(self, sessionHandle):
        self._oprot.writeMessageBegin('OnepEvent_keepaliveHeartbeatIDL', TMessageType.CALL, self._seqid)
        args = OnepEvent_keepaliveHeartbeatIDL_args()
        args.sessionHandle = sessionHandle
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def OnepEvent_applEventIDL(self, sessionHandle, eventHandle, applID, type, data1, data2, data3, data4):
        """
        Parameters:
         - sessionHandle
         - eventHandle
         - applID
         - type
         - data1
         - data2
         - data3
         - data4
        """
        self._oprot.rlock.acquire()
        try:
            self.send_OnepEvent_applEventIDL(sessionHandle, eventHandle, applID, type, data1, data2, data3, data4)
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()



    def send_OnepEvent_applEventIDL(self, sessionHandle, eventHandle, applID, type, data1, data2, data3, data4):
        self._oprot.writeMessageBegin('OnepEvent_applEventIDL', TMessageType.CALL, self._seqid)
        args = OnepEvent_applEventIDL_args()
        args.sessionHandle = sessionHandle
        args.eventHandle = eventHandle
        args.applID = applID
        args.type = type
        args.data1 = data1
        args.data2 = data2
        args.data3 = data3
        args.data4 = data4
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def OnepEvent_appLogLevelChangeIDL(self, sessionHandle, level, dummy):
        """
        Parameters:
         - sessionHandle
         - level
         - dummy
        """
        self._oprot.rlock.acquire()
        try:
            self.send_OnepEvent_appLogLevelChangeIDL(sessionHandle, level, dummy)
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()



    def send_OnepEvent_appLogLevelChangeIDL(self, sessionHandle, level, dummy):
        self._oprot.writeMessageBegin('OnepEvent_appLogLevelChangeIDL', TMessageType.CALL, self._seqid)
        args = OnepEvent_appLogLevelChangeIDL_args()
        args.sessionHandle = sessionHandle
        args.level = level
        args.dummy = dummy
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def OnepEvent_configNotificationIDL(self, sessionHandle, cfg_data_name, cfg_data_value):
        """
        Parameters:
         - sessionHandle
         - cfg_data_name
         - cfg_data_value
        """
        self._oprot.rlock.acquire()
        try:
            self.send_OnepEvent_configNotificationIDL(sessionHandle, cfg_data_name, cfg_data_value)
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()



    def send_OnepEvent_configNotificationIDL(self, sessionHandle, cfg_data_name, cfg_data_value):
        self._oprot.writeMessageBegin('OnepEvent_configNotificationIDL', TMessageType.CALL, self._seqid)
        args = OnepEvent_configNotificationIDL_args()
        args.sessionHandle = sessionHandle
        args.cfg_data_name = cfg_data_name
        args.cfg_data_value = cfg_data_value
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def OnepEvent_showDataIDL(self, sessionHandle, show_data_name):
        """
        Parameters:
         - sessionHandle
         - show_data_name
        """
        self._oprot.rlock.acquire()
        try:
            self.send_OnepEvent_showDataIDL(sessionHandle, show_data_name)
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()



    def send_OnepEvent_showDataIDL(self, sessionHandle, show_data_name):
        self._oprot.writeMessageBegin('OnepEvent_showDataIDL', TMessageType.CALL, self._seqid)
        args = OnepEvent_showDataIDL_args()
        args.sessionHandle = sessionHandle
        args.show_data_name = show_data_name
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def OnepEvent_cliEventIDL(self, sessionHandle, eventHandle, msgCount, tty, errorCode, sync, message):
        """
        Parameters:
         - sessionHandle
         - eventHandle
         - msgCount
         - tty
         - errorCode
         - sync
         - message
        """
        self._oprot.rlock.acquire()
        try:
            self.send_OnepEvent_cliEventIDL(sessionHandle, eventHandle, msgCount, tty, errorCode, sync, message)
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()



    def send_OnepEvent_cliEventIDL(self, sessionHandle, eventHandle, msgCount, tty, errorCode, sync, message):
        self._oprot.writeMessageBegin('OnepEvent_cliEventIDL', TMessageType.CALL, self._seqid)
        args = OnepEvent_cliEventIDL_args()
        args.sessionHandle = sessionHandle
        args.eventHandle = eventHandle
        args.msgCount = msgCount
        args.tty = tty
        args.errorCode = errorCode
        args.sync = sync
        args.message = message
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def OnepEvent_cdpEventIDL(self, sessionHandle, eventHandle, xosHandle, name, type, notifyType, neighborName, holdTime, mgmtDomain, platform, version, capabilities, addresses, neighborIntfName):
        """
        Parameters:
         - sessionHandle
         - eventHandle
         - xosHandle
         - name
         - type
         - notifyType
         - neighborName
         - holdTime
         - mgmtDomain
         - platform
         - version
         - capabilities
         - addresses
         - neighborIntfName
        """
        self._oprot.rlock.acquire()
        try:
            self.send_OnepEvent_cdpEventIDL(sessionHandle, eventHandle, xosHandle, name, type, notifyType, neighborName, holdTime, mgmtDomain, platform, version, capabilities, addresses, neighborIntfName)
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()



    def send_OnepEvent_cdpEventIDL(self, sessionHandle, eventHandle, xosHandle, name, type, notifyType, neighborName, holdTime, mgmtDomain, platform, version, capabilities, addresses, neighborIntfName):
        self._oprot.writeMessageBegin('OnepEvent_cdpEventIDL', TMessageType.CALL, self._seqid)
        args = OnepEvent_cdpEventIDL_args()
        args.sessionHandle = sessionHandle
        args.eventHandle = eventHandle
        args.xosHandle = xosHandle
        args.name = name
        args.type = type
        args.notifyType = notifyType
        args.neighborName = neighborName
        args.holdTime = holdTime
        args.mgmtDomain = mgmtDomain
        args.platform = platform
        args.version = version
        args.capabilities = capabilities
        args.addresses = addresses
        args.neighborIntfName = neighborIntfName
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def OnepEvent_syslogEventIDL(self, sessionHandle, eventHandle, msgCount, priority, message):
        """
        Parameters:
         - sessionHandle
         - eventHandle
         - msgCount
         - priority
         - message
        """
        self._oprot.rlock.acquire()
        try:
            self.send_OnepEvent_syslogEventIDL(sessionHandle, eventHandle, msgCount, priority, message)
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()



    def send_OnepEvent_syslogEventIDL(self, sessionHandle, eventHandle, msgCount, priority, message):
        self._oprot.writeMessageBegin('OnepEvent_syslogEventIDL', TMessageType.CALL, self._seqid)
        args = OnepEvent_syslogEventIDL_args()
        args.sessionHandle = sessionHandle
        args.eventHandle = eventHandle
        args.msgCount = msgCount
        args.priority = priority
        args.message = message
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def OnepEvent_oirEventIDL(self, sessionHandle, eventHandle, slot, oirType):
        """
        Parameters:
         - sessionHandle
         - eventHandle
         - slot
         - oirType
        """
        self._oprot.rlock.acquire()
        try:
            self.send_OnepEvent_oirEventIDL(sessionHandle, eventHandle, slot, oirType)
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()



    def send_OnepEvent_oirEventIDL(self, sessionHandle, eventHandle, slot, oirType):
        self._oprot.writeMessageBegin('OnepEvent_oirEventIDL', TMessageType.CALL, self._seqid)
        args = OnepEvent_oirEventIDL_args()
        args.sessionHandle = sessionHandle
        args.eventHandle = eventHandle
        args.slot = slot
        args.oirType = oirType
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def OnepEvent_InterfaceStateEventIDL(self, sessionHandle, eventHandle, xosHandle, intfType, stateEventType, intfState, shortName, link, lineproto):
        """
        Parameters:
         - sessionHandle
         - eventHandle
         - xosHandle
         - intfType
         - stateEventType
         - intfState
         - shortName
         - link
         - lineproto
        """
        self._oprot.rlock.acquire()
        try:
            self.send_OnepEvent_InterfaceStateEventIDL(sessionHandle, eventHandle, xosHandle, intfType, stateEventType, intfState, shortName, link, lineproto)
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()



    def send_OnepEvent_InterfaceStateEventIDL(self, sessionHandle, eventHandle, xosHandle, intfType, stateEventType, intfState, shortName, link, lineproto):
        self._oprot.writeMessageBegin('OnepEvent_InterfaceStateEventIDL', TMessageType.CALL, self._seqid)
        args = OnepEvent_InterfaceStateEventIDL_args()
        args.sessionHandle = sessionHandle
        args.eventHandle = eventHandle
        args.xosHandle = xosHandle
        args.intfType = intfType
        args.stateEventType = stateEventType
        args.intfState = intfState
        args.shortName = shortName
        args.link = link
        args.lineproto = lineproto
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def OnepEvent_InterfaceStatisticsEventIDL(self, sessionHandle, eventHandle, xosHandle, intfType, parameter, isIncrement, isExitEvent, value, deltaValue, shortName):
        """
        Parameters:
         - sessionHandle
         - eventHandle
         - xosHandle
         - intfType
         - parameter
         - isIncrement
         - isExitEvent
         - value
         - deltaValue
         - shortName
        """
        self._oprot.rlock.acquire()
        try:
            self.send_OnepEvent_InterfaceStatisticsEventIDL(sessionHandle, eventHandle, xosHandle, intfType, parameter, isIncrement, isExitEvent, value, deltaValue, shortName)
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()



    def send_OnepEvent_InterfaceStatisticsEventIDL(self, sessionHandle, eventHandle, xosHandle, intfType, parameter, isIncrement, isExitEvent, value, deltaValue, shortName):
        self._oprot.writeMessageBegin('OnepEvent_InterfaceStatisticsEventIDL', TMessageType.CALL, self._seqid)
        args = OnepEvent_InterfaceStatisticsEventIDL_args()
        args.sessionHandle = sessionHandle
        args.eventHandle = eventHandle
        args.xosHandle = xosHandle
        args.intfType = intfType
        args.parameter = parameter
        args.isIncrement = isIncrement
        args.isExitEvent = isExitEvent
        args.value = value
        args.deltaValue = deltaValue
        args.shortName = shortName
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def OnepEvent_InterfaceAddrChangeEventIDL(self, sessionHandle, eventHandle, intfXosHandle, intfName, intfType, oldAddress, newAddress, oldPrefix, newPrefix):
        """
        Parameters:
         - sessionHandle
         - eventHandle
         - intfXosHandle
         - intfName
         - intfType
         - oldAddress
         - newAddress
         - oldPrefix
         - newPrefix
        """
        self._oprot.rlock.acquire()
        try:
            self.send_OnepEvent_InterfaceAddrChangeEventIDL(sessionHandle, eventHandle, intfXosHandle, intfName, intfType, oldAddress, newAddress, oldPrefix, newPrefix)
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()



    def send_OnepEvent_InterfaceAddrChangeEventIDL(self, sessionHandle, eventHandle, intfXosHandle, intfName, intfType, oldAddress, newAddress, oldPrefix, newPrefix):
        self._oprot.writeMessageBegin('OnepEvent_InterfaceAddrChangeEventIDL', TMessageType.CALL, self._seqid)
        args = OnepEvent_InterfaceAddrChangeEventIDL_args()
        args.sessionHandle = sessionHandle
        args.eventHandle = eventHandle
        args.intfXosHandle = intfXosHandle
        args.intfName = intfName
        args.intfType = intfType
        args.oldAddress = oldAddress
        args.newAddress = newAddress
        args.oldPrefix = oldPrefix
        args.newPrefix = newPrefix
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def OnepEvent_InterfaceCreateDeleteEventIDL(self, sessionHandle, eventHandle, intfXosHandle, intfName, intfType, isCreated, isOir):
        """
        Parameters:
         - sessionHandle
         - eventHandle
         - intfXosHandle
         - intfName
         - intfType
         - isCreated
         - isOir
        """
        self._oprot.rlock.acquire()
        try:
            self.send_OnepEvent_InterfaceCreateDeleteEventIDL(sessionHandle, eventHandle, intfXosHandle, intfName, intfType, isCreated, isOir)
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()



    def send_OnepEvent_InterfaceCreateDeleteEventIDL(self, sessionHandle, eventHandle, intfXosHandle, intfName, intfType, isCreated, isOir):
        self._oprot.writeMessageBegin('OnepEvent_InterfaceCreateDeleteEventIDL', TMessageType.CALL, self._seqid)
        args = OnepEvent_InterfaceCreateDeleteEventIDL_args()
        args.sessionHandle = sessionHandle
        args.eventHandle = eventHandle
        args.intfXosHandle = intfXosHandle
        args.intfName = intfName
        args.intfType = intfType
        args.isCreated = isCreated
        args.isOir = isOir
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def OnepEvent_InterfaceCTXEnableDisableEventIDL(self, sessionHandle, eventHandle, intfXosHandle, intfName, intfType, oprType):
        """
        Parameters:
         - sessionHandle
         - eventHandle
         - intfXosHandle
         - intfName
         - intfType
         - oprType
        """
        self._oprot.rlock.acquire()
        try:
            self.send_OnepEvent_InterfaceCTXEnableDisableEventIDL(sessionHandle, eventHandle, intfXosHandle, intfName, intfType, oprType)
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()



    def send_OnepEvent_InterfaceCTXEnableDisableEventIDL(self, sessionHandle, eventHandle, intfXosHandle, intfName, intfType, oprType):
        self._oprot.writeMessageBegin('OnepEvent_InterfaceCTXEnableDisableEventIDL', TMessageType.CALL, self._seqid)
        args = OnepEvent_InterfaceCTXEnableDisableEventIDL_args()
        args.sessionHandle = sessionHandle
        args.eventHandle = eventHandle
        args.intfXosHandle = intfXosHandle
        args.intfName = intfName
        args.intfType = intfType
        args.oprType = oprType
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def OnepEvent_InterfaceStatisticsPollEventIDL(self, sessionHandle, eventHandle, intfXosHandle, intfName, intfType, intfstats):
        """
        Parameters:
         - sessionHandle
         - eventHandle
         - intfXosHandle
         - intfName
         - intfType
         - intfstats
        """
        self._oprot.rlock.acquire()
        try:
            self.send_OnepEvent_InterfaceStatisticsPollEventIDL(sessionHandle, eventHandle, intfXosHandle, intfName, intfType, intfstats)
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()



    def send_OnepEvent_InterfaceStatisticsPollEventIDL(self, sessionHandle, eventHandle, intfXosHandle, intfName, intfType, intfstats):
        self._oprot.writeMessageBegin('OnepEvent_InterfaceStatisticsPollEventIDL', TMessageType.CALL, self._seqid)
        args = OnepEvent_InterfaceStatisticsPollEventIDL_args()
        args.sessionHandle = sessionHandle
        args.eventHandle = eventHandle
        args.intfXosHandle = intfXosHandle
        args.intfName = intfName
        args.intfType = intfType
        args.intfstats = intfstats
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def OnepEvent_srvcDiscoveryEventIDL(self, sessionHandle, eventHandle, discoveryType, ssId, ssState, veridl, neAddr):
        """
        Parameters:
         - sessionHandle
         - eventHandle
         - discoveryType
         - ssId
         - ssState
         - veridl
         - neAddr
        """
        self._oprot.rlock.acquire()
        try:
            self.send_OnepEvent_srvcDiscoveryEventIDL(sessionHandle, eventHandle, discoveryType, ssId, ssState, veridl, neAddr)
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()



    def send_OnepEvent_srvcDiscoveryEventIDL(self, sessionHandle, eventHandle, discoveryType, ssId, ssState, veridl, neAddr):
        self._oprot.writeMessageBegin('OnepEvent_srvcDiscoveryEventIDL', TMessageType.CALL, self._seqid)
        args = OnepEvent_srvcDiscoveryEventIDL_args()
        args.sessionHandle = sessionHandle
        args.eventHandle = eventHandle
        args.discoveryType = discoveryType
        args.ssId = ssId
        args.ssState = ssState
        args.veridl = veridl
        args.neAddr = neAddr
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def OnepEvent_vtyEventIDL(self, sessionHandle, execHandle, state, msgType, data):
        """
        Parameters:
         - sessionHandle
         - execHandle
         - state
         - msgType
         - data
        """
        self._oprot.rlock.acquire()
        try:
            self.send_OnepEvent_vtyEventIDL(sessionHandle, execHandle, state, msgType, data)
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()



    def send_OnepEvent_vtyEventIDL(self, sessionHandle, execHandle, state, msgType, data):
        self._oprot.writeMessageBegin('OnepEvent_vtyEventIDL', TMessageType.CALL, self._seqid)
        args = OnepEvent_vtyEventIDL_args()
        args.sessionHandle = sessionHandle
        args.execHandle = execHandle
        args.state = state
        args.msgType = msgType
        args.data = data
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def OnepEvent_capIntIDL(self, sessionHandle, capabilty_name, capabilty_value):
        """
        Parameters:
         - sessionHandle
         - capabilty_name
         - capabilty_value
        """
        self._oprot.rlock.acquire()
        try:
            self.send_OnepEvent_capIntIDL(sessionHandle, capabilty_name, capabilty_value)
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()



    def send_OnepEvent_capIntIDL(self, sessionHandle, capabilty_name, capabilty_value):
        self._oprot.writeMessageBegin('OnepEvent_capIntIDL', TMessageType.CALL, self._seqid)
        args = OnepEvent_capIntIDL_args()
        args.sessionHandle = sessionHandle
        args.capabilty_name = capabilty_name
        args.capabilty_value = capabilty_value
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def OnepEvent_capStrIDL(self, sessionHandle, capabilty_name, capabilty_value):
        """
        Parameters:
         - sessionHandle
         - capabilty_name
         - capabilty_value
        """
        self._oprot.rlock.acquire()
        try:
            self.send_OnepEvent_capStrIDL(sessionHandle, capabilty_name, capabilty_value)
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()



    def send_OnepEvent_capStrIDL(self, sessionHandle, capabilty_name, capabilty_value):
        self._oprot.writeMessageBegin('OnepEvent_capStrIDL', TMessageType.CALL, self._seqid)
        args = OnepEvent_capStrIDL_args()
        args.sessionHandle = sessionHandle
        args.capabilty_name = capabilty_name
        args.capabilty_value = capabilty_value
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def OnepEvent_ContainerSrvChangeEventIDL(self, sessionHandle, eventtype, adding, mask, MacID, Addr):
        """
        Parameters:
         - sessionHandle
         - eventtype
         - adding
         - mask
         - MacID
         - Addr
        """
        self._oprot.rlock.acquire()
        try:
            self.send_OnepEvent_ContainerSrvChangeEventIDL(sessionHandle, eventtype, adding, mask, MacID, Addr)
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()



    def send_OnepEvent_ContainerSrvChangeEventIDL(self, sessionHandle, eventtype, adding, mask, MacID, Addr):
        self._oprot.writeMessageBegin('OnepEvent_ContainerSrvChangeEventIDL', TMessageType.CALL, self._seqid)
        args = OnepEvent_ContainerSrvChangeEventIDL_args()
        args.sessionHandle = sessionHandle
        args.eventtype = eventtype
        args.adding = adding
        args.mask = mask
        args.MacID = MacID
        args.Addr = Addr
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def OnepEvent_ContainerSrvInfoRequestIDL(self, sessionHandle, eventtype, transactionID, MacID, extrainfo):
        """
        Parameters:
         - sessionHandle
         - eventtype
         - transactionID
         - MacID
         - extrainfo
        """
        self._oprot.rlock.acquire()
        try:
            self.send_OnepEvent_ContainerSrvInfoRequestIDL(sessionHandle, eventtype, transactionID, MacID, extrainfo)
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()



    def send_OnepEvent_ContainerSrvInfoRequestIDL(self, sessionHandle, eventtype, transactionID, MacID, extrainfo):
        self._oprot.writeMessageBegin('OnepEvent_ContainerSrvInfoRequestIDL', TMessageType.CALL, self._seqid)
        args = OnepEvent_ContainerSrvInfoRequestIDL_args()
        args.sessionHandle = sessionHandle
        args.eventtype = eventtype
        args.transactionID = transactionID
        args.MacID = MacID
        args.extrainfo = extrainfo
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def OnepEvent_InterfaceMtuEventIDL(self, sessionHandle, eventHandle, xosHandle, intfType, shortName, mtu):
        """
        Parameters:
         - sessionHandle
         - eventHandle
         - xosHandle
         - intfType
         - shortName
         - mtu
        """
        self._oprot.rlock.acquire()
        try:
            self.send_OnepEvent_InterfaceMtuEventIDL(sessionHandle, eventHandle, xosHandle, intfType, shortName, mtu)
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()



    def send_OnepEvent_InterfaceMtuEventIDL(self, sessionHandle, eventHandle, xosHandle, intfType, shortName, mtu):
        self._oprot.writeMessageBegin('OnepEvent_InterfaceMtuEventIDL', TMessageType.CALL, self._seqid)
        args = OnepEvent_InterfaceMtuEventIDL_args()
        args.sessionHandle = sessionHandle
        args.eventHandle = eventHandle
        args.xosHandle = xosHandle
        args.intfType = intfType
        args.shortName = shortName
        args.mtu = mtu
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def OnepEvent_InterfaceSpeedEventIDL(self, sessionHandle, eventHandle, xosHandle, intfType, shortName, speed, configType):
        """
        Parameters:
         - sessionHandle
         - eventHandle
         - xosHandle
         - intfType
         - shortName
         - speed
         - configType
        """
        self._oprot.rlock.acquire()
        try:
            self.send_OnepEvent_InterfaceSpeedEventIDL(sessionHandle, eventHandle, xosHandle, intfType, shortName, speed, configType)
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()



    def send_OnepEvent_InterfaceSpeedEventIDL(self, sessionHandle, eventHandle, xosHandle, intfType, shortName, speed, configType):
        self._oprot.writeMessageBegin('OnepEvent_InterfaceSpeedEventIDL', TMessageType.CALL, self._seqid)
        args = OnepEvent_InterfaceSpeedEventIDL_args()
        args.sessionHandle = sessionHandle
        args.eventHandle = eventHandle
        args.xosHandle = xosHandle
        args.intfType = intfType
        args.shortName = shortName
        args.speed = speed
        args.configType = configType
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def OnepEvent_InterfaceDuplexModeEventIDL(self, sessionHandle, eventHandle, xosHandle, intfType, shortName, duplexMode, configType):
        """
        Parameters:
         - sessionHandle
         - eventHandle
         - xosHandle
         - intfType
         - shortName
         - duplexMode
         - configType
        """
        self._oprot.rlock.acquire()
        try:
            self.send_OnepEvent_InterfaceDuplexModeEventIDL(sessionHandle, eventHandle, xosHandle, intfType, shortName, duplexMode, configType)
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()



    def send_OnepEvent_InterfaceDuplexModeEventIDL(self, sessionHandle, eventHandle, xosHandle, intfType, shortName, duplexMode, configType):
        self._oprot.writeMessageBegin('OnepEvent_InterfaceDuplexModeEventIDL', TMessageType.CALL, self._seqid)
        args = OnepEvent_InterfaceDuplexModeEventIDL_args()
        args.sessionHandle = sessionHandle
        args.eventHandle = eventHandle
        args.xosHandle = xosHandle
        args.intfType = intfType
        args.shortName = shortName
        args.duplexMode = duplexMode
        args.configType = configType
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def OnepEvent_InterfaceAutoNegotiateEventIDL(self, sessionHandle, eventHandle, xosHandle, intfType, shortName, autoNeg, configType):
        """
        Parameters:
         - sessionHandle
         - eventHandle
         - xosHandle
         - intfType
         - shortName
         - autoNeg
         - configType
        """
        self._oprot.rlock.acquire()
        try:
            self.send_OnepEvent_InterfaceAutoNegotiateEventIDL(sessionHandle, eventHandle, xosHandle, intfType, shortName, autoNeg, configType)
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()



    def send_OnepEvent_InterfaceAutoNegotiateEventIDL(self, sessionHandle, eventHandle, xosHandle, intfType, shortName, autoNeg, configType):
        self._oprot.writeMessageBegin('OnepEvent_InterfaceAutoNegotiateEventIDL', TMessageType.CALL, self._seqid)
        args = OnepEvent_InterfaceAutoNegotiateEventIDL_args()
        args.sessionHandle = sessionHandle
        args.eventHandle = eventHandle
        args.xosHandle = xosHandle
        args.intfType = intfType
        args.shortName = shortName
        args.autoNeg = autoNeg
        args.configType = configType
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def OnepEvent_InterfaceLayer2ModeEventIDL(self, sessionHandle, eventHandle, xosHandle, intfType, shortName, laye2Mode):
        """
        Parameters:
         - sessionHandle
         - eventHandle
         - xosHandle
         - intfType
         - shortName
         - laye2Mode
        """
        self._oprot.rlock.acquire()
        try:
            self.send_OnepEvent_InterfaceLayer2ModeEventIDL(sessionHandle, eventHandle, xosHandle, intfType, shortName, laye2Mode)
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()



    def send_OnepEvent_InterfaceLayer2ModeEventIDL(self, sessionHandle, eventHandle, xosHandle, intfType, shortName, laye2Mode):
        self._oprot.writeMessageBegin('OnepEvent_InterfaceLayer2ModeEventIDL', TMessageType.CALL, self._seqid)
        args = OnepEvent_InterfaceLayer2ModeEventIDL_args()
        args.sessionHandle = sessionHandle
        args.eventHandle = eventHandle
        args.xosHandle = xosHandle
        args.intfType = intfType
        args.shortName = shortName
        args.laye2Mode = laye2Mode
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def OnepEvent_InterfaceFlowcontrolEventIDL(self, sessionHandle, eventHandle, xosHandle, intfType, shortName, inFlow, outFlow, configType):
        """
        Parameters:
         - sessionHandle
         - eventHandle
         - xosHandle
         - intfType
         - shortName
         - inFlow
         - outFlow
         - configType
        """
        self._oprot.rlock.acquire()
        try:
            self.send_OnepEvent_InterfaceFlowcontrolEventIDL(sessionHandle, eventHandle, xosHandle, intfType, shortName, inFlow, outFlow, configType)
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()



    def send_OnepEvent_InterfaceFlowcontrolEventIDL(self, sessionHandle, eventHandle, xosHandle, intfType, shortName, inFlow, outFlow, configType):
        self._oprot.writeMessageBegin('OnepEvent_InterfaceFlowcontrolEventIDL', TMessageType.CALL, self._seqid)
        args = OnepEvent_InterfaceFlowcontrolEventIDL_args()
        args.sessionHandle = sessionHandle
        args.eventHandle = eventHandle
        args.xosHandle = xosHandle
        args.intfType = intfType
        args.shortName = shortName
        args.inFlow = inFlow
        args.outFlow = outFlow
        args.configType = configType
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def OnepEvent_InterfaceForwardClassIDEventIDL(self, sessionHandle, eventHandle, xosHandle, intfType, shortName, fwdClassID):
        """
        Parameters:
         - sessionHandle
         - eventHandle
         - xosHandle
         - intfType
         - shortName
         - fwdClassID
        """
        self._oprot.rlock.acquire()
        try:
            self.send_OnepEvent_InterfaceForwardClassIDEventIDL(sessionHandle, eventHandle, xosHandle, intfType, shortName, fwdClassID)
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()



    def send_OnepEvent_InterfaceForwardClassIDEventIDL(self, sessionHandle, eventHandle, xosHandle, intfType, shortName, fwdClassID):
        self._oprot.writeMessageBegin('OnepEvent_InterfaceForwardClassIDEventIDL', TMessageType.CALL, self._seqid)
        args = OnepEvent_InterfaceForwardClassIDEventIDL_args()
        args.sessionHandle = sessionHandle
        args.eventHandle = eventHandle
        args.xosHandle = xosHandle
        args.intfType = intfType
        args.shortName = shortName
        args.fwdClassID = fwdClassID
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def OnepEvent_InterfaceBandwidthEventIDL(self, sessionHandle, eventHandle, xosHandle, intfType, shortName, bandwidth, is_tx):
        """
        Parameters:
         - sessionHandle
         - eventHandle
         - xosHandle
         - intfType
         - shortName
         - bandwidth
         - is_tx
        """
        self._oprot.rlock.acquire()
        try:
            self.send_OnepEvent_InterfaceBandwidthEventIDL(sessionHandle, eventHandle, xosHandle, intfType, shortName, bandwidth, is_tx)
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()



    def send_OnepEvent_InterfaceBandwidthEventIDL(self, sessionHandle, eventHandle, xosHandle, intfType, shortName, bandwidth, is_tx):
        self._oprot.writeMessageBegin('OnepEvent_InterfaceBandwidthEventIDL', TMessageType.CALL, self._seqid)
        args = OnepEvent_InterfaceBandwidthEventIDL_args()
        args.sessionHandle = sessionHandle
        args.eventHandle = eventHandle
        args.xosHandle = xosHandle
        args.intfType = intfType
        args.shortName = shortName
        args.bandwidth = bandwidth
        args.is_tx = is_tx
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def OnepEvent_InterfaceVlanEventIDL(self, sessionHandle, eventHandle, xosHandle, intfType, shortName, vlan, vlanEventType):
        """
        Parameters:
         - sessionHandle
         - eventHandle
         - xosHandle
         - intfType
         - shortName
         - vlan
         - vlanEventType
        """
        self._oprot.rlock.acquire()
        try:
            self.send_OnepEvent_InterfaceVlanEventIDL(sessionHandle, eventHandle, xosHandle, intfType, shortName, vlan, vlanEventType)
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()



    def send_OnepEvent_InterfaceVlanEventIDL(self, sessionHandle, eventHandle, xosHandle, intfType, shortName, vlan, vlanEventType):
        self._oprot.writeMessageBegin('OnepEvent_InterfaceVlanEventIDL', TMessageType.CALL, self._seqid)
        args = OnepEvent_InterfaceVlanEventIDL_args()
        args.sessionHandle = sessionHandle
        args.eventHandle = eventHandle
        args.xosHandle = xosHandle
        args.intfType = intfType
        args.shortName = shortName
        args.vlan = vlan
        args.vlanEventType = vlanEventType
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def OnepEvent_InterfaceVrfEventIDL(self, sessionHandle, eventHandle, xosHandle, intfType, shortName, vrf, vrfEventType):
        """
        Parameters:
         - sessionHandle
         - eventHandle
         - xosHandle
         - intfType
         - shortName
         - vrf
         - vrfEventType
        """
        self._oprot.rlock.acquire()
        try:
            self.send_OnepEvent_InterfaceVrfEventIDL(sessionHandle, eventHandle, xosHandle, intfType, shortName, vrf, vrfEventType)
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()



    def send_OnepEvent_InterfaceVrfEventIDL(self, sessionHandle, eventHandle, xosHandle, intfType, shortName, vrf, vrfEventType):
        self._oprot.writeMessageBegin('OnepEvent_InterfaceVrfEventIDL', TMessageType.CALL, self._seqid)
        args = OnepEvent_InterfaceVrfEventIDL_args()
        args.sessionHandle = sessionHandle
        args.eventHandle = eventHandle
        args.xosHandle = xosHandle
        args.intfType = intfType
        args.shortName = shortName
        args.vrf = vrf
        args.vrfEventType = vrfEventType
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def OnepEvent_HsrpStateEventIDL(self, sessionHandle, eventHandle, xosHandle, intfType, shortName, groupid, family, state):
        """
        Parameters:
         - sessionHandle
         - eventHandle
         - xosHandle
         - intfType
         - shortName
         - groupid
         - family
         - state
        """
        self._oprot.rlock.acquire()
        try:
            self.send_OnepEvent_HsrpStateEventIDL(sessionHandle, eventHandle, xosHandle, intfType, shortName, groupid, family, state)
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()



    def send_OnepEvent_HsrpStateEventIDL(self, sessionHandle, eventHandle, xosHandle, intfType, shortName, groupid, family, state):
        self._oprot.writeMessageBegin('OnepEvent_HsrpStateEventIDL', TMessageType.CALL, self._seqid)
        args = OnepEvent_HsrpStateEventIDL_args()
        args.sessionHandle = sessionHandle
        args.eventHandle = eventHandle
        args.xosHandle = xosHandle
        args.intfType = intfType
        args.shortName = shortName
        args.groupid = groupid
        args.family = family
        args.state = state
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def OnepEvent_BDEventIDL(self, sessionHandle, eventHandle, type, id, name, xosHandle, intfType, shortName):
        """
        Parameters:
         - sessionHandle
         - eventHandle
         - type
         - id
         - name
         - xosHandle
         - intfType
         - shortName
        """
        self._oprot.rlock.acquire()
        try:
            self.send_OnepEvent_BDEventIDL(sessionHandle, eventHandle, type, id, name, xosHandle, intfType, shortName)
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()



    def send_OnepEvent_BDEventIDL(self, sessionHandle, eventHandle, type, id, name, xosHandle, intfType, shortName):
        self._oprot.writeMessageBegin('OnepEvent_BDEventIDL', TMessageType.CALL, self._seqid)
        args = OnepEvent_BDEventIDL_args()
        args.sessionHandle = sessionHandle
        args.eventHandle = eventHandle
        args.type = type
        args.id = id
        args.name = name
        args.xosHandle = xosHandle
        args.intfType = intfType
        args.shortName = shortName
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def OnepEvent_BDServiceStatusEventIDL(self, sessionHandle, eventHandle, status, resync):
        """
        Parameters:
         - sessionHandle
         - eventHandle
         - status
         - resync
        """
        self._oprot.rlock.acquire()
        try:
            self.send_OnepEvent_BDServiceStatusEventIDL(sessionHandle, eventHandle, status, resync)
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()



    def send_OnepEvent_BDServiceStatusEventIDL(self, sessionHandle, eventHandle, status, resync):
        self._oprot.writeMessageBegin('OnepEvent_BDServiceStatusEventIDL', TMessageType.CALL, self._seqid)
        args = OnepEvent_BDServiceStatusEventIDL_args()
        args.sessionHandle = sessionHandle
        args.eventHandle = eventHandle
        args.status = status
        args.resync = resync
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def OnepEvent_PortChannelEventIDL(self, sessionHandle, eventHandle, pcHandle, pcName, ifHandle, ifName, intfType, add):
        """
        Parameters:
         - sessionHandle
         - eventHandle
         - pcHandle
         - pcName
         - ifHandle
         - ifName
         - intfType
         - add
        """
        self._oprot.rlock.acquire()
        try:
            self.send_OnepEvent_PortChannelEventIDL(sessionHandle, eventHandle, pcHandle, pcName, ifHandle, ifName, intfType, add)
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()



    def send_OnepEvent_PortChannelEventIDL(self, sessionHandle, eventHandle, pcHandle, pcName, ifHandle, ifName, intfType, add):
        self._oprot.writeMessageBegin('OnepEvent_PortChannelEventIDL', TMessageType.CALL, self._seqid)
        args = OnepEvent_PortChannelEventIDL_args()
        args.sessionHandle = sessionHandle
        args.eventHandle = eventHandle
        args.pcHandle = pcHandle
        args.pcName = pcName
        args.ifHandle = ifHandle
        args.ifName = ifName
        args.intfType = intfType
        args.add = add
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()




class Processor(Iface, TProcessor):

    def __init__(self, handler):
        self._handler = handler
        self._processMap = {}
        self._processMap['OnepEvent_keepaliveHeartbeatIDL'] = Processor.process_OnepEvent_keepaliveHeartbeatIDL
        self._processMap['OnepEvent_applEventIDL'] = Processor.process_OnepEvent_applEventIDL
        self._processMap['OnepEvent_appLogLevelChangeIDL'] = Processor.process_OnepEvent_appLogLevelChangeIDL
        self._processMap['OnepEvent_configNotificationIDL'] = Processor.process_OnepEvent_configNotificationIDL
        self._processMap['OnepEvent_showDataIDL'] = Processor.process_OnepEvent_showDataIDL
        self._processMap['OnepEvent_cliEventIDL'] = Processor.process_OnepEvent_cliEventIDL
        self._processMap['OnepEvent_cdpEventIDL'] = Processor.process_OnepEvent_cdpEventIDL
        self._processMap['OnepEvent_syslogEventIDL'] = Processor.process_OnepEvent_syslogEventIDL
        self._processMap['OnepEvent_oirEventIDL'] = Processor.process_OnepEvent_oirEventIDL
        self._processMap['OnepEvent_InterfaceStateEventIDL'] = Processor.process_OnepEvent_InterfaceStateEventIDL
        self._processMap['OnepEvent_InterfaceStatisticsEventIDL'] = Processor.process_OnepEvent_InterfaceStatisticsEventIDL
        self._processMap['OnepEvent_InterfaceAddrChangeEventIDL'] = Processor.process_OnepEvent_InterfaceAddrChangeEventIDL
        self._processMap['OnepEvent_InterfaceCreateDeleteEventIDL'] = Processor.process_OnepEvent_InterfaceCreateDeleteEventIDL
        self._processMap['OnepEvent_InterfaceCTXEnableDisableEventIDL'] = Processor.process_OnepEvent_InterfaceCTXEnableDisableEventIDL
        self._processMap['OnepEvent_InterfaceStatisticsPollEventIDL'] = Processor.process_OnepEvent_InterfaceStatisticsPollEventIDL
        self._processMap['OnepEvent_srvcDiscoveryEventIDL'] = Processor.process_OnepEvent_srvcDiscoveryEventIDL
        self._processMap['OnepEvent_vtyEventIDL'] = Processor.process_OnepEvent_vtyEventIDL
        self._processMap['OnepEvent_capIntIDL'] = Processor.process_OnepEvent_capIntIDL
        self._processMap['OnepEvent_capStrIDL'] = Processor.process_OnepEvent_capStrIDL
        self._processMap['OnepEvent_ContainerSrvChangeEventIDL'] = Processor.process_OnepEvent_ContainerSrvChangeEventIDL
        self._processMap['OnepEvent_ContainerSrvInfoRequestIDL'] = Processor.process_OnepEvent_ContainerSrvInfoRequestIDL
        self._processMap['OnepEvent_InterfaceMtuEventIDL'] = Processor.process_OnepEvent_InterfaceMtuEventIDL
        self._processMap['OnepEvent_InterfaceSpeedEventIDL'] = Processor.process_OnepEvent_InterfaceSpeedEventIDL
        self._processMap['OnepEvent_InterfaceDuplexModeEventIDL'] = Processor.process_OnepEvent_InterfaceDuplexModeEventIDL
        self._processMap['OnepEvent_InterfaceAutoNegotiateEventIDL'] = Processor.process_OnepEvent_InterfaceAutoNegotiateEventIDL
        self._processMap['OnepEvent_InterfaceLayer2ModeEventIDL'] = Processor.process_OnepEvent_InterfaceLayer2ModeEventIDL
        self._processMap['OnepEvent_InterfaceFlowcontrolEventIDL'] = Processor.process_OnepEvent_InterfaceFlowcontrolEventIDL
        self._processMap['OnepEvent_InterfaceForwardClassIDEventIDL'] = Processor.process_OnepEvent_InterfaceForwardClassIDEventIDL
        self._processMap['OnepEvent_InterfaceBandwidthEventIDL'] = Processor.process_OnepEvent_InterfaceBandwidthEventIDL
        self._processMap['OnepEvent_InterfaceVlanEventIDL'] = Processor.process_OnepEvent_InterfaceVlanEventIDL
        self._processMap['OnepEvent_InterfaceVrfEventIDL'] = Processor.process_OnepEvent_InterfaceVrfEventIDL
        self._processMap['OnepEvent_HsrpStateEventIDL'] = Processor.process_OnepEvent_HsrpStateEventIDL
        self._processMap['OnepEvent_BDEventIDL'] = Processor.process_OnepEvent_BDEventIDL
        self._processMap['OnepEvent_BDServiceStatusEventIDL'] = Processor.process_OnepEvent_BDServiceStatusEventIDL
        self._processMap['OnepEvent_PortChannelEventIDL'] = Processor.process_OnepEvent_PortChannelEventIDL



    def process(self, iprot, oprot):
        (name, type, seqid,) = iprot.readMessageBegin()
        if name not in self._processMap:
            iprot.skip(TType.STRUCT)
            iprot.readMessageEnd()
            x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % name)
            oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
            x.write(oprot)
            oprot.writeMessageEnd()
            oprot.trans.flush()
            return 
        self._processMap[name](self, seqid, iprot, oprot)
        return True



    def process_OnepEvent_keepaliveHeartbeatIDL(self, seqid, iprot, oprot):
        args = OnepEvent_keepaliveHeartbeatIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        self._handler.OnepEvent_keepaliveHeartbeatIDL(args.sessionHandle)



    def process_OnepEvent_applEventIDL(self, seqid, iprot, oprot):
        args = OnepEvent_applEventIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        self._handler.OnepEvent_applEventIDL(args.sessionHandle, args.eventHandle, args.applID, args.type, args.data1, args.data2, args.data3, args.data4)



    def process_OnepEvent_appLogLevelChangeIDL(self, seqid, iprot, oprot):
        args = OnepEvent_appLogLevelChangeIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        self._handler.OnepEvent_appLogLevelChangeIDL(args.sessionHandle, args.level, args.dummy)



    def process_OnepEvent_configNotificationIDL(self, seqid, iprot, oprot):
        args = OnepEvent_configNotificationIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        self._handler.OnepEvent_configNotificationIDL(args.sessionHandle, args.cfg_data_name, args.cfg_data_value)



    def process_OnepEvent_showDataIDL(self, seqid, iprot, oprot):
        args = OnepEvent_showDataIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        self._handler.OnepEvent_showDataIDL(args.sessionHandle, args.show_data_name)



    def process_OnepEvent_cliEventIDL(self, seqid, iprot, oprot):
        args = OnepEvent_cliEventIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        self._handler.OnepEvent_cliEventIDL(args.sessionHandle, args.eventHandle, args.msgCount, args.tty, args.errorCode, args.sync, args.message)



    def process_OnepEvent_cdpEventIDL(self, seqid, iprot, oprot):
        args = OnepEvent_cdpEventIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        self._handler.OnepEvent_cdpEventIDL(args.sessionHandle, args.eventHandle, args.xosHandle, args.name, args.type, args.notifyType, args.neighborName, args.holdTime, args.mgmtDomain, args.platform, args.version, args.capabilities, args.addresses, args.neighborIntfName)



    def process_OnepEvent_syslogEventIDL(self, seqid, iprot, oprot):
        args = OnepEvent_syslogEventIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        self._handler.OnepEvent_syslogEventIDL(args.sessionHandle, args.eventHandle, args.msgCount, args.priority, args.message)



    def process_OnepEvent_oirEventIDL(self, seqid, iprot, oprot):
        args = OnepEvent_oirEventIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        self._handler.OnepEvent_oirEventIDL(args.sessionHandle, args.eventHandle, args.slot, args.oirType)



    def process_OnepEvent_InterfaceStateEventIDL(self, seqid, iprot, oprot):
        args = OnepEvent_InterfaceStateEventIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        self._handler.OnepEvent_InterfaceStateEventIDL(args.sessionHandle, args.eventHandle, args.xosHandle, args.intfType, args.stateEventType, args.intfState, args.shortName, args.link, args.lineproto)



    def process_OnepEvent_InterfaceStatisticsEventIDL(self, seqid, iprot, oprot):
        args = OnepEvent_InterfaceStatisticsEventIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        self._handler.OnepEvent_InterfaceStatisticsEventIDL(args.sessionHandle, args.eventHandle, args.xosHandle, args.intfType, args.parameter, args.isIncrement, args.isExitEvent, args.value, args.deltaValue, args.shortName)



    def process_OnepEvent_InterfaceAddrChangeEventIDL(self, seqid, iprot, oprot):
        args = OnepEvent_InterfaceAddrChangeEventIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        self._handler.OnepEvent_InterfaceAddrChangeEventIDL(args.sessionHandle, args.eventHandle, args.intfXosHandle, args.intfName, args.intfType, args.oldAddress, args.newAddress, args.oldPrefix, args.newPrefix)



    def process_OnepEvent_InterfaceCreateDeleteEventIDL(self, seqid, iprot, oprot):
        args = OnepEvent_InterfaceCreateDeleteEventIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        self._handler.OnepEvent_InterfaceCreateDeleteEventIDL(args.sessionHandle, args.eventHandle, args.intfXosHandle, args.intfName, args.intfType, args.isCreated, args.isOir)



    def process_OnepEvent_InterfaceCTXEnableDisableEventIDL(self, seqid, iprot, oprot):
        args = OnepEvent_InterfaceCTXEnableDisableEventIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        self._handler.OnepEvent_InterfaceCTXEnableDisableEventIDL(args.sessionHandle, args.eventHandle, args.intfXosHandle, args.intfName, args.intfType, args.oprType)



    def process_OnepEvent_InterfaceStatisticsPollEventIDL(self, seqid, iprot, oprot):
        args = OnepEvent_InterfaceStatisticsPollEventIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        self._handler.OnepEvent_InterfaceStatisticsPollEventIDL(args.sessionHandle, args.eventHandle, args.intfXosHandle, args.intfName, args.intfType, args.intfstats)



    def process_OnepEvent_srvcDiscoveryEventIDL(self, seqid, iprot, oprot):
        args = OnepEvent_srvcDiscoveryEventIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        self._handler.OnepEvent_srvcDiscoveryEventIDL(args.sessionHandle, args.eventHandle, args.discoveryType, args.ssId, args.ssState, args.veridl, args.neAddr)



    def process_OnepEvent_vtyEventIDL(self, seqid, iprot, oprot):
        args = OnepEvent_vtyEventIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        self._handler.OnepEvent_vtyEventIDL(args.sessionHandle, args.execHandle, args.state, args.msgType, args.data)



    def process_OnepEvent_capIntIDL(self, seqid, iprot, oprot):
        args = OnepEvent_capIntIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        self._handler.OnepEvent_capIntIDL(args.sessionHandle, args.capabilty_name, args.capabilty_value)



    def process_OnepEvent_capStrIDL(self, seqid, iprot, oprot):
        args = OnepEvent_capStrIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        self._handler.OnepEvent_capStrIDL(args.sessionHandle, args.capabilty_name, args.capabilty_value)



    def process_OnepEvent_ContainerSrvChangeEventIDL(self, seqid, iprot, oprot):
        args = OnepEvent_ContainerSrvChangeEventIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        self._handler.OnepEvent_ContainerSrvChangeEventIDL(args.sessionHandle, args.eventtype, args.adding, args.mask, args.MacID, args.Addr)



    def process_OnepEvent_ContainerSrvInfoRequestIDL(self, seqid, iprot, oprot):
        args = OnepEvent_ContainerSrvInfoRequestIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        self._handler.OnepEvent_ContainerSrvInfoRequestIDL(args.sessionHandle, args.eventtype, args.transactionID, args.MacID, args.extrainfo)



    def process_OnepEvent_InterfaceMtuEventIDL(self, seqid, iprot, oprot):
        args = OnepEvent_InterfaceMtuEventIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        self._handler.OnepEvent_InterfaceMtuEventIDL(args.sessionHandle, args.eventHandle, args.xosHandle, args.intfType, args.shortName, args.mtu)



    def process_OnepEvent_InterfaceSpeedEventIDL(self, seqid, iprot, oprot):
        args = OnepEvent_InterfaceSpeedEventIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        self._handler.OnepEvent_InterfaceSpeedEventIDL(args.sessionHandle, args.eventHandle, args.xosHandle, args.intfType, args.shortName, args.speed, args.configType)



    def process_OnepEvent_InterfaceDuplexModeEventIDL(self, seqid, iprot, oprot):
        args = OnepEvent_InterfaceDuplexModeEventIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        self._handler.OnepEvent_InterfaceDuplexModeEventIDL(args.sessionHandle, args.eventHandle, args.xosHandle, args.intfType, args.shortName, args.duplexMode, args.configType)



    def process_OnepEvent_InterfaceAutoNegotiateEventIDL(self, seqid, iprot, oprot):
        args = OnepEvent_InterfaceAutoNegotiateEventIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        self._handler.OnepEvent_InterfaceAutoNegotiateEventIDL(args.sessionHandle, args.eventHandle, args.xosHandle, args.intfType, args.shortName, args.autoNeg, args.configType)



    def process_OnepEvent_InterfaceLayer2ModeEventIDL(self, seqid, iprot, oprot):
        args = OnepEvent_InterfaceLayer2ModeEventIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        self._handler.OnepEvent_InterfaceLayer2ModeEventIDL(args.sessionHandle, args.eventHandle, args.xosHandle, args.intfType, args.shortName, args.laye2Mode)



    def process_OnepEvent_InterfaceFlowcontrolEventIDL(self, seqid, iprot, oprot):
        args = OnepEvent_InterfaceFlowcontrolEventIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        self._handler.OnepEvent_InterfaceFlowcontrolEventIDL(args.sessionHandle, args.eventHandle, args.xosHandle, args.intfType, args.shortName, args.inFlow, args.outFlow, args.configType)



    def process_OnepEvent_InterfaceForwardClassIDEventIDL(self, seqid, iprot, oprot):
        args = OnepEvent_InterfaceForwardClassIDEventIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        self._handler.OnepEvent_InterfaceForwardClassIDEventIDL(args.sessionHandle, args.eventHandle, args.xosHandle, args.intfType, args.shortName, args.fwdClassID)



    def process_OnepEvent_InterfaceBandwidthEventIDL(self, seqid, iprot, oprot):
        args = OnepEvent_InterfaceBandwidthEventIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        self._handler.OnepEvent_InterfaceBandwidthEventIDL(args.sessionHandle, args.eventHandle, args.xosHandle, args.intfType, args.shortName, args.bandwidth, args.is_tx)



    def process_OnepEvent_InterfaceVlanEventIDL(self, seqid, iprot, oprot):
        args = OnepEvent_InterfaceVlanEventIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        self._handler.OnepEvent_InterfaceVlanEventIDL(args.sessionHandle, args.eventHandle, args.xosHandle, args.intfType, args.shortName, args.vlan, args.vlanEventType)



    def process_OnepEvent_InterfaceVrfEventIDL(self, seqid, iprot, oprot):
        args = OnepEvent_InterfaceVrfEventIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        self._handler.OnepEvent_InterfaceVrfEventIDL(args.sessionHandle, args.eventHandle, args.xosHandle, args.intfType, args.shortName, args.vrf, args.vrfEventType)



    def process_OnepEvent_HsrpStateEventIDL(self, seqid, iprot, oprot):
        args = OnepEvent_HsrpStateEventIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        self._handler.OnepEvent_HsrpStateEventIDL(args.sessionHandle, args.eventHandle, args.xosHandle, args.intfType, args.shortName, args.groupid, args.family, args.state)



    def process_OnepEvent_BDEventIDL(self, seqid, iprot, oprot):
        args = OnepEvent_BDEventIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        self._handler.OnepEvent_BDEventIDL(args.sessionHandle, args.eventHandle, args.type, args.id, args.name, args.xosHandle, args.intfType, args.shortName)



    def process_OnepEvent_BDServiceStatusEventIDL(self, seqid, iprot, oprot):
        args = OnepEvent_BDServiceStatusEventIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        self._handler.OnepEvent_BDServiceStatusEventIDL(args.sessionHandle, args.eventHandle, args.status, args.resync)



    def process_OnepEvent_PortChannelEventIDL(self, seqid, iprot, oprot):
        args = OnepEvent_PortChannelEventIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        self._handler.OnepEvent_PortChannelEventIDL(args.sessionHandle, args.eventHandle, args.pcHandle, args.pcName, args.ifHandle, args.ifName, args.intfType, args.add)




class OnepEvent_keepaliveHeartbeatIDL_args(object):
    """
    Attributes:
     - sessionHandle
    """

    thrift_spec = (None, (1,
      TType.I32,
      'sessionHandle',
      None,
      None))

    def __init__(self, sessionHandle = None):
        self.sessionHandle = sessionHandle



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.sessionHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()

        iprot.readStructEnd()



    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return 
        oprot.writeStructBegin('OnepEvent_keepaliveHeartbeatIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

        def validate(self):
            pass





    def __repr__(self):
        L = [ '%s=%r' % (key, value) for (key, value,) in self.__dict__.iteritems() ]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))



    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__



    def __ne__(self, other):
        return not self == other




class OnepEvent_applEventIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - eventHandle
     - applID
     - type
     - data1
     - data2
     - data3
     - data4
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionHandle',
      None,
      None),
     (2,
      TType.I32,
      'eventHandle',
      None,
      None),
     (3,
      TType.I32,
      'applID',
      None,
      None),
     (4,
      TType.I32,
      'type',
      None,
      None),
     (5,
      TType.STRING,
      'data1',
      None,
      None),
     (6,
      TType.STRING,
      'data2',
      None,
      None),
     (7,
      TType.STRING,
      'data3',
      None,
      None),
     (8,
      TType.STRING,
      'data4',
      None,
      None))

    def __init__(self, sessionHandle = None, eventHandle = None, applID = None, type = None, data1 = None, data2 = None, data3 = None, data4 = None):
        self.sessionHandle = sessionHandle
        self.eventHandle = eventHandle
        self.applID = applID
        self.type = type
        self.data1 = data1
        self.data2 = data2
        self.data3 = data3
        self.data4 = data4



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.sessionHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.eventHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.applID = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.data1 = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRING:
                    self.data2 = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.STRING:
                    self.data3 = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.STRING:
                    self.data4 = iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()

        iprot.readStructEnd()



    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return 
        oprot.writeStructBegin('OnepEvent_applEventIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.eventHandle != None:
            oprot.writeFieldBegin('eventHandle', TType.I32, 2)
            oprot.writeI32(self.eventHandle)
            oprot.writeFieldEnd()
        if self.applID != None:
            oprot.writeFieldBegin('applID', TType.I32, 3)
            oprot.writeI32(self.applID)
            oprot.writeFieldEnd()
        if self.type != None:
            oprot.writeFieldBegin('type', TType.I32, 4)
            oprot.writeI32(self.type)
            oprot.writeFieldEnd()
        if self.data1 != None:
            oprot.writeFieldBegin('data1', TType.STRING, 5)
            oprot.writeString(self.data1)
            oprot.writeFieldEnd()
        if self.data2 != None:
            oprot.writeFieldBegin('data2', TType.STRING, 6)
            oprot.writeString(self.data2)
            oprot.writeFieldEnd()
        if self.data3 != None:
            oprot.writeFieldBegin('data3', TType.STRING, 7)
            oprot.writeString(self.data3)
            oprot.writeFieldEnd()
        if self.data4 != None:
            oprot.writeFieldBegin('data4', TType.STRING, 8)
            oprot.writeString(self.data4)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

        def validate(self):
            pass





    def __repr__(self):
        L = [ '%s=%r' % (key, value) for (key, value,) in self.__dict__.iteritems() ]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))



    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__



    def __ne__(self, other):
        return not self == other




class OnepEvent_appLogLevelChangeIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - level
     - dummy
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionHandle',
      None,
      None),
     (2,
      TType.I32,
      'level',
      None,
      None),
     (3,
      TType.STRING,
      'dummy',
      None,
      None))

    def __init__(self, sessionHandle = None, level = None, dummy = None):
        self.sessionHandle = sessionHandle
        self.level = level
        self.dummy = dummy



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.sessionHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.level = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.dummy = iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()

        iprot.readStructEnd()



    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return 
        oprot.writeStructBegin('OnepEvent_appLogLevelChangeIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.level != None:
            oprot.writeFieldBegin('level', TType.I32, 2)
            oprot.writeI32(self.level)
            oprot.writeFieldEnd()
        if self.dummy != None:
            oprot.writeFieldBegin('dummy', TType.STRING, 3)
            oprot.writeString(self.dummy)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

        def validate(self):
            pass





    def __repr__(self):
        L = [ '%s=%r' % (key, value) for (key, value,) in self.__dict__.iteritems() ]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))



    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__



    def __ne__(self, other):
        return not self == other




class OnepEvent_configNotificationIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - cfg_data_name
     - cfg_data_value
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionHandle',
      None,
      None),
     (2,
      TType.STRING,
      'cfg_data_name',
      None,
      None),
     (3,
      TType.STRING,
      'cfg_data_value',
      None,
      None))

    def __init__(self, sessionHandle = None, cfg_data_name = None, cfg_data_value = None):
        self.sessionHandle = sessionHandle
        self.cfg_data_name = cfg_data_name
        self.cfg_data_value = cfg_data_value



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.sessionHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.cfg_data_name = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.cfg_data_value = iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()

        iprot.readStructEnd()



    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return 
        oprot.writeStructBegin('OnepEvent_configNotificationIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.cfg_data_name != None:
            oprot.writeFieldBegin('cfg_data_name', TType.STRING, 2)
            oprot.writeString(self.cfg_data_name)
            oprot.writeFieldEnd()
        if self.cfg_data_value != None:
            oprot.writeFieldBegin('cfg_data_value', TType.STRING, 3)
            oprot.writeString(self.cfg_data_value)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

        def validate(self):
            pass





    def __repr__(self):
        L = [ '%s=%r' % (key, value) for (key, value,) in self.__dict__.iteritems() ]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))



    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__



    def __ne__(self, other):
        return not self == other




class OnepEvent_showDataIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - show_data_name
    """

    thrift_spec = (None, (1,
      TType.I32,
      'sessionHandle',
      None,
      None), (2,
      TType.STRING,
      'show_data_name',
      None,
      None))

    def __init__(self, sessionHandle = None, show_data_name = None):
        self.sessionHandle = sessionHandle
        self.show_data_name = show_data_name



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.sessionHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.show_data_name = iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()

        iprot.readStructEnd()



    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return 
        oprot.writeStructBegin('OnepEvent_showDataIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.show_data_name != None:
            oprot.writeFieldBegin('show_data_name', TType.STRING, 2)
            oprot.writeString(self.show_data_name)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

        def validate(self):
            pass





    def __repr__(self):
        L = [ '%s=%r' % (key, value) for (key, value,) in self.__dict__.iteritems() ]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))



    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__



    def __ne__(self, other):
        return not self == other




class OnepEvent_cliEventIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - eventHandle
     - msgCount
     - tty
     - errorCode
     - sync
     - message
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionHandle',
      None,
      None),
     (2,
      TType.I32,
      'eventHandle',
      None,
      None),
     (3,
      TType.I32,
      'msgCount',
      None,
      None),
     (4,
      TType.I32,
      'tty',
      None,
      None),
     (5,
      TType.I32,
      'errorCode',
      None,
      None),
     (6,
      TType.I32,
      'sync',
      None,
      None),
     (7,
      TType.STRING,
      'message',
      None,
      None))

    def __init__(self, sessionHandle = None, eventHandle = None, msgCount = None, tty = None, errorCode = None, sync = None, message = None):
        self.sessionHandle = sessionHandle
        self.eventHandle = eventHandle
        self.msgCount = msgCount
        self.tty = tty
        self.errorCode = errorCode
        self.sync = sync
        self.message = message



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.sessionHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.eventHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.msgCount = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.tty = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.errorCode = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I32:
                    self.sync = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.STRING:
                    self.message = iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()

        iprot.readStructEnd()



    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return 
        oprot.writeStructBegin('OnepEvent_cliEventIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.eventHandle != None:
            oprot.writeFieldBegin('eventHandle', TType.I32, 2)
            oprot.writeI32(self.eventHandle)
            oprot.writeFieldEnd()
        if self.msgCount != None:
            oprot.writeFieldBegin('msgCount', TType.I32, 3)
            oprot.writeI32(self.msgCount)
            oprot.writeFieldEnd()
        if self.tty != None:
            oprot.writeFieldBegin('tty', TType.I32, 4)
            oprot.writeI32(self.tty)
            oprot.writeFieldEnd()
        if self.errorCode != None:
            oprot.writeFieldBegin('errorCode', TType.I32, 5)
            oprot.writeI32(self.errorCode)
            oprot.writeFieldEnd()
        if self.sync != None:
            oprot.writeFieldBegin('sync', TType.I32, 6)
            oprot.writeI32(self.sync)
            oprot.writeFieldEnd()
        if self.message != None:
            oprot.writeFieldBegin('message', TType.STRING, 7)
            oprot.writeString(self.message)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

        def validate(self):
            pass





    def __repr__(self):
        L = [ '%s=%r' % (key, value) for (key, value,) in self.__dict__.iteritems() ]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))



    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__



    def __ne__(self, other):
        return not self == other




class OnepEvent_cdpEventIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - eventHandle
     - xosHandle
     - name
     - type
     - notifyType
     - neighborName
     - holdTime
     - mgmtDomain
     - platform
     - version
     - capabilities
     - addresses
     - neighborIntfName
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionHandle',
      None,
      None),
     (2,
      TType.I32,
      'eventHandle',
      None,
      None),
     (3,
      TType.I64,
      'xosHandle',
      None,
      None),
     (4,
      TType.STRING,
      'name',
      None,
      None),
     (5,
      TType.I32,
      'type',
      None,
      None),
     (6,
      TType.I32,
      'notifyType',
      None,
      None),
     (7,
      TType.STRING,
      'neighborName',
      None,
      None),
     (8,
      TType.I32,
      'holdTime',
      None,
      None),
     (9,
      TType.STRING,
      'mgmtDomain',
      None,
      None),
     (10,
      TType.STRING,
      'platform',
      None,
      None),
     (11,
      TType.STRING,
      'version',
      None,
      None),
     (12,
      TType.STRING,
      'capabilities',
      None,
      None),
     (13,
      TType.LIST,
      'addresses',
      (TType.STRUCT, (SharedOut.ttypes.NetworkAddressOutIDL, SharedOut.ttypes.NetworkAddressOutIDL.thrift_spec)),
      None),
     (14,
      TType.STRING,
      'neighborIntfName',
      None,
      None))

    def __init__(self, sessionHandle = None, eventHandle = None, xosHandle = None, name = None, type = None, notifyType = None, neighborName = None, holdTime = None, mgmtDomain = None, platform = None, version = None, capabilities = None, addresses = None, neighborIntfName = None):
        self.sessionHandle = sessionHandle
        self.eventHandle = eventHandle
        self.xosHandle = xosHandle
        self.name = name
        self.type = type
        self.notifyType = notifyType
        self.neighborName = neighborName
        self.holdTime = holdTime
        self.mgmtDomain = mgmtDomain
        self.platform = platform
        self.version = version
        self.capabilities = capabilities
        self.addresses = addresses
        self.neighborIntfName = neighborIntfName



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.sessionHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.eventHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I64:
                    self.xosHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.name = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I32:
                    self.notifyType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.STRING:
                    self.neighborName = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.I32:
                    self.holdTime = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.STRING:
                    self.mgmtDomain = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.STRING:
                    self.platform = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.STRING:
                    self.version = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 12:
                if ftype == TType.STRING:
                    self.capabilities = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 13:
                if ftype == TType.LIST:
                    self.addresses = []
                    (_etype3, _size0,) = iprot.readListBegin()
                    for _i4 in xrange(_size0):
                        _elem5 = SharedOut.ttypes.NetworkAddressOutIDL()
                        _elem5.read(iprot)
                        self.addresses.append(_elem5)

                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 14:
                if ftype == TType.STRING:
                    self.neighborIntfName = iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()

        iprot.readStructEnd()



    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return 
        oprot.writeStructBegin('OnepEvent_cdpEventIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.eventHandle != None:
            oprot.writeFieldBegin('eventHandle', TType.I32, 2)
            oprot.writeI32(self.eventHandle)
            oprot.writeFieldEnd()
        if self.xosHandle != None:
            oprot.writeFieldBegin('xosHandle', TType.I64, 3)
            oprot.writeI64(self.xosHandle)
            oprot.writeFieldEnd()
        if self.name != None:
            oprot.writeFieldBegin('name', TType.STRING, 4)
            oprot.writeString(self.name)
            oprot.writeFieldEnd()
        if self.type != None:
            oprot.writeFieldBegin('type', TType.I32, 5)
            oprot.writeI32(self.type)
            oprot.writeFieldEnd()
        if self.notifyType != None:
            oprot.writeFieldBegin('notifyType', TType.I32, 6)
            oprot.writeI32(self.notifyType)
            oprot.writeFieldEnd()
        if self.neighborName != None:
            oprot.writeFieldBegin('neighborName', TType.STRING, 7)
            oprot.writeString(self.neighborName)
            oprot.writeFieldEnd()
        if self.holdTime != None:
            oprot.writeFieldBegin('holdTime', TType.I32, 8)
            oprot.writeI32(self.holdTime)
            oprot.writeFieldEnd()
        if self.mgmtDomain != None:
            oprot.writeFieldBegin('mgmtDomain', TType.STRING, 9)
            oprot.writeString(self.mgmtDomain)
            oprot.writeFieldEnd()
        if self.platform != None:
            oprot.writeFieldBegin('platform', TType.STRING, 10)
            oprot.writeString(self.platform)
            oprot.writeFieldEnd()
        if self.version != None:
            oprot.writeFieldBegin('version', TType.STRING, 11)
            oprot.writeString(self.version)
            oprot.writeFieldEnd()
        if self.capabilities != None:
            oprot.writeFieldBegin('capabilities', TType.STRING, 12)
            oprot.writeString(self.capabilities)
            oprot.writeFieldEnd()
        if self.addresses != None:
            oprot.writeFieldBegin('addresses', TType.LIST, 13)
            oprot.writeListBegin(TType.STRUCT, len(self.addresses))
            for iter6 in self.addresses:
                iter6.write(oprot)

            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.neighborIntfName != None:
            oprot.writeFieldBegin('neighborIntfName', TType.STRING, 14)
            oprot.writeString(self.neighborIntfName)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

        def validate(self):
            pass





    def __repr__(self):
        L = [ '%s=%r' % (key, value) for (key, value,) in self.__dict__.iteritems() ]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))



    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__



    def __ne__(self, other):
        return not self == other




class OnepEvent_syslogEventIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - eventHandle
     - msgCount
     - priority
     - message
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionHandle',
      None,
      None),
     (2,
      TType.I32,
      'eventHandle',
      None,
      None),
     (3,
      TType.I32,
      'msgCount',
      None,
      None),
     (4,
      TType.I32,
      'priority',
      None,
      None),
     (5,
      TType.STRING,
      'message',
      None,
      None))

    def __init__(self, sessionHandle = None, eventHandle = None, msgCount = None, priority = None, message = None):
        self.sessionHandle = sessionHandle
        self.eventHandle = eventHandle
        self.msgCount = msgCount
        self.priority = priority
        self.message = message



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.sessionHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.eventHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.msgCount = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.priority = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.message = iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()

        iprot.readStructEnd()



    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return 
        oprot.writeStructBegin('OnepEvent_syslogEventIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.eventHandle != None:
            oprot.writeFieldBegin('eventHandle', TType.I32, 2)
            oprot.writeI32(self.eventHandle)
            oprot.writeFieldEnd()
        if self.msgCount != None:
            oprot.writeFieldBegin('msgCount', TType.I32, 3)
            oprot.writeI32(self.msgCount)
            oprot.writeFieldEnd()
        if self.priority != None:
            oprot.writeFieldBegin('priority', TType.I32, 4)
            oprot.writeI32(self.priority)
            oprot.writeFieldEnd()
        if self.message != None:
            oprot.writeFieldBegin('message', TType.STRING, 5)
            oprot.writeString(self.message)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

        def validate(self):
            pass





    def __repr__(self):
        L = [ '%s=%r' % (key, value) for (key, value,) in self.__dict__.iteritems() ]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))



    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__



    def __ne__(self, other):
        return not self == other




class OnepEvent_oirEventIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - eventHandle
     - slot
     - oirType
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionHandle',
      None,
      None),
     (2,
      TType.I32,
      'eventHandle',
      None,
      None),
     (3,
      TType.I32,
      'slot',
      None,
      None),
     (4,
      TType.I32,
      'oirType',
      None,
      None))

    def __init__(self, sessionHandle = None, eventHandle = None, slot = None, oirType = None):
        self.sessionHandle = sessionHandle
        self.eventHandle = eventHandle
        self.slot = slot
        self.oirType = oirType



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.sessionHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.eventHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.slot = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.oirType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()

        iprot.readStructEnd()



    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return 
        oprot.writeStructBegin('OnepEvent_oirEventIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.eventHandle != None:
            oprot.writeFieldBegin('eventHandle', TType.I32, 2)
            oprot.writeI32(self.eventHandle)
            oprot.writeFieldEnd()
        if self.slot != None:
            oprot.writeFieldBegin('slot', TType.I32, 3)
            oprot.writeI32(self.slot)
            oprot.writeFieldEnd()
        if self.oirType != None:
            oprot.writeFieldBegin('oirType', TType.I32, 4)
            oprot.writeI32(self.oirType)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

        def validate(self):
            pass





    def __repr__(self):
        L = [ '%s=%r' % (key, value) for (key, value,) in self.__dict__.iteritems() ]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))



    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__



    def __ne__(self, other):
        return not self == other




class OnepEvent_InterfaceStateEventIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - eventHandle
     - xosHandle
     - intfType
     - stateEventType
     - intfState
     - shortName
     - link
     - lineproto
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionHandle',
      None,
      None),
     (2,
      TType.I32,
      'eventHandle',
      None,
      None),
     (3,
      TType.I64,
      'xosHandle',
      None,
      None),
     (4,
      TType.I32,
      'intfType',
      None,
      None),
     (5,
      TType.I32,
      'stateEventType',
      None,
      None),
     (6,
      TType.I32,
      'intfState',
      None,
      None),
     (7,
      TType.STRING,
      'shortName',
      None,
      None),
     (8,
      TType.I32,
      'link',
      None,
      None),
     (9,
      TType.I32,
      'lineproto',
      None,
      None))

    def __init__(self, sessionHandle = None, eventHandle = None, xosHandle = None, intfType = None, stateEventType = None, intfState = None, shortName = None, link = None, lineproto = None):
        self.sessionHandle = sessionHandle
        self.eventHandle = eventHandle
        self.xosHandle = xosHandle
        self.intfType = intfType
        self.stateEventType = stateEventType
        self.intfState = intfState
        self.shortName = shortName
        self.link = link
        self.lineproto = lineproto



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.sessionHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.eventHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I64:
                    self.xosHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.intfType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.stateEventType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I32:
                    self.intfState = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.STRING:
                    self.shortName = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.I32:
                    self.link = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.I32:
                    self.lineproto = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()

        iprot.readStructEnd()



    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return 
        oprot.writeStructBegin('OnepEvent_InterfaceStateEventIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.eventHandle != None:
            oprot.writeFieldBegin('eventHandle', TType.I32, 2)
            oprot.writeI32(self.eventHandle)
            oprot.writeFieldEnd()
        if self.xosHandle != None:
            oprot.writeFieldBegin('xosHandle', TType.I64, 3)
            oprot.writeI64(self.xosHandle)
            oprot.writeFieldEnd()
        if self.intfType != None:
            oprot.writeFieldBegin('intfType', TType.I32, 4)
            oprot.writeI32(self.intfType)
            oprot.writeFieldEnd()
        if self.stateEventType != None:
            oprot.writeFieldBegin('stateEventType', TType.I32, 5)
            oprot.writeI32(self.stateEventType)
            oprot.writeFieldEnd()
        if self.intfState != None:
            oprot.writeFieldBegin('intfState', TType.I32, 6)
            oprot.writeI32(self.intfState)
            oprot.writeFieldEnd()
        if self.shortName != None:
            oprot.writeFieldBegin('shortName', TType.STRING, 7)
            oprot.writeString(self.shortName)
            oprot.writeFieldEnd()
        if self.link != None:
            oprot.writeFieldBegin('link', TType.I32, 8)
            oprot.writeI32(self.link)
            oprot.writeFieldEnd()
        if self.lineproto != None:
            oprot.writeFieldBegin('lineproto', TType.I32, 9)
            oprot.writeI32(self.lineproto)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

        def validate(self):
            pass





    def __repr__(self):
        L = [ '%s=%r' % (key, value) for (key, value,) in self.__dict__.iteritems() ]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))



    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__



    def __ne__(self, other):
        return not self == other




class OnepEvent_InterfaceStatisticsEventIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - eventHandle
     - xosHandle
     - intfType
     - parameter
     - isIncrement
     - isExitEvent
     - value
     - deltaValue
     - shortName
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionHandle',
      None,
      None),
     (2,
      TType.I32,
      'eventHandle',
      None,
      None),
     (3,
      TType.I64,
      'xosHandle',
      None,
      None),
     (4,
      TType.I32,
      'intfType',
      None,
      None),
     (5,
      TType.I32,
      'parameter',
      None,
      None),
     (6,
      TType.I32,
      'isIncrement',
      None,
      None),
     (7,
      TType.I32,
      'isExitEvent',
      None,
      None),
     (8,
      TType.I32,
      'value',
      None,
      None),
     (9,
      TType.I32,
      'deltaValue',
      None,
      None),
     (10,
      TType.STRING,
      'shortName',
      None,
      None))

    def __init__(self, sessionHandle = None, eventHandle = None, xosHandle = None, intfType = None, parameter = None, isIncrement = None, isExitEvent = None, value = None, deltaValue = None, shortName = None):
        self.sessionHandle = sessionHandle
        self.eventHandle = eventHandle
        self.xosHandle = xosHandle
        self.intfType = intfType
        self.parameter = parameter
        self.isIncrement = isIncrement
        self.isExitEvent = isExitEvent
        self.value = value
        self.deltaValue = deltaValue
        self.shortName = shortName



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.sessionHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.eventHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I64:
                    self.xosHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.intfType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.parameter = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I32:
                    self.isIncrement = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I32:
                    self.isExitEvent = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.I32:
                    self.value = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.I32:
                    self.deltaValue = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.STRING:
                    self.shortName = iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()

        iprot.readStructEnd()



    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return 
        oprot.writeStructBegin('OnepEvent_InterfaceStatisticsEventIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.eventHandle != None:
            oprot.writeFieldBegin('eventHandle', TType.I32, 2)
            oprot.writeI32(self.eventHandle)
            oprot.writeFieldEnd()
        if self.xosHandle != None:
            oprot.writeFieldBegin('xosHandle', TType.I64, 3)
            oprot.writeI64(self.xosHandle)
            oprot.writeFieldEnd()
        if self.intfType != None:
            oprot.writeFieldBegin('intfType', TType.I32, 4)
            oprot.writeI32(self.intfType)
            oprot.writeFieldEnd()
        if self.parameter != None:
            oprot.writeFieldBegin('parameter', TType.I32, 5)
            oprot.writeI32(self.parameter)
            oprot.writeFieldEnd()
        if self.isIncrement != None:
            oprot.writeFieldBegin('isIncrement', TType.I32, 6)
            oprot.writeI32(self.isIncrement)
            oprot.writeFieldEnd()
        if self.isExitEvent != None:
            oprot.writeFieldBegin('isExitEvent', TType.I32, 7)
            oprot.writeI32(self.isExitEvent)
            oprot.writeFieldEnd()
        if self.value != None:
            oprot.writeFieldBegin('value', TType.I32, 8)
            oprot.writeI32(self.value)
            oprot.writeFieldEnd()
        if self.deltaValue != None:
            oprot.writeFieldBegin('deltaValue', TType.I32, 9)
            oprot.writeI32(self.deltaValue)
            oprot.writeFieldEnd()
        if self.shortName != None:
            oprot.writeFieldBegin('shortName', TType.STRING, 10)
            oprot.writeString(self.shortName)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

        def validate(self):
            pass





    def __repr__(self):
        L = [ '%s=%r' % (key, value) for (key, value,) in self.__dict__.iteritems() ]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))



    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__



    def __ne__(self, other):
        return not self == other




class OnepEvent_InterfaceAddrChangeEventIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - eventHandle
     - intfXosHandle
     - intfName
     - intfType
     - oldAddress
     - newAddress
     - oldPrefix
     - newPrefix
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionHandle',
      None,
      None),
     (2,
      TType.I32,
      'eventHandle',
      None,
      None),
     (3,
      TType.I64,
      'intfXosHandle',
      None,
      None),
     (4,
      TType.STRING,
      'intfName',
      None,
      None),
     (5,
      TType.I32,
      'intfType',
      None,
      None),
     (6,
      TType.STRUCT,
      'oldAddress',
      (SharedOut.ttypes.NetworkAddressOutIDL, SharedOut.ttypes.NetworkAddressOutIDL.thrift_spec),
      None),
     (7,
      TType.STRUCT,
      'newAddress',
      (SharedOut.ttypes.NetworkAddressOutIDL, SharedOut.ttypes.NetworkAddressOutIDL.thrift_spec),
      None),
     (8,
      TType.STRUCT,
      'oldPrefix',
      (SharedOut.ttypes.NetworkPrefixOutIDL, SharedOut.ttypes.NetworkPrefixOutIDL.thrift_spec),
      None),
     (9,
      TType.STRUCT,
      'newPrefix',
      (SharedOut.ttypes.NetworkPrefixOutIDL, SharedOut.ttypes.NetworkPrefixOutIDL.thrift_spec),
      None))

    def __init__(self, sessionHandle = None, eventHandle = None, intfXosHandle = None, intfName = None, intfType = None, oldAddress = None, newAddress = None, oldPrefix = None, newPrefix = None):
        self.sessionHandle = sessionHandle
        self.eventHandle = eventHandle
        self.intfXosHandle = intfXosHandle
        self.intfName = intfName
        self.intfType = intfType
        self.oldAddress = oldAddress
        self.newAddress = newAddress
        self.oldPrefix = oldPrefix
        self.newPrefix = newPrefix



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.sessionHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.eventHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I64:
                    self.intfXosHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.intfName = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.intfType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRUCT:
                    self.oldAddress = SharedOut.ttypes.NetworkAddressOutIDL()
                    self.oldAddress.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.STRUCT:
                    self.newAddress = SharedOut.ttypes.NetworkAddressOutIDL()
                    self.newAddress.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.STRUCT:
                    self.oldPrefix = SharedOut.ttypes.NetworkPrefixOutIDL()
                    self.oldPrefix.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.STRUCT:
                    self.newPrefix = SharedOut.ttypes.NetworkPrefixOutIDL()
                    self.newPrefix.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()

        iprot.readStructEnd()



    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return 
        oprot.writeStructBegin('OnepEvent_InterfaceAddrChangeEventIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.eventHandle != None:
            oprot.writeFieldBegin('eventHandle', TType.I32, 2)
            oprot.writeI32(self.eventHandle)
            oprot.writeFieldEnd()
        if self.intfXosHandle != None:
            oprot.writeFieldBegin('intfXosHandle', TType.I64, 3)
            oprot.writeI64(self.intfXosHandle)
            oprot.writeFieldEnd()
        if self.intfName != None:
            oprot.writeFieldBegin('intfName', TType.STRING, 4)
            oprot.writeString(self.intfName)
            oprot.writeFieldEnd()
        if self.intfType != None:
            oprot.writeFieldBegin('intfType', TType.I32, 5)
            oprot.writeI32(self.intfType)
            oprot.writeFieldEnd()
        if self.oldAddress != None:
            oprot.writeFieldBegin('oldAddress', TType.STRUCT, 6)
            self.oldAddress.write(oprot)
            oprot.writeFieldEnd()
        if self.newAddress != None:
            oprot.writeFieldBegin('newAddress', TType.STRUCT, 7)
            self.newAddress.write(oprot)
            oprot.writeFieldEnd()
        if self.oldPrefix != None:
            oprot.writeFieldBegin('oldPrefix', TType.STRUCT, 8)
            self.oldPrefix.write(oprot)
            oprot.writeFieldEnd()
        if self.newPrefix != None:
            oprot.writeFieldBegin('newPrefix', TType.STRUCT, 9)
            self.newPrefix.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

        def validate(self):
            pass





    def __repr__(self):
        L = [ '%s=%r' % (key, value) for (key, value,) in self.__dict__.iteritems() ]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))



    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__



    def __ne__(self, other):
        return not self == other




class OnepEvent_InterfaceCreateDeleteEventIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - eventHandle
     - intfXosHandle
     - intfName
     - intfType
     - isCreated
     - isOir
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionHandle',
      None,
      None),
     (2,
      TType.I32,
      'eventHandle',
      None,
      None),
     (3,
      TType.I64,
      'intfXosHandle',
      None,
      None),
     (4,
      TType.STRING,
      'intfName',
      None,
      None),
     (5,
      TType.I32,
      'intfType',
      None,
      None),
     (6,
      TType.I32,
      'isCreated',
      None,
      None),
     (7,
      TType.I32,
      'isOir',
      None,
      None))

    def __init__(self, sessionHandle = None, eventHandle = None, intfXosHandle = None, intfName = None, intfType = None, isCreated = None, isOir = None):
        self.sessionHandle = sessionHandle
        self.eventHandle = eventHandle
        self.intfXosHandle = intfXosHandle
        self.intfName = intfName
        self.intfType = intfType
        self.isCreated = isCreated
        self.isOir = isOir



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.sessionHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.eventHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I64:
                    self.intfXosHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.intfName = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.intfType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I32:
                    self.isCreated = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I32:
                    self.isOir = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()

        iprot.readStructEnd()



    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return 
        oprot.writeStructBegin('OnepEvent_InterfaceCreateDeleteEventIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.eventHandle != None:
            oprot.writeFieldBegin('eventHandle', TType.I32, 2)
            oprot.writeI32(self.eventHandle)
            oprot.writeFieldEnd()
        if self.intfXosHandle != None:
            oprot.writeFieldBegin('intfXosHandle', TType.I64, 3)
            oprot.writeI64(self.intfXosHandle)
            oprot.writeFieldEnd()
        if self.intfName != None:
            oprot.writeFieldBegin('intfName', TType.STRING, 4)
            oprot.writeString(self.intfName)
            oprot.writeFieldEnd()
        if self.intfType != None:
            oprot.writeFieldBegin('intfType', TType.I32, 5)
            oprot.writeI32(self.intfType)
            oprot.writeFieldEnd()
        if self.isCreated != None:
            oprot.writeFieldBegin('isCreated', TType.I32, 6)
            oprot.writeI32(self.isCreated)
            oprot.writeFieldEnd()
        if self.isOir != None:
            oprot.writeFieldBegin('isOir', TType.I32, 7)
            oprot.writeI32(self.isOir)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

        def validate(self):
            pass





    def __repr__(self):
        L = [ '%s=%r' % (key, value) for (key, value,) in self.__dict__.iteritems() ]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))



    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__



    def __ne__(self, other):
        return not self == other




class OnepEvent_InterfaceCTXEnableDisableEventIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - eventHandle
     - intfXosHandle
     - intfName
     - intfType
     - oprType
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionHandle',
      None,
      None),
     (2,
      TType.I32,
      'eventHandle',
      None,
      None),
     (3,
      TType.I64,
      'intfXosHandle',
      None,
      None),
     (4,
      TType.STRING,
      'intfName',
      None,
      None),
     (5,
      TType.I32,
      'intfType',
      None,
      None),
     (6,
      TType.I32,
      'oprType',
      None,
      None))

    def __init__(self, sessionHandle = None, eventHandle = None, intfXosHandle = None, intfName = None, intfType = None, oprType = None):
        self.sessionHandle = sessionHandle
        self.eventHandle = eventHandle
        self.intfXosHandle = intfXosHandle
        self.intfName = intfName
        self.intfType = intfType
        self.oprType = oprType



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.sessionHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.eventHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I64:
                    self.intfXosHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.intfName = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.intfType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I32:
                    self.oprType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()

        iprot.readStructEnd()



    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return 
        oprot.writeStructBegin('OnepEvent_InterfaceCTXEnableDisableEventIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.eventHandle != None:
            oprot.writeFieldBegin('eventHandle', TType.I32, 2)
            oprot.writeI32(self.eventHandle)
            oprot.writeFieldEnd()
        if self.intfXosHandle != None:
            oprot.writeFieldBegin('intfXosHandle', TType.I64, 3)
            oprot.writeI64(self.intfXosHandle)
            oprot.writeFieldEnd()
        if self.intfName != None:
            oprot.writeFieldBegin('intfName', TType.STRING, 4)
            oprot.writeString(self.intfName)
            oprot.writeFieldEnd()
        if self.intfType != None:
            oprot.writeFieldBegin('intfType', TType.I32, 5)
            oprot.writeI32(self.intfType)
            oprot.writeFieldEnd()
        if self.oprType != None:
            oprot.writeFieldBegin('oprType', TType.I32, 6)
            oprot.writeI32(self.oprType)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

        def validate(self):
            pass





    def __repr__(self):
        L = [ '%s=%r' % (key, value) for (key, value,) in self.__dict__.iteritems() ]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))



    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__



    def __ne__(self, other):
        return not self == other




class OnepEvent_InterfaceStatisticsPollEventIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - eventHandle
     - intfXosHandle
     - intfName
     - intfType
     - intfstats
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionHandle',
      None,
      None),
     (2,
      TType.I32,
      'eventHandle',
      None,
      None),
     (3,
      TType.I64,
      'intfXosHandle',
      None,
      None),
     (4,
      TType.STRING,
      'intfName',
      None,
      None),
     (5,
      TType.I32,
      'intfType',
      None,
      None),
     (6,
      TType.LIST,
      'intfstats',
      (TType.STRUCT, (InterfaceStatisticsOutIDL, InterfaceStatisticsOutIDL.thrift_spec)),
      None))

    def __init__(self, sessionHandle = None, eventHandle = None, intfXosHandle = None, intfName = None, intfType = None, intfstats = None):
        self.sessionHandle = sessionHandle
        self.eventHandle = eventHandle
        self.intfXosHandle = intfXosHandle
        self.intfName = intfName
        self.intfType = intfType
        self.intfstats = intfstats



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.sessionHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.eventHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I64:
                    self.intfXosHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.intfName = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.intfType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.LIST:
                    self.intfstats = []
                    (_etype10, _size7,) = iprot.readListBegin()
                    for _i11 in xrange(_size7):
                        _elem12 = InterfaceStatisticsOutIDL()
                        _elem12.read(iprot)
                        self.intfstats.append(_elem12)

                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()

        iprot.readStructEnd()



    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return 
        oprot.writeStructBegin('OnepEvent_InterfaceStatisticsPollEventIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.eventHandle != None:
            oprot.writeFieldBegin('eventHandle', TType.I32, 2)
            oprot.writeI32(self.eventHandle)
            oprot.writeFieldEnd()
        if self.intfXosHandle != None:
            oprot.writeFieldBegin('intfXosHandle', TType.I64, 3)
            oprot.writeI64(self.intfXosHandle)
            oprot.writeFieldEnd()
        if self.intfName != None:
            oprot.writeFieldBegin('intfName', TType.STRING, 4)
            oprot.writeString(self.intfName)
            oprot.writeFieldEnd()
        if self.intfType != None:
            oprot.writeFieldBegin('intfType', TType.I32, 5)
            oprot.writeI32(self.intfType)
            oprot.writeFieldEnd()
        if self.intfstats != None:
            oprot.writeFieldBegin('intfstats', TType.LIST, 6)
            oprot.writeListBegin(TType.STRUCT, len(self.intfstats))
            for iter13 in self.intfstats:
                iter13.write(oprot)

            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

        def validate(self):
            pass





    def __repr__(self):
        L = [ '%s=%r' % (key, value) for (key, value,) in self.__dict__.iteritems() ]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))



    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__



    def __ne__(self, other):
        return not self == other




class OnepEvent_srvcDiscoveryEventIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - eventHandle
     - discoveryType
     - ssId
     - ssState
     - veridl
     - neAddr
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionHandle',
      None,
      None),
     (2,
      TType.I32,
      'eventHandle',
      None,
      None),
     (3,
      TType.I32,
      'discoveryType',
      None,
      None),
     (4,
      TType.I32,
      'ssId',
      None,
      None),
     (5,
      TType.I32,
      'ssState',
      None,
      None),
     (6,
      TType.STRUCT,
      'veridl',
      (SharedOut.ttypes.OnepVersionOutIDL, SharedOut.ttypes.OnepVersionOutIDL.thrift_spec),
      None),
     (7,
      TType.STRUCT,
      'neAddr',
      (SharedOut.ttypes.NetworkAddressOutIDL, SharedOut.ttypes.NetworkAddressOutIDL.thrift_spec),
      None))

    def __init__(self, sessionHandle = None, eventHandle = None, discoveryType = None, ssId = None, ssState = None, veridl = None, neAddr = None):
        self.sessionHandle = sessionHandle
        self.eventHandle = eventHandle
        self.discoveryType = discoveryType
        self.ssId = ssId
        self.ssState = ssState
        self.veridl = veridl
        self.neAddr = neAddr



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.sessionHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.eventHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.discoveryType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.ssId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.ssState = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRUCT:
                    self.veridl = SharedOut.ttypes.OnepVersionOutIDL()
                    self.veridl.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.STRUCT:
                    self.neAddr = SharedOut.ttypes.NetworkAddressOutIDL()
                    self.neAddr.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()

        iprot.readStructEnd()



    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return 
        oprot.writeStructBegin('OnepEvent_srvcDiscoveryEventIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.eventHandle != None:
            oprot.writeFieldBegin('eventHandle', TType.I32, 2)
            oprot.writeI32(self.eventHandle)
            oprot.writeFieldEnd()
        if self.discoveryType != None:
            oprot.writeFieldBegin('discoveryType', TType.I32, 3)
            oprot.writeI32(self.discoveryType)
            oprot.writeFieldEnd()
        if self.ssId != None:
            oprot.writeFieldBegin('ssId', TType.I32, 4)
            oprot.writeI32(self.ssId)
            oprot.writeFieldEnd()
        if self.ssState != None:
            oprot.writeFieldBegin('ssState', TType.I32, 5)
            oprot.writeI32(self.ssState)
            oprot.writeFieldEnd()
        if self.veridl != None:
            oprot.writeFieldBegin('veridl', TType.STRUCT, 6)
            self.veridl.write(oprot)
            oprot.writeFieldEnd()
        if self.neAddr != None:
            oprot.writeFieldBegin('neAddr', TType.STRUCT, 7)
            self.neAddr.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

        def validate(self):
            pass





    def __repr__(self):
        L = [ '%s=%r' % (key, value) for (key, value,) in self.__dict__.iteritems() ]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))



    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__



    def __ne__(self, other):
        return not self == other




class OnepEvent_vtyEventIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - execHandle
     - state
     - msgType
     - data
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionHandle',
      None,
      None),
     (2,
      TType.I32,
      'execHandle',
      None,
      None),
     (3,
      TType.I32,
      'state',
      None,
      None),
     (4,
      TType.I32,
      'msgType',
      None,
      None),
     (5,
      TType.STRING,
      'data',
      None,
      None))

    def __init__(self, sessionHandle = None, execHandle = None, state = None, msgType = None, data = None):
        self.sessionHandle = sessionHandle
        self.execHandle = execHandle
        self.state = state
        self.msgType = msgType
        self.data = data



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.sessionHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.execHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.state = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.msgType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.data = iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()

        iprot.readStructEnd()



    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return 
        oprot.writeStructBegin('OnepEvent_vtyEventIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.execHandle != None:
            oprot.writeFieldBegin('execHandle', TType.I32, 2)
            oprot.writeI32(self.execHandle)
            oprot.writeFieldEnd()
        if self.state != None:
            oprot.writeFieldBegin('state', TType.I32, 3)
            oprot.writeI32(self.state)
            oprot.writeFieldEnd()
        if self.msgType != None:
            oprot.writeFieldBegin('msgType', TType.I32, 4)
            oprot.writeI32(self.msgType)
            oprot.writeFieldEnd()
        if self.data != None:
            oprot.writeFieldBegin('data', TType.STRING, 5)
            oprot.writeString(self.data)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

        def validate(self):
            pass





    def __repr__(self):
        L = [ '%s=%r' % (key, value) for (key, value,) in self.__dict__.iteritems() ]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))



    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__



    def __ne__(self, other):
        return not self == other




class OnepEvent_capIntIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - capabilty_name
     - capabilty_value
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionHandle',
      None,
      None),
     (2,
      TType.STRING,
      'capabilty_name',
      None,
      None),
     (3,
      TType.LIST,
      'capabilty_value',
      (TType.STRUCT, (SharedOut.ttypes.I32OutIDL, SharedOut.ttypes.I32OutIDL.thrift_spec)),
      None))

    def __init__(self, sessionHandle = None, capabilty_name = None, capabilty_value = None):
        self.sessionHandle = sessionHandle
        self.capabilty_name = capabilty_name
        self.capabilty_value = capabilty_value



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.sessionHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.capabilty_name = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.LIST:
                    self.capabilty_value = []
                    (_etype17, _size14,) = iprot.readListBegin()
                    for _i18 in xrange(_size14):
                        _elem19 = SharedOut.ttypes.I32OutIDL()
                        _elem19.read(iprot)
                        self.capabilty_value.append(_elem19)

                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()

        iprot.readStructEnd()



    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return 
        oprot.writeStructBegin('OnepEvent_capIntIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.capabilty_name != None:
            oprot.writeFieldBegin('capabilty_name', TType.STRING, 2)
            oprot.writeString(self.capabilty_name)
            oprot.writeFieldEnd()
        if self.capabilty_value != None:
            oprot.writeFieldBegin('capabilty_value', TType.LIST, 3)
            oprot.writeListBegin(TType.STRUCT, len(self.capabilty_value))
            for iter20 in self.capabilty_value:
                iter20.write(oprot)

            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

        def validate(self):
            pass





    def __repr__(self):
        L = [ '%s=%r' % (key, value) for (key, value,) in self.__dict__.iteritems() ]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))



    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__



    def __ne__(self, other):
        return not self == other




class OnepEvent_capStrIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - capabilty_name
     - capabilty_value
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionHandle',
      None,
      None),
     (2,
      TType.STRING,
      'capabilty_name',
      None,
      None),
     (3,
      TType.LIST,
      'capabilty_value',
      (TType.STRUCT, (SharedOut.ttypes.StringOutIDL, SharedOut.ttypes.StringOutIDL.thrift_spec)),
      None))

    def __init__(self, sessionHandle = None, capabilty_name = None, capabilty_value = None):
        self.sessionHandle = sessionHandle
        self.capabilty_name = capabilty_name
        self.capabilty_value = capabilty_value



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.sessionHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.capabilty_name = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.LIST:
                    self.capabilty_value = []
                    (_etype24, _size21,) = iprot.readListBegin()
                    for _i25 in xrange(_size21):
                        _elem26 = SharedOut.ttypes.StringOutIDL()
                        _elem26.read(iprot)
                        self.capabilty_value.append(_elem26)

                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()

        iprot.readStructEnd()



    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return 
        oprot.writeStructBegin('OnepEvent_capStrIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.capabilty_name != None:
            oprot.writeFieldBegin('capabilty_name', TType.STRING, 2)
            oprot.writeString(self.capabilty_name)
            oprot.writeFieldEnd()
        if self.capabilty_value != None:
            oprot.writeFieldBegin('capabilty_value', TType.LIST, 3)
            oprot.writeListBegin(TType.STRUCT, len(self.capabilty_value))
            for iter27 in self.capabilty_value:
                iter27.write(oprot)

            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

        def validate(self):
            pass





    def __repr__(self):
        L = [ '%s=%r' % (key, value) for (key, value,) in self.__dict__.iteritems() ]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))



    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__



    def __ne__(self, other):
        return not self == other




class OnepEvent_ContainerSrvChangeEventIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - eventtype
     - adding
     - mask
     - MacID
     - Addr
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionHandle',
      None,
      None),
     (2,
      TType.I32,
      'eventtype',
      None,
      None),
     (3,
      TType.I32,
      'adding',
      None,
      None),
     (4,
      TType.I32,
      'mask',
      None,
      None),
     (5,
      TType.STRUCT,
      'MacID',
      (MacAddressOutIDL, MacAddressOutIDL.thrift_spec),
      None),
     (6,
      TType.STRUCT,
      'Addr',
      (SharedOut.ttypes.NetworkAddressOutIDL, SharedOut.ttypes.NetworkAddressOutIDL.thrift_spec),
      None))

    def __init__(self, sessionHandle = None, eventtype = None, adding = None, mask = None, MacID = None, Addr = None):
        self.sessionHandle = sessionHandle
        self.eventtype = eventtype
        self.adding = adding
        self.mask = mask
        self.MacID = MacID
        self.Addr = Addr



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.sessionHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.eventtype = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.adding = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.mask = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRUCT:
                    self.MacID = MacAddressOutIDL()
                    self.MacID.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRUCT:
                    self.Addr = SharedOut.ttypes.NetworkAddressOutIDL()
                    self.Addr.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()

        iprot.readStructEnd()



    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return 
        oprot.writeStructBegin('OnepEvent_ContainerSrvChangeEventIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.eventtype != None:
            oprot.writeFieldBegin('eventtype', TType.I32, 2)
            oprot.writeI32(self.eventtype)
            oprot.writeFieldEnd()
        if self.adding != None:
            oprot.writeFieldBegin('adding', TType.I32, 3)
            oprot.writeI32(self.adding)
            oprot.writeFieldEnd()
        if self.mask != None:
            oprot.writeFieldBegin('mask', TType.I32, 4)
            oprot.writeI32(self.mask)
            oprot.writeFieldEnd()
        if self.MacID != None:
            oprot.writeFieldBegin('MacID', TType.STRUCT, 5)
            self.MacID.write(oprot)
            oprot.writeFieldEnd()
        if self.Addr != None:
            oprot.writeFieldBegin('Addr', TType.STRUCT, 6)
            self.Addr.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

        def validate(self):
            pass





    def __repr__(self):
        L = [ '%s=%r' % (key, value) for (key, value,) in self.__dict__.iteritems() ]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))



    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__



    def __ne__(self, other):
        return not self == other




class OnepEvent_ContainerSrvInfoRequestIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - eventtype
     - transactionID
     - MacID
     - extrainfo
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionHandle',
      None,
      None),
     (2,
      TType.I32,
      'eventtype',
      None,
      None),
     (3,
      TType.I32,
      'transactionID',
      None,
      None),
     (4,
      TType.STRUCT,
      'MacID',
      (MacAddressOutIDL, MacAddressOutIDL.thrift_spec),
      None),
     (5,
      TType.I32,
      'extrainfo',
      None,
      None))

    def __init__(self, sessionHandle = None, eventtype = None, transactionID = None, MacID = None, extrainfo = None):
        self.sessionHandle = sessionHandle
        self.eventtype = eventtype
        self.transactionID = transactionID
        self.MacID = MacID
        self.extrainfo = extrainfo



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.sessionHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.eventtype = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.transactionID = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRUCT:
                    self.MacID = MacAddressOutIDL()
                    self.MacID.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.extrainfo = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()

        iprot.readStructEnd()



    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return 
        oprot.writeStructBegin('OnepEvent_ContainerSrvInfoRequestIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.eventtype != None:
            oprot.writeFieldBegin('eventtype', TType.I32, 2)
            oprot.writeI32(self.eventtype)
            oprot.writeFieldEnd()
        if self.transactionID != None:
            oprot.writeFieldBegin('transactionID', TType.I32, 3)
            oprot.writeI32(self.transactionID)
            oprot.writeFieldEnd()
        if self.MacID != None:
            oprot.writeFieldBegin('MacID', TType.STRUCT, 4)
            self.MacID.write(oprot)
            oprot.writeFieldEnd()
        if self.extrainfo != None:
            oprot.writeFieldBegin('extrainfo', TType.I32, 5)
            oprot.writeI32(self.extrainfo)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

        def validate(self):
            pass





    def __repr__(self):
        L = [ '%s=%r' % (key, value) for (key, value,) in self.__dict__.iteritems() ]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))



    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__



    def __ne__(self, other):
        return not self == other




class OnepEvent_InterfaceMtuEventIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - eventHandle
     - xosHandle
     - intfType
     - shortName
     - mtu
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionHandle',
      None,
      None),
     (2,
      TType.I32,
      'eventHandle',
      None,
      None),
     (3,
      TType.I64,
      'xosHandle',
      None,
      None),
     (4,
      TType.I32,
      'intfType',
      None,
      None),
     (5,
      TType.STRING,
      'shortName',
      None,
      None),
     (6,
      TType.I32,
      'mtu',
      None,
      None))

    def __init__(self, sessionHandle = None, eventHandle = None, xosHandle = None, intfType = None, shortName = None, mtu = None):
        self.sessionHandle = sessionHandle
        self.eventHandle = eventHandle
        self.xosHandle = xosHandle
        self.intfType = intfType
        self.shortName = shortName
        self.mtu = mtu



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.sessionHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.eventHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I64:
                    self.xosHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.intfType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.shortName = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I32:
                    self.mtu = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()

        iprot.readStructEnd()



    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return 
        oprot.writeStructBegin('OnepEvent_InterfaceMtuEventIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.eventHandle != None:
            oprot.writeFieldBegin('eventHandle', TType.I32, 2)
            oprot.writeI32(self.eventHandle)
            oprot.writeFieldEnd()
        if self.xosHandle != None:
            oprot.writeFieldBegin('xosHandle', TType.I64, 3)
            oprot.writeI64(self.xosHandle)
            oprot.writeFieldEnd()
        if self.intfType != None:
            oprot.writeFieldBegin('intfType', TType.I32, 4)
            oprot.writeI32(self.intfType)
            oprot.writeFieldEnd()
        if self.shortName != None:
            oprot.writeFieldBegin('shortName', TType.STRING, 5)
            oprot.writeString(self.shortName)
            oprot.writeFieldEnd()
        if self.mtu != None:
            oprot.writeFieldBegin('mtu', TType.I32, 6)
            oprot.writeI32(self.mtu)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

        def validate(self):
            pass





    def __repr__(self):
        L = [ '%s=%r' % (key, value) for (key, value,) in self.__dict__.iteritems() ]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))



    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__



    def __ne__(self, other):
        return not self == other




class OnepEvent_InterfaceSpeedEventIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - eventHandle
     - xosHandle
     - intfType
     - shortName
     - speed
     - configType
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionHandle',
      None,
      None),
     (2,
      TType.I32,
      'eventHandle',
      None,
      None),
     (3,
      TType.I64,
      'xosHandle',
      None,
      None),
     (4,
      TType.I32,
      'intfType',
      None,
      None),
     (5,
      TType.STRING,
      'shortName',
      None,
      None),
     (6,
      TType.I32,
      'speed',
      None,
      None),
     (7,
      TType.I32,
      'configType',
      None,
      None))

    def __init__(self, sessionHandle = None, eventHandle = None, xosHandle = None, intfType = None, shortName = None, speed = None, configType = None):
        self.sessionHandle = sessionHandle
        self.eventHandle = eventHandle
        self.xosHandle = xosHandle
        self.intfType = intfType
        self.shortName = shortName
        self.speed = speed
        self.configType = configType



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.sessionHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.eventHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I64:
                    self.xosHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.intfType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.shortName = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I32:
                    self.speed = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I32:
                    self.configType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()

        iprot.readStructEnd()



    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return 
        oprot.writeStructBegin('OnepEvent_InterfaceSpeedEventIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.eventHandle != None:
            oprot.writeFieldBegin('eventHandle', TType.I32, 2)
            oprot.writeI32(self.eventHandle)
            oprot.writeFieldEnd()
        if self.xosHandle != None:
            oprot.writeFieldBegin('xosHandle', TType.I64, 3)
            oprot.writeI64(self.xosHandle)
            oprot.writeFieldEnd()
        if self.intfType != None:
            oprot.writeFieldBegin('intfType', TType.I32, 4)
            oprot.writeI32(self.intfType)
            oprot.writeFieldEnd()
        if self.shortName != None:
            oprot.writeFieldBegin('shortName', TType.STRING, 5)
            oprot.writeString(self.shortName)
            oprot.writeFieldEnd()
        if self.speed != None:
            oprot.writeFieldBegin('speed', TType.I32, 6)
            oprot.writeI32(self.speed)
            oprot.writeFieldEnd()
        if self.configType != None:
            oprot.writeFieldBegin('configType', TType.I32, 7)
            oprot.writeI32(self.configType)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

        def validate(self):
            pass





    def __repr__(self):
        L = [ '%s=%r' % (key, value) for (key, value,) in self.__dict__.iteritems() ]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))



    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__



    def __ne__(self, other):
        return not self == other




class OnepEvent_InterfaceDuplexModeEventIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - eventHandle
     - xosHandle
     - intfType
     - shortName
     - duplexMode
     - configType
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionHandle',
      None,
      None),
     (2,
      TType.I32,
      'eventHandle',
      None,
      None),
     (3,
      TType.I64,
      'xosHandle',
      None,
      None),
     (4,
      TType.I32,
      'intfType',
      None,
      None),
     (5,
      TType.STRING,
      'shortName',
      None,
      None),
     (6,
      TType.I32,
      'duplexMode',
      None,
      None),
     (7,
      TType.I32,
      'configType',
      None,
      None))

    def __init__(self, sessionHandle = None, eventHandle = None, xosHandle = None, intfType = None, shortName = None, duplexMode = None, configType = None):
        self.sessionHandle = sessionHandle
        self.eventHandle = eventHandle
        self.xosHandle = xosHandle
        self.intfType = intfType
        self.shortName = shortName
        self.duplexMode = duplexMode
        self.configType = configType



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.sessionHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.eventHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I64:
                    self.xosHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.intfType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.shortName = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I32:
                    self.duplexMode = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I32:
                    self.configType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()

        iprot.readStructEnd()



    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return 
        oprot.writeStructBegin('OnepEvent_InterfaceDuplexModeEventIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.eventHandle != None:
            oprot.writeFieldBegin('eventHandle', TType.I32, 2)
            oprot.writeI32(self.eventHandle)
            oprot.writeFieldEnd()
        if self.xosHandle != None:
            oprot.writeFieldBegin('xosHandle', TType.I64, 3)
            oprot.writeI64(self.xosHandle)
            oprot.writeFieldEnd()
        if self.intfType != None:
            oprot.writeFieldBegin('intfType', TType.I32, 4)
            oprot.writeI32(self.intfType)
            oprot.writeFieldEnd()
        if self.shortName != None:
            oprot.writeFieldBegin('shortName', TType.STRING, 5)
            oprot.writeString(self.shortName)
            oprot.writeFieldEnd()
        if self.duplexMode != None:
            oprot.writeFieldBegin('duplexMode', TType.I32, 6)
            oprot.writeI32(self.duplexMode)
            oprot.writeFieldEnd()
        if self.configType != None:
            oprot.writeFieldBegin('configType', TType.I32, 7)
            oprot.writeI32(self.configType)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

        def validate(self):
            pass





    def __repr__(self):
        L = [ '%s=%r' % (key, value) for (key, value,) in self.__dict__.iteritems() ]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))



    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__



    def __ne__(self, other):
        return not self == other




class OnepEvent_InterfaceAutoNegotiateEventIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - eventHandle
     - xosHandle
     - intfType
     - shortName
     - autoNeg
     - configType
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionHandle',
      None,
      None),
     (2,
      TType.I32,
      'eventHandle',
      None,
      None),
     (3,
      TType.I64,
      'xosHandle',
      None,
      None),
     (4,
      TType.I32,
      'intfType',
      None,
      None),
     (5,
      TType.STRING,
      'shortName',
      None,
      None),
     (6,
      TType.I32,
      'autoNeg',
      None,
      None),
     (7,
      TType.I32,
      'configType',
      None,
      None))

    def __init__(self, sessionHandle = None, eventHandle = None, xosHandle = None, intfType = None, shortName = None, autoNeg = None, configType = None):
        self.sessionHandle = sessionHandle
        self.eventHandle = eventHandle
        self.xosHandle = xosHandle
        self.intfType = intfType
        self.shortName = shortName
        self.autoNeg = autoNeg
        self.configType = configType



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.sessionHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.eventHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I64:
                    self.xosHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.intfType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.shortName = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I32:
                    self.autoNeg = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I32:
                    self.configType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()

        iprot.readStructEnd()



    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return 
        oprot.writeStructBegin('OnepEvent_InterfaceAutoNegotiateEventIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.eventHandle != None:
            oprot.writeFieldBegin('eventHandle', TType.I32, 2)
            oprot.writeI32(self.eventHandle)
            oprot.writeFieldEnd()
        if self.xosHandle != None:
            oprot.writeFieldBegin('xosHandle', TType.I64, 3)
            oprot.writeI64(self.xosHandle)
            oprot.writeFieldEnd()
        if self.intfType != None:
            oprot.writeFieldBegin('intfType', TType.I32, 4)
            oprot.writeI32(self.intfType)
            oprot.writeFieldEnd()
        if self.shortName != None:
            oprot.writeFieldBegin('shortName', TType.STRING, 5)
            oprot.writeString(self.shortName)
            oprot.writeFieldEnd()
        if self.autoNeg != None:
            oprot.writeFieldBegin('autoNeg', TType.I32, 6)
            oprot.writeI32(self.autoNeg)
            oprot.writeFieldEnd()
        if self.configType != None:
            oprot.writeFieldBegin('configType', TType.I32, 7)
            oprot.writeI32(self.configType)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

        def validate(self):
            pass





    def __repr__(self):
        L = [ '%s=%r' % (key, value) for (key, value,) in self.__dict__.iteritems() ]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))



    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__



    def __ne__(self, other):
        return not self == other




class OnepEvent_InterfaceLayer2ModeEventIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - eventHandle
     - xosHandle
     - intfType
     - shortName
     - laye2Mode
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionHandle',
      None,
      None),
     (2,
      TType.I32,
      'eventHandle',
      None,
      None),
     (3,
      TType.I64,
      'xosHandle',
      None,
      None),
     (4,
      TType.I32,
      'intfType',
      None,
      None),
     (5,
      TType.STRING,
      'shortName',
      None,
      None),
     (6,
      TType.I32,
      'laye2Mode',
      None,
      None))

    def __init__(self, sessionHandle = None, eventHandle = None, xosHandle = None, intfType = None, shortName = None, laye2Mode = None):
        self.sessionHandle = sessionHandle
        self.eventHandle = eventHandle
        self.xosHandle = xosHandle
        self.intfType = intfType
        self.shortName = shortName
        self.laye2Mode = laye2Mode



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.sessionHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.eventHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I64:
                    self.xosHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.intfType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.shortName = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I32:
                    self.laye2Mode = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()

        iprot.readStructEnd()



    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return 
        oprot.writeStructBegin('OnepEvent_InterfaceLayer2ModeEventIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.eventHandle != None:
            oprot.writeFieldBegin('eventHandle', TType.I32, 2)
            oprot.writeI32(self.eventHandle)
            oprot.writeFieldEnd()
        if self.xosHandle != None:
            oprot.writeFieldBegin('xosHandle', TType.I64, 3)
            oprot.writeI64(self.xosHandle)
            oprot.writeFieldEnd()
        if self.intfType != None:
            oprot.writeFieldBegin('intfType', TType.I32, 4)
            oprot.writeI32(self.intfType)
            oprot.writeFieldEnd()
        if self.shortName != None:
            oprot.writeFieldBegin('shortName', TType.STRING, 5)
            oprot.writeString(self.shortName)
            oprot.writeFieldEnd()
        if self.laye2Mode != None:
            oprot.writeFieldBegin('laye2Mode', TType.I32, 6)
            oprot.writeI32(self.laye2Mode)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

        def validate(self):
            pass





    def __repr__(self):
        L = [ '%s=%r' % (key, value) for (key, value,) in self.__dict__.iteritems() ]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))



    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__



    def __ne__(self, other):
        return not self == other




class OnepEvent_InterfaceFlowcontrolEventIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - eventHandle
     - xosHandle
     - intfType
     - shortName
     - inFlow
     - outFlow
     - configType
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionHandle',
      None,
      None),
     (2,
      TType.I32,
      'eventHandle',
      None,
      None),
     (3,
      TType.I64,
      'xosHandle',
      None,
      None),
     (4,
      TType.I32,
      'intfType',
      None,
      None),
     (5,
      TType.STRING,
      'shortName',
      None,
      None),
     (6,
      TType.I32,
      'inFlow',
      None,
      None),
     (7,
      TType.I32,
      'outFlow',
      None,
      None),
     (8,
      TType.I32,
      'configType',
      None,
      None))

    def __init__(self, sessionHandle = None, eventHandle = None, xosHandle = None, intfType = None, shortName = None, inFlow = None, outFlow = None, configType = None):
        self.sessionHandle = sessionHandle
        self.eventHandle = eventHandle
        self.xosHandle = xosHandle
        self.intfType = intfType
        self.shortName = shortName
        self.inFlow = inFlow
        self.outFlow = outFlow
        self.configType = configType



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.sessionHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.eventHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I64:
                    self.xosHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.intfType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.shortName = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I32:
                    self.inFlow = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I32:
                    self.outFlow = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.I32:
                    self.configType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()

        iprot.readStructEnd()



    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return 
        oprot.writeStructBegin('OnepEvent_InterfaceFlowcontrolEventIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.eventHandle != None:
            oprot.writeFieldBegin('eventHandle', TType.I32, 2)
            oprot.writeI32(self.eventHandle)
            oprot.writeFieldEnd()
        if self.xosHandle != None:
            oprot.writeFieldBegin('xosHandle', TType.I64, 3)
            oprot.writeI64(self.xosHandle)
            oprot.writeFieldEnd()
        if self.intfType != None:
            oprot.writeFieldBegin('intfType', TType.I32, 4)
            oprot.writeI32(self.intfType)
            oprot.writeFieldEnd()
        if self.shortName != None:
            oprot.writeFieldBegin('shortName', TType.STRING, 5)
            oprot.writeString(self.shortName)
            oprot.writeFieldEnd()
        if self.inFlow != None:
            oprot.writeFieldBegin('inFlow', TType.I32, 6)
            oprot.writeI32(self.inFlow)
            oprot.writeFieldEnd()
        if self.outFlow != None:
            oprot.writeFieldBegin('outFlow', TType.I32, 7)
            oprot.writeI32(self.outFlow)
            oprot.writeFieldEnd()
        if self.configType != None:
            oprot.writeFieldBegin('configType', TType.I32, 8)
            oprot.writeI32(self.configType)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

        def validate(self):
            pass





    def __repr__(self):
        L = [ '%s=%r' % (key, value) for (key, value,) in self.__dict__.iteritems() ]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))



    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__



    def __ne__(self, other):
        return not self == other




class OnepEvent_InterfaceForwardClassIDEventIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - eventHandle
     - xosHandle
     - intfType
     - shortName
     - fwdClassID
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionHandle',
      None,
      None),
     (2,
      TType.I32,
      'eventHandle',
      None,
      None),
     (3,
      TType.I64,
      'xosHandle',
      None,
      None),
     (4,
      TType.I32,
      'intfType',
      None,
      None),
     (5,
      TType.STRING,
      'shortName',
      None,
      None),
     (6,
      TType.I32,
      'fwdClassID',
      None,
      None))

    def __init__(self, sessionHandle = None, eventHandle = None, xosHandle = None, intfType = None, shortName = None, fwdClassID = None):
        self.sessionHandle = sessionHandle
        self.eventHandle = eventHandle
        self.xosHandle = xosHandle
        self.intfType = intfType
        self.shortName = shortName
        self.fwdClassID = fwdClassID



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.sessionHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.eventHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I64:
                    self.xosHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.intfType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.shortName = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I32:
                    self.fwdClassID = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()

        iprot.readStructEnd()



    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return 
        oprot.writeStructBegin('OnepEvent_InterfaceForwardClassIDEventIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.eventHandle != None:
            oprot.writeFieldBegin('eventHandle', TType.I32, 2)
            oprot.writeI32(self.eventHandle)
            oprot.writeFieldEnd()
        if self.xosHandle != None:
            oprot.writeFieldBegin('xosHandle', TType.I64, 3)
            oprot.writeI64(self.xosHandle)
            oprot.writeFieldEnd()
        if self.intfType != None:
            oprot.writeFieldBegin('intfType', TType.I32, 4)
            oprot.writeI32(self.intfType)
            oprot.writeFieldEnd()
        if self.shortName != None:
            oprot.writeFieldBegin('shortName', TType.STRING, 5)
            oprot.writeString(self.shortName)
            oprot.writeFieldEnd()
        if self.fwdClassID != None:
            oprot.writeFieldBegin('fwdClassID', TType.I32, 6)
            oprot.writeI32(self.fwdClassID)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

        def validate(self):
            pass





    def __repr__(self):
        L = [ '%s=%r' % (key, value) for (key, value,) in self.__dict__.iteritems() ]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))



    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__



    def __ne__(self, other):
        return not self == other




class OnepEvent_InterfaceBandwidthEventIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - eventHandle
     - xosHandle
     - intfType
     - shortName
     - bandwidth
     - is_tx
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionHandle',
      None,
      None),
     (2,
      TType.I32,
      'eventHandle',
      None,
      None),
     (3,
      TType.I64,
      'xosHandle',
      None,
      None),
     (4,
      TType.I32,
      'intfType',
      None,
      None),
     (5,
      TType.STRING,
      'shortName',
      None,
      None),
     (6,
      TType.I32,
      'bandwidth',
      None,
      None),
     (7,
      TType.I32,
      'is_tx',
      None,
      None))

    def __init__(self, sessionHandle = None, eventHandle = None, xosHandle = None, intfType = None, shortName = None, bandwidth = None, is_tx = None):
        self.sessionHandle = sessionHandle
        self.eventHandle = eventHandle
        self.xosHandle = xosHandle
        self.intfType = intfType
        self.shortName = shortName
        self.bandwidth = bandwidth
        self.is_tx = is_tx



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.sessionHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.eventHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I64:
                    self.xosHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.intfType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.shortName = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I32:
                    self.bandwidth = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I32:
                    self.is_tx = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()

        iprot.readStructEnd()



    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return 
        oprot.writeStructBegin('OnepEvent_InterfaceBandwidthEventIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.eventHandle != None:
            oprot.writeFieldBegin('eventHandle', TType.I32, 2)
            oprot.writeI32(self.eventHandle)
            oprot.writeFieldEnd()
        if self.xosHandle != None:
            oprot.writeFieldBegin('xosHandle', TType.I64, 3)
            oprot.writeI64(self.xosHandle)
            oprot.writeFieldEnd()
        if self.intfType != None:
            oprot.writeFieldBegin('intfType', TType.I32, 4)
            oprot.writeI32(self.intfType)
            oprot.writeFieldEnd()
        if self.shortName != None:
            oprot.writeFieldBegin('shortName', TType.STRING, 5)
            oprot.writeString(self.shortName)
            oprot.writeFieldEnd()
        if self.bandwidth != None:
            oprot.writeFieldBegin('bandwidth', TType.I32, 6)
            oprot.writeI32(self.bandwidth)
            oprot.writeFieldEnd()
        if self.is_tx != None:
            oprot.writeFieldBegin('is_tx', TType.I32, 7)
            oprot.writeI32(self.is_tx)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

        def validate(self):
            pass





    def __repr__(self):
        L = [ '%s=%r' % (key, value) for (key, value,) in self.__dict__.iteritems() ]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))



    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__



    def __ne__(self, other):
        return not self == other




class OnepEvent_InterfaceVlanEventIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - eventHandle
     - xosHandle
     - intfType
     - shortName
     - vlan
     - vlanEventType
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionHandle',
      None,
      None),
     (2,
      TType.I32,
      'eventHandle',
      None,
      None),
     (3,
      TType.I64,
      'xosHandle',
      None,
      None),
     (4,
      TType.I32,
      'intfType',
      None,
      None),
     (5,
      TType.STRING,
      'shortName',
      None,
      None),
     (6,
      TType.STRUCT,
      'vlan',
      (InterfaceVlanOutIDL, InterfaceVlanOutIDL.thrift_spec),
      None),
     (7,
      TType.I32,
      'vlanEventType',
      None,
      None))

    def __init__(self, sessionHandle = None, eventHandle = None, xosHandle = None, intfType = None, shortName = None, vlan = None, vlanEventType = None):
        self.sessionHandle = sessionHandle
        self.eventHandle = eventHandle
        self.xosHandle = xosHandle
        self.intfType = intfType
        self.shortName = shortName
        self.vlan = vlan
        self.vlanEventType = vlanEventType



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.sessionHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.eventHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I64:
                    self.xosHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.intfType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.shortName = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRUCT:
                    self.vlan = InterfaceVlanOutIDL()
                    self.vlan.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I32:
                    self.vlanEventType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()

        iprot.readStructEnd()



    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return 
        oprot.writeStructBegin('OnepEvent_InterfaceVlanEventIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.eventHandle != None:
            oprot.writeFieldBegin('eventHandle', TType.I32, 2)
            oprot.writeI32(self.eventHandle)
            oprot.writeFieldEnd()
        if self.xosHandle != None:
            oprot.writeFieldBegin('xosHandle', TType.I64, 3)
            oprot.writeI64(self.xosHandle)
            oprot.writeFieldEnd()
        if self.intfType != None:
            oprot.writeFieldBegin('intfType', TType.I32, 4)
            oprot.writeI32(self.intfType)
            oprot.writeFieldEnd()
        if self.shortName != None:
            oprot.writeFieldBegin('shortName', TType.STRING, 5)
            oprot.writeString(self.shortName)
            oprot.writeFieldEnd()
        if self.vlan != None:
            oprot.writeFieldBegin('vlan', TType.STRUCT, 6)
            self.vlan.write(oprot)
            oprot.writeFieldEnd()
        if self.vlanEventType != None:
            oprot.writeFieldBegin('vlanEventType', TType.I32, 7)
            oprot.writeI32(self.vlanEventType)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

        def validate(self):
            pass





    def __repr__(self):
        L = [ '%s=%r' % (key, value) for (key, value,) in self.__dict__.iteritems() ]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))



    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__



    def __ne__(self, other):
        return not self == other




class OnepEvent_InterfaceVrfEventIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - eventHandle
     - xosHandle
     - intfType
     - shortName
     - vrf
     - vrfEventType
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionHandle',
      None,
      None),
     (2,
      TType.I32,
      'eventHandle',
      None,
      None),
     (3,
      TType.I64,
      'xosHandle',
      None,
      None),
     (4,
      TType.I32,
      'intfType',
      None,
      None),
     (5,
      TType.STRING,
      'shortName',
      None,
      None),
     (6,
      TType.STRING,
      'vrf',
      None,
      None),
     (7,
      TType.I32,
      'vrfEventType',
      None,
      None))

    def __init__(self, sessionHandle = None, eventHandle = None, xosHandle = None, intfType = None, shortName = None, vrf = None, vrfEventType = None):
        self.sessionHandle = sessionHandle
        self.eventHandle = eventHandle
        self.xosHandle = xosHandle
        self.intfType = intfType
        self.shortName = shortName
        self.vrf = vrf
        self.vrfEventType = vrfEventType



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.sessionHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.eventHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I64:
                    self.xosHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.intfType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.shortName = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRING:
                    self.vrf = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I32:
                    self.vrfEventType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()

        iprot.readStructEnd()



    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return 
        oprot.writeStructBegin('OnepEvent_InterfaceVrfEventIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.eventHandle != None:
            oprot.writeFieldBegin('eventHandle', TType.I32, 2)
            oprot.writeI32(self.eventHandle)
            oprot.writeFieldEnd()
        if self.xosHandle != None:
            oprot.writeFieldBegin('xosHandle', TType.I64, 3)
            oprot.writeI64(self.xosHandle)
            oprot.writeFieldEnd()
        if self.intfType != None:
            oprot.writeFieldBegin('intfType', TType.I32, 4)
            oprot.writeI32(self.intfType)
            oprot.writeFieldEnd()
        if self.shortName != None:
            oprot.writeFieldBegin('shortName', TType.STRING, 5)
            oprot.writeString(self.shortName)
            oprot.writeFieldEnd()
        if self.vrf != None:
            oprot.writeFieldBegin('vrf', TType.STRING, 6)
            oprot.writeString(self.vrf)
            oprot.writeFieldEnd()
        if self.vrfEventType != None:
            oprot.writeFieldBegin('vrfEventType', TType.I32, 7)
            oprot.writeI32(self.vrfEventType)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

        def validate(self):
            pass





    def __repr__(self):
        L = [ '%s=%r' % (key, value) for (key, value,) in self.__dict__.iteritems() ]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))



    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__



    def __ne__(self, other):
        return not self == other




class OnepEvent_HsrpStateEventIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - eventHandle
     - xosHandle
     - intfType
     - shortName
     - groupid
     - family
     - state
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionHandle',
      None,
      None),
     (2,
      TType.I32,
      'eventHandle',
      None,
      None),
     (3,
      TType.I64,
      'xosHandle',
      None,
      None),
     (4,
      TType.I32,
      'intfType',
      None,
      None),
     (5,
      TType.STRING,
      'shortName',
      None,
      None),
     (6,
      TType.I32,
      'groupid',
      None,
      None),
     (7,
      TType.I32,
      'family',
      None,
      None),
     (8,
      TType.I32,
      'state',
      None,
      None))

    def __init__(self, sessionHandle = None, eventHandle = None, xosHandle = None, intfType = None, shortName = None, groupid = None, family = None, state = None):
        self.sessionHandle = sessionHandle
        self.eventHandle = eventHandle
        self.xosHandle = xosHandle
        self.intfType = intfType
        self.shortName = shortName
        self.groupid = groupid
        self.family = family
        self.state = state



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.sessionHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.eventHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I64:
                    self.xosHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.intfType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.shortName = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I32:
                    self.groupid = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I32:
                    self.family = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.I32:
                    self.state = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()

        iprot.readStructEnd()



    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return 
        oprot.writeStructBegin('OnepEvent_HsrpStateEventIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.eventHandle != None:
            oprot.writeFieldBegin('eventHandle', TType.I32, 2)
            oprot.writeI32(self.eventHandle)
            oprot.writeFieldEnd()
        if self.xosHandle != None:
            oprot.writeFieldBegin('xosHandle', TType.I64, 3)
            oprot.writeI64(self.xosHandle)
            oprot.writeFieldEnd()
        if self.intfType != None:
            oprot.writeFieldBegin('intfType', TType.I32, 4)
            oprot.writeI32(self.intfType)
            oprot.writeFieldEnd()
        if self.shortName != None:
            oprot.writeFieldBegin('shortName', TType.STRING, 5)
            oprot.writeString(self.shortName)
            oprot.writeFieldEnd()
        if self.groupid != None:
            oprot.writeFieldBegin('groupid', TType.I32, 6)
            oprot.writeI32(self.groupid)
            oprot.writeFieldEnd()
        if self.family != None:
            oprot.writeFieldBegin('family', TType.I32, 7)
            oprot.writeI32(self.family)
            oprot.writeFieldEnd()
        if self.state != None:
            oprot.writeFieldBegin('state', TType.I32, 8)
            oprot.writeI32(self.state)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

        def validate(self):
            pass





    def __repr__(self):
        L = [ '%s=%r' % (key, value) for (key, value,) in self.__dict__.iteritems() ]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))



    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__



    def __ne__(self, other):
        return not self == other




class OnepEvent_BDEventIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - eventHandle
     - type
     - id
     - name
     - xosHandle
     - intfType
     - shortName
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionHandle',
      None,
      None),
     (2,
      TType.I32,
      'eventHandle',
      None,
      None),
     (3,
      TType.I32,
      'type',
      None,
      None),
     (4,
      TType.I32,
      'id',
      None,
      None),
     (5,
      TType.STRING,
      'name',
      None,
      None),
     (6,
      TType.I64,
      'xosHandle',
      None,
      None),
     (7,
      TType.I32,
      'intfType',
      None,
      None),
     (8,
      TType.STRING,
      'shortName',
      None,
      None))

    def __init__(self, sessionHandle = None, eventHandle = None, type = None, id = None, name = None, xosHandle = None, intfType = None, shortName = None):
        self.sessionHandle = sessionHandle
        self.eventHandle = eventHandle
        self.type = type
        self.id = id
        self.name = name
        self.xosHandle = xosHandle
        self.intfType = intfType
        self.shortName = shortName



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.sessionHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.eventHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.id = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.name = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I64:
                    self.xosHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I32:
                    self.intfType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.STRING:
                    self.shortName = iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()

        iprot.readStructEnd()



    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return 
        oprot.writeStructBegin('OnepEvent_BDEventIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.eventHandle != None:
            oprot.writeFieldBegin('eventHandle', TType.I32, 2)
            oprot.writeI32(self.eventHandle)
            oprot.writeFieldEnd()
        if self.type != None:
            oprot.writeFieldBegin('type', TType.I32, 3)
            oprot.writeI32(self.type)
            oprot.writeFieldEnd()
        if self.id != None:
            oprot.writeFieldBegin('id', TType.I32, 4)
            oprot.writeI32(self.id)
            oprot.writeFieldEnd()
        if self.name != None:
            oprot.writeFieldBegin('name', TType.STRING, 5)
            oprot.writeString(self.name)
            oprot.writeFieldEnd()
        if self.xosHandle != None:
            oprot.writeFieldBegin('xosHandle', TType.I64, 6)
            oprot.writeI64(self.xosHandle)
            oprot.writeFieldEnd()
        if self.intfType != None:
            oprot.writeFieldBegin('intfType', TType.I32, 7)
            oprot.writeI32(self.intfType)
            oprot.writeFieldEnd()
        if self.shortName != None:
            oprot.writeFieldBegin('shortName', TType.STRING, 8)
            oprot.writeString(self.shortName)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

        def validate(self):
            pass





    def __repr__(self):
        L = [ '%s=%r' % (key, value) for (key, value,) in self.__dict__.iteritems() ]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))



    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__



    def __ne__(self, other):
        return not self == other




class OnepEvent_BDServiceStatusEventIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - eventHandle
     - status
     - resync
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionHandle',
      None,
      None),
     (2,
      TType.I32,
      'eventHandle',
      None,
      None),
     None,
     None,
     None,
     (6,
      TType.I32,
      'status',
      None,
      None),
     (7,
      TType.I32,
      'resync',
      None,
      None))

    def __init__(self, sessionHandle = None, eventHandle = None, status = None, resync = None):
        self.sessionHandle = sessionHandle
        self.eventHandle = eventHandle
        self.status = status
        self.resync = resync



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.sessionHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.eventHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I32:
                    self.status = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I32:
                    self.resync = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()

        iprot.readStructEnd()



    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return 
        oprot.writeStructBegin('OnepEvent_BDServiceStatusEventIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.eventHandle != None:
            oprot.writeFieldBegin('eventHandle', TType.I32, 2)
            oprot.writeI32(self.eventHandle)
            oprot.writeFieldEnd()
        if self.status != None:
            oprot.writeFieldBegin('status', TType.I32, 6)
            oprot.writeI32(self.status)
            oprot.writeFieldEnd()
        if self.resync != None:
            oprot.writeFieldBegin('resync', TType.I32, 7)
            oprot.writeI32(self.resync)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

        def validate(self):
            pass





    def __repr__(self):
        L = [ '%s=%r' % (key, value) for (key, value,) in self.__dict__.iteritems() ]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))



    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__



    def __ne__(self, other):
        return not self == other




class OnepEvent_PortChannelEventIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - eventHandle
     - pcHandle
     - pcName
     - ifHandle
     - ifName
     - intfType
     - add
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionHandle',
      None,
      None),
     (2,
      TType.I32,
      'eventHandle',
      None,
      None),
     (3,
      TType.I64,
      'pcHandle',
      None,
      None),
     (4,
      TType.STRING,
      'pcName',
      None,
      None),
     (5,
      TType.I64,
      'ifHandle',
      None,
      None),
     (6,
      TType.STRING,
      'ifName',
      None,
      None),
     (7,
      TType.I32,
      'intfType',
      None,
      None),
     (8,
      TType.I32,
      'add',
      None,
      None))

    def __init__(self, sessionHandle = None, eventHandle = None, pcHandle = None, pcName = None, ifHandle = None, ifName = None, intfType = None, add = None):
        self.sessionHandle = sessionHandle
        self.eventHandle = eventHandle
        self.pcHandle = pcHandle
        self.pcName = pcName
        self.ifHandle = ifHandle
        self.ifName = ifName
        self.intfType = intfType
        self.add = add



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.sessionHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.eventHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I64:
                    self.pcHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.pcName = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I64:
                    self.ifHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRING:
                    self.ifName = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I32:
                    self.intfType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.I32:
                    self.add = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()

        iprot.readStructEnd()



    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return 
        oprot.writeStructBegin('OnepEvent_PortChannelEventIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.eventHandle != None:
            oprot.writeFieldBegin('eventHandle', TType.I32, 2)
            oprot.writeI32(self.eventHandle)
            oprot.writeFieldEnd()
        if self.pcHandle != None:
            oprot.writeFieldBegin('pcHandle', TType.I64, 3)
            oprot.writeI64(self.pcHandle)
            oprot.writeFieldEnd()
        if self.pcName != None:
            oprot.writeFieldBegin('pcName', TType.STRING, 4)
            oprot.writeString(self.pcName)
            oprot.writeFieldEnd()
        if self.ifHandle != None:
            oprot.writeFieldBegin('ifHandle', TType.I64, 5)
            oprot.writeI64(self.ifHandle)
            oprot.writeFieldEnd()
        if self.ifName != None:
            oprot.writeFieldBegin('ifName', TType.STRING, 6)
            oprot.writeString(self.ifName)
            oprot.writeFieldEnd()
        if self.intfType != None:
            oprot.writeFieldBegin('intfType', TType.I32, 7)
            oprot.writeI32(self.intfType)
            oprot.writeFieldEnd()
        if self.add != None:
            oprot.writeFieldBegin('add', TType.I32, 8)
            oprot.writeI32(self.add)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

        def validate(self):
            pass





    def __repr__(self):
        L = [ '%s=%r' % (key, value) for (key, value,) in self.__dict__.iteritems() ]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))



    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__



    def __ne__(self, other):
        return not self == other




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:21:56 IST
