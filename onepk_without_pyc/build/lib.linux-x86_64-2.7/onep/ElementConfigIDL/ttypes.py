# 2015.02.05 17:18:23 IST
from thrift.Thrift import *
import Shared.ttypes
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
    from thrift.protocol import fastbinary
except:
    fastbinary = None

class SyslogHostIDL(object):
    """
      Syslog IDL
    
      Attributes:
       - hostAddr
       - vrfName
       - protocol
       - port
      """

    thrift_spec = (None,
     (1,
      TType.STRUCT,
      'hostAddr',
      (Shared.ttypes.NetworkAddressIDL, Shared.ttypes.NetworkAddressIDL.thrift_spec),
      None),
     (2,
      TType.STRING,
      'vrfName',
      None,
      None),
     (3,
      TType.I32,
      'protocol',
      None,
      None),
     (4,
      TType.I16,
      'port',
      None,
      None))

    def __init__(self, hostAddr = None, vrfName = None, protocol = None, port = None):
        self.hostAddr = hostAddr
        self.vrfName = vrfName
        self.protocol = protocol
        self.port = port



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
                    self.hostAddr = Shared.ttypes.NetworkAddressIDL()
                    self.hostAddr.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.vrfName = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.protocol = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I16:
                    self.port = iprot.readI16()
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
        oprot.writeStructBegin('SyslogHostIDL')
        if self.hostAddr != None:
            oprot.writeFieldBegin('hostAddr', TType.STRUCT, 1)
            self.hostAddr.write(oprot)
            oprot.writeFieldEnd()
        if self.vrfName != None:
            oprot.writeFieldBegin('vrfName', TType.STRING, 2)
            oprot.writeString(self.vrfName)
            oprot.writeFieldEnd()
        if self.protocol != None:
            oprot.writeFieldBegin('protocol', TType.I32, 3)
            oprot.writeI32(self.protocol)
            oprot.writeFieldEnd()
        if self.port != None:
            oprot.writeFieldBegin('port', TType.I16, 4)
            oprot.writeI16(self.port)
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




class SnmpServerIDL(object):
    """
      SNMP server IDL
    
      Attributes:
       - hostAddr
       - commString
       - secModel
       - secLevel
       - udp_port
       - vrfName
       - trapList
      """

    thrift_spec = (None,
     (1,
      TType.STRUCT,
      'hostAddr',
      (Shared.ttypes.NetworkAddressIDL, Shared.ttypes.NetworkAddressIDL.thrift_spec),
      None),
     (2,
      TType.STRING,
      'commString',
      None,
      None),
     (3,
      TType.I16,
      'secModel',
      None,
      None),
     (4,
      TType.I16,
      'secLevel',
      None,
      None),
     (5,
      TType.I16,
      'udp_port',
      None,
      None),
     (6,
      TType.STRING,
      'vrfName',
      None,
      None),
     (7,
      TType.LIST,
      'trapList',
      (TType.I32, None),
      None))

    def __init__(self, hostAddr = None, commString = None, secModel = None, secLevel = None, udp_port = None, vrfName = None, trapList = None):
        self.hostAddr = hostAddr
        self.commString = commString
        self.secModel = secModel
        self.secLevel = secLevel
        self.udp_port = udp_port
        self.vrfName = vrfName
        self.trapList = trapList



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
                    self.hostAddr = Shared.ttypes.NetworkAddressIDL()
                    self.hostAddr.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.commString = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I16:
                    self.secModel = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I16:
                    self.secLevel = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I16:
                    self.udp_port = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRING:
                    self.vrfName = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.LIST:
                    self.trapList = []
                    (_etype3, _size0,) = iprot.readListBegin()
                    for _i4 in xrange(_size0):
                        _elem5 = iprot.readI32()
                        self.trapList.append(_elem5)

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
        oprot.writeStructBegin('SnmpServerIDL')
        if self.hostAddr != None:
            oprot.writeFieldBegin('hostAddr', TType.STRUCT, 1)
            self.hostAddr.write(oprot)
            oprot.writeFieldEnd()
        if self.commString != None:
            oprot.writeFieldBegin('commString', TType.STRING, 2)
            oprot.writeString(self.commString)
            oprot.writeFieldEnd()
        if self.secModel != None:
            oprot.writeFieldBegin('secModel', TType.I16, 3)
            oprot.writeI16(self.secModel)
            oprot.writeFieldEnd()
        if self.secLevel != None:
            oprot.writeFieldBegin('secLevel', TType.I16, 4)
            oprot.writeI16(self.secLevel)
            oprot.writeFieldEnd()
        if self.udp_port != None:
            oprot.writeFieldBegin('udp_port', TType.I16, 5)
            oprot.writeI16(self.udp_port)
            oprot.writeFieldEnd()
        if self.vrfName != None:
            oprot.writeFieldBegin('vrfName', TType.STRING, 6)
            oprot.writeString(self.vrfName)
            oprot.writeFieldEnd()
        if self.trapList != None:
            oprot.writeFieldBegin('trapList', TType.LIST, 7)
            oprot.writeListBegin(TType.I32, len(self.trapList))
            for iter6 in self.trapList:
                oprot.writeI32(iter6)

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




