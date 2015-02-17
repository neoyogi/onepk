# 2015.02.05 17:19:25 IST
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

    def Policy_submitPmapBulkIDL(self, sessionId, type, opList):
        """
            Submit a Pmap Op List - Sync
        
            Parameters:
             - sessionId
             - type
             - opList
            """
        pass



    def Policy_submitCmapBulkIDL(self, sessionId, type, opList):
        """
            Submit a Cmap Op List - Sync
        
            Parameters:
             - sessionId
             - type
             - opList
            """
        pass



    def Policy_submitPmapActivateIDL(self, sessionId, type, opList):
        """
            Submit a Pmap Activate List - Sync
        
            Parameters:
             - sessionId
             - type
             - opList
            """
        pass



    def Policy_submitPmapBulkAsyncIDL(self, sessionId, type, asyncHandle, opList):
        """
            Submit a Pmap Op List - Async
        
            Parameters:
             - sessionId
             - type
             - asyncHandle
             - opList
            """
        pass



    def Policy_submitCmapBulkAsyncIDL(self, sessionId, type, asyncHandle, opList):
        """
            Submit a Cmap Op List - Async
        
            Parameters:
             - sessionId
             - type
             - asyncHandle
             - opList
            """
        pass



    def Policy_submitPmapActivateAsyncIDL(self, sessionId, type, asyncHandle, opList):
        """
            Submit a Pmap Activate List - Async
        
            Parameters:
             - sessionId
             - type
             - asyncHandle
             - opList
            """
        pass



    def Policy_getGlobalCapIDL(self, sessionId):
        """
            Query Platform global capabilities
        
            Parameters:
             - sessionId
            """
        pass



    def Policy_getCapListIDL(self, sessionId):
        """
            ===================
            To be deprecated:
            ===================
            Query Platform table capabilities
            Deprecated when Global Capabilities
            is supported on all platforms.
        
            Parameters:
             - sessionId
            """
        pass




