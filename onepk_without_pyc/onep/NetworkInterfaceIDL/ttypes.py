# 2015.02.05 17:22:05 IST
from thrift.Thrift import *
import Shared.ttypes
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
    from thrift.protocol import fastbinary
except:
    fastbinary = None

class InterfacePropertyIDL(object):
    """
      Hard property for interface which is
      obtained only once from NE.
    
      Attributes:
       - slot
       - port
       - speed
       - shortname
       - subif_id
      """

    thrift_spec = (None,
     (1,
      TType.I32,
      'slot',
      None,
      None),
     (2,
      TType.I32,
      'port',
      None,
      None),
     (3,
      TType.I32,
      'speed',
      None,
      None),
     (4,
      TType.STRING,
      'shortname',
      None,
      None),
     (5,
      TType.I64,
      'subif_id',
      None,
      None))

    def __init__(self, slot = None, port = None, speed = None, shortname = None, subif_id = None):
        self.slot = slot
        self.port = port
        self.speed = speed
        self.shortname = shortname
        self.subif_id = subif_id



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
                    self.slot = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.port = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.speed = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.shortname = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I64:
                    self.subif_id = iprot.readI64()
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
        oprot.writeStructBegin('InterfacePropertyIDL')
        if self.slot != None:
            oprot.writeFieldBegin('slot', TType.I32, 1)
            oprot.writeI32(self.slot)
            oprot.writeFieldEnd()
        if self.port != None:
            oprot.writeFieldBegin('port', TType.I32, 2)
            oprot.writeI32(self.port)
            oprot.writeFieldEnd()
        if self.speed != None:
            oprot.writeFieldBegin('speed', TType.I32, 3)
            oprot.writeI32(self.speed)
            oprot.writeFieldEnd()
        if self.shortname != None:
            oprot.writeFieldBegin('shortname', TType.STRING, 4)
            oprot.writeString(self.shortname)
            oprot.writeFieldEnd()
        if self.subif_id != None:
            oprot.writeFieldBegin('subif_id', TType.I64, 5)
            oprot.writeI64(self.subif_id)
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




class IssubInterfaceIDL(object):
    """
      subif_id is uint32_t
    
      Attributes:
       - is_sub
      """

    thrift_spec = (None, (1,
      TType.I32,
      'is_sub',
      None,
      None))

    def __init__(self, is_sub = None):
        self.is_sub = is_sub



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
                    self.is_sub = iprot.readI32()
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
        oprot.writeStructBegin('IssubInterfaceIDL')
        if self.is_sub != None:
            oprot.writeFieldBegin('is_sub', TType.I32, 1)
            oprot.writeI32(self.is_sub)
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




