# 2015.02.05 17:20:30 IST
from thrift.Thrift import *
import Shared.ttypes
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
    from thrift.protocol import fastbinary
except:
    fastbinary = None

class ZoneConfig_IDL(object):
    """
    Attributes:
     - name
     - description
    """

    thrift_spec = (None, (1,
      TType.STRING,
      'name',
      None,
      None), (2,
      TType.STRING,
      'description',
      None,
      None))

    def __init__(self, name = None, description = None):
        self.name = name
        self.description = description



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
                    self.name = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.description = iprot.readString()
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
        oprot.writeStructBegin('ZoneConfig_IDL')
        if self.name != None:
            oprot.writeFieldBegin('name', TType.STRING, 1)
            oprot.writeString(self.name)
            oprot.writeFieldEnd()
        if self.description != None:
            oprot.writeFieldBegin('description', TType.STRING, 2)
            oprot.writeString(self.description)
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




class ZonePairConfig_IDL(object):
    """
    Attributes:
     - name
     - srcZone
     - dstZone
    """

    thrift_spec = (None,
     (1,
      TType.STRING,
      'name',
      None,
      None),
     (2,
      TType.STRUCT,
      'srcZone',
      (ZoneConfig_IDL, ZoneConfig_IDL.thrift_spec),
      None),
     (3,
      TType.STRUCT,
      'dstZone',
      (ZoneConfig_IDL, ZoneConfig_IDL.thrift_spec),
      None))

    def __init__(self, name = None, srcZone = None, dstZone = None):
        self.name = name
        self.srcZone = srcZone
        self.dstZone = dstZone



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
                    self.name = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.srcZone = ZoneConfig_IDL()
                    self.srcZone.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRUCT:
                    self.dstZone = ZoneConfig_IDL()
                    self.dstZone.read(iprot)
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
        oprot.writeStructBegin('ZonePairConfig_IDL')
        if self.name != None:
            oprot.writeFieldBegin('name', TType.STRING, 1)
            oprot.writeString(self.name)
            oprot.writeFieldEnd()
        if self.srcZone != None:
            oprot.writeFieldBegin('srcZone', TType.STRUCT, 2)
            self.srcZone.write(oprot)
            oprot.writeFieldEnd()
        if self.dstZone != None:
            oprot.writeFieldBegin('dstZone', TType.STRUCT, 3)
            self.dstZone.write(oprot)
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




class LoggerConfig_IDL(object):
    """
    Attributes:
     - enable
     - timeout
     - collectorType
     - transportType
     - host
     - srcPort
     - dstPort
    """

    thrift_spec = (None,
     (1,
      TType.I16,
      'enable',
      None,
      None),
     (2,
      TType.I32,
      'timeout',
      None,
      None),
     (3,
      TType.I32,
      'collectorType',
      None,
      None),
     (4,
      TType.I32,
      'transportType',
      None,
      None),
     (5,
      TType.STRUCT,
      'host',
      (Shared.ttypes.NetworkAddressIDL, Shared.ttypes.NetworkAddressIDL.thrift_spec),
      None),
     (6,
      TType.I16,
      'srcPort',
      None,
      None),
     (7,
      TType.I16,
      'dstPort',
      None,
      None))

    def __init__(self, enable = None, timeout = None, collectorType = None, transportType = None, host = None, srcPort = None, dstPort = None):
        self.enable = enable
        self.timeout = timeout
        self.collectorType = collectorType
        self.transportType = transportType
        self.host = host
        self.srcPort = srcPort
        self.dstPort = dstPort



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
                if ftype == TType.I16:
                    self.enable = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.timeout = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.collectorType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.transportType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRUCT:
                    self.host = Shared.ttypes.NetworkAddressIDL()
                    self.host.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I16:
                    self.srcPort = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I16:
                    self.dstPort = iprot.readI16()
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
        oprot.writeStructBegin('LoggerConfig_IDL')
        if self.enable != None:
            oprot.writeFieldBegin('enable', TType.I16, 1)
            oprot.writeI16(self.enable)
            oprot.writeFieldEnd()
        if self.timeout != None:
            oprot.writeFieldBegin('timeout', TType.I32, 2)
            oprot.writeI32(self.timeout)
            oprot.writeFieldEnd()
        if self.collectorType != None:
            oprot.writeFieldBegin('collectorType', TType.I32, 3)
            oprot.writeI32(self.collectorType)
            oprot.writeFieldEnd()
        if self.transportType != None:
            oprot.writeFieldBegin('transportType', TType.I32, 4)
            oprot.writeI32(self.transportType)
            oprot.writeFieldEnd()
        if self.host != None:
            oprot.writeFieldBegin('host', TType.STRUCT, 5)
            self.host.write(oprot)
            oprot.writeFieldEnd()
        if self.srcPort != None:
            oprot.writeFieldBegin('srcPort', TType.I16, 6)
            oprot.writeI16(self.srcPort)
            oprot.writeFieldEnd()
        if self.dstPort != None:
            oprot.writeFieldBegin('dstPort', TType.I16, 7)
            oprot.writeI16(self.dstPort)
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
# 2015.02.05 17:20:31 IST
