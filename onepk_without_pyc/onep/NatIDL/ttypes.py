# 2015.02.05 17:21:40 IST
from thrift.Thrift import *
import Shared.ttypes
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
    from thrift.protocol import fastbinary
except:
    fastbinary = None

class StaticNatParam_IDL(object):
    """
      static NAT parameter
    
      Attributes:
       - ruleId
       - mode
       - mapping
       - family
       - protocol
       - localPort
       - globalPort
       - localIpAddr
       - globalIpAddr
       - prefixLen
       - vrfName
       - matchInVrf
      """

    thrift_spec = (None,
     (1,
      TType.STRING,
      'ruleId',
      None,
      None),
     (2,
      TType.I16,
      'mode',
      None,
      None),
     (3,
      TType.I16,
      'mapping',
      None,
      None),
     (4,
      TType.I32,
      'family',
      None,
      None),
     (5,
      TType.I16,
      'protocol',
      None,
      None),
     (6,
      TType.I16,
      'localPort',
      None,
      None),
     (7,
      TType.I16,
      'globalPort',
      None,
      None),
     (8,
      TType.STRUCT,
      'localIpAddr',
      (Shared.ttypes.NetworkAddressIDL, Shared.ttypes.NetworkAddressIDL.thrift_spec),
      None),
     (9,
      TType.STRUCT,
      'globalIpAddr',
      (Shared.ttypes.NetworkAddressIDL, Shared.ttypes.NetworkAddressIDL.thrift_spec),
      None),
     (10,
      TType.I16,
      'prefixLen',
      None,
      None),
     (11,
      TType.STRING,
      'vrfName',
      None,
      None),
     (12,
      TType.I16,
      'matchInVrf',
      None,
      None))

    def __init__(self, ruleId = None, mode = None, mapping = None, family = None, protocol = None, localPort = None, globalPort = None, localIpAddr = None, globalIpAddr = None, prefixLen = None, vrfName = None, matchInVrf = None):
        self.ruleId = ruleId
        self.mode = mode
        self.mapping = mapping
        self.family = family
        self.protocol = protocol
        self.localPort = localPort
        self.globalPort = globalPort
        self.localIpAddr = localIpAddr
        self.globalIpAddr = globalIpAddr
        self.prefixLen = prefixLen
        self.vrfName = vrfName
        self.matchInVrf = matchInVrf



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
                    self.ruleId = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I16:
                    self.mode = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I16:
                    self.mapping = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.family = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I16:
                    self.protocol = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I16:
                    self.localPort = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I16:
                    self.globalPort = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.STRUCT:
                    self.localIpAddr = Shared.ttypes.NetworkAddressIDL()
                    self.localIpAddr.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.STRUCT:
                    self.globalIpAddr = Shared.ttypes.NetworkAddressIDL()
                    self.globalIpAddr.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.I16:
                    self.prefixLen = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.STRING:
                    self.vrfName = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 12:
                if ftype == TType.I16:
                    self.matchInVrf = iprot.readI16()
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
        oprot.writeStructBegin('StaticNatParam_IDL')
        if self.ruleId != None:
            oprot.writeFieldBegin('ruleId', TType.STRING, 1)
            oprot.writeString(self.ruleId)
            oprot.writeFieldEnd()
        if self.mode != None:
            oprot.writeFieldBegin('mode', TType.I16, 2)
            oprot.writeI16(self.mode)
            oprot.writeFieldEnd()
        if self.mapping != None:
            oprot.writeFieldBegin('mapping', TType.I16, 3)
            oprot.writeI16(self.mapping)
            oprot.writeFieldEnd()
        if self.family != None:
            oprot.writeFieldBegin('family', TType.I32, 4)
            oprot.writeI32(self.family)
            oprot.writeFieldEnd()
        if self.protocol != None:
            oprot.writeFieldBegin('protocol', TType.I16, 5)
            oprot.writeI16(self.protocol)
            oprot.writeFieldEnd()
        if self.localPort != None:
            oprot.writeFieldBegin('localPort', TType.I16, 6)
            oprot.writeI16(self.localPort)
            oprot.writeFieldEnd()
        if self.globalPort != None:
            oprot.writeFieldBegin('globalPort', TType.I16, 7)
            oprot.writeI16(self.globalPort)
            oprot.writeFieldEnd()
        if self.localIpAddr != None:
            oprot.writeFieldBegin('localIpAddr', TType.STRUCT, 8)
            self.localIpAddr.write(oprot)
            oprot.writeFieldEnd()
        if self.globalIpAddr != None:
            oprot.writeFieldBegin('globalIpAddr', TType.STRUCT, 9)
            self.globalIpAddr.write(oprot)
            oprot.writeFieldEnd()
        if self.prefixLen != None:
            oprot.writeFieldBegin('prefixLen', TType.I16, 10)
            oprot.writeI16(self.prefixLen)
            oprot.writeFieldEnd()
        if self.vrfName != None:
            oprot.writeFieldBegin('vrfName', TType.STRING, 11)
            oprot.writeString(self.vrfName)
            oprot.writeFieldEnd()
        if self.matchInVrf != None:
            oprot.writeFieldBegin('matchInVrf', TType.I16, 12)
            oprot.writeI16(self.matchInVrf)
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