class LocalAuthUserIDL(object):
    """
      Local Authentication User.
    
      Attributes:
       - username
       - cliPrivilegeLevel
       - password
       - secretKeyEncryption
       - private_secret
      """

    thrift_spec = (None,
     (1,
      TType.STRING,
      'username',
      None,
      None),
     (2,
      TType.I32,
      'cliPrivilegeLevel',
      None,
      None),
     (3,
      TType.STRING,
      'password',
      None,
      None),
     (4,
      TType.I32,
      'secretKeyEncryption',
      None,
      None),
     (5,
      TType.STRING,
      'private_secret',
      None,
      None))

    def __init__(self, username = None, cliPrivilegeLevel = None, password = None, secretKeyEncryption = None, private_secret = None):
        self.username = username
        self.cliPrivilegeLevel = cliPrivilegeLevel
        self.password = password
        self.secretKeyEncryption = secretKeyEncryption
        self.private_secret = private_secret



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
                    self.username = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.cliPrivilegeLevel = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.password = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.secretKeyEncryption = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.private_secret = iprot.readString()
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
        oprot.writeStructBegin('LocalAuthUserIDL')
        if self.username != None:
            oprot.writeFieldBegin('username', TType.STRING, 1)
            oprot.writeString(self.username)
            oprot.writeFieldEnd()
        if self.cliPrivilegeLevel != None:
            oprot.writeFieldBegin('cliPrivilegeLevel', TType.I32, 2)
            oprot.writeI32(self.cliPrivilegeLevel)
            oprot.writeFieldEnd()
        if self.password != None:
            oprot.writeFieldBegin('password', TType.STRING, 3)
            oprot.writeString(self.password)
            oprot.writeFieldEnd()
        if self.secretKeyEncryption != None:
            oprot.writeFieldBegin('secretKeyEncryption', TType.I32, 4)
            oprot.writeI32(self.secretKeyEncryption)
            oprot.writeFieldEnd()
        if self.private_secret != None:
            oprot.writeFieldBegin('private_secret', TType.STRING, 5)
            oprot.writeString(self.private_secret)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

        def validate(self):
            if self.username is None:
                raise TProtocol.TProtocolException(message='Required field username is unset!')





    def __repr__(self):
        L = [ '%s=%r' % (key, value) for (key, value,) in self.__dict__.iteritems() ]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))



    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__



    def __ne__(self, other):
        return not self == other




class TACACSServerIDL(object):
    """
      Represents the TACACS Server
    
      Attributes:
       - address
       - name
       - tcpPort
       - timeout
       - tACACSSecretKey
      """

    thrift_spec = (None,
     (1,
      TType.STRUCT,
      'address',
      (Shared.ttypes.NetworkAddressIDL, Shared.ttypes.NetworkAddressIDL.thrift_spec),
      None),
     (2,
      TType.STRING,
      'name',
      None,
      None),
     (3,
      TType.I32,
      'tcpPort',
      None,
      None),
     (4,
      TType.I32,
      'timeout',
      None,
      None),
     (5,
      TType.STRING,
      'tACACSSecretKey',
      None,
      None))

    def __init__(self, address = None, name = None, tcpPort = None, timeout = None, tACACSSecretKey = None):
        self.address = address
        self.name = name
        self.tcpPort = tcpPort
        self.timeout = timeout
        self.tACACSSecretKey = tACACSSecretKey



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
                    self.name = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.tcpPort = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.timeout = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.tACACSSecretKey = iprot.readString()
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
        oprot.writeStructBegin('TACACSServerIDL')
        if self.address != None:
            oprot.writeFieldBegin('address', TType.STRUCT, 1)
            self.address.write(oprot)
            oprot.writeFieldEnd()
        if self.name != None:
            oprot.writeFieldBegin('name', TType.STRING, 2)
            oprot.writeString(self.name)
            oprot.writeFieldEnd()
        if self.tcpPort != None:
            oprot.writeFieldBegin('tcpPort', TType.I32, 3)
            oprot.writeI32(self.tcpPort)
            oprot.writeFieldEnd()
        if self.timeout != None:
            oprot.writeFieldBegin('timeout', TType.I32, 4)
            oprot.writeI32(self.timeout)
            oprot.writeFieldEnd()
        if self.tACACSSecretKey != None:
            oprot.writeFieldBegin('tACACSSecretKey', TType.STRING, 5)
            oprot.writeString(self.tACACSSecretKey)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

        def validate(self):
            if self.address is None:
                raise TProtocol.TProtocolException(message='Required field address is unset!')





    def __repr__(self):
        L = [ '%s=%r' % (key, value) for (key, value,) in self.__dict__.iteritems() ]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))



    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__



    def __ne__(self, other):
        return not self == other




class DNSServerIDL(object):
    """
      DNS Server IDL
    
      Attributes:
       - addr
       - primary
       - vrfName
      """

    thrift_spec = (None,
     (1,
      TType.STRUCT,
      'addr',
      (Shared.ttypes.NetworkAddressIDL, Shared.ttypes.NetworkAddressIDL.thrift_spec),
      None),
     (2,
      TType.I32,
      'primary',
      None,
      None),
     (3,
      TType.STRING,
      'vrfName',
      None,
      None))

    def __init__(self, addr = None, primary = None, vrfName = None):
        self.addr = addr
        self.primary = primary
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
                    self.addr = Shared.ttypes.NetworkAddressIDL()
                    self.addr.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.primary = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
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
        oprot.writeStructBegin('DNSServerIDL')
        if self.addr != None:
            oprot.writeFieldBegin('addr', TType.STRUCT, 1)
            self.addr.write(oprot)
            oprot.writeFieldEnd()
        if self.primary != None:
            oprot.writeFieldBegin('primary', TType.I32, 2)
            oprot.writeI32(self.primary)
            oprot.writeFieldEnd()
        if self.vrfName != None:
            oprot.writeFieldBegin('vrfName', TType.STRING, 3)
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




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:18:23 IST
