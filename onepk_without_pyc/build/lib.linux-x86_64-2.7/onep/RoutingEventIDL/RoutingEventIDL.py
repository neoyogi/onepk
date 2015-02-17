# 2015.02.05 17:20:05 IST
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

    def OnepEvent_L3UcastRibRouteEventIDL(self, base, ribState):
        """
        Parameters:
         - base
         - ribState
        """
        pass



    def OnepEvent_L3UcastARTRouteEventIDL(self, base, artState):
        """
        Parameters:
         - base
         - artState
        """
        pass



    def AsyncMsg_L3UcastARTRouteUpdateAsyncIDL(self, base, scope, opList, status):
        """
        Parameters:
         - base
         - scope
         - opList
         - status
        """
        pass



    def OnepEvent_RoutingServiceStatusEventIDL(self, sessionHandle, eventHandle, routingService, status):
        """
        Parameters:
         - sessionHandle
         - eventHandle
         - routingService
         - status
        """
        pass



    def OnepEvent_RoutingReplayRouteEventIDL(self, sessionHandle, eventHandle, afi, safi, vrfName, topoName):
        """
        Parameters:
         - sessionHandle
         - eventHandle
         - afi
         - safi
         - vrfName
         - topoName
        """
        pass



    def OnepEvent_VrfStatusEventIDL(self, sessionHandle, eventHandle, vrf, event_type):
        """
        Parameters:
         - sessionHandle
         - eventHandle
         - vrf
         - event_type
        """
        pass




class Client(Iface):

    def __init__(self, iprot, oprot = None):
        self._iprot = self._oprot = iprot
        if oprot != None:
            self._oprot = oprot
        self._seqid = 0



    def OnepEvent_L3UcastRibRouteEventIDL(self, base, ribState):
        """
        Parameters:
         - base
         - ribState
        """
        self._oprot.rlock.acquire()
        try:
            self.send_OnepEvent_L3UcastRibRouteEventIDL(base, ribState)
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()



    def send_OnepEvent_L3UcastRibRouteEventIDL(self, base, ribState):
        self._oprot.writeMessageBegin('OnepEvent_L3UcastRibRouteEventIDL', TMessageType.CALL, self._seqid)
        args = OnepEvent_L3UcastRibRouteEventIDL_args()
        args.base = base
        args.ribState = ribState
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def OnepEvent_L3UcastARTRouteEventIDL(self, base, artState):
        """
        Parameters:
         - base
         - artState
        """
        self._oprot.rlock.acquire()
        try:
            self.send_OnepEvent_L3UcastARTRouteEventIDL(base, artState)
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()



    def send_OnepEvent_L3UcastARTRouteEventIDL(self, base, artState):
        self._oprot.writeMessageBegin('OnepEvent_L3UcastARTRouteEventIDL', TMessageType.CALL, self._seqid)
        args = OnepEvent_L3UcastARTRouteEventIDL_args()
        args.base = base
        args.artState = artState
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def AsyncMsg_L3UcastARTRouteUpdateAsyncIDL(self, base, scope, opList, status):
        """
        Parameters:
         - base
         - scope
         - opList
         - status
        """
        self._oprot.rlock.acquire()
        try:
            self.send_AsyncMsg_L3UcastARTRouteUpdateAsyncIDL(base, scope, opList, status)
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()



    def send_AsyncMsg_L3UcastARTRouteUpdateAsyncIDL(self, base, scope, opList, status):
        self._oprot.writeMessageBegin('AsyncMsg_L3UcastARTRouteUpdateAsyncIDL', TMessageType.CALL, self._seqid)
        args = AsyncMsg_L3UcastARTRouteUpdateAsyncIDL_args()
        args.base = base
        args.scope = scope
        args.opList = opList
        args.status = status
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def OnepEvent_RoutingServiceStatusEventIDL(self, sessionHandle, eventHandle, routingService, status):
        """
        Parameters:
         - sessionHandle
         - eventHandle
         - routingService
         - status
        """
        self._oprot.rlock.acquire()
        try:
            self.send_OnepEvent_RoutingServiceStatusEventIDL(sessionHandle, eventHandle, routingService, status)
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()



    def send_OnepEvent_RoutingServiceStatusEventIDL(self, sessionHandle, eventHandle, routingService, status):
        self._oprot.writeMessageBegin('OnepEvent_RoutingServiceStatusEventIDL', TMessageType.CALL, self._seqid)
        args = OnepEvent_RoutingServiceStatusEventIDL_args()
        args.sessionHandle = sessionHandle
        args.eventHandle = eventHandle
        args.routingService = routingService
        args.status = status
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def OnepEvent_RoutingReplayRouteEventIDL(self, sessionHandle, eventHandle, afi, safi, vrfName, topoName):
        """
        Parameters:
         - sessionHandle
         - eventHandle
         - afi
         - safi
         - vrfName
         - topoName
        """
        self._oprot.rlock.acquire()
        try:
            self.send_OnepEvent_RoutingReplayRouteEventIDL(sessionHandle, eventHandle, afi, safi, vrfName, topoName)
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()



    def send_OnepEvent_RoutingReplayRouteEventIDL(self, sessionHandle, eventHandle, afi, safi, vrfName, topoName):
        self._oprot.writeMessageBegin('OnepEvent_RoutingReplayRouteEventIDL', TMessageType.CALL, self._seqid)
        args = OnepEvent_RoutingReplayRouteEventIDL_args()
        args.sessionHandle = sessionHandle
        args.eventHandle = eventHandle
        args.afi = afi
        args.safi = safi
        args.vrfName = vrfName
        args.topoName = topoName
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def OnepEvent_VrfStatusEventIDL(self, sessionHandle, eventHandle, vrf, event_type):
        """
        Parameters:
         - sessionHandle
         - eventHandle
         - vrf
         - event_type
        """
        self._oprot.rlock.acquire()
        try:
            self.send_OnepEvent_VrfStatusEventIDL(sessionHandle, eventHandle, vrf, event_type)
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()



    def send_OnepEvent_VrfStatusEventIDL(self, sessionHandle, eventHandle, vrf, event_type):
        self._oprot.writeMessageBegin('OnepEvent_VrfStatusEventIDL', TMessageType.CALL, self._seqid)
        args = OnepEvent_VrfStatusEventIDL_args()
        args.sessionHandle = sessionHandle
        args.eventHandle = eventHandle
        args.vrf = vrf
        args.event_type = event_type
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()




