# 2015.02.05 17:20:56 IST
from thrift.Thrift import *
import Shared.ttypes
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
    from thrift.protocol import fastbinary
except:
    fastbinary = None

class CS_profile_info_IDL(object):
    """
    Attributes:
     - profile_level
     - profile_name
     - profile_description
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'profile_level',
      None,
      None),
     (2,
      TType.STRING,
      'profile_name',
      None,
      None),
     (3,
      TType.STRING,
      'profile_description',
      None,
      None))

    def __init__(self, profile_level = None, profile_name = None, profile_description = None):
        self.profile_level = profile_level
        self.profile_name = profile_name
        self.profile_description = profile_description



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
                    self.profile_level = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.profile_name = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.profile_description = iprot.readString()
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
        oprot.writeStructBegin('CS_profile_info_IDL')
        if self.profile_level != None:
            oprot.writeFieldBegin('profile_level', TType.I32, 1)
            oprot.writeI32(self.profile_level)
            oprot.writeFieldEnd()
        if self.profile_name != None:
            oprot.writeFieldBegin('profile_name', TType.STRING, 2)
            oprot.writeString(self.profile_name)
            oprot.writeFieldEnd()
        if self.profile_description != None:
            oprot.writeFieldBegin('profile_description', TType.STRING, 3)
            oprot.writeString(self.profile_description)
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




class CS_network_config_IDL(object):
    """
    Attributes:
     - address
     - mask
     - gateway
     - intftype
     - vrfid
    """

    thrift_spec = (None,
     (1,
      TType.STRUCT,
      'address',
      (Shared.ttypes.NetworkAddressIDL, Shared.ttypes.NetworkAddressIDL.thrift_spec),
      None),
     (2,
      TType.I32,
      'mask',
      None,
      None),
     (3,
      TType.STRUCT,
      'gateway',
      (Shared.ttypes.NetworkAddressIDL, Shared.ttypes.NetworkAddressIDL.thrift_spec),
      None),
     (4,
      TType.I32,
      'intftype',
      None,
      None),
     (5,
      TType.I32,
      'vrfid',
      None,
      None))

    def __init__(self, address = None, mask = None, gateway = None, intftype = None, vrfid = None):
        self.address = address
        self.mask = mask
        self.gateway = gateway
        self.intftype = intftype
        self.vrfid = vrfid



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
                if ftype == TType.I32:
                    self.mask = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRUCT:
                    self.gateway = Shared.ttypes.NetworkAddressIDL()
                    self.gateway.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.intftype = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.vrfid = iprot.readI32()
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
        oprot.writeStructBegin('CS_network_config_IDL')
        if self.address != None:
            oprot.writeFieldBegin('address', TType.STRUCT, 1)
            self.address.write(oprot)
            oprot.writeFieldEnd()
        if self.mask != None:
            oprot.writeFieldBegin('mask', TType.I32, 2)
            oprot.writeI32(self.mask)
            oprot.writeFieldEnd()
        if self.gateway != None:
            oprot.writeFieldBegin('gateway', TType.STRUCT, 3)
            self.gateway.write(oprot)
            oprot.writeFieldEnd()
        if self.intftype != None:
            oprot.writeFieldBegin('intftype', TType.I32, 4)
            oprot.writeI32(self.intftype)
            oprot.writeFieldEnd()
        if self.vrfid != None:
            oprot.writeFieldBegin('vrfid', TType.I32, 5)
            oprot.writeI32(self.vrfid)
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




class CS_mac_id_IDL(object):
    """
    Attributes:
     - addr1
     - addr2
     - addr3
     - addr4
     - addr5
     - addr6
    """

    thrift_spec = (None,
     (1,
      TType.BYTE,
      'addr1',
      None,
      None),
     (2,
      TType.BYTE,
      'addr2',
      None,
      None),
     (3,
      TType.BYTE,
      'addr3',
      None,
      None),
     (4,
      TType.BYTE,
      'addr4',
      None,
      None),
     (5,
      TType.BYTE,
      'addr5',
      None,
      None),
     (6,
      TType.BYTE,
      'addr6',
      None,
      None))

    def __init__(self, addr1 = None, addr2 = None, addr3 = None, addr4 = None, addr5 = None, addr6 = None):
        self.addr1 = addr1
        self.addr2 = addr2
        self.addr3 = addr3
        self.addr4 = addr4
        self.addr5 = addr5
        self.addr6 = addr6



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
                    self.addr1 = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.BYTE:
                    self.addr2 = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.BYTE:
                    self.addr3 = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.BYTE:
                    self.addr4 = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.BYTE:
                    self.addr5 = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.BYTE:
                    self.addr6 = iprot.readByte()
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
        oprot.writeStructBegin('CS_mac_id_IDL')
        if self.addr1 != None:
            oprot.writeFieldBegin('addr1', TType.BYTE, 1)
            oprot.writeByte(self.addr1)
            oprot.writeFieldEnd()
        if self.addr2 != None:
            oprot.writeFieldBegin('addr2', TType.BYTE, 2)
            oprot.writeByte(self.addr2)
            oprot.writeFieldEnd()
        if self.addr3 != None:
            oprot.writeFieldBegin('addr3', TType.BYTE, 3)
            oprot.writeByte(self.addr3)
            oprot.writeFieldEnd()
        if self.addr4 != None:
            oprot.writeFieldBegin('addr4', TType.BYTE, 4)
            oprot.writeByte(self.addr4)
            oprot.writeFieldEnd()
        if self.addr5 != None:
            oprot.writeFieldBegin('addr5', TType.BYTE, 5)
            oprot.writeByte(self.addr5)
            oprot.writeFieldEnd()
        if self.addr6 != None:
            oprot.writeFieldBegin('addr6', TType.BYTE, 6)
            oprot.writeByte(self.addr6)
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




class CS_netip_IDL(object):
    """
    Attributes:
     - macid
     - intfname
     - ip
     - gw
     - mask
    """

    thrift_spec = (None,
     (1,
      TType.STRUCT,
      'macid',
      (CS_mac_id_IDL, CS_mac_id_IDL.thrift_spec),
      None),
     (2,
      TType.STRING,
      'intfname',
      None,
      None),
     (3,
      TType.STRUCT,
      'ip',
      (Shared.ttypes.NetworkAddressIDL, Shared.ttypes.NetworkAddressIDL.thrift_spec),
      None),
     (4,
      TType.STRUCT,
      'gw',
      (Shared.ttypes.NetworkAddressIDL, Shared.ttypes.NetworkAddressIDL.thrift_spec),
      None),
     (5,
      TType.I32,
      'mask',
      None,
      None))

    def __init__(self, macid = None, intfname = None, ip = None, gw = None, mask = None):
        self.macid = macid
        self.intfname = intfname
        self.ip = ip
        self.gw = gw
        self.mask = mask



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
                    self.macid = CS_mac_id_IDL()
                    self.macid.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.intfname = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRUCT:
                    self.ip = Shared.ttypes.NetworkAddressIDL()
                    self.ip.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRUCT:
                    self.gw = Shared.ttypes.NetworkAddressIDL()
                    self.gw.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.mask = iprot.readI32()
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
        oprot.writeStructBegin('CS_netip_IDL')
        if self.macid != None:
            oprot.writeFieldBegin('macid', TType.STRUCT, 1)
            self.macid.write(oprot)
            oprot.writeFieldEnd()
        if self.intfname != None:
            oprot.writeFieldBegin('intfname', TType.STRING, 2)
            oprot.writeString(self.intfname)
            oprot.writeFieldEnd()
        if self.ip != None:
            oprot.writeFieldBegin('ip', TType.STRUCT, 3)
            self.ip.write(oprot)
            oprot.writeFieldEnd()
        if self.gw != None:
            oprot.writeFieldBegin('gw', TType.STRUCT, 4)
            self.gw.write(oprot)
            oprot.writeFieldEnd()
        if self.mask != None:
            oprot.writeFieldBegin('mask', TType.I32, 5)
            oprot.writeI32(self.mask)
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




class CS_netlist_IDL(object):
    """
    Attributes:
     - count
     - netip
    """

    thrift_spec = (None, (1,
      TType.I32,
      'count',
      None,
      None), (2,
      TType.LIST,
      'netip',
      (TType.STRUCT, (CS_netip_IDL, CS_netip_IDL.thrift_spec)),
      None))

    def __init__(self, count = None, netip = None):
        self.count = count
        self.netip = netip



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
                    self.count = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.netip = []
                    (_etype3, _size0,) = iprot.readListBegin()
                    for _i4 in xrange(_size0):
                        _elem5 = CS_netip_IDL()
                        _elem5.read(iprot)
                        self.netip.append(_elem5)

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
        oprot.writeStructBegin('CS_netlist_IDL')
        if self.count != None:
            oprot.writeFieldBegin('count', TType.I32, 1)
            oprot.writeI32(self.count)
            oprot.writeFieldEnd()
        if self.netip != None:
            oprot.writeFieldBegin('netip', TType.LIST, 2)
            oprot.writeListBegin(TType.STRUCT, len(self.netip))
            for iter6 in self.netip:
                iter6.write(oprot)

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




class CS_ntp_servers(object):
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
      (Shared.ttypes.NetworkAddressIDL, Shared.ttypes.NetworkAddressIDL.thrift_spec),
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
                    self.ntpaddr = Shared.ttypes.NetworkAddressIDL()
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
        oprot.writeStructBegin('CS_ntp_servers')
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




class CS_timezone(object):
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
        oprot.writeStructBegin('CS_timezone')
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




class CS_domainname(object):
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
        oprot.writeStructBegin('CS_domainname')
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




class CS_ext_host_info_IDL(object):
    """
    Attributes:
     - tag
     - ntpservers
     - cs_timezone
     - domainname
     - containername
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'tag',
      None,
      None),
     (2,
      TType.LIST,
      'ntpservers',
      (TType.STRUCT, (CS_ntp_servers, CS_ntp_servers.thrift_spec)),
      None),
     (3,
      TType.STRUCT,
      'cs_timezone',
      (CS_timezone, CS_timezone.thrift_spec),
      None),
     (4,
      TType.STRUCT,
      'domainname',
      (CS_domainname, CS_domainname.thrift_spec),
      None),
     (5,
      TType.STRING,
      'containername',
      None,
      None))

    def __init__(self, tag = None, ntpservers = None, cs_timezone = None, domainname = None, containername = None):
        self.tag = tag
        self.ntpservers = ntpservers
        self.cs_timezone = cs_timezone
        self.domainname = domainname
        self.containername = containername



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
                if ftype == TType.LIST:
                    self.ntpservers = []
                    (_etype10, _size7,) = iprot.readListBegin()
                    for _i11 in xrange(_size7):
                        _elem12 = CS_ntp_servers()
                        _elem12.read(iprot)
                        self.ntpservers.append(_elem12)

                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRUCT:
                    self.cs_timezone = CS_timezone()
                    self.cs_timezone.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRUCT:
                    self.domainname = CS_domainname()
                    self.domainname.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.containername = iprot.readString()
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
        oprot.writeStructBegin('CS_ext_host_info_IDL')
        if self.tag != None:
            oprot.writeFieldBegin('tag', TType.I32, 1)
            oprot.writeI32(self.tag)
            oprot.writeFieldEnd()
        if self.ntpservers != None:
            oprot.writeFieldBegin('ntpservers', TType.LIST, 2)
            oprot.writeListBegin(TType.STRUCT, len(self.ntpservers))
            for iter13 in self.ntpservers:
                iter13.write(oprot)

            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.cs_timezone != None:
            oprot.writeFieldBegin('cs_timezone', TType.STRUCT, 3)
            self.cs_timezone.write(oprot)
            oprot.writeFieldEnd()
        if self.domainname != None:
            oprot.writeFieldBegin('domainname', TType.STRUCT, 4)
            self.domainname.write(oprot)
            oprot.writeFieldEnd()
        if self.containername != None:
            oprot.writeFieldBegin('containername', TType.STRING, 5)
            oprot.writeString(self.containername)
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




