# 2015.02.05 17:19:22 IST
from thrift.Thrift import *
import Shared.ttypes
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
    from thrift.protocol import fastbinary
except:
    fastbinary = None

class PathSpecIDL(object):
    """
    Attributes:
     - src_port
     - dst_port
     - protocol
     - src_ip
     - dst_ip
    """

    thrift_spec = (None,
     (1,
      TType.I16,
      'src_port',
      None,
      None),
     (2,
      TType.I16,
      'dst_port',
      None,
      None),
     (3,
      TType.I16,
      'protocol',
      None,
      None),
     (4,
      TType.STRUCT,
      'src_ip',
      (Shared.ttypes.NetworkAddressIDL, Shared.ttypes.NetworkAddressIDL.thrift_spec),
      None),
     (5,
      TType.STRUCT,
      'dst_ip',
      (Shared.ttypes.NetworkAddressIDL, Shared.ttypes.NetworkAddressIDL.thrift_spec),
      None))

    def __init__(self, src_port = None, dst_port = None, protocol = None, src_ip = None, dst_ip = None):
        self.src_port = src_port
        self.dst_port = dst_port
        self.protocol = protocol
        self.src_ip = src_ip
        self.dst_ip = dst_ip



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
                    self.src_port = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I16:
                    self.dst_port = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I16:
                    self.protocol = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRUCT:
                    self.src_ip = Shared.ttypes.NetworkAddressIDL()
                    self.src_ip.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRUCT:
                    self.dst_ip = Shared.ttypes.NetworkAddressIDL()
                    self.dst_ip.read(iprot)
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
        oprot.writeStructBegin('PathSpecIDL')
        if self.src_port != None:
            oprot.writeFieldBegin('src_port', TType.I16, 1)
            oprot.writeI16(self.src_port)
            oprot.writeFieldEnd()
        if self.dst_port != None:
            oprot.writeFieldBegin('dst_port', TType.I16, 2)
            oprot.writeI16(self.dst_port)
            oprot.writeFieldEnd()
        if self.protocol != None:
            oprot.writeFieldBegin('protocol', TType.I16, 3)
            oprot.writeI16(self.protocol)
            oprot.writeFieldEnd()
        if self.src_ip != None:
            oprot.writeFieldBegin('src_ip', TType.STRUCT, 4)
            self.src_ip.write(oprot)
            oprot.writeFieldEnd()
        if self.dst_ip != None:
            oprot.writeFieldBegin('dst_ip', TType.STRUCT, 5)
            self.dst_ip.write(oprot)
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




class PathTraceRequestIDL(object):
    """
    Attributes:
     - profile
     - timeout
     - pathspec
    """

    thrift_spec = (None,
     (1,
      TType.BYTE,
      'profile',
      None,
      None),
     (2,
      TType.I16,
      'timeout',
      None,
      None),
     (3,
      TType.STRUCT,
      'pathspec',
      (PathSpecIDL, PathSpecIDL.thrift_spec),
      None))

    def __init__(self, profile = None, timeout = None, pathspec = None):
        self.profile = profile
        self.timeout = timeout
        self.pathspec = pathspec



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
                    self.profile = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I16:
                    self.timeout = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRUCT:
                    self.pathspec = PathSpecIDL()
                    self.pathspec.read(iprot)
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
        oprot.writeStructBegin('PathTraceRequestIDL')
        if self.profile != None:
            oprot.writeFieldBegin('profile', TType.BYTE, 1)
            oprot.writeByte(self.profile)
            oprot.writeFieldEnd()
        if self.timeout != None:
            oprot.writeFieldBegin('timeout', TType.I16, 2)
            oprot.writeI16(self.timeout)
            oprot.writeFieldEnd()
        if self.pathspec != None:
            oprot.writeFieldBegin('pathspec', TType.STRUCT, 3)
            self.pathspec.write(oprot)
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




