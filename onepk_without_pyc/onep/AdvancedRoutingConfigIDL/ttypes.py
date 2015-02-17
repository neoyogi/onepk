# 2015.02.05 17:20:39 IST
from thrift.Thrift import *
import Shared.ttypes
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
    from thrift.protocol import fastbinary
except:
    fastbinary = None

class RouterConfigAGGIDL(object):
    """
    Attributes:
     - object_uid
     - prefix
     - as_set
     - summary_only
     - suppress_policy_name
     - advertise_policy_name
     - attribute_policy_name
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'object_uid',
      None,
      None),
     (2,
      TType.STRUCT,
      'prefix',
      (Shared.ttypes.NetworkPrefixIDL, Shared.ttypes.NetworkPrefixIDL.thrift_spec),
      None),
     (3,
      TType.I32,
      'as_set',
      None,
      None),
     (4,
      TType.I32,
      'summary_only',
      None,
      None),
     (5,
      TType.STRING,
      'suppress_policy_name',
      None,
      None),
     (6,
      TType.STRING,
      'advertise_policy_name',
      None,
      None),
     (7,
      TType.STRING,
      'attribute_policy_name',
      None,
      None))

    def __init__(self, object_uid = None, prefix = None, as_set = None, summary_only = None, suppress_policy_name = None, advertise_policy_name = None, attribute_policy_name = None):
        self.object_uid = object_uid
        self.prefix = prefix
        self.as_set = as_set
        self.summary_only = summary_only
        self.suppress_policy_name = suppress_policy_name
        self.advertise_policy_name = advertise_policy_name
        self.attribute_policy_name = attribute_policy_name



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
                    self.object_uid = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.prefix = Shared.ttypes.NetworkPrefixIDL()
                    self.prefix.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.as_set = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.summary_only = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.suppress_policy_name = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRING:
                    self.advertise_policy_name = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.STRING:
                    self.attribute_policy_name = iprot.readString()
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
        oprot.writeStructBegin('RouterConfigAGGIDL')
        if self.object_uid != None:
            oprot.writeFieldBegin('object_uid', TType.I32, 1)
            oprot.writeI32(self.object_uid)
            oprot.writeFieldEnd()
        if self.prefix != None:
            oprot.writeFieldBegin('prefix', TType.STRUCT, 2)
            self.prefix.write(oprot)
            oprot.writeFieldEnd()
        if self.as_set != None:
            oprot.writeFieldBegin('as_set', TType.I32, 3)
            oprot.writeI32(self.as_set)
            oprot.writeFieldEnd()
        if self.summary_only != None:
            oprot.writeFieldBegin('summary_only', TType.I32, 4)
            oprot.writeI32(self.summary_only)
            oprot.writeFieldEnd()
        if self.suppress_policy_name != None:
            oprot.writeFieldBegin('suppress_policy_name', TType.STRING, 5)
            oprot.writeString(self.suppress_policy_name)
            oprot.writeFieldEnd()
        if self.advertise_policy_name != None:
            oprot.writeFieldBegin('advertise_policy_name', TType.STRING, 6)
            oprot.writeString(self.advertise_policy_name)
            oprot.writeFieldEnd()
        if self.attribute_policy_name != None:
            oprot.writeFieldBegin('attribute_policy_name', TType.STRING, 7)
            oprot.writeString(self.attribute_policy_name)
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




class RouterConfigNETIDL(object):
    """
    Attributes:
     - object_uid
     - prefix
     - policy_name
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'object_uid',
      None,
      None),
     (2,
      TType.STRUCT,
      'prefix',
      (Shared.ttypes.NetworkPrefixIDL, Shared.ttypes.NetworkPrefixIDL.thrift_spec),
      None),
     (3,
      TType.STRING,
      'policy_name',
      None,
      None))

    def __init__(self, object_uid = None, prefix = None, policy_name = None):
        self.object_uid = object_uid
        self.prefix = prefix
        self.policy_name = policy_name



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
                    self.object_uid = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.prefix = Shared.ttypes.NetworkPrefixIDL()
                    self.prefix.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.policy_name = iprot.readString()
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
        oprot.writeStructBegin('RouterConfigNETIDL')
        if self.object_uid != None:
            oprot.writeFieldBegin('object_uid', TType.I32, 1)
            oprot.writeI32(self.object_uid)
            oprot.writeFieldEnd()
        if self.prefix != None:
            oprot.writeFieldBegin('prefix', TType.STRUCT, 2)
            self.prefix.write(oprot)
            oprot.writeFieldEnd()
        if self.policy_name != None:
            oprot.writeFieldBegin('policy_name', TType.STRING, 3)
            oprot.writeString(self.policy_name)
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




