# 2015.02.05 17:20:50 IST
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

    def Cert_TrustPointGetInfoIDL(self, sessionHandle, TrustPointName, info_filter):
        """
            ==============================================
            Get Certificate Info Async API
            ==============================================
        
            Parameters:
             - sessionHandle
             - TrustPointName
             - info_filter
            """
        pass



    def Certificate_Event_registerIDL(self, sessionHandle, TrustPointName, info_filter):
        """
            ==============================================
            Event listener API
            ==============================================
        
            Parameters:
             - sessionHandle
             - TrustPointName
             - info_filter
            """
        pass



    def Cert_TrustPointSetInfoIDL(self, TrustPointName, action, SetInfo):
        """
            ==============================================
            Write Certificate Info Async API
            ==============================================
        
            Parameters:
             - TrustPointName
             - action
             - SetInfo
            """
        pass



    def Cert_TrustPointSetInfoSyncIDL(self, TrustPointName, action, SetInfo):
        """
            ==============================================
            Write Certificate Info Sync API
            ==============================================
        
            Parameters:
             - TrustPointName
             - action
             - SetInfo
            """
        pass



    def Cert_TrustPointGetInfoSyncIDL(self, TrustPointName, TrustPoint):
        """
            ==============================================
            Get Certificate Info Sync API
            ==============================================
        
            Parameters:
             - TrustPointName
             - TrustPoint
            """
        pass




class Client(Iface):

    def __init__(self, iprot, oprot = None):
        self._iprot = self._oprot = iprot
        if oprot != None:
            self._oprot = oprot
        self._seqid = 0



    def Cert_TrustPointGetInfoIDL(self, sessionHandle, TrustPointName, info_filter):
        """
            ==============================================
            Get Certificate Info Async API
            ==============================================
        
            Parameters:
             - sessionHandle
             - TrustPointName
             - info_filter
            """
        self._oprot.rlock.acquire()
        try:
            self.send_Cert_TrustPointGetInfoIDL(sessionHandle, TrustPointName, info_filter)
            result = self.recv_Cert_TrustPointGetInfoIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_Cert_TrustPointGetInfoIDL(self, sessionHandle, TrustPointName, info_filter):
        self._oprot.writeMessageBegin('Cert_TrustPointGetInfoIDL', TMessageType.CALL, self._seqid)
        args = Cert_TrustPointGetInfoIDL_args()
        args.sessionHandle = sessionHandle
        args.TrustPointName = TrustPointName
        args.info_filter = info_filter
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_Cert_TrustPointGetInfoIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = Cert_TrustPointGetInfoIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'Cert_TrustPointGetInfoIDL failed: unknown result')



    def Certificate_Event_registerIDL(self, sessionHandle, TrustPointName, info_filter):
        """
            ==============================================
            Event listener API
            ==============================================
        
            Parameters:
             - sessionHandle
             - TrustPointName
             - info_filter
            """
        self._oprot.rlock.acquire()
        try:
            self.send_Certificate_Event_registerIDL(sessionHandle, TrustPointName, info_filter)
            result = self.recv_Certificate_Event_registerIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_Certificate_Event_registerIDL(self, sessionHandle, TrustPointName, info_filter):
        self._oprot.writeMessageBegin('Certificate_Event_registerIDL', TMessageType.CALL, self._seqid)
        args = Certificate_Event_registerIDL_args()
        args.sessionHandle = sessionHandle
        args.TrustPointName = TrustPointName
        args.info_filter = info_filter
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_Certificate_Event_registerIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = Certificate_Event_registerIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'Certificate_Event_registerIDL failed: unknown result')



    def Cert_TrustPointSetInfoIDL(self, TrustPointName, action, SetInfo):
        """
            ==============================================
            Write Certificate Info Async API
            ==============================================
        
            Parameters:
             - TrustPointName
             - action
             - SetInfo
            """
        self._oprot.rlock.acquire()
        try:
            self.send_Cert_TrustPointSetInfoIDL(TrustPointName, action, SetInfo)
            result = self.recv_Cert_TrustPointSetInfoIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_Cert_TrustPointSetInfoIDL(self, TrustPointName, action, SetInfo):
        self._oprot.writeMessageBegin('Cert_TrustPointSetInfoIDL', TMessageType.CALL, self._seqid)
        args = Cert_TrustPointSetInfoIDL_args()
        args.TrustPointName = TrustPointName
        args.action = action
        args.SetInfo = SetInfo
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_Cert_TrustPointSetInfoIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = Cert_TrustPointSetInfoIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'Cert_TrustPointSetInfoIDL failed: unknown result')



    def Cert_TrustPointSetInfoSyncIDL(self, TrustPointName, action, SetInfo):
        """
            ==============================================
            Write Certificate Info Sync API
            ==============================================
        
            Parameters:
             - TrustPointName
             - action
             - SetInfo
            """
        self._oprot.rlock.acquire()
        try:
            self.send_Cert_TrustPointSetInfoSyncIDL(TrustPointName, action, SetInfo)
            result = self.recv_Cert_TrustPointSetInfoSyncIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_Cert_TrustPointSetInfoSyncIDL(self, TrustPointName, action, SetInfo):
        self._oprot.writeMessageBegin('Cert_TrustPointSetInfoSyncIDL', TMessageType.CALL, self._seqid)
        args = Cert_TrustPointSetInfoSyncIDL_args()
        args.TrustPointName = TrustPointName
        args.action = action
        args.SetInfo = SetInfo
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_Cert_TrustPointSetInfoSyncIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = Cert_TrustPointSetInfoSyncIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'Cert_TrustPointSetInfoSyncIDL failed: unknown result')



    def Cert_TrustPointGetInfoSyncIDL(self, TrustPointName, TrustPoint):
        """
            ==============================================
            Get Certificate Info Sync API
            ==============================================
        
            Parameters:
             - TrustPointName
             - TrustPoint
            """
        self._oprot.rlock.acquire()
        try:
            self.send_Cert_TrustPointGetInfoSyncIDL(TrustPointName, TrustPoint)
            result = self.recv_Cert_TrustPointGetInfoSyncIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_Cert_TrustPointGetInfoSyncIDL(self, TrustPointName, TrustPoint):
        self._oprot.writeMessageBegin('Cert_TrustPointGetInfoSyncIDL', TMessageType.CALL, self._seqid)
        args = Cert_TrustPointGetInfoSyncIDL_args()
        args.TrustPointName = TrustPointName
        args.TrustPoint = TrustPoint
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_Cert_TrustPointGetInfoSyncIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = Cert_TrustPointGetInfoSyncIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'Cert_TrustPointGetInfoSyncIDL failed: unknown result')




