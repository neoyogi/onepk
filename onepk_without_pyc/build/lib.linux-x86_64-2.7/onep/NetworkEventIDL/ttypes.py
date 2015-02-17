# 2015.02.05 17:19:01 IST
from thrift.Thrift import *
import SharedOut.ttypes
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
    from thrift.protocol import fastbinary
except:
    fastbinary = None

class MacAddressOutIDL(object):
    """
    Attributes:
     - b1
     - b2
     - b3
     - b4
     - b5
     - b6
    """

    thrift_spec = (None,
     (1,
      TType.BYTE,
      'b1',
      None,
      None),
     (2,
      TType.BYTE,
      'b2',
      None,
      None),
     (3,
      TType.BYTE,
      'b3',
      None,
      None),
     (4,
      TType.BYTE,
      'b4',
      None,
      None),
     (5,
      TType.BYTE,
      'b5',
      None,
      None),
     (6,
      TType.BYTE,
      'b6',
      None,
      None))

    def __init__(self, b1 = None, b2 = None, b3 = None, b4 = None, b5 = None, b6 = None):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
        self.b6 = b6



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
                    self.b1 = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.BYTE:
                    self.b2 = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.BYTE:
                    self.b3 = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.BYTE:
                    self.b4 = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.BYTE:
                    self.b5 = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.BYTE:
                    self.b6 = iprot.readByte()
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
        oprot.writeStructBegin('MacAddressOutIDL')
        if self.b1 != None:
            oprot.writeFieldBegin('b1', TType.BYTE, 1)
            oprot.writeByte(self.b1)
            oprot.writeFieldEnd()
        if self.b2 != None:
            oprot.writeFieldBegin('b2', TType.BYTE, 2)
            oprot.writeByte(self.b2)
            oprot.writeFieldEnd()
        if self.b3 != None:
            oprot.writeFieldBegin('b3', TType.BYTE, 3)
            oprot.writeByte(self.b3)
            oprot.writeFieldEnd()
        if self.b4 != None:
            oprot.writeFieldBegin('b4', TType.BYTE, 4)
            oprot.writeByte(self.b4)
            oprot.writeFieldEnd()
        if self.b5 != None:
            oprot.writeFieldBegin('b5', TType.BYTE, 5)
            oprot.writeByte(self.b5)
            oprot.writeFieldEnd()
        if self.b6 != None:
            oprot.writeFieldBegin('b6', TType.BYTE, 6)
            oprot.writeByte(self.b6)
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




class InterfaceVlanOutIDL(object):
    """
    Attributes:
     - encapType
     - vlanTag1
     - vlanTag2
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'encapType',
      None,
      None),
     (2,
      TType.I32,
      'vlanTag1',
      None,
      None),
     (3,
      TType.I32,
      'vlanTag2',
      None,
      None))

    def __init__(self, encapType = None, vlanTag1 = None, vlanTag2 = None):
        self.encapType = encapType
        self.vlanTag1 = vlanTag1
        self.vlanTag2 = vlanTag2



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
                    self.encapType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.vlanTag1 = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.vlanTag2 = iprot.readI32()
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
        oprot.writeStructBegin('InterfaceVlanOutIDL')
        if self.encapType != None:
            oprot.writeFieldBegin('encapType', TType.I32, 1)
            oprot.writeI32(self.encapType)
            oprot.writeFieldEnd()
        if self.vlanTag1 != None:
            oprot.writeFieldBegin('vlanTag1', TType.I32, 2)
            oprot.writeI32(self.vlanTag1)
            oprot.writeFieldEnd()
        if self.vlanTag2 != None:
            oprot.writeFieldBegin('vlanTag2', TType.I32, 3)
            oprot.writeI32(self.vlanTag2)
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




class InterfaceStatisticsOutIDL(object):
    """
    Attributes:
     - retcode
     - stats
    """

    thrift_spec = (None, (1,
      TType.I32,
      'retcode',
      None,
      None), (2,
      TType.I64,
      'stats',
      None,
      None))

    def __init__(self, retcode = None, stats = None):
        self.retcode = retcode
        self.stats = stats



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
                    self.retcode = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.stats = iprot.readI64()
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
        oprot.writeStructBegin('InterfaceStatisticsOutIDL')
        if self.retcode != None:
            oprot.writeFieldBegin('retcode', TType.I32, 1)
            oprot.writeI32(self.retcode)
            oprot.writeFieldEnd()
        if self.stats != None:
            oprot.writeFieldBegin('stats', TType.I64, 2)
            oprot.writeI64(self.stats)
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
# 2015.02.05 17:19:01 IST
