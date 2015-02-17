# 2015.02.05 17:20:09 IST
from thrift.Thrift import *
import Shared.ttypes
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
    from thrift.protocol import fastbinary
except:
    fastbinary = None

class VrfState_e(object):
    VRF_STATE_INVALID = 0
    VRF_STATE_DOWN = 1
    VRF_STATE_UP = 2
    VRF_STATE_MAX = 3
    _VALUES_TO_NAMES = {0: 'VRF_STATE_INVALID',
     1: 'VRF_STATE_DOWN',
     2: 'VRF_STATE_UP',
     3: 'VRF_STATE_MAX'}
    _NAMES_TO_VALUES = {'VRF_STATE_INVALID': 0,
     'VRF_STATE_DOWN': 1,
     'VRF_STATE_UP': 2,
     'VRF_STATE_MAX': 3}


class VrfAf_e(object):
    VRF_AF_INVALID = 0
    VRF_AF_IPV4_UNICAST = 1
    VRF_AF_IPV6_UNICAST = 2
    VRF_AF_IPV4_MULTICAST = 4
    VRF_AF_IPV6_MULTICAST = 8
    _VALUES_TO_NAMES = {0: 'VRF_AF_INVALID',
     1: 'VRF_AF_IPV4_UNICAST',
     2: 'VRF_AF_IPV6_UNICAST',
     4: 'VRF_AF_IPV4_MULTICAST',
     8: 'VRF_AF_IPV6_MULTICAST'}
    _NAMES_TO_VALUES = {'VRF_AF_INVALID': 0,
     'VRF_AF_IPV4_UNICAST': 1,
     'VRF_AF_IPV6_UNICAST': 2,
     'VRF_AF_IPV4_MULTICAST': 4,
     'VRF_AF_IPV6_MULTICAST': 8}


class VrfOperation_e(object):
    VRF_OPER_ADD_VRF = 0
    VRF_OPER_REMOVE_VRF = 1
    VRF_OPER_ADD_INTF = 2
    VRF_OPER_REMOVE_INTF = 3
    VRF_OPER_MAX = 4
    _VALUES_TO_NAMES = {0: 'VRF_OPER_ADD_VRF',
     1: 'VRF_OPER_REMOVE_VRF',
     2: 'VRF_OPER_ADD_INTF',
     3: 'VRF_OPER_REMOVE_INTF',
     4: 'VRF_OPER_MAX'}
    _NAMES_TO_VALUES = {'VRF_OPER_ADD_VRF': 0,
     'VRF_OPER_REMOVE_VRF': 1,
     'VRF_OPER_ADD_INTF': 2,
     'VRF_OPER_REMOVE_INTF': 3,
     'VRF_OPER_MAX': 4}


class VrfEventType_e(object):
    VRF_EVENT_VRF_CREATED = 1
    VRF_EVENT_VRF_DELETED = 2
    VRF_EVENT_AF_ACTIVATED = 4
    VRF_EVENT_AF_DEACTIVATED = 8
    VRF_EVENT_INTERFACE_ADD = 16
    VRF_EVENT_INTERFACE_REMOVE = 32
    VRF_EVENT_MAX_ROUTES_CHANGE = 64
    VRF_EVENT_STATE_CHANGE = 128
    _VALUES_TO_NAMES = {1: 'VRF_EVENT_VRF_CREATED',
     2: 'VRF_EVENT_VRF_DELETED',
     4: 'VRF_EVENT_AF_ACTIVATED',
     8: 'VRF_EVENT_AF_DEACTIVATED',
     16: 'VRF_EVENT_INTERFACE_ADD',
     32: 'VRF_EVENT_INTERFACE_REMOVE',
     64: 'VRF_EVENT_MAX_ROUTES_CHANGE',
     128: 'VRF_EVENT_STATE_CHANGE'}
    _NAMES_TO_VALUES = {'VRF_EVENT_VRF_CREATED': 1,
     'VRF_EVENT_VRF_DELETED': 2,
     'VRF_EVENT_AF_ACTIVATED': 4,
     'VRF_EVENT_AF_DEACTIVATED': 8,
     'VRF_EVENT_INTERFACE_ADD': 16,
     'VRF_EVENT_INTERFACE_REMOVE': 32,
     'VRF_EVENT_MAX_ROUTES_CHANGE': 64,
     'VRF_EVENT_STATE_CHANGE': 128}