class PathTraceEchoProfileIDL(object):
    """
    Attributes:
     - reachability_addr
     - ingress_intf_name
     - egress_intf_name
    """

    thrift_spec = (None,
     (1,
      TType.STRUCT,
      'reachability_addr',
      (Shared.ttypes.NetworkAddressIDL, Shared.ttypes.NetworkAddressIDL.thrift_spec),
      None),
     (2,
      TType.STRING,
      'ingress_intf_name',
      None,
      None),
     (3,
      TType.STRING,
      'egress_intf_name',
      None,
      None))

    def __init__(self, reachability_addr = None, ingress_intf_name = None, egress_intf_name = None):
        self.reachability_addr = reachability_addr
        self.ingress_intf_name = ingress_intf_name
        self.egress_intf_name = egress_intf_name



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
                    self.reachability_addr = Shared.ttypes.NetworkAddressIDL()
                    self.reachability_addr.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.ingress_intf_name = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.egress_intf_name = iprot.readString()
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
        oprot.writeStructBegin('PathTraceEchoProfileIDL')
        if self.reachability_addr != None:
            oprot.writeFieldBegin('reachability_addr', TType.STRUCT, 1)
            self.reachability_addr.write(oprot)
            oprot.writeFieldEnd()
        if self.ingress_intf_name != None:
            oprot.writeFieldBegin('ingress_intf_name', TType.STRING, 2)
            oprot.writeString(self.ingress_intf_name)
            oprot.writeFieldEnd()
        if self.egress_intf_name != None:
            oprot.writeFieldBegin('egress_intf_name', TType.STRING, 3)
            oprot.writeString(self.egress_intf_name)
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




class PathTraceIntfProfileIDL(object):
    """
    Attributes:
     - collection_timestamp
     - octet_input_ingress
     - octet_output_egress
     - pkts_errored_ingress
     - pkts_errored_egress
     - pkts_discarded_ingress
     - pkts_discarded_egress
     - ingress_intf_speed
     - egress_intf_speed
    """

    thrift_spec = (None,
     (1,
      TType.I64,
      'collection_timestamp',
      None,
      None),
     (2,
      TType.I32,
      'octet_input_ingress',
      None,
      None),
     (3,
      TType.I32,
      'octet_output_egress',
      None,
      None),
     (4,
      TType.I32,
      'pkts_errored_ingress',
      None,
      None),
     (5,
      TType.I32,
      'pkts_errored_egress',
      None,
      None),
     (6,
      TType.I32,
      'pkts_discarded_ingress',
      None,
      None),
     (7,
      TType.I32,
      'pkts_discarded_egress',
      None,
      None),
     (8,
      TType.I32,
      'ingress_intf_speed',
      None,
      None),
     (9,
      TType.I32,
      'egress_intf_speed',
      None,
      None))

    def __init__(self, collection_timestamp = None, octet_input_ingress = None, octet_output_egress = None, pkts_errored_ingress = None, pkts_errored_egress = None, pkts_discarded_ingress = None, pkts_discarded_egress = None, ingress_intf_speed = None, egress_intf_speed = None):
        self.collection_timestamp = collection_timestamp
        self.octet_input_ingress = octet_input_ingress
        self.octet_output_egress = octet_output_egress
        self.pkts_errored_ingress = pkts_errored_ingress
        self.pkts_errored_egress = pkts_errored_egress
        self.pkts_discarded_ingress = pkts_discarded_ingress
        self.pkts_discarded_egress = pkts_discarded_egress
        self.ingress_intf_speed = ingress_intf_speed
        self.egress_intf_speed = egress_intf_speed



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
                    self.collection_timestamp = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.octet_input_ingress = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.octet_output_egress = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.pkts_errored_ingress = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.pkts_errored_egress = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I32:
                    self.pkts_discarded_ingress = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I32:
                    self.pkts_discarded_egress = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.I32:
                    self.ingress_intf_speed = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.I32:
                    self.egress_intf_speed = iprot.readI32()
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
        oprot.writeStructBegin('PathTraceIntfProfileIDL')
        if self.collection_timestamp != None:
            oprot.writeFieldBegin('collection_timestamp', TType.I64, 1)
            oprot.writeI64(self.collection_timestamp)
            oprot.writeFieldEnd()
        if self.octet_input_ingress != None:
            oprot.writeFieldBegin('octet_input_ingress', TType.I32, 2)
            oprot.writeI32(self.octet_input_ingress)
            oprot.writeFieldEnd()
        if self.octet_output_egress != None:
            oprot.writeFieldBegin('octet_output_egress', TType.I32, 3)
            oprot.writeI32(self.octet_output_egress)
            oprot.writeFieldEnd()
        if self.pkts_errored_ingress != None:
            oprot.writeFieldBegin('pkts_errored_ingress', TType.I32, 4)
            oprot.writeI32(self.pkts_errored_ingress)
            oprot.writeFieldEnd()
        if self.pkts_errored_egress != None:
            oprot.writeFieldBegin('pkts_errored_egress', TType.I32, 5)
            oprot.writeI32(self.pkts_errored_egress)
            oprot.writeFieldEnd()
        if self.pkts_discarded_ingress != None:
            oprot.writeFieldBegin('pkts_discarded_ingress', TType.I32, 6)
            oprot.writeI32(self.pkts_discarded_ingress)
            oprot.writeFieldEnd()
        if self.pkts_discarded_egress != None:
            oprot.writeFieldBegin('pkts_discarded_egress', TType.I32, 7)
            oprot.writeI32(self.pkts_discarded_egress)
            oprot.writeFieldEnd()
        if self.ingress_intf_speed != None:
            oprot.writeFieldBegin('ingress_intf_speed', TType.I32, 8)
            oprot.writeI32(self.ingress_intf_speed)
            oprot.writeFieldEnd()
        if self.egress_intf_speed != None:
            oprot.writeFieldBegin('egress_intf_speed', TType.I32, 9)
            oprot.writeI32(self.egress_intf_speed)
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