class Processor(Iface, TProcessor):

    def __init__(self, handler):
        self._handler = handler
        self._processMap = {}
        self._processMap['OnepEvent_L3UcastRibRouteEventIDL'] = Processor.process_OnepEvent_L3UcastRibRouteEventIDL
        self._processMap['OnepEvent_L3UcastARTRouteEventIDL'] = Processor.process_OnepEvent_L3UcastARTRouteEventIDL
        self._processMap['AsyncMsg_L3UcastARTRouteUpdateAsyncIDL'] = Processor.process_AsyncMsg_L3UcastARTRouteUpdateAsyncIDL
        self._processMap['OnepEvent_RoutingServiceStatusEventIDL'] = Processor.process_OnepEvent_RoutingServiceStatusEventIDL
        self._processMap['OnepEvent_RoutingReplayRouteEventIDL'] = Processor.process_OnepEvent_RoutingReplayRouteEventIDL
        self._processMap['OnepEvent_VrfStatusEventIDL'] = Processor.process_OnepEvent_VrfStatusEventIDL



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



    def process_OnepEvent_L3UcastRibRouteEventIDL(self, seqid, iprot, oprot):
        args = OnepEvent_L3UcastRibRouteEventIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        self._handler.OnepEvent_L3UcastRibRouteEventIDL(args.base, args.ribState)



    def process_OnepEvent_L3UcastARTRouteEventIDL(self, seqid, iprot, oprot):
        args = OnepEvent_L3UcastARTRouteEventIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        self._handler.OnepEvent_L3UcastARTRouteEventIDL(args.base, args.artState)



    def process_AsyncMsg_L3UcastARTRouteUpdateAsyncIDL(self, seqid, iprot, oprot):
        args = AsyncMsg_L3UcastARTRouteUpdateAsyncIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        self._handler.AsyncMsg_L3UcastARTRouteUpdateAsyncIDL(args.base, args.scope, args.opList, args.status)



    def process_OnepEvent_RoutingServiceStatusEventIDL(self, seqid, iprot, oprot):
        args = OnepEvent_RoutingServiceStatusEventIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        self._handler.OnepEvent_RoutingServiceStatusEventIDL(args.sessionHandle, args.eventHandle, args.routingService, args.status)



    def process_OnepEvent_RoutingReplayRouteEventIDL(self, seqid, iprot, oprot):
        args = OnepEvent_RoutingReplayRouteEventIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        self._handler.OnepEvent_RoutingReplayRouteEventIDL(args.sessionHandle, args.eventHandle, args.afi, args.safi, args.vrfName, args.topoName)



    def process_OnepEvent_VrfStatusEventIDL(self, seqid, iprot, oprot):
        args = OnepEvent_VrfStatusEventIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        self._handler.OnepEvent_VrfStatusEventIDL(args.sessionHandle, args.eventHandle, args.vrf, args.event_type)