class RouteIDL(object):
    """
    Attributes:
     - adminDistance
     - metric
     - ec
    """

    thrift_spec = (None,
     (1,
      TType.I64,
      'adminDistance',
      None,
      None),
     (2,
      TType.I64,
      'metric',
      None,
      None),
     (3,
      TType.I32,
      'ec',
      None,
      None))

    def __init__(self, adminDistance = None, metric = None, ec = None):
        self.adminDistance = adminDistance
        self.metric = metric
        self.ec = ec



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
                    self.adminDistance = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.metric = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.ec = iprot.readI32()
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
        oprot.writeStructBegin('RouteIDL')
        if self.adminDistance != None:
            oprot.writeFieldBegin('adminDistance', TType.I64, 1)
            oprot.writeI64(self.adminDistance)
            oprot.writeFieldEnd()
        if self.metric != None:
            oprot.writeFieldBegin('metric', TType.I64, 2)
            oprot.writeI64(self.metric)
            oprot.writeFieldEnd()
        if self.ec != None:
            oprot.writeFieldBegin('ec', TType.I32, 3)
            oprot.writeI32(self.ec)
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




class RouteNextHopIDL(object):
    """
    Attributes:
     - name
     - address
     - xosHandle
     - interfaceType
     - ec
     - metric
     - route_tag
    """

    thrift_spec = (None,
     (1,
      TType.STRING,
      'name',
      None,
      None),
     (2,
      TType.STRUCT,
      'address',
      (Shared.ttypes.NetworkAddressIDL, Shared.ttypes.NetworkAddressIDL.thrift_spec),
      None),
     (3,
      TType.I64,
      'xosHandle',
      None,
      None),
     (4,
      TType.I32,
      'interfaceType',
      None,
      None),
     (5,
      TType.I32,
      'ec',
      None,
      None),
     (6,
      TType.I64,
      'metric',
      None,
      None),
     (7,
      TType.I32,
      'route_tag',
      None,
      None))

    def __init__(self, name = None, address = None, xosHandle = None, interfaceType = None, ec = None, metric = None, route_tag = None):
        self.name = name
        self.address = address
        self.xosHandle = xosHandle
        self.interfaceType = interfaceType
        self.ec = ec
        self.metric = metric
        self.route_tag = route_tag



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
                if ftype == TType.STRUCT:
                    self.address = Shared.ttypes.NetworkAddressIDL()
                    self.address.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I64:
                    self.xosHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.interfaceType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.ec = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I64:
                    self.metric = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I32:
                    self.route_tag = iprot.readI32()
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
        oprot.writeStructBegin('RouteNextHopIDL')
        if self.name != None:
            oprot.writeFieldBegin('name', TType.STRING, 1)
            oprot.writeString(self.name)
            oprot.writeFieldEnd()
        if self.address != None:
            oprot.writeFieldBegin('address', TType.STRUCT, 2)
            self.address.write(oprot)
            oprot.writeFieldEnd()
        if self.xosHandle != None:
            oprot.writeFieldBegin('xosHandle', TType.I64, 3)
            oprot.writeI64(self.xosHandle)
            oprot.writeFieldEnd()
        if self.interfaceType != None:
            oprot.writeFieldBegin('interfaceType', TType.I32, 4)
            oprot.writeI32(self.interfaceType)
            oprot.writeFieldEnd()
        if self.ec != None:
            oprot.writeFieldBegin('ec', TType.I32, 5)
            oprot.writeI32(self.ec)
            oprot.writeFieldEnd()
        if self.metric != None:
            oprot.writeFieldBegin('metric', TType.I64, 6)
            oprot.writeI64(self.metric)
            oprot.writeFieldEnd()
        if self.route_tag != None:
            oprot.writeFieldBegin('route_tag', TType.I32, 7)
            oprot.writeI32(self.route_tag)
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