class PathTraceCPUProfileIDL(object):
    """
    Attributes:
     - collection_timestamp
     - one_min_cpu_util
     - five_min_cpu_util
    """

    thrift_spec = (None,
     (1,
      TType.I64,
      'collection_timestamp',
      None,
      None),
     (2,
      TType.BYTE,
      'one_min_cpu_util',
      None,
      None),
     (3,
      TType.BYTE,
      'five_min_cpu_util',
      None,
      None))

    def __init__(self, collection_timestamp = None, one_min_cpu_util = None, five_min_cpu_util = None):
        self.collection_timestamp = collection_timestamp
        self.one_min_cpu_util = one_min_cpu_util
        self.five_min_cpu_util = five_min_cpu_util



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
                    self.collection_timestamp = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.BYTE:
                    self.one_min_cpu_util = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.BYTE:
                    self.five_min_cpu_util = iprot.readByte()
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
        oprot.writeStructBegin('PathTraceCPUProfileIDL')
        if self.collection_timestamp != None:
            oprot.writeFieldBegin('collection_timestamp', TType.I64, 1)
            oprot.writeI64(self.collection_timestamp)
            oprot.writeFieldEnd()
        if self.one_min_cpu_util != None:
            oprot.writeFieldBegin('one_min_cpu_util', TType.BYTE, 2)
            oprot.writeByte(self.one_min_cpu_util)
            oprot.writeFieldEnd()
        if self.five_min_cpu_util != None:
            oprot.writeFieldBegin('five_min_cpu_util', TType.BYTE, 3)
            oprot.writeByte(self.five_min_cpu_util)
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




