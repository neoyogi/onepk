# 2015.02.05 17:20:25 IST
from thrift.Thrift import *
import SharedOut.ttypes
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
    from thrift.protocol import fastbinary
except:
    fastbinary = None

class TopologyNodeOutIDL(object):
    """
    Attributes:
     - hostname
     - addrlist
    """

    thrift_spec = (None, (1,
      TType.STRING,
      'hostname',
      None,
      None), (2,
      TType.LIST,
      'addrlist',
      (TType.STRUCT, (SharedOut.ttypes.NetworkAddressOutIDL, SharedOut.ttypes.NetworkAddressOutIDL.thrift_spec)),
      None))

    def __init__(self, hostname = None, addrlist = None):
        self.hostname = hostname
        self.addrlist = addrlist



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
                if ftype == TType.LIST:
                    self.addrlist = []
                    (_etype3, _size0,) = iprot.readListBegin()
                    for _i4 in xrange(_size0):
                        _elem5 = SharedOut.ttypes.NetworkAddressOutIDL()
                        _elem5.read(iprot)
                        self.addrlist.append(_elem5)

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
        oprot.writeStructBegin('TopologyNodeOutIDL')
        if self.hostname != None:
            oprot.writeFieldBegin('hostname', TType.STRING, 1)
            oprot.writeString(self.hostname)
            oprot.writeFieldEnd()
        if self.addrlist != None:
            oprot.writeFieldBegin('addrlist', TType.LIST, 2)
            oprot.writeListBegin(TType.STRUCT, len(self.addrlist))
            for iter6 in self.addrlist:
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




class TopologyConnectorOutIDL(object):
    """
    Attributes:
     - connname
     - addrlist
    """

    thrift_spec = (None, (1,
      TType.STRING,
      'connname',
      None,
      None), (2,
      TType.LIST,
      'addrlist',
      (TType.STRUCT, (SharedOut.ttypes.NetworkAddressOutIDL, SharedOut.ttypes.NetworkAddressOutIDL.thrift_spec)),
      None))

    def __init__(self, connname = None, addrlist = None):
        self.connname = connname
        self.addrlist = addrlist



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
                    self.connname = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.addrlist = []
                    (_etype10, _size7,) = iprot.readListBegin()
                    for _i11 in xrange(_size7):
                        _elem12 = SharedOut.ttypes.NetworkAddressOutIDL()
                        _elem12.read(iprot)
                        self.addrlist.append(_elem12)

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
        oprot.writeStructBegin('TopologyConnectorOutIDL')
        if self.connname != None:
            oprot.writeFieldBegin('connname', TType.STRING, 1)
            oprot.writeString(self.connname)
            oprot.writeFieldEnd()
        if self.addrlist != None:
            oprot.writeFieldBegin('addrlist', TType.LIST, 2)
            oprot.writeListBegin(TType.STRUCT, len(self.addrlist))
            for iter13 in self.addrlist:
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




class TopologyEdgeOutIDL(object):
    """
    Attributes:
     - headnode
     - headconn
     - tailnode
     - tailconn
    """

    thrift_spec = (None,
     (1,
      TType.STRUCT,
      'headnode',
      (TopologyNodeOutIDL, TopologyNodeOutIDL.thrift_spec),
      None),
     (2,
      TType.STRUCT,
      'headconn',
      (TopologyConnectorOutIDL, TopologyConnectorOutIDL.thrift_spec),
      None),
     (3,
      TType.STRUCT,
      'tailnode',
      (TopologyNodeOutIDL, TopologyNodeOutIDL.thrift_spec),
      None),
     (4,
      TType.STRUCT,
      'tailconn',
      (TopologyConnectorOutIDL, TopologyConnectorOutIDL.thrift_spec),
      None))

    def __init__(self, headnode = None, headconn = None, tailnode = None, tailconn = None):
        self.headnode = headnode
        self.headconn = headconn
        self.tailnode = tailnode
        self.tailconn = tailconn



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
                    self.headnode = TopologyNodeOutIDL()
                    self.headnode.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.headconn = TopologyConnectorOutIDL()
                    self.headconn.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRUCT:
                    self.tailnode = TopologyNodeOutIDL()
                    self.tailnode.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRUCT:
                    self.tailconn = TopologyConnectorOutIDL()
                    self.tailconn.read(iprot)
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
        oprot.writeStructBegin('TopologyEdgeOutIDL')
        if self.headnode != None:
            oprot.writeFieldBegin('headnode', TType.STRUCT, 1)
            self.headnode.write(oprot)
            oprot.writeFieldEnd()
        if self.headconn != None:
            oprot.writeFieldBegin('headconn', TType.STRUCT, 2)
            self.headconn.write(oprot)
            oprot.writeFieldEnd()
        if self.tailnode != None:
            oprot.writeFieldBegin('tailnode', TType.STRUCT, 3)
            self.tailnode.write(oprot)
            oprot.writeFieldEnd()
        if self.tailconn != None:
            oprot.writeFieldBegin('tailconn', TType.STRUCT, 4)
            self.tailconn.write(oprot)
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




class TopologyConfigOutIDL(object):
    """
    Attributes:
     - Type
    """

    thrift_spec = (None, (1,
      TType.I32,
      'Type',
      None,
      None))

    def __init__(self, Type = None):
        self.Type = Type



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
                    self.Type = iprot.readI32()
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
        oprot.writeStructBegin('TopologyConfigOutIDL')
        if self.Type != None:
            oprot.writeFieldBegin('Type', TType.I32, 1)
            oprot.writeI32(self.Type)
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
# 2015.02.05 17:20:26 IST