class L3UcastScopeIDL(object):
    """
    Attributes:
     - afi
     - safi
     - topoName
     - vrfName
    """

    thrift_spec = (None,
     (1,
      TType.I16,
      'afi',
      None,
      None),
     (2,
      TType.I16,
      'safi',
      None,
      None),
     (3,
      TType.STRING,
      'topoName',
      None,
      ''),
     (4,
      TType.STRING,
      'vrfName',
      None,
      ''))

    def __init__(self, afi = None, safi = None, topoName = thrift_spec[3][4], vrfName = thrift_spec[4][4]):
        self.afi = afi
        self.safi = safi
        self.topoName = topoName
        self.vrfName = vrfName



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
                    self.afi = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I16:
                    self.safi = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.topoName = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.vrfName = iprot.readString()
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
        oprot.writeStructBegin('L3UcastScopeIDL')
        if self.afi != None:
            oprot.writeFieldBegin('afi', TType.I16, 1)
            oprot.writeI16(self.afi)
            oprot.writeFieldEnd()
        if self.safi != None:
            oprot.writeFieldBegin('safi', TType.I16, 2)
            oprot.writeI16(self.safi)
            oprot.writeFieldEnd()
        if self.topoName != None:
            oprot.writeFieldBegin('topoName', TType.STRING, 3)
            oprot.writeString(self.topoName)
            oprot.writeFieldEnd()
        if self.vrfName != None:
            oprot.writeFieldBegin('vrfName', TType.STRING, 4)
            oprot.writeString(self.vrfName)
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




class L3UcastRouteNextHopIDL(object):
    """
    Attributes:
     - nextHop
     - hopType
     - scope
    """

    thrift_spec = (None,
     (1,
      TType.STRUCT,
      'nextHop',
      (RouteNextHopIDL, RouteNextHopIDL.thrift_spec),
      None),
     (2,
      TType.I32,
      'hopType',
      None,
      None),
     (3,
      TType.STRUCT,
      'scope',
      (L3UcastScopeIDL, L3UcastScopeIDL.thrift_spec),
      None))

    def __init__(self, nextHop = None, hopType = None, scope = None):
        self.nextHop = nextHop
        self.hopType = hopType
        self.scope = scope



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
                    self.nextHop = RouteNextHopIDL()
                    self.nextHop.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.hopType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRUCT:
                    self.scope = L3UcastScopeIDL()
                    self.scope.read(iprot)
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
        oprot.writeStructBegin('L3UcastRouteNextHopIDL')
        if self.nextHop != None:
            oprot.writeFieldBegin('nextHop', TType.STRUCT, 1)
            self.nextHop.write(oprot)
            oprot.writeFieldEnd()
        if self.hopType != None:
            oprot.writeFieldBegin('hopType', TType.I32, 2)
            oprot.writeI32(self.hopType)
            oprot.writeFieldEnd()
        if self.scope != None:
            oprot.writeFieldBegin('scope', TType.STRUCT, 3)
            self.scope.write(oprot)
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




class L3UcastRouteIDL(object):
    """
    Attributes:
     - route
     - l3UcastRouteType
     - ownerType
     - tag
     - prefix
     - hopList
    """

    thrift_spec = (None,
     (1,
      TType.STRUCT,
      'route',
      (RouteIDL, RouteIDL.thrift_spec),
      None),
     (2,
      TType.I16,
      'l3UcastRouteType',
      None,
      None),
     (3,
      TType.I16,
      'ownerType',
      None,
      None),
     (4,
      TType.STRING,
      'tag',
      None,
      None),
     (5,
      TType.STRUCT,
      'prefix',
      (Shared.ttypes.NetworkPrefixIDL, Shared.ttypes.NetworkPrefixIDL.thrift_spec),
      None),
     (6,
      TType.LIST,
      'hopList',
      (TType.STRUCT, (L3UcastRouteNextHopIDL, L3UcastRouteNextHopIDL.thrift_spec)),
      None))

    def __init__(self, route = None, l3UcastRouteType = None, ownerType = None, tag = None, prefix = None, hopList = None):
        self.route = route
        self.l3UcastRouteType = l3UcastRouteType
        self.ownerType = ownerType
        self.tag = tag
        self.prefix = prefix
        self.hopList = hopList



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
                    self.route = RouteIDL()
                    self.route.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I16:
                    self.l3UcastRouteType = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I16:
                    self.ownerType = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.tag = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRUCT:
                    self.prefix = Shared.ttypes.NetworkPrefixIDL()
                    self.prefix.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.LIST:
                    self.hopList = []
                    (_etype3, _size0,) = iprot.readListBegin()
                    for _i4 in xrange(_size0):
                        _elem5 = L3UcastRouteNextHopIDL()
                        _elem5.read(iprot)
                        self.hopList.append(_elem5)

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
        oprot.writeStructBegin('L3UcastRouteIDL')
        if self.route != None:
            oprot.writeFieldBegin('route', TType.STRUCT, 1)
            self.route.write(oprot)
            oprot.writeFieldEnd()
        if self.l3UcastRouteType != None:
            oprot.writeFieldBegin('l3UcastRouteType', TType.I16, 2)
            oprot.writeI16(self.l3UcastRouteType)
            oprot.writeFieldEnd()
        if self.ownerType != None:
            oprot.writeFieldBegin('ownerType', TType.I16, 3)
            oprot.writeI16(self.ownerType)
            oprot.writeFieldEnd()
        if self.tag != None:
            oprot.writeFieldBegin('tag', TType.STRING, 4)
            oprot.writeString(self.tag)
            oprot.writeFieldEnd()
        if self.prefix != None:
            oprot.writeFieldBegin('prefix', TType.STRUCT, 5)
            self.prefix.write(oprot)
            oprot.writeFieldEnd()
        if self.hopList != None:
            oprot.writeFieldBegin('hopList', TType.LIST, 6)
            oprot.writeListBegin(TType.STRUCT, len(self.hopList))
            for iter6 in self.hopList:
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




