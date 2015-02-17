# 2015.02.05 17:18:42 IST
from thrift.Thrift import *
import Shared.ttypes
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
    from thrift.protocol import fastbinary
except:
    fastbinary = None

class GeoIDL(object):
    """
    Attributes:
     - latitude
     - lat_resolution
     - longitude
     - long_resolution
     - altitude
     - alt_resolution
     - alt_type
    """

    thrift_spec = (None,
     (1,
      TType.STRING,
      'latitude',
      None,
      None),
     (2,
      TType.STRING,
      'lat_resolution',
      None,
      None),
     (3,
      TType.STRING,
      'longitude',
      None,
      None),
     (4,
      TType.STRING,
      'long_resolution',
      None,
      None),
     (5,
      TType.STRING,
      'altitude',
      None,
      None),
     (6,
      TType.STRING,
      'alt_resolution',
      None,
      None),
     (7,
      TType.I16,
      'alt_type',
      None,
      None))

    def __init__(self, latitude = None, lat_resolution = None, longitude = None, long_resolution = None, altitude = None, alt_resolution = None, alt_type = None):
        self.latitude = latitude
        self.lat_resolution = lat_resolution
        self.longitude = longitude
        self.long_resolution = long_resolution
        self.altitude = altitude
        self.alt_resolution = alt_resolution
        self.alt_type = alt_type



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
                    self.latitude = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.lat_resolution = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.longitude = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.long_resolution = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.altitude = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRING:
                    self.alt_resolution = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I16:
                    self.alt_type = iprot.readI16()
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
        oprot.writeStructBegin('GeoIDL')
        if self.latitude != None:
            oprot.writeFieldBegin('latitude', TType.STRING, 1)
            oprot.writeString(self.latitude)
            oprot.writeFieldEnd()
        if self.lat_resolution != None:
            oprot.writeFieldBegin('lat_resolution', TType.STRING, 2)
            oprot.writeString(self.lat_resolution)
            oprot.writeFieldEnd()
        if self.longitude != None:
            oprot.writeFieldBegin('longitude', TType.STRING, 3)
            oprot.writeString(self.longitude)
            oprot.writeFieldEnd()
        if self.long_resolution != None:
            oprot.writeFieldBegin('long_resolution', TType.STRING, 4)
            oprot.writeString(self.long_resolution)
            oprot.writeFieldEnd()
        if self.altitude != None:
            oprot.writeFieldBegin('altitude', TType.STRING, 5)
            oprot.writeString(self.altitude)
            oprot.writeFieldEnd()
        if self.alt_resolution != None:
            oprot.writeFieldBegin('alt_resolution', TType.STRING, 6)
            oprot.writeString(self.alt_resolution)
            oprot.writeFieldEnd()
        if self.alt_type != None:
            oprot.writeFieldBegin('alt_type', TType.I16, 7)
            oprot.writeI16(self.alt_type)
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




class CivicIDL(object):
    """
    Attributes:
     - catype
     - value
    """

    thrift_spec = (None, (1,
      TType.I16,
      'catype',
      None,
      None), (2,
      TType.STRING,
      'value',
      None,
      None))

    def __init__(self, catype = None, value = None):
        self.catype = catype
        self.value = value



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
                    self.catype = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.value = iprot.readString()
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
        oprot.writeStructBegin('CivicIDL')
        if self.catype != None:
            oprot.writeFieldBegin('catype', TType.I16, 1)
            oprot.writeI16(self.catype)
            oprot.writeFieldEnd()
        if self.value != None:
            oprot.writeFieldBegin('value', TType.STRING, 2)
            oprot.writeString(self.value)
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




class CustomIDL(object):
    """
    Attributes:
     - name
     - value
    """

    thrift_spec = (None, (1,
      TType.STRING,
      'name',
      None,
      None), (2,
      TType.STRING,
      'value',
      None,
      None))

    def __init__(self, name = None, value = None):
        self.name = name
        self.value = value



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
                    self.value = iprot.readString()
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
        oprot.writeStructBegin('CustomIDL')
        if self.name != None:
            oprot.writeFieldBegin('name', TType.STRING, 1)
            oprot.writeString(self.name)
            oprot.writeFieldEnd()
        if self.value != None:
            oprot.writeFieldBegin('value', TType.STRING, 2)
            oprot.writeString(self.value)
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




class NetworkLocationIDL(object):
    """
    Attributes:
     - subtype
     - elin
     - civic
     - custom
     - geo
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'subtype',
      None,
      None),
     (2,
      TType.STRING,
      'elin',
      None,
      None),
     (3,
      TType.LIST,
      'civic',
      (TType.STRUCT, (CivicIDL, CivicIDL.thrift_spec)),
      None),
     (4,
      TType.LIST,
      'custom',
      (TType.STRUCT, (CustomIDL, CustomIDL.thrift_spec)),
      None),
     (5,
      TType.STRUCT,
      'geo',
      (GeoIDL, GeoIDL.thrift_spec),
      None))

    def __init__(self, subtype = None, elin = None, civic = None, custom = None, geo = None):
        self.subtype = subtype
        self.elin = elin
        self.civic = civic
        self.custom = custom
        self.geo = geo



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
                    self.subtype = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.elin = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.LIST:
                    self.civic = []
                    (_etype3, _size0,) = iprot.readListBegin()
                    for _i4 in xrange(_size0):
                        _elem5 = CivicIDL()
                        _elem5.read(iprot)
                        self.civic.append(_elem5)

                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.LIST:
                    self.custom = []
                    (_etype9, _size6,) = iprot.readListBegin()
                    for _i10 in xrange(_size6):
                        _elem11 = CustomIDL()
                        _elem11.read(iprot)
                        self.custom.append(_elem11)

                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRUCT:
                    self.geo = GeoIDL()
                    self.geo.read(iprot)
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
        oprot.writeStructBegin('NetworkLocationIDL')
        if self.subtype != None:
            oprot.writeFieldBegin('subtype', TType.I32, 1)
            oprot.writeI32(self.subtype)
            oprot.writeFieldEnd()
        if self.elin != None:
            oprot.writeFieldBegin('elin', TType.STRING, 2)
            oprot.writeString(self.elin)
            oprot.writeFieldEnd()
        if self.civic != None:
            oprot.writeFieldBegin('civic', TType.LIST, 3)
            oprot.writeListBegin(TType.STRUCT, len(self.civic))
            for iter12 in self.civic:
                iter12.write(oprot)

            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.custom != None:
            oprot.writeFieldBegin('custom', TType.LIST, 4)
            oprot.writeListBegin(TType.STRUCT, len(self.custom))
            for iter13 in self.custom:
                iter13.write(oprot)

            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.geo != None:
            oprot.writeFieldBegin('geo', TType.STRUCT, 5)
            self.geo.write(oprot)
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




class LocationFilterIDL(object):
    """
    Attributes:
     - subtype
    """

    thrift_spec = (None, (1,
      TType.I32,
      'subtype',
      None,
      None))

    def __init__(self, subtype = None):
        self.subtype = subtype



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
                    self.subtype = iprot.readI32()
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
        oprot.writeStructBegin('LocationFilterIDL')
        if self.subtype != None:
            oprot.writeFieldBegin('subtype', TType.I32, 1)
            oprot.writeI32(self.subtype)
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
# 2015.02.05 17:18:42 IST
