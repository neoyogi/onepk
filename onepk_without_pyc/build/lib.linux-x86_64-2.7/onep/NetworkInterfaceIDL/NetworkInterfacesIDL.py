# 2015.02.05 17:19:02 IST
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

    def NetworkElement_getInterfaceListIDL(self, sessionHandle, xoshandle, ifType, tag, slot):
        """
            Get all the interfaces (physical and logical) on the
            NetworkElement
        
            Parameters:
             - sessionHandle
             - xoshandle
             - ifType
             - tag
             - slot
            """
        pass



    def NetworkElement_getInterfaceByNameIDL(self, ifname):
        """
            Get the interface instance given the name
        
            Parameters:
             - ifname
            """
        pass



    def NetworkElement_getInterfaceByIifIdIDL(self, iif_id):
        """
            Get the interface instance given the iif_id (private for DPSS)
            (IOS-XE if ID outside IOSd)
        
            Parameters:
             - iif_id
            """
        pass



    def NetworkElement_getInterfaceByIdIDL(self, if_id):
        """
            Get the interface instance given the if_id / xosHandle (private for DPSS)
        
            Parameters:
             - if_id
            """
        pass



    def NetworkInterface_getPropertyIDL(self, xosHandle):
        """
            Get the InterfaceProperty on a particular interface
            This is done only once for an interface instance
        
            Parameters:
             - xosHandle
            """
        pass



    def NetworkInterface_issubInterfaceIDL(self, xosHandle):
        """
            Gets if the Interface is sub-interface or not
        
            Parameters:
             - xosHandle
            """
        pass



    def NetworkInterface_getConfigIDL(self, xosHandle):
        """
            Get the refreshed InterfaceConfig on a particular interface
        
            Parameters:
             - xosHandle
            """
        pass



    def NetworkInterface_getStatusIDL(self, xosHandle):
        """
            Get the snapshot Status on a particular interface
        
            Parameters:
             - xosHandle
            """
        pass



    def NetworkInterface_getStatisticsIDL(self, xosHandle):
        """
            Get the snapshot statistics on a particular interface
        
            Parameters:
             - xosHandle
            """
        pass



    def NetworkInterface_getParentIDL(self, xosHandle):
        """
            Get parent(base) interface, if any
        
            Parameters:
             - xosHandle
            """
        pass



    def NetworkInterface_getSubInterfaceIDL(self, xosHandle):
        """
            Get parent(base) interface, if any
        
            Parameters:
             - xosHandle
            """
        pass



    def NetworkInterface_getAddressListIDL(self, xoshandle):
        """
            Get all the interface addresses (IPv4 and IPv6) on the
            NetworkInterface
        
            Parameters:
             - xoshandle
            """
        pass



    def NetworkInterface_getPrefixListIDL(self, xoshandle):
        """
            Get all the interface prefixes (IPv4 and IPv6) on the
            NetworkInterface
        
            Parameters:
             - xoshandle
            """
        pass



    def NetworkInterface_setInterfaceShutdownIDL(self, xosHandle, shutdown):
        """
            API to set Interface shutdown state
        
            Parameters:
             - xosHandle
             - shutdown
            """
        pass



    def NetworkInterface_clearStatisticsIDL(self, xosHandle):
        """
            API to clear Interface statistics
        
            Parameters:
             - xosHandle
            """
        pass



    def NetworkInterface_setDescriptionIDL(self, xosHandle, description):
        """
            API to set Interface Description
        
            Parameters:
             - xosHandle
             - description
            """
        pass



    def NetworkInterface_setIpHelperIDL(self, xosHandle, addr, vrf, setUnset):
        """
            API to set IpHelperIDL
        
            Parameters:
             - xosHandle
             - addr
             - vrf
             - setUnset
            """
        pass



    def NetworkInterface_setIpProxyArpIDL(self, xosHandle, setUnset):
        """
            API to set IpProxyArp
        
            Parameters:
             - xosHandle
             - setUnset
            """
        pass



    def NetworkInterface_setIpUnreachableIDL(self, xosHandle, setUnset):
        """
            API to set Unreachable
        
            Parameters:
             - xosHandle
             - setUnset
            """
        pass



    def NetworkInterface_setIpRedirectIDL(self, xosHandle, setUnset):
        """
            API to set redirects
        
            Parameters:
             - xosHandle
             - setUnset
            """
        pass



    def NetworkInterface_setIpUnicastReversePathIDL(self, xosHandle, ipAccessList, setUnset):
        """
            API to set UnicastReversePathIDL
        
            Parameters:
             - xosHandle
             - ipAccessList
             - setUnset
            """
        pass



    def NetworkInterface_setLoadIntervalIDL(self, xosHandle, interval):
        """
            API to set load interval
        
            Parameters:
             - xosHandle
             - interval
            """
        pass



    def NetworkInterface_setMTUIDL(self, xosHandle, mtu):
        """
            API to set Interface MTU
        
            Parameters:
             - xosHandle
             - mtu
            """
        pass



    def NetworkInterface_setFwdClassIDL(self, xosHandle, cid):
        """
            API to set Interface forward class
        
            Parameters:
             - xosHandle
             - cid
            """
        pass



    def NetworkInterface_setEncapIDL(self, xosHandle, encap):
        """
            API to set Interface Encap
        
            Parameters:
             - xosHandle
             - encap
            """
        pass



    def NetworkInterface_setBwIDL(self, xosHandle, bw):
        """
            API to set Interface bandwidth
        
            Parameters:
             - xosHandle
             - bw
            """
        pass



    def NetworkInterface_setAddressIDL(self, xosHandle, opertype, scope, addr, prefix_len):
        """
            API to set IP Address
        
            Parameters:
             - xosHandle
             - opertype
             - scope
             - addr
             - prefix_len
            """
        pass



    def NetworkInterface_setSwitchportModeIDL(self, xosHandle, mode):
        """
            API to set Interface switchport mode
        
            Parameters:
             - xosHandle
             - mode
            """
        pass



    def NetworkInterface_setLayer2IDL(self, xosHandle, layer2):
        """
            API to set Interface L2/L3 mode
        
            Parameters:
             - xosHandle
             - layer2
            """
        pass



    def NetworkInterface_registerApplicationTagIDL(self, sessionHandle, apptag):
        """
            API to register application tag for interface context filtering
        
            Parameters:
             - sessionHandle
             - apptag
            """
        pass



    def NetworkInterface_setTagIDL(self, xosHandle, tag):
        """
            API to set Interface Tag
        
            Parameters:
             - xosHandle
             - tag
            """
        pass



    def NetworkInterface_getSubInterfaceByIdIDL(self, xosHandle, type, id):
        """
            API to retrieve subinterface by id
        
            Parameters:
             - xosHandle
             - type
             - id
            """
        pass



    def InterfaceStateEvent_registerIDL(self, sessionHandle, xosHandle, interfaceType, stateEventType, maxrun_sec, maxrun_msec):
        """
            ---------------------------------------
            NetworkInterface Event Registration API
            ---------------------------------------
        
            Parameters:
             - sessionHandle
             - xosHandle
             - interfaceType
             - stateEventType
             - maxrun_sec
             - maxrun_msec
            """
        pass



    def InterfaceStatisticsEvent_registerIDL(self, sessionHandle, xosHandle, parameter, poll_interval_sec, poll_interval_msec, entry_value, entry_op, entry_type, exit_value_set, exit_value, exit_op, exit_type, exit_comb, exit_time_sec, exit_time_msec, exit_event, average_factor, maxrun_sec, maxrun_msec):
        """
        Parameters:
         - sessionHandle
         - xosHandle
         - parameter
         - poll_interval_sec
         - poll_interval_msec
         - entry_value
         - entry_op
         - entry_type
         - exit_value_set
         - exit_value
         - exit_op
         - exit_type
         - exit_comb
         - exit_time_sec
         - exit_time_msec
         - exit_event
         - average_factor
         - maxrun_sec
         - maxrun_msec
        """
        pass



    def InterfaceMtuEvent_registerIDL(self, sessionHandle, xosHandle, interfaceType):
        """
            ---------------------------------------
            NetworkInterface MTU Event Registration API
            ---------------------------------------
        
            Parameters:
             - sessionHandle
             - xosHandle
             - interfaceType
            """
        pass



    def InterfaceSpeedEvent_registerIDL(self, sessionHandle, xosHandle, interfaceType):
        """
            ---------------------------------------
            NetworkInterface Speed Event Registration API
            ---------------------------------------
        
            Parameters:
             - sessionHandle
             - xosHandle
             - interfaceType
            """
        pass



    def InterfaceDuplexModeEvent_registerIDL(self, sessionHandle, xosHandle, interfaceType):
        """
            ---------------------------------------
            NetworkInterface Duplex Mode Event Registration API
            ---------------------------------------
        
            Parameters:
             - sessionHandle
             - xosHandle
             - interfaceType
            """
        pass



    def InterfaceAutoNegotiateEvent_registerIDL(self, sessionHandle, xosHandle, interfaceType):
        """
            ---------------------------------------
            NetworkInterface Autoneg Event Registration API
            ---------------------------------------
        
            Parameters:
             - sessionHandle
             - xosHandle
             - interfaceType
            """
        pass



    def InterfaceFlowcontrolEvent_registerIDL(self, sessionHandle, xosHandle, interfaceType):
        """
            ---------------------------------------
            NetworkInterface FlowCtrl Event Registration API
            ---------------------------------------
        
            Parameters:
             - sessionHandle
             - xosHandle
             - interfaceType
            """
        pass



    def InterfaceLayer2ModeEvent_registerIDL(self, sessionHandle, xosHandle, interfaceType):
        """
            ---------------------------------------
            NetworkInterface Layer2 Event Registration API
            ---------------------------------------
        
            Parameters:
             - sessionHandle
             - xosHandle
             - interfaceType
            """
        pass



    def InterfaceForwardClassIDEvent_registerIDL(self, sessionHandle, xosHandle, interfaceType):
        """
            ---------------------------------------
            NetworkInterface FwdClassID Event Registration API
            ---------------------------------------
        
            Parameters:
             - sessionHandle
             - xosHandle
             - interfaceType
            """
        pass



    def InterfaceBandwidthEvent_registerIDL(self, sessionHandle, xosHandle, interfaceType):
        """
            ---------------------------------------
            NetworkInterface Bandwidth Event Registration API
            ---------------------------------------
        
            Parameters:
             - sessionHandle
             - xosHandle
             - interfaceType
            """
        pass



    def InterfaceVrfEvent_registerIDL(self, sessionHandle, xosHandle, interfaceType, vrfname):
        """
            ---------------------------------------
            NetworkInterface Vrf Event Registration API
            ---------------------------------------
        
            Parameters:
             - sessionHandle
             - xosHandle
             - interfaceType
             - vrfname
            """
        pass



    def InterfaceVlanEvent_registerIDL(self, sessionHandle, xosHandle, interfaceType, vlanEvtType):
        """
            ---------------------------------------
            NetworkInterface Vlan Event Registration API
            ---------------------------------------
        
            Parameters:
             - sessionHandle
             - xosHandle
             - interfaceType
             - vlanEvtType
            """
        pass



    def NetworkInterface_getVrfIDL(self, xosHandle):
        """
            Get the Vrf info on a particular interface
        
            Parameters:
             - xosHandle
            """
        pass



    def NetworkInterface_getVlanIDL(self, xosHandle):
        """
            Get the snapshot Vlan on a particular interface
        
            Parameters:
             - xosHandle
            """
        pass



    def NetworkInterface_createConfigIDL(self, sessionHandle, type, index, parentHandle, add):
        """
            Create an Interface configuration
        
            Parameters:
             - sessionHandle
             - type
             - index
             - parentHandle
             - add
            """
        pass



    def NetworkInterface_getBDInstanceIDL(self, xosHandle):
        """
            Get the BridegDomain info on a particular interface
        
            Parameters:
             - xosHandle
            """
        pass



    def PChannel_getMembersIDL(self, sessionHandle, xosHandle):
        """
            Get port channel members
        
            Parameters:
             - sessionHandle
             - xosHandle
            """
        pass



    def PChannel_getMemberModeIDL(self, sessionHandle, xosHandle):
        """
        Parameters:
         - sessionHandle
         - xosHandle
        """
        pass



    def PChannel_getMemberPriorityIDL(self, sessionHandle, xosHandle):
        """
        Parameters:
         - sessionHandle
         - xosHandle
        """
        pass



    def NetworkInterface_getPChannelIDL(self, sessionHandle, xosHandle):
        """
        Parameters:
         - sessionHandle
         - xosHandle
        """
        pass



    def NetworkInterface_getIifIdIDL(self, xosHandle):
        """
            API to get the iif_id of an interface (IOS-XE)
        
            Parameters:
             - xosHandle
            """
        pass