class Processor(Iface, TProcessor):

    def __init__(self, handler):
        self._handler = handler
        self._processMap = {}
        self._processMap['Cert_TrustPointGetInfoIDL'] = Processor.process_Cert_TrustPointGetInfoIDL
        self._processMap['Certificate_Event_registerIDL'] = Processor.process_Certificate_Event_registerIDL
        self._processMap['Cert_TrustPointSetInfoIDL'] = Processor.process_Cert_TrustPointSetInfoIDL
        self._processMap['Cert_TrustPointSetInfoSyncIDL'] = Processor.process_Cert_TrustPointSetInfoSyncIDL
        self._processMap['Cert_TrustPointGetInfoSyncIDL'] = Processor.process_Cert_TrustPointGetInfoSyncIDL



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



    def process_Cert_TrustPointGetInfoIDL(self, seqid, iprot, oprot):
        args = Cert_TrustPointGetInfoIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = Cert_TrustPointGetInfoIDL_result()
        try:
            result.success = self._handler.Cert_TrustPointGetInfoIDL(args.sessionHandle, args.TrustPointName, args.info_filter)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('Cert_TrustPointGetInfoIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_Certificate_Event_registerIDL(self, seqid, iprot, oprot):
        args = Certificate_Event_registerIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = Certificate_Event_registerIDL_result()
        try:
            result.success = self._handler.Certificate_Event_registerIDL(args.sessionHandle, args.TrustPointName, args.info_filter)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('Certificate_Event_registerIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_Cert_TrustPointSetInfoIDL(self, seqid, iprot, oprot):
        args = Cert_TrustPointSetInfoIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = Cert_TrustPointSetInfoIDL_result()
        try:
            result.success = self._handler.Cert_TrustPointSetInfoIDL(args.TrustPointName, args.action, args.SetInfo)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('Cert_TrustPointSetInfoIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_Cert_TrustPointSetInfoSyncIDL(self, seqid, iprot, oprot):
        args = Cert_TrustPointSetInfoSyncIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = Cert_TrustPointSetInfoSyncIDL_result()
        try:
            result.success = self._handler.Cert_TrustPointSetInfoSyncIDL(args.TrustPointName, args.action, args.SetInfo)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('Cert_TrustPointSetInfoSyncIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_Cert_TrustPointGetInfoSyncIDL(self, seqid, iprot, oprot):
        args = Cert_TrustPointGetInfoSyncIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = Cert_TrustPointGetInfoSyncIDL_result()
        try:
            result.success = self._handler.Cert_TrustPointGetInfoSyncIDL(args.TrustPointName, args.TrustPoint)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('Cert_TrustPointGetInfoSyncIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()




class Cert_TrustPointGetInfoIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - TrustPointName
     - info_filter
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionHandle',
      None,
      None),
     (2,
      TType.STRING,
      'TrustPointName',
      None,
      None),
     (3,
      TType.I32,
      'info_filter',
      None,
      None))

    def __init__(self, sessionHandle = None, TrustPointName = None, info_filter = None):
        self.sessionHandle = sessionHandle
        self.TrustPointName = TrustPointName
        self.info_filter = info_filter



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
                    self.TrustPointName = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.info_filter = iprot.readI32()
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
        oprot.writeStructBegin('Cert_TrustPointGetInfoIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.TrustPointName != None:
            oprot.writeFieldBegin('TrustPointName', TType.STRING, 2)
            oprot.writeString(self.TrustPointName)
            oprot.writeFieldEnd()
        if self.info_filter != None:
            oprot.writeFieldBegin('info_filter', TType.I32, 3)
            oprot.writeI32(self.info_filter)
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




class Cert_TrustPointGetInfoIDL_result(object):
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
        oprot.writeStructBegin('Cert_TrustPointGetInfoIDL_result')
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




class Certificate_Event_registerIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - TrustPointName
     - info_filter
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionHandle',
      None,
      None),
     (2,
      TType.STRING,
      'TrustPointName',
      None,
      None),
     (3,
      TType.I32,
      'info_filter',
      None,
      None))

    def __init__(self, sessionHandle = None, TrustPointName = None, info_filter = None):
        self.sessionHandle = sessionHandle
        self.TrustPointName = TrustPointName
        self.info_filter = info_filter



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
                    self.TrustPointName = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.info_filter = iprot.readI32()
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
        oprot.writeStructBegin('Certificate_Event_registerIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.TrustPointName != None:
            oprot.writeFieldBegin('TrustPointName', TType.STRING, 2)
            oprot.writeString(self.TrustPointName)
            oprot.writeFieldEnd()
        if self.info_filter != None:
            oprot.writeFieldBegin('info_filter', TType.I32, 3)
            oprot.writeI32(self.info_filter)
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




class Certificate_Event_registerIDL_result(object):
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
        oprot.writeStructBegin('Certificate_Event_registerIDL_result')
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




class Cert_TrustPointSetInfoIDL_args(object):
    """
    Attributes:
     - TrustPointName
     - action
     - SetInfo
    """

    thrift_spec = (None,
     (1,
      TType.STRING,
      'TrustPointName',
      None,
      None),
     (2,
      TType.I32,
      'action',
      None,
      None),
     (3,
      TType.STRUCT,
      'SetInfo',
      (CertTrustpointInfoInIDL, CertTrustpointInfoInIDL.thrift_spec),
      None))

    def __init__(self, TrustPointName = None, action = None, SetInfo = None):
        self.TrustPointName = TrustPointName
        self.action = action
        self.SetInfo = SetInfo



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
                    self.TrustPointName = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.action = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRUCT:
                    self.SetInfo = CertTrustpointInfoInIDL()
                    self.SetInfo.read(iprot)
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
        oprot.writeStructBegin('Cert_TrustPointSetInfoIDL_args')
        if self.TrustPointName != None:
            oprot.writeFieldBegin('TrustPointName', TType.STRING, 1)
            oprot.writeString(self.TrustPointName)
            oprot.writeFieldEnd()
        if self.action != None:
            oprot.writeFieldBegin('action', TType.I32, 2)
            oprot.writeI32(self.action)
            oprot.writeFieldEnd()
        if self.SetInfo != None:
            oprot.writeFieldBegin('SetInfo', TType.STRUCT, 3)
            self.SetInfo.write(oprot)
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




class Cert_TrustPointSetInfoIDL_result(object):
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
        oprot.writeStructBegin('Cert_TrustPointSetInfoIDL_result')
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




class Cert_TrustPointSetInfoSyncIDL_args(object):
    """
    Attributes:
     - TrustPointName
     - action
     - SetInfo
    """

    thrift_spec = (None,
     (1,
      TType.STRING,
      'TrustPointName',
      None,
      None),
     (2,
      TType.I32,
      'action',
      None,
      None),
     (3,
      TType.STRUCT,
      'SetInfo',
      (CertTrustpointInfoInIDL, CertTrustpointInfoInIDL.thrift_spec),
      None))

    def __init__(self, TrustPointName = None, action = None, SetInfo = None):
        self.TrustPointName = TrustPointName
        self.action = action
        self.SetInfo = SetInfo



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
                    self.TrustPointName = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.action = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRUCT:
                    self.SetInfo = CertTrustpointInfoInIDL()
                    self.SetInfo.read(iprot)
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
        oprot.writeStructBegin('Cert_TrustPointSetInfoSyncIDL_args')
        if self.TrustPointName != None:
            oprot.writeFieldBegin('TrustPointName', TType.STRING, 1)
            oprot.writeString(self.TrustPointName)
            oprot.writeFieldEnd()
        if self.action != None:
            oprot.writeFieldBegin('action', TType.I32, 2)
            oprot.writeI32(self.action)
            oprot.writeFieldEnd()
        if self.SetInfo != None:
            oprot.writeFieldBegin('SetInfo', TType.STRUCT, 3)
            self.SetInfo.write(oprot)
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




class Cert_TrustPointSetInfoSyncIDL_result(object):
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
        oprot.writeStructBegin('Cert_TrustPointSetInfoSyncIDL_result')
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




class Cert_TrustPointGetInfoSyncIDL_args(object):
    """
    Attributes:
     - TrustPointName
     - TrustPoint
    """

    thrift_spec = (None, (1,
      TType.STRING,
      'TrustPointName',
      None,
      None), (2,
      TType.STRUCT,
      'TrustPoint',
      (CertTrustpointInfoInIDL, CertTrustpointInfoInIDL.thrift_spec),
      None))

    def __init__(self, TrustPointName = None, TrustPoint = None):
        self.TrustPointName = TrustPointName
        self.TrustPoint = TrustPoint



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
                    self.TrustPointName = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.TrustPoint = CertTrustpointInfoInIDL()
                    self.TrustPoint.read(iprot)
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
        oprot.writeStructBegin('Cert_TrustPointGetInfoSyncIDL_args')
        if self.TrustPointName != None:
            oprot.writeFieldBegin('TrustPointName', TType.STRING, 1)
            oprot.writeString(self.TrustPointName)
            oprot.writeFieldEnd()
        if self.TrustPoint != None:
            oprot.writeFieldBegin('TrustPoint', TType.STRUCT, 2)
            self.TrustPoint.write(oprot)
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




class Cert_TrustPointGetInfoSyncIDL_result(object):
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
        oprot.writeStructBegin('Cert_TrustPointGetInfoSyncIDL_result')
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




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:20:51 IST
