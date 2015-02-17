# 2015.02.05 17:18:55 IST
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

    def NetworkElementTest_DeferredIDL(self, sessionHandle, test_delay_msec, disable_keepalives, test_message):
        """
            ---------------------------
            Send a test deferred results message.
            ---------------------------
        
            Parameters:
             - sessionHandle
             - test_delay_msec
             - disable_keepalives
             - test_message
            """
        pass



    def AsyncMsg_TestRegisterIDL(self, sessionHandle, test_id, op_id_offset):
        """
            ---------------------------
            Send a test async registration message.
            ---------------------------
        
            Parameters:
             - sessionHandle
             - test_id
             - op_id_offset
            """
        pass



    def NetworkElementTest_UtOpIDL(self, op_code, req_args):
        """
            ---------------------------
            Send a test unit test operation message.
            ---------------------------
        
            Parameters:
             - op_code
             - req_args
            """
        pass



    def NetworkElementTest_NullOutputIDL(self, op):
        """
            ---------------------------
            Tests NULL IDL output parameters
            ---------------------------
        
            Parameters:
             - op
            """
        pass




class Client(Iface):

    def __init__(self, iprot, oprot = None):
        self._iprot = self._oprot = iprot
        if oprot != None:
            self._oprot = oprot
        self._seqid = 0



    def NetworkElementTest_DeferredIDL(self, sessionHandle, test_delay_msec, disable_keepalives, test_message):
        """
            ---------------------------
            Send a test deferred results message.
            ---------------------------
        
            Parameters:
             - sessionHandle
             - test_delay_msec
             - disable_keepalives
             - test_message
            """
        self._oprot.rlock.acquire()
        try:
            self.send_NetworkElementTest_DeferredIDL(sessionHandle, test_delay_msec, disable_keepalives, test_message)
            result = self.recv_NetworkElementTest_DeferredIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_NetworkElementTest_DeferredIDL(self, sessionHandle, test_delay_msec, disable_keepalives, test_message):
        self._oprot.writeMessageBegin('NetworkElementTest_DeferredIDL', TMessageType.CALL, self._seqid)
        args = NetworkElementTest_DeferredIDL_args()
        args.sessionHandle = sessionHandle
        args.test_delay_msec = test_delay_msec
        args.disable_keepalives = disable_keepalives
        args.test_message = test_message
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_NetworkElementTest_DeferredIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = NetworkElementTest_DeferredIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'NetworkElementTest_DeferredIDL failed: unknown result')



    def AsyncMsg_TestRegisterIDL(self, sessionHandle, test_id, op_id_offset):
        """
            ---------------------------
            Send a test async registration message.
            ---------------------------
        
            Parameters:
             - sessionHandle
             - test_id
             - op_id_offset
            """
        self._oprot.rlock.acquire()
        try:
            self.send_AsyncMsg_TestRegisterIDL(sessionHandle, test_id, op_id_offset)
            result = self.recv_AsyncMsg_TestRegisterIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_AsyncMsg_TestRegisterIDL(self, sessionHandle, test_id, op_id_offset):
        self._oprot.writeMessageBegin('AsyncMsg_TestRegisterIDL', TMessageType.CALL, self._seqid)
        args = AsyncMsg_TestRegisterIDL_args()
        args.sessionHandle = sessionHandle
        args.test_id = test_id
        args.op_id_offset = op_id_offset
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_AsyncMsg_TestRegisterIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = AsyncMsg_TestRegisterIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'AsyncMsg_TestRegisterIDL failed: unknown result')



    def NetworkElementTest_UtOpIDL(self, op_code, req_args):
        """
            ---------------------------
            Send a test unit test operation message.
            ---------------------------
        
            Parameters:
             - op_code
             - req_args
            """
        self._oprot.rlock.acquire()
        try:
            self.send_NetworkElementTest_UtOpIDL(op_code, req_args)
            result = self.recv_NetworkElementTest_UtOpIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_NetworkElementTest_UtOpIDL(self, op_code, req_args):
        self._oprot.writeMessageBegin('NetworkElementTest_UtOpIDL', TMessageType.CALL, self._seqid)
        args = NetworkElementTest_UtOpIDL_args()
        args.op_code = op_code
        args.req_args = req_args
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_NetworkElementTest_UtOpIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = NetworkElementTest_UtOpIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'NetworkElementTest_UtOpIDL failed: unknown result')



    def NetworkElementTest_NullOutputIDL(self, op):
        """
            ---------------------------
            Tests NULL IDL output parameters
            ---------------------------
        
            Parameters:
             - op
            """
        self._oprot.rlock.acquire()
        try:
            self.send_NetworkElementTest_NullOutputIDL(op)
            result = self.recv_NetworkElementTest_NullOutputIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_NetworkElementTest_NullOutputIDL(self, op):
        self._oprot.writeMessageBegin('NetworkElementTest_NullOutputIDL', TMessageType.CALL, self._seqid)
        args = NetworkElementTest_NullOutputIDL_args()
        args.op = op
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_NetworkElementTest_NullOutputIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = NetworkElementTest_NullOutputIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'NetworkElementTest_NullOutputIDL failed: unknown result')




