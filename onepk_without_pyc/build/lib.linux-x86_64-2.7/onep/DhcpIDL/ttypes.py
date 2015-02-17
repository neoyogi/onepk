# 2015.02.05 17:18:14 IST
from thrift.Thrift import *
import Shared.ttypes
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
    from thrift.protocol import fastbinary
except:
    fastbinary = None

class DhcpBindParamIDL(object):
    """
    Attributes:
     - ipAddr
     - macAddr
     - bindLease
     - bindType
     - bindState
     - xosHandle
    """

    thrift_spec = (None,
     (1,
      TType.STRUCT,
      'ipAddr',
      (Shared.ttypes.NetworkAddressIDL, Shared.ttypes.NetworkAddressIDL.thrift_spec),
      None),
     (2,
      TType.STRING,
      'macAddr',
      None,
      None),
     (3,
      TType.I64,
      'bindLease',
      None,
      None),
     (4,
      TType.I32,
      'bindType',
      None,
      None),
     (5,
      TType.I32,
      'bindState',
      None,
      None),
     (6,
      TType.I64,
      'xosHandle',
      None,
      None))

    def __init__(self, ipAddr = None, macAddr = None, bindLease = None, bindType = None, bindState = None, xosHandle = None):
        self.ipAddr = ipAddr
        self.macAddr = macAddr
        self.bindLease = bindLease
        self.bindType = bindType
        self.bindState = bindState
        self.xosHandle = xosHandle



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
                    self.ipAddr = Shared.ttypes.NetworkAddressIDL()
                    self.ipAddr.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.macAddr = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I64:
                    self.bindLease = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.bindType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.bindState = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I64:
                    self.xosHandle = iprot.readI64()
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
        oprot.writeStructBegin('DhcpBindParamIDL')
        if self.ipAddr != None:
            oprot.writeFieldBegin('ipAddr', TType.STRUCT, 1)
            self.ipAddr.write(oprot)
            oprot.writeFieldEnd()
        if self.macAddr != None:
            oprot.writeFieldBegin('macAddr', TType.STRING, 2)
            oprot.writeString(self.macAddr)
            oprot.writeFieldEnd()
        if self.bindLease != None:
            oprot.writeFieldBegin('bindLease', TType.I64, 3)
            oprot.writeI64(self.bindLease)
            oprot.writeFieldEnd()
        if self.bindType != None:
            oprot.writeFieldBegin('bindType', TType.I32, 4)
            oprot.writeI32(self.bindType)
            oprot.writeFieldEnd()
        if self.bindState != None:
            oprot.writeFieldBegin('bindState', TType.I32, 5)
            oprot.writeI32(self.bindState)
            oprot.writeFieldEnd()
        if self.xosHandle != None:
            oprot.writeFieldBegin('xosHandle', TType.I64, 6)
            oprot.writeI64(self.xosHandle)
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




class DhcpPoolSubnetIDL(object):
    """
    Attributes:
     - ipRangeLow
     - ipRangeHigh
     - ipCurrentIndex
     - ipLeased
     - ipTotal
     - subnetType
    """

    thrift_spec = (None,
     (1,
      TType.STRUCT,
      'ipRangeLow',
      (Shared.ttypes.NetworkAddressIDL, Shared.ttypes.NetworkAddressIDL.thrift_spec),
      None),
     (2,
      TType.STRUCT,
      'ipRangeHigh',
      (Shared.ttypes.NetworkAddressIDL, Shared.ttypes.NetworkAddressIDL.thrift_spec),
      None),
     (3,
      TType.STRUCT,
      'ipCurrentIndex',
      (Shared.ttypes.NetworkAddressIDL, Shared.ttypes.NetworkAddressIDL.thrift_spec),
      None),
     (4,
      TType.I32,
      'ipLeased',
      None,
      None),
     (5,
      TType.I32,
      'ipTotal',
      None,
      None),
     (6,
      TType.I32,
      'subnetType',
      None,
      None))

    def __init__(self, ipRangeLow = None, ipRangeHigh = None, ipCurrentIndex = None, ipLeased = None, ipTotal = None, subnetType = None):
        self.ipRangeLow = ipRangeLow
        self.ipRangeHigh = ipRangeHigh
        self.ipCurrentIndex = ipCurrentIndex
        self.ipLeased = ipLeased
        self.ipTotal = ipTotal
        self.subnetType = subnetType



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
                    self.ipRangeLow = Shared.ttypes.NetworkAddressIDL()
                    self.ipRangeLow.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.ipRangeHigh = Shared.ttypes.NetworkAddressIDL()
                    self.ipRangeHigh.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRUCT:
                    self.ipCurrentIndex = Shared.ttypes.NetworkAddressIDL()
                    self.ipCurrentIndex.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.ipLeased = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.ipTotal = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I32:
                    self.subnetType = iprot.readI32()
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
        oprot.writeStructBegin('DhcpPoolSubnetIDL')
        if self.ipRangeLow != None:
            oprot.writeFieldBegin('ipRangeLow', TType.STRUCT, 1)
            self.ipRangeLow.write(oprot)
            oprot.writeFieldEnd()
        if self.ipRangeHigh != None:
            oprot.writeFieldBegin('ipRangeHigh', TType.STRUCT, 2)
            self.ipRangeHigh.write(oprot)
            oprot.writeFieldEnd()
        if self.ipCurrentIndex != None:
            oprot.writeFieldBegin('ipCurrentIndex', TType.STRUCT, 3)
            self.ipCurrentIndex.write(oprot)
            oprot.writeFieldEnd()
        if self.ipLeased != None:
            oprot.writeFieldBegin('ipLeased', TType.I32, 4)
            oprot.writeI32(self.ipLeased)
            oprot.writeFieldEnd()
        if self.ipTotal != None:
            oprot.writeFieldBegin('ipTotal', TType.I32, 5)
            oprot.writeI32(self.ipTotal)
            oprot.writeFieldEnd()
        if self.subnetType != None:
            oprot.writeFieldBegin('subnetType', TType.I32, 6)
            oprot.writeI32(self.subnetType)
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




