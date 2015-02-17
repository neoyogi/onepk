# 2015.02.05 17:22:56 IST
from thrift.Thrift import *
import Shared.ttypes
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
    from thrift.protocol import fastbinary
except:
    fastbinary = None

class ProbeL2PTPIDL(object):
    """
    Attributes:
     - srcMac
     - dstMac
     - vlan
     - cos
     - ifHandle
    """

    thrift_spec = (None,
     (1,
      TType.LIST,
      'srcMac',
      (TType.BYTE, None),
      None),
     (2,
      TType.LIST,
      'dstMac',
      (TType.BYTE, None),
      None),
     (3,
      TType.I32,
      'vlan',
      None,
      None),
     (4,
      TType.I32,
      'cos',
      None,
      None),
     (5,
      TType.I64,
      'ifHandle',
      None,
      None))

    def __init__(self, srcMac = None, dstMac = None, vlan = None, cos = None, ifHandle = None):
        self.srcMac = srcMac
        self.dstMac = dstMac
        self.vlan = vlan
        self.cos = cos
        self.ifHandle = ifHandle



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
                    self.srcMac = []
                    (_etype3, _size0,) = iprot.readListBegin()
                    for _i4 in xrange(_size0):
                        _elem5 = iprot.readByte()
                        self.srcMac.append(_elem5)

                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.dstMac = []
                    (_etype9, _size6,) = iprot.readListBegin()
                    for _i10 in xrange(_size6):
                        _elem11 = iprot.readByte()
                        self.dstMac.append(_elem11)

                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.vlan = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.cos = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I64:
                    self.ifHandle = iprot.readI64()
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
        oprot.writeStructBegin('ProbeL2PTPIDL')
        if self.srcMac != None:
            oprot.writeFieldBegin('srcMac', TType.LIST, 1)
            oprot.writeListBegin(TType.BYTE, len(self.srcMac))
            for iter12 in self.srcMac:
                oprot.writeByte(iter12)

            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.dstMac != None:
            oprot.writeFieldBegin('dstMac', TType.LIST, 2)
            oprot.writeListBegin(TType.BYTE, len(self.dstMac))
            for iter13 in self.dstMac:
                oprot.writeByte(iter13)

            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.vlan != None:
            oprot.writeFieldBegin('vlan', TType.I32, 3)
            oprot.writeI32(self.vlan)
            oprot.writeFieldEnd()
        if self.cos != None:
            oprot.writeFieldBegin('cos', TType.I32, 4)
            oprot.writeI32(self.cos)
            oprot.writeFieldEnd()
        if self.ifHandle != None:
            oprot.writeFieldBegin('ifHandle', TType.I64, 5)
            oprot.writeI64(self.ifHandle)
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




class ProbeOperIDL(object):
    """
    Attributes:
     - probeType
     - packets
     - interval
     - timeout
     - L2PTP
    """

    thrift_spec = (None,
     (1,
      TType.I16,
      'probeType',
      None,
      None),
     (2,
      TType.I32,
      'packets',
      None,
      None),
     (3,
      TType.I32,
      'interval',
      None,
      None),
     (4,
      TType.I32,
      'timeout',
      None,
      None),
     (5,
      TType.STRUCT,
      'L2PTP',
      (ProbeL2PTPIDL, ProbeL2PTPIDL.thrift_spec),
      None))

    def __init__(self, probeType = None, packets = None, interval = None, timeout = None, L2PTP = None):
        self.probeType = probeType
        self.packets = packets
        self.interval = interval
        self.timeout = timeout
        self.L2PTP = L2PTP



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
                    self.probeType = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.packets = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.interval = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.timeout = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRUCT:
                    self.L2PTP = ProbeL2PTPIDL()
                    self.L2PTP.read(iprot)
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
        oprot.writeStructBegin('ProbeOperIDL')
        if self.probeType != None:
            oprot.writeFieldBegin('probeType', TType.I16, 1)
            oprot.writeI16(self.probeType)
            oprot.writeFieldEnd()
        if self.packets != None:
            oprot.writeFieldBegin('packets', TType.I32, 2)
            oprot.writeI32(self.packets)
            oprot.writeFieldEnd()
        if self.interval != None:
            oprot.writeFieldBegin('interval', TType.I32, 3)
            oprot.writeI32(self.interval)
            oprot.writeFieldEnd()
        if self.timeout != None:
            oprot.writeFieldBegin('timeout', TType.I32, 4)
            oprot.writeI32(self.timeout)
            oprot.writeFieldEnd()
        if self.L2PTP != None:
            oprot.writeFieldBegin('L2PTP', TType.STRUCT, 5)
            self.L2PTP.write(oprot)
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