class Client(Iface):

    def __init__(self, iprot, oprot = None):
        self._iprot = self._oprot = iprot
        if oprot != None:
            self._oprot = oprot
        self._seqid = 0



    def Policy_submitPmapBulkIDL(self, sessionId, type, opList):
        """
            Submit a Pmap Op List - Sync
        
            Parameters:
             - sessionId
             - type
             - opList
            """
        self._oprot.rlock.acquire()
        try:
            self.send_Policy_submitPmapBulkIDL(sessionId, type, opList)
            result = self.recv_Policy_submitPmapBulkIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_Policy_submitPmapBulkIDL(self, sessionId, type, opList):
        self._oprot.writeMessageBegin('Policy_submitPmapBulkIDL', TMessageType.CALL, self._seqid)
        args = Policy_submitPmapBulkIDL_args()
        args.sessionId = sessionId
        args.type = type
        args.opList = opList
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_Policy_submitPmapBulkIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = Policy_submitPmapBulkIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'Policy_submitPmapBulkIDL failed: unknown result')



    def Policy_submitCmapBulkIDL(self, sessionId, type, opList):
        """
            Submit a Cmap Op List - Sync
        
            Parameters:
             - sessionId
             - type
             - opList
            """
        self._oprot.rlock.acquire()
        try:
            self.send_Policy_submitCmapBulkIDL(sessionId, type, opList)
            result = self.recv_Policy_submitCmapBulkIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_Policy_submitCmapBulkIDL(self, sessionId, type, opList):
        self._oprot.writeMessageBegin('Policy_submitCmapBulkIDL', TMessageType.CALL, self._seqid)
        args = Policy_submitCmapBulkIDL_args()
        args.sessionId = sessionId
        args.type = type
        args.opList = opList
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_Policy_submitCmapBulkIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = Policy_submitCmapBulkIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'Policy_submitCmapBulkIDL failed: unknown result')



    def Policy_submitPmapActivateIDL(self, sessionId, type, opList):
        """
            Submit a Pmap Activate List - Sync
        
            Parameters:
             - sessionId
             - type
             - opList
            """
        self._oprot.rlock.acquire()
        try:
            self.send_Policy_submitPmapActivateIDL(sessionId, type, opList)
            result = self.recv_Policy_submitPmapActivateIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_Policy_submitPmapActivateIDL(self, sessionId, type, opList):
        self._oprot.writeMessageBegin('Policy_submitPmapActivateIDL', TMessageType.CALL, self._seqid)
        args = Policy_submitPmapActivateIDL_args()
        args.sessionId = sessionId
        args.type = type
        args.opList = opList
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_Policy_submitPmapActivateIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = Policy_submitPmapActivateIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'Policy_submitPmapActivateIDL failed: unknown result')



    def Policy_submitPmapBulkAsyncIDL(self, sessionId, type, asyncHandle, opList):
        """
            Submit a Pmap Op List - Async
        
            Parameters:
             - sessionId
             - type
             - asyncHandle
             - opList
            """
        self._oprot.rlock.acquire()
        try:
            self.send_Policy_submitPmapBulkAsyncIDL(sessionId, type, asyncHandle, opList)
            result = self.recv_Policy_submitPmapBulkAsyncIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_Policy_submitPmapBulkAsyncIDL(self, sessionId, type, asyncHandle, opList):
        self._oprot.writeMessageBegin('Policy_submitPmapBulkAsyncIDL', TMessageType.CALL, self._seqid)
        args = Policy_submitPmapBulkAsyncIDL_args()
        args.sessionId = sessionId
        args.type = type
        args.asyncHandle = asyncHandle
        args.opList = opList
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_Policy_submitPmapBulkAsyncIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = Policy_submitPmapBulkAsyncIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'Policy_submitPmapBulkAsyncIDL failed: unknown result')



    def Policy_submitCmapBulkAsyncIDL(self, sessionId, type, asyncHandle, opList):
        """
            Submit a Cmap Op List - Async
        
            Parameters:
             - sessionId
             - type
             - asyncHandle
             - opList
            """
        self._oprot.rlock.acquire()
        try:
            self.send_Policy_submitCmapBulkAsyncIDL(sessionId, type, asyncHandle, opList)
            result = self.recv_Policy_submitCmapBulkAsyncIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_Policy_submitCmapBulkAsyncIDL(self, sessionId, type, asyncHandle, opList):
        self._oprot.writeMessageBegin('Policy_submitCmapBulkAsyncIDL', TMessageType.CALL, self._seqid)
        args = Policy_submitCmapBulkAsyncIDL_args()
        args.sessionId = sessionId
        args.type = type
        args.asyncHandle = asyncHandle
        args.opList = opList
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_Policy_submitCmapBulkAsyncIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = Policy_submitCmapBulkAsyncIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'Policy_submitCmapBulkAsyncIDL failed: unknown result')



    def Policy_submitPmapActivateAsyncIDL(self, sessionId, type, asyncHandle, opList):
        """
            Submit a Pmap Activate List - Async
        
            Parameters:
             - sessionId
             - type
             - asyncHandle
             - opList
            """
        self._oprot.rlock.acquire()
        try:
            self.send_Policy_submitPmapActivateAsyncIDL(sessionId, type, asyncHandle, opList)
            result = self.recv_Policy_submitPmapActivateAsyncIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_Policy_submitPmapActivateAsyncIDL(self, sessionId, type, asyncHandle, opList):
        self._oprot.writeMessageBegin('Policy_submitPmapActivateAsyncIDL', TMessageType.CALL, self._seqid)
        args = Policy_submitPmapActivateAsyncIDL_args()
        args.sessionId = sessionId
        args.type = type
        args.asyncHandle = asyncHandle
        args.opList = opList
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_Policy_submitPmapActivateAsyncIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = Policy_submitPmapActivateAsyncIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'Policy_submitPmapActivateAsyncIDL failed: unknown result')



    def Policy_getGlobalCapIDL(self, sessionId):
        """
            Query Platform global capabilities
        
            Parameters:
             - sessionId
            """
        self._oprot.rlock.acquire()
        try:
            self.send_Policy_getGlobalCapIDL(sessionId)
            result = self.recv_Policy_getGlobalCapIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_Policy_getGlobalCapIDL(self, sessionId):
        self._oprot.writeMessageBegin('Policy_getGlobalCapIDL', TMessageType.CALL, self._seqid)
        args = Policy_getGlobalCapIDL_args()
        args.sessionId = sessionId
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_Policy_getGlobalCapIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = Policy_getGlobalCapIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'Policy_getGlobalCapIDL failed: unknown result')



    def Policy_getCapListIDL(self, sessionId):
        """
            ===================
            To be deprecated:
            ===================
            Query Platform table capabilities
            Deprecated when Global Capabilities
            is supported on all platforms.
        
            Parameters:
             - sessionId
            """
        self._oprot.rlock.acquire()
        try:
            self.send_Policy_getCapListIDL(sessionId)
            result = self.recv_Policy_getCapListIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_Policy_getCapListIDL(self, sessionId):
        self._oprot.writeMessageBegin('Policy_getCapListIDL', TMessageType.CALL, self._seqid)
        args = Policy_getCapListIDL_args()
        args.sessionId = sessionId
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_Policy_getCapListIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = Policy_getCapListIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'Policy_getCapListIDL failed: unknown result')