class RouterConfigNBRAFIDL(object):
    """
    Attributes:
     - object_uid
     - afi
     - safi
     - inbound_policy_name
     - outbound_policy_name
     - peer_policy_template_name
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'object_uid',
      None,
      None),
     (2,
      TType.I32,
      'afi',
      None,
      None),
     (3,
      TType.I32,
      'safi',
      None,
      None),
     (4,
      TType.STRING,
      'inbound_policy_name',
      None,
      None),
     (5,
      TType.STRING,
      'outbound_policy_name',
      None,
      None),
     (6,
      TType.STRING,
      'peer_policy_template_name',
      None,
      None))

    def __init__(self, object_uid = None, afi = None, safi = None, inbound_policy_name = None, outbound_policy_name = None, peer_policy_template_name = None):
        self.object_uid = object_uid
        self.afi = afi
        self.safi = safi
        self.inbound_policy_name = inbound_policy_name
        self.outbound_policy_name = outbound_policy_name
        self.peer_policy_template_name = peer_policy_template_name



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
                    self.object_uid = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.afi = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.safi = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.inbound_policy_name = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.outbound_policy_name = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRING:
                    self.peer_policy_template_name = iprot.readString()
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
        oprot.writeStructBegin('RouterConfigNBRAFIDL')
        if self.object_uid != None:
            oprot.writeFieldBegin('object_uid', TType.I32, 1)
            oprot.writeI32(self.object_uid)
            oprot.writeFieldEnd()
        if self.afi != None:
            oprot.writeFieldBegin('afi', TType.I32, 2)
            oprot.writeI32(self.afi)
            oprot.writeFieldEnd()
        if self.safi != None:
            oprot.writeFieldBegin('safi', TType.I32, 3)
            oprot.writeI32(self.safi)
            oprot.writeFieldEnd()
        if self.inbound_policy_name != None:
            oprot.writeFieldBegin('inbound_policy_name', TType.STRING, 4)
            oprot.writeString(self.inbound_policy_name)
            oprot.writeFieldEnd()
        if self.outbound_policy_name != None:
            oprot.writeFieldBegin('outbound_policy_name', TType.STRING, 5)
            oprot.writeString(self.outbound_policy_name)
            oprot.writeFieldEnd()
        if self.peer_policy_template_name != None:
            oprot.writeFieldBegin('peer_policy_template_name', TType.STRING, 6)
            oprot.writeString(self.peer_policy_template_name)
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




class RouterConfigNBRIDL(object):
    """
    Attributes:
     - object_uid
     - address
     - remote_as
     - keepalive_time
     - hold_time
     - update_source_xos_if_handle
     - peer_session_template_name
     - peer_template_name
     - af_list
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'object_uid',
      None,
      None),
     (2,
      TType.STRUCT,
      'address',
      (Shared.ttypes.NetworkAddressIDL, Shared.ttypes.NetworkAddressIDL.thrift_spec),
      None),
     (3,
      TType.I32,
      'remote_as',
      None,
      None),
     (4,
      TType.I32,
      'keepalive_time',
      None,
      None),
     (5,
      TType.I32,
      'hold_time',
      None,
      None),
     (6,
      TType.I64,
      'update_source_xos_if_handle',
      None,
      None),
     (7,
      TType.STRING,
      'peer_session_template_name',
      None,
      None),
     (8,
      TType.STRING,
      'peer_template_name',
      None,
      None),
     (9,
      TType.LIST,
      'af_list',
      (TType.STRUCT, (RouterConfigNBRAFIDL, RouterConfigNBRAFIDL.thrift_spec)),
      None))

    def __init__(self, object_uid = None, address = None, remote_as = None, keepalive_time = None, hold_time = None, update_source_xos_if_handle = None, peer_session_template_name = None, peer_template_name = None, af_list = None):
        self.object_uid = object_uid
        self.address = address
        self.remote_as = remote_as
        self.keepalive_time = keepalive_time
        self.hold_time = hold_time
        self.update_source_xos_if_handle = update_source_xos_if_handle
        self.peer_session_template_name = peer_session_template_name
        self.peer_template_name = peer_template_name
        self.af_list = af_list



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
                    self.object_uid = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.address = Shared.ttypes.NetworkAddressIDL()
                    self.address.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.remote_as = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.keepalive_time = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.hold_time = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I64:
                    self.update_source_xos_if_handle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.STRING:
                    self.peer_session_template_name = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.STRING:
                    self.peer_template_name = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.LIST:
                    self.af_list = []
                    (_etype3, _size0,) = iprot.readListBegin()
                    for _i4 in xrange(_size0):
                        _elem5 = RouterConfigNBRAFIDL()
                        _elem5.read(iprot)
                        self.af_list.append(_elem5)

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
        oprot.writeStructBegin('RouterConfigNBRIDL')
        if self.object_uid != None:
            oprot.writeFieldBegin('object_uid', TType.I32, 1)
            oprot.writeI32(self.object_uid)
            oprot.writeFieldEnd()
        if self.address != None:
            oprot.writeFieldBegin('address', TType.STRUCT, 2)
            self.address.write(oprot)
            oprot.writeFieldEnd()
        if self.remote_as != None:
            oprot.writeFieldBegin('remote_as', TType.I32, 3)
            oprot.writeI32(self.remote_as)
            oprot.writeFieldEnd()
        if self.keepalive_time != None:
            oprot.writeFieldBegin('keepalive_time', TType.I32, 4)
            oprot.writeI32(self.keepalive_time)
            oprot.writeFieldEnd()
        if self.hold_time != None:
            oprot.writeFieldBegin('hold_time', TType.I32, 5)
            oprot.writeI32(self.hold_time)
            oprot.writeFieldEnd()
        if self.update_source_xos_if_handle != None:
            oprot.writeFieldBegin('update_source_xos_if_handle', TType.I64, 6)
            oprot.writeI64(self.update_source_xos_if_handle)
            oprot.writeFieldEnd()
        if self.peer_session_template_name != None:
            oprot.writeFieldBegin('peer_session_template_name', TType.STRING, 7)
            oprot.writeString(self.peer_session_template_name)
            oprot.writeFieldEnd()
        if self.peer_template_name != None:
            oprot.writeFieldBegin('peer_template_name', TType.STRING, 8)
            oprot.writeString(self.peer_template_name)
            oprot.writeFieldEnd()
        if self.af_list != None:
            oprot.writeFieldBegin('af_list', TType.LIST, 9)
            oprot.writeListBegin(TType.STRUCT, len(self.af_list))
            for iter6 in self.af_list:
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