class ProbeSchedulerIDL(object):
    """
    Attributes:
     - startType
     - recurring
     - afterDuration
     - period
     - ageout
     - life
    """

    thrift_spec = (None,
     (1,
      TType.BYTE,
      'startType',
      None,
      None),
     (2,
      TType.BYTE,
      'recurring',
      None,
      None),
     (3,
      TType.I32,
      'afterDuration',
      None,
      None),
     (4,
      TType.I64,
      'period',
      None,
      None),
     (5,
      TType.I32,
      'ageout',
      None,
      None),
     (6,
      TType.I64,
      'life',
      None,
      None))

    def __init__(self, startType = None, recurring = None, afterDuration = None, period = None, ageout = None, life = None):
        self.startType = startType
        self.recurring = recurring
        self.afterDuration = afterDuration
        self.period = period
        self.ageout = ageout
        self.life = life



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
                    self.startType = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.BYTE:
                    self.recurring = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.afterDuration = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I64:
                    self.period = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.ageout = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I64:
                    self.life = iprot.readI64()
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
        oprot.writeStructBegin('ProbeSchedulerIDL')
        if self.startType != None:
            oprot.writeFieldBegin('startType', TType.BYTE, 1)
            oprot.writeByte(self.startType)
            oprot.writeFieldEnd()
        if self.recurring != None:
            oprot.writeFieldBegin('recurring', TType.BYTE, 2)
            oprot.writeByte(self.recurring)
            oprot.writeFieldEnd()
        if self.afterDuration != None:
            oprot.writeFieldBegin('afterDuration', TType.I32, 3)
            oprot.writeI32(self.afterDuration)
            oprot.writeFieldEnd()
        if self.period != None:
            oprot.writeFieldBegin('period', TType.I64, 4)
            oprot.writeI64(self.period)
            oprot.writeFieldEnd()
        if self.ageout != None:
            oprot.writeFieldBegin('ageout', TType.I32, 5)
            oprot.writeI32(self.ageout)
            oprot.writeFieldEnd()
        if self.life != None:
            oprot.writeFieldBegin('life', TType.I64, 6)
            oprot.writeI64(self.life)
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




class ProbeFilterIDL(object):
    """
    Attributes:
     - filterType
     - probeType
    """

    thrift_spec = (None, (1,
      TType.I16,
      'filterType',
      None,
      None), (2,
      TType.I16,
      'probeType',
      None,
      None))

    def __init__(self, filterType = None, probeType = None):
        self.filterType = filterType
        self.probeType = probeType



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
                    self.filterType = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I16:
                    self.probeType = iprot.readI16()
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
        oprot.writeStructBegin('ProbeFilterIDL')
        if self.filterType != None:
            oprot.writeFieldBegin('filterType', TType.I16, 1)
            oprot.writeI16(self.filterType)
            oprot.writeFieldEnd()
        if self.probeType != None:
            oprot.writeFieldBegin('probeType', TType.I16, 2)
            oprot.writeI16(self.probeType)
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




