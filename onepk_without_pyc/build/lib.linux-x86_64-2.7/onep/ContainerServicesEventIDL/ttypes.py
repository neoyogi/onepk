# 2015.02.05 17:18:02 IST
from thrift.Thrift import *
import SharedOut.ttypes
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
    from thrift.protocol import fastbinary
except:
    fastbinary = None

class CS_out_ntp_servers(object):
    """
    Attributes:
     - adding
     - ntpaddr
    """

    thrift_spec = (None, (1,
      TType.I32,
      'adding',
      None,
      None), (2,
      TType.STRUCT,
      'ntpaddr',
      (SharedOut.ttypes.NetworkAddressOutIDL, SharedOut.ttypes.NetworkAddressOutIDL.thrift_spec),
      None))

    def __init__(self, adding = None, ntpaddr = None):
        self.adding = adding
        self.ntpaddr = ntpaddr



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
                    self.adding = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.ntpaddr = SharedOut.ttypes.NetworkAddressOutIDL()
                    self.ntpaddr.read(iprot)
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
        oprot.writeStructBegin('CS_out_ntp_servers')
        if self.adding != None:
            oprot.writeFieldBegin('adding', TType.I32, 1)
            oprot.writeI32(self.adding)
            oprot.writeFieldEnd()
        if self.ntpaddr != None:
            oprot.writeFieldBegin('ntpaddr', TType.STRUCT, 2)
            self.ntpaddr.write(oprot)
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




class CS_out_timezone(object):
    """
    Attributes:
     - timezone_offset
     - timezone_name
    """

    thrift_spec = (None, (1,
      TType.I32,
      'timezone_offset',
      None,
      None), (2,
      TType.STRING,
      'timezone_name',
      None,
      None))

    def __init__(self, timezone_offset = None, timezone_name = None):
        self.timezone_offset = timezone_offset
        self.timezone_name = timezone_name



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
                    self.timezone_offset = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.timezone_name = iprot.readString()
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
        oprot.writeStructBegin('CS_out_timezone')
        if self.timezone_offset != None:
            oprot.writeFieldBegin('timezone_offset', TType.I32, 1)
            oprot.writeI32(self.timezone_offset)
            oprot.writeFieldEnd()
        if self.timezone_name != None:
            oprot.writeFieldBegin('timezone_name', TType.STRING, 2)
            oprot.writeString(self.timezone_name)
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




class CS_out_domainname(object):
    """
    Attributes:
     - domainname
    """

    thrift_spec = (None, (1,
      TType.STRING,
      'domainname',
      None,
      None))

    def __init__(self, domainname = None):
        self.domainname = domainname



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
                    self.domainname = iprot.readString()
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
        oprot.writeStructBegin('CS_out_domainname')
        if self.domainname != None:
            oprot.writeFieldBegin('domainname', TType.STRING, 1)
            oprot.writeString(self.domainname)
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




class CS_ext_update_IDL(object):
    """
    Attributes:
     - tag
     - ntpservers
     - cs_timezone
     - domainname_info
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'tag',
      None,
      None),
     (2,
      TType.STRUCT,
      'ntpservers',
      (CS_out_ntp_servers, CS_out_ntp_servers.thrift_spec),
      None),
     (3,
      TType.STRUCT,
      'cs_timezone',
      (CS_out_timezone, CS_out_timezone.thrift_spec),
      None),
     (4,
      TType.STRUCT,
      'domainname_info',
      (CS_out_domainname, CS_out_domainname.thrift_spec),
      None))

    def __init__(self, tag = None, ntpservers = None, cs_timezone = None, domainname_info = None):
        self.tag = tag
        self.ntpservers = ntpservers
        self.cs_timezone = cs_timezone
        self.domainname_info = domainname_info



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
                    self.tag = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.ntpservers = CS_out_ntp_servers()
                    self.ntpservers.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRUCT:
                    self.cs_timezone = CS_out_timezone()
                    self.cs_timezone.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRUCT:
                    self.domainname_info = CS_out_domainname()
                    self.domainname_info.read(iprot)
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
        oprot.writeStructBegin('CS_ext_update_IDL')
        if self.tag != None:
            oprot.writeFieldBegin('tag', TType.I32, 1)
            oprot.writeI32(self.tag)
            oprot.writeFieldEnd()
        if self.ntpservers != None:
            oprot.writeFieldBegin('ntpservers', TType.STRUCT, 2)
            self.ntpservers.write(oprot)
            oprot.writeFieldEnd()
        if self.cs_timezone != None:
            oprot.writeFieldBegin('cs_timezone', TType.STRUCT, 3)
            self.cs_timezone.write(oprot)
            oprot.writeFieldEnd()
        if self.domainname_info != None:
            oprot.writeFieldBegin('domainname_info', TType.STRUCT, 4)
            self.domainname_info.write(oprot)
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




class CS_ext_query_IDL(object):
    """
    Attributes:
     - tag
    """

    thrift_spec = (None, (1,
      TType.I32,
      'tag',
      None,
      None))

    def __init__(self, tag = None):
        self.tag = tag



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
                    self.tag = iprot.readI32()
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
        oprot.writeStructBegin('CS_ext_query_IDL')
        if self.tag != None:
            oprot.writeFieldBegin('tag', TType.I32, 1)
            oprot.writeI32(self.tag)
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
# 2015.02.05 17:18:03 IST
