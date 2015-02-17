# 2015.02.05 17:23:07 IST
from thrift.Thrift import *
import SharedEnum.ttypes
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
    from thrift.protocol import fastbinary
except:
    fastbinary = None

class ExceptionIDL(Exception):
    """
      Common Exception/Error that can be used by all thrift IPC calls
      The context value can be used to optionally send back context
      specific info.
      Ex: In case of ONEP_ERR_DUPLICATE, the session handle of the
      existing session is sent back in the context parameter.
    
      Attributes:
       - code
       - text
       - context
      """

    thrift_spec = (None,
     (1,
      TType.I32,
      'code',
      None,
      None),
     (2,
      TType.STRING,
      'text',
      None,
      None),
     (3,
      TType.I32,
      'context',
      None,
      0))

    def __init__(self, code = None, text = None, context = thrift_spec[3][4]):
        self.code = code
        self.text = text
        self.context = context



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
                    self.code = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.text = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.context = iprot.readI32()
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
        oprot.writeStructBegin('ExceptionIDL')
        if self.code != None:
            oprot.writeFieldBegin('code', TType.I32, 1)
            oprot.writeI32(self.code)
            oprot.writeFieldEnd()
        if self.text != None:
            oprot.writeFieldBegin('text', TType.STRING, 2)
            oprot.writeString(self.text)
            oprot.writeFieldEnd()
        if self.context != None:
            oprot.writeFieldBegin('context', TType.I32, 3)
            oprot.writeI32(self.context)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

        def validate(self):
            pass





    def __str__(self):
        return repr(self)



    def __repr__(self):
        L = [ '%s=%r' % (key, value) for (key, value,) in self.__dict__.iteritems() ]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))



    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__



    def __ne__(self, other):
        return not self == other




class EventHandleIDL(object):
    """
      Common return of event registration API
    
      Attributes:
       - eventHandle
      """

    thrift_spec = (None, (1,
      TType.I32,
      'eventHandle',
      None,
      None))

    def __init__(self, eventHandle = None):
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
        oprot.writeStructBegin('EventHandleIDL')
        if self.eventHandle != None:
            oprot.writeFieldBegin('eventHandle', TType.I32, 1)
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




class NetworkInterfaceIDL(object):
    """
      Common DataStructures for Inbound IDLs
      for interface. Later for Outbound as well.
    
      Attributes:
       - xosHandle
       - name
       - type
      """

    thrift_spec = (None,
     (1,
      TType.I64,
      'xosHandle',
      None,
      None),
     (2,
      TType.STRING,
      'name',
      None,
      None),
     (3,
      TType.I32,
      'type',
      None,
      None))

    def __init__(self, xosHandle = None, name = None, type = None):
        self.xosHandle = xosHandle
        self.name = name
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
                if ftype == TType.I64:
                    self.xosHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.name = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
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
        oprot.writeStructBegin('NetworkInterfaceIDL')
        if self.xosHandle != None:
            oprot.writeFieldBegin('xosHandle', TType.I64, 1)
            oprot.writeI64(self.xosHandle)
            oprot.writeFieldEnd()
        if self.name != None:
            oprot.writeFieldBegin('name', TType.STRING, 2)
            oprot.writeString(self.name)
            oprot.writeFieldEnd()
        if self.type != None:
            oprot.writeFieldBegin('type', TType.I32, 3)
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




class InterfaceFilterIDL(object):
    """
      InterfaceFilterIDL - to avoid ripple effect of changes in
             register apis when InterfaceFilter object gets new field added.
    
    
      Attributes:
       - interfaceType
       - interfaceXOSHandle
      """

    thrift_spec = (None, (1,
      TType.I32,
      'interfaceType',
      None,
      None), (2,
      TType.I64,
      'interfaceXOSHandle',
      None,
      None))

    def __init__(self, interfaceType = None, interfaceXOSHandle = None):
        self.interfaceType = interfaceType
        self.interfaceXOSHandle = interfaceXOSHandle



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
                    self.interfaceType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.interfaceXOSHandle = iprot.readI64()
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
        oprot.writeStructBegin('InterfaceFilterIDL')
        if self.interfaceType != None:
            oprot.writeFieldBegin('interfaceType', TType.I32, 1)
            oprot.writeI32(self.interfaceType)
            oprot.writeFieldEnd()
        if self.interfaceXOSHandle != None:
            oprot.writeFieldBegin('interfaceXOSHandle', TType.I64, 2)
            oprot.writeI64(self.interfaceXOSHandle)
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




class NetworkAddressIDL(object):
    """
    Attributes:
     - family
     - addr
    """

    thrift_spec = (None, (1,
      TType.I32,
      'family',
      None,
      None), (2,
      TType.LIST,
      'addr',
      (TType.BYTE, None),
      None))

    def __init__(self, family = None, addr = None):
        self.family = family
        self.addr = addr



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
                    self.family = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.addr = []
                    (_etype3, _size0,) = iprot.readListBegin()
                    for _i4 in xrange(_size0):
                        _elem5 = iprot.readByte()
                        self.addr.append(_elem5)

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
        oprot.writeStructBegin('NetworkAddressIDL')
        if self.family != None:
            oprot.writeFieldBegin('family', TType.I32, 1)
            oprot.writeI32(self.family)
            oprot.writeFieldEnd()
        if self.addr != None:
            oprot.writeFieldBegin('addr', TType.LIST, 2)
            oprot.writeListBegin(TType.BYTE, len(self.addr))
            for iter6 in self.addr:
                oprot.writeByte(iter6)

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