class Processor(Iface, TProcessor):

    def __init__(self, handler):
        self._handler = handler
        self._processMap = {}
        self._processMap['Policy_submitPmapBulkIDL'] = Processor.process_Policy_submitPmapBulkIDL
        self._processMap['Policy_submitCmapBulkIDL'] = Processor.process_Policy_submitCmapBulkIDL
        self._processMap['Policy_submitPmapActivateIDL'] = Processor.process_Policy_submitPmapActivateIDL
        self._processMap['Policy_submitPmapBulkAsyncIDL'] = Processor.process_Policy_submitPmapBulkAsyncIDL
        self._processMap['Policy_submitCmapBulkAsyncIDL'] = Processor.process_Policy_submitCmapBulkAsyncIDL
        self._processMap['Policy_submitPmapActivateAsyncIDL'] = Processor.process_Policy_submitPmapActivateAsyncIDL
        self._processMap['Policy_getGlobalCapIDL'] = Processor.process_Policy_getGlobalCapIDL
        self._processMap['Policy_getCapListIDL'] = Processor.process_Policy_getCapListIDL



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



    def process_Policy_submitPmapBulkIDL(self, seqid, iprot, oprot):
        args = Policy_submitPmapBulkIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = Policy_submitPmapBulkIDL_result()
        try:
            result.success = self._handler.Policy_submitPmapBulkIDL(args.sessionId, args.type, args.opList)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('Policy_submitPmapBulkIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_Policy_submitCmapBulkIDL(self, seqid, iprot, oprot):
        args = Policy_submitCmapBulkIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = Policy_submitCmapBulkIDL_result()
        try:
            result.success = self._handler.Policy_submitCmapBulkIDL(args.sessionId, args.type, args.opList)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('Policy_submitCmapBulkIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_Policy_submitPmapActivateIDL(self, seqid, iprot, oprot):
        args = Policy_submitPmapActivateIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = Policy_submitPmapActivateIDL_result()
        try:
            result.success = self._handler.Policy_submitPmapActivateIDL(args.sessionId, args.type, args.opList)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('Policy_submitPmapActivateIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_Policy_submitPmapBulkAsyncIDL(self, seqid, iprot, oprot):
        args = Policy_submitPmapBulkAsyncIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = Policy_submitPmapBulkAsyncIDL_result()
        try:
            result.success = self._handler.Policy_submitPmapBulkAsyncIDL(args.sessionId, args.type, args.asyncHandle, args.opList)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('Policy_submitPmapBulkAsyncIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_Policy_submitCmapBulkAsyncIDL(self, seqid, iprot, oprot):
        args = Policy_submitCmapBulkAsyncIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = Policy_submitCmapBulkAsyncIDL_result()
        try:
            result.success = self._handler.Policy_submitCmapBulkAsyncIDL(args.sessionId, args.type, args.asyncHandle, args.opList)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('Policy_submitCmapBulkAsyncIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_Policy_submitPmapActivateAsyncIDL(self, seqid, iprot, oprot):
        args = Policy_submitPmapActivateAsyncIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = Policy_submitPmapActivateAsyncIDL_result()
        try:
            result.success = self._handler.Policy_submitPmapActivateAsyncIDL(args.sessionId, args.type, args.asyncHandle, args.opList)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('Policy_submitPmapActivateAsyncIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_Policy_getGlobalCapIDL(self, seqid, iprot, oprot):
        args = Policy_getGlobalCapIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = Policy_getGlobalCapIDL_result()
        try:
            result.success = self._handler.Policy_getGlobalCapIDL(args.sessionId)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('Policy_getGlobalCapIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_Policy_getCapListIDL(self, seqid, iprot, oprot):
        args = Policy_getCapListIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = Policy_getCapListIDL_result()
        try:
            result.success = self._handler.Policy_getCapListIDL(args.sessionId)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('Policy_getCapListIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()




class Policy_submitPmapBulkIDL_args(object):
    """
    Attributes:
     - sessionId
     - type
     - opList
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionId',
      None,
      None),
     (2,
      TType.I32,
      'type',
      None,
      None),
     (3,
      TType.LIST,
      'opList',
      (TType.STRUCT, (PmapIDL, PmapIDL.thrift_spec)),
      None))

    def __init__(self, sessionId = None, type = None, opList = None):
        self.sessionId = sessionId
        self.type = type
        self.opList = opList



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
                    self.sessionId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.LIST:
                    self.opList = []
                    (_etype332, _size329,) = iprot.readListBegin()
                    for _i333 in xrange(_size329):
                        _elem334 = PmapIDL()
                        _elem334.read(iprot)
                        self.opList.append(_elem334)

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
        oprot.writeStructBegin('Policy_submitPmapBulkIDL_args')
        if self.sessionId != None:
            oprot.writeFieldBegin('sessionId', TType.I32, 1)
            oprot.writeI32(self.sessionId)
            oprot.writeFieldEnd()
        if self.type != None:
            oprot.writeFieldBegin('type', TType.I32, 2)
            oprot.writeI32(self.type)
            oprot.writeFieldEnd()
        if self.opList != None:
            oprot.writeFieldBegin('opList', TType.LIST, 3)
            oprot.writeListBegin(TType.STRUCT, len(self.opList))
            for iter335 in self.opList:
                iter335.write(oprot)

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




class Policy_submitPmapBulkIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.LIST,
      'success',
      (TType.STRUCT, (PmapResultIDL, PmapResultIDL.thrift_spec)),
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
                    (_etype339, _size336,) = iprot.readListBegin()
                    for _i340 in xrange(_size336):
                        _elem341 = PmapResultIDL()
                        _elem341.read(iprot)
                        self.success.append(_elem341)

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
        oprot.writeStructBegin('Policy_submitPmapBulkIDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.STRUCT, len(self.success))
            for iter342 in self.success:
                iter342.write(oprot)

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




class Policy_submitCmapBulkIDL_args(object):
    """
    Attributes:
     - sessionId
     - type
     - opList
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionId',
      None,
      None),
     (2,
      TType.I32,
      'type',
      None,
      None),
     (3,
      TType.LIST,
      'opList',
      (TType.STRUCT, (CmapIDL, CmapIDL.thrift_spec)),
      None))

    def __init__(self, sessionId = None, type = None, opList = None):
        self.sessionId = sessionId
        self.type = type
        self.opList = opList



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
                    self.sessionId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.LIST:
                    self.opList = []
                    (_etype346, _size343,) = iprot.readListBegin()
                    for _i347 in xrange(_size343):
                        _elem348 = CmapIDL()
                        _elem348.read(iprot)
                        self.opList.append(_elem348)

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
        oprot.writeStructBegin('Policy_submitCmapBulkIDL_args')
        if self.sessionId != None:
            oprot.writeFieldBegin('sessionId', TType.I32, 1)
            oprot.writeI32(self.sessionId)
            oprot.writeFieldEnd()
        if self.type != None:
            oprot.writeFieldBegin('type', TType.I32, 2)
            oprot.writeI32(self.type)
            oprot.writeFieldEnd()
        if self.opList != None:
            oprot.writeFieldBegin('opList', TType.LIST, 3)
            oprot.writeListBegin(TType.STRUCT, len(self.opList))
            for iter349 in self.opList:
                iter349.write(oprot)

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




class Policy_submitCmapBulkIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.LIST,
      'success',
      (TType.STRUCT, (CmapResultIDL, CmapResultIDL.thrift_spec)),
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
                    (_etype353, _size350,) = iprot.readListBegin()
                    for _i354 in xrange(_size350):
                        _elem355 = CmapResultIDL()
                        _elem355.read(iprot)
                        self.success.append(_elem355)

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
        oprot.writeStructBegin('Policy_submitCmapBulkIDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.STRUCT, len(self.success))
            for iter356 in self.success:
                iter356.write(oprot)

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




class Policy_submitPmapActivateIDL_args(object):
    """
    Attributes:
     - sessionId
     - type
     - opList
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionId',
      None,
      None),
     (2,
      TType.I32,
      'type',
      None,
      None),
     (3,
      TType.LIST,
      'opList',
      (TType.STRUCT, (PmapActivateIDL, PmapActivateIDL.thrift_spec)),
      None))

    def __init__(self, sessionId = None, type = None, opList = None):
        self.sessionId = sessionId
        self.type = type
        self.opList = opList



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
                    self.sessionId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.LIST:
                    self.opList = []
                    (_etype360, _size357,) = iprot.readListBegin()
                    for _i361 in xrange(_size357):
                        _elem362 = PmapActivateIDL()
                        _elem362.read(iprot)
                        self.opList.append(_elem362)

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
        oprot.writeStructBegin('Policy_submitPmapActivateIDL_args')
        if self.sessionId != None:
            oprot.writeFieldBegin('sessionId', TType.I32, 1)
            oprot.writeI32(self.sessionId)
            oprot.writeFieldEnd()
        if self.type != None:
            oprot.writeFieldBegin('type', TType.I32, 2)
            oprot.writeI32(self.type)
            oprot.writeFieldEnd()
        if self.opList != None:
            oprot.writeFieldBegin('opList', TType.LIST, 3)
            oprot.writeListBegin(TType.STRUCT, len(self.opList))
            for iter363 in self.opList:
                iter363.write(oprot)

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




class Policy_submitPmapActivateIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.LIST,
      'success',
      (TType.STRUCT, (PolicyCommonTypes.ttypes.PmapActivateResultIDL, PolicyCommonTypes.ttypes.PmapActivateResultIDL.thrift_spec)),
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
                    (_etype367, _size364,) = iprot.readListBegin()
                    for _i368 in xrange(_size364):
                        _elem369 = PolicyCommonTypes.ttypes.PmapActivateResultIDL()
                        _elem369.read(iprot)
                        self.success.append(_elem369)

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
        oprot.writeStructBegin('Policy_submitPmapActivateIDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.STRUCT, len(self.success))
            for iter370 in self.success:
                iter370.write(oprot)

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




class Policy_submitPmapBulkAsyncIDL_args(object):
    """
    Attributes:
     - sessionId
     - type
     - asyncHandle
     - opList
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionId',
      None,
      None),
     (2,
      TType.I32,
      'type',
      None,
      None),
     (3,
      TType.I32,
      'asyncHandle',
      None,
      None),
     (4,
      TType.LIST,
      'opList',
      (TType.STRUCT, (PmapIDL, PmapIDL.thrift_spec)),
      None))

    def __init__(self, sessionId = None, type = None, asyncHandle = None, opList = None):
        self.sessionId = sessionId
        self.type = type
        self.asyncHandle = asyncHandle
        self.opList = opList



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
                    self.sessionId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.asyncHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.LIST:
                    self.opList = []
                    (_etype374, _size371,) = iprot.readListBegin()
                    for _i375 in xrange(_size371):
                        _elem376 = PmapIDL()
                        _elem376.read(iprot)
                        self.opList.append(_elem376)

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
        oprot.writeStructBegin('Policy_submitPmapBulkAsyncIDL_args')
        if self.sessionId != None:
            oprot.writeFieldBegin('sessionId', TType.I32, 1)
            oprot.writeI32(self.sessionId)
            oprot.writeFieldEnd()
        if self.type != None:
            oprot.writeFieldBegin('type', TType.I32, 2)
            oprot.writeI32(self.type)
            oprot.writeFieldEnd()
        if self.asyncHandle != None:
            oprot.writeFieldBegin('asyncHandle', TType.I32, 3)
            oprot.writeI32(self.asyncHandle)
            oprot.writeFieldEnd()
        if self.opList != None:
            oprot.writeFieldBegin('opList', TType.LIST, 4)
            oprot.writeListBegin(TType.STRUCT, len(self.opList))
            for iter377 in self.opList:
                iter377.write(oprot)

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




class Policy_submitPmapBulkAsyncIDL_result(object):
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
        oprot.writeStructBegin('Policy_submitPmapBulkAsyncIDL_result')
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




class Policy_submitCmapBulkAsyncIDL_args(object):
    """
    Attributes:
     - sessionId
     - type
     - asyncHandle
     - opList
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionId',
      None,
      None),
     (2,
      TType.I32,
      'type',
      None,
      None),
     (3,
      TType.I32,
      'asyncHandle',
      None,
      None),
     (4,
      TType.LIST,
      'opList',
      (TType.STRUCT, (CmapIDL, CmapIDL.thrift_spec)),
      None))

    def __init__(self, sessionId = None, type = None, asyncHandle = None, opList = None):
        self.sessionId = sessionId
        self.type = type
        self.asyncHandle = asyncHandle
        self.opList = opList



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
                    self.sessionId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.asyncHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.LIST:
                    self.opList = []
                    (_etype381, _size378,) = iprot.readListBegin()
                    for _i382 in xrange(_size378):
                        _elem383 = CmapIDL()
                        _elem383.read(iprot)
                        self.opList.append(_elem383)

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
        oprot.writeStructBegin('Policy_submitCmapBulkAsyncIDL_args')
        if self.sessionId != None:
            oprot.writeFieldBegin('sessionId', TType.I32, 1)
            oprot.writeI32(self.sessionId)
            oprot.writeFieldEnd()
        if self.type != None:
            oprot.writeFieldBegin('type', TType.I32, 2)
            oprot.writeI32(self.type)
            oprot.writeFieldEnd()
        if self.asyncHandle != None:
            oprot.writeFieldBegin('asyncHandle', TType.I32, 3)
            oprot.writeI32(self.asyncHandle)
            oprot.writeFieldEnd()
        if self.opList != None:
            oprot.writeFieldBegin('opList', TType.LIST, 4)
            oprot.writeListBegin(TType.STRUCT, len(self.opList))
            for iter384 in self.opList:
                iter384.write(oprot)

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




class Policy_submitCmapBulkAsyncIDL_result(object):
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
        oprot.writeStructBegin('Policy_submitCmapBulkAsyncIDL_result')
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




class Policy_submitPmapActivateAsyncIDL_args(object):
    """
    Attributes:
     - sessionId
     - type
     - asyncHandle
     - opList
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionId',
      None,
      None),
     (2,
      TType.I32,
      'type',
      None,
      None),
     (3,
      TType.I32,
      'asyncHandle',
      None,
      None),
     (4,
      TType.LIST,
      'opList',
      (TType.STRUCT, (PmapActivateIDL, PmapActivateIDL.thrift_spec)),
      None))

    def __init__(self, sessionId = None, type = None, asyncHandle = None, opList = None):
        self.sessionId = sessionId
        self.type = type
        self.asyncHandle = asyncHandle
        self.opList = opList



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
                    self.sessionId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.asyncHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.LIST:
                    self.opList = []
                    (_etype388, _size385,) = iprot.readListBegin()
                    for _i389 in xrange(_size385):
                        _elem390 = PmapActivateIDL()
                        _elem390.read(iprot)
                        self.opList.append(_elem390)

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
        oprot.writeStructBegin('Policy_submitPmapActivateAsyncIDL_args')
        if self.sessionId != None:
            oprot.writeFieldBegin('sessionId', TType.I32, 1)
            oprot.writeI32(self.sessionId)
            oprot.writeFieldEnd()
        if self.type != None:
            oprot.writeFieldBegin('type', TType.I32, 2)
            oprot.writeI32(self.type)
            oprot.writeFieldEnd()
        if self.asyncHandle != None:
            oprot.writeFieldBegin('asyncHandle', TType.I32, 3)
            oprot.writeI32(self.asyncHandle)
            oprot.writeFieldEnd()
        if self.opList != None:
            oprot.writeFieldBegin('opList', TType.LIST, 4)
            oprot.writeListBegin(TType.STRUCT, len(self.opList))
            for iter391 in self.opList:
                iter391.write(oprot)

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




class Policy_submitPmapActivateAsyncIDL_result(object):
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
        oprot.writeStructBegin('Policy_submitPmapActivateAsyncIDL_result')
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




class Policy_getGlobalCapIDL_args(object):
    """
    Attributes:
     - sessionId
    """

    thrift_spec = (None, (1,
      TType.I32,
      'sessionId',
      None,
      None))

    def __init__(self, sessionId = None):
        self.sessionId = sessionId



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
                    self.sessionId = iprot.readI32()
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
        oprot.writeStructBegin('Policy_getGlobalCapIDL_args')
        if self.sessionId != None:
            oprot.writeFieldBegin('sessionId', TType.I32, 1)
            oprot.writeI32(self.sessionId)
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




class Policy_getGlobalCapIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.STRUCT,
      'success',
      (PssGlobalCapIDL, PssGlobalCapIDL.thrift_spec),
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
                    self.success = PssGlobalCapIDL()
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
        oprot.writeStructBegin('Policy_getGlobalCapIDL_result')
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




class Policy_getCapListIDL_args(object):
    """
    Attributes:
     - sessionId
    """

    thrift_spec = (None, (1,
      TType.I32,
      'sessionId',
      None,
      None))

    def __init__(self, sessionId = None):
        self.sessionId = sessionId



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
                    self.sessionId = iprot.readI32()
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
        oprot.writeStructBegin('Policy_getCapListIDL_args')
        if self.sessionId != None:
            oprot.writeFieldBegin('sessionId', TType.I32, 1)
            oprot.writeI32(self.sessionId)
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




class Policy_getCapListIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.LIST,
      'success',
      (TType.I16, None),
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
                    (_etype395, _size392,) = iprot.readListBegin()
                    for _i396 in xrange(_size392):
                        _elem397 = iprot.readI16()
                        self.success.append(_elem397)

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
        oprot.writeStructBegin('Policy_getCapListIDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.I16, len(self.success))
            for iter398 in self.success:
                oprot.writeI16(iter398)

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




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:19:26 IST
