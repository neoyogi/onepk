# 2015.02.05 17:20:29 IST
from thrift.Thrift import *
import Shared.ttypes
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
    from thrift.protocol import fastbinary
except:
    fastbinary = None

class VlanParam_IDL(object):
    """
      VLAN parameter
    
      Attributes:
       - vlanId
       - dsid
       - vlanName
       - vlanState
       - vlanAdminState
      """

    thrift_spec = (None,
     (1,
      TType.I32,
      'vlanId',
      None,
      None),
     (2,
      TType.I32,
      'dsid',
      None,
      None),
     (3,
      TType.STRING,
      'vlanName',
      None,
      None),
     (4,
      TType.I16,
      'vlanState',
      None,
      None),
     None,
     (6,
      TType.I16,
      'vlanAdminState',
      None,
      None))

    def __init__(self, vlanId = None, dsid = None, vlanName = None, vlanState = None, vlanAdminState = None):
        self.vlanId = vlanId
        self.dsid = dsid
        self.vlanName = vlanName
        self.vlanState = vlanState
        self.vlanAdminState = vlanAdminState



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
                    self.vlanId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.dsid = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.vlanName = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I16:
                    self.vlanState = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I16:
                    self.vlanAdminState = iprot.readI16()
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
        oprot.writeStructBegin('VlanParam_IDL')
        if self.vlanId != None:
            oprot.writeFieldBegin('vlanId', TType.I32, 1)
            oprot.writeI32(self.vlanId)
            oprot.writeFieldEnd()
        if self.dsid != None:
            oprot.writeFieldBegin('dsid', TType.I32, 2)
            oprot.writeI32(self.dsid)
            oprot.writeFieldEnd()
        if self.vlanName != None:
            oprot.writeFieldBegin('vlanName', TType.STRING, 3)
            oprot.writeString(self.vlanName)
            oprot.writeFieldEnd()
        if self.vlanState != None:
            oprot.writeFieldBegin('vlanState', TType.I16, 4)
            oprot.writeI16(self.vlanState)
            oprot.writeFieldEnd()
        if self.vlanAdminState != None:
            oprot.writeFieldBegin('vlanAdminState', TType.I16, 6)
            oprot.writeI16(self.vlanAdminState)
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
# 2015.02.05 17:20:29 IST
