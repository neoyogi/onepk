# 2015.02.05 17:21:08 IST
from thrift.Thrift import *
import Shared.ttypes
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
    from thrift.protocol import fastbinary
except:
    fastbinary = None

class ServiceDescriptionIDL(object):
    """
      -------------------------------------
      Service Discovery related information
      -------------------------------------
    
      Attributes:
       - ipAddress
       - serviceNameKey
       - version
      """

    thrift_spec = (None,
     (1,
      TType.STRING,
      'ipAddress',
      None,
      None),
     (2,
      TType.I32,
      'serviceNameKey',
      None,
      None),
     (3,
      TType.STRUCT,
      'version',
      (Shared.ttypes.OnepVersionIDL, Shared.ttypes.OnepVersionIDL.thrift_spec),
      None))

    def __init__(self, ipAddress = None, serviceNameKey = None, version = None):
        self.ipAddress = ipAddress
        self.serviceNameKey = serviceNameKey
        self.version = version



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
                    self.ipAddress = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.serviceNameKey = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRUCT:
                    self.version = Shared.ttypes.OnepVersionIDL()
                    self.version.read(iprot)
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
        oprot.writeStructBegin('ServiceDescriptionIDL')
        if self.ipAddress != None:
            oprot.writeFieldBegin('ipAddress', TType.STRING, 1)
            oprot.writeString(self.ipAddress)
            oprot.writeFieldEnd()
        if self.serviceNameKey != None:
            oprot.writeFieldBegin('serviceNameKey', TType.I32, 2)
            oprot.writeI32(self.serviceNameKey)
            oprot.writeFieldEnd()
        if self.version != None:
            oprot.writeFieldBegin('version', TType.STRUCT, 3)
            self.version.write(oprot)
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
# 2015.02.05 17:21:08 IST