class PathTraceMemProfileIDL(object):
    """
    Attributes:
     - collection_timestamp
     - proc_mem_util
    """

    thrift_spec = (None, (1,
      TType.I64,
      'collection_timestamp',
      None,
      None), (2,
      TType.BYTE,
      'proc_mem_util',
      None,
      None))

    def __init__(self, collection_timestamp = None, proc_mem_util = None):
        self.collection_timestamp = collection_timestamp
        self.proc_mem_util = proc_mem_util



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
                    self.collection_timestamp = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.BYTE:
                    self.proc_mem_util = iprot.readByte()
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
        oprot.writeStructBegin('PathTraceMemProfileIDL')
        if self.collection_timestamp != None:
            oprot.writeFieldBegin('collection_timestamp', TType.I64, 1)
            oprot.writeI64(self.collection_timestamp)
            oprot.writeFieldEnd()
        if self.proc_mem_util != None:
            oprot.writeFieldBegin('proc_mem_util', TType.BYTE, 2)
            oprot.writeByte(self.proc_mem_util)
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




class PathTracePerfMonProfileIDL(object):
    """
    Attributes:
     - src_ip
     - dst_ip
     - src_port
     - dst_port
     - collection_timestamp
     - loss_of_measurement_confidence
     - media_stop_event_occured
     - ip_packet_drop_count
     - ip_byte_count
     - ip_packet_count
     - ip_byte_rate
     - route_fwd_status
     - ip_dscp
     - ip_ttl
     - flow_count
     - flow_dirn
     - protocol
    """

    thrift_spec = (None,
     (1,
      TType.STRUCT,
      'src_ip',
      (Shared.ttypes.NetworkAddressIDL, Shared.ttypes.NetworkAddressIDL.thrift_spec),
      None),
     (2,
      TType.STRUCT,
      'dst_ip',
      (Shared.ttypes.NetworkAddressIDL, Shared.ttypes.NetworkAddressIDL.thrift_spec),
      None),
     (3,
      TType.I16,
      'src_port',
      None,
      None),
     (4,
      TType.I16,
      'dst_port',
      None,
      None),
     (5,
      TType.I64,
      'collection_timestamp',
      None,
      None),
     (6,
      TType.BYTE,
      'loss_of_measurement_confidence',
      None,
      None),
     (7,
      TType.BYTE,
      'media_stop_event_occured',
      None,
      None),
     (8,
      TType.I64,
      'ip_packet_drop_count',
      None,
      None),
     (9,
      TType.I64,
      'ip_byte_count',
      None,
      None),
     (10,
      TType.I64,
      'ip_packet_count',
      None,
      None),
     (11,
      TType.I32,
      'ip_byte_rate',
      None,
      None),
     (12,
      TType.STRING,
      'route_fwd_status',
      None,
      None),
     (13,
      TType.BYTE,
      'ip_dscp',
      None,
      None),
     (14,
      TType.BYTE,
      'ip_ttl',
      None,
      None),
     (15,
      TType.I32,
      'flow_count',
      None,
      None),
     (16,
      TType.BYTE,
      'flow_dirn',
      None,
      None),
     (17,
      TType.I16,
      'protocol',
      None,
      None))

    def __init__(self, src_ip = None, dst_ip = None, src_port = None, dst_port = None, collection_timestamp = None, loss_of_measurement_confidence = None, media_stop_event_occured = None, ip_packet_drop_count = None, ip_byte_count = None, ip_packet_count = None, ip_byte_rate = None, route_fwd_status = None, ip_dscp = None, ip_ttl = None, flow_count = None, flow_dirn = None, protocol = None):
        self.src_ip = src_ip
        self.dst_ip = dst_ip
        self.src_port = src_port
        self.dst_port = dst_port
        self.collection_timestamp = collection_timestamp
        self.loss_of_measurement_confidence = loss_of_measurement_confidence
        self.media_stop_event_occured = media_stop_event_occured
        self.ip_packet_drop_count = ip_packet_drop_count
        self.ip_byte_count = ip_byte_count
        self.ip_packet_count = ip_packet_count
        self.ip_byte_rate = ip_byte_rate
        self.route_fwd_status = route_fwd_status
        self.ip_dscp = ip_dscp
        self.ip_ttl = ip_ttl
        self.flow_count = flow_count
        self.flow_dirn = flow_dirn
        self.protocol = protocol



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
                    self.src_ip = Shared.ttypes.NetworkAddressIDL()
                    self.src_ip.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.dst_ip = Shared.ttypes.NetworkAddressIDL()
                    self.dst_ip.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I16:
                    self.src_port = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I16:
                    self.dst_port = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I64:
                    self.collection_timestamp = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.BYTE:
                    self.loss_of_measurement_confidence = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.BYTE:
                    self.media_stop_event_occured = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.I64:
                    self.ip_packet_drop_count = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.I64:
                    self.ip_byte_count = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.I64:
                    self.ip_packet_count = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.I32:
                    self.ip_byte_rate = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 12:
                if ftype == TType.STRING:
                    self.route_fwd_status = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 13:
                if ftype == TType.BYTE:
                    self.ip_dscp = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 14:
                if ftype == TType.BYTE:
                    self.ip_ttl = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 15:
                if ftype == TType.I32:
                    self.flow_count = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 16:
                if ftype == TType.BYTE:
                    self.flow_dirn = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 17:
                if ftype == TType.I16:
                    self.protocol = iprot.readI16()
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
        oprot.writeStructBegin('PathTracePerfMonProfileIDL')
        if self.src_ip != None:
            oprot.writeFieldBegin('src_ip', TType.STRUCT, 1)
            self.src_ip.write(oprot)
            oprot.writeFieldEnd()
        if self.dst_ip != None:
            oprot.writeFieldBegin('dst_ip', TType.STRUCT, 2)
            self.dst_ip.write(oprot)
            oprot.writeFieldEnd()
        if self.src_port != None:
            oprot.writeFieldBegin('src_port', TType.I16, 3)
            oprot.writeI16(self.src_port)
            oprot.writeFieldEnd()
        if self.dst_port != None:
            oprot.writeFieldBegin('dst_port', TType.I16, 4)
            oprot.writeI16(self.dst_port)
            oprot.writeFieldEnd()
        if self.collection_timestamp != None:
            oprot.writeFieldBegin('collection_timestamp', TType.I64, 5)
            oprot.writeI64(self.collection_timestamp)
            oprot.writeFieldEnd()
        if self.loss_of_measurement_confidence != None:
            oprot.writeFieldBegin('loss_of_measurement_confidence', TType.BYTE, 6)
            oprot.writeByte(self.loss_of_measurement_confidence)
            oprot.writeFieldEnd()
        if self.media_stop_event_occured != None:
            oprot.writeFieldBegin('media_stop_event_occured', TType.BYTE, 7)
            oprot.writeByte(self.media_stop_event_occured)
            oprot.writeFieldEnd()
        if self.ip_packet_drop_count != None:
            oprot.writeFieldBegin('ip_packet_drop_count', TType.I64, 8)
            oprot.writeI64(self.ip_packet_drop_count)
            oprot.writeFieldEnd()
        if self.ip_byte_count != None:
            oprot.writeFieldBegin('ip_byte_count', TType.I64, 9)
            oprot.writeI64(self.ip_byte_count)
            oprot.writeFieldEnd()
        if self.ip_packet_count != None:
            oprot.writeFieldBegin('ip_packet_count', TType.I64, 10)
            oprot.writeI64(self.ip_packet_count)
            oprot.writeFieldEnd()
        if self.ip_byte_rate != None:
            oprot.writeFieldBegin('ip_byte_rate', TType.I32, 11)
            oprot.writeI32(self.ip_byte_rate)
            oprot.writeFieldEnd()
        if self.route_fwd_status != None:
            oprot.writeFieldBegin('route_fwd_status', TType.STRING, 12)
            oprot.writeString(self.route_fwd_status)
            oprot.writeFieldEnd()
        if self.ip_dscp != None:
            oprot.writeFieldBegin('ip_dscp', TType.BYTE, 13)
            oprot.writeByte(self.ip_dscp)
            oprot.writeFieldEnd()
        if self.ip_ttl != None:
            oprot.writeFieldBegin('ip_ttl', TType.BYTE, 14)
            oprot.writeByte(self.ip_ttl)
            oprot.writeFieldEnd()
        if self.flow_count != None:
            oprot.writeFieldBegin('flow_count', TType.I32, 15)
            oprot.writeI32(self.flow_count)
            oprot.writeFieldEnd()
        if self.flow_dirn != None:
            oprot.writeFieldBegin('flow_dirn', TType.BYTE, 16)
            oprot.writeByte(self.flow_dirn)
            oprot.writeFieldEnd()
        if self.protocol != None:
            oprot.writeFieldBegin('protocol', TType.I16, 17)
            oprot.writeI16(self.protocol)
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




