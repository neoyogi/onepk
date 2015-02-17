# 2015.02.05 17:17:57 IST
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

    def AsyncMsg_Cert_TrustPointGetInfoIDL(self, base, TrustPointName, result, InfoRsp):
        """
            ==============================================
            Certificate Get Info Async API Response
            ==============================================
        
            Parameters:
             - base
             - TrustPointName
             - result
             - InfoRsp
            """
        pass



    def OnepEvent_CertificateChangeEventIDL(self, sessionID, eventHandle, TrustPointName, eventType, EvtRspIDL):
        """
            ==============================================
            Event notification
            ==============================================
        
            Parameters:
             - sessionID
             - eventHandle
             - TrustPointName
             - eventType
             - EvtRspIDL
            """
        pass



    def AsyncMsg_Cert_TrustPointSetInfoRspIDL(self, base, TrustPointName, result):
        """
            ==============================================
            Set Info response
            ==============================================
        
            Parameters:
             - base
             - TrustPointName
             - result
            """
        pass




class Client(Iface):

    def __init__(self, iprot, oprot = None):
        self._iprot = self._oprot = iprot
        if oprot != None:
            self._oprot = oprot
        self._seqid = 0



    def AsyncMsg_Cert_TrustPointGetInfoIDL(self, base, TrustPointName, result, InfoRsp):
        """
            ==============================================
            Certificate Get Info Async API Response
            ==============================================
        
            Parameters:
             - base
             - TrustPointName
             - result
             - InfoRsp
            """
        self._oprot.rlock.acquire()
        try:
            self.send_AsyncMsg_Cert_TrustPointGetInfoIDL(base, TrustPointName, result, InfoRsp)
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()



    def send_AsyncMsg_Cert_TrustPointGetInfoIDL(self, base, TrustPointName, result, InfoRsp):
        self._oprot.writeMessageBegin('AsyncMsg_Cert_TrustPointGetInfoIDL', TMessageType.CALL, self._seqid)
        args = AsyncMsg_Cert_TrustPointGetInfoIDL_args()
        args.base = base
        args.TrustPointName = TrustPointName
        args.result = result
        args.InfoRsp = InfoRsp
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def OnepEvent_CertificateChangeEventIDL(self, sessionID, eventHandle, TrustPointName, eventType, EvtRspIDL):
        """
            ==============================================
            Event notification
            ==============================================
        
            Parameters:
             - sessionID
             - eventHandle
             - TrustPointName
             - eventType
             - EvtRspIDL
            """
        self._oprot.rlock.acquire()
        try:
            self.send_OnepEvent_CertificateChangeEventIDL(sessionID, eventHandle, TrustPointName, eventType, EvtRspIDL)
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()



    def send_OnepEvent_CertificateChangeEventIDL(self, sessionID, eventHandle, TrustPointName, eventType, EvtRspIDL):
        self._oprot.writeMessageBegin('OnepEvent_CertificateChangeEventIDL', TMessageType.CALL, self._seqid)
        args = OnepEvent_CertificateChangeEventIDL_args()
        args.sessionID = sessionID
        args.eventHandle = eventHandle
        args.TrustPointName = TrustPointName
        args.eventType = eventType
        args.EvtRspIDL = EvtRspIDL
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def AsyncMsg_Cert_TrustPointSetInfoRspIDL(self, base, TrustPointName, result):
        """
            ==============================================
            Set Info response
            ==============================================
        
            Parameters:
             - base
             - TrustPointName
             - result
            """
        self._oprot.rlock.acquire()
        try:
            self.send_AsyncMsg_Cert_TrustPointSetInfoRspIDL(base, TrustPointName, result)
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()



    def send_AsyncMsg_Cert_TrustPointSetInfoRspIDL(self, base, TrustPointName, result):
        self._oprot.writeMessageBegin('AsyncMsg_Cert_TrustPointSetInfoRspIDL', TMessageType.CALL, self._seqid)
        args = AsyncMsg_Cert_TrustPointSetInfoRspIDL_args()
        args.base = base
        args.TrustPointName = TrustPointName
        args.result = result
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()




class Processor(Iface, TProcessor):

    def __init__(self, handler):
        self._handler = handler
        self._processMap = {}
        self._processMap['AsyncMsg_Cert_TrustPointGetInfoIDL'] = Processor.process_AsyncMsg_Cert_TrustPointGetInfoIDL
        self._processMap['OnepEvent_CertificateChangeEventIDL'] = Processor.process_OnepEvent_CertificateChangeEventIDL
        self._processMap['AsyncMsg_Cert_TrustPointSetInfoRspIDL'] = Processor.process_AsyncMsg_Cert_TrustPointSetInfoRspIDL



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



    def process_AsyncMsg_Cert_TrustPointGetInfoIDL(self, seqid, iprot, oprot):
        args = AsyncMsg_Cert_TrustPointGetInfoIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        self._handler.AsyncMsg_Cert_TrustPointGetInfoIDL(args.base, args.TrustPointName, args.result, args.InfoRsp)



    def process_OnepEvent_CertificateChangeEventIDL(self, seqid, iprot, oprot):
        args = OnepEvent_CertificateChangeEventIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        self._handler.OnepEvent_CertificateChangeEventIDL(args.sessionID, args.eventHandle, args.TrustPointName, args.eventType, args.EvtRspIDL)



    def process_AsyncMsg_Cert_TrustPointSetInfoRspIDL(self, seqid, iprot, oprot):
        args = AsyncMsg_Cert_TrustPointSetInfoRspIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        self._handler.AsyncMsg_Cert_TrustPointSetInfoRspIDL(args.base, args.TrustPointName, args.result)