class Client(Iface):

    def __init__(self, iprot, oprot = None):
        self._iprot = self._oprot = iprot
        if oprot != None:
            self._oprot = oprot
        self._seqid = 0



    def NetworkElement_getInterfaceListIDL(self, sessionHandle, xoshandle, ifType, tag, slot):
        """
            Get all the interfaces (physical and logical) on the
            NetworkElement
        
            Parameters:
             - sessionHandle
             - xoshandle
             - ifType
             - tag
             - slot
            """
        self._oprot.rlock.acquire()
        try:
            self.send_NetworkElement_getInterfaceListIDL(sessionHandle, xoshandle, ifType, tag, slot)
            result = self.recv_NetworkElement_getInterfaceListIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_NetworkElement_getInterfaceListIDL(self, sessionHandle, xoshandle, ifType, tag, slot):
        self._oprot.writeMessageBegin('NetworkElement_getInterfaceListIDL', TMessageType.CALL, self._seqid)
        args = NetworkElement_getInterfaceListIDL_args()
        args.sessionHandle = sessionHandle
        args.xoshandle = xoshandle
        args.ifType = ifType
        args.tag = tag
        args.slot = slot
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_NetworkElement_getInterfaceListIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = NetworkElement_getInterfaceListIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'NetworkElement_getInterfaceListIDL failed: unknown result')



    def NetworkElement_getInterfaceByNameIDL(self, ifname):
        """
            Get the interface instance given the name
        
            Parameters:
             - ifname
            """
        self._oprot.rlock.acquire()
        try:
            self.send_NetworkElement_getInterfaceByNameIDL(ifname)
            result = self.recv_NetworkElement_getInterfaceByNameIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_NetworkElement_getInterfaceByNameIDL(self, ifname):
        self._oprot.writeMessageBegin('NetworkElement_getInterfaceByNameIDL', TMessageType.CALL, self._seqid)
        args = NetworkElement_getInterfaceByNameIDL_args()
        args.ifname = ifname
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_NetworkElement_getInterfaceByNameIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = NetworkElement_getInterfaceByNameIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'NetworkElement_getInterfaceByNameIDL failed: unknown result')



    def NetworkElement_getInterfaceByIifIdIDL(self, iif_id):
        """
            Get the interface instance given the iif_id (private for DPSS)
            (IOS-XE if ID outside IOSd)
        
            Parameters:
             - iif_id
            """
        self._oprot.rlock.acquire()
        try:
            self.send_NetworkElement_getInterfaceByIifIdIDL(iif_id)
            result = self.recv_NetworkElement_getInterfaceByIifIdIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_NetworkElement_getInterfaceByIifIdIDL(self, iif_id):
        self._oprot.writeMessageBegin('NetworkElement_getInterfaceByIifIdIDL', TMessageType.CALL, self._seqid)
        args = NetworkElement_getInterfaceByIifIdIDL_args()
        args.iif_id = iif_id
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_NetworkElement_getInterfaceByIifIdIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = NetworkElement_getInterfaceByIifIdIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'NetworkElement_getInterfaceByIifIdIDL failed: unknown result')



    def NetworkElement_getInterfaceByIdIDL(self, if_id):
        """
            Get the interface instance given the if_id / xosHandle (private for DPSS)
        
            Parameters:
             - if_id
            """
        self._oprot.rlock.acquire()
        try:
            self.send_NetworkElement_getInterfaceByIdIDL(if_id)
            result = self.recv_NetworkElement_getInterfaceByIdIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_NetworkElement_getInterfaceByIdIDL(self, if_id):
        self._oprot.writeMessageBegin('NetworkElement_getInterfaceByIdIDL', TMessageType.CALL, self._seqid)
        args = NetworkElement_getInterfaceByIdIDL_args()
        args.if_id = if_id
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_NetworkElement_getInterfaceByIdIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = NetworkElement_getInterfaceByIdIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'NetworkElement_getInterfaceByIdIDL failed: unknown result')



    def NetworkInterface_getPropertyIDL(self, xosHandle):
        """
            Get the InterfaceProperty on a particular interface
            This is done only once for an interface instance
        
            Parameters:
             - xosHandle
            """
        self._oprot.rlock.acquire()
        try:
            self.send_NetworkInterface_getPropertyIDL(xosHandle)
            result = self.recv_NetworkInterface_getPropertyIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_NetworkInterface_getPropertyIDL(self, xosHandle):
        self._oprot.writeMessageBegin('NetworkInterface_getPropertyIDL', TMessageType.CALL, self._seqid)
        args = NetworkInterface_getPropertyIDL_args()
        args.xosHandle = xosHandle
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_NetworkInterface_getPropertyIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = NetworkInterface_getPropertyIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'NetworkInterface_getPropertyIDL failed: unknown result')



    def NetworkInterface_issubInterfaceIDL(self, xosHandle):
        """
            Gets if the Interface is sub-interface or not
        
            Parameters:
             - xosHandle
            """
        self._oprot.rlock.acquire()
        try:
            self.send_NetworkInterface_issubInterfaceIDL(xosHandle)
            result = self.recv_NetworkInterface_issubInterfaceIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_NetworkInterface_issubInterfaceIDL(self, xosHandle):
        self._oprot.writeMessageBegin('NetworkInterface_issubInterfaceIDL', TMessageType.CALL, self._seqid)
        args = NetworkInterface_issubInterfaceIDL_args()
        args.xosHandle = xosHandle
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_NetworkInterface_issubInterfaceIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = NetworkInterface_issubInterfaceIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'NetworkInterface_issubInterfaceIDL failed: unknown result')



    def NetworkInterface_getConfigIDL(self, xosHandle):
        """
            Get the refreshed InterfaceConfig on a particular interface
        
            Parameters:
             - xosHandle
            """
        self._oprot.rlock.acquire()
        try:
            self.send_NetworkInterface_getConfigIDL(xosHandle)
            result = self.recv_NetworkInterface_getConfigIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_NetworkInterface_getConfigIDL(self, xosHandle):
        self._oprot.writeMessageBegin('NetworkInterface_getConfigIDL', TMessageType.CALL, self._seqid)
        args = NetworkInterface_getConfigIDL_args()
        args.xosHandle = xosHandle
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_NetworkInterface_getConfigIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = NetworkInterface_getConfigIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'NetworkInterface_getConfigIDL failed: unknown result')



    def NetworkInterface_getStatusIDL(self, xosHandle):
        """
            Get the snapshot Status on a particular interface
        
            Parameters:
             - xosHandle
            """
        self._oprot.rlock.acquire()
        try:
            self.send_NetworkInterface_getStatusIDL(xosHandle)
            result = self.recv_NetworkInterface_getStatusIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_NetworkInterface_getStatusIDL(self, xosHandle):
        self._oprot.writeMessageBegin('NetworkInterface_getStatusIDL', TMessageType.CALL, self._seqid)
        args = NetworkInterface_getStatusIDL_args()
        args.xosHandle = xosHandle
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_NetworkInterface_getStatusIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = NetworkInterface_getStatusIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'NetworkInterface_getStatusIDL failed: unknown result')



    def NetworkInterface_getStatisticsIDL(self, xosHandle):
        """
            Get the snapshot statistics on a particular interface
        
            Parameters:
             - xosHandle
            """
        self._oprot.rlock.acquire()
        try:
            self.send_NetworkInterface_getStatisticsIDL(xosHandle)
            result = self.recv_NetworkInterface_getStatisticsIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_NetworkInterface_getStatisticsIDL(self, xosHandle):
        self._oprot.writeMessageBegin('NetworkInterface_getStatisticsIDL', TMessageType.CALL, self._seqid)
        args = NetworkInterface_getStatisticsIDL_args()
        args.xosHandle = xosHandle
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_NetworkInterface_getStatisticsIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = NetworkInterface_getStatisticsIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'NetworkInterface_getStatisticsIDL failed: unknown result')



    def NetworkInterface_getParentIDL(self, xosHandle):
        """
            Get parent(base) interface, if any
        
            Parameters:
             - xosHandle
            """
        self._oprot.rlock.acquire()
        try:
            self.send_NetworkInterface_getParentIDL(xosHandle)
            result = self.recv_NetworkInterface_getParentIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_NetworkInterface_getParentIDL(self, xosHandle):
        self._oprot.writeMessageBegin('NetworkInterface_getParentIDL', TMessageType.CALL, self._seqid)
        args = NetworkInterface_getParentIDL_args()
        args.xosHandle = xosHandle
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_NetworkInterface_getParentIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = NetworkInterface_getParentIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'NetworkInterface_getParentIDL failed: unknown result')



    def NetworkInterface_getSubInterfaceIDL(self, xosHandle):
        """
            Get parent(base) interface, if any
        
            Parameters:
             - xosHandle
            """
        self._oprot.rlock.acquire()
        try:
            self.send_NetworkInterface_getSubInterfaceIDL(xosHandle)
            result = self.recv_NetworkInterface_getSubInterfaceIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_NetworkInterface_getSubInterfaceIDL(self, xosHandle):
        self._oprot.writeMessageBegin('NetworkInterface_getSubInterfaceIDL', TMessageType.CALL, self._seqid)
        args = NetworkInterface_getSubInterfaceIDL_args()
        args.xosHandle = xosHandle
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_NetworkInterface_getSubInterfaceIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = NetworkInterface_getSubInterfaceIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'NetworkInterface_getSubInterfaceIDL failed: unknown result')



    def NetworkInterface_getAddressListIDL(self, xoshandle):
        """
            Get all the interface addresses (IPv4 and IPv6) on the
            NetworkInterface
        
            Parameters:
             - xoshandle
            """
        self._oprot.rlock.acquire()
        try:
            self.send_NetworkInterface_getAddressListIDL(xoshandle)
            result = self.recv_NetworkInterface_getAddressListIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_NetworkInterface_getAddressListIDL(self, xoshandle):
        self._oprot.writeMessageBegin('NetworkInterface_getAddressListIDL', TMessageType.CALL, self._seqid)
        args = NetworkInterface_getAddressListIDL_args()
        args.xoshandle = xoshandle
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_NetworkInterface_getAddressListIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = NetworkInterface_getAddressListIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'NetworkInterface_getAddressListIDL failed: unknown result')



    def NetworkInterface_getPrefixListIDL(self, xoshandle):
        """
            Get all the interface prefixes (IPv4 and IPv6) on the
            NetworkInterface
        
            Parameters:
             - xoshandle
            """
        self._oprot.rlock.acquire()
        try:
            self.send_NetworkInterface_getPrefixListIDL(xoshandle)
            result = self.recv_NetworkInterface_getPrefixListIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_NetworkInterface_getPrefixListIDL(self, xoshandle):
        self._oprot.writeMessageBegin('NetworkInterface_getPrefixListIDL', TMessageType.CALL, self._seqid)
        args = NetworkInterface_getPrefixListIDL_args()
        args.xoshandle = xoshandle
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_NetworkInterface_getPrefixListIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = NetworkInterface_getPrefixListIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'NetworkInterface_getPrefixListIDL failed: unknown result')



    def NetworkInterface_setInterfaceShutdownIDL(self, xosHandle, shutdown):
        """
            API to set Interface shutdown state
        
            Parameters:
             - xosHandle
             - shutdown
            """
        self._oprot.rlock.acquire()
        try:
            self.send_NetworkInterface_setInterfaceShutdownIDL(xosHandle, shutdown)
            result = self.recv_NetworkInterface_setInterfaceShutdownIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_NetworkInterface_setInterfaceShutdownIDL(self, xosHandle, shutdown):
        self._oprot.writeMessageBegin('NetworkInterface_setInterfaceShutdownIDL', TMessageType.CALL, self._seqid)
        args = NetworkInterface_setInterfaceShutdownIDL_args()
        args.xosHandle = xosHandle
        args.shutdown = shutdown
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_NetworkInterface_setInterfaceShutdownIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = NetworkInterface_setInterfaceShutdownIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'NetworkInterface_setInterfaceShutdownIDL failed: unknown result')



    def NetworkInterface_clearStatisticsIDL(self, xosHandle):
        """
            API to clear Interface statistics
        
            Parameters:
             - xosHandle
            """
        self._oprot.rlock.acquire()
        try:
            self.send_NetworkInterface_clearStatisticsIDL(xosHandle)
            result = self.recv_NetworkInterface_clearStatisticsIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_NetworkInterface_clearStatisticsIDL(self, xosHandle):
        self._oprot.writeMessageBegin('NetworkInterface_clearStatisticsIDL', TMessageType.CALL, self._seqid)
        args = NetworkInterface_clearStatisticsIDL_args()
        args.xosHandle = xosHandle
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_NetworkInterface_clearStatisticsIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = NetworkInterface_clearStatisticsIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'NetworkInterface_clearStatisticsIDL failed: unknown result')



    def NetworkInterface_setDescriptionIDL(self, xosHandle, description):
        """
            API to set Interface Description
        
            Parameters:
             - xosHandle
             - description
            """
        self._oprot.rlock.acquire()
        try:
            self.send_NetworkInterface_setDescriptionIDL(xosHandle, description)
            result = self.recv_NetworkInterface_setDescriptionIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_NetworkInterface_setDescriptionIDL(self, xosHandle, description):
        self._oprot.writeMessageBegin('NetworkInterface_setDescriptionIDL', TMessageType.CALL, self._seqid)
        args = NetworkInterface_setDescriptionIDL_args()
        args.xosHandle = xosHandle
        args.description = description
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_NetworkInterface_setDescriptionIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = NetworkInterface_setDescriptionIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'NetworkInterface_setDescriptionIDL failed: unknown result')



    def NetworkInterface_setIpHelperIDL(self, xosHandle, addr, vrf, setUnset):
        """
            API to set IpHelperIDL
        
            Parameters:
             - xosHandle
             - addr
             - vrf
             - setUnset
            """
        self._oprot.rlock.acquire()
        try:
            self.send_NetworkInterface_setIpHelperIDL(xosHandle, addr, vrf, setUnset)
            result = self.recv_NetworkInterface_setIpHelperIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_NetworkInterface_setIpHelperIDL(self, xosHandle, addr, vrf, setUnset):
        self._oprot.writeMessageBegin('NetworkInterface_setIpHelperIDL', TMessageType.CALL, self._seqid)
        args = NetworkInterface_setIpHelperIDL_args()
        args.xosHandle = xosHandle
        args.addr = addr
        args.vrf = vrf
        args.setUnset = setUnset
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_NetworkInterface_setIpHelperIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = NetworkInterface_setIpHelperIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'NetworkInterface_setIpHelperIDL failed: unknown result')



    def NetworkInterface_setIpProxyArpIDL(self, xosHandle, setUnset):
        """
            API to set IpProxyArp
        
            Parameters:
             - xosHandle
             - setUnset
            """
        self._oprot.rlock.acquire()
        try:
            self.send_NetworkInterface_setIpProxyArpIDL(xosHandle, setUnset)
            result = self.recv_NetworkInterface_setIpProxyArpIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_NetworkInterface_setIpProxyArpIDL(self, xosHandle, setUnset):
        self._oprot.writeMessageBegin('NetworkInterface_setIpProxyArpIDL', TMessageType.CALL, self._seqid)
        args = NetworkInterface_setIpProxyArpIDL_args()
        args.xosHandle = xosHandle
        args.setUnset = setUnset
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_NetworkInterface_setIpProxyArpIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = NetworkInterface_setIpProxyArpIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'NetworkInterface_setIpProxyArpIDL failed: unknown result')



    def NetworkInterface_setIpUnreachableIDL(self, xosHandle, setUnset):
        """
            API to set Unreachable
        
            Parameters:
             - xosHandle
             - setUnset
            """
        self._oprot.rlock.acquire()
        try:
            self.send_NetworkInterface_setIpUnreachableIDL(xosHandle, setUnset)
            result = self.recv_NetworkInterface_setIpUnreachableIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_NetworkInterface_setIpUnreachableIDL(self, xosHandle, setUnset):
        self._oprot.writeMessageBegin('NetworkInterface_setIpUnreachableIDL', TMessageType.CALL, self._seqid)
        args = NetworkInterface_setIpUnreachableIDL_args()
        args.xosHandle = xosHandle
        args.setUnset = setUnset
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_NetworkInterface_setIpUnreachableIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = NetworkInterface_setIpUnreachableIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'NetworkInterface_setIpUnreachableIDL failed: unknown result')



    def NetworkInterface_setIpRedirectIDL(self, xosHandle, setUnset):
        """
            API to set redirects
        
            Parameters:
             - xosHandle
             - setUnset
            """
        self._oprot.rlock.acquire()
        try:
            self.send_NetworkInterface_setIpRedirectIDL(xosHandle, setUnset)
            result = self.recv_NetworkInterface_setIpRedirectIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_NetworkInterface_setIpRedirectIDL(self, xosHandle, setUnset):
        self._oprot.writeMessageBegin('NetworkInterface_setIpRedirectIDL', TMessageType.CALL, self._seqid)
        args = NetworkInterface_setIpRedirectIDL_args()
        args.xosHandle = xosHandle
        args.setUnset = setUnset
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_NetworkInterface_setIpRedirectIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = NetworkInterface_setIpRedirectIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'NetworkInterface_setIpRedirectIDL failed: unknown result')



    def NetworkInterface_setIpUnicastReversePathIDL(self, xosHandle, ipAccessList, setUnset):
        """
            API to set UnicastReversePathIDL
        
            Parameters:
             - xosHandle
             - ipAccessList
             - setUnset
            """
        self._oprot.rlock.acquire()
        try:
            self.send_NetworkInterface_setIpUnicastReversePathIDL(xosHandle, ipAccessList, setUnset)
            result = self.recv_NetworkInterface_setIpUnicastReversePathIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_NetworkInterface_setIpUnicastReversePathIDL(self, xosHandle, ipAccessList, setUnset):
        self._oprot.writeMessageBegin('NetworkInterface_setIpUnicastReversePathIDL', TMessageType.CALL, self._seqid)
        args = NetworkInterface_setIpUnicastReversePathIDL_args()
        args.xosHandle = xosHandle
        args.ipAccessList = ipAccessList
        args.setUnset = setUnset
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_NetworkInterface_setIpUnicastReversePathIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = NetworkInterface_setIpUnicastReversePathIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'NetworkInterface_setIpUnicastReversePathIDL failed: unknown result')



    def NetworkInterface_setLoadIntervalIDL(self, xosHandle, interval):
        """
            API to set load interval
        
            Parameters:
             - xosHandle
             - interval
            """
        self._oprot.rlock.acquire()
        try:
            self.send_NetworkInterface_setLoadIntervalIDL(xosHandle, interval)
            result = self.recv_NetworkInterface_setLoadIntervalIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_NetworkInterface_setLoadIntervalIDL(self, xosHandle, interval):
        self._oprot.writeMessageBegin('NetworkInterface_setLoadIntervalIDL', TMessageType.CALL, self._seqid)
        args = NetworkInterface_setLoadIntervalIDL_args()
        args.xosHandle = xosHandle
        args.interval = interval
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_NetworkInterface_setLoadIntervalIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = NetworkInterface_setLoadIntervalIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'NetworkInterface_setLoadIntervalIDL failed: unknown result')



    def NetworkInterface_setMTUIDL(self, xosHandle, mtu):
        """
            API to set Interface MTU
        
            Parameters:
             - xosHandle
             - mtu
            """
        self._oprot.rlock.acquire()
        try:
            self.send_NetworkInterface_setMTUIDL(xosHandle, mtu)
            result = self.recv_NetworkInterface_setMTUIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_NetworkInterface_setMTUIDL(self, xosHandle, mtu):
        self._oprot.writeMessageBegin('NetworkInterface_setMTUIDL', TMessageType.CALL, self._seqid)
        args = NetworkInterface_setMTUIDL_args()
        args.xosHandle = xosHandle
        args.mtu = mtu
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_NetworkInterface_setMTUIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = NetworkInterface_setMTUIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'NetworkInterface_setMTUIDL failed: unknown result')



    def NetworkInterface_setFwdClassIDL(self, xosHandle, cid):
        """
            API to set Interface forward class
        
            Parameters:
             - xosHandle
             - cid
            """
        self._oprot.rlock.acquire()
        try:
            self.send_NetworkInterface_setFwdClassIDL(xosHandle, cid)
            result = self.recv_NetworkInterface_setFwdClassIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_NetworkInterface_setFwdClassIDL(self, xosHandle, cid):
        self._oprot.writeMessageBegin('NetworkInterface_setFwdClassIDL', TMessageType.CALL, self._seqid)
        args = NetworkInterface_setFwdClassIDL_args()
        args.xosHandle = xosHandle
        args.cid = cid
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_NetworkInterface_setFwdClassIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = NetworkInterface_setFwdClassIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'NetworkInterface_setFwdClassIDL failed: unknown result')



    def NetworkInterface_setEncapIDL(self, xosHandle, encap):
        """
            API to set Interface Encap
        
            Parameters:
             - xosHandle
             - encap
            """
        self._oprot.rlock.acquire()
        try:
            self.send_NetworkInterface_setEncapIDL(xosHandle, encap)
            result = self.recv_NetworkInterface_setEncapIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_NetworkInterface_setEncapIDL(self, xosHandle, encap):
        self._oprot.writeMessageBegin('NetworkInterface_setEncapIDL', TMessageType.CALL, self._seqid)
        args = NetworkInterface_setEncapIDL_args()
        args.xosHandle = xosHandle
        args.encap = encap
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_NetworkInterface_setEncapIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = NetworkInterface_setEncapIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'NetworkInterface_setEncapIDL failed: unknown result')



    def NetworkInterface_setBwIDL(self, xosHandle, bw):
        """
            API to set Interface bandwidth
        
            Parameters:
             - xosHandle
             - bw
            """
        self._oprot.rlock.acquire()
        try:
            self.send_NetworkInterface_setBwIDL(xosHandle, bw)
            result = self.recv_NetworkInterface_setBwIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_NetworkInterface_setBwIDL(self, xosHandle, bw):
        self._oprot.writeMessageBegin('NetworkInterface_setBwIDL', TMessageType.CALL, self._seqid)
        args = NetworkInterface_setBwIDL_args()
        args.xosHandle = xosHandle
        args.bw = bw
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_NetworkInterface_setBwIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = NetworkInterface_setBwIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'NetworkInterface_setBwIDL failed: unknown result')



    def NetworkInterface_setAddressIDL(self, xosHandle, opertype, scope, addr, prefix_len):
        """
            API to set IP Address
        
            Parameters:
             - xosHandle
             - opertype
             - scope
             - addr
             - prefix_len
            """
        self._oprot.rlock.acquire()
        try:
            self.send_NetworkInterface_setAddressIDL(xosHandle, opertype, scope, addr, prefix_len)
            result = self.recv_NetworkInterface_setAddressIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_NetworkInterface_setAddressIDL(self, xosHandle, opertype, scope, addr, prefix_len):
        self._oprot.writeMessageBegin('NetworkInterface_setAddressIDL', TMessageType.CALL, self._seqid)
        args = NetworkInterface_setAddressIDL_args()
        args.xosHandle = xosHandle
        args.opertype = opertype
        args.scope = scope
        args.addr = addr
        args.prefix_len = prefix_len
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_NetworkInterface_setAddressIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = NetworkInterface_setAddressIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'NetworkInterface_setAddressIDL failed: unknown result')



    def NetworkInterface_setSwitchportModeIDL(self, xosHandle, mode):
        """
            API to set Interface switchport mode
        
            Parameters:
             - xosHandle
             - mode
            """
        self._oprot.rlock.acquire()
        try:
            self.send_NetworkInterface_setSwitchportModeIDL(xosHandle, mode)
            result = self.recv_NetworkInterface_setSwitchportModeIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_NetworkInterface_setSwitchportModeIDL(self, xosHandle, mode):
        self._oprot.writeMessageBegin('NetworkInterface_setSwitchportModeIDL', TMessageType.CALL, self._seqid)
        args = NetworkInterface_setSwitchportModeIDL_args()
        args.xosHandle = xosHandle
        args.mode = mode
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_NetworkInterface_setSwitchportModeIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = NetworkInterface_setSwitchportModeIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'NetworkInterface_setSwitchportModeIDL failed: unknown result')



    def NetworkInterface_setLayer2IDL(self, xosHandle, layer2):
        """
            API to set Interface L2/L3 mode
        
            Parameters:
             - xosHandle
             - layer2
            """
        self._oprot.rlock.acquire()
        try:
            self.send_NetworkInterface_setLayer2IDL(xosHandle, layer2)
            result = self.recv_NetworkInterface_setLayer2IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_NetworkInterface_setLayer2IDL(self, xosHandle, layer2):
        self._oprot.writeMessageBegin('NetworkInterface_setLayer2IDL', TMessageType.CALL, self._seqid)
        args = NetworkInterface_setLayer2IDL_args()
        args.xosHandle = xosHandle
        args.layer2 = layer2
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_NetworkInterface_setLayer2IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = NetworkInterface_setLayer2IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'NetworkInterface_setLayer2IDL failed: unknown result')



    def NetworkInterface_registerApplicationTagIDL(self, sessionHandle, apptag):
        """
            API to register application tag for interface context filtering
        
            Parameters:
             - sessionHandle
             - apptag
            """
        self._oprot.rlock.acquire()
        try:
            self.send_NetworkInterface_registerApplicationTagIDL(sessionHandle, apptag)
            result = self.recv_NetworkInterface_registerApplicationTagIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_NetworkInterface_registerApplicationTagIDL(self, sessionHandle, apptag):
        self._oprot.writeMessageBegin('NetworkInterface_registerApplicationTagIDL', TMessageType.CALL, self._seqid)
        args = NetworkInterface_registerApplicationTagIDL_args()
        args.sessionHandle = sessionHandle
        args.apptag = apptag
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_NetworkInterface_registerApplicationTagIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = NetworkInterface_registerApplicationTagIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'NetworkInterface_registerApplicationTagIDL failed: unknown result')



    def NetworkInterface_setTagIDL(self, xosHandle, tag):
        """
            API to set Interface Tag
        
            Parameters:
             - xosHandle
             - tag
            """
        self._oprot.rlock.acquire()
        try:
            self.send_NetworkInterface_setTagIDL(xosHandle, tag)
            result = self.recv_NetworkInterface_setTagIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_NetworkInterface_setTagIDL(self, xosHandle, tag):
        self._oprot.writeMessageBegin('NetworkInterface_setTagIDL', TMessageType.CALL, self._seqid)
        args = NetworkInterface_setTagIDL_args()
        args.xosHandle = xosHandle
        args.tag = tag
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_NetworkInterface_setTagIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = NetworkInterface_setTagIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'NetworkInterface_setTagIDL failed: unknown result')



    def NetworkInterface_getSubInterfaceByIdIDL(self, xosHandle, type, id):
        """
            API to retrieve subinterface by id
        
            Parameters:
             - xosHandle
             - type
             - id
            """
        self._oprot.rlock.acquire()
        try:
            self.send_NetworkInterface_getSubInterfaceByIdIDL(xosHandle, type, id)
            result = self.recv_NetworkInterface_getSubInterfaceByIdIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_NetworkInterface_getSubInterfaceByIdIDL(self, xosHandle, type, id):
        self._oprot.writeMessageBegin('NetworkInterface_getSubInterfaceByIdIDL', TMessageType.CALL, self._seqid)
        args = NetworkInterface_getSubInterfaceByIdIDL_args()
        args.xosHandle = xosHandle
        args.type = type
        args.id = id
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_NetworkInterface_getSubInterfaceByIdIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = NetworkInterface_getSubInterfaceByIdIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'NetworkInterface_getSubInterfaceByIdIDL failed: unknown result')



    def InterfaceStateEvent_registerIDL(self, sessionHandle, xosHandle, interfaceType, stateEventType, maxrun_sec, maxrun_msec):
        """
            ---------------------------------------
            NetworkInterface Event Registration API
            ---------------------------------------
        
            Parameters:
             - sessionHandle
             - xosHandle
             - interfaceType
             - stateEventType
             - maxrun_sec
             - maxrun_msec
            """
        self._oprot.rlock.acquire()
        try:
            self.send_InterfaceStateEvent_registerIDL(sessionHandle, xosHandle, interfaceType, stateEventType, maxrun_sec, maxrun_msec)
            result = self.recv_InterfaceStateEvent_registerIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_InterfaceStateEvent_registerIDL(self, sessionHandle, xosHandle, interfaceType, stateEventType, maxrun_sec, maxrun_msec):
        self._oprot.writeMessageBegin('InterfaceStateEvent_registerIDL', TMessageType.CALL, self._seqid)
        args = InterfaceStateEvent_registerIDL_args()
        args.sessionHandle = sessionHandle
        args.xosHandle = xosHandle
        args.interfaceType = interfaceType
        args.stateEventType = stateEventType
        args.maxrun_sec = maxrun_sec
        args.maxrun_msec = maxrun_msec
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_InterfaceStateEvent_registerIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = InterfaceStateEvent_registerIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'InterfaceStateEvent_registerIDL failed: unknown result')



    def InterfaceStatisticsEvent_registerIDL(self, sessionHandle, xosHandle, parameter, poll_interval_sec, poll_interval_msec, entry_value, entry_op, entry_type, exit_value_set, exit_value, exit_op, exit_type, exit_comb, exit_time_sec, exit_time_msec, exit_event, average_factor, maxrun_sec, maxrun_msec):
        """
        Parameters:
         - sessionHandle
         - xosHandle
         - parameter
         - poll_interval_sec
         - poll_interval_msec
         - entry_value
         - entry_op
         - entry_type
         - exit_value_set
         - exit_value
         - exit_op
         - exit_type
         - exit_comb
         - exit_time_sec
         - exit_time_msec
         - exit_event
         - average_factor
         - maxrun_sec
         - maxrun_msec
        """
        self._oprot.rlock.acquire()
        try:
            self.send_InterfaceStatisticsEvent_registerIDL(sessionHandle, xosHandle, parameter, poll_interval_sec, poll_interval_msec, entry_value, entry_op, entry_type, exit_value_set, exit_value, exit_op, exit_type, exit_comb, exit_time_sec, exit_time_msec, exit_event, average_factor, maxrun_sec, maxrun_msec)
            result = self.recv_InterfaceStatisticsEvent_registerIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_InterfaceStatisticsEvent_registerIDL(self, sessionHandle, xosHandle, parameter, poll_interval_sec, poll_interval_msec, entry_value, entry_op, entry_type, exit_value_set, exit_value, exit_op, exit_type, exit_comb, exit_time_sec, exit_time_msec, exit_event, average_factor, maxrun_sec, maxrun_msec):
        self._oprot.writeMessageBegin('InterfaceStatisticsEvent_registerIDL', TMessageType.CALL, self._seqid)
        args = InterfaceStatisticsEvent_registerIDL_args()
        args.sessionHandle = sessionHandle
        args.xosHandle = xosHandle
        args.parameter = parameter
        args.poll_interval_sec = poll_interval_sec
        args.poll_interval_msec = poll_interval_msec
        args.entry_value = entry_value
        args.entry_op = entry_op
        args.entry_type = entry_type
        args.exit_value_set = exit_value_set
        args.exit_value = exit_value
        args.exit_op = exit_op
        args.exit_type = exit_type
        args.exit_comb = exit_comb
        args.exit_time_sec = exit_time_sec
        args.exit_time_msec = exit_time_msec
        args.exit_event = exit_event
        args.average_factor = average_factor
        args.maxrun_sec = maxrun_sec
        args.maxrun_msec = maxrun_msec
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_InterfaceStatisticsEvent_registerIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = InterfaceStatisticsEvent_registerIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'InterfaceStatisticsEvent_registerIDL failed: unknown result')



    def InterfaceMtuEvent_registerIDL(self, sessionHandle, xosHandle, interfaceType):
        """
            ---------------------------------------
            NetworkInterface MTU Event Registration API
            ---------------------------------------
        
            Parameters:
             - sessionHandle
             - xosHandle
             - interfaceType
            """
        self._oprot.rlock.acquire()
        try:
            self.send_InterfaceMtuEvent_registerIDL(sessionHandle, xosHandle, interfaceType)
            result = self.recv_InterfaceMtuEvent_registerIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_InterfaceMtuEvent_registerIDL(self, sessionHandle, xosHandle, interfaceType):
        self._oprot.writeMessageBegin('InterfaceMtuEvent_registerIDL', TMessageType.CALL, self._seqid)
        args = InterfaceMtuEvent_registerIDL_args()
        args.sessionHandle = sessionHandle
        args.xosHandle = xosHandle
        args.interfaceType = interfaceType
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_InterfaceMtuEvent_registerIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = InterfaceMtuEvent_registerIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'InterfaceMtuEvent_registerIDL failed: unknown result')



    def InterfaceSpeedEvent_registerIDL(self, sessionHandle, xosHandle, interfaceType):
        """
            ---------------------------------------
            NetworkInterface Speed Event Registration API
            ---------------------------------------
        
            Parameters:
             - sessionHandle
             - xosHandle
             - interfaceType
            """
        self._oprot.rlock.acquire()
        try:
            self.send_InterfaceSpeedEvent_registerIDL(sessionHandle, xosHandle, interfaceType)
            result = self.recv_InterfaceSpeedEvent_registerIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_InterfaceSpeedEvent_registerIDL(self, sessionHandle, xosHandle, interfaceType):
        self._oprot.writeMessageBegin('InterfaceSpeedEvent_registerIDL', TMessageType.CALL, self._seqid)
        args = InterfaceSpeedEvent_registerIDL_args()
        args.sessionHandle = sessionHandle
        args.xosHandle = xosHandle
        args.interfaceType = interfaceType
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_InterfaceSpeedEvent_registerIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = InterfaceSpeedEvent_registerIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'InterfaceSpeedEvent_registerIDL failed: unknown result')



    def InterfaceDuplexModeEvent_registerIDL(self, sessionHandle, xosHandle, interfaceType):
        """
            ---------------------------------------
            NetworkInterface Duplex Mode Event Registration API
            ---------------------------------------
        
            Parameters:
             - sessionHandle
             - xosHandle
             - interfaceType
            """
        self._oprot.rlock.acquire()
        try:
            self.send_InterfaceDuplexModeEvent_registerIDL(sessionHandle, xosHandle, interfaceType)
            result = self.recv_InterfaceDuplexModeEvent_registerIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_InterfaceDuplexModeEvent_registerIDL(self, sessionHandle, xosHandle, interfaceType):
        self._oprot.writeMessageBegin('InterfaceDuplexModeEvent_registerIDL', TMessageType.CALL, self._seqid)
        args = InterfaceDuplexModeEvent_registerIDL_args()
        args.sessionHandle = sessionHandle
        args.xosHandle = xosHandle
        args.interfaceType = interfaceType
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_InterfaceDuplexModeEvent_registerIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = InterfaceDuplexModeEvent_registerIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'InterfaceDuplexModeEvent_registerIDL failed: unknown result')



    def InterfaceAutoNegotiateEvent_registerIDL(self, sessionHandle, xosHandle, interfaceType):
        """
            ---------------------------------------
            NetworkInterface Autoneg Event Registration API
            ---------------------------------------
        
            Parameters:
             - sessionHandle
             - xosHandle
             - interfaceType
            """
        self._oprot.rlock.acquire()
        try:
            self.send_InterfaceAutoNegotiateEvent_registerIDL(sessionHandle, xosHandle, interfaceType)
            result = self.recv_InterfaceAutoNegotiateEvent_registerIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_InterfaceAutoNegotiateEvent_registerIDL(self, sessionHandle, xosHandle, interfaceType):
        self._oprot.writeMessageBegin('InterfaceAutoNegotiateEvent_registerIDL', TMessageType.CALL, self._seqid)
        args = InterfaceAutoNegotiateEvent_registerIDL_args()
        args.sessionHandle = sessionHandle
        args.xosHandle = xosHandle
        args.interfaceType = interfaceType
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_InterfaceAutoNegotiateEvent_registerIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = InterfaceAutoNegotiateEvent_registerIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'InterfaceAutoNegotiateEvent_registerIDL failed: unknown result')



    def InterfaceFlowcontrolEvent_registerIDL(self, sessionHandle, xosHandle, interfaceType):
        """
            ---------------------------------------
            NetworkInterface FlowCtrl Event Registration API
            ---------------------------------------
        
            Parameters:
             - sessionHandle
             - xosHandle
             - interfaceType
            """
        self._oprot.rlock.acquire()
        try:
            self.send_InterfaceFlowcontrolEvent_registerIDL(sessionHandle, xosHandle, interfaceType)
            result = self.recv_InterfaceFlowcontrolEvent_registerIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_InterfaceFlowcontrolEvent_registerIDL(self, sessionHandle, xosHandle, interfaceType):
        self._oprot.writeMessageBegin('InterfaceFlowcontrolEvent_registerIDL', TMessageType.CALL, self._seqid)
        args = InterfaceFlowcontrolEvent_registerIDL_args()
        args.sessionHandle = sessionHandle
        args.xosHandle = xosHandle
        args.interfaceType = interfaceType
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_InterfaceFlowcontrolEvent_registerIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = InterfaceFlowcontrolEvent_registerIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'InterfaceFlowcontrolEvent_registerIDL failed: unknown result')



    def InterfaceLayer2ModeEvent_registerIDL(self, sessionHandle, xosHandle, interfaceType):
        """
            ---------------------------------------
            NetworkInterface Layer2 Event Registration API
            ---------------------------------------
        
            Parameters:
             - sessionHandle
             - xosHandle
             - interfaceType
            """
        self._oprot.rlock.acquire()
        try:
            self.send_InterfaceLayer2ModeEvent_registerIDL(sessionHandle, xosHandle, interfaceType)
            result = self.recv_InterfaceLayer2ModeEvent_registerIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_InterfaceLayer2ModeEvent_registerIDL(self, sessionHandle, xosHandle, interfaceType):
        self._oprot.writeMessageBegin('InterfaceLayer2ModeEvent_registerIDL', TMessageType.CALL, self._seqid)
        args = InterfaceLayer2ModeEvent_registerIDL_args()
        args.sessionHandle = sessionHandle
        args.xosHandle = xosHandle
        args.interfaceType = interfaceType
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_InterfaceLayer2ModeEvent_registerIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = InterfaceLayer2ModeEvent_registerIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'InterfaceLayer2ModeEvent_registerIDL failed: unknown result')



    def InterfaceForwardClassIDEvent_registerIDL(self, sessionHandle, xosHandle, interfaceType):
        """
            ---------------------------------------
            NetworkInterface FwdClassID Event Registration API
            ---------------------------------------
        
            Parameters:
             - sessionHandle
             - xosHandle
             - interfaceType
            """
        self._oprot.rlock.acquire()
        try:
            self.send_InterfaceForwardClassIDEvent_registerIDL(sessionHandle, xosHandle, interfaceType)
            result = self.recv_InterfaceForwardClassIDEvent_registerIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_InterfaceForwardClassIDEvent_registerIDL(self, sessionHandle, xosHandle, interfaceType):
        self._oprot.writeMessageBegin('InterfaceForwardClassIDEvent_registerIDL', TMessageType.CALL, self._seqid)
        args = InterfaceForwardClassIDEvent_registerIDL_args()
        args.sessionHandle = sessionHandle
        args.xosHandle = xosHandle
        args.interfaceType = interfaceType
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_InterfaceForwardClassIDEvent_registerIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = InterfaceForwardClassIDEvent_registerIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'InterfaceForwardClassIDEvent_registerIDL failed: unknown result')



    def InterfaceBandwidthEvent_registerIDL(self, sessionHandle, xosHandle, interfaceType):
        """
            ---------------------------------------
            NetworkInterface Bandwidth Event Registration API
            ---------------------------------------
        
            Parameters:
             - sessionHandle
             - xosHandle
             - interfaceType
            """
        self._oprot.rlock.acquire()
        try:
            self.send_InterfaceBandwidthEvent_registerIDL(sessionHandle, xosHandle, interfaceType)
            result = self.recv_InterfaceBandwidthEvent_registerIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_InterfaceBandwidthEvent_registerIDL(self, sessionHandle, xosHandle, interfaceType):
        self._oprot.writeMessageBegin('InterfaceBandwidthEvent_registerIDL', TMessageType.CALL, self._seqid)
        args = InterfaceBandwidthEvent_registerIDL_args()
        args.sessionHandle = sessionHandle
        args.xosHandle = xosHandle
        args.interfaceType = interfaceType
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_InterfaceBandwidthEvent_registerIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = InterfaceBandwidthEvent_registerIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'InterfaceBandwidthEvent_registerIDL failed: unknown result')



    def InterfaceVrfEvent_registerIDL(self, sessionHandle, xosHandle, interfaceType, vrfname):
        """
            ---------------------------------------
            NetworkInterface Vrf Event Registration API
            ---------------------------------------
        
            Parameters:
             - sessionHandle
             - xosHandle
             - interfaceType
             - vrfname
            """
        self._oprot.rlock.acquire()
        try:
            self.send_InterfaceVrfEvent_registerIDL(sessionHandle, xosHandle, interfaceType, vrfname)
            result = self.recv_InterfaceVrfEvent_registerIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_InterfaceVrfEvent_registerIDL(self, sessionHandle, xosHandle, interfaceType, vrfname):
        self._oprot.writeMessageBegin('InterfaceVrfEvent_registerIDL', TMessageType.CALL, self._seqid)
        args = InterfaceVrfEvent_registerIDL_args()
        args.sessionHandle = sessionHandle
        args.xosHandle = xosHandle
        args.interfaceType = interfaceType
        args.vrfname = vrfname
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_InterfaceVrfEvent_registerIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = InterfaceVrfEvent_registerIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'InterfaceVrfEvent_registerIDL failed: unknown result')



    def InterfaceVlanEvent_registerIDL(self, sessionHandle, xosHandle, interfaceType, vlanEvtType):
        """
            ---------------------------------------
            NetworkInterface Vlan Event Registration API
            ---------------------------------------
        
            Parameters:
             - sessionHandle
             - xosHandle
             - interfaceType
             - vlanEvtType
            """
        self._oprot.rlock.acquire()
        try:
            self.send_InterfaceVlanEvent_registerIDL(sessionHandle, xosHandle, interfaceType, vlanEvtType)
            result = self.recv_InterfaceVlanEvent_registerIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_InterfaceVlanEvent_registerIDL(self, sessionHandle, xosHandle, interfaceType, vlanEvtType):
        self._oprot.writeMessageBegin('InterfaceVlanEvent_registerIDL', TMessageType.CALL, self._seqid)
        args = InterfaceVlanEvent_registerIDL_args()
        args.sessionHandle = sessionHandle
        args.xosHandle = xosHandle
        args.interfaceType = interfaceType
        args.vlanEvtType = vlanEvtType
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_InterfaceVlanEvent_registerIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = InterfaceVlanEvent_registerIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'InterfaceVlanEvent_registerIDL failed: unknown result')



    def NetworkInterface_getVrfIDL(self, xosHandle):
        """
            Get the Vrf info on a particular interface
        
            Parameters:
             - xosHandle
            """
        self._oprot.rlock.acquire()
        try:
            self.send_NetworkInterface_getVrfIDL(xosHandle)
            result = self.recv_NetworkInterface_getVrfIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_NetworkInterface_getVrfIDL(self, xosHandle):
        self._oprot.writeMessageBegin('NetworkInterface_getVrfIDL', TMessageType.CALL, self._seqid)
        args = NetworkInterface_getVrfIDL_args()
        args.xosHandle = xosHandle
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_NetworkInterface_getVrfIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = NetworkInterface_getVrfIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'NetworkInterface_getVrfIDL failed: unknown result')



    def NetworkInterface_getVlanIDL(self, xosHandle):
        """
            Get the snapshot Vlan on a particular interface
        
            Parameters:
             - xosHandle
            """
        self._oprot.rlock.acquire()
        try:
            self.send_NetworkInterface_getVlanIDL(xosHandle)
            result = self.recv_NetworkInterface_getVlanIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_NetworkInterface_getVlanIDL(self, xosHandle):
        self._oprot.writeMessageBegin('NetworkInterface_getVlanIDL', TMessageType.CALL, self._seqid)
        args = NetworkInterface_getVlanIDL_args()
        args.xosHandle = xosHandle
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_NetworkInterface_getVlanIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = NetworkInterface_getVlanIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'NetworkInterface_getVlanIDL failed: unknown result')



    def NetworkInterface_createConfigIDL(self, sessionHandle, type, index, parentHandle, add):
        """
            Create an Interface configuration
        
            Parameters:
             - sessionHandle
             - type
             - index
             - parentHandle
             - add
            """
        self._oprot.rlock.acquire()
        try:
            self.send_NetworkInterface_createConfigIDL(sessionHandle, type, index, parentHandle, add)
            result = self.recv_NetworkInterface_createConfigIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_NetworkInterface_createConfigIDL(self, sessionHandle, type, index, parentHandle, add):
        self._oprot.writeMessageBegin('NetworkInterface_createConfigIDL', TMessageType.CALL, self._seqid)
        args = NetworkInterface_createConfigIDL_args()
        args.sessionHandle = sessionHandle
        args.type = type
        args.index = index
        args.parentHandle = parentHandle
        args.add = add
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_NetworkInterface_createConfigIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = NetworkInterface_createConfigIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'NetworkInterface_createConfigIDL failed: unknown result')



    def NetworkInterface_getBDInstanceIDL(self, xosHandle):
        """
            Get the BridegDomain info on a particular interface
        
            Parameters:
             - xosHandle
            """
        self._oprot.rlock.acquire()
        try:
            self.send_NetworkInterface_getBDInstanceIDL(xosHandle)
            result = self.recv_NetworkInterface_getBDInstanceIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_NetworkInterface_getBDInstanceIDL(self, xosHandle):
        self._oprot.writeMessageBegin('NetworkInterface_getBDInstanceIDL', TMessageType.CALL, self._seqid)
        args = NetworkInterface_getBDInstanceIDL_args()
        args.xosHandle = xosHandle
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_NetworkInterface_getBDInstanceIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = NetworkInterface_getBDInstanceIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'NetworkInterface_getBDInstanceIDL failed: unknown result')



    def PChannel_getMembersIDL(self, sessionHandle, xosHandle):
        """
            Get port channel members
        
            Parameters:
             - sessionHandle
             - xosHandle
            """
        self._oprot.rlock.acquire()
        try:
            self.send_PChannel_getMembersIDL(sessionHandle, xosHandle)
            result = self.recv_PChannel_getMembersIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_PChannel_getMembersIDL(self, sessionHandle, xosHandle):
        self._oprot.writeMessageBegin('PChannel_getMembersIDL', TMessageType.CALL, self._seqid)
        args = PChannel_getMembersIDL_args()
        args.sessionHandle = sessionHandle
        args.xosHandle = xosHandle
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_PChannel_getMembersIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = PChannel_getMembersIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'PChannel_getMembersIDL failed: unknown result')



    def PChannel_getMemberModeIDL(self, sessionHandle, xosHandle):
        """
        Parameters:
         - sessionHandle
         - xosHandle
        """
        self._oprot.rlock.acquire()
        try:
            self.send_PChannel_getMemberModeIDL(sessionHandle, xosHandle)
            result = self.recv_PChannel_getMemberModeIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_PChannel_getMemberModeIDL(self, sessionHandle, xosHandle):
        self._oprot.writeMessageBegin('PChannel_getMemberModeIDL', TMessageType.CALL, self._seqid)
        args = PChannel_getMemberModeIDL_args()
        args.sessionHandle = sessionHandle
        args.xosHandle = xosHandle
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_PChannel_getMemberModeIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = PChannel_getMemberModeIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'PChannel_getMemberModeIDL failed: unknown result')



    def PChannel_getMemberPriorityIDL(self, sessionHandle, xosHandle):
        """
        Parameters:
         - sessionHandle
         - xosHandle
        """
        self._oprot.rlock.acquire()
        try:
            self.send_PChannel_getMemberPriorityIDL(sessionHandle, xosHandle)
            result = self.recv_PChannel_getMemberPriorityIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_PChannel_getMemberPriorityIDL(self, sessionHandle, xosHandle):
        self._oprot.writeMessageBegin('PChannel_getMemberPriorityIDL', TMessageType.CALL, self._seqid)
        args = PChannel_getMemberPriorityIDL_args()
        args.sessionHandle = sessionHandle
        args.xosHandle = xosHandle
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_PChannel_getMemberPriorityIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = PChannel_getMemberPriorityIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'PChannel_getMemberPriorityIDL failed: unknown result')



    def NetworkInterface_getPChannelIDL(self, sessionHandle, xosHandle):
        """
        Parameters:
         - sessionHandle
         - xosHandle
        """
        self._oprot.rlock.acquire()
        try:
            self.send_NetworkInterface_getPChannelIDL(sessionHandle, xosHandle)
            result = self.recv_NetworkInterface_getPChannelIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_NetworkInterface_getPChannelIDL(self, sessionHandle, xosHandle):
        self._oprot.writeMessageBegin('NetworkInterface_getPChannelIDL', TMessageType.CALL, self._seqid)
        args = NetworkInterface_getPChannelIDL_args()
        args.sessionHandle = sessionHandle
        args.xosHandle = xosHandle
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_NetworkInterface_getPChannelIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = NetworkInterface_getPChannelIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'NetworkInterface_getPChannelIDL failed: unknown result')



    def NetworkInterface_getIifIdIDL(self, xosHandle):
        """
            API to get the iif_id of an interface (IOS-XE)
        
            Parameters:
             - xosHandle
            """
        self._oprot.rlock.acquire()
        try:
            self.send_NetworkInterface_getIifIdIDL(xosHandle)
            result = self.recv_NetworkInterface_getIifIdIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_NetworkInterface_getIifIdIDL(self, xosHandle):
        self._oprot.writeMessageBegin('NetworkInterface_getIifIdIDL', TMessageType.CALL, self._seqid)
        args = NetworkInterface_getIifIdIDL_args()
        args.xosHandle = xosHandle
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_NetworkInterface_getIifIdIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = NetworkInterface_getIifIdIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'NetworkInterface_getIifIdIDL failed: unknown result')