class L3UcastRouteAppRouteTableOpIDL(object):
    """
    Attributes:
     - opType
     - route
    """

    thrift_spec = (None, (1,
      TType.I16,
      'opType',
      None,
      None), (2,
      TType.STRUCT,
      'route',
      (L3UcastRouteIDL, L3UcastRouteIDL.thrift_spec),
      None))

    def __init__(self, opType = None, route = None):
        self.opType = opType
        self.route = route



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
                    self.opType = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.route = L3UcastRouteIDL()
                    self.route.read(iprot)
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
        oprot.writeStructBegin('L3UcastRouteAppRouteTableOpIDL')
        if self.opType != None:
            oprot.writeFieldBegin('opType', TType.I16, 1)
            oprot.writeI16(self.opType)
            oprot.writeFieldEnd()
        if self.route != None:
            oprot.writeFieldBegin('route', TType.STRUCT, 2)
            self.route.write(oprot)
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




class L3UcastRouteRangeIDL(object):
    """
    Attributes:
     - rangeType
     - count
     - startPrefix
    """

    thrift_spec = (None,
     (1,
      TType.I16,
      'rangeType',
      None,
      None),
     (2,
      TType.I64,
      'count',
      None,
      None),
     (3,
      TType.STRUCT,
      'startPrefix',
      (Shared.ttypes.NetworkPrefixIDL, Shared.ttypes.NetworkPrefixIDL.thrift_spec),
      None))

    def __init__(self, rangeType = None, count = None, startPrefix = None):
        self.rangeType = rangeType
        self.count = count
        self.startPrefix = startPrefix



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
                    self.rangeType = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.count = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRUCT:
                    self.startPrefix = Shared.ttypes.NetworkPrefixIDL()
                    self.startPrefix.read(iprot)
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
        oprot.writeStructBegin('L3UcastRouteRangeIDL')
        if self.rangeType != None:
            oprot.writeFieldBegin('rangeType', TType.I16, 1)
            oprot.writeI16(self.rangeType)
            oprot.writeFieldEnd()
        if self.count != None:
            oprot.writeFieldBegin('count', TType.I64, 2)
            oprot.writeI64(self.count)
            oprot.writeFieldEnd()
        if self.startPrefix != None:
            oprot.writeFieldBegin('startPrefix', TType.STRUCT, 3)
            self.startPrefix.write(oprot)
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




