# 2015.02.05 17:22:08 IST
from thrift.Thrift import *
import Shared.ttypes
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
    from thrift.protocol import fastbinary
except:
    fastbinary = None

class NtpServerIDL(object):
    """
    Attributes:
     - address
     - hostname
     - authKey
     - mode
     - vrfName
    """

    thrift_spec = (None,
     (1,
      TType.STRUCT,
      'address',
      (Shared.ttypes.NetworkAddressIDL, Shared.ttypes.NetworkAddressIDL.thrift_spec),
      None),
     (2,
      TType.STRING,
      'hostname',
      None,
      None),
     (3,
      TType.I32,
      'authKey',
      None,
      None),
     (4,
      TType.I32,
      'mode',
      None,
      None),
     (5,
      TType.STRING,
      'vrfName',
      None,
      None))

    def __init__(self, address = None, hostname = None, authKey = None, mode = None, vrfName = None):
        self.address = address
        self.hostname = hostname
        self.authKey = authKey
        self.mode = mode
        self.vrfName = vrfName



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
                    self.address = Shared.ttypes.NetworkAddressIDL()
                    self.address.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.hostname = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.authKey = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.mode = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.vrfName = iprot.readString()
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
        oprot.writeStructBegin('NtpServerIDL')
        if self.address != None:
            oprot.writeFieldBegin('address', TType.STRUCT, 1)
            self.address.write(oprot)
            oprot.writeFieldEnd()
        if self.hostname != None:
            oprot.writeFieldBegin('hostname', TType.STRING, 2)
            oprot.writeString(self.hostname)
            oprot.writeFieldEnd()
        if self.authKey != None:
            oprot.writeFieldBegin('authKey', TType.I32, 3)
            oprot.writeI32(self.authKey)
            oprot.writeFieldEnd()
        if self.mode != None:
            oprot.writeFieldBegin('mode', TType.I32, 4)
            oprot.writeI32(self.mode)
            oprot.writeFieldEnd()
        if self.vrfName != None:
            oprot.writeFieldBegin('vrfName', TType.STRING, 5)
            oprot.writeString(self.vrfName)
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




class NtpAssociationIDL(object):
    """
    Attributes:
     - peer_info
     - address
     - refClock
     - stratum
     - ntpWhen
     - poll
     - reach
     - delay
     - dispersion
     - offset
    """

    thrift_spec = (None,
     (1,
      TType.STRING,
      'peer_info',
      None,
      None),
     (2,
      TType.STRUCT,
      'address',
      (Shared.ttypes.NetworkAddressIDL, Shared.ttypes.NetworkAddressIDL.thrift_spec),
      None),
     (3,
      TType.STRING,
      'refClock',
      None,
      None),
     (4,
      TType.I32,
      'stratum',
      None,
      None),
     (5,
      TType.I32,
      'ntpWhen',
      None,
      None),
     (6,
      TType.I32,
      'poll',
      None,
      None),
     (7,
      TType.STRING,
      'reach',
      None,
      None),
     (8,
      TType.STRING,
      'delay',
      None,
      None),
     (9,
      TType.STRING,
      'dispersion',
      None,
      None),
     (10,
      TType.STRING,
      'offset',
      None,
      None))

    def __init__(self, peer_info = None, address = None, refClock = None, stratum = None, ntpWhen = None, poll = None, reach = None, delay = None, dispersion = None, offset = None):
        self.peer_info = peer_info
        self.address = address
        self.refClock = refClock
        self.stratum = stratum
        self.ntpWhen = ntpWhen
        self.poll = poll
        self.reach = reach
        self.delay = delay
        self.dispersion = dispersion
        self.offset = offset



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
                    self.peer_info = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.address = Shared.ttypes.NetworkAddressIDL()
                    self.address.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.refClock = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.stratum = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.ntpWhen = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I32:
                    self.poll = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.STRING:
                    self.reach = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.STRING:
                    self.delay = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.STRING:
                    self.dispersion = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.STRING:
                    self.offset = iprot.readString()
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
        oprot.writeStructBegin('NtpAssociationIDL')
        if self.peer_info != None:
            oprot.writeFieldBegin('peer_info', TType.STRING, 1)
            oprot.writeString(self.peer_info)
            oprot.writeFieldEnd()
        if self.address != None:
            oprot.writeFieldBegin('address', TType.STRUCT, 2)
            self.address.write(oprot)
            oprot.writeFieldEnd()
        if self.refClock != None:
            oprot.writeFieldBegin('refClock', TType.STRING, 3)
            oprot.writeString(self.refClock)
            oprot.writeFieldEnd()
        if self.stratum != None:
            oprot.writeFieldBegin('stratum', TType.I32, 4)
            oprot.writeI32(self.stratum)
            oprot.writeFieldEnd()
        if self.ntpWhen != None:
            oprot.writeFieldBegin('ntpWhen', TType.I32, 5)
            oprot.writeI32(self.ntpWhen)
            oprot.writeFieldEnd()
        if self.poll != None:
            oprot.writeFieldBegin('poll', TType.I32, 6)
            oprot.writeI32(self.poll)
            oprot.writeFieldEnd()
        if self.reach != None:
            oprot.writeFieldBegin('reach', TType.STRING, 7)
            oprot.writeString(self.reach)
            oprot.writeFieldEnd()
        if self.delay != None:
            oprot.writeFieldBegin('delay', TType.STRING, 8)
            oprot.writeString(self.delay)
            oprot.writeFieldEnd()
        if self.dispersion != None:
            oprot.writeFieldBegin('dispersion', TType.STRING, 9)
            oprot.writeString(self.dispersion)
            oprot.writeFieldEnd()
        if self.offset != None:
            oprot.writeFieldBegin('offset', TType.STRING, 10)
            oprot.writeString(self.offset)
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