class NatPoolParam_IDL(object):
    """
      NAT pool parameter
    
      Attributes:
       - natPoolId
       - family
       - startIpAddr
       - endIpAddr
       - prefixLen
      """

    thrift_spec = (None,
     (1,
      TType.STRING,
      'natPoolId',
      None,
      None),
     (2,
      TType.I32,
      'family',
      None,
      None),
     (3,
      TType.STRUCT,
      'startIpAddr',
      (Shared.ttypes.NetworkAddressIDL, Shared.ttypes.NetworkAddressIDL.thrift_spec),
      None),
     (4,
      TType.STRUCT,
      'endIpAddr',
      (Shared.ttypes.NetworkAddressIDL, Shared.ttypes.NetworkAddressIDL.thrift_spec),
      None),
     (5,
      TType.I16,
      'prefixLen',
      None,
      None))

    def __init__(self, natPoolId = None, family = None, startIpAddr = None, endIpAddr = None, prefixLen = None):
        self.natPoolId = natPoolId
        self.family = family
        self.startIpAddr = startIpAddr
        self.endIpAddr = endIpAddr
        self.prefixLen = prefixLen



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
                    self.natPoolId = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.family = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRUCT:
                    self.startIpAddr = Shared.ttypes.NetworkAddressIDL()
                    self.startIpAddr.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRUCT:
                    self.endIpAddr = Shared.ttypes.NetworkAddressIDL()
                    self.endIpAddr.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I16:
                    self.prefixLen = iprot.readI16()
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
        oprot.writeStructBegin('NatPoolParam_IDL')
        if self.natPoolId != None:
            oprot.writeFieldBegin('natPoolId', TType.STRING, 1)
            oprot.writeString(self.natPoolId)
            oprot.writeFieldEnd()
        if self.family != None:
            oprot.writeFieldBegin('family', TType.I32, 2)
            oprot.writeI32(self.family)
            oprot.writeFieldEnd()
        if self.startIpAddr != None:
            oprot.writeFieldBegin('startIpAddr', TType.STRUCT, 3)
            self.startIpAddr.write(oprot)
            oprot.writeFieldEnd()
        if self.endIpAddr != None:
            oprot.writeFieldBegin('endIpAddr', TType.STRUCT, 4)
            self.endIpAddr.write(oprot)
            oprot.writeFieldEnd()
        if self.prefixLen != None:
            oprot.writeFieldBegin('prefixLen', TType.I16, 5)
            oprot.writeI16(self.prefixLen)
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




class DynamicNatParam_IDL(object):
    """
      dynamic NAT parameter
    
      Attributes:
       - ruleId
       - mode
       - mapping
       - aclHandle
       - natPoolId
       - patEnabled
       - vrfName
       - matchInVrf
      """

    thrift_spec = (None,
     (1,
      TType.STRING,
      'ruleId',
      None,
      None),
     (2,
      TType.I16,
      'mode',
      None,
      None),
     (3,
      TType.I16,
      'mapping',
      None,
      None),
     (4,
      TType.STRING,
      'aclHandle',
      None,
      None),
     (5,
      TType.STRING,
      'natPoolId',
      None,
      None),
     (6,
      TType.I16,
      'patEnabled',
      None,
      None),
     (7,
      TType.STRING,
      'vrfName',
      None,
      None),
     (8,
      TType.I16,
      'matchInVrf',
      None,
      None))

    def __init__(self, ruleId = None, mode = None, mapping = None, aclHandle = None, natPoolId = None, patEnabled = None, vrfName = None, matchInVrf = None):
        self.ruleId = ruleId
        self.mode = mode
        self.mapping = mapping
        self.aclHandle = aclHandle
        self.natPoolId = natPoolId
        self.patEnabled = patEnabled
        self.vrfName = vrfName
        self.matchInVrf = matchInVrf



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
                    self.ruleId = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I16:
                    self.mode = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I16:
                    self.mapping = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.aclHandle = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.natPoolId = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I16:
                    self.patEnabled = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.STRING:
                    self.vrfName = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.I16:
                    self.matchInVrf = iprot.readI16()
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
        oprot.writeStructBegin('DynamicNatParam_IDL')
        if self.ruleId != None:
            oprot.writeFieldBegin('ruleId', TType.STRING, 1)
            oprot.writeString(self.ruleId)
            oprot.writeFieldEnd()
        if self.mode != None:
            oprot.writeFieldBegin('mode', TType.I16, 2)
            oprot.writeI16(self.mode)
            oprot.writeFieldEnd()
        if self.mapping != None:
            oprot.writeFieldBegin('mapping', TType.I16, 3)
            oprot.writeI16(self.mapping)
            oprot.writeFieldEnd()
        if self.aclHandle != None:
            oprot.writeFieldBegin('aclHandle', TType.STRING, 4)
            oprot.writeString(self.aclHandle)
            oprot.writeFieldEnd()
        if self.natPoolId != None:
            oprot.writeFieldBegin('natPoolId', TType.STRING, 5)
            oprot.writeString(self.natPoolId)
            oprot.writeFieldEnd()
        if self.patEnabled != None:
            oprot.writeFieldBegin('patEnabled', TType.I16, 6)
            oprot.writeI16(self.patEnabled)
            oprot.writeFieldEnd()
        if self.vrfName != None:
            oprot.writeFieldBegin('vrfName', TType.STRING, 7)
            oprot.writeString(self.vrfName)
            oprot.writeFieldEnd()
        if self.matchInVrf != None:
            oprot.writeFieldBegin('matchInVrf', TType.I16, 8)
            oprot.writeI16(self.matchInVrf)
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
# 2015.02.05 17:21:40 IST
