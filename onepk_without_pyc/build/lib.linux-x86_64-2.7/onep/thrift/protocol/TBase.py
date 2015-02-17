# 2015.02.05 17:20:17 IST
from thrift.Thrift import *
from thrift.protocol import TBinaryProtocol
from thrift.transport import TTransport
try:
    from thrift.protocol import fastbinary
except:
    fastbinary = None

class TBase(object):
    __slots__ = []

    def __repr__(self):
        L = [ '%s=%r' % (key, getattr(self, key)) for key in self.__slots__ ]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))



    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        for attr in self.__slots__:
            my_val = getattr(self, attr)
            other_val = getattr(other, attr)
            if my_val != other_val:
                return False

        return True



    def __ne__(self, other):
        return not self == other



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStruct(self, self.thrift_spec)



    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return 
        oprot.writeStruct(self, self.thrift_spec)




class TExceptionBase(Exception):
    __slots__ = []
    __repr__ = TBase.__repr__.im_func
    __eq__ = TBase.__eq__.im_func
    __ne__ = TBase.__ne__.im_func
    read = TBase.read.im_func
    write = TBase.write.im_func


# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:20:17 IST
