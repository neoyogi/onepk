# 2015.02.05 17:18:31 IST
from thrift.Thrift import *
import Shared.ttypes
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
    from thrift.protocol import fastbinary
except:
    fastbinary = None

class ValidityPeriodIDL(object):
    """
    Attributes:
     - weeks
     - days
     - hours
     - minutes
     - seconds
    """

    thrift_spec = (None,
     (1,
      TType.I16,
      'weeks',
      None,
      None),
     (2,
      TType.I16,
      'days',
      None,
      None),
     (3,
      TType.I16,
      'hours',
      None,
      None),
     (4,
      TType.I16,
      'minutes',
      None,
      None),
     (5,
      TType.I16,
      'seconds',
      None,
      None))

    def __init__(self, weeks = None, days = None, hours = None, minutes = None, seconds = None):
        self.weeks = weeks
        self.days = days
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds



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
                    self.weeks = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I16:
                    self.days = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I16:
                    self.hours = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I16:
                    self.minutes = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I16:
                    self.seconds = iprot.readI16()
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
        oprot.writeStructBegin('ValidityPeriodIDL')
        if self.weeks != None:
            oprot.writeFieldBegin('weeks', TType.I16, 1)
            oprot.writeI16(self.weeks)
            oprot.writeFieldEnd()
        if self.days != None:
            oprot.writeFieldBegin('days', TType.I16, 2)
            oprot.writeI16(self.days)
            oprot.writeFieldEnd()
        if self.hours != None:
            oprot.writeFieldBegin('hours', TType.I16, 3)
            oprot.writeI16(self.hours)
            oprot.writeFieldEnd()
        if self.minutes != None:
            oprot.writeFieldBegin('minutes', TType.I16, 4)
            oprot.writeI16(self.minutes)
            oprot.writeFieldEnd()
        if self.seconds != None:
            oprot.writeFieldBegin('seconds', TType.I16, 5)
            oprot.writeI16(self.seconds)
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




class LicenseInfoIDL(object):
    """
    Attributes:
     - feature
     - licenseType
     - endDate
     - periodLeft
     - licenseState
     - isCounted
     - count
     - usage
    """

    thrift_spec = (None,
     (1,
      TType.STRING,
      'feature',
      None,
      None),
     (2,
      TType.I32,
      'licenseType',
      None,
      None),
     (3,
      TType.STRUCT,
      'endDate',
      (Shared.ttypes.DateTimeIDL, Shared.ttypes.DateTimeIDL.thrift_spec),
      None),
     (4,
      TType.STRUCT,
      'periodLeft',
      (ValidityPeriodIDL, ValidityPeriodIDL.thrift_spec),
      None),
     (5,
      TType.I32,
      'licenseState',
      None,
      None),
     (6,
      TType.I32,
      'isCounted',
      None,
      None),
     (7,
      TType.I32,
      'count',
      None,
      None),
     (8,
      TType.I32,
      'usage',
      None,
      None))

    def __init__(self, feature = None, licenseType = None, endDate = None, periodLeft = None, licenseState = None, isCounted = None, count = None, usage = None):
        self.feature = feature
        self.licenseType = licenseType
        self.endDate = endDate
        self.periodLeft = periodLeft
        self.licenseState = licenseState
        self.isCounted = isCounted
        self.count = count
        self.usage = usage



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
                    self.feature = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.licenseType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRUCT:
                    self.endDate = Shared.ttypes.DateTimeIDL()
                    self.endDate.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRUCT:
                    self.periodLeft = ValidityPeriodIDL()
                    self.periodLeft.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.licenseState = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I32:
                    self.isCounted = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I32:
                    self.count = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.I32:
                    self.usage = iprot.readI32()
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
        oprot.writeStructBegin('LicenseInfoIDL')
        if self.feature != None:
            oprot.writeFieldBegin('feature', TType.STRING, 1)
            oprot.writeString(self.feature)
            oprot.writeFieldEnd()
        if self.licenseType != None:
            oprot.writeFieldBegin('licenseType', TType.I32, 2)
            oprot.writeI32(self.licenseType)
            oprot.writeFieldEnd()
        if self.endDate != None:
            oprot.writeFieldBegin('endDate', TType.STRUCT, 3)
            self.endDate.write(oprot)
            oprot.writeFieldEnd()
        if self.periodLeft != None:
            oprot.writeFieldBegin('periodLeft', TType.STRUCT, 4)
            self.periodLeft.write(oprot)
            oprot.writeFieldEnd()
        if self.licenseState != None:
            oprot.writeFieldBegin('licenseState', TType.I32, 5)
            oprot.writeI32(self.licenseState)
            oprot.writeFieldEnd()
        if self.isCounted != None:
            oprot.writeFieldBegin('isCounted', TType.I32, 6)
            oprot.writeI32(self.isCounted)
            oprot.writeFieldEnd()
        if self.count != None:
            oprot.writeFieldBegin('count', TType.I32, 7)
            oprot.writeI32(self.count)
            oprot.writeFieldEnd()
        if self.usage != None:
            oprot.writeFieldBegin('usage', TType.I32, 8)
            oprot.writeI32(self.usage)
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