class OnepEvent_L3UcastRibRouteEventIDL_args(object):
    """
    Attributes:
     - base
     - ribState
    """

    thrift_spec = (None, (1,
      TType.STRUCT,
      'base',
      (L3UcastRouteTableEventOutIDL, L3UcastRouteTableEventOutIDL.thrift_spec),
      None), (2,
      TType.I32,
      'ribState',
      None,
      None))

    def __init__(self, base = None, ribState = None):
        self.base = base
        self.ribState = ribState



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
                if ftype == TType.STRUCT:
                    self.base = L3UcastRouteTableEventOutIDL()
                    self.base.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.ribState = iprot.readI32()
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
        oprot.writeStructBegin('OnepEvent_L3UcastRibRouteEventIDL_args')
        if self.base != None:
            oprot.writeFieldBegin('base', TType.STRUCT, 1)
            self.base.write(oprot)
            oprot.writeFieldEnd()
        if self.ribState != None:
            oprot.writeFieldBegin('ribState', TType.I32, 2)
            oprot.writeI32(self.ribState)
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




class OnepEvent_L3UcastARTRouteEventIDL_args(object):
    """
    Attributes:
     - base
     - artState
    """

    thrift_spec = (None, (1,
      TType.STRUCT,
      'base',
      (L3UcastRouteTableEventOutIDL, L3UcastRouteTableEventOutIDL.thrift_spec),
      None), (2,
      TType.I32,
      'artState',
      None,
      None))

    def __init__(self, base = None, artState = None):
        self.base = base
        self.artState = artState



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
                if ftype == TType.STRUCT:
                    self.base = L3UcastRouteTableEventOutIDL()
                    self.base.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.artState = iprot.readI32()
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
        oprot.writeStructBegin('OnepEvent_L3UcastARTRouteEventIDL_args')
        if self.base != None:
            oprot.writeFieldBegin('base', TType.STRUCT, 1)
            self.base.write(oprot)
            oprot.writeFieldEnd()
        if self.artState != None:
            oprot.writeFieldBegin('artState', TType.I32, 2)
            oprot.writeI32(self.artState)
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




class AsyncMsg_L3UcastARTRouteUpdateAsyncIDL_args(object):
    """
    Attributes:
     - base
     - scope
     - opList
     - status
    """

    thrift_spec = (None,
     (1,
      TType.STRUCT,
      'base',
      (AsyncMessageIDL.ttypes.AsyncBaseOutIDL, AsyncMessageIDL.ttypes.AsyncBaseOutIDL.thrift_spec),
      None),
     (2,
      TType.STRUCT,
      'scope',
      (L3UcastScopeOutIDL, L3UcastScopeOutIDL.thrift_spec),
      None),
     (3,
      TType.LIST,
      'opList',
      (TType.STRUCT, (L3UcastRouteAppRouteTableOpOutIDL, L3UcastRouteAppRouteTableOpOutIDL.thrift_spec)),
      None),
     (4,
      TType.I32,
      'status',
      None,
      None))

    def __init__(self, base = None, scope = None, opList = None, status = None):
        self.base = base
        self.scope = scope
        self.opList = opList
        self.status = status



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
                if ftype == TType.STRUCT:
                    self.base = AsyncMessageIDL.ttypes.AsyncBaseOutIDL()
                    self.base.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.scope = L3UcastScopeOutIDL()
                    self.scope.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.LIST:
                    self.opList = []
                    (_etype17, _size14,) = iprot.readListBegin()
                    for _i18 in xrange(_size14):
                        _elem19 = L3UcastRouteAppRouteTableOpOutIDL()
                        _elem19.read(iprot)
                        self.opList.append(_elem19)

                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.status = iprot.readI32()
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
        oprot.writeStructBegin('AsyncMsg_L3UcastARTRouteUpdateAsyncIDL_args')
        if self.base != None:
            oprot.writeFieldBegin('base', TType.STRUCT, 1)
            self.base.write(oprot)
            oprot.writeFieldEnd()
        if self.scope != None:
            oprot.writeFieldBegin('scope', TType.STRUCT, 2)
            self.scope.write(oprot)
            oprot.writeFieldEnd()
        if self.opList != None:
            oprot.writeFieldBegin('opList', TType.LIST, 3)
            oprot.writeListBegin(TType.STRUCT, len(self.opList))
            for iter20 in self.opList:
                iter20.write(oprot)

            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.status != None:
            oprot.writeFieldBegin('status', TType.I32, 4)
            oprot.writeI32(self.status)
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




class OnepEvent_RoutingServiceStatusEventIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - eventHandle
     - routingService
     - status
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
      'routingService',
      None,
      None),
     (4,
      TType.I32,
      'status',
      None,
      None))

    def __init__(self, sessionHandle = None, eventHandle = None, routingService = None, status = None):
        self.sessionHandle = sessionHandle
        self.eventHandle = eventHandle
        self.routingService = routingService
        self.status = status



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
                    self.routingService = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.status = iprot.readI32()
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
        oprot.writeStructBegin('OnepEvent_RoutingServiceStatusEventIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.eventHandle != None:
            oprot.writeFieldBegin('eventHandle', TType.I32, 2)
            oprot.writeI32(self.eventHandle)
            oprot.writeFieldEnd()
        if self.routingService != None:
            oprot.writeFieldBegin('routingService', TType.I32, 3)
            oprot.writeI32(self.routingService)
            oprot.writeFieldEnd()
        if self.status != None:
            oprot.writeFieldBegin('status', TType.I32, 4)
            oprot.writeI32(self.status)
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




class OnepEvent_RoutingReplayRouteEventIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - eventHandle
     - afi
     - safi
     - vrfName
     - topoName
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
      'afi',
      None,
      None),
     (4,
      TType.I32,
      'safi',
      None,
      None),
     (5,
      TType.STRING,
      'vrfName',
      None,
      None),
     (6,
      TType.STRING,
      'topoName',
      None,
      None))

    def __init__(self, sessionHandle = None, eventHandle = None, afi = None, safi = None, vrfName = None, topoName = None):
        self.sessionHandle = sessionHandle
        self.eventHandle = eventHandle
        self.afi = afi
        self.safi = safi
        self.vrfName = vrfName
        self.topoName = topoName



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
                    self.afi = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.safi = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.vrfName = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRING:
                    self.topoName = iprot.readString()
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
        oprot.writeStructBegin('OnepEvent_RoutingReplayRouteEventIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.eventHandle != None:
            oprot.writeFieldBegin('eventHandle', TType.I32, 2)
            oprot.writeI32(self.eventHandle)
            oprot.writeFieldEnd()
        if self.afi != None:
            oprot.writeFieldBegin('afi', TType.I32, 3)
            oprot.writeI32(self.afi)
            oprot.writeFieldEnd()
        if self.safi != None:
            oprot.writeFieldBegin('safi', TType.I32, 4)
            oprot.writeI32(self.safi)
            oprot.writeFieldEnd()
        if self.vrfName != None:
            oprot.writeFieldBegin('vrfName', TType.STRING, 5)
            oprot.writeString(self.vrfName)
            oprot.writeFieldEnd()
        if self.topoName != None:
            oprot.writeFieldBegin('topoName', TType.STRING, 6)
            oprot.writeString(self.topoName)
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




class OnepEvent_VrfStatusEventIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - eventHandle
     - vrf
     - event_type
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
      TType.STRUCT,
      'vrf',
      (VrfEventIDL, VrfEventIDL.thrift_spec),
      None),
     (4,
      TType.I32,
      'event_type',
      None,
      None))

    def __init__(self, sessionHandle = None, eventHandle = None, vrf = None, event_type = None):
        self.sessionHandle = sessionHandle
        self.eventHandle = eventHandle
        self.vrf = vrf
        self.event_type = event_type



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
                if ftype == TType.STRUCT:
                    self.vrf = VrfEventIDL()
                    self.vrf.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.event_type = iprot.readI32()
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
        oprot.writeStructBegin('OnepEvent_VrfStatusEventIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.eventHandle != None:
            oprot.writeFieldBegin('eventHandle', TType.I32, 2)
            oprot.writeI32(self.eventHandle)
            oprot.writeFieldEnd()
        if self.vrf != None:
            oprot.writeFieldBegin('vrf', TType.STRUCT, 3)
            self.vrf.write(oprot)
            oprot.writeFieldEnd()
        if self.event_type != None:
            oprot.writeFieldBegin('event_type', TType.I32, 4)
            oprot.writeI32(self.event_type)
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
# 2015.02.05 17:20:06 IST
