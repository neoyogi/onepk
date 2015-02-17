# 2015.02.05 17:19:15 IST
from thrift.Thrift import *
import Shared.ttypes
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
    from thrift.protocol import fastbinary
except:
    fastbinary = None

class SatisfiedTag_IDL(object):
    """
      Satisfied Tag
    
      Attributes:
       - tag_ref_bit_id
       - tag_uid
      """

    thrift_spec = (None, (1,
      TType.I32,
      'tag_ref_bit_id',
      None,
      None), (2,
      TType.I64,
      'tag_uid',
      None,
      None))

    def __init__(self, tag_ref_bit_id = None, tag_uid = None):
        self.tag_ref_bit_id = tag_ref_bit_id
        self.tag_uid = tag_uid



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
                    self.tag_ref_bit_id = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.tag_uid = iprot.readI64()
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
        oprot.writeStructBegin('SatisfiedTag_IDL')
        if self.tag_ref_bit_id != None:
            oprot.writeFieldBegin('tag_ref_bit_id', TType.I32, 1)
            oprot.writeI32(self.tag_ref_bit_id)
            oprot.writeFieldEnd()
        if self.tag_uid != None:
            oprot.writeFieldBegin('tag_uid', TType.I64, 2)
            oprot.writeI64(self.tag_uid)
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




