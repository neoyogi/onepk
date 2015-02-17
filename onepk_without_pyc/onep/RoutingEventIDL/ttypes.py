# 2015.02.05 17:23:01 IST
from thrift.Thrift import *
import SharedOut.ttypes
import AsyncMessageIDL.ttypes
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
    from thrift.protocol import fastbinary
except:
    fastbinary = None

class VrfStateOutbound_e(object):
    VRF_STATE_OUT_INVALID = 0
    VRF_STATE_OUT_DOWN = 1
    VRF_STATE_OUT_UP = 2
    VRF_STATE_OUT_MAX = 3
    _VALUES_TO_NAMES = {0: 'VRF_STATE_OUT_INVALID',
     1: 'VRF_STATE_OUT_DOWN',
     2: 'VRF_STATE_OUT_UP',
     3: 'VRF_STATE_OUT_MAX'}
    _NAMES_TO_VALUES = {'VRF_STATE_OUT_INVALID': 0,
     'VRF_STATE_OUT_DOWN': 1,
     'VRF_STATE_OUT_UP': 2,
     'VRF_STATE_OUT_MAX': 3}


class RouteOutIDL(object):
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
        oprot.writeStructBegin('RouteOutIDL')
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




class RouteNextHopOutIDL(object):
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
      (SharedOut.ttypes.NetworkAddressOutIDL, SharedOut.ttypes.NetworkAddressOutIDL.thrift_spec),
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
                    self.address = SharedOut.ttypes.NetworkAddressOutIDL()
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
        oprot.writeStructBegin('RouteNextHopOutIDL')
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




class L3UcastScopeOutIDL(object):
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
        oprot.writeStructBegin('L3UcastScopeOutIDL')
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




