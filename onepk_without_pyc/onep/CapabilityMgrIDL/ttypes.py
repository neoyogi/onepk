# 2015.02.05 17:20:47 IST
from thrift.Thrift import *
import Shared.ttypes
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
    from thrift.protocol import fastbinary
except:
    fastbinary = None

class CapabilityStrIDL(object):
    """
      If Successfully authenticated and connected to NetworkElement,
      A session handle should be assigned and along with other info
      retrieved from Network Element.  Let's do it at one round trip
      as much info on hard property as we can.
    
      Attributes:
       - cap_name
       - cap_value
      """

    thrift_spec = (None, (1,
      TType.STRING,
      'cap_name',
      None,
      None), (2,
      TType.LIST,
      'cap_value',
      (TType.STRING, None),
      None))

    def __init__(self, cap_name = None, cap_value = None):
        self.cap_name = cap_name
        self.cap_value = cap_value



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
                    self.cap_name = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.cap_value = []
                    (_etype3, _size0,) = iprot.readListBegin()
                    for _i4 in xrange(_size0):
                        _elem5 = iprot.readString()
                        self.cap_value.append(_elem5)

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
        oprot.writeStructBegin('CapabilityStrIDL')
        if self.cap_name != None:
            oprot.writeFieldBegin('cap_name', TType.STRING, 1)
            oprot.writeString(self.cap_name)
            oprot.writeFieldEnd()
        if self.cap_value != None:
            oprot.writeFieldBegin('cap_value', TType.LIST, 2)
            oprot.writeListBegin(TType.STRING, len(self.cap_value))
            for iter6 in self.cap_value:
                oprot.writeString(iter6)

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




class CapabilityIntIDL(object):
    """
    Attributes:
     - cap_name
     - cap_value
    """

    thrift_spec = (None, (1,
      TType.STRING,
      'cap_name',
      None,
      None), (2,
      TType.LIST,
      'cap_value',
      (TType.I32, None),
      None))

    def __init__(self, cap_name = None, cap_value = None):
        self.cap_name = cap_name
        self.cap_value = cap_value



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
                    self.cap_name = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.cap_value = []
                    (_etype10, _size7,) = iprot.readListBegin()
                    for _i11 in xrange(_size7):
                        _elem12 = iprot.readI32()
                        self.cap_value.append(_elem12)

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
        oprot.writeStructBegin('CapabilityIntIDL')
        if self.cap_name != None:
            oprot.writeFieldBegin('cap_name', TType.STRING, 1)
            oprot.writeString(self.cap_name)
            oprot.writeFieldEnd()
        if self.cap_value != None:
            oprot.writeFieldBegin('cap_value', TType.LIST, 2)
            oprot.writeListBegin(TType.I32, len(self.cap_value))
            for iter13 in self.cap_value:
                oprot.writeI32(iter13)

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
# 2015.02.05 17:20:47 IST