class Proposition_IDL(object):
    """
      Proposition Parameters
    
      Attributes:
       - type
       - id
       - data_type
       - policy_version
       - name_string
       - numeric_value
       - value_string
       - address
       - end_address
       - mask
       - protocol
       - protocol_subtype
       - src_port_start
       - src_port_end
       - dst_port_start
       - dst_port_end
       - app_name
       - app_type
       - nbar_id
       - unified_id
       - satisfied_tags
       - uid
       - deny_reason
      """

    thrift_spec = (None,
     (1,
      TType.I32,
      'type',
      None,
      None),
     (2,
      TType.I32,
      'id',
      None,
      None),
     (3,
      TType.I32,
      'data_type',
      None,
      None),
     (4,
      TType.I64,
      'policy_version',
      None,
      None),
     (5,
      TType.STRING,
      'name_string',
      None,
      None),
     (6,
      TType.I64,
      'numeric_value',
      None,
      None),
     (7,
      TType.STRING,
      'value_string',
      None,
      None),
     (8,
      TType.STRUCT,
      'address',
      (Shared.ttypes.NetworkAddressIDL, Shared.ttypes.NetworkAddressIDL.thrift_spec),
      None),
     (9,
      TType.STRUCT,
      'end_address',
      (Shared.ttypes.NetworkAddressIDL, Shared.ttypes.NetworkAddressIDL.thrift_spec),
      None),
     (10,
      TType.I32,
      'mask',
      None,
      None),
     (11,
      TType.I32,
      'protocol',
      None,
      None),
     (12,
      TType.I32,
      'protocol_subtype',
      None,
      None),
     (13,
      TType.I32,
      'src_port_start',
      None,
      None),
     (14,
      TType.I32,
      'src_port_end',
      None,
      None),
     (15,
      TType.I32,
      'dst_port_start',
      None,
      None),
     (16,
      TType.I32,
      'dst_port_end',
      None,
      None),
     (17,
      TType.STRING,
      'app_name',
      None,
      None),
     (18,
      TType.STRING,
      'app_type',
      None,
      None),
     (19,
      TType.I32,
      'nbar_id',
      None,
      None),
     (20,
      TType.I32,
      'unified_id',
      None,
      None),
     (21,
      TType.LIST,
      'satisfied_tags',
      (TType.STRUCT, (SatisfiedTag_IDL, SatisfiedTag_IDL.thrift_spec)),
      None),
     (22,
      TType.I32,
      'uid',
      None,
      None),
     (23,
      TType.I32,
      'deny_reason',
      None,
      None))

    def __init__(self, type = None, id = None, data_type = None, policy_version = None, name_string = None, numeric_value = None, value_string = None, address = None, end_address = None, mask = None, protocol = None, protocol_subtype = None, src_port_start = None, src_port_end = None, dst_port_start = None, dst_port_end = None, app_name = None, app_type = None, nbar_id = None, unified_id = None, satisfied_tags = None, uid = None, deny_reason = None):
        self.type = type
        self.id = id
        self.data_type = data_type
        self.policy_version = policy_version
        self.name_string = name_string
        self.numeric_value = numeric_value
        self.value_string = value_string
        self.address = address
        self.end_address = end_address
        self.mask = mask
        self.protocol = protocol
        self.protocol_subtype = protocol_subtype
        self.src_port_start = src_port_start
        self.src_port_end = src_port_end
        self.dst_port_start = dst_port_start
        self.dst_port_end = dst_port_end
        self.app_name = app_name
        self.app_type = app_type
        self.nbar_id = nbar_id
        self.unified_id = unified_id
        self.satisfied_tags = satisfied_tags
        self.uid = uid
        self.deny_reason = deny_reason



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
                    self.type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.id = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.data_type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I64:
                    self.policy_version = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.name_string = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I64:
                    self.numeric_value = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.STRING:
                    self.value_string = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.STRUCT:
                    self.address = Shared.ttypes.NetworkAddressIDL()
                    self.address.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.STRUCT:
                    self.end_address = Shared.ttypes.NetworkAddressIDL()
                    self.end_address.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.I32:
                    self.mask = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.I32:
                    self.protocol = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 12:
                if ftype == TType.I32:
                    self.protocol_subtype = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 13:
                if ftype == TType.I32:
                    self.src_port_start = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 14:
                if ftype == TType.I32:
                    self.src_port_end = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 15:
                if ftype == TType.I32:
                    self.dst_port_start = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 16:
                if ftype == TType.I32:
                    self.dst_port_end = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 17:
                if ftype == TType.STRING:
                    self.app_name = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 18:
                if ftype == TType.STRING:
                    self.app_type = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 19:
                if ftype == TType.I32:
                    self.nbar_id = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 20:
                if ftype == TType.I32:
                    self.unified_id = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 21:
                if ftype == TType.LIST:
                    self.satisfied_tags = []
                    (_etype3, _size0,) = iprot.readListBegin()
                    for _i4 in xrange(_size0):
                        _elem5 = SatisfiedTag_IDL()
                        _elem5.read(iprot)
                        self.satisfied_tags.append(_elem5)

                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 22:
                if ftype == TType.I32:
                    self.uid = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 23:
                if ftype == TType.I32:
                    self.deny_reason = iprot.readI32()
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
        oprot.writeStructBegin('Proposition_IDL')
        if self.type != None:
            oprot.writeFieldBegin('type', TType.I32, 1)
            oprot.writeI32(self.type)
            oprot.writeFieldEnd()
        if self.id != None:
            oprot.writeFieldBegin('id', TType.I32, 2)
            oprot.writeI32(self.id)
            oprot.writeFieldEnd()
        if self.data_type != None:
            oprot.writeFieldBegin('data_type', TType.I32, 3)
            oprot.writeI32(self.data_type)
            oprot.writeFieldEnd()
        if self.policy_version != None:
            oprot.writeFieldBegin('policy_version', TType.I64, 4)
            oprot.writeI64(self.policy_version)
            oprot.writeFieldEnd()
        if self.name_string != None:
            oprot.writeFieldBegin('name_string', TType.STRING, 5)
            oprot.writeString(self.name_string)
            oprot.writeFieldEnd()
        if self.numeric_value != None:
            oprot.writeFieldBegin('numeric_value', TType.I64, 6)
            oprot.writeI64(self.numeric_value)
            oprot.writeFieldEnd()
        if self.value_string != None:
            oprot.writeFieldBegin('value_string', TType.STRING, 7)
            oprot.writeString(self.value_string)
            oprot.writeFieldEnd()
        if self.address != None:
            oprot.writeFieldBegin('address', TType.STRUCT, 8)
            self.address.write(oprot)
            oprot.writeFieldEnd()
        if self.end_address != None:
            oprot.writeFieldBegin('end_address', TType.STRUCT, 9)
            self.end_address.write(oprot)
            oprot.writeFieldEnd()
        if self.mask != None:
            oprot.writeFieldBegin('mask', TType.I32, 10)
            oprot.writeI32(self.mask)
            oprot.writeFieldEnd()
        if self.protocol != None:
            oprot.writeFieldBegin('protocol', TType.I32, 11)
            oprot.writeI32(self.protocol)
            oprot.writeFieldEnd()
        if self.protocol_subtype != None:
            oprot.writeFieldBegin('protocol_subtype', TType.I32, 12)
            oprot.writeI32(self.protocol_subtype)
            oprot.writeFieldEnd()
        if self.src_port_start != None:
            oprot.writeFieldBegin('src_port_start', TType.I32, 13)
            oprot.writeI32(self.src_port_start)
            oprot.writeFieldEnd()
        if self.src_port_end != None:
            oprot.writeFieldBegin('src_port_end', TType.I32, 14)
            oprot.writeI32(self.src_port_end)
            oprot.writeFieldEnd()
        if self.dst_port_start != None:
            oprot.writeFieldBegin('dst_port_start', TType.I32, 15)
            oprot.writeI32(self.dst_port_start)
            oprot.writeFieldEnd()
        if self.dst_port_end != None:
            oprot.writeFieldBegin('dst_port_end', TType.I32, 16)
            oprot.writeI32(self.dst_port_end)
            oprot.writeFieldEnd()
        if self.app_name != None:
            oprot.writeFieldBegin('app_name', TType.STRING, 17)
            oprot.writeString(self.app_name)
            oprot.writeFieldEnd()
        if self.app_type != None:
            oprot.writeFieldBegin('app_type', TType.STRING, 18)
            oprot.writeString(self.app_type)
            oprot.writeFieldEnd()
        if self.nbar_id != None:
            oprot.writeFieldBegin('nbar_id', TType.I32, 19)
            oprot.writeI32(self.nbar_id)
            oprot.writeFieldEnd()
        if self.unified_id != None:
            oprot.writeFieldBegin('unified_id', TType.I32, 20)
            oprot.writeI32(self.unified_id)
            oprot.writeFieldEnd()
        if self.satisfied_tags != None:
            oprot.writeFieldBegin('satisfied_tags', TType.LIST, 21)
            oprot.writeListBegin(TType.STRUCT, len(self.satisfied_tags))
            for iter6 in self.satisfied_tags:
                iter6.write(oprot)

            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.uid != None:
            oprot.writeFieldBegin('uid', TType.I32, 22)
            oprot.writeI32(self.uid)
            oprot.writeFieldEnd()
        if self.deny_reason != None:
            oprot.writeFieldBegin('deny_reason', TType.I32, 23)
            oprot.writeI32(self.deny_reason)
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




