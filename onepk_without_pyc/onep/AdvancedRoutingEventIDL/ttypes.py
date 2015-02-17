# 2015.02.05 17:20:43 IST
from thrift.Thrift import *
import SharedOut.ttypes
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
    from thrift.protocol import fastbinary
except:
    fastbinary = None

class RoutingAdjacencyOutIDL(object):
    """
    Attributes:
     - protocol
     - state
     - node_id
     - protocol_tag
     - if_name
     - vrf_name
     - remote_as
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'protocol',
      None,
      None),
     (2,
      TType.I32,
      'state',
      None,
      None),
     (3,
      TType.STRUCT,
      'node_id',
      (SharedOut.ttypes.NetworkAddressOutIDL, SharedOut.ttypes.NetworkAddressOutIDL.thrift_spec),
      None),
     (4,
      TType.STRING,
      'protocol_tag',
      None,
      None),
     (5,
      TType.STRING,
      'if_name',
      None,
      None),
     (6,
      TType.STRING,
      'vrf_name',
      None,
      None),
     (7,
      TType.I32,
      'remote_as',
      None,
      None))

    def __init__(self, protocol = None, state = None, node_id = None, protocol_tag = None, if_name = None, vrf_name = None, remote_as = None):
        self.protocol = protocol
        self.state = state
        self.node_id = node_id
        self.protocol_tag = protocol_tag
        self.if_name = if_name
        self.vrf_name = vrf_name
        self.remote_as = remote_as



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
                    self.protocol = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.state = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRUCT:
                    self.node_id = SharedOut.ttypes.NetworkAddressOutIDL()
                    self.node_id.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.protocol_tag = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.if_name = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRING:
                    self.vrf_name = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I32:
                    self.remote_as = iprot.readI32()
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
        oprot.writeStructBegin('RoutingAdjacencyOutIDL')
        if self.protocol != None:
            oprot.writeFieldBegin('protocol', TType.I32, 1)
            oprot.writeI32(self.protocol)
            oprot.writeFieldEnd()
        if self.state != None:
            oprot.writeFieldBegin('state', TType.I32, 2)
            oprot.writeI32(self.state)
            oprot.writeFieldEnd()
        if self.node_id != None:
            oprot.writeFieldBegin('node_id', TType.STRUCT, 3)
            self.node_id.write(oprot)
            oprot.writeFieldEnd()
        if self.protocol_tag != None:
            oprot.writeFieldBegin('protocol_tag', TType.STRING, 4)
            oprot.writeString(self.protocol_tag)
            oprot.writeFieldEnd()
        if self.if_name != None:
            oprot.writeFieldBegin('if_name', TType.STRING, 5)
            oprot.writeString(self.if_name)
            oprot.writeFieldEnd()
        if self.vrf_name != None:
            oprot.writeFieldBegin('vrf_name', TType.STRING, 6)
            oprot.writeString(self.vrf_name)
            oprot.writeFieldEnd()
        if self.remote_as != None:
            oprot.writeFieldBegin('remote_as', TType.I32, 7)
            oprot.writeI32(self.remote_as)
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
# 2015.02.05 17:20:44 IST
