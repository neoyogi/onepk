# 2015.02.05 17:23:09 IST
from thrift.Thrift import *
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
    from thrift.protocol import fastbinary
except:
    fastbinary = None

class AsyncExceptionIDL(Exception):
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
        oprot.writeStructBegin('AsyncExceptionIDL')
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




class NetworkInterfaceOutIDL(object):
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
        oprot.writeStructBegin('NetworkInterfaceOutIDL')
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




class NetworkAddressOutIDL(object):
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
      TType.STRING,
      'addr',
      None,
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
                if ftype == TType.STRING:
                    self.addr = iprot.readString()
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
        oprot.writeStructBegin('NetworkAddressOutIDL')
        if self.family != None:
            oprot.writeFieldBegin('family', TType.I32, 1)
            oprot.writeI32(self.family)
            oprot.writeFieldEnd()
        if self.addr != None:
            oprot.writeFieldBegin('addr', TType.STRING, 2)
            oprot.writeString(self.addr)
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




class NetworkPrefixOutIDL(object):
    """
    Attributes:
     - addr
     - prefix_len
    """

    thrift_spec = (None, (1,
      TType.STRUCT,
      'addr',
      (NetworkAddressOutIDL, NetworkAddressOutIDL.thrift_spec),
      None), (2,
      TType.I16,
      'prefix_len',
      None,
      None))

    def __init__(self, addr = None, prefix_len = None):
        self.addr = addr
        self.prefix_len = prefix_len



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
                    self.addr = NetworkAddressOutIDL()
                    self.addr.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I16:
                    self.prefix_len = iprot.readI16()
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
        oprot.writeStructBegin('NetworkPrefixOutIDL')
        if self.addr != None:
            oprot.writeFieldBegin('addr', TType.STRUCT, 1)
            self.addr.write(oprot)
            oprot.writeFieldEnd()
        if self.prefix_len != None:
            oprot.writeFieldBegin('prefix_len', TType.I16, 2)
            oprot.writeI16(self.prefix_len)
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




class OnepVersionOutIDL(object):
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
        oprot.writeStructBegin('OnepVersionOutIDL')
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




class I32OutIDL(object):
    """
    Attributes:
     - value
    """

    thrift_spec = (None, (1,
      TType.I32,
      'value',
      None,
      None))

    def __init__(self, value = None):
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
                if ftype == TType.I32:
                    self.value = iprot.readI32()
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
        oprot.writeStructBegin('I32OutIDL')
        if self.value != None:
            oprot.writeFieldBegin('value', TType.I32, 1)
            oprot.writeI32(self.value)
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




class StringOutIDL(object):
    """
    Attributes:
     - value
    """

    thrift_spec = (None, (1,
      TType.STRING,
      'value',
      None,
      None))

    def __init__(self, value = None):
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
        oprot.writeStructBegin('StringOutIDL')
        if self.value != None:
            oprot.writeFieldBegin('value', TType.STRING, 1)
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




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:23:09 IST