class PathTraceProfilesIDL(object):
    """
    Attributes:
     - profile_type
     - EchoProfile
     - IntfProfile
     - CPUProfile
     - MemProfile
     - PerfMonProfile
    """

    thrift_spec = (None,
     (1,
      TType.BYTE,
      'profile_type',
      None,
      None),
     (2,
      TType.STRUCT,
      'EchoProfile',
      (PathTraceEchoProfileIDL, PathTraceEchoProfileIDL.thrift_spec),
      None),
     (3,
      TType.STRUCT,
      'IntfProfile',
      (PathTraceIntfProfileIDL, PathTraceIntfProfileIDL.thrift_spec),
      None),
     (4,
      TType.STRUCT,
      'CPUProfile',
      (PathTraceCPUProfileIDL, PathTraceCPUProfileIDL.thrift_spec),
      None),
     (5,
      TType.STRUCT,
      'MemProfile',
      (PathTraceMemProfileIDL, PathTraceMemProfileIDL.thrift_spec),
      None),
     (6,
      TType.STRUCT,
      'PerfMonProfile',
      (PathTracePerfMonProfileIDL, PathTracePerfMonProfileIDL.thrift_spec),
      None))

    def __init__(self, profile_type = None, EchoProfile = None, IntfProfile = None, CPUProfile = None, MemProfile = None, PerfMonProfile = None):
        self.profile_type = profile_type
        self.EchoProfile = EchoProfile
        self.IntfProfile = IntfProfile
        self.CPUProfile = CPUProfile
        self.MemProfile = MemProfile
        self.PerfMonProfile = PerfMonProfile



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
                    self.profile_type = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.EchoProfile = PathTraceEchoProfileIDL()
                    self.EchoProfile.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRUCT:
                    self.IntfProfile = PathTraceIntfProfileIDL()
                    self.IntfProfile.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRUCT:
                    self.CPUProfile = PathTraceCPUProfileIDL()
                    self.CPUProfile.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRUCT:
                    self.MemProfile = PathTraceMemProfileIDL()
                    self.MemProfile.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRUCT:
                    self.PerfMonProfile = PathTracePerfMonProfileIDL()
                    self.PerfMonProfile.read(iprot)
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
        oprot.writeStructBegin('PathTraceProfilesIDL')
        if self.profile_type != None:
            oprot.writeFieldBegin('profile_type', TType.BYTE, 1)
            oprot.writeByte(self.profile_type)
            oprot.writeFieldEnd()
        if self.EchoProfile != None:
            oprot.writeFieldBegin('EchoProfile', TType.STRUCT, 2)
            self.EchoProfile.write(oprot)
            oprot.writeFieldEnd()
        if self.IntfProfile != None:
            oprot.writeFieldBegin('IntfProfile', TType.STRUCT, 3)
            self.IntfProfile.write(oprot)
            oprot.writeFieldEnd()
        if self.CPUProfile != None:
            oprot.writeFieldBegin('CPUProfile', TType.STRUCT, 4)
            self.CPUProfile.write(oprot)
            oprot.writeFieldEnd()
        if self.MemProfile != None:
            oprot.writeFieldBegin('MemProfile', TType.STRUCT, 5)
            self.MemProfile.write(oprot)
            oprot.writeFieldEnd()
        if self.PerfMonProfile != None:
            oprot.writeFieldBegin('PerfMonProfile', TType.STRUCT, 6)
            self.PerfMonProfile.write(oprot)
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