class L3UcastRouteNextHopOutIDL(object):
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
      (RouteNextHopOutIDL, RouteNextHopOutIDL.thrift_spec),
      None),
     (2,
      TType.I32,
      'hopType',
      None,
      None),
     (3,
      TType.STRUCT,
      'scope',
      (L3UcastScopeOutIDL, L3UcastScopeOutIDL.thrift_spec),
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
                    self.nextHop = RouteNextHopOutIDL()
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
                    self.scope = L3UcastScopeOutIDL()
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
        oprot.writeStructBegin('L3UcastRouteNextHopOutIDL')
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




class L3UcastRouteOutIDL(object):
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
      (RouteOutIDL, RouteOutIDL.thrift_spec),
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
      (SharedOut.ttypes.NetworkPrefixOutIDL, SharedOut.ttypes.NetworkPrefixOutIDL.thrift_spec),
      None),
     (6,
      TType.LIST,
      'hopList',
      (TType.STRUCT, (L3UcastRouteNextHopOutIDL, L3UcastRouteNextHopOutIDL.thrift_spec)),
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
                    self.route = RouteOutIDL()
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
                    self.prefix = SharedOut.ttypes.NetworkPrefixOutIDL()
                    self.prefix.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.LIST:
                    self.hopList = []
                    (_etype3, _size0,) = iprot.readListBegin()
                    for _i4 in xrange(_size0):
                        _elem5 = L3UcastRouteNextHopOutIDL()
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
        oprot.writeStructBegin('L3UcastRouteOutIDL')
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




class L3UcastRouteAppRouteTableOpOutIDL(object):
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
      (L3UcastRouteOutIDL, L3UcastRouteOutIDL.thrift_spec),
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
                    self.route = L3UcastRouteOutIDL()
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
        oprot.writeStructBegin('L3UcastRouteAppRouteTableOpOutIDL')
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




class L3UcastRouteTableEventOutIDL(object):
    """
    Attributes:
     - sessionHandle
     - eventHandle
     - protocol
     - metric
     - distance
     - topoName
     - vrfName
     - tagName
     - prefix
     - hopList
     - l3UcastRouteType
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionHandle',
      None,
      None),
     (2,
      TType.I32,
      'eventHandle',
      None,
      None),
     (3,
      TType.I32,
      'protocol',
      None,
      None),
     (4,
      TType.I32,
      'metric',
      None,
      None),
     (5,
      TType.I32,
      'distance',
      None,
      None),
     (6,
      TType.STRING,
      'topoName',
      None,
      None),
     (7,
      TType.STRING,
      'vrfName',
      None,
      None),
     (8,
      TType.STRING,
      'tagName',
      None,
      None),
     (9,
      TType.STRUCT,
      'prefix',
      (SharedOut.ttypes.NetworkPrefixOutIDL, SharedOut.ttypes.NetworkPrefixOutIDL.thrift_spec),
      None),
     (10,
      TType.LIST,
      'hopList',
      (TType.STRUCT, (L3UcastRouteNextHopOutIDL, L3UcastRouteNextHopOutIDL.thrift_spec)),
      None),
     (11,
      TType.I16,
      'l3UcastRouteType',
      None,
      None))

    def __init__(self, sessionHandle = None, eventHandle = None, protocol = None, metric = None, distance = None, topoName = None, vrfName = None, tagName = None, prefix = None, hopList = None, l3UcastRouteType = None):
        self.sessionHandle = sessionHandle
        self.eventHandle = eventHandle
        self.protocol = protocol
        self.metric = metric
        self.distance = distance
        self.topoName = topoName
        self.vrfName = vrfName
        self.tagName = tagName
        self.prefix = prefix
        self.hopList = hopList
        self.l3UcastRouteType = l3UcastRouteType



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
                    self.sessionHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.eventHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.protocol = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.metric = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.distance = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRING:
                    self.topoName = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.STRING:
                    self.vrfName = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.STRING:
                    self.tagName = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.STRUCT:
                    self.prefix = SharedOut.ttypes.NetworkPrefixOutIDL()
                    self.prefix.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.LIST:
                    self.hopList = []
                    (_etype10, _size7,) = iprot.readListBegin()
                    for _i11 in xrange(_size7):
                        _elem12 = L3UcastRouteNextHopOutIDL()
                        _elem12.read(iprot)
                        self.hopList.append(_elem12)

                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.I16:
                    self.l3UcastRouteType = iprot.readI16()
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
        oprot.writeStructBegin('L3UcastRouteTableEventOutIDL')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.eventHandle != None:
            oprot.writeFieldBegin('eventHandle', TType.I32, 2)
            oprot.writeI32(self.eventHandle)
            oprot.writeFieldEnd()
        if self.protocol != None:
            oprot.writeFieldBegin('protocol', TType.I32, 3)
            oprot.writeI32(self.protocol)
            oprot.writeFieldEnd()
        if self.metric != None:
            oprot.writeFieldBegin('metric', TType.I32, 4)
            oprot.writeI32(self.metric)
            oprot.writeFieldEnd()
        if self.distance != None:
            oprot.writeFieldBegin('distance', TType.I32, 5)
            oprot.writeI32(self.distance)
            oprot.writeFieldEnd()
        if self.topoName != None:
            oprot.writeFieldBegin('topoName', TType.STRING, 6)
            oprot.writeString(self.topoName)
            oprot.writeFieldEnd()
        if self.vrfName != None:
            oprot.writeFieldBegin('vrfName', TType.STRING, 7)
            oprot.writeString(self.vrfName)
            oprot.writeFieldEnd()
        if self.tagName != None:
            oprot.writeFieldBegin('tagName', TType.STRING, 8)
            oprot.writeString(self.tagName)
            oprot.writeFieldEnd()
        if self.prefix != None:
            oprot.writeFieldBegin('prefix', TType.STRUCT, 9)
            self.prefix.write(oprot)
            oprot.writeFieldEnd()
        if self.hopList != None:
            oprot.writeFieldBegin('hopList', TType.LIST, 10)
            oprot.writeListBegin(TType.STRUCT, len(self.hopList))
            for iter13 in self.hopList:
                iter13.write(oprot)

            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.l3UcastRouteType != None:
            oprot.writeFieldBegin('l3UcastRouteType', TType.I16, 11)
            oprot.writeI16(self.l3UcastRouteType)
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




class VrfEventIDL(object):
    """
    Attributes:
     - vrfName
     - vrfId
     - vrfState
     - af_mask
     - if_name
     - xosHandle
     - interfaceType
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
      TType.STRING,
      'if_name',
      None,
      None),
     (6,
      TType.I64,
      'xosHandle',
      None,
      None),
     (7,
      TType.I32,
      'interfaceType',
      None,
      None))

    def __init__(self, vrfName = None, vrfId = None, vrfState = None, af_mask = None, if_name = None, xosHandle = None, interfaceType = None):
        self.vrfName = vrfName
        self.vrfId = vrfId
        self.vrfState = vrfState
        self.af_mask = af_mask
        self.if_name = if_name
        self.xosHandle = xosHandle
        self.interfaceType = interfaceType



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
                if ftype == TType.STRING:
                    self.if_name = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I64:
                    self.xosHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I32:
                    self.interfaceType = iprot.readI32()
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
        oprot.writeStructBegin('VrfEventIDL')
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
        if self.if_name != None:
            oprot.writeFieldBegin('if_name', TType.STRING, 5)
            oprot.writeString(self.if_name)
            oprot.writeFieldEnd()
        if self.xosHandle != None:
            oprot.writeFieldBegin('xosHandle', TType.I64, 6)
            oprot.writeI64(self.xosHandle)
            oprot.writeFieldEnd()
        if self.interfaceType != None:
            oprot.writeFieldBegin('interfaceType', TType.I32, 7)
            oprot.writeI32(self.interfaceType)
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
# 2015.02.05 17:23:02 IST