class DhcpPoolParamIDL(object):
    """
    Attributes:
     - poolName
     - vrfName
     - poolType
    """

    thrift_spec = (None,
     (1,
      TType.STRING,
      'poolName',
      None,
      None),
     (2,
      TType.STRING,
      'vrfName',
      None,
      None),
     (3,
      TType.I16,
      'poolType',
      None,
      None))

    def __init__(self, poolName = None, vrfName = None, poolType = None):
        self.poolName = poolName
        self.vrfName = vrfName
        self.poolType = poolType



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
                    self.poolName = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.vrfName = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I16:
                    self.poolType = iprot.readI16()
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
        oprot.writeStructBegin('DhcpPoolParamIDL')
        if self.poolName != None:
            oprot.writeFieldBegin('poolName', TType.STRING, 1)
            oprot.writeString(self.poolName)
            oprot.writeFieldEnd()
        if self.vrfName != None:
            oprot.writeFieldBegin('vrfName', TType.STRING, 2)
            oprot.writeString(self.vrfName)
            oprot.writeFieldEnd()
        if self.poolType != None:
            oprot.writeFieldBegin('poolType', TType.I16, 3)
            oprot.writeI16(self.poolType)
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




class DhcpDbAgentIDL(object):
    """
    Attributes:
     - upToDate
     - readTime
     - writeTime
     - writeDelay
     - timeOut
     - failures
     - successes
     - status
     - type
    """

    thrift_spec = (None,
     (1,
      TType.STRUCT,
      'upToDate',
      (Shared.ttypes.DateTimeIDL, Shared.ttypes.DateTimeIDL.thrift_spec),
      None),
     (2,
      TType.STRUCT,
      'readTime',
      (Shared.ttypes.DateTimeIDL, Shared.ttypes.DateTimeIDL.thrift_spec),
      None),
     (3,
      TType.STRUCT,
      'writeTime',
      (Shared.ttypes.DateTimeIDL, Shared.ttypes.DateTimeIDL.thrift_spec),
      None),
     (4,
      TType.I32,
      'writeDelay',
      None,
      None),
     (5,
      TType.I32,
      'timeOut',
      None,
      None),
     (6,
      TType.I32,
      'failures',
      None,
      None),
     (7,
      TType.I32,
      'successes',
      None,
      None),
     (8,
      TType.I32,
      'status',
      None,
      None),
     (9,
      TType.I32,
      'type',
      None,
      None))

    def __init__(self, upToDate = None, readTime = None, writeTime = None, writeDelay = None, timeOut = None, failures = None, successes = None, status = None, type = None):
        self.upToDate = upToDate
        self.readTime = readTime
        self.writeTime = writeTime
        self.writeDelay = writeDelay
        self.timeOut = timeOut
        self.failures = failures
        self.successes = successes
        self.status = status
        self.type = type



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
                    self.upToDate = Shared.ttypes.DateTimeIDL()
                    self.upToDate.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.readTime = Shared.ttypes.DateTimeIDL()
                    self.readTime.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRUCT:
                    self.writeTime = Shared.ttypes.DateTimeIDL()
                    self.writeTime.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.writeDelay = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.timeOut = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I32:
                    self.failures = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I32:
                    self.successes = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.I32:
                    self.status = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.I32:
                    self.type = iprot.readI32()
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
        oprot.writeStructBegin('DhcpDbAgentIDL')
        if self.upToDate != None:
            oprot.writeFieldBegin('upToDate', TType.STRUCT, 1)
            self.upToDate.write(oprot)
            oprot.writeFieldEnd()
        if self.readTime != None:
            oprot.writeFieldBegin('readTime', TType.STRUCT, 2)
            self.readTime.write(oprot)
            oprot.writeFieldEnd()
        if self.writeTime != None:
            oprot.writeFieldBegin('writeTime', TType.STRUCT, 3)
            self.writeTime.write(oprot)
            oprot.writeFieldEnd()
        if self.writeDelay != None:
            oprot.writeFieldBegin('writeDelay', TType.I32, 4)
            oprot.writeI32(self.writeDelay)
            oprot.writeFieldEnd()
        if self.timeOut != None:
            oprot.writeFieldBegin('timeOut', TType.I32, 5)
            oprot.writeI32(self.timeOut)
            oprot.writeFieldEnd()
        if self.failures != None:
            oprot.writeFieldBegin('failures', TType.I32, 6)
            oprot.writeI32(self.failures)
            oprot.writeFieldEnd()
        if self.successes != None:
            oprot.writeFieldBegin('successes', TType.I32, 7)
            oprot.writeI32(self.successes)
            oprot.writeFieldEnd()
        if self.status != None:
            oprot.writeFieldBegin('status', TType.I32, 8)
            oprot.writeI32(self.status)
            oprot.writeFieldEnd()
        if self.type != None:
            oprot.writeFieldBegin('type', TType.I32, 9)
            oprot.writeI32(self.type)
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