class PathTraceNodeIDL(object):
    """
    Attributes:
     - hostname
     - node_type
     - node_index
     - ip_ttl
     - rtt
     - node_status
     - Profiles
    """

    thrift_spec = (None,
     (1,
      TType.STRING,
      'hostname',
      None,
      None),
     (2,
      TType.BYTE,
      'node_type',
      None,
      None),
     (3,
      TType.I16,
      'node_index',
      None,
      None),
     (4,
      TType.BYTE,
      'ip_ttl',
      None,
      None),
     (5,
      TType.I16,
      'rtt',
      None,
      None),
     (6,
      TType.BYTE,
      'node_status',
      None,
      None),
     (7,
      TType.STRUCT,
      'Profiles',
      (PathTraceProfilesIDL, PathTraceProfilesIDL.thrift_spec),
      None))

    def __init__(self, hostname = None, node_type = None, node_index = None, ip_ttl = None, rtt = None, node_status = None, Profiles = None):
        self.hostname = hostname
        self.node_type = node_type
        self.node_index = node_index
        self.ip_ttl = ip_ttl
        self.rtt = rtt
        self.node_status = node_status
        self.Profiles = Profiles



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
                    self.hostname = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.BYTE:
                    self.node_type = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I16:
                    self.node_index = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.BYTE:
                    self.ip_ttl = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I16:
                    self.rtt = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.BYTE:
                    self.node_status = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.STRUCT:
                    self.Profiles = PathTraceProfilesIDL()
                    self.Profiles.read(iprot)
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
        oprot.writeStructBegin('PathTraceNodeIDL')
        if self.hostname != None:
            oprot.writeFieldBegin('hostname', TType.STRING, 1)
            oprot.writeString(self.hostname)
            oprot.writeFieldEnd()
        if self.node_type != None:
            oprot.writeFieldBegin('node_type', TType.BYTE, 2)
            oprot.writeByte(self.node_type)
            oprot.writeFieldEnd()
        if self.node_index != None:
            oprot.writeFieldBegin('node_index', TType.I16, 3)
            oprot.writeI16(self.node_index)
            oprot.writeFieldEnd()
        if self.ip_ttl != None:
            oprot.writeFieldBegin('ip_ttl', TType.BYTE, 4)
            oprot.writeByte(self.ip_ttl)
            oprot.writeFieldEnd()
        if self.rtt != None:
            oprot.writeFieldBegin('rtt', TType.I16, 5)
            oprot.writeI16(self.rtt)
            oprot.writeFieldEnd()
        if self.node_status != None:
            oprot.writeFieldBegin('node_status', TType.BYTE, 6)
            oprot.writeByte(self.node_status)
            oprot.writeFieldEnd()
        if self.Profiles != None:
            oprot.writeFieldBegin('Profiles', TType.STRUCT, 7)
            self.Profiles.write(oprot)
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