class Processor(Iface, TProcessor):

    def __init__(self, handler):
        self._handler = handler
        self._processMap = {}
        self._processMap['NetworkElementTest_DeferredIDL'] = Processor.process_NetworkElementTest_DeferredIDL
        self._processMap['AsyncMsg_TestRegisterIDL'] = Processor.process_AsyncMsg_TestRegisterIDL
        self._processMap['NetworkElementTest_UtOpIDL'] = Processor.process_NetworkElementTest_UtOpIDL
        self._processMap['NetworkElementTest_NullOutputIDL'] = Processor.process_NetworkElementTest_NullOutputIDL



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



    def process_NetworkElementTest_DeferredIDL(self, seqid, iprot, oprot):
        args = NetworkElementTest_DeferredIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = NetworkElementTest_DeferredIDL_result()
        try:
            result.success = self._handler.NetworkElementTest_DeferredIDL(args.sessionHandle, args.test_delay_msec, args.disable_keepalives, args.test_message)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('NetworkElementTest_DeferredIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_AsyncMsg_TestRegisterIDL(self, seqid, iprot, oprot):
        args = AsyncMsg_TestRegisterIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = AsyncMsg_TestRegisterIDL_result()
        try:
            result.success = self._handler.AsyncMsg_TestRegisterIDL(args.sessionHandle, args.test_id, args.op_id_offset)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('AsyncMsg_TestRegisterIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_NetworkElementTest_UtOpIDL(self, seqid, iprot, oprot):
        args = NetworkElementTest_UtOpIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = NetworkElementTest_UtOpIDL_result()
        try:
            result.success = self._handler.NetworkElementTest_UtOpIDL(args.op_code, args.req_args)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('NetworkElementTest_UtOpIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_NetworkElementTest_NullOutputIDL(self, seqid, iprot, oprot):
        args = NetworkElementTest_NullOutputIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = NetworkElementTest_NullOutputIDL_result()
        try:
            result.success = self._handler.NetworkElementTest_NullOutputIDL(args.op)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('NetworkElementTest_NullOutputIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()




class NetworkElementTest_DeferredIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - test_delay_msec
     - disable_keepalives
     - test_message
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionHandle',
      None,
      None),
     (2,
      TType.I32,
      'test_delay_msec',
      None,
      None),
     (3,
      TType.I32,
      'disable_keepalives',
      None,
      None),
     (4,
      TType.STRING,
      'test_message',
      None,
      None))

    def __init__(self, sessionHandle = None, test_delay_msec = None, disable_keepalives = None, test_message = None):
        self.sessionHandle = sessionHandle
        self.test_delay_msec = test_delay_msec
        self.disable_keepalives = disable_keepalives
        self.test_message = test_message



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
                    self.test_delay_msec = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.disable_keepalives = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.test_message = iprot.readString()
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
        oprot.writeStructBegin('NetworkElementTest_DeferredIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.test_delay_msec != None:
            oprot.writeFieldBegin('test_delay_msec', TType.I32, 2)
            oprot.writeI32(self.test_delay_msec)
            oprot.writeFieldEnd()
        if self.disable_keepalives != None:
            oprot.writeFieldBegin('disable_keepalives', TType.I32, 3)
            oprot.writeI32(self.disable_keepalives)
            oprot.writeFieldEnd()
        if self.test_message != None:
            oprot.writeFieldBegin('test_message', TType.STRING, 4)
            oprot.writeString(self.test_message)
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




class NetworkElementTest_DeferredIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.STRUCT,
      'success',
      (NetworkElementTestDeferredResults, NetworkElementTestDeferredResults.thrift_spec),
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
                    self.success = NetworkElementTestDeferredResults()
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
        oprot.writeStructBegin('NetworkElementTest_DeferredIDL_result')
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




class AsyncMsg_TestRegisterIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - test_id
     - op_id_offset
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionHandle',
      None,
      None),
     (2,
      TType.I32,
      'test_id',
      None,
      None),
     (3,
      TType.I32,
      'op_id_offset',
      None,
      None))

    def __init__(self, sessionHandle = None, test_id = None, op_id_offset = None):
        self.sessionHandle = sessionHandle
        self.test_id = test_id
        self.op_id_offset = op_id_offset



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
                    self.test_id = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.op_id_offset = iprot.readI32()
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
        oprot.writeStructBegin('AsyncMsg_TestRegisterIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.test_id != None:
            oprot.writeFieldBegin('test_id', TType.I32, 2)
            oprot.writeI32(self.test_id)
            oprot.writeFieldEnd()
        if self.op_id_offset != None:
            oprot.writeFieldBegin('op_id_offset', TType.I32, 3)
            oprot.writeI32(self.op_id_offset)
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




class AsyncMsg_TestRegisterIDL_result(object):
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
        oprot.writeStructBegin('AsyncMsg_TestRegisterIDL_result')
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




class NetworkElementTest_UtOpIDL_args(object):
    """
    Attributes:
     - op_code
     - req_args
    """

    thrift_spec = (None, (1,
      TType.I32,
      'op_code',
      None,
      None), (2,
      TType.STRUCT,
      'req_args',
      (NetworkElementTestUtOpArgs, NetworkElementTestUtOpArgs.thrift_spec),
      None))

    def __init__(self, op_code = None, req_args = None):
        self.op_code = op_code
        self.req_args = req_args



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
                    self.op_code = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.req_args = NetworkElementTestUtOpArgs()
                    self.req_args.read(iprot)
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
        oprot.writeStructBegin('NetworkElementTest_UtOpIDL_args')
        if self.op_code != None:
            oprot.writeFieldBegin('op_code', TType.I32, 1)
            oprot.writeI32(self.op_code)
            oprot.writeFieldEnd()
        if self.req_args != None:
            oprot.writeFieldBegin('req_args', TType.STRUCT, 2)
            self.req_args.write(oprot)
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




class NetworkElementTest_UtOpIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.STRUCT,
      'success',
      (NetworkElementTestUtOpArgs, NetworkElementTestUtOpArgs.thrift_spec),
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
                    self.success = NetworkElementTestUtOpArgs()
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
        oprot.writeStructBegin('NetworkElementTest_UtOpIDL_result')
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




class NetworkElementTest_NullOutputIDL_args(object):
    """
    Attributes:
     - op
    """

    thrift_spec = (None, (1,
      TType.I32,
      'op',
      None,
      None))

    def __init__(self, op = None):
        self.op = op



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
                    self.op = iprot.readI32()
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
        oprot.writeStructBegin('NetworkElementTest_NullOutputIDL_args')
        if self.op != None:
            oprot.writeFieldBegin('op', TType.I32, 1)
            oprot.writeI32(self.op)
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




class NetworkElementTest_NullOutputIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.STRUCT,
      'success',
      (NetworkElementTestNullOutput, NetworkElementTestNullOutput.thrift_spec),
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
                    self.success = NetworkElementTestNullOutput()
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
        oprot.writeStructBegin('NetworkElementTest_NullOutputIDL_result')
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




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:18:56 IST
