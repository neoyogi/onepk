# 2015.02.05 17:22:54 IST
from thrift.Thrift import *
import SharedOut.ttypes
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
    from thrift.protocol import fastbinary
except:
    fastbinary = None

class ProbeStatsOutIDL(object):
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
     - owSdMax
     - owDs
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
      'owSdMax',
      None,
      None),
     (11,
      TType.I64,
      'owDs',
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

    def __init__(self, probeId = None, probeType = None, timeStamp = None, returnCode = None, rtt = None, rttMin = None, rttMax = None, owSd = None, owSdMin = None, owSdMax = None, owDs = None, owDsMin = None, owDsMax = None):
        self.probeId = probeId
        self.probeType = probeType
        self.timeStamp = timeStamp
        self.returnCode = returnCode
        self.rtt = rtt
        self.rttMin = rttMin
        self.rttMax = rttMax
        self.owSd = owSd
        self.owSdMin = owSdMin
        self.owSdMax = owSdMax
        self.owDs = owDs
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
                    self.owSdMax = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.I64:
                    self.owDs = iprot.readI64()
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
        oprot.writeStructBegin('ProbeStatsOutIDL')
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
        if self.owSdMax != None:
            oprot.writeFieldBegin('owSdMax', TType.I64, 10)
            oprot.writeI64(self.owSdMax)
            oprot.writeFieldEnd()
        if self.owDs != None:
            oprot.writeFieldBegin('owDs', TType.I64, 11)
            oprot.writeI64(self.owDs)
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




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:22:55 IST
