# 2015.02.05 17:17:56 IST
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

    def AsyncMsg_TestResponseIDL(self, base, test_id, op_id_offset):
        """
            Async messages from network element to application
        
            Parameters:
             - base
             - test_id
             - op_id_offset
            """
        pass




class Client(Iface):

    def __init__(self, iprot, oprot = None):
        self._iprot = self._oprot = iprot
        if oprot != None:
            self._oprot = oprot
        self._seqid = 0



    def AsyncMsg_TestResponseIDL(self, base, test_id, op_id_offset):
        """
            Async messages from network element to application
        
            Parameters:
             - base
             - test_id
             - op_id_offset
            """
        self._oprot.rlock.acquire()
        try:
            self.send_AsyncMsg_TestResponseIDL(base, test_id, op_id_offset)
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()



    def send_AsyncMsg_TestResponseIDL(self, base, test_id, op_id_offset):
        self._oprot.writeMessageBegin('AsyncMsg_TestResponseIDL', TMessageType.CALL, self._seqid)
        args = AsyncMsg_TestResponseIDL_args()
        args.base = base
        args.test_id = test_id
        args.op_id_offset = op_id_offset
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()




class Processor(Iface, TProcessor):

    def __init__(self, handler):
        self._handler = handler
        self._processMap = {}
        self._processMap['AsyncMsg_TestResponseIDL'] = Processor.process_AsyncMsg_TestResponseIDL



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



    def process_AsyncMsg_TestResponseIDL(self, seqid, iprot, oprot):
        args = AsyncMsg_TestResponseIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        self._handler.AsyncMsg_TestResponseIDL(args.base, args.test_id, args.op_id_offset)




class AsyncMsg_TestResponseIDL_args(object):
    """
    Attributes:
     - base
     - test_id
     - op_id_offset
    """

    thrift_spec = (None,
     (1,
      TType.STRUCT,
      'base',
      (AsyncBaseOutIDL, AsyncBaseOutIDL.thrift_spec),
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

    def __init__(self, base = None, test_id = None, op_id_offset = None):
        self.base = base
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
                if ftype == TType.STRUCT:
                    self.base = AsyncBaseOutIDL()
                    self.base.read(iprot)
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
        oprot.writeStructBegin('AsyncMsg_TestResponseIDL_args')
        if self.base != None:
            oprot.writeFieldBegin('base', TType.STRUCT, 1)
            self.base.write(oprot)
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




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:17:56 IST