class AsyncMsg_Cert_TrustPointGetInfoIDL_args(object):
    """
    Attributes:
     - base
     - TrustPointName
     - result
     - InfoRsp
    """

    thrift_spec = (None,
     (1,
      TType.STRUCT,
      'base',
      (AsyncMessageIDL.ttypes.AsyncBaseOutIDL, AsyncMessageIDL.ttypes.AsyncBaseOutIDL.thrift_spec),
      None),
     (2,
      TType.STRING,
      'TrustPointName',
      None,
      None),
     (3,
      TType.I32,
      'result',
      None,
      None),
     (4,
      TType.STRUCT,
      'InfoRsp',
      (CertTrustpointInfoIDL, CertTrustpointInfoIDL.thrift_spec),
      None))

    def __init__(self, base = None, TrustPointName = None, result = None, InfoRsp = None):
        self.base = base
        self.TrustPointName = TrustPointName
        self.result = result
        self.InfoRsp = InfoRsp



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
                if ftype == TType.STRING:
                    self.TrustPointName = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.result = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRUCT:
                    self.InfoRsp = CertTrustpointInfoIDL()
                    self.InfoRsp.read(iprot)
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
        oprot.writeStructBegin('AsyncMsg_Cert_TrustPointGetInfoIDL_args')
        if self.base != None:
            oprot.writeFieldBegin('base', TType.STRUCT, 1)
            self.base.write(oprot)
            oprot.writeFieldEnd()
        if self.TrustPointName != None:
            oprot.writeFieldBegin('TrustPointName', TType.STRING, 2)
            oprot.writeString(self.TrustPointName)
            oprot.writeFieldEnd()
        if self.result != None:
            oprot.writeFieldBegin('result', TType.I32, 3)
            oprot.writeI32(self.result)
            oprot.writeFieldEnd()
        if self.InfoRsp != None:
            oprot.writeFieldBegin('InfoRsp', TType.STRUCT, 4)
            self.InfoRsp.write(oprot)
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




class OnepEvent_CertificateChangeEventIDL_args(object):
    """
    Attributes:
     - sessionID
     - eventHandle
     - TrustPointName
     - eventType
     - EvtRspIDL
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionID',
      None,
      None),
     (2,
      TType.I32,
      'eventHandle',
      None,
      None),
     (3,
      TType.STRING,
      'TrustPointName',
      None,
      None),
     (4,
      TType.I32,
      'eventType',
      None,
      None),
     (5,
      TType.STRUCT,
      'EvtRspIDL',
      (CertTrustpointInfoIDL, CertTrustpointInfoIDL.thrift_spec),
      None))

    def __init__(self, sessionID = None, eventHandle = None, TrustPointName = None, eventType = None, EvtRspIDL = None):
        self.sessionID = sessionID
        self.eventHandle = eventHandle
        self.TrustPointName = TrustPointName
        self.eventType = eventType
        self.EvtRspIDL = EvtRspIDL



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
                    self.sessionID = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.eventHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.TrustPointName = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.eventType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRUCT:
                    self.EvtRspIDL = CertTrustpointInfoIDL()
                    self.EvtRspIDL.read(iprot)
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
        oprot.writeStructBegin('OnepEvent_CertificateChangeEventIDL_args')
        if self.sessionID != None:
            oprot.writeFieldBegin('sessionID', TType.I32, 1)
            oprot.writeI32(self.sessionID)
            oprot.writeFieldEnd()
        if self.eventHandle != None:
            oprot.writeFieldBegin('eventHandle', TType.I32, 2)
            oprot.writeI32(self.eventHandle)
            oprot.writeFieldEnd()
        if self.TrustPointName != None:
            oprot.writeFieldBegin('TrustPointName', TType.STRING, 3)
            oprot.writeString(self.TrustPointName)
            oprot.writeFieldEnd()
        if self.eventType != None:
            oprot.writeFieldBegin('eventType', TType.I32, 4)
            oprot.writeI32(self.eventType)
            oprot.writeFieldEnd()
        if self.EvtRspIDL != None:
            oprot.writeFieldBegin('EvtRspIDL', TType.STRUCT, 5)
            self.EvtRspIDL.write(oprot)
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




class AsyncMsg_Cert_TrustPointSetInfoRspIDL_args(object):
    """
    Attributes:
     - base
     - TrustPointName
     - result
    """

    thrift_spec = (None,
     (1,
      TType.STRUCT,
      'base',
      (AsyncMessageIDL.ttypes.AsyncBaseOutIDL, AsyncMessageIDL.ttypes.AsyncBaseOutIDL.thrift_spec),
      None),
     (2,
      TType.STRING,
      'TrustPointName',
      None,
      None),
     (3,
      TType.I32,
      'result',
      None,
      None))

    def __init__(self, base = None, TrustPointName = None, result = None):
        self.base = base
        self.TrustPointName = TrustPointName
        self.result = result



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
                if ftype == TType.STRING:
                    self.TrustPointName = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.result = iprot.readI32()
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
        oprot.writeStructBegin('AsyncMsg_Cert_TrustPointSetInfoRspIDL_args')
        if self.base != None:
            oprot.writeFieldBegin('base', TType.STRUCT, 1)
            self.base.write(oprot)
            oprot.writeFieldEnd()
        if self.TrustPointName != None:
            oprot.writeFieldBegin('TrustPointName', TType.STRING, 2)
            oprot.writeString(self.TrustPointName)
            oprot.writeFieldEnd()
        if self.result != None:
            oprot.writeFieldBegin('result', TType.I32, 3)
            oprot.writeI32(self.result)
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
# 2015.02.05 17:17:58 IST
