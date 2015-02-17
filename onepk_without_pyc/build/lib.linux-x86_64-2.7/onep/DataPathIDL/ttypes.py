# 2015.02.05 17:18:09 IST
from thrift.Thrift import *
import Shared.ttypes
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
    from thrift.protocol import fastbinary
except:
    fastbinary = None

class onep_element_provisioning_params_t(object):
    """
    Attributes:
     - elem_sender_id
     - elem_transport_address
    """

    thrift_spec = (None, (1,
      TType.I32,
      'elem_sender_id',
      None,
      None), (2,
      TType.STRING,
      'elem_transport_address',
      None,
      None))

    def __init__(self, elem_sender_id = None, elem_transport_address = None):
        self.elem_sender_id = elem_sender_id
        self.elem_transport_address = elem_transport_address



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
                    self.elem_sender_id = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.elem_transport_address = iprot.readString()
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
        oprot.writeStructBegin('onep_element_provisioning_params_t')
        if self.elem_sender_id != None:
            oprot.writeFieldBegin('elem_sender_id', TType.I32, 1)
            oprot.writeI32(self.elem_sender_id)
            oprot.writeFieldEnd()
        if self.elem_transport_address != None:
            oprot.writeFieldBegin('elem_transport_address', TType.STRING, 2)
            oprot.writeString(self.elem_transport_address)
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
# 2015.02.05 17:18:09 IST