class InterfaceConfigSpeedIDL(object):
    """
    Attributes:
     - configured
     - operational
     - capability
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'configured',
      None,
      None),
     (2,
      TType.I32,
      'operational',
      None,
      None),
     (3,
      TType.I32,
      'capability',
      None,
      None))

    def __init__(self, configured = None, operational = None, capability = None):
        self.configured = configured
        self.operational = operational
        self.capability = capability



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
                    self.configured = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.operational = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.capability = iprot.readI32()
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
        oprot.writeStructBegin('InterfaceConfigSpeedIDL')
        if self.configured != None:
            oprot.writeFieldBegin('configured', TType.I32, 1)
            oprot.writeI32(self.configured)
            oprot.writeFieldEnd()
        if self.operational != None:
            oprot.writeFieldBegin('operational', TType.I32, 2)
            oprot.writeI32(self.operational)
            oprot.writeFieldEnd()
        if self.capability != None:
            oprot.writeFieldBegin('capability', TType.I32, 3)
            oprot.writeI32(self.capability)
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




class InterfaceConfigDuplexIDL(object):
    """
    Attributes:
     - configured
     - operational
    """

    thrift_spec = (None, (1,
      TType.BYTE,
      'configured',
      None,
      None), (2,
      TType.BYTE,
      'operational',
      None,
      None))

    def __init__(self, configured = None, operational = None):
        self.configured = configured
        self.operational = operational



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
                    self.configured = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.BYTE:
                    self.operational = iprot.readByte()
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
        oprot.writeStructBegin('InterfaceConfigDuplexIDL')
        if self.configured != None:
            oprot.writeFieldBegin('configured', TType.BYTE, 1)
            oprot.writeByte(self.configured)
            oprot.writeFieldEnd()
        if self.operational != None:
            oprot.writeFieldBegin('operational', TType.BYTE, 2)
            oprot.writeByte(self.operational)
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




class InterfaceConfigAutonegIDL(object):
    """
    Attributes:
     - configured
     - operational
    """

    thrift_spec = (None, (1,
      TType.BYTE,
      'configured',
      None,
      None), (2,
      TType.BYTE,
      'operational',
      None,
      None))

    def __init__(self, configured = None, operational = None):
        self.configured = configured
        self.operational = operational



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
                    self.configured = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.BYTE:
                    self.operational = iprot.readByte()
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
        oprot.writeStructBegin('InterfaceConfigAutonegIDL')
        if self.configured != None:
            oprot.writeFieldBegin('configured', TType.BYTE, 1)
            oprot.writeByte(self.configured)
            oprot.writeFieldEnd()
        if self.operational != None:
            oprot.writeFieldBegin('operational', TType.BYTE, 2)
            oprot.writeByte(self.operational)
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




class InterfaceConfigFlowCtrlIDL(object):
    """
    Attributes:
     - input_configured
     - input_operational
     - output_configured
     - output_operational
    """

    thrift_spec = (None,
     (1,
      TType.BYTE,
      'input_configured',
      None,
      None),
     (2,
      TType.BYTE,
      'input_operational',
      None,
      None),
     (3,
      TType.BYTE,
      'output_configured',
      None,
      None),
     (4,
      TType.BYTE,
      'output_operational',
      None,
      None))

    def __init__(self, input_configured = None, input_operational = None, output_configured = None, output_operational = None):
        self.input_configured = input_configured
        self.input_operational = input_operational
        self.output_configured = output_configured
        self.output_operational = output_operational



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
                    self.input_configured = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.BYTE:
                    self.input_operational = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.BYTE:
                    self.output_configured = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.BYTE:
                    self.output_operational = iprot.readByte()
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
        oprot.writeStructBegin('InterfaceConfigFlowCtrlIDL')
        if self.input_configured != None:
            oprot.writeFieldBegin('input_configured', TType.BYTE, 1)
            oprot.writeByte(self.input_configured)
            oprot.writeFieldEnd()
        if self.input_operational != None:
            oprot.writeFieldBegin('input_operational', TType.BYTE, 2)
            oprot.writeByte(self.input_operational)
            oprot.writeFieldEnd()
        if self.output_configured != None:
            oprot.writeFieldBegin('output_configured', TType.BYTE, 3)
            oprot.writeByte(self.output_configured)
            oprot.writeFieldEnd()
        if self.output_operational != None:
            oprot.writeFieldBegin('output_operational', TType.BYTE, 4)
            oprot.writeByte(self.output_operational)
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




class InterfaceConfigIDL(object):
    """
      Soft property (configuration) of interface
      Currently retrieved on demand
      in future can be refreshed automatically
    
      Attributes:
       - layer2
       - mtu
       - snmp
       - tx
       - rx
       - mode
       - encap
       - duplex
       - displayName
       - macaddr
       - descr
       - ipRedirect
       - ipUnreachable
       - ipProxyArp
       - ipUnicastReversePath
       - ipHelperAddr
       - speedIDL
       - duplexIDL
       - autoNegIDL
       - fcIDL
       - fwdClassID
      """

    thrift_spec = (None,
     (1,
      TType.I32,
      'layer2',
      None,
      None),
     (2,
      TType.I32,
      'mtu',
      None,
      None),
     (3,
      TType.I64,
      'snmp',
      None,
      None),
     (4,
      TType.I32,
      'tx',
      None,
      None),
     (5,
      TType.I32,
      'rx',
      None,
      None),
     (6,
      TType.BYTE,
      'mode',
      None,
      None),
     (7,
      TType.BYTE,
      'encap',
      None,
      None),
     (8,
      TType.BYTE,
      'duplex',
      None,
      None),
     (9,
      TType.STRING,
      'displayName',
      None,
      None),
     (10,
      TType.LIST,
      'macaddr',
      (TType.BYTE, None),
      [1,
       2,
       3,
       4,
       5,
       6]),
     (11,
      TType.STRING,
      'descr',
      None,
      None),
     (12,
      TType.I32,
      'ipRedirect',
      None,
      None),
     (13,
      TType.I32,
      'ipUnreachable',
      None,
      None),
     (14,
      TType.I32,
      'ipProxyArp',
      None,
      None),
     (15,
      TType.I32,
      'ipUnicastReversePath',
      None,
      None),
     (16,
      TType.LIST,
      'ipHelperAddr',
      (TType.STRUCT, (Shared.ttypes.NetworkAddressIDL, Shared.ttypes.NetworkAddressIDL.thrift_spec)),
      None),
     (17,
      TType.STRUCT,
      'speedIDL',
      (InterfaceConfigSpeedIDL, InterfaceConfigSpeedIDL.thrift_spec),
      None),
     (18,
      TType.STRUCT,
      'duplexIDL',
      (InterfaceConfigDuplexIDL, InterfaceConfigDuplexIDL.thrift_spec),
      None),
     (19,
      TType.STRUCT,
      'autoNegIDL',
      (InterfaceConfigAutonegIDL, InterfaceConfigAutonegIDL.thrift_spec),
      None),
     (20,
      TType.STRUCT,
      'fcIDL',
      (InterfaceConfigFlowCtrlIDL, InterfaceConfigFlowCtrlIDL.thrift_spec),
      None),
     (21,
      TType.I32,
      'fwdClassID',
      None,
      None))

    def __init__(self, layer2 = None, mtu = None, snmp = None, tx = None, rx = None, mode = None, encap = None, duplex = None, displayName = None, macaddr = thrift_spec[10][4], descr = None, ipRedirect = None, ipUnreachable = None, ipProxyArp = None, ipUnicastReversePath = None, ipHelperAddr = None, speedIDL = None, duplexIDL = None, autoNegIDL = None, fcIDL = None, fwdClassID = None):
        self.layer2 = layer2
        self.mtu = mtu
        self.snmp = snmp
        self.tx = tx
        self.rx = rx
        self.mode = mode
        self.encap = encap
        self.duplex = duplex
        self.displayName = displayName
        if macaddr is self.thrift_spec[10][4]:
            macaddr = [1,
             2,
             3,
             4,
             5,
             6]
        self.macaddr = macaddr
        self.descr = descr
        self.ipRedirect = ipRedirect
        self.ipUnreachable = ipUnreachable
        self.ipProxyArp = ipProxyArp
        self.ipUnicastReversePath = ipUnicastReversePath
        self.ipHelperAddr = ipHelperAddr
        self.speedIDL = speedIDL
        self.duplexIDL = duplexIDL
        self.autoNegIDL = autoNegIDL
        self.fcIDL = fcIDL
        self.fwdClassID = fwdClassID



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
                    self.layer2 = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.mtu = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I64:
                    self.snmp = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.tx = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.rx = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.BYTE:
                    self.mode = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.BYTE:
                    self.encap = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.BYTE:
                    self.duplex = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.STRING:
                    self.displayName = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.LIST:
                    self.macaddr = []
                    (_etype3, _size0,) = iprot.readListBegin()
                    for _i4 in xrange(_size0):
                        _elem5 = iprot.readByte()
                        self.macaddr.append(_elem5)

                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.STRING:
                    self.descr = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 12:
                if ftype == TType.I32:
                    self.ipRedirect = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 13:
                if ftype == TType.I32:
                    self.ipUnreachable = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 14:
                if ftype == TType.I32:
                    self.ipProxyArp = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 15:
                if ftype == TType.I32:
                    self.ipUnicastReversePath = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 16:
                if ftype == TType.LIST:
                    self.ipHelperAddr = []
                    (_etype9, _size6,) = iprot.readListBegin()
                    for _i10 in xrange(_size6):
                        _elem11 = Shared.ttypes.NetworkAddressIDL()
                        _elem11.read(iprot)
                        self.ipHelperAddr.append(_elem11)

                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 17:
                if ftype == TType.STRUCT:
                    self.speedIDL = InterfaceConfigSpeedIDL()
                    self.speedIDL.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 18:
                if ftype == TType.STRUCT:
                    self.duplexIDL = InterfaceConfigDuplexIDL()
                    self.duplexIDL.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 19:
                if ftype == TType.STRUCT:
                    self.autoNegIDL = InterfaceConfigAutonegIDL()
                    self.autoNegIDL.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 20:
                if ftype == TType.STRUCT:
                    self.fcIDL = InterfaceConfigFlowCtrlIDL()
                    self.fcIDL.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 21:
                if ftype == TType.I32:
                    self.fwdClassID = iprot.readI32()
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
        oprot.writeStructBegin('InterfaceConfigIDL')
        if self.layer2 != None:
            oprot.writeFieldBegin('layer2', TType.I32, 1)
            oprot.writeI32(self.layer2)
            oprot.writeFieldEnd()
        if self.mtu != None:
            oprot.writeFieldBegin('mtu', TType.I32, 2)
            oprot.writeI32(self.mtu)
            oprot.writeFieldEnd()
        if self.snmp != None:
            oprot.writeFieldBegin('snmp', TType.I64, 3)
            oprot.writeI64(self.snmp)
            oprot.writeFieldEnd()
        if self.tx != None:
            oprot.writeFieldBegin('tx', TType.I32, 4)
            oprot.writeI32(self.tx)
            oprot.writeFieldEnd()
        if self.rx != None:
            oprot.writeFieldBegin('rx', TType.I32, 5)
            oprot.writeI32(self.rx)
            oprot.writeFieldEnd()
        if self.mode != None:
            oprot.writeFieldBegin('mode', TType.BYTE, 6)
            oprot.writeByte(self.mode)
            oprot.writeFieldEnd()
        if self.encap != None:
            oprot.writeFieldBegin('encap', TType.BYTE, 7)
            oprot.writeByte(self.encap)
            oprot.writeFieldEnd()
        if self.duplex != None:
            oprot.writeFieldBegin('duplex', TType.BYTE, 8)
            oprot.writeByte(self.duplex)
            oprot.writeFieldEnd()
        if self.displayName != None:
            oprot.writeFieldBegin('displayName', TType.STRING, 9)
            oprot.writeString(self.displayName)
            oprot.writeFieldEnd()
        if self.macaddr != None:
            oprot.writeFieldBegin('macaddr', TType.LIST, 10)
            oprot.writeListBegin(TType.BYTE, len(self.macaddr))
            for iter12 in self.macaddr:
                oprot.writeByte(iter12)

            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.descr != None:
            oprot.writeFieldBegin('descr', TType.STRING, 11)
            oprot.writeString(self.descr)
            oprot.writeFieldEnd()
        if self.ipRedirect != None:
            oprot.writeFieldBegin('ipRedirect', TType.I32, 12)
            oprot.writeI32(self.ipRedirect)
            oprot.writeFieldEnd()
        if self.ipUnreachable != None:
            oprot.writeFieldBegin('ipUnreachable', TType.I32, 13)
            oprot.writeI32(self.ipUnreachable)
            oprot.writeFieldEnd()
        if self.ipProxyArp != None:
            oprot.writeFieldBegin('ipProxyArp', TType.I32, 14)
            oprot.writeI32(self.ipProxyArp)
            oprot.writeFieldEnd()
        if self.ipUnicastReversePath != None:
            oprot.writeFieldBegin('ipUnicastReversePath', TType.I32, 15)
            oprot.writeI32(self.ipUnicastReversePath)
            oprot.writeFieldEnd()
        if self.ipHelperAddr != None:
            oprot.writeFieldBegin('ipHelperAddr', TType.LIST, 16)
            oprot.writeListBegin(TType.STRUCT, len(self.ipHelperAddr))
            for iter13 in self.ipHelperAddr:
                iter13.write(oprot)

            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.speedIDL != None:
            oprot.writeFieldBegin('speedIDL', TType.STRUCT, 17)
            self.speedIDL.write(oprot)
            oprot.writeFieldEnd()
        if self.duplexIDL != None:
            oprot.writeFieldBegin('duplexIDL', TType.STRUCT, 18)
            self.duplexIDL.write(oprot)
            oprot.writeFieldEnd()
        if self.autoNegIDL != None:
            oprot.writeFieldBegin('autoNegIDL', TType.STRUCT, 19)
            self.autoNegIDL.write(oprot)
            oprot.writeFieldEnd()
        if self.fcIDL != None:
            oprot.writeFieldBegin('fcIDL', TType.STRUCT, 20)
            self.fcIDL.write(oprot)
            oprot.writeFieldEnd()
        if self.fwdClassID != None:
            oprot.writeFieldBegin('fwdClassID', TType.I32, 21)
            oprot.writeI32(self.fwdClassID)
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




class InterfaceStatusIDL(object):
    """
      Snapshot of dynamic status, retrieved on demand
    
      Attributes:
       - link
       - lineproto
      """

    thrift_spec = (None, (1,
      TType.I32,
      'link',
      None,
      None), (2,
      TType.I32,
      'lineproto',
      None,
      None))

    def __init__(self, link = None, lineproto = None):
        self.link = link
        self.lineproto = lineproto



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
                    self.link = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.lineproto = iprot.readI32()
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
        oprot.writeStructBegin('InterfaceStatusIDL')
        if self.link != None:
            oprot.writeFieldBegin('link', TType.I32, 1)
            oprot.writeI32(self.link)
            oprot.writeFieldEnd()
        if self.lineproto != None:
            oprot.writeFieldBegin('lineproto', TType.I32, 2)
            oprot.writeI32(self.lineproto)
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




class InterfaceStatisticsIDL(object):
    """
    Attributes:
     - retcode
     - stats
    """

    thrift_spec = (None, (1,
      TType.I32,
      'retcode',
      None,
      None), (2,
      TType.I64,
      'stats',
      None,
      None))

    def __init__(self, retcode = None, stats = None):
        self.retcode = retcode
        self.stats = stats



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
                    self.retcode = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.stats = iprot.readI64()
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
        oprot.writeStructBegin('InterfaceStatisticsIDL')
        if self.retcode != None:
            oprot.writeFieldBegin('retcode', TType.I32, 1)
            oprot.writeI32(self.retcode)
            oprot.writeFieldEnd()
        if self.stats != None:
            oprot.writeFieldBegin('stats', TType.I64, 2)
            oprot.writeI64(self.stats)
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




class InterfaceVlanIDL(object):
    """
    Attributes:
     - encapType
     - vlanTag1
     - vlanTag2
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'encapType',
      None,
      None),
     (2,
      TType.I32,
      'vlanTag1',
      None,
      None),
     (3,
      TType.I32,
      'vlanTag2',
      None,
      None))

    def __init__(self, encapType = None, vlanTag1 = None, vlanTag2 = None):
        self.encapType = encapType
        self.vlanTag1 = vlanTag1
        self.vlanTag2 = vlanTag2



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
                    self.encapType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.vlanTag1 = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.vlanTag2 = iprot.readI32()
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
        oprot.writeStructBegin('InterfaceVlanIDL')
        if self.encapType != None:
            oprot.writeFieldBegin('encapType', TType.I32, 1)
            oprot.writeI32(self.encapType)
            oprot.writeFieldEnd()
        if self.vlanTag1 != None:
            oprot.writeFieldBegin('vlanTag1', TType.I32, 2)
            oprot.writeI32(self.vlanTag1)
            oprot.writeFieldEnd()
        if self.vlanTag2 != None:
            oprot.writeFieldBegin('vlanTag2', TType.I32, 3)
            oprot.writeI32(self.vlanTag2)
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




class PChannel_MemberIDL(object):
    """
    Attributes:
     - xosHandle
    """

    thrift_spec = (None, (1,
      TType.I64,
      'xosHandle',
      None,
      None))

    def __init__(self, xosHandle = None):
        self.xosHandle = xosHandle



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
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()

        iprot.readStructEnd()



    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return 
        oprot.writeStructBegin('PChannel_MemberIDL')
        if self.xosHandle != None:
            oprot.writeFieldBegin('xosHandle', TType.I64, 1)
            oprot.writeI64(self.xosHandle)
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
# 2015.02.05 17:22:06 IST