class L3UcastRibFilterIDL(object):
    """
    Attributes:
     - ownerType
     - tag
     - prefix
     - matchPrefixGeLen
     - matchPrefixLeLen
     - matchPrefixNeLen
    """

    thrift_spec = (None,
     (1,
      TType.I16,
      'ownerType',
      None,
      None),
     (2,
      TType.STRING,
      'tag',
      None,
      ''),
     (3,
      TType.STRUCT,
      'prefix',
      (Shared.ttypes.NetworkPrefixIDL, Shared.ttypes.NetworkPrefixIDL.thrift_spec),
      None),
     (4,
      TType.I32,
      'matchPrefixGeLen',
      None,
      None),
     (5,
      TType.I32,
      'matchPrefixLeLen',
      None,
      None),
     (6,
      TType.I32,
      'matchPrefixNeLen',
      None,
      None))

    def __init__(self, ownerType = None, tag = thrift_spec[2][4], prefix = None, matchPrefixGeLen = None, matchPrefixLeLen = None, matchPrefixNeLen = None):
        self.ownerType = ownerType
        self.tag = tag
        self.prefix = prefix
        self.matchPrefixGeLen = matchPrefixGeLen
        self.matchPrefixLeLen = matchPrefixLeLen
        self.matchPrefixNeLen = matchPrefixNeLen



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
                    self.ownerType = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.tag = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRUCT:
                    self.prefix = Shared.ttypes.NetworkPrefixIDL()
                    self.prefix.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.matchPrefixGeLen = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.matchPrefixLeLen = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I32:
                    self.matchPrefixNeLen = iprot.readI32()
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
        oprot.writeStructBegin('L3UcastRibFilterIDL')
        if self.ownerType != None:
            oprot.writeFieldBegin('ownerType', TType.I16, 1)
            oprot.writeI16(self.ownerType)
            oprot.writeFieldEnd()
        if self.tag != None:
            oprot.writeFieldBegin('tag', TType.STRING, 2)
            oprot.writeString(self.tag)
            oprot.writeFieldEnd()
        if self.prefix != None:
            oprot.writeFieldBegin('prefix', TType.STRUCT, 3)
            self.prefix.write(oprot)
            oprot.writeFieldEnd()
        if self.matchPrefixGeLen != None:
            oprot.writeFieldBegin('matchPrefixGeLen', TType.I32, 4)
            oprot.writeI32(self.matchPrefixGeLen)
            oprot.writeFieldEnd()
        if self.matchPrefixLeLen != None:
            oprot.writeFieldBegin('matchPrefixLeLen', TType.I32, 5)
            oprot.writeI32(self.matchPrefixLeLen)
            oprot.writeFieldEnd()
        if self.matchPrefixNeLen != None:
            oprot.writeFieldBegin('matchPrefixNeLen', TType.I32, 6)
            oprot.writeI32(self.matchPrefixNeLen)
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




class VrfKeyIDL(object):
    """
    Attributes:
     - vrfName
     - vrfId
    """

    thrift_spec = (None, (1,
      TType.STRING,
      'vrfName',
      None,
      ''), (2,
      TType.I64,
      'vrfId',
      None,
      None))

    def __init__(self, vrfName = thrift_spec[1][4], vrfId = None):
        self.vrfName = vrfName
        self.vrfId = vrfId



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
                    self.vrfName = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.vrfId = iprot.readI64()
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
        oprot.writeStructBegin('VrfKeyIDL')
        if self.vrfName != None:
            oprot.writeFieldBegin('vrfName', TType.STRING, 1)
            oprot.writeString(self.vrfName)
            oprot.writeFieldEnd()
        if self.vrfId != None:
            oprot.writeFieldBegin('vrfId', TType.I64, 2)
            oprot.writeI64(self.vrfId)
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




class VrfIDL(object):
    """
    Attributes:
     - vrfName
     - vrfId
     - vrfState
     - af_mask
     - errcode
    """

    thrift_spec = (None,
     (1,
      TType.STRING,
      'vrfName',
      None,
      None),
     (2,
      TType.I64,
      'vrfId',
      None,
      None),
     (3,
      TType.I32,
      'vrfState',
      None,
      None),
     (4,
      TType.I32,
      'af_mask',
      None,
      None),
     (5,
      TType.I32,
      'errcode',
      None,
      None))

    def __init__(self, vrfName = None, vrfId = None, vrfState = None, af_mask = None, errcode = None):
        self.vrfName = vrfName
        self.vrfId = vrfId
        self.vrfState = vrfState
        self.af_mask = af_mask
        self.errcode = errcode



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
                    self.vrfName = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.vrfId = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.vrfState = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.af_mask = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.errcode = iprot.readI32()
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
        oprot.writeStructBegin('VrfIDL')
        if self.vrfName != None:
            oprot.writeFieldBegin('vrfName', TType.STRING, 1)
            oprot.writeString(self.vrfName)
            oprot.writeFieldEnd()
        if self.vrfId != None:
            oprot.writeFieldBegin('vrfId', TType.I64, 2)
            oprot.writeI64(self.vrfId)
            oprot.writeFieldEnd()
        if self.vrfState != None:
            oprot.writeFieldBegin('vrfState', TType.I32, 3)
            oprot.writeI32(self.vrfState)
            oprot.writeFieldEnd()
        if self.af_mask != None:
            oprot.writeFieldBegin('af_mask', TType.I32, 4)
            oprot.writeI32(self.af_mask)
            oprot.writeFieldEnd()
        if self.errcode != None:
            oprot.writeFieldBegin('errcode', TType.I32, 5)
            oprot.writeI32(self.errcode)
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




