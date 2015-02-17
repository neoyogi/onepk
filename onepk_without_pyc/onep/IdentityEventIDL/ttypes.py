# 2015.02.05 17:21:18 IST
from thrift.Thrift import *
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
    from thrift.protocol import fastbinary
except:
    fastbinary = None

class AttrFormatOut_e(object):
    IDEN_AAA_TYPE_FORMAT_ULONG = 1
    IDEN_AAA_TYPE_FORMAT_STRING = 2
    IDEN_AAA_TYPE_FORMAT_BINARY = 3
    IDEN_AAA_TYPE_FORMAT_IP_ADDR = 4
    IDEN_AAA_TYPE_FORMAT_IPV6_ADDR = 5
    _VALUES_TO_NAMES = {1: 'IDEN_AAA_TYPE_FORMAT_ULONG',
     2: 'IDEN_AAA_TYPE_FORMAT_STRING',
     3: 'IDEN_AAA_TYPE_FORMAT_BINARY',
     4: 'IDEN_AAA_TYPE_FORMAT_IP_ADDR',
     5: 'IDEN_AAA_TYPE_FORMAT_IPV6_ADDR'}
    _NAMES_TO_VALUES = {'IDEN_AAA_TYPE_FORMAT_ULONG': 1,
     'IDEN_AAA_TYPE_FORMAT_STRING': 2,
     'IDEN_AAA_TYPE_FORMAT_BINARY': 3,
     'IDEN_AAA_TYPE_FORMAT_IP_ADDR': 4,
     'IDEN_AAA_TYPE_FORMAT_IPV6_ADDR': 5}


class ByteOutIDL(object):
    """
    Attributes:
     - binary_value
    """

    thrift_spec = (None, (1,
      TType.BYTE,
      'binary_value',
      None,
      None))

    def __init__(self, binary_value = None):
        self.binary_value = binary_value



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
                if ftype == TType.BYTE:
                    self.binary_value = iprot.readByte()
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
        oprot.writeStructBegin('ByteOutIDL')
        if self.binary_value != None:
            oprot.writeFieldBegin('binary_value', TType.BYTE, 1)
            oprot.writeByte(self.binary_value)
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




class AttributeOutIDL(object):
    """
    Attributes:
     - type
     - format
     - str_value
     - ulong_value
     - binary_value
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'type',
      None,
      None),
     (2,
      TType.I32,
      'format',
      None,
      None),
     (3,
      TType.STRING,
      'str_value',
      None,
      None),
     (4,
      TType.I64,
      'ulong_value',
      None,
      None),
     (5,
      TType.LIST,
      'binary_value',
      (TType.STRUCT, (ByteOutIDL, ByteOutIDL.thrift_spec)),
      None))

    def __init__(self, type = None, format = None, str_value = None, ulong_value = None, binary_value = None):
        self.type = type
        self.format = format
        self.str_value = str_value
        self.ulong_value = ulong_value
        self.binary_value = binary_value



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
                    self.type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.format = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.str_value = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I64:
                    self.ulong_value = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.LIST:
                    self.binary_value = []
                    (_etype3, _size0,) = iprot.readListBegin()
                    for _i4 in xrange(_size0):
                        _elem5 = ByteOutIDL()
                        _elem5.read(iprot)
                        self.binary_value.append(_elem5)

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
        oprot.writeStructBegin('AttributeOutIDL')
        if self.type != None:
            oprot.writeFieldBegin('type', TType.I32, 1)
            oprot.writeI32(self.type)
            oprot.writeFieldEnd()
        if self.format != None:
            oprot.writeFieldBegin('format', TType.I32, 2)
            oprot.writeI32(self.format)
            oprot.writeFieldEnd()
        if self.str_value != None:
            oprot.writeFieldBegin('str_value', TType.STRING, 3)
            oprot.writeString(self.str_value)
            oprot.writeFieldEnd()
        if self.ulong_value != None:
            oprot.writeFieldBegin('ulong_value', TType.I64, 4)
            oprot.writeI64(self.ulong_value)
            oprot.writeFieldEnd()
        if self.binary_value != None:
            oprot.writeFieldBegin('binary_value', TType.LIST, 5)
            oprot.writeListBegin(TType.STRUCT, len(self.binary_value))
            for iter6 in self.binary_value:
                iter6.write(oprot)

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




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:21:18 IST
