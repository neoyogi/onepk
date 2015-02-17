# 2015.02.05 17:20:12 IST
from thrift.Thrift import *
import Shared.ttypes
import AaaIDL.ttypes
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
    from thrift.protocol import fastbinary
except:
    fastbinary = None

class SanetSessionListIDL(object):
    """
    Attributes:
     - sessionNum
     - attr_list
    """

    thrift_spec = (None, (1,
      TType.I32,
      'sessionNum',
      None,
      None), (2,
      TType.LIST,
      'attr_list',
      (TType.STRUCT, (AaaIDL.ttypes.Attribute_IDL, AaaIDL.ttypes.Attribute_IDL.thrift_spec)),
      None))

    def __init__(self, sessionNum = None, attr_list = None):
        self.sessionNum = sessionNum
        self.attr_list = attr_list



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
                    self.sessionNum = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.attr_list = []
                    (_etype3, _size0,) = iprot.readListBegin()
                    for _i4 in xrange(_size0):
                        _elem5 = AaaIDL.ttypes.Attribute_IDL()
                        _elem5.read(iprot)
                        self.attr_list.append(_elem5)

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
        oprot.writeStructBegin('SanetSessionListIDL')
        if self.sessionNum != None:
            oprot.writeFieldBegin('sessionNum', TType.I32, 1)
            oprot.writeI32(self.sessionNum)
            oprot.writeFieldEnd()
        if self.attr_list != None:
            oprot.writeFieldBegin('attr_list', TType.LIST, 2)
            oprot.writeListBegin(TType.STRUCT, len(self.attr_list))
            for iter6 in self.attr_list:
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




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:20:12 IST