class Region_IDL(object):
    """
      Regions Parameters
    
      Attributes:
       - type
       - start_bit_id
       - region_length
      """

    thrift_spec = (None,
     (1,
      TType.I32,
      'type',
      None,
      None),
     (2,
      TType.I32,
      'start_bit_id',
      None,
      None),
     (3,
      TType.I32,
      'region_length',
      None,
      None))

    def __init__(self, type = None, start_bit_id = None, region_length = None):
        self.type = type
        self.start_bit_id = start_bit_id
        self.region_length = region_length



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
                    self.type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.start_bit_id = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.region_length = iprot.readI32()
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
        oprot.writeStructBegin('Region_IDL')
        if self.type != None:
            oprot.writeFieldBegin('type', TType.I32, 1)
            oprot.writeI32(self.type)
            oprot.writeFieldEnd()
        if self.start_bit_id != None:
            oprot.writeFieldBegin('start_bit_id', TType.I32, 2)
            oprot.writeI32(self.start_bit_id)
            oprot.writeFieldEnd()
        if self.region_length != None:
            oprot.writeFieldBegin('region_length', TType.I32, 3)
            oprot.writeI32(self.region_length)
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




class PropositionSummary_IDL(object):
    """
      PropositionSummary Parameters
    
      Attributes:
       - bitmap_length
       - total_count
       - subject_count
       - max_bit_id_used
       - last_resized_policy_version
       - last_renumbered_policy_version
       - regions
      """

    thrift_spec = (None,
     (1,
      TType.I32,
      'bitmap_length',
      None,
      None),
     (2,
      TType.I32,
      'total_count',
      None,
      None),
     (3,
      TType.I32,
      'subject_count',
      None,
      None),
     (4,
      TType.I32,
      'max_bit_id_used',
      None,
      None),
     (5,
      TType.I32,
      'last_resized_policy_version',
      None,
      None),
     (6,
      TType.I32,
      'last_renumbered_policy_version',
      None,
      None),
     (7,
      TType.LIST,
      'regions',
      (TType.STRUCT, (Region_IDL, Region_IDL.thrift_spec)),
      None))

    def __init__(self, bitmap_length = None, total_count = None, subject_count = None, max_bit_id_used = None, last_resized_policy_version = None, last_renumbered_policy_version = None, regions = None):
        self.bitmap_length = bitmap_length
        self.total_count = total_count
        self.subject_count = subject_count
        self.max_bit_id_used = max_bit_id_used
        self.last_resized_policy_version = last_resized_policy_version
        self.last_renumbered_policy_version = last_renumbered_policy_version
        self.regions = regions



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
                    self.bitmap_length = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.total_count = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.subject_count = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.max_bit_id_used = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.last_resized_policy_version = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I32:
                    self.last_renumbered_policy_version = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.LIST:
                    self.regions = []
                    (_etype10, _size7,) = iprot.readListBegin()
                    for _i11 in xrange(_size7):
                        _elem12 = Region_IDL()
                        _elem12.read(iprot)
                        self.regions.append(_elem12)

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
        oprot.writeStructBegin('PropositionSummary_IDL')
        if self.bitmap_length != None:
            oprot.writeFieldBegin('bitmap_length', TType.I32, 1)
            oprot.writeI32(self.bitmap_length)
            oprot.writeFieldEnd()
        if self.total_count != None:
            oprot.writeFieldBegin('total_count', TType.I32, 2)
            oprot.writeI32(self.total_count)
            oprot.writeFieldEnd()
        if self.subject_count != None:
            oprot.writeFieldBegin('subject_count', TType.I32, 3)
            oprot.writeI32(self.subject_count)
            oprot.writeFieldEnd()
        if self.max_bit_id_used != None:
            oprot.writeFieldBegin('max_bit_id_used', TType.I32, 4)
            oprot.writeI32(self.max_bit_id_used)
            oprot.writeFieldEnd()
        if self.last_resized_policy_version != None:
            oprot.writeFieldBegin('last_resized_policy_version', TType.I32, 5)
            oprot.writeI32(self.last_resized_policy_version)
            oprot.writeFieldEnd()
        if self.last_renumbered_policy_version != None:
            oprot.writeFieldBegin('last_renumbered_policy_version', TType.I32, 6)
            oprot.writeI32(self.last_renumbered_policy_version)
            oprot.writeFieldEnd()
        if self.regions != None:
            oprot.writeFieldBegin('regions', TType.LIST, 7)
            oprot.writeListBegin(TType.STRUCT, len(self.regions))
            for iter13 in self.regions:
                iter13.write(oprot)

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




class PropositionVector_IDL(object):
    """
      PropositionVector Parameters
    
      Attributes:
       - policy_version
       - summary
       - propositions
      """

    thrift_spec = (None,
     (1,
      TType.I64,
      'policy_version',
      None,
      None),
     (2,
      TType.STRUCT,
      'summary',
      (PropositionSummary_IDL, PropositionSummary_IDL.thrift_spec),
      None),
     (3,
      TType.LIST,
      'propositions',
      (TType.STRUCT, (Proposition_IDL, Proposition_IDL.thrift_spec)),
      None))

    def __init__(self, policy_version = None, summary = None, propositions = None):
        self.policy_version = policy_version
        self.summary = summary
        self.propositions = propositions



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
                    self.policy_version = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.summary = PropositionSummary_IDL()
                    self.summary.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.LIST:
                    self.propositions = []
                    (_etype17, _size14,) = iprot.readListBegin()
                    for _i18 in xrange(_size14):
                        _elem19 = Proposition_IDL()
                        _elem19.read(iprot)
                        self.propositions.append(_elem19)

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
        oprot.writeStructBegin('PropositionVector_IDL')
        if self.policy_version != None:
            oprot.writeFieldBegin('policy_version', TType.I64, 1)
            oprot.writeI64(self.policy_version)
            oprot.writeFieldEnd()
        if self.summary != None:
            oprot.writeFieldBegin('summary', TType.STRUCT, 2)
            self.summary.write(oprot)
            oprot.writeFieldEnd()
        if self.propositions != None:
            oprot.writeFieldBegin('propositions', TType.LIST, 3)
            oprot.writeListBegin(TType.STRUCT, len(self.propositions))
            for iter20 in self.propositions:
                iter20.write(oprot)

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




