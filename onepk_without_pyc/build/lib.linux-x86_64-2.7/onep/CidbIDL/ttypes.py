# 2015.02.05 17:18:01 IST
from thrift.Thrift import *
import Shared.ttypes
import OneFwIDL.ttypes
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
    from thrift.protocol import fastbinary
except:
    fastbinary = None

class IdentityDirectory_IDL(object):
    """
    Attributes:
     - realm_id
     - config_version
     - domain_id
    """

    thrift_spec = (None,
     (1,
      TType.I64,
      'realm_id',
      None,
      None),
     (2,
      TType.I64,
      'config_version',
      None,
      None),
     (3,
      TType.I64,
      'domain_id',
      None,
      None))

    def __init__(self, realm_id = None, config_version = None, domain_id = None):
        self.realm_id = realm_id
        self.config_version = config_version
        self.domain_id = domain_id



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
                    self.realm_id = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.config_version = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I64:
                    self.domain_id = iprot.readI64()
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
        oprot.writeStructBegin('IdentityDirectory_IDL')
        if self.realm_id != None:
            oprot.writeFieldBegin('realm_id', TType.I64, 1)
            oprot.writeI64(self.realm_id)
            oprot.writeFieldEnd()
        if self.config_version != None:
            oprot.writeFieldBegin('config_version', TType.I64, 2)
            oprot.writeI64(self.config_version)
            oprot.writeFieldEnd()
        if self.domain_id != None:
            oprot.writeFieldBegin('domain_id', TType.I64, 3)
            oprot.writeI64(self.domain_id)
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




class IdentitySession_IDL(object):
    """
    Attributes:
     - user_name
     - ipaddress
     - config_version
     - session_type
     - propbit_vector
     - rowbit_vector
     - intf
    """

    thrift_spec = (None,
     (1,
      TType.STRING,
      'user_name',
      None,
      None),
     (2,
      TType.STRUCT,
      'ipaddress',
      (Shared.ttypes.NetworkAddressIDL, Shared.ttypes.NetworkAddressIDL.thrift_spec),
      None),
     (3,
      TType.I64,
      'config_version',
      None,
      None),
     (4,
      TType.I32,
      'session_type',
      None,
      None),
     (5,
      TType.STRUCT,
      'propbit_vector',
      (OneFwIDL.ttypes.BitVector_IDL, OneFwIDL.ttypes.BitVector_IDL.thrift_spec),
      None),
     (6,
      TType.STRUCT,
      'rowbit_vector',
      (OneFwIDL.ttypes.BitVector_IDL, OneFwIDL.ttypes.BitVector_IDL.thrift_spec),
      None),
     (7,
      TType.I64,
      'intf',
      None,
      None))

    def __init__(self, user_name = None, ipaddress = None, config_version = None, session_type = None, propbit_vector = None, rowbit_vector = None, intf = None):
        self.user_name = user_name
        self.ipaddress = ipaddress
        self.config_version = config_version
        self.session_type = session_type
        self.propbit_vector = propbit_vector
        self.rowbit_vector = rowbit_vector
        self.intf = intf



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
                    self.user_name = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.ipaddress = Shared.ttypes.NetworkAddressIDL()
                    self.ipaddress.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I64:
                    self.config_version = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.session_type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRUCT:
                    self.propbit_vector = OneFwIDL.ttypes.BitVector_IDL()
                    self.propbit_vector.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRUCT:
                    self.rowbit_vector = OneFwIDL.ttypes.BitVector_IDL()
                    self.rowbit_vector.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I64:
                    self.intf = iprot.readI64()
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
        oprot.writeStructBegin('IdentitySession_IDL')
        if self.user_name != None:
            oprot.writeFieldBegin('user_name', TType.STRING, 1)
            oprot.writeString(self.user_name)
            oprot.writeFieldEnd()
        if self.ipaddress != None:
            oprot.writeFieldBegin('ipaddress', TType.STRUCT, 2)
            self.ipaddress.write(oprot)
            oprot.writeFieldEnd()
        if self.config_version != None:
            oprot.writeFieldBegin('config_version', TType.I64, 3)
            oprot.writeI64(self.config_version)
            oprot.writeFieldEnd()
        if self.session_type != None:
            oprot.writeFieldBegin('session_type', TType.I32, 4)
            oprot.writeI32(self.session_type)
            oprot.writeFieldEnd()
        if self.propbit_vector != None:
            oprot.writeFieldBegin('propbit_vector', TType.STRUCT, 5)
            self.propbit_vector.write(oprot)
            oprot.writeFieldEnd()
        if self.rowbit_vector != None:
            oprot.writeFieldBegin('rowbit_vector', TType.STRUCT, 6)
            self.rowbit_vector.write(oprot)
            oprot.writeFieldEnd()
        if self.intf != None:
            oprot.writeFieldBegin('intf', TType.I64, 7)
            oprot.writeI64(self.intf)
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
# 2015.02.05 17:18:01 IST