class LicenseDetailIDL(object):
    """
    Attributes:
     - storageName
     - featureVersion
     - storeIndex
     - startDate
     - validityPeriod
     - lockType
     - vendor
     - addition
     - priority
     - licInfo
    """

    thrift_spec = (None,
     (1,
      TType.STRING,
      'storageName',
      None,
      None),
     (2,
      TType.STRING,
      'featureVersion',
      None,
      None),
     (3,
      TType.I32,
      'storeIndex',
      None,
      None),
     (4,
      TType.STRUCT,
      'startDate',
      (Shared.ttypes.DateTimeIDL, Shared.ttypes.DateTimeIDL.thrift_spec),
      None),
     (5,
      TType.STRUCT,
      'validityPeriod',
      (ValidityPeriodIDL, ValidityPeriodIDL.thrift_spec),
      None),
     (6,
      TType.STRING,
      'lockType',
      None,
      None),
     (7,
      TType.STRING,
      'vendor',
      None,
      None),
     (8,
      TType.STRING,
      'addition',
      None,
      None),
     (9,
      TType.STRING,
      'priority',
      None,
      None),
     (10,
      TType.STRUCT,
      'licInfo',
      (LicenseInfoIDL, LicenseInfoIDL.thrift_spec),
      None))

    def __init__(self, storageName = None, featureVersion = None, storeIndex = None, startDate = None, validityPeriod = None, lockType = None, vendor = None, addition = None, priority = None, licInfo = None):
        self.storageName = storageName
        self.featureVersion = featureVersion
        self.storeIndex = storeIndex
        self.startDate = startDate
        self.validityPeriod = validityPeriod
        self.lockType = lockType
        self.vendor = vendor
        self.addition = addition
        self.priority = priority
        self.licInfo = licInfo



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
                    self.storageName = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.featureVersion = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.storeIndex = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRUCT:
                    self.startDate = Shared.ttypes.DateTimeIDL()
                    self.startDate.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRUCT:
                    self.validityPeriod = ValidityPeriodIDL()
                    self.validityPeriod.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRING:
                    self.lockType = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.STRING:
                    self.vendor = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.STRING:
                    self.addition = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.STRING:
                    self.priority = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.STRUCT:
                    self.licInfo = LicenseInfoIDL()
                    self.licInfo.read(iprot)
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
        oprot.writeStructBegin('LicenseDetailIDL')
        if self.storageName != None:
            oprot.writeFieldBegin('storageName', TType.STRING, 1)
            oprot.writeString(self.storageName)
            oprot.writeFieldEnd()
        if self.featureVersion != None:
            oprot.writeFieldBegin('featureVersion', TType.STRING, 2)
            oprot.writeString(self.featureVersion)
            oprot.writeFieldEnd()
        if self.storeIndex != None:
            oprot.writeFieldBegin('storeIndex', TType.I32, 3)
            oprot.writeI32(self.storeIndex)
            oprot.writeFieldEnd()
        if self.startDate != None:
            oprot.writeFieldBegin('startDate', TType.STRUCT, 4)
            self.startDate.write(oprot)
            oprot.writeFieldEnd()
        if self.validityPeriod != None:
            oprot.writeFieldBegin('validityPeriod', TType.STRUCT, 5)
            self.validityPeriod.write(oprot)
            oprot.writeFieldEnd()
        if self.lockType != None:
            oprot.writeFieldBegin('lockType', TType.STRING, 6)
            oprot.writeString(self.lockType)
            oprot.writeFieldEnd()
        if self.vendor != None:
            oprot.writeFieldBegin('vendor', TType.STRING, 7)
            oprot.writeString(self.vendor)
            oprot.writeFieldEnd()
        if self.addition != None:
            oprot.writeFieldBegin('addition', TType.STRING, 8)
            oprot.writeString(self.addition)
            oprot.writeFieldEnd()
        if self.priority != None:
            oprot.writeFieldBegin('priority', TType.STRING, 9)
            oprot.writeString(self.priority)
            oprot.writeFieldEnd()
        if self.licInfo != None:
            oprot.writeFieldBegin('licInfo', TType.STRUCT, 10)
            self.licInfo.write(oprot)
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