class AVCTypeToApp_IDL(object):
    """
      AVCTypeToApp Parameters
    
      Attributes:
       - type_id
       - app_id
      """

    thrift_spec = (None, (1,
      TType.I32,
      'type_id',
      None,
      None), (2,
      TType.LIST,
      'app_id',
      (TType.I32, None),
      None))

    def __init__(self, type_id = None, app_id = None):
        self.type_id = type_id
        self.app_id = app_id



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
                    self.type_id = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.app_id = []
                    (_etype24, _size21,) = iprot.readListBegin()
                    for _i25 in xrange(_size21):
                        _elem26 = iprot.readI32()
                        self.app_id.append(_elem26)

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
        oprot.writeStructBegin('AVCTypeToApp_IDL')
        if self.type_id != None:
            oprot.writeFieldBegin('type_id', TType.I32, 1)
            oprot.writeI32(self.type_id)
            oprot.writeFieldEnd()
        if self.app_id != None:
            oprot.writeFieldBegin('app_id', TType.LIST, 2)
            oprot.writeListBegin(TType.I32, len(self.app_id))
            for iter27 in self.app_id:
                oprot.writeI32(iter27)

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




class Run_IDL(object):
    """
      Run
      Used to define Run-Length-Encoded bit sequences.
    
      Attributes:
       - start
       - length
      """

    thrift_spec = (None, (1,
      TType.I32,
      'start',
      None,
      None), (2,
      TType.I32,
      'length',
      None,
      None))

    def __init__(self, start = None, length = None):
        self.start = start
        self.length = length



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
                    self.start = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.length = iprot.readI32()
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
        oprot.writeStructBegin('Run_IDL')
        if self.start != None:
            oprot.writeFieldBegin('start', TType.I32, 1)
            oprot.writeI32(self.start)
            oprot.writeFieldEnd()
        if self.length != None:
            oprot.writeFieldBegin('length', TType.I32, 2)
            oprot.writeI32(self.length)
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




class BitVector_IDL(object):
    """
      BitVector
    
    
      Attributes:
       - bitmap_length
       - bitmap
      """

    thrift_spec = (None, (1,
      TType.I32,
      'bitmap_length',
      None,
      None), (2,
      TType.LIST,
      'bitmap',
      (TType.STRUCT, (Run_IDL, Run_IDL.thrift_spec)),
      None))

    def __init__(self, bitmap_length = None, bitmap = None):
        self.bitmap_length = bitmap_length
        self.bitmap = bitmap



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
                    self.bitmap_length = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.bitmap = []
                    (_etype31, _size28,) = iprot.readListBegin()
                    for _i32 in xrange(_size28):
                        _elem33 = Run_IDL()
                        _elem33.read(iprot)
                        self.bitmap.append(_elem33)

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
        oprot.writeStructBegin('BitVector_IDL')
        if self.bitmap_length != None:
            oprot.writeFieldBegin('bitmap_length', TType.I32, 1)
            oprot.writeI32(self.bitmap_length)
            oprot.writeFieldEnd()
        if self.bitmap != None:
            oprot.writeFieldBegin('bitmap', TType.LIST, 2)
            oprot.writeListBegin(TType.STRUCT, len(self.bitmap))
            for iter34 in self.bitmap:
                iter34.write(oprot)

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