class RouterConfigAFIDL(object):
    """
    Attributes:
     - object_uid
     - afi
     - safi
     - max_paths_ibgp
     - max_paths_ebgp
     - max_paths_eibgp
     - net_list
     - agg_list
     - nbr_list
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'object_uid',
      None,
      None),
     (2,
      TType.I32,
      'afi',
      None,
      None),
     (3,
      TType.I32,
      'safi',
      None,
      None),
     (4,
      TType.I32,
      'max_paths_ibgp',
      None,
      None),
     (5,
      TType.I32,
      'max_paths_ebgp',
      None,
      None),
     (6,
      TType.I32,
      'max_paths_eibgp',
      None,
      None),
     (7,
      TType.LIST,
      'net_list',
      (TType.STRUCT, (RouterConfigNETIDL, RouterConfigNETIDL.thrift_spec)),
      None),
     (8,
      TType.LIST,
      'agg_list',
      (TType.STRUCT, (RouterConfigAGGIDL, RouterConfigAGGIDL.thrift_spec)),
      None),
     (9,
      TType.LIST,
      'nbr_list',
      (TType.STRUCT, (RouterConfigNBRIDL, RouterConfigNBRIDL.thrift_spec)),
      None))

    def __init__(self, object_uid = None, afi = None, safi = None, max_paths_ibgp = None, max_paths_ebgp = None, max_paths_eibgp = None, net_list = None, agg_list = None, nbr_list = None):
        self.object_uid = object_uid
        self.afi = afi
        self.safi = safi
        self.max_paths_ibgp = max_paths_ibgp
        self.max_paths_ebgp = max_paths_ebgp
        self.max_paths_eibgp = max_paths_eibgp
        self.net_list = net_list
        self.agg_list = agg_list
        self.nbr_list = nbr_list



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
                    self.object_uid = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.afi = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.safi = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.max_paths_ibgp = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.max_paths_ebgp = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I32:
                    self.max_paths_eibgp = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.LIST:
                    self.net_list = []
                    (_etype10, _size7,) = iprot.readListBegin()
                    for _i11 in xrange(_size7):
                        _elem12 = RouterConfigNETIDL()
                        _elem12.read(iprot)
                        self.net_list.append(_elem12)

                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.LIST:
                    self.agg_list = []
                    (_etype16, _size13,) = iprot.readListBegin()
                    for _i17 in xrange(_size13):
                        _elem18 = RouterConfigAGGIDL()
                        _elem18.read(iprot)
                        self.agg_list.append(_elem18)

                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.LIST:
                    self.nbr_list = []
                    (_etype22, _size19,) = iprot.readListBegin()
                    for _i23 in xrange(_size19):
                        _elem24 = RouterConfigNBRIDL()
                        _elem24.read(iprot)
                        self.nbr_list.append(_elem24)

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
        oprot.writeStructBegin('RouterConfigAFIDL')
        if self.object_uid != None:
            oprot.writeFieldBegin('object_uid', TType.I32, 1)
            oprot.writeI32(self.object_uid)
            oprot.writeFieldEnd()
        if self.afi != None:
            oprot.writeFieldBegin('afi', TType.I32, 2)
            oprot.writeI32(self.afi)
            oprot.writeFieldEnd()
        if self.safi != None:
            oprot.writeFieldBegin('safi', TType.I32, 3)
            oprot.writeI32(self.safi)
            oprot.writeFieldEnd()
        if self.max_paths_ibgp != None:
            oprot.writeFieldBegin('max_paths_ibgp', TType.I32, 4)
            oprot.writeI32(self.max_paths_ibgp)
            oprot.writeFieldEnd()
        if self.max_paths_ebgp != None:
            oprot.writeFieldBegin('max_paths_ebgp', TType.I32, 5)
            oprot.writeI32(self.max_paths_ebgp)
            oprot.writeFieldEnd()
        if self.max_paths_eibgp != None:
            oprot.writeFieldBegin('max_paths_eibgp', TType.I32, 6)
            oprot.writeI32(self.max_paths_eibgp)
            oprot.writeFieldEnd()
        if self.net_list != None:
            oprot.writeFieldBegin('net_list', TType.LIST, 7)
            oprot.writeListBegin(TType.STRUCT, len(self.net_list))
            for iter25 in self.net_list:
                iter25.write(oprot)

            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.agg_list != None:
            oprot.writeFieldBegin('agg_list', TType.LIST, 8)
            oprot.writeListBegin(TType.STRUCT, len(self.agg_list))
            for iter26 in self.agg_list:
                iter26.write(oprot)

            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.nbr_list != None:
            oprot.writeFieldBegin('nbr_list', TType.LIST, 9)
            oprot.writeListBegin(TType.STRUCT, len(self.nbr_list))
            for iter27 in self.nbr_list:
                iter27.write(oprot)

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




class RouterConfigVRFIDL(object):
    """
    Attributes:
     - object_uid
     - vrf_name
     - router_id
     - af_list
     - nbr_list
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'object_uid',
      None,
      None),
     (2,
      TType.STRING,
      'vrf_name',
      None,
      None),
     (3,
      TType.I32,
      'router_id',
      None,
      None),
     (4,
      TType.LIST,
      'af_list',
      (TType.STRUCT, (RouterConfigAFIDL, RouterConfigAFIDL.thrift_spec)),
      None),
     (5,
      TType.LIST,
      'nbr_list',
      (TType.STRUCT, (RouterConfigNBRIDL, RouterConfigNBRIDL.thrift_spec)),
      None))

    def __init__(self, object_uid = None, vrf_name = None, router_id = None, af_list = None, nbr_list = None):
        self.object_uid = object_uid
        self.vrf_name = vrf_name
        self.router_id = router_id
        self.af_list = af_list
        self.nbr_list = nbr_list



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
                    self.object_uid = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.vrf_name = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.router_id = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.LIST:
                    self.af_list = []
                    (_etype31, _size28,) = iprot.readListBegin()
                    for _i32 in xrange(_size28):
                        _elem33 = RouterConfigAFIDL()
                        _elem33.read(iprot)
                        self.af_list.append(_elem33)

                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.LIST:
                    self.nbr_list = []
                    (_etype37, _size34,) = iprot.readListBegin()
                    for _i38 in xrange(_size34):
                        _elem39 = RouterConfigNBRIDL()
                        _elem39.read(iprot)
                        self.nbr_list.append(_elem39)

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
        oprot.writeStructBegin('RouterConfigVRFIDL')
        if self.object_uid != None:
            oprot.writeFieldBegin('object_uid', TType.I32, 1)
            oprot.writeI32(self.object_uid)
            oprot.writeFieldEnd()
        if self.vrf_name != None:
            oprot.writeFieldBegin('vrf_name', TType.STRING, 2)
            oprot.writeString(self.vrf_name)
            oprot.writeFieldEnd()
        if self.router_id != None:
            oprot.writeFieldBegin('router_id', TType.I32, 3)
            oprot.writeI32(self.router_id)
            oprot.writeFieldEnd()
        if self.af_list != None:
            oprot.writeFieldBegin('af_list', TType.LIST, 4)
            oprot.writeListBegin(TType.STRUCT, len(self.af_list))
            for iter40 in self.af_list:
                iter40.write(oprot)

            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.nbr_list != None:
            oprot.writeFieldBegin('nbr_list', TType.LIST, 5)
            oprot.writeListBegin(TType.STRUCT, len(self.nbr_list))
            for iter41 in self.nbr_list:
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




