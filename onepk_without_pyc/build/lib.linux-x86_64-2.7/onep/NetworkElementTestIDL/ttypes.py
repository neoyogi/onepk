# 2015.02.05 17:18:56 IST
from thrift.Thrift import *
import Shared.ttypes
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
    from thrift.protocol import fastbinary
except:
    fastbinary = None

class NetworkElementTestDeferredResults(object):
    """
    Attributes:
     - test_delay_msec
     - test_message
    """

    thrift_spec = (None, (1,
      TType.I32,
      'test_delay_msec',
      None,
      None), (2,
      TType.STRING,
      'test_message',
      None,
      None))

    def __init__(self, test_delay_msec = None, test_message = None):
        self.test_delay_msec = test_delay_msec
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
                    self.test_delay_msec = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
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
        oprot.writeStructBegin('NetworkElementTestDeferredResults')
        if self.test_delay_msec != None:
            oprot.writeFieldBegin('test_delay_msec', TType.I32, 1)
            oprot.writeI32(self.test_delay_msec)
            oprot.writeFieldEnd()
        if self.test_message != None:
            oprot.writeFieldBegin('test_message', TType.STRING, 2)
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




class NetworkElementTestUtOpArgs(object):
    """
    Attributes:
     - i64_args
     - str_arg
    """

    thrift_spec = (None, (1,
      TType.LIST,
      'i64_args',
      (TType.I64, None),
      None), (2,
      TType.STRING,
      'str_arg',
      None,
      None))

    def __init__(self, i64_args = None, str_arg = None):
        self.i64_args = i64_args
        self.str_arg = str_arg



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
                if ftype == TType.LIST:
                    self.i64_args = []
                    (_etype3, _size0,) = iprot.readListBegin()
                    for _i4 in xrange(_size0):
                        _elem5 = iprot.readI64()
                        self.i64_args.append(_elem5)

                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.str_arg = iprot.readString()
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
        oprot.writeStructBegin('NetworkElementTestUtOpArgs')
        if self.i64_args != None:
            oprot.writeFieldBegin('i64_args', TType.LIST, 1)
            oprot.writeListBegin(TType.I64, len(self.i64_args))
            for iter6 in self.i64_args:
                oprot.writeI64(iter6)

            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.str_arg != None:
            oprot.writeFieldBegin('str_arg', TType.STRING, 2)
            oprot.writeString(self.str_arg)
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




class NetworkElementTestNullOutput(object):
    """
    Attributes:
     - val1
     - val2
    """

    thrift_spec = (None, (1,
      TType.I32,
      'val1',
      None,
      None), (2,
      TType.I32,
      'val2',
      None,
      None))

    def __init__(self, val1 = None, val2 = None):
        self.val1 = val1
        self.val2 = val2



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
                    self.val1 = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.val2 = iprot.readI32()
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
        oprot.writeStructBegin('NetworkElementTestNullOutput')
        if self.val1 != None:
            oprot.writeFieldBegin('val1', TType.I32, 1)
            oprot.writeI32(self.val1)
            oprot.writeFieldEnd()
        if self.val2 != None:
            oprot.writeFieldBegin('val2', TType.I32, 2)
            oprot.writeI32(self.val2)
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