class FeatureEulaInfoIDL(object):
    """
    Attributes:
     - feature
     - accepted
    """

    thrift_spec = (None, (1,
      TType.STRING,
      'feature',
      None,
      None), (2,
      TType.I32,
      'accepted',
      None,
      None))

    def __init__(self, feature = None, accepted = None):
        self.feature = feature
        self.accepted = accepted



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
                    self.feature = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.accepted = iprot.readI32()
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
        oprot.writeStructBegin('FeatureEulaInfoIDL')
        if self.feature != None:
            oprot.writeFieldBegin('feature', TType.STRING, 1)
            oprot.writeString(self.feature)
            oprot.writeFieldEnd()
        if self.accepted != None:
            oprot.writeFieldBegin('accepted', TType.I32, 2)
            oprot.writeI32(self.accepted)
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




class LicenseEulaIDL(object):
    """
    Attributes:
     - featureInfo
     - eula
    """

    thrift_spec = (None, (1,
      TType.LIST,
      'featureInfo',
      (TType.STRUCT, (FeatureEulaInfoIDL, FeatureEulaInfoIDL.thrift_spec)),
      None), (2,
      TType.STRING,
      'eula',
      None,
      None))

    def __init__(self, featureInfo = None, eula = None):
        self.featureInfo = featureInfo
        self.eula = eula



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
                    self.featureInfo = []
                    (_etype3, _size0,) = iprot.readListBegin()
                    for _i4 in xrange(_size0):
                        _elem5 = FeatureEulaInfoIDL()
                        _elem5.read(iprot)
                        self.featureInfo.append(_elem5)

                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.eula = iprot.readString()
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
        oprot.writeStructBegin('LicenseEulaIDL')
        if self.featureInfo != None:
            oprot.writeFieldBegin('featureInfo', TType.LIST, 1)
            oprot.writeListBegin(TType.STRUCT, len(self.featureInfo))
            for iter6 in self.featureInfo:
                iter6.write(oprot)

            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.eula != None:
            oprot.writeFieldBegin('eula', TType.STRING, 2)
            oprot.writeString(self.eula)
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




class LicenseInstallStatusIDL(object):
    """
    Attributes:
     - total
     - success
     - fail
     - existing
    """

    thrift_spec = (None,
     (1,
      TType.I16,
      'total',
      None,
      None),
     (2,
      TType.I16,
      'success',
      None,
      None),
     (3,
      TType.I16,
      'fail',
      None,
      None),
     (4,
      TType.I16,
      'existing',
      None,
      None))

    def __init__(self, total = None, success = None, fail = None, existing = None):
        self.total = total
        self.success = success
        self.fail = fail
        self.existing = existing



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
                    self.total = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I16:
                    self.success = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I16:
                    self.fail = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I16:
                    self.existing = iprot.readI16()
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
        oprot.writeStructBegin('LicenseInstallStatusIDL')
        if self.total != None:
            oprot.writeFieldBegin('total', TType.I16, 1)
            oprot.writeI16(self.total)
            oprot.writeFieldEnd()
        if self.success != None:
            oprot.writeFieldBegin('success', TType.I16, 2)
            oprot.writeI16(self.success)
            oprot.writeFieldEnd()
        if self.fail != None:
            oprot.writeFieldBegin('fail', TType.I16, 3)
            oprot.writeI16(self.fail)
            oprot.writeFieldEnd()
        if self.existing != None:
            oprot.writeFieldBegin('existing', TType.I16, 4)
            oprot.writeI16(self.existing)
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




class LicenseUDIIDL(object):
    """
    Attributes:
     - pid
     - sn
     - vid
    """

    thrift_spec = (None,
     (1,
      TType.STRING,
      'pid',
      None,
      None),
     (2,
      TType.STRING,
      'sn',
      None,
      None),
     (3,
      TType.STRING,
      'vid',
      None,
      None))

    def __init__(self, pid = None, sn = None, vid = None):
        self.pid = pid
        self.sn = sn
        self.vid = vid



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
                    self.pid = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.sn = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.vid = iprot.readString()
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
        oprot.writeStructBegin('LicenseUDIIDL')
        if self.pid != None:
            oprot.writeFieldBegin('pid', TType.STRING, 1)
            oprot.writeString(self.pid)
            oprot.writeFieldEnd()
        if self.sn != None:
            oprot.writeFieldBegin('sn', TType.STRING, 2)
            oprot.writeString(self.sn)
            oprot.writeFieldEnd()
        if self.vid != None:
            oprot.writeFieldBegin('vid', TType.STRING, 3)
            oprot.writeString(self.vid)
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
# 2015.02.05 17:18:32 IST
