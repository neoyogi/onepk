# 2015.02.05 17:18:39 IST
from thrift.Thrift import *
import Shared.ttypes
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
    from thrift.protocol import fastbinary
except:
    fastbinary = None

class RlocIDL(object):
    """
      RLOC Address
    
      Attributes:
       - addressAF
       - address
      """

    thrift_spec = (None, (1,
      TType.I32,
      'addressAF',
      None,
      None), (2,
      TType.STRING,
      'address',
      None,
      None))

    def __init__(self, addressAF = None, address = None):
        self.addressAF = addressAF
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
                    self.addressAF = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.address = iprot.readString()
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
        oprot.writeStructBegin('RlocIDL')
        if self.addressAF != None:
            oprot.writeFieldBegin('addressAF', TType.I32, 1)
            oprot.writeI32(self.addressAF)
            oprot.writeFieldEnd()
        if self.address != None:
            oprot.writeFieldBegin('address', TType.STRING, 2)
            oprot.writeString(self.address)
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




class LocalRlocIDL(object):
    """
      Local RLOC Address
    
      Attributes:
       - rlocAF
       - rloc
       - priority
       - weight
      """

    thrift_spec = (None,
     (1,
      TType.I32,
      'rlocAF',
      None,
      None),
     (2,
      TType.STRING,
      'rloc',
      None,
      None),
     (3,
      TType.BYTE,
      'priority',
      None,
      None),
     (4,
      TType.BYTE,
      'weight',
      None,
      None))

    def __init__(self, rlocAF = None, rloc = None, priority = None, weight = None):
        self.rlocAF = rlocAF
        self.rloc = rloc
        self.priority = priority
        self.weight = weight



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
                    self.rlocAF = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.rloc = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.BYTE:
                    self.priority = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.BYTE:
                    self.weight = iprot.readByte()
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
        oprot.writeStructBegin('LocalRlocIDL')
        if self.rlocAF != None:
            oprot.writeFieldBegin('rlocAF', TType.I32, 1)
            oprot.writeI32(self.rlocAF)
            oprot.writeFieldEnd()
        if self.rloc != None:
            oprot.writeFieldBegin('rloc', TType.STRING, 2)
            oprot.writeString(self.rloc)
            oprot.writeFieldEnd()
        if self.priority != None:
            oprot.writeFieldBegin('priority', TType.BYTE, 3)
            oprot.writeByte(self.priority)
            oprot.writeFieldEnd()
        if self.weight != None:
            oprot.writeFieldBegin('weight', TType.BYTE, 4)
            oprot.writeByte(self.weight)
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




class RemoteRlocIDL(object):
    """
      Remote RLOC Address
    
      Attributes:
       - addressAF
       - address
       - priority
       - weight
       - reachability
      """

    thrift_spec = (None,
     (1,
      TType.I32,
      'addressAF',
      None,
      None),
     (2,
      TType.STRING,
      'address',
      None,
      None),
     (3,
      TType.BYTE,
      'priority',
      None,
      None),
     (4,
      TType.BYTE,
      'weight',
      None,
      None),
     (5,
      TType.I32,
      'reachability',
      None,
      None))

    def __init__(self, addressAF = None, address = None, priority = None, weight = None, reachability = None):
        self.addressAF = addressAF
        self.address = address
        self.priority = priority
        self.weight = weight
        self.reachability = reachability



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
                    self.addressAF = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.address = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.BYTE:
                    self.priority = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.BYTE:
                    self.weight = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.reachability = iprot.readI32()
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
        oprot.writeStructBegin('RemoteRlocIDL')
        if self.addressAF != None:
            oprot.writeFieldBegin('addressAF', TType.I32, 1)
            oprot.writeI32(self.addressAF)
            oprot.writeFieldEnd()
        if self.address != None:
            oprot.writeFieldBegin('address', TType.STRING, 2)
            oprot.writeString(self.address)
            oprot.writeFieldEnd()
        if self.priority != None:
            oprot.writeFieldBegin('priority', TType.BYTE, 3)
            oprot.writeByte(self.priority)
            oprot.writeFieldEnd()
        if self.weight != None:
            oprot.writeFieldBegin('weight', TType.BYTE, 4)
            oprot.writeByte(self.weight)
            oprot.writeFieldEnd()
        if self.reachability != None:
            oprot.writeFieldBegin('reachability', TType.I32, 5)
            oprot.writeI32(self.reachability)
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




class RemoteEidPrefixIDL(object):
    """
      Remote EID Prefix
    
      Attributes:
       - prefixAF
       - prefix
       - prefixLen
       - state
       - rlocs
      """

    thrift_spec = (None,
     (1,
      TType.I32,
      'prefixAF',
      None,
      None),
     (2,
      TType.STRING,
      'prefix',
      None,
      None),
     (3,
      TType.I16,
      'prefixLen',
      None,
      None),
     (4,
      TType.I32,
      'state',
      None,
      None),
     (5,
      TType.LIST,
      'rlocs',
      (TType.STRUCT, (RemoteRlocIDL, RemoteRlocIDL.thrift_spec)),
      None))

    def __init__(self, prefixAF = None, prefix = None, prefixLen = None, state = None, rlocs = None):
        self.prefixAF = prefixAF
        self.prefix = prefix
        self.prefixLen = prefixLen
        self.state = state
        self.rlocs = rlocs



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
                    self.prefixAF = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.prefix = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I16:
                    self.prefixLen = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.state = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.LIST:
                    self.rlocs = []
                    (_etype3, _size0,) = iprot.readListBegin()
                    for _i4 in xrange(_size0):
                        _elem5 = RemoteRlocIDL()
                        _elem5.read(iprot)
                        self.rlocs.append(_elem5)

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
        oprot.writeStructBegin('RemoteEidPrefixIDL')
        if self.prefixAF != None:
            oprot.writeFieldBegin('prefixAF', TType.I32, 1)
            oprot.writeI32(self.prefixAF)
            oprot.writeFieldEnd()
        if self.prefix != None:
            oprot.writeFieldBegin('prefix', TType.STRING, 2)
            oprot.writeString(self.prefix)
            oprot.writeFieldEnd()
        if self.prefixLen != None:
            oprot.writeFieldBegin('prefixLen', TType.I16, 3)
            oprot.writeI16(self.prefixLen)
            oprot.writeFieldEnd()
        if self.state != None:
            oprot.writeFieldBegin('state', TType.I32, 4)
            oprot.writeI32(self.state)
            oprot.writeFieldEnd()
        if self.rlocs != None:
            oprot.writeFieldBegin('rlocs', TType.LIST, 5)
            oprot.writeListBegin(TType.STRUCT, len(self.rlocs))
            for iter6 in self.rlocs:
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
# 2015.02.05 17:18:40 IST
