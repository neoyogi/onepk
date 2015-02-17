# 2015.02.05 17:17:51 IST
from thrift.Thrift import *
import Shared.ttypes
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
    from thrift.protocol import fastbinary
except:
    fastbinary = None

class AttrFormat_e(object):
    AAA_TYPE_FORMAT_ULONG = 1
    AAA_TYPE_FORMAT_STRING = 2
    AAA_TYPE_FORMAT_BINARY = 3
    AAA_TYPE_FORMAT_IP_ADDR = 4
    AAA_TYPE_FORMAT_IPV6_ADDR = 5
    _VALUES_TO_NAMES = {1: 'AAA_TYPE_FORMAT_ULONG',
     2: 'AAA_TYPE_FORMAT_STRING',
     3: 'AAA_TYPE_FORMAT_BINARY',
     4: 'AAA_TYPE_FORMAT_IP_ADDR',
     5: 'AAA_TYPE_FORMAT_IPV6_ADDR'}
    _NAMES_TO_VALUES = {'AAA_TYPE_FORMAT_ULONG': 1,
     'AAA_TYPE_FORMAT_STRING': 2,
     'AAA_TYPE_FORMAT_BINARY': 3,
     'AAA_TYPE_FORMAT_IP_ADDR': 4,
     'AAA_TYPE_FORMAT_IPV6_ADDR': 5}


class Attribute_IDL(object):
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
      (TType.BYTE, None),
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
                        _elem5 = iprot.readByte()
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
        oprot.writeStructBegin('Attribute_IDL')
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
            oprot.writeListBegin(TType.BYTE, len(self.binary_value))
            for iter6 in self.binary_value:
                oprot.writeByte(iter6)

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




class AaaServer_IDL(object):
    """
    Attributes:
     - aaa_protocol
     - address
    """

    thrift_spec = (None, (1,
      TType.I32,
      'aaa_protocol',
      None,
      None), (2,
      TType.STRUCT,
      'address',
      (Shared.ttypes.NetworkAddressIDL, Shared.ttypes.NetworkAddressIDL.thrift_spec),
      None))

    def __init__(self, aaa_protocol = None, address = None):
        self.aaa_protocol = aaa_protocol
        self.address = address



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
                    self.aaa_protocol = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.address = Shared.ttypes.NetworkAddressIDL()
                    self.address.read(iprot)
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
        oprot.writeStructBegin('AaaServer_IDL')
        if self.aaa_protocol != None:
            oprot.writeFieldBegin('aaa_protocol', TType.I32, 1)
            oprot.writeI32(self.aaa_protocol)
            oprot.writeFieldEnd()
        if self.address != None:
            oprot.writeFieldBegin('address', TType.STRUCT, 2)
            self.address.write(oprot)
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




class AuthenResult_IDL(object):
    """
    Attributes:
     - aaa_user_id
     - auto_acct_enabled
     - author_profile
     - server
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'aaa_user_id',
      None,
      None),
     (2,
      TType.I32,
      'auto_acct_enabled',
      None,
      None),
     (3,
      TType.LIST,
      'author_profile',
      (TType.STRUCT, (Attribute_IDL, Attribute_IDL.thrift_spec)),
      None),
     (4,
      TType.STRUCT,
      'server',
      (AaaServer_IDL, AaaServer_IDL.thrift_spec),
      None))

    def __init__(self, aaa_user_id = None, auto_acct_enabled = None, author_profile = None, server = None):
        self.aaa_user_id = aaa_user_id
        self.auto_acct_enabled = auto_acct_enabled
        self.author_profile = author_profile
        self.server = server



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
                    self.aaa_user_id = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.auto_acct_enabled = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.LIST:
                    self.author_profile = []
                    (_etype10, _size7,) = iprot.readListBegin()
                    for _i11 in xrange(_size7):
                        _elem12 = Attribute_IDL()
                        _elem12.read(iprot)
                        self.author_profile.append(_elem12)

                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRUCT:
                    self.server = AaaServer_IDL()
                    self.server.read(iprot)
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
        oprot.writeStructBegin('AuthenResult_IDL')
        if self.aaa_user_id != None:
            oprot.writeFieldBegin('aaa_user_id', TType.I32, 1)
            oprot.writeI32(self.aaa_user_id)
            oprot.writeFieldEnd()
        if self.auto_acct_enabled != None:
            oprot.writeFieldBegin('auto_acct_enabled', TType.I32, 2)
            oprot.writeI32(self.auto_acct_enabled)
            oprot.writeFieldEnd()
        if self.author_profile != None:
            oprot.writeFieldBegin('author_profile', TType.LIST, 3)
            oprot.writeListBegin(TType.STRUCT, len(self.author_profile))
            for iter13 in self.author_profile:
                iter13.write(oprot)

            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.server != None:
            oprot.writeFieldBegin('server', TType.STRUCT, 4)
            self.server.write(oprot)
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




class AcctResult_IDL(object):
    """
    Attributes:
     - aaa_user_id
    """

    thrift_spec = (None, (1,
      TType.I32,
      'aaa_user_id',
      None,
      None))

    def __init__(self, aaa_user_id = None):
        self.aaa_user_id = aaa_user_id



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
                    self.aaa_user_id = iprot.readI32()
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
        oprot.writeStructBegin('AcctResult_IDL')
        if self.aaa_user_id != None:
            oprot.writeFieldBegin('aaa_user_id', TType.I32, 1)
            oprot.writeI32(self.aaa_user_id)
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
# 2015.02.05 17:17:51 IST