class PathTraceGraphIDL(object):
    """
    Attributes:
     - route_index
     - profile
     - route_status
     - traceroute_status
     - nodes_successful
     - nodes_errored
     - nodes_no_data
     - non_pt_nodes
     - collection_timestamp
     - last_route_change_timestamp
     - node_list
    """

    thrift_spec = (None,
     (1,
      TType.BYTE,
      'route_index',
      None,
      None),
     (2,
      TType.BYTE,
      'profile',
      None,
      None),
     (3,
      TType.BYTE,
      'route_status',
      None,
      None),
     (4,
      TType.BYTE,
      'traceroute_status',
      None,
      None),
     (5,
      TType.BYTE,
      'nodes_successful',
      None,
      None),
     (6,
      TType.BYTE,
      'nodes_errored',
      None,
      None),
     (7,
      TType.BYTE,
      'nodes_no_data',
      None,
      None),
     (8,
      TType.BYTE,
      'non_pt_nodes',
      None,
      None),
     (9,
      TType.I64,
      'collection_timestamp',
      None,
      None),
     (10,
      TType.I64,
      'last_route_change_timestamp',
      None,
      None),
     (11,
      TType.LIST,
      'node_list',
      (TType.STRUCT, (PathTraceNodeIDL, PathTraceNodeIDL.thrift_spec)),
      None))

    def __init__(self, route_index = None, profile = None, route_status = None, traceroute_status = None, nodes_successful = None, nodes_errored = None, nodes_no_data = None, non_pt_nodes = None, collection_timestamp = None, last_route_change_timestamp = None, node_list = None):
        self.route_index = route_index
        self.profile = profile
        self.route_status = route_status
        self.traceroute_status = traceroute_status
        self.nodes_successful = nodes_successful
        self.nodes_errored = nodes_errored
        self.nodes_no_data = nodes_no_data
        self.non_pt_nodes = non_pt_nodes
        self.collection_timestamp = collection_timestamp
        self.last_route_change_timestamp = last_route_change_timestamp
        self.node_list = node_list



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
                    self.route_index = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.BYTE:
                    self.profile = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.BYTE:
                    self.route_status = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.BYTE:
                    self.traceroute_status = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.BYTE:
                    self.nodes_successful = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.BYTE:
                    self.nodes_errored = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.BYTE:
                    self.nodes_no_data = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.BYTE:
                    self.non_pt_nodes = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.I64:
                    self.collection_timestamp = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.I64:
                    self.last_route_change_timestamp = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.LIST:
                    self.node_list = []
                    (_etype3, _size0,) = iprot.readListBegin()
                    for _i4 in xrange(_size0):
                        _elem5 = PathTraceNodeIDL()
                        _elem5.read(iprot)
                        self.node_list.append(_elem5)

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
        oprot.writeStructBegin('PathTraceGraphIDL')
        if self.route_index != None:
            oprot.writeFieldBegin('route_index', TType.BYTE, 1)
            oprot.writeByte(self.route_index)
            oprot.writeFieldEnd()
        if self.profile != None:
            oprot.writeFieldBegin('profile', TType.BYTE, 2)
            oprot.writeByte(self.profile)
            oprot.writeFieldEnd()
        if self.route_status != None:
            oprot.writeFieldBegin('route_status', TType.BYTE, 3)
            oprot.writeByte(self.route_status)
            oprot.writeFieldEnd()
        if self.traceroute_status != None:
            oprot.writeFieldBegin('traceroute_status', TType.BYTE, 4)
            oprot.writeByte(self.traceroute_status)
            oprot.writeFieldEnd()
        if self.nodes_successful != None:
            oprot.writeFieldBegin('nodes_successful', TType.BYTE, 5)
            oprot.writeByte(self.nodes_successful)
            oprot.writeFieldEnd()
        if self.nodes_errored != None:
            oprot.writeFieldBegin('nodes_errored', TType.BYTE, 6)
            oprot.writeByte(self.nodes_errored)
            oprot.writeFieldEnd()
        if self.nodes_no_data != None:
            oprot.writeFieldBegin('nodes_no_data', TType.BYTE, 7)
            oprot.writeByte(self.nodes_no_data)
            oprot.writeFieldEnd()
        if self.non_pt_nodes != None:
            oprot.writeFieldBegin('non_pt_nodes', TType.BYTE, 8)
            oprot.writeByte(self.non_pt_nodes)
            oprot.writeFieldEnd()
        if self.collection_timestamp != None:
            oprot.writeFieldBegin('collection_timestamp', TType.I64, 9)
            oprot.writeI64(self.collection_timestamp)
            oprot.writeFieldEnd()
        if self.last_route_change_timestamp != None:
            oprot.writeFieldBegin('last_route_change_timestamp', TType.I64, 10)
            oprot.writeI64(self.last_route_change_timestamp)
            oprot.writeFieldEnd()
        if self.node_list != None:
            oprot.writeFieldBegin('node_list', TType.LIST, 11)
            oprot.writeListBegin(TType.STRUCT, len(self.node_list))
            for iter6 in self.node_list:
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
# 2015.02.05 17:19:23 IST