class NtpStatusIDL(object):
    """
    Attributes:
     - synced
     - stratum
     - reference
     - nominalFreq
     - actualFreq
     - precision
     - ntpUptime
     - resolution
     - referenceTime
     - clockOffset
     - rootDelay
     - rootDispersion
     - peerDispersion
     - loopfilterSate
     - drift
     - poll_int
     - lastUptime
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'synced',
      None,
      None),
     (2,
      TType.I32,
      'stratum',
      None,
      None),
     (3,
      TType.STRING,
      'reference',
      None,
      None),
     (4,
      TType.STRING,
      'nominalFreq',
      None,
      None),
     (5,
      TType.STRING,
      'actualFreq',
      None,
      None),
     (6,
      TType.I32,
      'precision',
      None,
      None),
     (7,
      TType.I32,
      'ntpUptime',
      None,
      None),
     (8,
      TType.I32,
      'resolution',
      None,
      None),
     (9,
      TType.STRING,
      'referenceTime',
      None,
      None),
     (10,
      TType.STRING,
      'clockOffset',
      None,
      None),
     (11,
      TType.STRING,
      'rootDelay',
      None,
      None),
     (12,
      TType.STRING,
      'rootDispersion',
      None,
      None),
     (13,
      TType.STRING,
      'peerDispersion',
      None,
      None),
     (14,
      TType.STRING,
      'loopfilterSate',
      None,
      None),
     (15,
      TType.STRING,
      'drift',
      None,
      None),
     (16,
      TType.I32,
      'poll_int',
      None,
      None),
     (17,
      TType.I32,
      'lastUptime',
      None,
      None))

    def __init__(self, synced = None, stratum = None, reference = None, nominalFreq = None, actualFreq = None, precision = None, ntpUptime = None, resolution = None, referenceTime = None, clockOffset = None, rootDelay = None, rootDispersion = None, peerDispersion = None, loopfilterSate = None, drift = None, poll_int = None, lastUptime = None):
        self.synced = synced
        self.stratum = stratum
        self.reference = reference
        self.nominalFreq = nominalFreq
        self.actualFreq = actualFreq
        self.precision = precision
        self.ntpUptime = ntpUptime
        self.resolution = resolution
        self.referenceTime = referenceTime
        self.clockOffset = clockOffset
        self.rootDelay = rootDelay
        self.rootDispersion = rootDispersion
        self.peerDispersion = peerDispersion
        self.loopfilterSate = loopfilterSate
        self.drift = drift
        self.poll_int = poll_int
        self.lastUptime = lastUptime



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
                    self.synced = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.stratum = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.reference = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.nominalFreq = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.actualFreq = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I32:
                    self.precision = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I32:
                    self.ntpUptime = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.I32:
                    self.resolution = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.STRING:
                    self.referenceTime = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.STRING:
                    self.clockOffset = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.STRING:
                    self.rootDelay = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 12:
                if ftype == TType.STRING:
                    self.rootDispersion = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 13:
                if ftype == TType.STRING:
                    self.peerDispersion = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 14:
                if ftype == TType.STRING:
                    self.loopfilterSate = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 15:
                if ftype == TType.STRING:
                    self.drift = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 16:
                if ftype == TType.I32:
                    self.poll_int = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 17:
                if ftype == TType.I32:
                    self.lastUptime = iprot.readI32()
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
        oprot.writeStructBegin('NtpStatusIDL')
        if self.synced != None:
            oprot.writeFieldBegin('synced', TType.I32, 1)
            oprot.writeI32(self.synced)
            oprot.writeFieldEnd()
        if self.stratum != None:
            oprot.writeFieldBegin('stratum', TType.I32, 2)
            oprot.writeI32(self.stratum)
            oprot.writeFieldEnd()
        if self.reference != None:
            oprot.writeFieldBegin('reference', TType.STRING, 3)
            oprot.writeString(self.reference)
            oprot.writeFieldEnd()
        if self.nominalFreq != None:
            oprot.writeFieldBegin('nominalFreq', TType.STRING, 4)
            oprot.writeString(self.nominalFreq)
            oprot.writeFieldEnd()
        if self.actualFreq != None:
            oprot.writeFieldBegin('actualFreq', TType.STRING, 5)
            oprot.writeString(self.actualFreq)
            oprot.writeFieldEnd()
        if self.precision != None:
            oprot.writeFieldBegin('precision', TType.I32, 6)
            oprot.writeI32(self.precision)
            oprot.writeFieldEnd()
        if self.ntpUptime != None:
            oprot.writeFieldBegin('ntpUptime', TType.I32, 7)
            oprot.writeI32(self.ntpUptime)
            oprot.writeFieldEnd()
        if self.resolution != None:
            oprot.writeFieldBegin('resolution', TType.I32, 8)
            oprot.writeI32(self.resolution)
            oprot.writeFieldEnd()
        if self.referenceTime != None:
            oprot.writeFieldBegin('referenceTime', TType.STRING, 9)
            oprot.writeString(self.referenceTime)
            oprot.writeFieldEnd()
        if self.clockOffset != None:
            oprot.writeFieldBegin('clockOffset', TType.STRING, 10)
            oprot.writeString(self.clockOffset)
            oprot.writeFieldEnd()
        if self.rootDelay != None:
            oprot.writeFieldBegin('rootDelay', TType.STRING, 11)
            oprot.writeString(self.rootDelay)
            oprot.writeFieldEnd()
        if self.rootDispersion != None:
            oprot.writeFieldBegin('rootDispersion', TType.STRING, 12)
            oprot.writeString(self.rootDispersion)
            oprot.writeFieldEnd()
        if self.peerDispersion != None:
            oprot.writeFieldBegin('peerDispersion', TType.STRING, 13)
            oprot.writeString(self.peerDispersion)
            oprot.writeFieldEnd()
        if self.loopfilterSate != None:
            oprot.writeFieldBegin('loopfilterSate', TType.STRING, 14)
            oprot.writeString(self.loopfilterSate)
            oprot.writeFieldEnd()
        if self.drift != None:
            oprot.writeFieldBegin('drift', TType.STRING, 15)
            oprot.writeString(self.drift)
            oprot.writeFieldEnd()
        if self.poll_int != None:
            oprot.writeFieldBegin('poll_int', TType.I32, 16)
            oprot.writeI32(self.poll_int)
            oprot.writeFieldEnd()
        if self.lastUptime != None:
            oprot.writeFieldBegin('lastUptime', TType.I32, 17)
            oprot.writeI32(self.lastUptime)
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
# 2015.02.05 17:22:09 IST