class NetworkPrefixIDL(object):
    """
    Attributes:
     - prefix_len
     - addr
    """

    thrift_spec = (None, (1,
      TType.I16,
      'prefix_len',
      None,
      None), (2,
      TType.STRUCT,
      'addr',
      (NetworkAddressIDL, NetworkAddressIDL.thrift_spec),
      None))

    def __init__(self, prefix_len = None, addr = None):
        self.prefix_len = prefix_len
        self.addr = addr



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
                    self.prefix_len = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.addr = NetworkAddressIDL()
                    self.addr.read(iprot)
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
        oprot.writeStructBegin('NetworkPrefixIDL')
        if self.prefix_len != None:
            oprot.writeFieldBegin('prefix_len', TType.I16, 1)
            oprot.writeI16(self.prefix_len)
            oprot.writeFieldEnd()
        if self.addr != None:
            oprot.writeFieldBegin('addr', TType.STRUCT, 2)
            self.addr.write(oprot)
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




class BDInstanceIDL(object):
    """
      BDInstanceIDL
    
      Attributes:
       - id
       - name
      """

    thrift_spec = (None, (1,
      TType.I32,
      'id',
      None,
      None), (2,
      TType.STRING,
      'name',
      None,
      ''))

    def __init__(self, id = None, name = thrift_spec[2][4]):
        self.id = id
        self.name = name



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
                    self.id = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.name = iprot.readString()
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
        oprot.writeStructBegin('BDInstanceIDL')
        if self.id != None:
            oprot.writeFieldBegin('id', TType.I32, 1)
            oprot.writeI32(self.id)
            oprot.writeFieldEnd()
        if self.name != None:
            oprot.writeFieldBegin('name', TType.STRING, 2)
            oprot.writeString(self.name)
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




class OnepVersionIDL(object):
    """
    Attributes:
     - major
     - minor
     - maint
    """

    thrift_spec = (None,
     (1,
      TType.I16,
      'major',
      None,
      None),
     (2,
      TType.I16,
      'minor',
      None,
      None),
     (3,
      TType.I16,
      'maint',
      None,
      None))

    def __init__(self, major = None, minor = None, maint = None):
        self.major = major
        self.minor = minor
        self.maint = maint



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
                    self.major = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I16:
                    self.minor = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I16:
                    self.maint = iprot.readI16()
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
        oprot.writeStructBegin('OnepVersionIDL')
        if self.major != None:
            oprot.writeFieldBegin('major', TType.I16, 1)
            oprot.writeI16(self.major)
            oprot.writeFieldEnd()
        if self.minor != None:
            oprot.writeFieldBegin('minor', TType.I16, 2)
            oprot.writeI16(self.minor)
            oprot.writeFieldEnd()
        if self.maint != None:
            oprot.writeFieldBegin('maint', TType.I16, 3)
            oprot.writeI16(self.maint)
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




class DateTimeIDL(object):
    """
    Attributes:
     - year
     - month
     - day
     - hour
     - minute
     - second
     - millisec
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'year',
      None,
      None),
     (2,
      TType.I32,
      'month',
      None,
      None),
     (3,
      TType.I32,
      'day',
      None,
      None),
     (4,
      TType.I32,
      'hour',
      None,
      None),
     (5,
      TType.I32,
      'minute',
      None,
      None),
     (6,
      TType.I32,
      'second',
      None,
      None),
     (7,
      TType.I32,
      'millisec',
      None,
      None))

    def __init__(self, year = None, month = None, day = None, hour = None, minute = None, second = None, millisec = None):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second
        self.millisec = millisec



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
                    self.year = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.month = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.day = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.hour = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.minute = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I32:
                    self.second = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I32:
                    self.millisec = iprot.readI32()
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
        oprot.writeStructBegin('DateTimeIDL')
        if self.year != None:
            oprot.writeFieldBegin('year', TType.I32, 1)
            oprot.writeI32(self.year)
            oprot.writeFieldEnd()
        if self.month != None:
            oprot.writeFieldBegin('month', TType.I32, 2)
            oprot.writeI32(self.month)
            oprot.writeFieldEnd()
        if self.day != None:
            oprot.writeFieldBegin('day', TType.I32, 3)
            oprot.writeI32(self.day)
            oprot.writeFieldEnd()
        if self.hour != None:
            oprot.writeFieldBegin('hour', TType.I32, 4)
            oprot.writeI32(self.hour)
            oprot.writeFieldEnd()
        if self.minute != None:
            oprot.writeFieldBegin('minute', TType.I32, 5)
            oprot.writeI32(self.minute)
            oprot.writeFieldEnd()
        if self.second != None:
            oprot.writeFieldBegin('second', TType.I32, 6)
            oprot.writeI32(self.second)
            oprot.writeFieldEnd()
        if self.millisec != None:
            oprot.writeFieldBegin('millisec', TType.I32, 7)
            oprot.writeI32(self.millisec)
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




class MacAddressIDL(object):
    """
    Attributes:
     - macaddr
    """

    thrift_spec = (None, (1,
      TType.LIST,
      'macaddr',
      (TType.BYTE, None),
      [1,
       2,
       3,
       4,
       5,
       6]))

    def __init__(self, macaddr = thrift_spec[1][4]):
        if macaddr is self.thrift_spec[1][4]:
            macaddr = [1,
             2,
             3,
             4,
             5,
             6]
        self.macaddr = macaddr



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
                    self.macaddr = []
                    (_etype10, _size7,) = iprot.readListBegin()
                    for _i11 in xrange(_size7):
                        _elem12 = iprot.readByte()
                        self.macaddr.append(_elem12)

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
        oprot.writeStructBegin('MacAddressIDL')
        if self.macaddr != None:
            oprot.writeFieldBegin('macaddr', TType.LIST, 1)
            oprot.writeListBegin(TType.BYTE, len(self.macaddr))
            for iter13 in self.macaddr:
                oprot.writeByte(iter13)

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




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:23:08 IST