class AuthInfo_IDL(object):
    """
    Attributes:
     - scheme
     - ref_uid
     - ref_class_name
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'scheme',
      None,
      None),
     (2,
      TType.I32,
      'ref_uid',
      None,
      None),
     (3,
      TType.STRING,
      'ref_class_name',
      None,
      None))

    def __init__(self, scheme = None, ref_uid = None, ref_class_name = None):
        self.scheme = scheme
        self.ref_uid = ref_uid
        self.ref_class_name = ref_class_name



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
                    self.scheme = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.ref_uid = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.ref_class_name = iprot.readString()
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
        oprot.writeStructBegin('AuthInfo_IDL')
        if self.scheme != None:
            oprot.writeFieldBegin('scheme', TType.I32, 1)
            oprot.writeI32(self.scheme)
            oprot.writeFieldEnd()
        if self.ref_uid != None:
            oprot.writeFieldBegin('ref_uid', TType.I32, 2)
            oprot.writeI32(self.ref_uid)
            oprot.writeFieldEnd()
        if self.ref_class_name != None:
            oprot.writeFieldBegin('ref_class_name', TType.STRING, 3)
            oprot.writeString(self.ref_class_name)
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




class Row_IDL(object):
    """
      Row
    
    
      Attributes:
       - id
       - obligations
       - decision
       - true_items
       - false_items
       - leaf_table_id
       - auth_info
       - name
       - deny_reason
      """

    thrift_spec = (None,
     (1,
      TType.I32,
      'id',
      None,
      None),
     (2,
      TType.I32,
      'obligations',
      None,
      None),
     (3,
      TType.I32,
      'decision',
      None,
      None),
     (4,
      TType.STRUCT,
      'true_items',
      (BitVector_IDL, BitVector_IDL.thrift_spec),
      None),
     (5,
      TType.STRUCT,
      'false_items',
      (BitVector_IDL, BitVector_IDL.thrift_spec),
      None),
     (6,
      TType.I32,
      'leaf_table_id',
      None,
      None),
     (7,
      TType.STRUCT,
      'auth_info',
      (AuthInfo_IDL, AuthInfo_IDL.thrift_spec),
      None),
     (8,
      TType.STRING,
      'name',
      None,
      None),
     (9,
      TType.I32,
      'deny_reason',
      None,
      None))

    def __init__(self, id = None, obligations = None, decision = None, true_items = None, false_items = None, leaf_table_id = None, auth_info = None, name = None, deny_reason = None):
        self.id = id
        self.obligations = obligations
        self.decision = decision
        self.true_items = true_items
        self.false_items = false_items
        self.leaf_table_id = leaf_table_id
        self.auth_info = auth_info
        self.name = name
        self.deny_reason = deny_reason



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
                    self.id = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.obligations = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.decision = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRUCT:
                    self.true_items = BitVector_IDL()
                    self.true_items.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRUCT:
                    self.false_items = BitVector_IDL()
                    self.false_items.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I32:
                    self.leaf_table_id = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.STRUCT:
                    self.auth_info = AuthInfo_IDL()
                    self.auth_info.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.STRING:
                    self.name = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.I32:
                    self.deny_reason = iprot.readI32()
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
        oprot.writeStructBegin('Row_IDL')
        if self.id != None:
            oprot.writeFieldBegin('id', TType.I32, 1)
            oprot.writeI32(self.id)
            oprot.writeFieldEnd()
        if self.obligations != None:
            oprot.writeFieldBegin('obligations', TType.I32, 2)
            oprot.writeI32(self.obligations)
            oprot.writeFieldEnd()
        if self.decision != None:
            oprot.writeFieldBegin('decision', TType.I32, 3)
            oprot.writeI32(self.decision)
            oprot.writeFieldEnd()
        if self.true_items != None:
            oprot.writeFieldBegin('true_items', TType.STRUCT, 4)
            self.true_items.write(oprot)
            oprot.writeFieldEnd()
        if self.false_items != None:
            oprot.writeFieldBegin('false_items', TType.STRUCT, 5)
            self.false_items.write(oprot)
            oprot.writeFieldEnd()
        if self.leaf_table_id != None:
            oprot.writeFieldBegin('leaf_table_id', TType.I32, 6)
            oprot.writeI32(self.leaf_table_id)
            oprot.writeFieldEnd()
        if self.auth_info != None:
            oprot.writeFieldBegin('auth_info', TType.STRUCT, 7)
            self.auth_info.write(oprot)
            oprot.writeFieldEnd()
        if self.name != None:
            oprot.writeFieldBegin('name', TType.STRING, 8)
            oprot.writeString(self.name)
            oprot.writeFieldEnd()
        if self.deny_reason != None:
            oprot.writeFieldBegin('deny_reason', TType.I32, 9)
            oprot.writeI32(self.deny_reason)
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




class Table_IDL(object):
    """
      Table
    
    
      Attributes:
       - type
       - id
       - domain_id
       - name
       - policy_version
       - combining_alg
       - table_hierarchy
       - persist_id
       - deny_reason
       - tagref_bit_id
      """

    thrift_spec = (None,
     (1,
      TType.I32,
      'type',
      None,
      None),
     (2,
      TType.I32,
      'id',
      None,
      None),
     (3,
      TType.I32,
      'domain_id',
      None,
      None),
     (4,
      TType.STRING,
      'name',
      None,
      None),
     (5,
      TType.I64,
      'policy_version',
      None,
      None),
     (6,
      TType.I32,
      'combining_alg',
      None,
      None),
     (7,
      TType.I32,
      'table_hierarchy',
      None,
      None),
     (8,
      TType.I64,
      'persist_id',
      None,
      None),
     (9,
      TType.I32,
      'deny_reason',
      None,
      None),
     (10,
      TType.I32,
      'tagref_bit_id',
      None,
      None))

    def __init__(self, type = None, id = None, domain_id = None, name = None, policy_version = None, combining_alg = None, table_hierarchy = None, persist_id = None, deny_reason = None, tagref_bit_id = None):
        self.type = type
        self.id = id
        self.domain_id = domain_id
        self.name = name
        self.policy_version = policy_version
        self.combining_alg = combining_alg
        self.table_hierarchy = table_hierarchy
        self.persist_id = persist_id
        self.deny_reason = deny_reason
        self.tagref_bit_id = tagref_bit_id



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
                    self.type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.id = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.domain_id = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.name = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I64:
                    self.policy_version = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I32:
                    self.combining_alg = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I32:
                    self.table_hierarchy = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.I64:
                    self.persist_id = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.I32:
                    self.deny_reason = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.I32:
                    self.tagref_bit_id = iprot.readI32()
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
        oprot.writeStructBegin('Table_IDL')
        if self.type != None:
            oprot.writeFieldBegin('type', TType.I32, 1)
            oprot.writeI32(self.type)
            oprot.writeFieldEnd()
        if self.id != None:
            oprot.writeFieldBegin('id', TType.I32, 2)
            oprot.writeI32(self.id)
            oprot.writeFieldEnd()
        if self.domain_id != None:
            oprot.writeFieldBegin('domain_id', TType.I32, 3)
            oprot.writeI32(self.domain_id)
            oprot.writeFieldEnd()
        if self.name != None:
            oprot.writeFieldBegin('name', TType.STRING, 4)
            oprot.writeString(self.name)
            oprot.writeFieldEnd()
        if self.policy_version != None:
            oprot.writeFieldBegin('policy_version', TType.I64, 5)
            oprot.writeI64(self.policy_version)
            oprot.writeFieldEnd()
        if self.combining_alg != None:
            oprot.writeFieldBegin('combining_alg', TType.I32, 6)
            oprot.writeI32(self.combining_alg)
            oprot.writeFieldEnd()
        if self.table_hierarchy != None:
            oprot.writeFieldBegin('table_hierarchy', TType.I32, 7)
            oprot.writeI32(self.table_hierarchy)
            oprot.writeFieldEnd()
        if self.persist_id != None:
            oprot.writeFieldBegin('persist_id', TType.I64, 8)
            oprot.writeI64(self.persist_id)
            oprot.writeFieldEnd()
        if self.deny_reason != None:
            oprot.writeFieldBegin('deny_reason', TType.I32, 9)
            oprot.writeI32(self.deny_reason)
            oprot.writeFieldEnd()
        if self.tagref_bit_id != None:
            oprot.writeFieldBegin('tagref_bit_id', TType.I32, 10)
            oprot.writeI32(self.tagref_bit_id)
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




class Channel_IDL(object):
    """
      Channel Parameters
    
      Attributes:
       - src_addr
       - dst_addr
       - src_port
       - dst_port
       - table_id
      """

    thrift_spec = (None,
     (1,
      TType.STRUCT,
      'src_addr',
      (Shared.ttypes.NetworkAddressIDL, Shared.ttypes.NetworkAddressIDL.thrift_spec),
      None),
     (2,
      TType.STRUCT,
      'dst_addr',
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
      TType.I32,
      'table_id',
      None,
      None))

    def __init__(self, src_addr = None, dst_addr = None, src_port = None, dst_port = None, table_id = None):
        self.src_addr = src_addr
        self.dst_addr = dst_addr
        self.src_port = src_port
        self.dst_port = dst_port
        self.table_id = table_id



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
                    self.src_addr = Shared.ttypes.NetworkAddressIDL()
                    self.src_addr.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.dst_addr = Shared.ttypes.NetworkAddressIDL()
                    self.dst_addr.read(iprot)
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
                if ftype == TType.I32:
                    self.table_id = iprot.readI32()
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
        oprot.writeStructBegin('Channel_IDL')
        if self.src_addr != None:
            oprot.writeFieldBegin('src_addr', TType.STRUCT, 1)
            self.src_addr.write(oprot)
            oprot.writeFieldEnd()
        if self.dst_addr != None:
            oprot.writeFieldBegin('dst_addr', TType.STRUCT, 2)
            self.dst_addr.write(oprot)
            oprot.writeFieldEnd()
        if self.src_port != None:
            oprot.writeFieldBegin('src_port', TType.I16, 3)
            oprot.writeI16(self.src_port)
            oprot.writeFieldEnd()
        if self.dst_port != None:
            oprot.writeFieldBegin('dst_port', TType.I16, 4)
            oprot.writeI16(self.dst_port)
            oprot.writeFieldEnd()
        if self.table_id != None:
            oprot.writeFieldBegin('table_id', TType.I32, 5)
            oprot.writeI32(self.table_id)
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




class FlowRule_IDL(object):
    """
      Flow Rule
    
      Attributes:
       - domain_id
       - request_id
       - faddr
       - faddr2
       - fprefixlen
       - laddr
       - laddr2
       - lprefixlen
       - fport
       - fport2
       - lport
       - lport2
       - protocol
       - flags
       - flow_side
       - match_options
      """

    thrift_spec = (None,
     (1,
      TType.I32,
      'domain_id',
      None,
      None),
     (2,
      TType.I32,
      'request_id',
      None,
      None),
     (3,
      TType.STRUCT,
      'faddr',
      (Shared.ttypes.NetworkAddressIDL, Shared.ttypes.NetworkAddressIDL.thrift_spec),
      None),
     (4,
      TType.STRUCT,
      'faddr2',
      (Shared.ttypes.NetworkAddressIDL, Shared.ttypes.NetworkAddressIDL.thrift_spec),
      None),
     (5,
      TType.I32,
      'fprefixlen',
      None,
      None),
     (6,
      TType.STRUCT,
      'laddr',
      (Shared.ttypes.NetworkAddressIDL, Shared.ttypes.NetworkAddressIDL.thrift_spec),
      None),
     (7,
      TType.STRUCT,
      'laddr2',
      (Shared.ttypes.NetworkAddressIDL, Shared.ttypes.NetworkAddressIDL.thrift_spec),
      None),
     (8,
      TType.I32,
      'lprefixlen',
      None,
      None),
     (9,
      TType.I32,
      'fport',
      None,
      None),
     (10,
      TType.I32,
      'fport2',
      None,
      None),
     (11,
      TType.I32,
      'lport',
      None,
      None),
     (12,
      TType.I32,
      'lport2',
      None,
      None),
     (13,
      TType.I32,
      'protocol',
      None,
      None),
     (14,
      TType.I32,
      'flags',
      None,
      None),
     (15,
      TType.I32,
      'flow_side',
      None,
      None),
     (16,
      TType.I32,
      'match_options',
      None,
      None))

    def __init__(self, domain_id = None, request_id = None, faddr = None, faddr2 = None, fprefixlen = None, laddr = None, laddr2 = None, lprefixlen = None, fport = None, fport2 = None, lport = None, lport2 = None, protocol = None, flags = None, flow_side = None, match_options = None):
        self.domain_id = domain_id
        self.request_id = request_id
        self.faddr = faddr
        self.faddr2 = faddr2
        self.fprefixlen = fprefixlen
        self.laddr = laddr
        self.laddr2 = laddr2
        self.lprefixlen = lprefixlen
        self.fport = fport
        self.fport2 = fport2
        self.lport = lport
        self.lport2 = lport2
        self.protocol = protocol
        self.flags = flags
        self.flow_side = flow_side
        self.match_options = match_options



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
                    self.domain_id = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.request_id = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRUCT:
                    self.faddr = Shared.ttypes.NetworkAddressIDL()
                    self.faddr.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRUCT:
                    self.faddr2 = Shared.ttypes.NetworkAddressIDL()
                    self.faddr2.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.fprefixlen = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRUCT:
                    self.laddr = Shared.ttypes.NetworkAddressIDL()
                    self.laddr.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.STRUCT:
                    self.laddr2 = Shared.ttypes.NetworkAddressIDL()
                    self.laddr2.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.I32:
                    self.lprefixlen = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.I32:
                    self.fport = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.I32:
                    self.fport2 = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.I32:
                    self.lport = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 12:
                if ftype == TType.I32:
                    self.lport2 = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 13:
                if ftype == TType.I32:
                    self.protocol = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 14:
                if ftype == TType.I32:
                    self.flags = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 15:
                if ftype == TType.I32:
                    self.flow_side = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 16:
                if ftype == TType.I32:
                    self.match_options = iprot.readI32()
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
        oprot.writeStructBegin('FlowRule_IDL')
        if self.domain_id != None:
            oprot.writeFieldBegin('domain_id', TType.I32, 1)
            oprot.writeI32(self.domain_id)
            oprot.writeFieldEnd()
        if self.request_id != None:
            oprot.writeFieldBegin('request_id', TType.I32, 2)
            oprot.writeI32(self.request_id)
            oprot.writeFieldEnd()
        if self.faddr != None:
            oprot.writeFieldBegin('faddr', TType.STRUCT, 3)
            self.faddr.write(oprot)
            oprot.writeFieldEnd()
        if self.faddr2 != None:
            oprot.writeFieldBegin('faddr2', TType.STRUCT, 4)
            self.faddr2.write(oprot)
            oprot.writeFieldEnd()
        if self.fprefixlen != None:
            oprot.writeFieldBegin('fprefixlen', TType.I32, 5)
            oprot.writeI32(self.fprefixlen)
            oprot.writeFieldEnd()
        if self.laddr != None:
            oprot.writeFieldBegin('laddr', TType.STRUCT, 6)
            self.laddr.write(oprot)
            oprot.writeFieldEnd()
        if self.laddr2 != None:
            oprot.writeFieldBegin('laddr2', TType.STRUCT, 7)
            self.laddr2.write(oprot)
            oprot.writeFieldEnd()
        if self.lprefixlen != None:
            oprot.writeFieldBegin('lprefixlen', TType.I32, 8)
            oprot.writeI32(self.lprefixlen)
            oprot.writeFieldEnd()
        if self.fport != None:
            oprot.writeFieldBegin('fport', TType.I32, 9)
            oprot.writeI32(self.fport)
            oprot.writeFieldEnd()
        if self.fport2 != None:
            oprot.writeFieldBegin('fport2', TType.I32, 10)
            oprot.writeI32(self.fport2)
            oprot.writeFieldEnd()
        if self.lport != None:
            oprot.writeFieldBegin('lport', TType.I32, 11)
            oprot.writeI32(self.lport)
            oprot.writeFieldEnd()
        if self.lport2 != None:
            oprot.writeFieldBegin('lport2', TType.I32, 12)
            oprot.writeI32(self.lport2)
            oprot.writeFieldEnd()
        if self.protocol != None:
            oprot.writeFieldBegin('protocol', TType.I32, 13)
            oprot.writeI32(self.protocol)
            oprot.writeFieldEnd()
        if self.flags != None:
            oprot.writeFieldBegin('flags', TType.I32, 14)
            oprot.writeI32(self.flags)
            oprot.writeFieldEnd()
        if self.flow_side != None:
            oprot.writeFieldBegin('flow_side', TType.I32, 15)
            oprot.writeI32(self.flow_side)
            oprot.writeFieldEnd()
        if self.match_options != None:
            oprot.writeFieldBegin('match_options', TType.I32, 16)
            oprot.writeI32(self.match_options)
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




class Capability_IDL(object):
    """
      Capability Structure
    
      Attributes:
       - capability_class
       - capability_type
       - capability_value
      """

    thrift_spec = (None,
     (1,
      TType.I32,
      'capability_class',
      None,
      None),
     (2,
      TType.I32,
      'capability_type',
      None,
      None),
     (3,
      TType.I32,
      'capability_value',
      None,
      None))

    def __init__(self, capability_class = None, capability_type = None, capability_value = None):
        self.capability_class = capability_class
        self.capability_type = capability_type
        self.capability_value = capability_value



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
                    self.capability_class = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.capability_type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.capability_value = iprot.readI32()
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
        oprot.writeStructBegin('Capability_IDL')
        if self.capability_class != None:
            oprot.writeFieldBegin('capability_class', TType.I32, 1)
            oprot.writeI32(self.capability_class)
            oprot.writeFieldEnd()
        if self.capability_type != None:
            oprot.writeFieldBegin('capability_type', TType.I32, 2)
            oprot.writeI32(self.capability_type)
            oprot.writeFieldEnd()
        if self.capability_value != None:
            oprot.writeFieldBegin('capability_value', TType.I32, 3)
            oprot.writeI32(self.capability_value)
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




class CapabilityList_IDL(object):
    """
      Capability List
    
      Attributes:
       - capList
      """

    thrift_spec = (None, (1,
      TType.LIST,
      'capList',
      (TType.STRUCT, (Capability_IDL, Capability_IDL.thrift_spec)),
      None))

    def __init__(self, capList = None):
        self.capList = capList



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
                if ftype == TType.LIST:
                    self.capList = []
                    (_etype38, _size35,) = iprot.readListBegin()
                    for _i39 in xrange(_size35):
                        _elem40 = Capability_IDL()
                        _elem40.read(iprot)
                        self.capList.append(_elem40)

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
        oprot.writeStructBegin('CapabilityList_IDL')
        if self.capList != None:
            oprot.writeFieldBegin('capList', TType.LIST, 1)
            oprot.writeListBegin(TType.STRUCT, len(self.capList))
            for iter41 in self.capList:
                iter41.write(oprot)

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




class interfaceRoleMap_IDL(object):
    """
      Interface Role Map
    
      Attributes:
       - xosHandle
       - action
       - role_count
       - roles
      """

    thrift_spec = (None,
     (1,
      TType.I64,
      'xosHandle',
      None,
      None),
     (2,
      TType.BYTE,
      'action',
      None,
      None),
     (3,
      TType.I32,
      'role_count',
      None,
      None),
     (4,
      TType.LIST,
      'roles',
      (TType.I64, None),
      None))

    def __init__(self, xosHandle = None, action = None, role_count = None, roles = None):
        self.xosHandle = xosHandle
        self.action = action
        self.role_count = role_count
        self.roles = roles



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
                    self.xosHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.BYTE:
                    self.action = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.role_count = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.LIST:
                    self.roles = []
                    (_etype45, _size42,) = iprot.readListBegin()
                    for _i46 in xrange(_size42):
                        _elem47 = iprot.readI64()
                        self.roles.append(_elem47)

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
        oprot.writeStructBegin('interfaceRoleMap_IDL')
        if self.xosHandle != None:
            oprot.writeFieldBegin('xosHandle', TType.I64, 1)
            oprot.writeI64(self.xosHandle)
            oprot.writeFieldEnd()
        if self.action != None:
            oprot.writeFieldBegin('action', TType.BYTE, 2)
            oprot.writeByte(self.action)
            oprot.writeFieldEnd()
        if self.role_count != None:
            oprot.writeFieldBegin('role_count', TType.I32, 3)
            oprot.writeI32(self.role_count)
            oprot.writeFieldEnd()
        if self.roles != None:
            oprot.writeFieldBegin('roles', TType.LIST, 4)
            oprot.writeListBegin(TType.I64, len(self.roles))
            for iter48 in self.roles:
                oprot.writeI64(iter48)

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




class NbarProtocolPack_IDL(object):
    """
      NBAR Protocol Pack
    
      Attributes:
       - file_pathname
      """

    thrift_spec = (None, (1,
      TType.STRING,
      'file_pathname',
      None,
      None))

    def __init__(self, file_pathname = None):
        self.file_pathname = file_pathname



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
                    self.file_pathname = iprot.readString()
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
        oprot.writeStructBegin('NbarProtocolPack_IDL')
        if self.file_pathname != None:
            oprot.writeFieldBegin('file_pathname', TType.STRING, 1)
            oprot.writeString(self.file_pathname)
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




class avcObj_IDL(object):
    """
      AVC Object
    
      Attributes:
       - name
       - unified_id
       - display_name
       - nbar_id
      """

    thrift_spec = (None,
     (1,
      TType.STRING,
      'name',
      None,
      None),
     (2,
      TType.I32,
      'unified_id',
      None,
      None),
     (3,
      TType.STRING,
      'display_name',
      None,
      None),
     (4,
      TType.I32,
      'nbar_id',
      None,
      None))

    def __init__(self, name = None, unified_id = None, display_name = None, nbar_id = None):
        self.name = name
        self.unified_id = unified_id
        self.display_name = display_name
        self.nbar_id = nbar_id



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
                    self.name = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.unified_id = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.display_name = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.nbar_id = iprot.readI32()
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
        oprot.writeStructBegin('avcObj_IDL')
        if self.name != None:
            oprot.writeFieldBegin('name', TType.STRING, 1)
            oprot.writeString(self.name)
            oprot.writeFieldEnd()
        if self.unified_id != None:
            oprot.writeFieldBegin('unified_id', TType.I32, 2)
            oprot.writeI32(self.unified_id)
            oprot.writeFieldEnd()
        if self.display_name != None:
            oprot.writeFieldBegin('display_name', TType.STRING, 3)
            oprot.writeString(self.display_name)
            oprot.writeFieldEnd()
        if self.nbar_id != None:
            oprot.writeFieldBegin('nbar_id', TType.I32, 4)
            oprot.writeI32(self.nbar_id)
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




class avcGroupObj_IDL(object):
    """
      AVC Group Object
    
      Attributes:
       - type_id
       - app_id_count
       - app_ids
      """

    thrift_spec = (None,
     (1,
      TType.I32,
      'type_id',
      None,
      None),
     (2,
      TType.I32,
      'app_id_count',
      None,
      None),
     (3,
      TType.LIST,
      'app_ids',
      (TType.I32, None),
      None))

    def __init__(self, type_id = None, app_id_count = None, app_ids = None):
        self.type_id = type_id
        self.app_id_count = app_id_count
        self.app_ids = app_ids



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
                    self.type_id = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.app_id_count = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.LIST:
                    self.app_ids = []
                    (_etype52, _size49,) = iprot.readListBegin()
                    for _i53 in xrange(_size49):
                        _elem54 = iprot.readI32()
                        self.app_ids.append(_elem54)

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
        oprot.writeStructBegin('avcGroupObj_IDL')
        if self.type_id != None:
            oprot.writeFieldBegin('type_id', TType.I32, 1)
            oprot.writeI32(self.type_id)
            oprot.writeFieldEnd()
        if self.app_id_count != None:
            oprot.writeFieldBegin('app_id_count', TType.I32, 2)
            oprot.writeI32(self.app_id_count)
            oprot.writeFieldEnd()
        if self.app_ids != None:
            oprot.writeFieldBegin('app_ids', TType.LIST, 3)
            oprot.writeListBegin(TType.I32, len(self.app_ids))
            for iter55 in self.app_ids:
                oprot.writeI32(iter55)

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
# 2015.02.05 17:19:17 IST