class VrfTableOpIDL(object):
    """
    Attributes:
     - opType
     - vrf
     - intf
     - errcode
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'opType',
      None,
      None),
     (2,
      TType.STRUCT,
      'vrf',
      (VrfIDL, VrfIDL.thrift_spec),
      None),
     (3,
      TType.STRUCT,
      'intf',
      (Shared.ttypes.NetworkInterfaceIDL, Shared.ttypes.NetworkInterfaceIDL.thrift_spec),
      None),
     (4,
      TType.I32,
      'errcode',
      None,
      None))

    def __init__(self, opType = None, vrf = None, intf = None, errcode = None):
        self.opType = opType
        self.vrf = vrf
        self.intf = intf
        self.errcode = errcode



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
                    self.opType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.vrf = VrfIDL()
                    self.vrf.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRUCT:
                    self.intf = Shared.ttypes.NetworkInterfaceIDL()
                    self.intf.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.errcode = iprot.readI32()
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
        oprot.writeStructBegin('VrfTableOpIDL')
        if self.opType != None:
            oprot.writeFieldBegin('opType', TType.I32, 1)
            oprot.writeI32(self.opType)
            oprot.writeFieldEnd()
        if self.vrf != None:
            oprot.writeFieldBegin('vrf', TType.STRUCT, 2)
            self.vrf.write(oprot)
            oprot.writeFieldEnd()
        if self.intf != None:
            oprot.writeFieldBegin('intf', TType.STRUCT, 3)
            self.intf.write(oprot)
            oprot.writeFieldEnd()
        if self.errcode != None:
            oprot.writeFieldBegin('errcode', TType.I32, 4)
            oprot.writeI32(self.errcode)
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




class VrfFilterIDL(object):
    """
    Attributes:
     - vrfName
     - af_mask
     - flags
     - event_mask
    """

    thrift_spec = (None,
     (1,
      TType.STRING,
      'vrfName',
      None,
      None),
     (2,
      TType.I32,
      'af_mask',
      None,
      None),
     (3,
      TType.I32,
      'flags',
      None,
      None),
     (4,
      TType.SET,
      'event_mask',
      (TType.I32, None),
      None))

    def __init__(self, vrfName = None, af_mask = None, flags = None, event_mask = None):
        self.vrfName = vrfName
        self.af_mask = af_mask
        self.flags = flags
        self.event_mask = event_mask



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
                    self.vrfName = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.af_mask = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.flags = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.SET:
                    self.event_mask = set()
                    (_etype10, _size7,) = iprot.readSetBegin()
                    for _i11 in xrange(_size7):
                        _elem12 = iprot.readI32()
                        self.event_mask.add(_elem12)

                    iprot.readSetEnd()
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
        oprot.writeStructBegin('VrfFilterIDL')
        if self.vrfName != None:
            oprot.writeFieldBegin('vrfName', TType.STRING, 1)
            oprot.writeString(self.vrfName)
            oprot.writeFieldEnd()
        if self.af_mask != None:
            oprot.writeFieldBegin('af_mask', TType.I32, 2)
            oprot.writeI32(self.af_mask)
            oprot.writeFieldEnd()
        if self.flags != None:
            oprot.writeFieldBegin('flags', TType.I32, 3)
            oprot.writeI32(self.flags)
            oprot.writeFieldEnd()
        if self.event_mask != None:
            oprot.writeFieldBegin('event_mask', TType.SET, 4)
            oprot.writeSetBegin(TType.I32, len(self.event_mask))
            for iter13 in self.event_mask:
                oprot.writeI32(iter13)

            oprot.writeSetEnd()
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
# 2015.02.05 17:20:10 IST