class RouterConfigIDL(object):
    """
    Attributes:
     - object_uid
     - type
     - asn
     - instance_name
     - vrf_list
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'object_uid',
      None,
      None),
     (2,
      TType.I32,
      'type',
      None,
      None),
     (3,
      TType.I32,
      'asn',
      None,
      None),
     (4,
      TType.STRING,
      'instance_name',
      None,
      None),
     (5,
      TType.LIST,
      'vrf_list',
      (TType.STRUCT, (RouterConfigVRFIDL, RouterConfigVRFIDL.thrift_spec)),
      None))

    def __init__(self, object_uid = None, type = None, asn = None, instance_name = None, vrf_list = None):
        self.object_uid = object_uid
        self.type = type
        self.asn = asn
        self.instance_name = instance_name
        self.vrf_list = vrf_list



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
                    self.object_uid = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.asn = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.instance_name = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.LIST:
                    self.vrf_list = []
                    (_etype45, _size42,) = iprot.readListBegin()
                    for _i46 in xrange(_size42):
                        _elem47 = RouterConfigVRFIDL()
                        _elem47.read(iprot)
                        self.vrf_list.append(_elem47)

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
        oprot.writeStructBegin('RouterConfigIDL')
        if self.object_uid != None:
            oprot.writeFieldBegin('object_uid', TType.I32, 1)
            oprot.writeI32(self.object_uid)
            oprot.writeFieldEnd()
        if self.type != None:
            oprot.writeFieldBegin('type', TType.I32, 2)
            oprot.writeI32(self.type)
            oprot.writeFieldEnd()
        if self.asn != None:
            oprot.writeFieldBegin('asn', TType.I32, 3)
            oprot.writeI32(self.asn)
            oprot.writeFieldEnd()
        if self.instance_name != None:
            oprot.writeFieldBegin('instance_name', TType.STRING, 4)
            oprot.writeString(self.instance_name)
            oprot.writeFieldEnd()
        if self.vrf_list != None:
            oprot.writeFieldBegin('vrf_list', TType.LIST, 5)
            oprot.writeListBegin(TType.STRUCT, len(self.vrf_list))
            for iter48 in self.vrf_list:
                iter48.write(oprot)

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
# 2015.02.05 17:20:40 IST