class ProbeIDL(object):
    """
    Attributes:
     - probeId
     - oper
     - scheduler
     - filterList
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'probeId',
      None,
      None),
     (2,
      TType.STRUCT,
      'oper',
      (ProbeOperIDL, ProbeOperIDL.thrift_spec),
      None),
     (3,
      TType.STRUCT,
      'scheduler',
      (ProbeSchedulerIDL, ProbeSchedulerIDL.thrift_spec),
      None),
     (4,
      TType.LIST,
      'filterList',
      (TType.STRUCT, (ProbeFilterIDL, ProbeFilterIDL.thrift_spec)),
      None))

    def __init__(self, probeId = None, oper = None, scheduler = None, filterList = None):
        self.probeId = probeId
        self.oper = oper
        self.scheduler = scheduler
        self.filterList = filterList



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
                    self.probeId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.oper = ProbeOperIDL()
                    self.oper.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRUCT:
                    self.scheduler = ProbeSchedulerIDL()
                    self.scheduler.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.LIST:
                    self.filterList = []
                    (_etype17, _size14,) = iprot.readListBegin()
                    for _i18 in xrange(_size14):
                        _elem19 = ProbeFilterIDL()
                        _elem19.read(iprot)
                        self.filterList.append(_elem19)

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
        oprot.writeStructBegin('ProbeIDL')
        if self.probeId != None:
            oprot.writeFieldBegin('probeId', TType.I32, 1)
            oprot.writeI32(self.probeId)
            oprot.writeFieldEnd()
        if self.oper != None:
            oprot.writeFieldBegin('oper', TType.STRUCT, 2)
            self.oper.write(oprot)
            oprot.writeFieldEnd()
        if self.scheduler != None:
            oprot.writeFieldBegin('scheduler', TType.STRUCT, 3)
            self.scheduler.write(oprot)
            oprot.writeFieldEnd()
        if self.filterList != None:
            oprot.writeFieldBegin('filterList', TType.LIST, 4)
            oprot.writeListBegin(TType.STRUCT, len(self.filterList))
            for iter20 in self.filterList:
                iter20.write(oprot)

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




class ProbeStatsIDL(object):
    """
    Attributes:
     - probeId
     - probeType
     - timeStamp
     - returnCode
     - rtt
     - rttMin
     - rttMax
     - owSd
     - owSdMin
     - owDs
     - owSdMax
     - owDsMin
     - owDsMax
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'probeId',
      None,
      None),
     (2,
      TType.I16,
      'probeType',
      None,
      None),
     (3,
      TType.I64,
      'timeStamp',
      None,
      None),
     (4,
      TType.I32,
      'returnCode',
      None,
      None),
     (5,
      TType.I64,
      'rtt',
      None,
      None),
     (6,
      TType.I64,
      'rttMin',
      None,
      None),
     (7,
      TType.I64,
      'rttMax',
      None,
      None),
     (8,
      TType.I64,
      'owSd',
      None,
      None),
     (9,
      TType.I64,
      'owSdMin',
      None,
      None),
     (10,
      TType.I64,
      'owDs',
      None,
      None),
     (11,
      TType.I64,
      'owSdMax',
      None,
      None),
     (12,
      TType.I64,
      'owDsMin',
      None,
      None),
     (13,
      TType.I64,
      'owDsMax',
      None,
      None))

    def __init__(self, probeId = None, probeType = None, timeStamp = None, returnCode = None, rtt = None, rttMin = None, rttMax = None, owSd = None, owSdMin = None, owDs = None, owSdMax = None, owDsMin = None, owDsMax = None):
        self.probeId = probeId
        self.probeType = probeType
        self.timeStamp = timeStamp
        self.returnCode = returnCode
        self.rtt = rtt
        self.rttMin = rttMin
        self.rttMax = rttMax
        self.owSd = owSd
        self.owSdMin = owSdMin
        self.owDs = owDs
        self.owSdMax = owSdMax
        self.owDsMin = owDsMin
        self.owDsMax = owDsMax



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
                    self.probeId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I16:
                    self.probeType = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I64:
                    self.timeStamp = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.returnCode = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I64:
                    self.rtt = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I64:
                    self.rttMin = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I64:
                    self.rttMax = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.I64:
                    self.owSd = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.I64:
                    self.owSdMin = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.I64:
                    self.owDs = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.I64:
                    self.owSdMax = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 12:
                if ftype == TType.I64:
                    self.owDsMin = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 13:
                if ftype == TType.I64:
                    self.owDsMax = iprot.readI64()
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
        oprot.writeStructBegin('ProbeStatsIDL')
        if self.probeId != None:
            oprot.writeFieldBegin('probeId', TType.I32, 1)
            oprot.writeI32(self.probeId)
            oprot.writeFieldEnd()
        if self.probeType != None:
            oprot.writeFieldBegin('probeType', TType.I16, 2)
            oprot.writeI16(self.probeType)
            oprot.writeFieldEnd()
        if self.timeStamp != None:
            oprot.writeFieldBegin('timeStamp', TType.I64, 3)
            oprot.writeI64(self.timeStamp)
            oprot.writeFieldEnd()
        if self.returnCode != None:
            oprot.writeFieldBegin('returnCode', TType.I32, 4)
            oprot.writeI32(self.returnCode)
            oprot.writeFieldEnd()
        if self.rtt != None:
            oprot.writeFieldBegin('rtt', TType.I64, 5)
            oprot.writeI64(self.rtt)
            oprot.writeFieldEnd()
        if self.rttMin != None:
            oprot.writeFieldBegin('rttMin', TType.I64, 6)
            oprot.writeI64(self.rttMin)
            oprot.writeFieldEnd()
        if self.rttMax != None:
            oprot.writeFieldBegin('rttMax', TType.I64, 7)
            oprot.writeI64(self.rttMax)
            oprot.writeFieldEnd()
        if self.owSd != None:
            oprot.writeFieldBegin('owSd', TType.I64, 8)
            oprot.writeI64(self.owSd)
            oprot.writeFieldEnd()
        if self.owSdMin != None:
            oprot.writeFieldBegin('owSdMin', TType.I64, 9)
            oprot.writeI64(self.owSdMin)
            oprot.writeFieldEnd()
        if self.owDs != None:
            oprot.writeFieldBegin('owDs', TType.I64, 10)
            oprot.writeI64(self.owDs)
            oprot.writeFieldEnd()
        if self.owSdMax != None:
            oprot.writeFieldBegin('owSdMax', TType.I64, 11)
            oprot.writeI64(self.owSdMax)
            oprot.writeFieldEnd()
        if self.owDsMin != None:
            oprot.writeFieldBegin('owDsMin', TType.I64, 12)
            oprot.writeI64(self.owDsMin)
            oprot.writeFieldEnd()
        if self.owDsMax != None:
            oprot.writeFieldBegin('owDsMax', TType.I64, 13)
            oprot.writeI64(self.owDsMax)
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




class ProbeHandleIDL(object):
    """
    Attributes:
     - probeId
     - eventHandle
    """

    thrift_spec = (None, (1,
      TType.I32,
      'probeId',
      None,
      None), (2,
      TType.I32,
      'eventHandle',
      None,
      None))

    def __init__(self, probeId = None, eventHandle = None):
        self.probeId = probeId
        self.eventHandle = eventHandle



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
                    self.probeId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.eventHandle = iprot.readI32()
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
        oprot.writeStructBegin('ProbeHandleIDL')
        if self.probeId != None:
            oprot.writeFieldBegin('probeId', TType.I32, 1)
            oprot.writeI32(self.probeId)
            oprot.writeFieldEnd()
        if self.eventHandle != None:
            oprot.writeFieldBegin('eventHandle', TType.I32, 2)
            oprot.writeI32(self.eventHandle)
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
# 2015.02.05 17:22:57 IST