class Processor(Iface, TProcessor):

    def __init__(self, handler):
        self._handler = handler
        self._processMap = {}
        self._processMap['NetworkElement_getInterfaceListIDL'] = Processor.process_NetworkElement_getInterfaceListIDL
        self._processMap['NetworkElement_getInterfaceByNameIDL'] = Processor.process_NetworkElement_getInterfaceByNameIDL
        self._processMap['NetworkElement_getInterfaceByIifIdIDL'] = Processor.process_NetworkElement_getInterfaceByIifIdIDL
        self._processMap['NetworkElement_getInterfaceByIdIDL'] = Processor.process_NetworkElement_getInterfaceByIdIDL
        self._processMap['NetworkInterface_getPropertyIDL'] = Processor.process_NetworkInterface_getPropertyIDL
        self._processMap['NetworkInterface_issubInterfaceIDL'] = Processor.process_NetworkInterface_issubInterfaceIDL
        self._processMap['NetworkInterface_getConfigIDL'] = Processor.process_NetworkInterface_getConfigIDL
        self._processMap['NetworkInterface_getStatusIDL'] = Processor.process_NetworkInterface_getStatusIDL
        self._processMap['NetworkInterface_getStatisticsIDL'] = Processor.process_NetworkInterface_getStatisticsIDL
        self._processMap['NetworkInterface_getParentIDL'] = Processor.process_NetworkInterface_getParentIDL
        self._processMap['NetworkInterface_getSubInterfaceIDL'] = Processor.process_NetworkInterface_getSubInterfaceIDL
        self._processMap['NetworkInterface_getAddressListIDL'] = Processor.process_NetworkInterface_getAddressListIDL
        self._processMap['NetworkInterface_getPrefixListIDL'] = Processor.process_NetworkInterface_getPrefixListIDL
        self._processMap['NetworkInterface_setInterfaceShutdownIDL'] = Processor.process_NetworkInterface_setInterfaceShutdownIDL
        self._processMap['NetworkInterface_clearStatisticsIDL'] = Processor.process_NetworkInterface_clearStatisticsIDL
        self._processMap['NetworkInterface_setDescriptionIDL'] = Processor.process_NetworkInterface_setDescriptionIDL
        self._processMap['NetworkInterface_setIpHelperIDL'] = Processor.process_NetworkInterface_setIpHelperIDL
        self._processMap['NetworkInterface_setIpProxyArpIDL'] = Processor.process_NetworkInterface_setIpProxyArpIDL
        self._processMap['NetworkInterface_setIpUnreachableIDL'] = Processor.process_NetworkInterface_setIpUnreachableIDL
        self._processMap['NetworkInterface_setIpRedirectIDL'] = Processor.process_NetworkInterface_setIpRedirectIDL
        self._processMap['NetworkInterface_setIpUnicastReversePathIDL'] = Processor.process_NetworkInterface_setIpUnicastReversePathIDL
        self._processMap['NetworkInterface_setLoadIntervalIDL'] = Processor.process_NetworkInterface_setLoadIntervalIDL
        self._processMap['NetworkInterface_setMTUIDL'] = Processor.process_NetworkInterface_setMTUIDL
        self._processMap['NetworkInterface_setFwdClassIDL'] = Processor.process_NetworkInterface_setFwdClassIDL
        self._processMap['NetworkInterface_setEncapIDL'] = Processor.process_NetworkInterface_setEncapIDL
        self._processMap['NetworkInterface_setBwIDL'] = Processor.process_NetworkInterface_setBwIDL
        self._processMap['NetworkInterface_setAddressIDL'] = Processor.process_NetworkInterface_setAddressIDL
        self._processMap['NetworkInterface_setSwitchportModeIDL'] = Processor.process_NetworkInterface_setSwitchportModeIDL
        self._processMap['NetworkInterface_setLayer2IDL'] = Processor.process_NetworkInterface_setLayer2IDL
        self._processMap['NetworkInterface_registerApplicationTagIDL'] = Processor.process_NetworkInterface_registerApplicationTagIDL
        self._processMap['NetworkInterface_setTagIDL'] = Processor.process_NetworkInterface_setTagIDL
        self._processMap['NetworkInterface_getSubInterfaceByIdIDL'] = Processor.process_NetworkInterface_getSubInterfaceByIdIDL
        self._processMap['InterfaceStateEvent_registerIDL'] = Processor.process_InterfaceStateEvent_registerIDL
        self._processMap['InterfaceStatisticsEvent_registerIDL'] = Processor.process_InterfaceStatisticsEvent_registerIDL
        self._processMap['InterfaceMtuEvent_registerIDL'] = Processor.process_InterfaceMtuEvent_registerIDL
        self._processMap['InterfaceSpeedEvent_registerIDL'] = Processor.process_InterfaceSpeedEvent_registerIDL
        self._processMap['InterfaceDuplexModeEvent_registerIDL'] = Processor.process_InterfaceDuplexModeEvent_registerIDL
        self._processMap['InterfaceAutoNegotiateEvent_registerIDL'] = Processor.process_InterfaceAutoNegotiateEvent_registerIDL
        self._processMap['InterfaceFlowcontrolEvent_registerIDL'] = Processor.process_InterfaceFlowcontrolEvent_registerIDL
        self._processMap['InterfaceLayer2ModeEvent_registerIDL'] = Processor.process_InterfaceLayer2ModeEvent_registerIDL
        self._processMap['InterfaceForwardClassIDEvent_registerIDL'] = Processor.process_InterfaceForwardClassIDEvent_registerIDL
        self._processMap['InterfaceBandwidthEvent_registerIDL'] = Processor.process_InterfaceBandwidthEvent_registerIDL
        self._processMap['InterfaceVrfEvent_registerIDL'] = Processor.process_InterfaceVrfEvent_registerIDL
        self._processMap['InterfaceVlanEvent_registerIDL'] = Processor.process_InterfaceVlanEvent_registerIDL
        self._processMap['NetworkInterface_getVrfIDL'] = Processor.process_NetworkInterface_getVrfIDL
        self._processMap['NetworkInterface_getVlanIDL'] = Processor.process_NetworkInterface_getVlanIDL
        self._processMap['NetworkInterface_createConfigIDL'] = Processor.process_NetworkInterface_createConfigIDL
        self._processMap['NetworkInterface_getBDInstanceIDL'] = Processor.process_NetworkInterface_getBDInstanceIDL
        self._processMap['PChannel_getMembersIDL'] = Processor.process_PChannel_getMembersIDL
        self._processMap['PChannel_getMemberModeIDL'] = Processor.process_PChannel_getMemberModeIDL
        self._processMap['PChannel_getMemberPriorityIDL'] = Processor.process_PChannel_getMemberPriorityIDL
        self._processMap['NetworkInterface_getPChannelIDL'] = Processor.process_NetworkInterface_getPChannelIDL
        self._processMap['NetworkInterface_getIifIdIDL'] = Processor.process_NetworkInterface_getIifIdIDL



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



    def process_NetworkElement_getInterfaceListIDL(self, seqid, iprot, oprot):
        args = NetworkElement_getInterfaceListIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = NetworkElement_getInterfaceListIDL_result()
        try:
            result.success = self._handler.NetworkElement_getInterfaceListIDL(args.sessionHandle, args.xoshandle, args.ifType, args.tag, args.slot)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('NetworkElement_getInterfaceListIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_NetworkElement_getInterfaceByNameIDL(self, seqid, iprot, oprot):
        args = NetworkElement_getInterfaceByNameIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = NetworkElement_getInterfaceByNameIDL_result()
        try:
            result.success = self._handler.NetworkElement_getInterfaceByNameIDL(args.ifname)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('NetworkElement_getInterfaceByNameIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_NetworkElement_getInterfaceByIifIdIDL(self, seqid, iprot, oprot):
        args = NetworkElement_getInterfaceByIifIdIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = NetworkElement_getInterfaceByIifIdIDL_result()
        try:
            result.success = self._handler.NetworkElement_getInterfaceByIifIdIDL(args.iif_id)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('NetworkElement_getInterfaceByIifIdIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_NetworkElement_getInterfaceByIdIDL(self, seqid, iprot, oprot):
        args = NetworkElement_getInterfaceByIdIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = NetworkElement_getInterfaceByIdIDL_result()
        try:
            result.success = self._handler.NetworkElement_getInterfaceByIdIDL(args.if_id)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('NetworkElement_getInterfaceByIdIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_NetworkInterface_getPropertyIDL(self, seqid, iprot, oprot):
        args = NetworkInterface_getPropertyIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = NetworkInterface_getPropertyIDL_result()
        try:
            result.success = self._handler.NetworkInterface_getPropertyIDL(args.xosHandle)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('NetworkInterface_getPropertyIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_NetworkInterface_issubInterfaceIDL(self, seqid, iprot, oprot):
        args = NetworkInterface_issubInterfaceIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = NetworkInterface_issubInterfaceIDL_result()
        try:
            result.success = self._handler.NetworkInterface_issubInterfaceIDL(args.xosHandle)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('NetworkInterface_issubInterfaceIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_NetworkInterface_getConfigIDL(self, seqid, iprot, oprot):
        args = NetworkInterface_getConfigIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = NetworkInterface_getConfigIDL_result()
        try:
            result.success = self._handler.NetworkInterface_getConfigIDL(args.xosHandle)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('NetworkInterface_getConfigIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_NetworkInterface_getStatusIDL(self, seqid, iprot, oprot):
        args = NetworkInterface_getStatusIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = NetworkInterface_getStatusIDL_result()
        try:
            result.success = self._handler.NetworkInterface_getStatusIDL(args.xosHandle)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('NetworkInterface_getStatusIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_NetworkInterface_getStatisticsIDL(self, seqid, iprot, oprot):
        args = NetworkInterface_getStatisticsIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = NetworkInterface_getStatisticsIDL_result()
        try:
            result.success = self._handler.NetworkInterface_getStatisticsIDL(args.xosHandle)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('NetworkInterface_getStatisticsIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_NetworkInterface_getParentIDL(self, seqid, iprot, oprot):
        args = NetworkInterface_getParentIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = NetworkInterface_getParentIDL_result()
        try:
            result.success = self._handler.NetworkInterface_getParentIDL(args.xosHandle)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('NetworkInterface_getParentIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_NetworkInterface_getSubInterfaceIDL(self, seqid, iprot, oprot):
        args = NetworkInterface_getSubInterfaceIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = NetworkInterface_getSubInterfaceIDL_result()
        try:
            result.success = self._handler.NetworkInterface_getSubInterfaceIDL(args.xosHandle)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('NetworkInterface_getSubInterfaceIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_NetworkInterface_getAddressListIDL(self, seqid, iprot, oprot):
        args = NetworkInterface_getAddressListIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = NetworkInterface_getAddressListIDL_result()
        try:
            result.success = self._handler.NetworkInterface_getAddressListIDL(args.xoshandle)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('NetworkInterface_getAddressListIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_NetworkInterface_getPrefixListIDL(self, seqid, iprot, oprot):
        args = NetworkInterface_getPrefixListIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = NetworkInterface_getPrefixListIDL_result()
        try:
            result.success = self._handler.NetworkInterface_getPrefixListIDL(args.xoshandle)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('NetworkInterface_getPrefixListIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_NetworkInterface_setInterfaceShutdownIDL(self, seqid, iprot, oprot):
        args = NetworkInterface_setInterfaceShutdownIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = NetworkInterface_setInterfaceShutdownIDL_result()
        try:
            result.success = self._handler.NetworkInterface_setInterfaceShutdownIDL(args.xosHandle, args.shutdown)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('NetworkInterface_setInterfaceShutdownIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_NetworkInterface_clearStatisticsIDL(self, seqid, iprot, oprot):
        args = NetworkInterface_clearStatisticsIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = NetworkInterface_clearStatisticsIDL_result()
        try:
            result.success = self._handler.NetworkInterface_clearStatisticsIDL(args.xosHandle)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('NetworkInterface_clearStatisticsIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_NetworkInterface_setDescriptionIDL(self, seqid, iprot, oprot):
        args = NetworkInterface_setDescriptionIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = NetworkInterface_setDescriptionIDL_result()
        try:
            result.success = self._handler.NetworkInterface_setDescriptionIDL(args.xosHandle, args.description)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('NetworkInterface_setDescriptionIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_NetworkInterface_setIpHelperIDL(self, seqid, iprot, oprot):
        args = NetworkInterface_setIpHelperIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = NetworkInterface_setIpHelperIDL_result()
        try:
            result.success = self._handler.NetworkInterface_setIpHelperIDL(args.xosHandle, args.addr, args.vrf, args.setUnset)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('NetworkInterface_setIpHelperIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_NetworkInterface_setIpProxyArpIDL(self, seqid, iprot, oprot):
        args = NetworkInterface_setIpProxyArpIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = NetworkInterface_setIpProxyArpIDL_result()
        try:
            result.success = self._handler.NetworkInterface_setIpProxyArpIDL(args.xosHandle, args.setUnset)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('NetworkInterface_setIpProxyArpIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_NetworkInterface_setIpUnreachableIDL(self, seqid, iprot, oprot):
        args = NetworkInterface_setIpUnreachableIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = NetworkInterface_setIpUnreachableIDL_result()
        try:
            result.success = self._handler.NetworkInterface_setIpUnreachableIDL(args.xosHandle, args.setUnset)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('NetworkInterface_setIpUnreachableIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_NetworkInterface_setIpRedirectIDL(self, seqid, iprot, oprot):
        args = NetworkInterface_setIpRedirectIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = NetworkInterface_setIpRedirectIDL_result()
        try:
            result.success = self._handler.NetworkInterface_setIpRedirectIDL(args.xosHandle, args.setUnset)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('NetworkInterface_setIpRedirectIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_NetworkInterface_setIpUnicastReversePathIDL(self, seqid, iprot, oprot):
        args = NetworkInterface_setIpUnicastReversePathIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = NetworkInterface_setIpUnicastReversePathIDL_result()
        try:
            result.success = self._handler.NetworkInterface_setIpUnicastReversePathIDL(args.xosHandle, args.ipAccessList, args.setUnset)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('NetworkInterface_setIpUnicastReversePathIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_NetworkInterface_setLoadIntervalIDL(self, seqid, iprot, oprot):
        args = NetworkInterface_setLoadIntervalIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = NetworkInterface_setLoadIntervalIDL_result()
        try:
            result.success = self._handler.NetworkInterface_setLoadIntervalIDL(args.xosHandle, args.interval)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('NetworkInterface_setLoadIntervalIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_NetworkInterface_setMTUIDL(self, seqid, iprot, oprot):
        args = NetworkInterface_setMTUIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = NetworkInterface_setMTUIDL_result()
        try:
            result.success = self._handler.NetworkInterface_setMTUIDL(args.xosHandle, args.mtu)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('NetworkInterface_setMTUIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_NetworkInterface_setFwdClassIDL(self, seqid, iprot, oprot):
        args = NetworkInterface_setFwdClassIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = NetworkInterface_setFwdClassIDL_result()
        try:
            result.success = self._handler.NetworkInterface_setFwdClassIDL(args.xosHandle, args.cid)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('NetworkInterface_setFwdClassIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_NetworkInterface_setEncapIDL(self, seqid, iprot, oprot):
        args = NetworkInterface_setEncapIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = NetworkInterface_setEncapIDL_result()
        try:
            result.success = self._handler.NetworkInterface_setEncapIDL(args.xosHandle, args.encap)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('NetworkInterface_setEncapIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_NetworkInterface_setBwIDL(self, seqid, iprot, oprot):
        args = NetworkInterface_setBwIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = NetworkInterface_setBwIDL_result()
        try:
            result.success = self._handler.NetworkInterface_setBwIDL(args.xosHandle, args.bw)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('NetworkInterface_setBwIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_NetworkInterface_setAddressIDL(self, seqid, iprot, oprot):
        args = NetworkInterface_setAddressIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = NetworkInterface_setAddressIDL_result()
        try:
            result.success = self._handler.NetworkInterface_setAddressIDL(args.xosHandle, args.opertype, args.scope, args.addr, args.prefix_len)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('NetworkInterface_setAddressIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_NetworkInterface_setSwitchportModeIDL(self, seqid, iprot, oprot):
        args = NetworkInterface_setSwitchportModeIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = NetworkInterface_setSwitchportModeIDL_result()
        try:
            result.success = self._handler.NetworkInterface_setSwitchportModeIDL(args.xosHandle, args.mode)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('NetworkInterface_setSwitchportModeIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_NetworkInterface_setLayer2IDL(self, seqid, iprot, oprot):
        args = NetworkInterface_setLayer2IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = NetworkInterface_setLayer2IDL_result()
        try:
            result.success = self._handler.NetworkInterface_setLayer2IDL(args.xosHandle, args.layer2)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('NetworkInterface_setLayer2IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_NetworkInterface_registerApplicationTagIDL(self, seqid, iprot, oprot):
        args = NetworkInterface_registerApplicationTagIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = NetworkInterface_registerApplicationTagIDL_result()
        try:
            result.success = self._handler.NetworkInterface_registerApplicationTagIDL(args.sessionHandle, args.apptag)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('NetworkInterface_registerApplicationTagIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_NetworkInterface_setTagIDL(self, seqid, iprot, oprot):
        args = NetworkInterface_setTagIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = NetworkInterface_setTagIDL_result()
        try:
            result.success = self._handler.NetworkInterface_setTagIDL(args.xosHandle, args.tag)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('NetworkInterface_setTagIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_NetworkInterface_getSubInterfaceByIdIDL(self, seqid, iprot, oprot):
        args = NetworkInterface_getSubInterfaceByIdIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = NetworkInterface_getSubInterfaceByIdIDL_result()
        try:
            result.success = self._handler.NetworkInterface_getSubInterfaceByIdIDL(args.xosHandle, args.type, args.id)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('NetworkInterface_getSubInterfaceByIdIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_InterfaceStateEvent_registerIDL(self, seqid, iprot, oprot):
        args = InterfaceStateEvent_registerIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = InterfaceStateEvent_registerIDL_result()
        try:
            result.success = self._handler.InterfaceStateEvent_registerIDL(args.sessionHandle, args.xosHandle, args.interfaceType, args.stateEventType, args.maxrun_sec, args.maxrun_msec)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('InterfaceStateEvent_registerIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_InterfaceStatisticsEvent_registerIDL(self, seqid, iprot, oprot):
        args = InterfaceStatisticsEvent_registerIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = InterfaceStatisticsEvent_registerIDL_result()
        try:
            result.success = self._handler.InterfaceStatisticsEvent_registerIDL(args.sessionHandle, args.xosHandle, args.parameter, args.poll_interval_sec, args.poll_interval_msec, args.entry_value, args.entry_op, args.entry_type, args.exit_value_set, args.exit_value, args.exit_op, args.exit_type, args.exit_comb, args.exit_time_sec, args.exit_time_msec, args.exit_event, args.average_factor, args.maxrun_sec, args.maxrun_msec)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('InterfaceStatisticsEvent_registerIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_InterfaceMtuEvent_registerIDL(self, seqid, iprot, oprot):
        args = InterfaceMtuEvent_registerIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = InterfaceMtuEvent_registerIDL_result()
        try:
            result.success = self._handler.InterfaceMtuEvent_registerIDL(args.sessionHandle, args.xosHandle, args.interfaceType)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('InterfaceMtuEvent_registerIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_InterfaceSpeedEvent_registerIDL(self, seqid, iprot, oprot):
        args = InterfaceSpeedEvent_registerIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = InterfaceSpeedEvent_registerIDL_result()
        try:
            result.success = self._handler.InterfaceSpeedEvent_registerIDL(args.sessionHandle, args.xosHandle, args.interfaceType)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('InterfaceSpeedEvent_registerIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_InterfaceDuplexModeEvent_registerIDL(self, seqid, iprot, oprot):
        args = InterfaceDuplexModeEvent_registerIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = InterfaceDuplexModeEvent_registerIDL_result()
        try:
            result.success = self._handler.InterfaceDuplexModeEvent_registerIDL(args.sessionHandle, args.xosHandle, args.interfaceType)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('InterfaceDuplexModeEvent_registerIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_InterfaceAutoNegotiateEvent_registerIDL(self, seqid, iprot, oprot):
        args = InterfaceAutoNegotiateEvent_registerIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = InterfaceAutoNegotiateEvent_registerIDL_result()
        try:
            result.success = self._handler.InterfaceAutoNegotiateEvent_registerIDL(args.sessionHandle, args.xosHandle, args.interfaceType)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('InterfaceAutoNegotiateEvent_registerIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_InterfaceFlowcontrolEvent_registerIDL(self, seqid, iprot, oprot):
        args = InterfaceFlowcontrolEvent_registerIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = InterfaceFlowcontrolEvent_registerIDL_result()
        try:
            result.success = self._handler.InterfaceFlowcontrolEvent_registerIDL(args.sessionHandle, args.xosHandle, args.interfaceType)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('InterfaceFlowcontrolEvent_registerIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_InterfaceLayer2ModeEvent_registerIDL(self, seqid, iprot, oprot):
        args = InterfaceLayer2ModeEvent_registerIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = InterfaceLayer2ModeEvent_registerIDL_result()
        try:
            result.success = self._handler.InterfaceLayer2ModeEvent_registerIDL(args.sessionHandle, args.xosHandle, args.interfaceType)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('InterfaceLayer2ModeEvent_registerIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_InterfaceForwardClassIDEvent_registerIDL(self, seqid, iprot, oprot):
        args = InterfaceForwardClassIDEvent_registerIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = InterfaceForwardClassIDEvent_registerIDL_result()
        try:
            result.success = self._handler.InterfaceForwardClassIDEvent_registerIDL(args.sessionHandle, args.xosHandle, args.interfaceType)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('InterfaceForwardClassIDEvent_registerIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_InterfaceBandwidthEvent_registerIDL(self, seqid, iprot, oprot):
        args = InterfaceBandwidthEvent_registerIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = InterfaceBandwidthEvent_registerIDL_result()
        try:
            result.success = self._handler.InterfaceBandwidthEvent_registerIDL(args.sessionHandle, args.xosHandle, args.interfaceType)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('InterfaceBandwidthEvent_registerIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_InterfaceVrfEvent_registerIDL(self, seqid, iprot, oprot):
        args = InterfaceVrfEvent_registerIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = InterfaceVrfEvent_registerIDL_result()
        try:
            result.success = self._handler.InterfaceVrfEvent_registerIDL(args.sessionHandle, args.xosHandle, args.interfaceType, args.vrfname)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('InterfaceVrfEvent_registerIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_InterfaceVlanEvent_registerIDL(self, seqid, iprot, oprot):
        args = InterfaceVlanEvent_registerIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = InterfaceVlanEvent_registerIDL_result()
        try:
            result.success = self._handler.InterfaceVlanEvent_registerIDL(args.sessionHandle, args.xosHandle, args.interfaceType, args.vlanEvtType)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('InterfaceVlanEvent_registerIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_NetworkInterface_getVrfIDL(self, seqid, iprot, oprot):
        args = NetworkInterface_getVrfIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = NetworkInterface_getVrfIDL_result()
        try:
            result.success = self._handler.NetworkInterface_getVrfIDL(args.xosHandle)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('NetworkInterface_getVrfIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_NetworkInterface_getVlanIDL(self, seqid, iprot, oprot):
        args = NetworkInterface_getVlanIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = NetworkInterface_getVlanIDL_result()
        try:
            result.success = self._handler.NetworkInterface_getVlanIDL(args.xosHandle)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('NetworkInterface_getVlanIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_NetworkInterface_createConfigIDL(self, seqid, iprot, oprot):
        args = NetworkInterface_createConfigIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = NetworkInterface_createConfigIDL_result()
        try:
            result.success = self._handler.NetworkInterface_createConfigIDL(args.sessionHandle, args.type, args.index, args.parentHandle, args.add)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('NetworkInterface_createConfigIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_NetworkInterface_getBDInstanceIDL(self, seqid, iprot, oprot):
        args = NetworkInterface_getBDInstanceIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = NetworkInterface_getBDInstanceIDL_result()
        try:
            result.success = self._handler.NetworkInterface_getBDInstanceIDL(args.xosHandle)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('NetworkInterface_getBDInstanceIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_PChannel_getMembersIDL(self, seqid, iprot, oprot):
        args = PChannel_getMembersIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = PChannel_getMembersIDL_result()
        try:
            result.success = self._handler.PChannel_getMembersIDL(args.sessionHandle, args.xosHandle)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('PChannel_getMembersIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_PChannel_getMemberModeIDL(self, seqid, iprot, oprot):
        args = PChannel_getMemberModeIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = PChannel_getMemberModeIDL_result()
        try:
            result.success = self._handler.PChannel_getMemberModeIDL(args.sessionHandle, args.xosHandle)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('PChannel_getMemberModeIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_PChannel_getMemberPriorityIDL(self, seqid, iprot, oprot):
        args = PChannel_getMemberPriorityIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = PChannel_getMemberPriorityIDL_result()
        try:
            result.success = self._handler.PChannel_getMemberPriorityIDL(args.sessionHandle, args.xosHandle)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('PChannel_getMemberPriorityIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_NetworkInterface_getPChannelIDL(self, seqid, iprot, oprot):
        args = NetworkInterface_getPChannelIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = NetworkInterface_getPChannelIDL_result()
        try:
            result.success = self._handler.NetworkInterface_getPChannelIDL(args.sessionHandle, args.xosHandle)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('NetworkInterface_getPChannelIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_NetworkInterface_getIifIdIDL(self, seqid, iprot, oprot):
        args = NetworkInterface_getIifIdIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = NetworkInterface_getIifIdIDL_result()
        try:
            result.success = self._handler.NetworkInterface_getIifIdIDL(args.xosHandle)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('NetworkInterface_getIifIdIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()




class NetworkElement_getInterfaceListIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - xoshandle
     - ifType
     - tag
     - slot
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionHandle',
      None,
      None),
     (2,
      TType.I64,
      'xoshandle',
      None,
      None),
     (3,
      TType.I32,
      'ifType',
      None,
      None),
     (4,
      TType.I32,
      'tag',
      None,
      None),
     (5,
      TType.I32,
      'slot',
      None,
      None))

    def __init__(self, sessionHandle = None, xoshandle = None, ifType = None, tag = None, slot = None):
        self.sessionHandle = sessionHandle
        self.xoshandle = xoshandle
        self.ifType = ifType
        self.tag = tag
        self.slot = slot



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
                if ftype == TType.I64:
                    self.xoshandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.ifType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.tag = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.slot = iprot.readI32()
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
        oprot.writeStructBegin('NetworkElement_getInterfaceListIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.xoshandle != None:
            oprot.writeFieldBegin('xoshandle', TType.I64, 2)
            oprot.writeI64(self.xoshandle)
            oprot.writeFieldEnd()
        if self.ifType != None:
            oprot.writeFieldBegin('ifType', TType.I32, 3)
            oprot.writeI32(self.ifType)
            oprot.writeFieldEnd()
        if self.tag != None:
            oprot.writeFieldBegin('tag', TType.I32, 4)
            oprot.writeI32(self.tag)
            oprot.writeFieldEnd()
        if self.slot != None:
            oprot.writeFieldBegin('slot', TType.I32, 5)
            oprot.writeI32(self.slot)
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




class NetworkElement_getInterfaceListIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.LIST,
      'success',
      (TType.STRUCT, (Shared.ttypes.NetworkInterfaceIDL, Shared.ttypes.NetworkInterfaceIDL.thrift_spec)),
      None), (1,
      TType.STRUCT,
      'e',
      (Shared.ttypes.ExceptionIDL, Shared.ttypes.ExceptionIDL.thrift_spec),
      None))

    def __init__(self, success = None, e = None):
        self.success = success
        self.e = e



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.LIST:
                    self.success = []
                    (_etype17, _size14,) = iprot.readListBegin()
                    for _i18 in xrange(_size14):
                        _elem19 = Shared.ttypes.NetworkInterfaceIDL()
                        _elem19.read(iprot)
                        self.success.append(_elem19)

                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = Shared.ttypes.ExceptionIDL()
                    self.e.read(iprot)
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
        oprot.writeStructBegin('NetworkElement_getInterfaceListIDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.STRUCT, len(self.success))
            for iter20 in self.success:
                iter20.write(oprot)

            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.e != None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
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




class NetworkElement_getInterfaceByNameIDL_args(object):
    """
    Attributes:
     - ifname
    """

    thrift_spec = (None, (1,
      TType.STRING,
      'ifname',
      None,
      None))

    def __init__(self, ifname = None):
        self.ifname = ifname



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
                if ftype == TType.STRING:
                    self.ifname = iprot.readString()
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
        oprot.writeStructBegin('NetworkElement_getInterfaceByNameIDL_args')
        if self.ifname != None:
            oprot.writeFieldBegin('ifname', TType.STRING, 1)
            oprot.writeString(self.ifname)
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




class NetworkElement_getInterfaceByNameIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.STRUCT,
      'success',
      (Shared.ttypes.NetworkInterfaceIDL, Shared.ttypes.NetworkInterfaceIDL.thrift_spec),
      None), (1,
      TType.STRUCT,
      'e',
      (Shared.ttypes.ExceptionIDL, Shared.ttypes.ExceptionIDL.thrift_spec),
      None))

    def __init__(self, success = None, e = None):
        self.success = success
        self.e = e



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = Shared.ttypes.NetworkInterfaceIDL()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = Shared.ttypes.ExceptionIDL()
                    self.e.read(iprot)
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
        oprot.writeStructBegin('NetworkElement_getInterfaceByNameIDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e != None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
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




class NetworkElement_getInterfaceByIifIdIDL_args(object):
    """
    Attributes:
     - iif_id
    """

    thrift_spec = (None, (1,
      TType.I64,
      'iif_id',
      None,
      None))

    def __init__(self, iif_id = None):
        self.iif_id = iif_id



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
                if ftype == TType.I64:
                    self.iif_id = iprot.readI64()
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
        oprot.writeStructBegin('NetworkElement_getInterfaceByIifIdIDL_args')
        if self.iif_id != None:
            oprot.writeFieldBegin('iif_id', TType.I64, 1)
            oprot.writeI64(self.iif_id)
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




class NetworkElement_getInterfaceByIifIdIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.STRUCT,
      'success',
      (Shared.ttypes.NetworkInterfaceIDL, Shared.ttypes.NetworkInterfaceIDL.thrift_spec),
      None), (1,
      TType.STRUCT,
      'e',
      (Shared.ttypes.ExceptionIDL, Shared.ttypes.ExceptionIDL.thrift_spec),
      None))

    def __init__(self, success = None, e = None):
        self.success = success
        self.e = e



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = Shared.ttypes.NetworkInterfaceIDL()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = Shared.ttypes.ExceptionIDL()
                    self.e.read(iprot)
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
        oprot.writeStructBegin('NetworkElement_getInterfaceByIifIdIDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e != None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
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




class NetworkElement_getInterfaceByIdIDL_args(object):
    """
    Attributes:
     - if_id
    """

    thrift_spec = (None, (1,
      TType.I64,
      'if_id',
      None,
      None))

    def __init__(self, if_id = None):
        self.if_id = if_id



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
                if ftype == TType.I64:
                    self.if_id = iprot.readI64()
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
        oprot.writeStructBegin('NetworkElement_getInterfaceByIdIDL_args')
        if self.if_id != None:
            oprot.writeFieldBegin('if_id', TType.I64, 1)
            oprot.writeI64(self.if_id)
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




class NetworkElement_getInterfaceByIdIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.STRUCT,
      'success',
      (Shared.ttypes.NetworkInterfaceIDL, Shared.ttypes.NetworkInterfaceIDL.thrift_spec),
      None), (1,
      TType.STRUCT,
      'e',
      (Shared.ttypes.ExceptionIDL, Shared.ttypes.ExceptionIDL.thrift_spec),
      None))

    def __init__(self, success = None, e = None):
        self.success = success
        self.e = e



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = Shared.ttypes.NetworkInterfaceIDL()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = Shared.ttypes.ExceptionIDL()
                    self.e.read(iprot)
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
        oprot.writeStructBegin('NetworkElement_getInterfaceByIdIDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e != None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
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




class NetworkInterface_getPropertyIDL_args(object):
    """
    Attributes:
     - xosHandle
    """

    thrift_spec = (None, (1,
      TType.I64,
      'xosHandle',
      None,
      None))

    def __init__(self, xosHandle = None):
        self.xosHandle = xosHandle



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
                if ftype == TType.I64:
                    self.xosHandle = iprot.readI64()
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
        oprot.writeStructBegin('NetworkInterface_getPropertyIDL_args')
        if self.xosHandle != None:
            oprot.writeFieldBegin('xosHandle', TType.I64, 1)
            oprot.writeI64(self.xosHandle)
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




class NetworkInterface_getPropertyIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.STRUCT,
      'success',
      (InterfacePropertyIDL, InterfacePropertyIDL.thrift_spec),
      None), (1,
      TType.STRUCT,
      'e',
      (Shared.ttypes.ExceptionIDL, Shared.ttypes.ExceptionIDL.thrift_spec),
      None))

    def __init__(self, success = None, e = None):
        self.success = success
        self.e = e



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = InterfacePropertyIDL()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = Shared.ttypes.ExceptionIDL()
                    self.e.read(iprot)
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
        oprot.writeStructBegin('NetworkInterface_getPropertyIDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e != None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
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




class NetworkInterface_issubInterfaceIDL_args(object):
    """
    Attributes:
     - xosHandle
    """

    thrift_spec = (None, (1,
      TType.I64,
      'xosHandle',
      None,
      None))

    def __init__(self, xosHandle = None):
        self.xosHandle = xosHandle



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
                if ftype == TType.I64:
                    self.xosHandle = iprot.readI64()
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
        oprot.writeStructBegin('NetworkInterface_issubInterfaceIDL_args')
        if self.xosHandle != None:
            oprot.writeFieldBegin('xosHandle', TType.I64, 1)
            oprot.writeI64(self.xosHandle)
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




class NetworkInterface_issubInterfaceIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.STRUCT,
      'success',
      (IssubInterfaceIDL, IssubInterfaceIDL.thrift_spec),
      None), (1,
      TType.STRUCT,
      'e',
      (Shared.ttypes.ExceptionIDL, Shared.ttypes.ExceptionIDL.thrift_spec),
      None))

    def __init__(self, success = None, e = None):
        self.success = success
        self.e = e



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = IssubInterfaceIDL()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = Shared.ttypes.ExceptionIDL()
                    self.e.read(iprot)
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
        oprot.writeStructBegin('NetworkInterface_issubInterfaceIDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e != None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
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




class NetworkInterface_getConfigIDL_args(object):
    """
    Attributes:
     - xosHandle
    """

    thrift_spec = (None, (1,
      TType.I64,
      'xosHandle',
      None,
      None))

    def __init__(self, xosHandle = None):
        self.xosHandle = xosHandle



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
                if ftype == TType.I64:
                    self.xosHandle = iprot.readI64()
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
        oprot.writeStructBegin('NetworkInterface_getConfigIDL_args')
        if self.xosHandle != None:
            oprot.writeFieldBegin('xosHandle', TType.I64, 1)
            oprot.writeI64(self.xosHandle)
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




class NetworkInterface_getConfigIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.STRUCT,
      'success',
      (InterfaceConfigIDL, InterfaceConfigIDL.thrift_spec),
      None), (1,
      TType.STRUCT,
      'e',
      (Shared.ttypes.ExceptionIDL, Shared.ttypes.ExceptionIDL.thrift_spec),
      None))

    def __init__(self, success = None, e = None):
        self.success = success
        self.e = e



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = InterfaceConfigIDL()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = Shared.ttypes.ExceptionIDL()
                    self.e.read(iprot)
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
        oprot.writeStructBegin('NetworkInterface_getConfigIDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e != None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
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




class NetworkInterface_getStatusIDL_args(object):
    """
    Attributes:
     - xosHandle
    """

    thrift_spec = (None, (1,
      TType.I64,
      'xosHandle',
      None,
      None))

    def __init__(self, xosHandle = None):
        self.xosHandle = xosHandle



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
                if ftype == TType.I64:
                    self.xosHandle = iprot.readI64()
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
        oprot.writeStructBegin('NetworkInterface_getStatusIDL_args')
        if self.xosHandle != None:
            oprot.writeFieldBegin('xosHandle', TType.I64, 1)
            oprot.writeI64(self.xosHandle)
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




class NetworkInterface_getStatusIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.STRUCT,
      'success',
      (InterfaceStatusIDL, InterfaceStatusIDL.thrift_spec),
      None), (1,
      TType.STRUCT,
      'e',
      (Shared.ttypes.ExceptionIDL, Shared.ttypes.ExceptionIDL.thrift_spec),
      None))

    def __init__(self, success = None, e = None):
        self.success = success
        self.e = e



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = InterfaceStatusIDL()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = Shared.ttypes.ExceptionIDL()
                    self.e.read(iprot)
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
        oprot.writeStructBegin('NetworkInterface_getStatusIDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e != None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
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




class NetworkInterface_getStatisticsIDL_args(object):
    """
    Attributes:
     - xosHandle
    """

    thrift_spec = (None, (1,
      TType.I64,
      'xosHandle',
      None,
      None))

    def __init__(self, xosHandle = None):
        self.xosHandle = xosHandle



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
                if ftype == TType.I64:
                    self.xosHandle = iprot.readI64()
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
        oprot.writeStructBegin('NetworkInterface_getStatisticsIDL_args')
        if self.xosHandle != None:
            oprot.writeFieldBegin('xosHandle', TType.I64, 1)
            oprot.writeI64(self.xosHandle)
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




class NetworkInterface_getStatisticsIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.LIST,
      'success',
      (TType.STRUCT, (InterfaceStatisticsIDL, InterfaceStatisticsIDL.thrift_spec)),
      None), (1,
      TType.STRUCT,
      'e',
      (Shared.ttypes.ExceptionIDL, Shared.ttypes.ExceptionIDL.thrift_spec),
      None))

    def __init__(self, success = None, e = None):
        self.success = success
        self.e = e



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.LIST:
                    self.success = []
                    (_etype24, _size21,) = iprot.readListBegin()
                    for _i25 in xrange(_size21):
                        _elem26 = InterfaceStatisticsIDL()
                        _elem26.read(iprot)
                        self.success.append(_elem26)

                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = Shared.ttypes.ExceptionIDL()
                    self.e.read(iprot)
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
        oprot.writeStructBegin('NetworkInterface_getStatisticsIDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.STRUCT, len(self.success))
            for iter27 in self.success:
                iter27.write(oprot)

            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.e != None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
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




class NetworkInterface_getParentIDL_args(object):
    """
    Attributes:
     - xosHandle
    """

    thrift_spec = (None, (1,
      TType.I64,
      'xosHandle',
      None,
      None))

    def __init__(self, xosHandle = None):
        self.xosHandle = xosHandle



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
                if ftype == TType.I64:
                    self.xosHandle = iprot.readI64()
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
        oprot.writeStructBegin('NetworkInterface_getParentIDL_args')
        if self.xosHandle != None:
            oprot.writeFieldBegin('xosHandle', TType.I64, 1)
            oprot.writeI64(self.xosHandle)
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




class NetworkInterface_getParentIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.STRUCT,
      'success',
      (Shared.ttypes.NetworkInterfaceIDL, Shared.ttypes.NetworkInterfaceIDL.thrift_spec),
      None), (1,
      TType.STRUCT,
      'e',
      (Shared.ttypes.ExceptionIDL, Shared.ttypes.ExceptionIDL.thrift_spec),
      None))

    def __init__(self, success = None, e = None):
        self.success = success
        self.e = e



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = Shared.ttypes.NetworkInterfaceIDL()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = Shared.ttypes.ExceptionIDL()
                    self.e.read(iprot)
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
        oprot.writeStructBegin('NetworkInterface_getParentIDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e != None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
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




class NetworkInterface_getSubInterfaceIDL_args(object):
    """
    Attributes:
     - xosHandle
    """

    thrift_spec = (None, (1,
      TType.I64,
      'xosHandle',
      None,
      None))

    def __init__(self, xosHandle = None):
        self.xosHandle = xosHandle



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
                if ftype == TType.I64:
                    self.xosHandle = iprot.readI64()
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
        oprot.writeStructBegin('NetworkInterface_getSubInterfaceIDL_args')
        if self.xosHandle != None:
            oprot.writeFieldBegin('xosHandle', TType.I64, 1)
            oprot.writeI64(self.xosHandle)
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




class NetworkInterface_getSubInterfaceIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.LIST,
      'success',
      (TType.STRUCT, (Shared.ttypes.NetworkInterfaceIDL, Shared.ttypes.NetworkInterfaceIDL.thrift_spec)),
      None), (1,
      TType.STRUCT,
      'e',
      (Shared.ttypes.ExceptionIDL, Shared.ttypes.ExceptionIDL.thrift_spec),
      None))

    def __init__(self, success = None, e = None):
        self.success = success
        self.e = e



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.LIST:
                    self.success = []
                    (_etype31, _size28,) = iprot.readListBegin()
                    for _i32 in xrange(_size28):
                        _elem33 = Shared.ttypes.NetworkInterfaceIDL()
                        _elem33.read(iprot)
                        self.success.append(_elem33)

                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = Shared.ttypes.ExceptionIDL()
                    self.e.read(iprot)
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
        oprot.writeStructBegin('NetworkInterface_getSubInterfaceIDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.STRUCT, len(self.success))
            for iter34 in self.success:
                iter34.write(oprot)

            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.e != None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
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




class NetworkInterface_getAddressListIDL_args(object):
    """
    Attributes:
     - xoshandle
    """

    thrift_spec = (None, (1,
      TType.I64,
      'xoshandle',
      None,
      None))

    def __init__(self, xoshandle = None):
        self.xoshandle = xoshandle



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
                if ftype == TType.I64:
                    self.xoshandle = iprot.readI64()
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
        oprot.writeStructBegin('NetworkInterface_getAddressListIDL_args')
        if self.xoshandle != None:
            oprot.writeFieldBegin('xoshandle', TType.I64, 1)
            oprot.writeI64(self.xoshandle)
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




class NetworkInterface_getAddressListIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.LIST,
      'success',
      (TType.STRUCT, (Shared.ttypes.NetworkAddressIDL, Shared.ttypes.NetworkAddressIDL.thrift_spec)),
      None), (1,
      TType.STRUCT,
      'e',
      (Shared.ttypes.ExceptionIDL, Shared.ttypes.ExceptionIDL.thrift_spec),
      None))

    def __init__(self, success = None, e = None):
        self.success = success
        self.e = e



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.LIST:
                    self.success = []
                    (_etype38, _size35,) = iprot.readListBegin()
                    for _i39 in xrange(_size35):
                        _elem40 = Shared.ttypes.NetworkAddressIDL()
                        _elem40.read(iprot)
                        self.success.append(_elem40)

                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = Shared.ttypes.ExceptionIDL()
                    self.e.read(iprot)
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
        oprot.writeStructBegin('NetworkInterface_getAddressListIDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.STRUCT, len(self.success))
            for iter41 in self.success:
                iter41.write(oprot)

            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.e != None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
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




class NetworkInterface_getPrefixListIDL_args(object):
    """
    Attributes:
     - xoshandle
    """

    thrift_spec = (None, (1,
      TType.I64,
      'xoshandle',
      None,
      None))

    def __init__(self, xoshandle = None):
        self.xoshandle = xoshandle



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
                if ftype == TType.I64:
                    self.xoshandle = iprot.readI64()
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
        oprot.writeStructBegin('NetworkInterface_getPrefixListIDL_args')
        if self.xoshandle != None:
            oprot.writeFieldBegin('xoshandle', TType.I64, 1)
            oprot.writeI64(self.xoshandle)
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




class NetworkInterface_getPrefixListIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.LIST,
      'success',
      (TType.STRUCT, (Shared.ttypes.NetworkPrefixIDL, Shared.ttypes.NetworkPrefixIDL.thrift_spec)),
      None), (1,
      TType.STRUCT,
      'e',
      (Shared.ttypes.ExceptionIDL, Shared.ttypes.ExceptionIDL.thrift_spec),
      None))

    def __init__(self, success = None, e = None):
        self.success = success
        self.e = e



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.LIST:
                    self.success = []
                    (_etype45, _size42,) = iprot.readListBegin()
                    for _i46 in xrange(_size42):
                        _elem47 = Shared.ttypes.NetworkPrefixIDL()
                        _elem47.read(iprot)
                        self.success.append(_elem47)

                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = Shared.ttypes.ExceptionIDL()
                    self.e.read(iprot)
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
        oprot.writeStructBegin('NetworkInterface_getPrefixListIDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.STRUCT, len(self.success))
            for iter48 in self.success:
                iter48.write(oprot)

            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.e != None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
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




class NetworkInterface_setInterfaceShutdownIDL_args(object):
    """
    Attributes:
     - xosHandle
     - shutdown
    """

    thrift_spec = (None, (1,
      TType.I64,
      'xosHandle',
      None,
      None), (2,
      TType.I32,
      'shutdown',
      None,
      None))

    def __init__(self, xosHandle = None, shutdown = None):
        self.xosHandle = xosHandle
        self.shutdown = shutdown



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
                if ftype == TType.I64:
                    self.xosHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.shutdown = iprot.readI32()
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
        oprot.writeStructBegin('NetworkInterface_setInterfaceShutdownIDL_args')
        if self.xosHandle != None:
            oprot.writeFieldBegin('xosHandle', TType.I64, 1)
            oprot.writeI64(self.xosHandle)
            oprot.writeFieldEnd()
        if self.shutdown != None:
            oprot.writeFieldBegin('shutdown', TType.I32, 2)
            oprot.writeI32(self.shutdown)
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




class NetworkInterface_setInterfaceShutdownIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.I32,
      'success',
      None,
      None), (1,
      TType.STRUCT,
      'e',
      (Shared.ttypes.ExceptionIDL, Shared.ttypes.ExceptionIDL.thrift_spec),
      None))

    def __init__(self, success = None, e = None):
        self.success = success
        self.e = e



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.I32:
                    self.success = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = Shared.ttypes.ExceptionIDL()
                    self.e.read(iprot)
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
        oprot.writeStructBegin('NetworkInterface_setInterfaceShutdownIDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.I32, 0)
            oprot.writeI32(self.success)
            oprot.writeFieldEnd()
        if self.e != None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
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




class NetworkInterface_clearStatisticsIDL_args(object):
    """
    Attributes:
     - xosHandle
    """

    thrift_spec = (None, (1,
      TType.I64,
      'xosHandle',
      None,
      None))

    def __init__(self, xosHandle = None):
        self.xosHandle = xosHandle



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
                if ftype == TType.I64:
                    self.xosHandle = iprot.readI64()
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
        oprot.writeStructBegin('NetworkInterface_clearStatisticsIDL_args')
        if self.xosHandle != None:
            oprot.writeFieldBegin('xosHandle', TType.I64, 1)
            oprot.writeI64(self.xosHandle)
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




class NetworkInterface_clearStatisticsIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.I32,
      'success',
      None,
      None), (1,
      TType.STRUCT,
      'e',
      (Shared.ttypes.ExceptionIDL, Shared.ttypes.ExceptionIDL.thrift_spec),
      None))

    def __init__(self, success = None, e = None):
        self.success = success
        self.e = e



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.I32:
                    self.success = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = Shared.ttypes.ExceptionIDL()
                    self.e.read(iprot)
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
        oprot.writeStructBegin('NetworkInterface_clearStatisticsIDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.I32, 0)
            oprot.writeI32(self.success)
            oprot.writeFieldEnd()
        if self.e != None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
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




class NetworkInterface_setDescriptionIDL_args(object):
    """
    Attributes:
     - xosHandle
     - description
    """

    thrift_spec = (None, (1,
      TType.I64,
      'xosHandle',
      None,
      None), (2,
      TType.STRING,
      'description',
      None,
      None))

    def __init__(self, xosHandle = None, description = None):
        self.xosHandle = xosHandle
        self.description = description



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
                if ftype == TType.I64:
                    self.xosHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.description = iprot.readString()
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
        oprot.writeStructBegin('NetworkInterface_setDescriptionIDL_args')
        if self.xosHandle != None:
            oprot.writeFieldBegin('xosHandle', TType.I64, 1)
            oprot.writeI64(self.xosHandle)
            oprot.writeFieldEnd()
        if self.description != None:
            oprot.writeFieldBegin('description', TType.STRING, 2)
            oprot.writeString(self.description)
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




class NetworkInterface_setDescriptionIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.I32,
      'success',
      None,
      None), (1,
      TType.STRUCT,
      'e',
      (Shared.ttypes.ExceptionIDL, Shared.ttypes.ExceptionIDL.thrift_spec),
      None))

    def __init__(self, success = None, e = None):
        self.success = success
        self.e = e



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.I32:
                    self.success = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = Shared.ttypes.ExceptionIDL()
                    self.e.read(iprot)
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
        oprot.writeStructBegin('NetworkInterface_setDescriptionIDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.I32, 0)
            oprot.writeI32(self.success)
            oprot.writeFieldEnd()
        if self.e != None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
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




class NetworkInterface_setIpHelperIDL_args(object):
    """
    Attributes:
     - xosHandle
     - addr
     - vrf
     - setUnset
    """

    thrift_spec = (None,
     (1,
      TType.I64,
      'xosHandle',
      None,
      None),
     (2,
      TType.STRUCT,
      'addr',
      (Shared.ttypes.NetworkAddressIDL, Shared.ttypes.NetworkAddressIDL.thrift_spec),
      None),
     (3,
      TType.STRING,
      'vrf',
      None,
      None),
     (4,
      TType.I32,
      'setUnset',
      None,
      None))

    def __init__(self, xosHandle = None, addr = None, vrf = None, setUnset = None):
        self.xosHandle = xosHandle
        self.addr = addr
        self.vrf = vrf
        self.setUnset = setUnset



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
                if ftype == TType.I64:
                    self.xosHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.addr = Shared.ttypes.NetworkAddressIDL()
                    self.addr.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.vrf = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.setUnset = iprot.readI32()
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
        oprot.writeStructBegin('NetworkInterface_setIpHelperIDL_args')
        if self.xosHandle != None:
            oprot.writeFieldBegin('xosHandle', TType.I64, 1)
            oprot.writeI64(self.xosHandle)
            oprot.writeFieldEnd()
        if self.addr != None:
            oprot.writeFieldBegin('addr', TType.STRUCT, 2)
            self.addr.write(oprot)
            oprot.writeFieldEnd()
        if self.vrf != None:
            oprot.writeFieldBegin('vrf', TType.STRING, 3)
            oprot.writeString(self.vrf)
            oprot.writeFieldEnd()
        if self.setUnset != None:
            oprot.writeFieldBegin('setUnset', TType.I32, 4)
            oprot.writeI32(self.setUnset)
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




class NetworkInterface_setIpHelperIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.I32,
      'success',
      None,
      None), (1,
      TType.STRUCT,
      'e',
      (Shared.ttypes.ExceptionIDL, Shared.ttypes.ExceptionIDL.thrift_spec),
      None))

    def __init__(self, success = None, e = None):
        self.success = success
        self.e = e



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.I32:
                    self.success = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = Shared.ttypes.ExceptionIDL()
                    self.e.read(iprot)
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
        oprot.writeStructBegin('NetworkInterface_setIpHelperIDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.I32, 0)
            oprot.writeI32(self.success)
            oprot.writeFieldEnd()
        if self.e != None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
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




class NetworkInterface_setIpProxyArpIDL_args(object):
    """
    Attributes:
     - xosHandle
     - setUnset
    """

    thrift_spec = (None, (1,
      TType.I64,
      'xosHandle',
      None,
      None), (2,
      TType.I32,
      'setUnset',
      None,
      None))

    def __init__(self, xosHandle = None, setUnset = None):
        self.xosHandle = xosHandle
        self.setUnset = setUnset



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
                if ftype == TType.I64:
                    self.xosHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.setUnset = iprot.readI32()
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
        oprot.writeStructBegin('NetworkInterface_setIpProxyArpIDL_args')
        if self.xosHandle != None:
            oprot.writeFieldBegin('xosHandle', TType.I64, 1)
            oprot.writeI64(self.xosHandle)
            oprot.writeFieldEnd()
        if self.setUnset != None:
            oprot.writeFieldBegin('setUnset', TType.I32, 2)
            oprot.writeI32(self.setUnset)
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




class NetworkInterface_setIpProxyArpIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.I32,
      'success',
      None,
      None), (1,
      TType.STRUCT,
      'e',
      (Shared.ttypes.ExceptionIDL, Shared.ttypes.ExceptionIDL.thrift_spec),
      None))

    def __init__(self, success = None, e = None):
        self.success = success
        self.e = e



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.I32:
                    self.success = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = Shared.ttypes.ExceptionIDL()
                    self.e.read(iprot)
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
        oprot.writeStructBegin('NetworkInterface_setIpProxyArpIDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.I32, 0)
            oprot.writeI32(self.success)
            oprot.writeFieldEnd()
        if self.e != None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
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




class NetworkInterface_setIpUnreachableIDL_args(object):
    """
    Attributes:
     - xosHandle
     - setUnset
    """

    thrift_spec = (None, (1,
      TType.I64,
      'xosHandle',
      None,
      None), (2,
      TType.I32,
      'setUnset',
      None,
      None))

    def __init__(self, xosHandle = None, setUnset = None):
        self.xosHandle = xosHandle
        self.setUnset = setUnset



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
                if ftype == TType.I64:
                    self.xosHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.setUnset = iprot.readI32()
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
        oprot.writeStructBegin('NetworkInterface_setIpUnreachableIDL_args')
        if self.xosHandle != None:
            oprot.writeFieldBegin('xosHandle', TType.I64, 1)
            oprot.writeI64(self.xosHandle)
            oprot.writeFieldEnd()
        if self.setUnset != None:
            oprot.writeFieldBegin('setUnset', TType.I32, 2)
            oprot.writeI32(self.setUnset)
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




class NetworkInterface_setIpUnreachableIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.I32,
      'success',
      None,
      None), (1,
      TType.STRUCT,
      'e',
      (Shared.ttypes.ExceptionIDL, Shared.ttypes.ExceptionIDL.thrift_spec),
      None))

    def __init__(self, success = None, e = None):
        self.success = success
        self.e = e



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.I32:
                    self.success = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = Shared.ttypes.ExceptionIDL()
                    self.e.read(iprot)
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
        oprot.writeStructBegin('NetworkInterface_setIpUnreachableIDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.I32, 0)
            oprot.writeI32(self.success)
            oprot.writeFieldEnd()
        if self.e != None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
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




class NetworkInterface_setIpRedirectIDL_args(object):
    """
    Attributes:
     - xosHandle
     - setUnset
    """

    thrift_spec = (None, (1,
      TType.I64,
      'xosHandle',
      None,
      None), (2,
      TType.I32,
      'setUnset',
      None,
      None))

    def __init__(self, xosHandle = None, setUnset = None):
        self.xosHandle = xosHandle
        self.setUnset = setUnset



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
                if ftype == TType.I64:
                    self.xosHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.setUnset = iprot.readI32()
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
        oprot.writeStructBegin('NetworkInterface_setIpRedirectIDL_args')
        if self.xosHandle != None:
            oprot.writeFieldBegin('xosHandle', TType.I64, 1)
            oprot.writeI64(self.xosHandle)
            oprot.writeFieldEnd()
        if self.setUnset != None:
            oprot.writeFieldBegin('setUnset', TType.I32, 2)
            oprot.writeI32(self.setUnset)
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




class NetworkInterface_setIpRedirectIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.I32,
      'success',
      None,
      None), (1,
      TType.STRUCT,
      'e',
      (Shared.ttypes.ExceptionIDL, Shared.ttypes.ExceptionIDL.thrift_spec),
      None))

    def __init__(self, success = None, e = None):
        self.success = success
        self.e = e



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.I32:
                    self.success = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = Shared.ttypes.ExceptionIDL()
                    self.e.read(iprot)
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
        oprot.writeStructBegin('NetworkInterface_setIpRedirectIDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.I32, 0)
            oprot.writeI32(self.success)
            oprot.writeFieldEnd()
        if self.e != None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
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




class NetworkInterface_setIpUnicastReversePathIDL_args(object):
    """
    Attributes:
     - xosHandle
     - ipAccessList
     - setUnset
    """

    thrift_spec = (None,
     (1,
      TType.I64,
      'xosHandle',
      None,
      None),
     (2,
      TType.STRING,
      'ipAccessList',
      None,
      None),
     (3,
      TType.I32,
      'setUnset',
      None,
      None))

    def __init__(self, xosHandle = None, ipAccessList = None, setUnset = None):
        self.xosHandle = xosHandle
        self.ipAccessList = ipAccessList
        self.setUnset = setUnset



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
                if ftype == TType.I64:
                    self.xosHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.ipAccessList = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.setUnset = iprot.readI32()
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
        oprot.writeStructBegin('NetworkInterface_setIpUnicastReversePathIDL_args')
        if self.xosHandle != None:
            oprot.writeFieldBegin('xosHandle', TType.I64, 1)
            oprot.writeI64(self.xosHandle)
            oprot.writeFieldEnd()
        if self.ipAccessList != None:
            oprot.writeFieldBegin('ipAccessList', TType.STRING, 2)
            oprot.writeString(self.ipAccessList)
            oprot.writeFieldEnd()
        if self.setUnset != None:
            oprot.writeFieldBegin('setUnset', TType.I32, 3)
            oprot.writeI32(self.setUnset)
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




class NetworkInterface_setIpUnicastReversePathIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.I32,
      'success',
      None,
      None), (1,
      TType.STRUCT,
      'e',
      (Shared.ttypes.ExceptionIDL, Shared.ttypes.ExceptionIDL.thrift_spec),
      None))

    def __init__(self, success = None, e = None):
        self.success = success
        self.e = e



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.I32:
                    self.success = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = Shared.ttypes.ExceptionIDL()
                    self.e.read(iprot)
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
        oprot.writeStructBegin('NetworkInterface_setIpUnicastReversePathIDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.I32, 0)
            oprot.writeI32(self.success)
            oprot.writeFieldEnd()
        if self.e != None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
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




class NetworkInterface_setLoadIntervalIDL_args(object):
    """
    Attributes:
     - xosHandle
     - interval
    """

    thrift_spec = (None, (1,
      TType.I64,
      'xosHandle',
      None,
      None), (2,
      TType.I32,
      'interval',
      None,
      None))

    def __init__(self, xosHandle = None, interval = None):
        self.xosHandle = xosHandle
        self.interval = interval



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
                if ftype == TType.I64:
                    self.xosHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.interval = iprot.readI32()
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
        oprot.writeStructBegin('NetworkInterface_setLoadIntervalIDL_args')
        if self.xosHandle != None:
            oprot.writeFieldBegin('xosHandle', TType.I64, 1)
            oprot.writeI64(self.xosHandle)
            oprot.writeFieldEnd()
        if self.interval != None:
            oprot.writeFieldBegin('interval', TType.I32, 2)
            oprot.writeI32(self.interval)
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




class NetworkInterface_setLoadIntervalIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.I32,
      'success',
      None,
      None), (1,
      TType.STRUCT,
      'e',
      (Shared.ttypes.ExceptionIDL, Shared.ttypes.ExceptionIDL.thrift_spec),
      None))

    def __init__(self, success = None, e = None):
        self.success = success
        self.e = e



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.I32:
                    self.success = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = Shared.ttypes.ExceptionIDL()
                    self.e.read(iprot)
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
        oprot.writeStructBegin('NetworkInterface_setLoadIntervalIDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.I32, 0)
            oprot.writeI32(self.success)
            oprot.writeFieldEnd()
        if self.e != None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
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




class NetworkInterface_setMTUIDL_args(object):
    """
    Attributes:
     - xosHandle
     - mtu
    """

    thrift_spec = (None, (1,
      TType.I64,
      'xosHandle',
      None,
      None), (2,
      TType.I32,
      'mtu',
      None,
      None))

    def __init__(self, xosHandle = None, mtu = None):
        self.xosHandle = xosHandle
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
                if ftype == TType.I64:
                    self.xosHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
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
        oprot.writeStructBegin('NetworkInterface_setMTUIDL_args')
        if self.xosHandle != None:
            oprot.writeFieldBegin('xosHandle', TType.I64, 1)
            oprot.writeI64(self.xosHandle)
            oprot.writeFieldEnd()
        if self.mtu != None:
            oprot.writeFieldBegin('mtu', TType.I32, 2)
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




class NetworkInterface_setMTUIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.I32,
      'success',
      None,
      None), (1,
      TType.STRUCT,
      'e',
      (Shared.ttypes.ExceptionIDL, Shared.ttypes.ExceptionIDL.thrift_spec),
      None))

    def __init__(self, success = None, e = None):
        self.success = success
        self.e = e



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.I32:
                    self.success = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = Shared.ttypes.ExceptionIDL()
                    self.e.read(iprot)
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
        oprot.writeStructBegin('NetworkInterface_setMTUIDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.I32, 0)
            oprot.writeI32(self.success)
            oprot.writeFieldEnd()
        if self.e != None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
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




class NetworkInterface_setFwdClassIDL_args(object):
    """
    Attributes:
     - xosHandle
     - cid
    """

    thrift_spec = (None, (1,
      TType.I64,
      'xosHandle',
      None,
      None), (2,
      TType.I32,
      'cid',
      None,
      None))

    def __init__(self, xosHandle = None, cid = None):
        self.xosHandle = xosHandle
        self.cid = cid



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
                if ftype == TType.I64:
                    self.xosHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.cid = iprot.readI32()
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
        oprot.writeStructBegin('NetworkInterface_setFwdClassIDL_args')
        if self.xosHandle != None:
            oprot.writeFieldBegin('xosHandle', TType.I64, 1)
            oprot.writeI64(self.xosHandle)
            oprot.writeFieldEnd()
        if self.cid != None:
            oprot.writeFieldBegin('cid', TType.I32, 2)
            oprot.writeI32(self.cid)
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




class NetworkInterface_setFwdClassIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.I32,
      'success',
      None,
      None), (1,
      TType.STRUCT,
      'e',
      (Shared.ttypes.ExceptionIDL, Shared.ttypes.ExceptionIDL.thrift_spec),
      None))

    def __init__(self, success = None, e = None):
        self.success = success
        self.e = e



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.I32:
                    self.success = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = Shared.ttypes.ExceptionIDL()
                    self.e.read(iprot)
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
        oprot.writeStructBegin('NetworkInterface_setFwdClassIDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.I32, 0)
            oprot.writeI32(self.success)
            oprot.writeFieldEnd()
        if self.e != None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
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




class NetworkInterface_setEncapIDL_args(object):
    """
    Attributes:
     - xosHandle
     - encap
    """

    thrift_spec = (None, (1,
      TType.I64,
      'xosHandle',
      None,
      None), (2,
      TType.I32,
      'encap',
      None,
      None))

    def __init__(self, xosHandle = None, encap = None):
        self.xosHandle = xosHandle
        self.encap = encap



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
                if ftype == TType.I64:
                    self.xosHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.encap = iprot.readI32()
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
        oprot.writeStructBegin('NetworkInterface_setEncapIDL_args')
        if self.xosHandle != None:
            oprot.writeFieldBegin('xosHandle', TType.I64, 1)
            oprot.writeI64(self.xosHandle)
            oprot.writeFieldEnd()
        if self.encap != None:
            oprot.writeFieldBegin('encap', TType.I32, 2)
            oprot.writeI32(self.encap)
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




class NetworkInterface_setEncapIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.I32,
      'success',
      None,
      None), (1,
      TType.STRUCT,
      'e',
      (Shared.ttypes.ExceptionIDL, Shared.ttypes.ExceptionIDL.thrift_spec),
      None))

    def __init__(self, success = None, e = None):
        self.success = success
        self.e = e



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.I32:
                    self.success = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = Shared.ttypes.ExceptionIDL()
                    self.e.read(iprot)
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
        oprot.writeStructBegin('NetworkInterface_setEncapIDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.I32, 0)
            oprot.writeI32(self.success)
            oprot.writeFieldEnd()
        if self.e != None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
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




class NetworkInterface_setBwIDL_args(object):
    """
    Attributes:
     - xosHandle
     - bw
    """

    thrift_spec = (None, (1,
      TType.I64,
      'xosHandle',
      None,
      None), (2,
      TType.I32,
      'bw',
      None,
      None))

    def __init__(self, xosHandle = None, bw = None):
        self.xosHandle = xosHandle
        self.bw = bw



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
                if ftype == TType.I64:
                    self.xosHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.bw = iprot.readI32()
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
        oprot.writeStructBegin('NetworkInterface_setBwIDL_args')
        if self.xosHandle != None:
            oprot.writeFieldBegin('xosHandle', TType.I64, 1)
            oprot.writeI64(self.xosHandle)
            oprot.writeFieldEnd()
        if self.bw != None:
            oprot.writeFieldBegin('bw', TType.I32, 2)
            oprot.writeI32(self.bw)
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




class NetworkInterface_setBwIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.I32,
      'success',
      None,
      None), (1,
      TType.STRUCT,
      'e',
      (Shared.ttypes.ExceptionIDL, Shared.ttypes.ExceptionIDL.thrift_spec),
      None))

    def __init__(self, success = None, e = None):
        self.success = success
        self.e = e



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.I32:
                    self.success = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = Shared.ttypes.ExceptionIDL()
                    self.e.read(iprot)
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
        oprot.writeStructBegin('NetworkInterface_setBwIDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.I32, 0)
            oprot.writeI32(self.success)
            oprot.writeFieldEnd()
        if self.e != None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
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




class NetworkInterface_setAddressIDL_args(object):
    """
    Attributes:
     - xosHandle
     - opertype
     - scope
     - addr
     - prefix_len
    """

    thrift_spec = (None,
     (1,
      TType.I64,
      'xosHandle',
      None,
      None),
     (2,
      TType.I32,
      'opertype',
      None,
      None),
     (3,
      TType.I32,
      'scope',
      None,
      None),
     (4,
      TType.STRUCT,
      'addr',
      (Shared.ttypes.NetworkAddressIDL, Shared.ttypes.NetworkAddressIDL.thrift_spec),
      None),
     (5,
      TType.I16,
      'prefix_len',
      None,
      None))

    def __init__(self, xosHandle = None, opertype = None, scope = None, addr = None, prefix_len = None):
        self.xosHandle = xosHandle
        self.opertype = opertype
        self.scope = scope
        self.addr = addr
        self.prefix_len = prefix_len



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
                if ftype == TType.I64:
                    self.xosHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.opertype = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.scope = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRUCT:
                    self.addr = Shared.ttypes.NetworkAddressIDL()
                    self.addr.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I16:
                    self.prefix_len = iprot.readI16()
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
        oprot.writeStructBegin('NetworkInterface_setAddressIDL_args')
        if self.xosHandle != None:
            oprot.writeFieldBegin('xosHandle', TType.I64, 1)
            oprot.writeI64(self.xosHandle)
            oprot.writeFieldEnd()
        if self.opertype != None:
            oprot.writeFieldBegin('opertype', TType.I32, 2)
            oprot.writeI32(self.opertype)
            oprot.writeFieldEnd()
        if self.scope != None:
            oprot.writeFieldBegin('scope', TType.I32, 3)
            oprot.writeI32(self.scope)
            oprot.writeFieldEnd()
        if self.addr != None:
            oprot.writeFieldBegin('addr', TType.STRUCT, 4)
            self.addr.write(oprot)
            oprot.writeFieldEnd()
        if self.prefix_len != None:
            oprot.writeFieldBegin('prefix_len', TType.I16, 5)
            oprot.writeI16(self.prefix_len)
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




class NetworkInterface_setAddressIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.I32,
      'success',
      None,
      None), (1,
      TType.STRUCT,
      'e',
      (Shared.ttypes.ExceptionIDL, Shared.ttypes.ExceptionIDL.thrift_spec),
      None))

    def __init__(self, success = None, e = None):
        self.success = success
        self.e = e



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.I32:
                    self.success = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = Shared.ttypes.ExceptionIDL()
                    self.e.read(iprot)
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
        oprot.writeStructBegin('NetworkInterface_setAddressIDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.I32, 0)
            oprot.writeI32(self.success)
            oprot.writeFieldEnd()
        if self.e != None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
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




class NetworkInterface_setSwitchportModeIDL_args(object):
    """
    Attributes:
     - xosHandle
     - mode
    """

    thrift_spec = (None, (1,
      TType.I64,
      'xosHandle',
      None,
      None), (2,
      TType.I32,
      'mode',
      None,
      None))

    def __init__(self, xosHandle = None, mode = None):
        self.xosHandle = xosHandle
        self.mode = mode



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
                if ftype == TType.I64:
                    self.xosHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.mode = iprot.readI32()
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
        oprot.writeStructBegin('NetworkInterface_setSwitchportModeIDL_args')
        if self.xosHandle != None:
            oprot.writeFieldBegin('xosHandle', TType.I64, 1)
            oprot.writeI64(self.xosHandle)
            oprot.writeFieldEnd()
        if self.mode != None:
            oprot.writeFieldBegin('mode', TType.I32, 2)
            oprot.writeI32(self.mode)
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




class NetworkInterface_setSwitchportModeIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.I32,
      'success',
      None,
      None), (1,
      TType.STRUCT,
      'e',
      (Shared.ttypes.ExceptionIDL, Shared.ttypes.ExceptionIDL.thrift_spec),
      None))

    def __init__(self, success = None, e = None):
        self.success = success
        self.e = e



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.I32:
                    self.success = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = Shared.ttypes.ExceptionIDL()
                    self.e.read(iprot)
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
        oprot.writeStructBegin('NetworkInterface_setSwitchportModeIDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.I32, 0)
            oprot.writeI32(self.success)
            oprot.writeFieldEnd()
        if self.e != None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
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




class NetworkInterface_setLayer2IDL_args(object):
    """
    Attributes:
     - xosHandle
     - layer2
    """

    thrift_spec = (None, (1,
      TType.I64,
      'xosHandle',
      None,
      None), (2,
      TType.I32,
      'layer2',
      None,
      None))

    def __init__(self, xosHandle = None, layer2 = None):
        self.xosHandle = xosHandle
        self.layer2 = layer2



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
                if ftype == TType.I64:
                    self.xosHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.layer2 = iprot.readI32()
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
        oprot.writeStructBegin('NetworkInterface_setLayer2IDL_args')
        if self.xosHandle != None:
            oprot.writeFieldBegin('xosHandle', TType.I64, 1)
            oprot.writeI64(self.xosHandle)
            oprot.writeFieldEnd()
        if self.layer2 != None:
            oprot.writeFieldBegin('layer2', TType.I32, 2)
            oprot.writeI32(self.layer2)
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




class NetworkInterface_setLayer2IDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.I32,
      'success',
      None,
      None), (1,
      TType.STRUCT,
      'e',
      (Shared.ttypes.ExceptionIDL, Shared.ttypes.ExceptionIDL.thrift_spec),
      None))

    def __init__(self, success = None, e = None):
        self.success = success
        self.e = e



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.I32:
                    self.success = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = Shared.ttypes.ExceptionIDL()
                    self.e.read(iprot)
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
        oprot.writeStructBegin('NetworkInterface_setLayer2IDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.I32, 0)
            oprot.writeI32(self.success)
            oprot.writeFieldEnd()
        if self.e != None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
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




class NetworkInterface_registerApplicationTagIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - apptag
    """

    thrift_spec = (None, (1,
      TType.I32,
      'sessionHandle',
      None,
      None), (2,
      TType.STRING,
      'apptag',
      None,
      None))

    def __init__(self, sessionHandle = None, apptag = None):
        self.sessionHandle = sessionHandle
        self.apptag = apptag



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
                    self.apptag = iprot.readString()
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
        oprot.writeStructBegin('NetworkInterface_registerApplicationTagIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.apptag != None:
            oprot.writeFieldBegin('apptag', TType.STRING, 2)
            oprot.writeString(self.apptag)
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




class NetworkInterface_registerApplicationTagIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.I32,
      'success',
      None,
      None), (1,
      TType.STRUCT,
      'e',
      (Shared.ttypes.ExceptionIDL, Shared.ttypes.ExceptionIDL.thrift_spec),
      None))

    def __init__(self, success = None, e = None):
        self.success = success
        self.e = e



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.I32:
                    self.success = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = Shared.ttypes.ExceptionIDL()
                    self.e.read(iprot)
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
        oprot.writeStructBegin('NetworkInterface_registerApplicationTagIDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.I32, 0)
            oprot.writeI32(self.success)
            oprot.writeFieldEnd()
        if self.e != None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
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




class NetworkInterface_setTagIDL_args(object):
    """
    Attributes:
     - xosHandle
     - tag
    """

    thrift_spec = (None, (1,
      TType.I64,
      'xosHandle',
      None,
      None), (2,
      TType.I32,
      'tag',
      None,
      None))

    def __init__(self, xosHandle = None, tag = None):
        self.xosHandle = xosHandle
        self.tag = tag



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
                if ftype == TType.I64:
                    self.xosHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.tag = iprot.readI32()
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
        oprot.writeStructBegin('NetworkInterface_setTagIDL_args')
        if self.xosHandle != None:
            oprot.writeFieldBegin('xosHandle', TType.I64, 1)
            oprot.writeI64(self.xosHandle)
            oprot.writeFieldEnd()
        if self.tag != None:
            oprot.writeFieldBegin('tag', TType.I32, 2)
            oprot.writeI32(self.tag)
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




class NetworkInterface_setTagIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.I32,
      'success',
      None,
      None), (1,
      TType.STRUCT,
      'e',
      (Shared.ttypes.ExceptionIDL, Shared.ttypes.ExceptionIDL.thrift_spec),
      None))

    def __init__(self, success = None, e = None):
        self.success = success
        self.e = e



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.I32:
                    self.success = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = Shared.ttypes.ExceptionIDL()
                    self.e.read(iprot)
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
        oprot.writeStructBegin('NetworkInterface_setTagIDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.I32, 0)
            oprot.writeI32(self.success)
            oprot.writeFieldEnd()
        if self.e != None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
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




class NetworkInterface_getSubInterfaceByIdIDL_args(object):
    """
    Attributes:
     - xosHandle
     - type
     - id
    """

    thrift_spec = (None,
     (1,
      TType.I64,
      'xosHandle',
      None,
      None),
     (2,
      TType.I32,
      'type',
      None,
      None),
     (3,
      TType.I64,
      'id',
      None,
      None))

    def __init__(self, xosHandle = None, type = None, id = None):
        self.xosHandle = xosHandle
        self.type = type
        self.id = id



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
                if ftype == TType.I64:
                    self.xosHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I64:
                    self.id = iprot.readI64()
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
        oprot.writeStructBegin('NetworkInterface_getSubInterfaceByIdIDL_args')
        if self.xosHandle != None:
            oprot.writeFieldBegin('xosHandle', TType.I64, 1)
            oprot.writeI64(self.xosHandle)
            oprot.writeFieldEnd()
        if self.type != None:
            oprot.writeFieldBegin('type', TType.I32, 2)
            oprot.writeI32(self.type)
            oprot.writeFieldEnd()
        if self.id != None:
            oprot.writeFieldBegin('id', TType.I64, 3)
            oprot.writeI64(self.id)
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




class NetworkInterface_getSubInterfaceByIdIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.STRUCT,
      'success',
      (Shared.ttypes.NetworkInterfaceIDL, Shared.ttypes.NetworkInterfaceIDL.thrift_spec),
      None), (1,
      TType.STRUCT,
      'e',
      (Shared.ttypes.ExceptionIDL, Shared.ttypes.ExceptionIDL.thrift_spec),
      None))

    def __init__(self, success = None, e = None):
        self.success = success
        self.e = e



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = Shared.ttypes.NetworkInterfaceIDL()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = Shared.ttypes.ExceptionIDL()
                    self.e.read(iprot)
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
        oprot.writeStructBegin('NetworkInterface_getSubInterfaceByIdIDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e != None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
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




class InterfaceStateEvent_registerIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - xosHandle
     - interfaceType
     - stateEventType
     - maxrun_sec
     - maxrun_msec
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionHandle',
      None,
      None),
     (2,
      TType.I64,
      'xosHandle',
      None,
      None),
     (3,
      TType.I32,
      'interfaceType',
      None,
      None),
     (4,
      TType.I32,
      'stateEventType',
      None,
      None),
     (5,
      TType.I32,
      'maxrun_sec',
      None,
      None),
     (6,
      TType.I32,
      'maxrun_msec',
      None,
      None))

    def __init__(self, sessionHandle = None, xosHandle = None, interfaceType = None, stateEventType = None, maxrun_sec = None, maxrun_msec = None):
        self.sessionHandle = sessionHandle
        self.xosHandle = xosHandle
        self.interfaceType = interfaceType
        self.stateEventType = stateEventType
        self.maxrun_sec = maxrun_sec
        self.maxrun_msec = maxrun_msec



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
                if ftype == TType.I64:
                    self.xosHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.interfaceType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.stateEventType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.maxrun_sec = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I32:
                    self.maxrun_msec = iprot.readI32()
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
        oprot.writeStructBegin('InterfaceStateEvent_registerIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.xosHandle != None:
            oprot.writeFieldBegin('xosHandle', TType.I64, 2)
            oprot.writeI64(self.xosHandle)
            oprot.writeFieldEnd()
        if self.interfaceType != None:
            oprot.writeFieldBegin('interfaceType', TType.I32, 3)
            oprot.writeI32(self.interfaceType)
            oprot.writeFieldEnd()
        if self.stateEventType != None:
            oprot.writeFieldBegin('stateEventType', TType.I32, 4)
            oprot.writeI32(self.stateEventType)
            oprot.writeFieldEnd()
        if self.maxrun_sec != None:
            oprot.writeFieldBegin('maxrun_sec', TType.I32, 5)
            oprot.writeI32(self.maxrun_sec)
            oprot.writeFieldEnd()
        if self.maxrun_msec != None:
            oprot.writeFieldBegin('maxrun_msec', TType.I32, 6)
            oprot.writeI32(self.maxrun_msec)
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




class InterfaceStateEvent_registerIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.STRUCT,
      'success',
      (Shared.ttypes.EventHandleIDL, Shared.ttypes.EventHandleIDL.thrift_spec),
      None), (1,
      TType.STRUCT,
      'e',
      (Shared.ttypes.ExceptionIDL, Shared.ttypes.ExceptionIDL.thrift_spec),
      None))

    def __init__(self, success = None, e = None):
        self.success = success
        self.e = e



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = Shared.ttypes.EventHandleIDL()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = Shared.ttypes.ExceptionIDL()
                    self.e.read(iprot)
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
        oprot.writeStructBegin('InterfaceStateEvent_registerIDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e != None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
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




class InterfaceStatisticsEvent_registerIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - xosHandle
     - parameter
     - poll_interval_sec
     - poll_interval_msec
     - entry_value
     - entry_op
     - entry_type
     - exit_value_set
     - exit_value
     - exit_op
     - exit_type
     - exit_comb
     - exit_time_sec
     - exit_time_msec
     - exit_event
     - average_factor
     - maxrun_sec
     - maxrun_msec
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionHandle',
      None,
      None),
     (2,
      TType.I64,
      'xosHandle',
      None,
      None),
     (3,
      TType.I32,
      'parameter',
      None,
      None),
     (4,
      TType.I32,
      'poll_interval_sec',
      None,
      None),
     (5,
      TType.I32,
      'poll_interval_msec',
      None,
      None),
     (6,
      TType.I32,
      'entry_value',
      None,
      None),
     (7,
      TType.I32,
      'entry_op',
      None,
      None),
     (8,
      TType.I32,
      'entry_type',
      None,
      None),
     (9,
      TType.I32,
      'exit_value_set',
      None,
      None),
     (10,
      TType.I32,
      'exit_value',
      None,
      None),
     (11,
      TType.I32,
      'exit_op',
      None,
      None),
     (12,
      TType.I32,
      'exit_type',
      None,
      None),
     (13,
      TType.I32,
      'exit_comb',
      None,
      None),
     (14,
      TType.I32,
      'exit_time_sec',
      None,
      None),
     (15,
      TType.I32,
      'exit_time_msec',
      None,
      None),
     (16,
      TType.I32,
      'exit_event',
      None,
      None),
     (17,
      TType.I32,
      'average_factor',
      None,
      None),
     (18,
      TType.I32,
      'maxrun_sec',
      None,
      None),
     (19,
      TType.I32,
      'maxrun_msec',
      None,
      None))

    def __init__(self, sessionHandle = None, xosHandle = None, parameter = None, poll_interval_sec = None, poll_interval_msec = None, entry_value = None, entry_op = None, entry_type = None, exit_value_set = None, exit_value = None, exit_op = None, exit_type = None, exit_comb = None, exit_time_sec = None, exit_time_msec = None, exit_event = None, average_factor = None, maxrun_sec = None, maxrun_msec = None):
        self.sessionHandle = sessionHandle
        self.xosHandle = xosHandle
        self.parameter = parameter
        self.poll_interval_sec = poll_interval_sec
        self.poll_interval_msec = poll_interval_msec
        self.entry_value = entry_value
        self.entry_op = entry_op
        self.entry_type = entry_type
        self.exit_value_set = exit_value_set
        self.exit_value = exit_value
        self.exit_op = exit_op
        self.exit_type = exit_type
        self.exit_comb = exit_comb
        self.exit_time_sec = exit_time_sec
        self.exit_time_msec = exit_time_msec
        self.exit_event = exit_event
        self.average_factor = average_factor
        self.maxrun_sec = maxrun_sec
        self.maxrun_msec = maxrun_msec



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
                if ftype == TType.I64:
                    self.xosHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.parameter = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.poll_interval_sec = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.poll_interval_msec = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I32:
                    self.entry_value = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I32:
                    self.entry_op = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.I32:
                    self.entry_type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.I32:
                    self.exit_value_set = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.I32:
                    self.exit_value = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.I32:
                    self.exit_op = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 12:
                if ftype == TType.I32:
                    self.exit_type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 13:
                if ftype == TType.I32:
                    self.exit_comb = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 14:
                if ftype == TType.I32:
                    self.exit_time_sec = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 15:
                if ftype == TType.I32:
                    self.exit_time_msec = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 16:
                if ftype == TType.I32:
                    self.exit_event = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 17:
                if ftype == TType.I32:
                    self.average_factor = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 18:
                if ftype == TType.I32:
                    self.maxrun_sec = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 19:
                if ftype == TType.I32:
                    self.maxrun_msec = iprot.readI32()
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
        oprot.writeStructBegin('InterfaceStatisticsEvent_registerIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.xosHandle != None:
            oprot.writeFieldBegin('xosHandle', TType.I64, 2)
            oprot.writeI64(self.xosHandle)
            oprot.writeFieldEnd()
        if self.parameter != None:
            oprot.writeFieldBegin('parameter', TType.I32, 3)
            oprot.writeI32(self.parameter)
            oprot.writeFieldEnd()
        if self.poll_interval_sec != None:
            oprot.writeFieldBegin('poll_interval_sec', TType.I32, 4)
            oprot.writeI32(self.poll_interval_sec)
            oprot.writeFieldEnd()
        if self.poll_interval_msec != None:
            oprot.writeFieldBegin('poll_interval_msec', TType.I32, 5)
            oprot.writeI32(self.poll_interval_msec)
            oprot.writeFieldEnd()
        if self.entry_value != None:
            oprot.writeFieldBegin('entry_value', TType.I32, 6)
            oprot.writeI32(self.entry_value)
            oprot.writeFieldEnd()
        if self.entry_op != None:
            oprot.writeFieldBegin('entry_op', TType.I32, 7)
            oprot.writeI32(self.entry_op)
            oprot.writeFieldEnd()
        if self.entry_type != None:
            oprot.writeFieldBegin('entry_type', TType.I32, 8)
            oprot.writeI32(self.entry_type)
            oprot.writeFieldEnd()
        if self.exit_value_set != None:
            oprot.writeFieldBegin('exit_value_set', TType.I32, 9)
            oprot.writeI32(self.exit_value_set)
            oprot.writeFieldEnd()
        if self.exit_value != None:
            oprot.writeFieldBegin('exit_value', TType.I32, 10)
            oprot.writeI32(self.exit_value)
            oprot.writeFieldEnd()
        if self.exit_op != None:
            oprot.writeFieldBegin('exit_op', TType.I32, 11)
            oprot.writeI32(self.exit_op)
            oprot.writeFieldEnd()
        if self.exit_type != None:
            oprot.writeFieldBegin('exit_type', TType.I32, 12)
            oprot.writeI32(self.exit_type)
            oprot.writeFieldEnd()
        if self.exit_comb != None:
            oprot.writeFieldBegin('exit_comb', TType.I32, 13)
            oprot.writeI32(self.exit_comb)
            oprot.writeFieldEnd()
        if self.exit_time_sec != None:
            oprot.writeFieldBegin('exit_time_sec', TType.I32, 14)
            oprot.writeI32(self.exit_time_sec)
            oprot.writeFieldEnd()
        if self.exit_time_msec != None:
            oprot.writeFieldBegin('exit_time_msec', TType.I32, 15)
            oprot.writeI32(self.exit_time_msec)
            oprot.writeFieldEnd()
        if self.exit_event != None:
            oprot.writeFieldBegin('exit_event', TType.I32, 16)
            oprot.writeI32(self.exit_event)
            oprot.writeFieldEnd()
        if self.average_factor != None:
            oprot.writeFieldBegin('average_factor', TType.I32, 17)
            oprot.writeI32(self.average_factor)
            oprot.writeFieldEnd()
        if self.maxrun_sec != None:
            oprot.writeFieldBegin('maxrun_sec', TType.I32, 18)
            oprot.writeI32(self.maxrun_sec)
            oprot.writeFieldEnd()
        if self.maxrun_msec != None:
            oprot.writeFieldBegin('maxrun_msec', TType.I32, 19)
            oprot.writeI32(self.maxrun_msec)
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




class InterfaceStatisticsEvent_registerIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.STRUCT,
      'success',
      (Shared.ttypes.EventHandleIDL, Shared.ttypes.EventHandleIDL.thrift_spec),
      None), (1,
      TType.STRUCT,
      'e',
      (Shared.ttypes.ExceptionIDL, Shared.ttypes.ExceptionIDL.thrift_spec),
      None))

    def __init__(self, success = None, e = None):
        self.success = success
        self.e = e



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = Shared.ttypes.EventHandleIDL()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = Shared.ttypes.ExceptionIDL()
                    self.e.read(iprot)
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
        oprot.writeStructBegin('InterfaceStatisticsEvent_registerIDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e != None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
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




class InterfaceMtuEvent_registerIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - xosHandle
     - interfaceType
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionHandle',
      None,
      None),
     (2,
      TType.I64,
      'xosHandle',
      None,
      None),
     (3,
      TType.I32,
      'interfaceType',
      None,
      None))

    def __init__(self, sessionHandle = None, xosHandle = None, interfaceType = None):
        self.sessionHandle = sessionHandle
        self.xosHandle = xosHandle
        self.interfaceType = interfaceType



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
                if ftype == TType.I64:
                    self.xosHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.interfaceType = iprot.readI32()
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
        oprot.writeStructBegin('InterfaceMtuEvent_registerIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.xosHandle != None:
            oprot.writeFieldBegin('xosHandle', TType.I64, 2)
            oprot.writeI64(self.xosHandle)
            oprot.writeFieldEnd()
        if self.interfaceType != None:
            oprot.writeFieldBegin('interfaceType', TType.I32, 3)
            oprot.writeI32(self.interfaceType)
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




class InterfaceMtuEvent_registerIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.STRUCT,
      'success',
      (Shared.ttypes.EventHandleIDL, Shared.ttypes.EventHandleIDL.thrift_spec),
      None), (1,
      TType.STRUCT,
      'e',
      (Shared.ttypes.ExceptionIDL, Shared.ttypes.ExceptionIDL.thrift_spec),
      None))

    def __init__(self, success = None, e = None):
        self.success = success
        self.e = e



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = Shared.ttypes.EventHandleIDL()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = Shared.ttypes.ExceptionIDL()
                    self.e.read(iprot)
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
        oprot.writeStructBegin('InterfaceMtuEvent_registerIDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e != None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
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




class InterfaceSpeedEvent_registerIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - xosHandle
     - interfaceType
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionHandle',
      None,
      None),
     (2,
      TType.I64,
      'xosHandle',
      None,
      None),
     (3,
      TType.I32,
      'interfaceType',
      None,
      None))

    def __init__(self, sessionHandle = None, xosHandle = None, interfaceType = None):
        self.sessionHandle = sessionHandle
        self.xosHandle = xosHandle
        self.interfaceType = interfaceType



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
                if ftype == TType.I64:
                    self.xosHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.interfaceType = iprot.readI32()
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
        oprot.writeStructBegin('InterfaceSpeedEvent_registerIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.xosHandle != None:
            oprot.writeFieldBegin('xosHandle', TType.I64, 2)
            oprot.writeI64(self.xosHandle)
            oprot.writeFieldEnd()
        if self.interfaceType != None:
            oprot.writeFieldBegin('interfaceType', TType.I32, 3)
            oprot.writeI32(self.interfaceType)
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




class InterfaceSpeedEvent_registerIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.STRUCT,
      'success',
      (Shared.ttypes.EventHandleIDL, Shared.ttypes.EventHandleIDL.thrift_spec),
      None), (1,
      TType.STRUCT,
      'e',
      (Shared.ttypes.ExceptionIDL, Shared.ttypes.ExceptionIDL.thrift_spec),
      None))

    def __init__(self, success = None, e = None):
        self.success = success
        self.e = e



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = Shared.ttypes.EventHandleIDL()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = Shared.ttypes.ExceptionIDL()
                    self.e.read(iprot)
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
        oprot.writeStructBegin('InterfaceSpeedEvent_registerIDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e != None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
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




class InterfaceDuplexModeEvent_registerIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - xosHandle
     - interfaceType
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionHandle',
      None,
      None),
     (2,
      TType.I64,
      'xosHandle',
      None,
      None),
     (3,
      TType.I32,
      'interfaceType',
      None,
      None))

    def __init__(self, sessionHandle = None, xosHandle = None, interfaceType = None):
        self.sessionHandle = sessionHandle
        self.xosHandle = xosHandle
        self.interfaceType = interfaceType



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
                if ftype == TType.I64:
                    self.xosHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.interfaceType = iprot.readI32()
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
        oprot.writeStructBegin('InterfaceDuplexModeEvent_registerIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.xosHandle != None:
            oprot.writeFieldBegin('xosHandle', TType.I64, 2)
            oprot.writeI64(self.xosHandle)
            oprot.writeFieldEnd()
        if self.interfaceType != None:
            oprot.writeFieldBegin('interfaceType', TType.I32, 3)
            oprot.writeI32(self.interfaceType)
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




class InterfaceDuplexModeEvent_registerIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.STRUCT,
      'success',
      (Shared.ttypes.EventHandleIDL, Shared.ttypes.EventHandleIDL.thrift_spec),
      None), (1,
      TType.STRUCT,
      'e',
      (Shared.ttypes.ExceptionIDL, Shared.ttypes.ExceptionIDL.thrift_spec),
      None))

    def __init__(self, success = None, e = None):
        self.success = success
        self.e = e



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = Shared.ttypes.EventHandleIDL()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = Shared.ttypes.ExceptionIDL()
                    self.e.read(iprot)
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
        oprot.writeStructBegin('InterfaceDuplexModeEvent_registerIDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e != None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
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




class InterfaceAutoNegotiateEvent_registerIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - xosHandle
     - interfaceType
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionHandle',
      None,
      None),
     (2,
      TType.I64,
      'xosHandle',
      None,
      None),
     (3,
      TType.I32,
      'interfaceType',
      None,
      None))

    def __init__(self, sessionHandle = None, xosHandle = None, interfaceType = None):
        self.sessionHandle = sessionHandle
        self.xosHandle = xosHandle
        self.interfaceType = interfaceType



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
                if ftype == TType.I64:
                    self.xosHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.interfaceType = iprot.readI32()
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
        oprot.writeStructBegin('InterfaceAutoNegotiateEvent_registerIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.xosHandle != None:
            oprot.writeFieldBegin('xosHandle', TType.I64, 2)
            oprot.writeI64(self.xosHandle)
            oprot.writeFieldEnd()
        if self.interfaceType != None:
            oprot.writeFieldBegin('interfaceType', TType.I32, 3)
            oprot.writeI32(self.interfaceType)
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




class InterfaceAutoNegotiateEvent_registerIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.STRUCT,
      'success',
      (Shared.ttypes.EventHandleIDL, Shared.ttypes.EventHandleIDL.thrift_spec),
      None), (1,
      TType.STRUCT,
      'e',
      (Shared.ttypes.ExceptionIDL, Shared.ttypes.ExceptionIDL.thrift_spec),
      None))

    def __init__(self, success = None, e = None):
        self.success = success
        self.e = e



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = Shared.ttypes.EventHandleIDL()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = Shared.ttypes.ExceptionIDL()
                    self.e.read(iprot)
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
        oprot.writeStructBegin('InterfaceAutoNegotiateEvent_registerIDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e != None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
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




class InterfaceFlowcontrolEvent_registerIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - xosHandle
     - interfaceType
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionHandle',
      None,
      None),
     (2,
      TType.I64,
      'xosHandle',
      None,
      None),
     (3,
      TType.I32,
      'interfaceType',
      None,
      None))

    def __init__(self, sessionHandle = None, xosHandle = None, interfaceType = None):
        self.sessionHandle = sessionHandle
        self.xosHandle = xosHandle
        self.interfaceType = interfaceType



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
                if ftype == TType.I64:
                    self.xosHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.interfaceType = iprot.readI32()
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
        oprot.writeStructBegin('InterfaceFlowcontrolEvent_registerIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.xosHandle != None:
            oprot.writeFieldBegin('xosHandle', TType.I64, 2)
            oprot.writeI64(self.xosHandle)
            oprot.writeFieldEnd()
        if self.interfaceType != None:
            oprot.writeFieldBegin('interfaceType', TType.I32, 3)
            oprot.writeI32(self.interfaceType)
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




class InterfaceFlowcontrolEvent_registerIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.STRUCT,
      'success',
      (Shared.ttypes.EventHandleIDL, Shared.ttypes.EventHandleIDL.thrift_spec),
      None), (1,
      TType.STRUCT,
      'e',
      (Shared.ttypes.ExceptionIDL, Shared.ttypes.ExceptionIDL.thrift_spec),
      None))

    def __init__(self, success = None, e = None):
        self.success = success
        self.e = e



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = Shared.ttypes.EventHandleIDL()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = Shared.ttypes.ExceptionIDL()
                    self.e.read(iprot)
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
        oprot.writeStructBegin('InterfaceFlowcontrolEvent_registerIDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e != None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
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




class InterfaceLayer2ModeEvent_registerIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - xosHandle
     - interfaceType
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionHandle',
      None,
      None),
     (2,
      TType.I64,
      'xosHandle',
      None,
      None),
     (3,
      TType.I32,
      'interfaceType',
      None,
      None))

    def __init__(self, sessionHandle = None, xosHandle = None, interfaceType = None):
        self.sessionHandle = sessionHandle
        self.xosHandle = xosHandle
        self.interfaceType = interfaceType



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
                if ftype == TType.I64:
                    self.xosHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.interfaceType = iprot.readI32()
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
        oprot.writeStructBegin('InterfaceLayer2ModeEvent_registerIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.xosHandle != None:
            oprot.writeFieldBegin('xosHandle', TType.I64, 2)
            oprot.writeI64(self.xosHandle)
            oprot.writeFieldEnd()
        if self.interfaceType != None:
            oprot.writeFieldBegin('interfaceType', TType.I32, 3)
            oprot.writeI32(self.interfaceType)
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




class InterfaceLayer2ModeEvent_registerIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.STRUCT,
      'success',
      (Shared.ttypes.EventHandleIDL, Shared.ttypes.EventHandleIDL.thrift_spec),
      None), (1,
      TType.STRUCT,
      'e',
      (Shared.ttypes.ExceptionIDL, Shared.ttypes.ExceptionIDL.thrift_spec),
      None))

    def __init__(self, success = None, e = None):
        self.success = success
        self.e = e



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = Shared.ttypes.EventHandleIDL()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = Shared.ttypes.ExceptionIDL()
                    self.e.read(iprot)
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
        oprot.writeStructBegin('InterfaceLayer2ModeEvent_registerIDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e != None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
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




class InterfaceForwardClassIDEvent_registerIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - xosHandle
     - interfaceType
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionHandle',
      None,
      None),
     (2,
      TType.I64,
      'xosHandle',
      None,
      None),
     (3,
      TType.I32,
      'interfaceType',
      None,
      None))

    def __init__(self, sessionHandle = None, xosHandle = None, interfaceType = None):
        self.sessionHandle = sessionHandle
        self.xosHandle = xosHandle
        self.interfaceType = interfaceType



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
                if ftype == TType.I64:
                    self.xosHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.interfaceType = iprot.readI32()
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
        oprot.writeStructBegin('InterfaceForwardClassIDEvent_registerIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.xosHandle != None:
            oprot.writeFieldBegin('xosHandle', TType.I64, 2)
            oprot.writeI64(self.xosHandle)
            oprot.writeFieldEnd()
        if self.interfaceType != None:
            oprot.writeFieldBegin('interfaceType', TType.I32, 3)
            oprot.writeI32(self.interfaceType)
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




class InterfaceForwardClassIDEvent_registerIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.STRUCT,
      'success',
      (Shared.ttypes.EventHandleIDL, Shared.ttypes.EventHandleIDL.thrift_spec),
      None), (1,
      TType.STRUCT,
      'e',
      (Shared.ttypes.ExceptionIDL, Shared.ttypes.ExceptionIDL.thrift_spec),
      None))

    def __init__(self, success = None, e = None):
        self.success = success
        self.e = e



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = Shared.ttypes.EventHandleIDL()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = Shared.ttypes.ExceptionIDL()
                    self.e.read(iprot)
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
        oprot.writeStructBegin('InterfaceForwardClassIDEvent_registerIDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e != None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
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




class InterfaceBandwidthEvent_registerIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - xosHandle
     - interfaceType
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionHandle',
      None,
      None),
     (2,
      TType.I64,
      'xosHandle',
      None,
      None),
     (3,
      TType.I32,
      'interfaceType',
      None,
      None))

    def __init__(self, sessionHandle = None, xosHandle = None, interfaceType = None):
        self.sessionHandle = sessionHandle
        self.xosHandle = xosHandle
        self.interfaceType = interfaceType



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
                if ftype == TType.I64:
                    self.xosHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.interfaceType = iprot.readI32()
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
        oprot.writeStructBegin('InterfaceBandwidthEvent_registerIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.xosHandle != None:
            oprot.writeFieldBegin('xosHandle', TType.I64, 2)
            oprot.writeI64(self.xosHandle)
            oprot.writeFieldEnd()
        if self.interfaceType != None:
            oprot.writeFieldBegin('interfaceType', TType.I32, 3)
            oprot.writeI32(self.interfaceType)
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




class InterfaceBandwidthEvent_registerIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.STRUCT,
      'success',
      (Shared.ttypes.EventHandleIDL, Shared.ttypes.EventHandleIDL.thrift_spec),
      None), (1,
      TType.STRUCT,
      'e',
      (Shared.ttypes.ExceptionIDL, Shared.ttypes.ExceptionIDL.thrift_spec),
      None))

    def __init__(self, success = None, e = None):
        self.success = success
        self.e = e



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = Shared.ttypes.EventHandleIDL()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = Shared.ttypes.ExceptionIDL()
                    self.e.read(iprot)
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
        oprot.writeStructBegin('InterfaceBandwidthEvent_registerIDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e != None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
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




class InterfaceVrfEvent_registerIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - xosHandle
     - interfaceType
     - vrfname
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionHandle',
      None,
      None),
     (2,
      TType.I64,
      'xosHandle',
      None,
      None),
     (3,
      TType.I32,
      'interfaceType',
      None,
      None),
     (4,
      TType.STRING,
      'vrfname',
      None,
      None))

    def __init__(self, sessionHandle = None, xosHandle = None, interfaceType = None, vrfname = None):
        self.sessionHandle = sessionHandle
        self.xosHandle = xosHandle
        self.interfaceType = interfaceType
        self.vrfname = vrfname



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
                if ftype == TType.I64:
                    self.xosHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.interfaceType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.vrfname = iprot.readString()
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
        oprot.writeStructBegin('InterfaceVrfEvent_registerIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.xosHandle != None:
            oprot.writeFieldBegin('xosHandle', TType.I64, 2)
            oprot.writeI64(self.xosHandle)
            oprot.writeFieldEnd()
        if self.interfaceType != None:
            oprot.writeFieldBegin('interfaceType', TType.I32, 3)
            oprot.writeI32(self.interfaceType)
            oprot.writeFieldEnd()
        if self.vrfname != None:
            oprot.writeFieldBegin('vrfname', TType.STRING, 4)
            oprot.writeString(self.vrfname)
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




class InterfaceVrfEvent_registerIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.STRUCT,
      'success',
      (Shared.ttypes.EventHandleIDL, Shared.ttypes.EventHandleIDL.thrift_spec),
      None), (1,
      TType.STRUCT,
      'e',
      (Shared.ttypes.ExceptionIDL, Shared.ttypes.ExceptionIDL.thrift_spec),
      None))

    def __init__(self, success = None, e = None):
        self.success = success
        self.e = e



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = Shared.ttypes.EventHandleIDL()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = Shared.ttypes.ExceptionIDL()
                    self.e.read(iprot)
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
        oprot.writeStructBegin('InterfaceVrfEvent_registerIDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e != None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
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




class InterfaceVlanEvent_registerIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - xosHandle
     - interfaceType
     - vlanEvtType
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionHandle',
      None,
      None),
     (2,
      TType.I64,
      'xosHandle',
      None,
      None),
     (3,
      TType.I32,
      'interfaceType',
      None,
      None),
     (4,
      TType.I32,
      'vlanEvtType',
      None,
      None))

    def __init__(self, sessionHandle = None, xosHandle = None, interfaceType = None, vlanEvtType = None):
        self.sessionHandle = sessionHandle
        self.xosHandle = xosHandle
        self.interfaceType = interfaceType
        self.vlanEvtType = vlanEvtType



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
                if ftype == TType.I64:
                    self.xosHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.interfaceType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.vlanEvtType = iprot.readI32()
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
        oprot.writeStructBegin('InterfaceVlanEvent_registerIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.xosHandle != None:
            oprot.writeFieldBegin('xosHandle', TType.I64, 2)
            oprot.writeI64(self.xosHandle)
            oprot.writeFieldEnd()
        if self.interfaceType != None:
            oprot.writeFieldBegin('interfaceType', TType.I32, 3)
            oprot.writeI32(self.interfaceType)
            oprot.writeFieldEnd()
        if self.vlanEvtType != None:
            oprot.writeFieldBegin('vlanEvtType', TType.I32, 4)
            oprot.writeI32(self.vlanEvtType)
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




class InterfaceVlanEvent_registerIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.STRUCT,
      'success',
      (Shared.ttypes.EventHandleIDL, Shared.ttypes.EventHandleIDL.thrift_spec),
      None), (1,
      TType.STRUCT,
      'e',
      (Shared.ttypes.ExceptionIDL, Shared.ttypes.ExceptionIDL.thrift_spec),
      None))

    def __init__(self, success = None, e = None):
        self.success = success
        self.e = e



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = Shared.ttypes.EventHandleIDL()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = Shared.ttypes.ExceptionIDL()
                    self.e.read(iprot)
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
        oprot.writeStructBegin('InterfaceVlanEvent_registerIDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e != None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
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




class NetworkInterface_getVrfIDL_args(object):
    """
    Attributes:
     - xosHandle
    """

    thrift_spec = (None, (1,
      TType.I64,
      'xosHandle',
      None,
      None))

    def __init__(self, xosHandle = None):
        self.xosHandle = xosHandle



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
                if ftype == TType.I64:
                    self.xosHandle = iprot.readI64()
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
        oprot.writeStructBegin('NetworkInterface_getVrfIDL_args')
        if self.xosHandle != None:
            oprot.writeFieldBegin('xosHandle', TType.I64, 1)
            oprot.writeI64(self.xosHandle)
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




class NetworkInterface_getVrfIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.STRING,
      'success',
      None,
      None), (1,
      TType.STRUCT,
      'e',
      (Shared.ttypes.ExceptionIDL, Shared.ttypes.ExceptionIDL.thrift_spec),
      None))

    def __init__(self, success = None, e = None):
        self.success = success
        self.e = e



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRING:
                    self.success = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = Shared.ttypes.ExceptionIDL()
                    self.e.read(iprot)
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
        oprot.writeStructBegin('NetworkInterface_getVrfIDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.STRING, 0)
            oprot.writeString(self.success)
            oprot.writeFieldEnd()
        if self.e != None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
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




class NetworkInterface_getVlanIDL_args(object):
    """
    Attributes:
     - xosHandle
    """

    thrift_spec = (None, (1,
      TType.I64,
      'xosHandle',
      None,
      None))

    def __init__(self, xosHandle = None):
        self.xosHandle = xosHandle



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
                if ftype == TType.I64:
                    self.xosHandle = iprot.readI64()
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
        oprot.writeStructBegin('NetworkInterface_getVlanIDL_args')
        if self.xosHandle != None:
            oprot.writeFieldBegin('xosHandle', TType.I64, 1)
            oprot.writeI64(self.xosHandle)
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




class NetworkInterface_getVlanIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.STRUCT,
      'success',
      (InterfaceVlanIDL, InterfaceVlanIDL.thrift_spec),
      None), (1,
      TType.STRUCT,
      'e',
      (Shared.ttypes.ExceptionIDL, Shared.ttypes.ExceptionIDL.thrift_spec),
      None))

    def __init__(self, success = None, e = None):
        self.success = success
        self.e = e



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = InterfaceVlanIDL()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = Shared.ttypes.ExceptionIDL()
                    self.e.read(iprot)
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
        oprot.writeStructBegin('NetworkInterface_getVlanIDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e != None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
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




class NetworkInterface_createConfigIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - type
     - index
     - parentHandle
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
      'type',
      None,
      None),
     (3,
      TType.I32,
      'index',
      None,
      None),
     (4,
      TType.I64,
      'parentHandle',
      None,
      None),
     (5,
      TType.I32,
      'add',
      None,
      None))

    def __init__(self, sessionHandle = None, type = None, index = None, parentHandle = None, add = None):
        self.sessionHandle = sessionHandle
        self.type = type
        self.index = index
        self.parentHandle = parentHandle
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
                    self.type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.index = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I64:
                    self.parentHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
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
        oprot.writeStructBegin('NetworkInterface_createConfigIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.type != None:
            oprot.writeFieldBegin('type', TType.I32, 2)
            oprot.writeI32(self.type)
            oprot.writeFieldEnd()
        if self.index != None:
            oprot.writeFieldBegin('index', TType.I32, 3)
            oprot.writeI32(self.index)
            oprot.writeFieldEnd()
        if self.parentHandle != None:
            oprot.writeFieldBegin('parentHandle', TType.I64, 4)
            oprot.writeI64(self.parentHandle)
            oprot.writeFieldEnd()
        if self.add != None:
            oprot.writeFieldBegin('add', TType.I32, 5)
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




class NetworkInterface_createConfigIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.I64,
      'success',
      None,
      None), (1,
      TType.STRUCT,
      'e',
      (Shared.ttypes.ExceptionIDL, Shared.ttypes.ExceptionIDL.thrift_spec),
      None))

    def __init__(self, success = None, e = None):
        self.success = success
        self.e = e



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.I64:
                    self.success = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = Shared.ttypes.ExceptionIDL()
                    self.e.read(iprot)
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
        oprot.writeStructBegin('NetworkInterface_createConfigIDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.I64, 0)
            oprot.writeI64(self.success)
            oprot.writeFieldEnd()
        if self.e != None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
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




class NetworkInterface_getBDInstanceIDL_args(object):
    """
    Attributes:
     - xosHandle
    """

    thrift_spec = (None, (1,
      TType.I64,
      'xosHandle',
      None,
      None))

    def __init__(self, xosHandle = None):
        self.xosHandle = xosHandle



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
                if ftype == TType.I64:
                    self.xosHandle = iprot.readI64()
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
        oprot.writeStructBegin('NetworkInterface_getBDInstanceIDL_args')
        if self.xosHandle != None:
            oprot.writeFieldBegin('xosHandle', TType.I64, 1)
            oprot.writeI64(self.xosHandle)
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




class NetworkInterface_getBDInstanceIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.STRUCT,
      'success',
      (Shared.ttypes.BDInstanceIDL, Shared.ttypes.BDInstanceIDL.thrift_spec),
      None), (1,
      TType.STRUCT,
      'e',
      (Shared.ttypes.ExceptionIDL, Shared.ttypes.ExceptionIDL.thrift_spec),
      None))

    def __init__(self, success = None, e = None):
        self.success = success
        self.e = e



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = Shared.ttypes.BDInstanceIDL()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = Shared.ttypes.ExceptionIDL()
                    self.e.read(iprot)
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
        oprot.writeStructBegin('NetworkInterface_getBDInstanceIDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e != None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
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




class PChannel_getMembersIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - xosHandle
    """

    thrift_spec = (None, (1,
      TType.I32,
      'sessionHandle',
      None,
      None), (2,
      TType.I64,
      'xosHandle',
      None,
      None))

    def __init__(self, sessionHandle = None, xosHandle = None):
        self.sessionHandle = sessionHandle
        self.xosHandle = xosHandle



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
                if ftype == TType.I64:
                    self.xosHandle = iprot.readI64()
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
        oprot.writeStructBegin('PChannel_getMembersIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.xosHandle != None:
            oprot.writeFieldBegin('xosHandle', TType.I64, 2)
            oprot.writeI64(self.xosHandle)
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




class PChannel_getMembersIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.LIST,
      'success',
      (TType.STRUCT, (Shared.ttypes.NetworkInterfaceIDL, Shared.ttypes.NetworkInterfaceIDL.thrift_spec)),
      None), (1,
      TType.STRUCT,
      'e',
      (Shared.ttypes.ExceptionIDL, Shared.ttypes.ExceptionIDL.thrift_spec),
      None))

    def __init__(self, success = None, e = None):
        self.success = success
        self.e = e



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.LIST:
                    self.success = []
                    (_etype52, _size49,) = iprot.readListBegin()
                    for _i53 in xrange(_size49):
                        _elem54 = Shared.ttypes.NetworkInterfaceIDL()
                        _elem54.read(iprot)
                        self.success.append(_elem54)

                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = Shared.ttypes.ExceptionIDL()
                    self.e.read(iprot)
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
        oprot.writeStructBegin('PChannel_getMembersIDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.STRUCT, len(self.success))
            for iter55 in self.success:
                iter55.write(oprot)

            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.e != None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
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




class PChannel_getMemberModeIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - xosHandle
    """

    thrift_spec = (None, (1,
      TType.I32,
      'sessionHandle',
      None,
      None), (2,
      TType.I64,
      'xosHandle',
      None,
      None))

    def __init__(self, sessionHandle = None, xosHandle = None):
        self.sessionHandle = sessionHandle
        self.xosHandle = xosHandle



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
                if ftype == TType.I64:
                    self.xosHandle = iprot.readI64()
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
        oprot.writeStructBegin('PChannel_getMemberModeIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.xosHandle != None:
            oprot.writeFieldBegin('xosHandle', TType.I64, 2)
            oprot.writeI64(self.xosHandle)
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




class PChannel_getMemberModeIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.I32,
      'success',
      None,
      None), (1,
      TType.STRUCT,
      'e',
      (Shared.ttypes.ExceptionIDL, Shared.ttypes.ExceptionIDL.thrift_spec),
      None))

    def __init__(self, success = None, e = None):
        self.success = success
        self.e = e



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.I32:
                    self.success = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = Shared.ttypes.ExceptionIDL()
                    self.e.read(iprot)
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
        oprot.writeStructBegin('PChannel_getMemberModeIDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.I32, 0)
            oprot.writeI32(self.success)
            oprot.writeFieldEnd()
        if self.e != None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
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




class PChannel_getMemberPriorityIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - xosHandle
    """

    thrift_spec = (None, (1,
      TType.I32,
      'sessionHandle',
      None,
      None), (2,
      TType.I64,
      'xosHandle',
      None,
      None))

    def __init__(self, sessionHandle = None, xosHandle = None):
        self.sessionHandle = sessionHandle
        self.xosHandle = xosHandle



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
                if ftype == TType.I64:
                    self.xosHandle = iprot.readI64()
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
        oprot.writeStructBegin('PChannel_getMemberPriorityIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.xosHandle != None:
            oprot.writeFieldBegin('xosHandle', TType.I64, 2)
            oprot.writeI64(self.xosHandle)
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




class PChannel_getMemberPriorityIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.I16,
      'success',
      None,
      None), (1,
      TType.STRUCT,
      'e',
      (Shared.ttypes.ExceptionIDL, Shared.ttypes.ExceptionIDL.thrift_spec),
      None))

    def __init__(self, success = None, e = None):
        self.success = success
        self.e = e



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.I16:
                    self.success = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = Shared.ttypes.ExceptionIDL()
                    self.e.read(iprot)
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
        oprot.writeStructBegin('PChannel_getMemberPriorityIDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.I16, 0)
            oprot.writeI16(self.success)
            oprot.writeFieldEnd()
        if self.e != None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
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




class NetworkInterface_getPChannelIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - xosHandle
    """

    thrift_spec = (None, (1,
      TType.I32,
      'sessionHandle',
      None,
      None), (2,
      TType.I64,
      'xosHandle',
      None,
      None))

    def __init__(self, sessionHandle = None, xosHandle = None):
        self.sessionHandle = sessionHandle
        self.xosHandle = xosHandle



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
                if ftype == TType.I64:
                    self.xosHandle = iprot.readI64()
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
        oprot.writeStructBegin('NetworkInterface_getPChannelIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.xosHandle != None:
            oprot.writeFieldBegin('xosHandle', TType.I64, 2)
            oprot.writeI64(self.xosHandle)
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




class NetworkInterface_getPChannelIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.STRUCT,
      'success',
      (Shared.ttypes.NetworkInterfaceIDL, Shared.ttypes.NetworkInterfaceIDL.thrift_spec),
      None), (1,
      TType.STRUCT,
      'e',
      (Shared.ttypes.ExceptionIDL, Shared.ttypes.ExceptionIDL.thrift_spec),
      None))

    def __init__(self, success = None, e = None):
        self.success = success
        self.e = e



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = Shared.ttypes.NetworkInterfaceIDL()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = Shared.ttypes.ExceptionIDL()
                    self.e.read(iprot)
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
        oprot.writeStructBegin('NetworkInterface_getPChannelIDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e != None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
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




class NetworkInterface_getIifIdIDL_args(object):
    """
    Attributes:
     - xosHandle
    """

    thrift_spec = (None, (1,
      TType.I64,
      'xosHandle',
      None,
      None))

    def __init__(self, xosHandle = None):
        self.xosHandle = xosHandle



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
                if ftype == TType.I64:
                    self.xosHandle = iprot.readI64()
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
        oprot.writeStructBegin('NetworkInterface_getIifIdIDL_args')
        if self.xosHandle != None:
            oprot.writeFieldBegin('xosHandle', TType.I64, 1)
            oprot.writeI64(self.xosHandle)
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




class NetworkInterface_getIifIdIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.I64,
      'success',
      None,
      None), (1,
      TType.STRUCT,
      'e',
      (Shared.ttypes.ExceptionIDL, Shared.ttypes.ExceptionIDL.thrift_spec),
      None))

    def __init__(self, success = None, e = None):
        self.success = success
        self.e = e



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.I64:
                    self.success = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = Shared.ttypes.ExceptionIDL()
                    self.e.read(iprot)
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
        oprot.writeStructBegin('NetworkInterface_getIifIdIDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.I64, 0)
            oprot.writeI64(self.success)
            oprot.writeFieldEnd()
        if self.e != None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
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
# 2015.02.05 17:19:11 IST