class CS_ext_guest_request_param_IDL(object):
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
        oprot.writeStructBegin('CS_ext_guest_request_param_IDL')
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




class CS_ext_guest_reply_IDL(object):
    """
    Attributes:
     - tag
     - ntpservers
     - cs_timezone
     - domainname
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'tag',
      None,
      None),
     (2,
      TType.LIST,
      'ntpservers',
      (TType.STRUCT, (CS_ntp_servers, CS_ntp_servers.thrift_spec)),
      None),
     (3,
      TType.STRUCT,
      'cs_timezone',
      (CS_timezone, CS_timezone.thrift_spec),
      None),
     (4,
      TType.STRUCT,
      'domainname',
      (CS_domainname, CS_domainname.thrift_spec),
      None))

    def __init__(self, tag = None, ntpservers = None, cs_timezone = None, domainname = None):
        self.tag = tag
        self.ntpservers = ntpservers
        self.cs_timezone = cs_timezone
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
                if ftype == TType.I32:
                    self.tag = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.ntpservers = []
                    (_etype17, _size14,) = iprot.readListBegin()
                    for _i18 in xrange(_size14):
                        _elem19 = CS_ntp_servers()
                        _elem19.read(iprot)
                        self.ntpservers.append(_elem19)

                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRUCT:
                    self.cs_timezone = CS_timezone()
                    self.cs_timezone.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRUCT:
                    self.domainname = CS_domainname()
                    self.domainname.read(iprot)
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
        oprot.writeStructBegin('CS_ext_guest_reply_IDL')
        if self.tag != None:
            oprot.writeFieldBegin('tag', TType.I32, 1)
            oprot.writeI32(self.tag)
            oprot.writeFieldEnd()
        if self.ntpservers != None:
            oprot.writeFieldBegin('ntpservers', TType.LIST, 2)
            oprot.writeListBegin(TType.STRUCT, len(self.ntpservers))
            for iter20 in self.ntpservers:
                iter20.write(oprot)

            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.cs_timezone != None:
            oprot.writeFieldBegin('cs_timezone', TType.STRUCT, 3)
            self.cs_timezone.write(oprot)
            oprot.writeFieldEnd()
        if self.domainname != None:
            oprot.writeFieldBegin('domainname', TType.STRUCT, 4)
            self.domainname.write(oprot)
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
# 2015.02.05 17:20:57 IST
