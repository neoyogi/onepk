# 2015.02.05 17:20:51 IST
from thrift.Thrift import *
import Shared.ttypes
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
    from thrift.protocol import fastbinary
except:
    fastbinary = None

class CertificateInIDL(object):
    """
    Attributes:
     - encoding_type
     - length
     - certificate
    """

    thrift_spec = (None,
     (1,
      TType.I16,
      'encoding_type',
      None,
      None),
     (2,
      TType.I32,
      'length',
      None,
      None),
     (3,
      TType.STRING,
      'certificate',
      None,
      None))

    def __init__(self, encoding_type = None, length = None, certificate = None):
        self.encoding_type = encoding_type
        self.length = length
        self.certificate = certificate



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
                    self.encoding_type = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.length = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.certificate = iprot.readString()
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
        oprot.writeStructBegin('CertificateInIDL')
        if self.encoding_type != None:
            oprot.writeFieldBegin('encoding_type', TType.I16, 1)
            oprot.writeI16(self.encoding_type)
            oprot.writeFieldEnd()
        if self.length != None:
            oprot.writeFieldBegin('length', TType.I32, 2)
            oprot.writeI32(self.length)
            oprot.writeFieldEnd()
        if self.certificate != None:
            oprot.writeFieldBegin('certificate', TType.STRING, 3)
            oprot.writeString(self.certificate)
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




class CertPkcs12InIDL(object):
    """
    Attributes:
     - length
     - pkcs12
    """

    thrift_spec = (None, (1,
      TType.I32,
      'length',
      None,
      None), (2,
      TType.STRING,
      'pkcs12',
      None,
      None))

    def __init__(self, length = None, pkcs12 = None):
        self.length = length
        self.pkcs12 = pkcs12



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
                    self.length = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.pkcs12 = iprot.readString()
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
        oprot.writeStructBegin('CertPkcs12InIDL')
        if self.length != None:
            oprot.writeFieldBegin('length', TType.I32, 1)
            oprot.writeI32(self.length)
            oprot.writeFieldEnd()
        if self.pkcs12 != None:
            oprot.writeFieldBegin('pkcs12', TType.STRING, 2)
            oprot.writeString(self.pkcs12)
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




class CertKeyInIDL(object):
    """
    Attributes:
     - encoding_type
     - length
     - private_key
    """

    thrift_spec = (None,
     (1,
      TType.I16,
      'encoding_type',
      None,
      None),
     (2,
      TType.I32,
      'length',
      None,
      None),
     (3,
      TType.STRING,
      'private_key',
      None,
      None))

    def __init__(self, encoding_type = None, length = None, private_key = None):
        self.encoding_type = encoding_type
        self.length = length
        self.private_key = private_key



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
                    self.encoding_type = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.length = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.private_key = iprot.readString()
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
        oprot.writeStructBegin('CertKeyInIDL')
        if self.encoding_type != None:
            oprot.writeFieldBegin('encoding_type', TType.I16, 1)
            oprot.writeI16(self.encoding_type)
            oprot.writeFieldEnd()
        if self.length != None:
            oprot.writeFieldBegin('length', TType.I32, 2)
            oprot.writeI32(self.length)
            oprot.writeFieldEnd()
        if self.private_key != None:
            oprot.writeFieldBegin('private_key', TType.STRING, 3)
            oprot.writeString(self.private_key)
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




class CertTrustpointInfoInIDL(object):
    """
    Attributes:
     - is_pkcs12
     - pkcs12
     - IDCert
     - caCertList
     - is_exportable_key
     - key
    """

    thrift_spec = (None,
     (1,
      TType.I16,
      'is_pkcs12',
      None,
      None),
     (2,
      TType.STRUCT,
      'pkcs12',
      (CertPkcs12InIDL, CertPkcs12InIDL.thrift_spec),
      None),
     (3,
      TType.STRUCT,
      'IDCert',
      (CertificateInIDL, CertificateInIDL.thrift_spec),
      None),
     (4,
      TType.LIST,
      'caCertList',
      (TType.STRUCT, (CertificateInIDL, CertificateInIDL.thrift_spec)),
      None),
     (5,
      TType.I16,
      'is_exportable_key',
      None,
      None),
     (6,
      TType.STRUCT,
      'key',
      (CertKeyInIDL, CertKeyInIDL.thrift_spec),
      None))

    def __init__(self, is_pkcs12 = None, pkcs12 = None, IDCert = None, caCertList = None, is_exportable_key = None, key = None):
        self.is_pkcs12 = is_pkcs12
        self.pkcs12 = pkcs12
        self.IDCert = IDCert
        self.caCertList = caCertList
        self.is_exportable_key = is_exportable_key
        self.key = key



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
                    self.is_pkcs12 = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.pkcs12 = CertPkcs12InIDL()
                    self.pkcs12.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRUCT:
                    self.IDCert = CertificateInIDL()
                    self.IDCert.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.LIST:
                    self.caCertList = []
                    (_etype3, _size0,) = iprot.readListBegin()
                    for _i4 in xrange(_size0):
                        _elem5 = CertificateInIDL()
                        _elem5.read(iprot)
                        self.caCertList.append(_elem5)

                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I16:
                    self.is_exportable_key = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRUCT:
                    self.key = CertKeyInIDL()
                    self.key.read(iprot)
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
        oprot.writeStructBegin('CertTrustpointInfoInIDL')
        if self.is_pkcs12 != None:
            oprot.writeFieldBegin('is_pkcs12', TType.I16, 1)
            oprot.writeI16(self.is_pkcs12)
            oprot.writeFieldEnd()
        if self.pkcs12 != None:
            oprot.writeFieldBegin('pkcs12', TType.STRUCT, 2)
            self.pkcs12.write(oprot)
            oprot.writeFieldEnd()
        if self.IDCert != None:
            oprot.writeFieldBegin('IDCert', TType.STRUCT, 3)
            self.IDCert.write(oprot)
            oprot.writeFieldEnd()
        if self.caCertList != None:
            oprot.writeFieldBegin('caCertList', TType.LIST, 4)
            oprot.writeListBegin(TType.STRUCT, len(self.caCertList))
            for iter6 in self.caCertList:
                iter6.write(oprot)

            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.is_exportable_key != None:
            oprot.writeFieldBegin('is_exportable_key', TType.I16, 5)
            oprot.writeI16(self.is_exportable_key)
            oprot.writeFieldEnd()
        if self.key != None:
            oprot.writeFieldBegin('key', TType.STRUCT, 6)
            self.key.write(oprot)
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
# 2015.02.05 17:20:51 IST