class DhcpExclusionIDL(object):
    """
    Attributes:
     - lowAddress
     - highAddress
     - type
     - count
    """

    thrift_spec = (None,
     (1,
      TType.STRUCT,
      'lowAddress',
      (Shared.ttypes.NetworkAddressIDL, Shared.ttypes.NetworkAddressIDL.thrift_spec),
      None),
     (2,
      TType.STRUCT,
      'highAddress',
      (Shared.ttypes.NetworkAddressIDL, Shared.ttypes.NetworkAddressIDL.thrift_spec),
      None),
     (3,
      TType.I16,
      'type',
      None,
      None),
     (4,
      TType.I32,
      'count',
      None,
      None))

    def __init__(self, lowAddress = None, highAddress = None, type = None, count = None):
        self.lowAddress = lowAddress
        self.highAddress = highAddress
        self.type = type
        self.count = count



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
                    self.lowAddress = Shared.ttypes.NetworkAddressIDL()
                    self.lowAddress.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.highAddress = Shared.ttypes.NetworkAddressIDL()
                    self.highAddress.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I16:
                    self.type = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.count = iprot.readI32()
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
        oprot.writeStructBegin('DhcpExclusionIDL')
        if self.lowAddress != None:
            oprot.writeFieldBegin('lowAddress', TType.STRUCT, 1)
            self.lowAddress.write(oprot)
            oprot.writeFieldEnd()
        if self.highAddress != None:
            oprot.writeFieldBegin('highAddress', TType.STRUCT, 2)
            self.highAddress.write(oprot)
            oprot.writeFieldEnd()
        if self.type != None:
            oprot.writeFieldBegin('type', TType.I16, 3)
            oprot.writeI16(self.type)
            oprot.writeFieldEnd()
        if self.count != None:
            oprot.writeFieldBegin('count', TType.I32, 4)
            oprot.writeI32(self.count)
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




class DhcpNwNodeIDL(object):
    """
    Attributes:
     - nwPrefix
     - nwType
    """

    thrift_spec = (None, (1,
      TType.STRUCT,
      'nwPrefix',
      (Shared.ttypes.NetworkPrefixIDL, Shared.ttypes.NetworkPrefixIDL.thrift_spec),
      None), (2,
      TType.I32,
      'nwType',
      None,
      None))

    def __init__(self, nwPrefix = None, nwType = None):
        self.nwPrefix = nwPrefix
        self.nwType = nwType



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
                    self.nwPrefix = Shared.ttypes.NetworkPrefixIDL()
                    self.nwPrefix.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.nwType = iprot.readI32()
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
        oprot.writeStructBegin('DhcpNwNodeIDL')
        if self.nwPrefix != None:
            oprot.writeFieldBegin('nwPrefix', TType.STRUCT, 1)
            self.nwPrefix.write(oprot)
            oprot.writeFieldEnd()
        if self.nwType != None:
            oprot.writeFieldBegin('nwType', TType.I32, 2)
            oprot.writeI32(self.nwType)
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
# 2015.02.05 17:18:15 IST
