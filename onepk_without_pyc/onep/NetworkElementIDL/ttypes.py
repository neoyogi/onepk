# 2015.02.05 17:21:48 IST
from thrift.Thrift import *
import Shared.ttypes
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
    from thrift.protocol import fastbinary
except:
    fastbinary = None

class ElementPropertyIDL(object):
    """
      If Successfully authenticated and connected to NetworkElement,
      A session handle should be assigned and along with other info
      retrieved from Network Element.  Let's do it at one round trip
      as much info on hard property as we can.
    
      Attributes:
       - sessionHandle
       - processor
       - serialNo
       - platform
       - sysDescr
       - neLogLevel
       - versionId
       - udi
       - sysObjectId
      """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionHandle',
      None,
      None),
     (2,
      TType.STRING,
      'processor',
      None,
      None),
     (3,
      TType.STRING,
      'serialNo',
      None,
      None),
     (4,
      TType.STRING,
      'platform',
      None,
      None),
     (5,
      TType.STRING,
      'sysDescr',
      None,
      None),
     (6,
      TType.I32,
      'neLogLevel',
      None,
      None),
     (7,
      TType.STRING,
      'versionId',
      None,
      None),
     (8,
      TType.STRING,
      'udi',
      None,
      None),
     (9,
      TType.STRING,
      'sysObjectId',
      None,
      None))

    def __init__(self, sessionHandle = None, processor = None, serialNo = None, platform = None, sysDescr = None, neLogLevel = None, versionId = None, udi = None, sysObjectId = None):
        self.sessionHandle = sessionHandle
        self.processor = processor
        self.serialNo = serialNo
        self.platform = platform
        self.sysDescr = sysDescr
        self.neLogLevel = neLogLevel
        self.versionId = versionId
        self.udi = udi
        self.sysObjectId = sysObjectId



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
                if ftype == TType.STRING:
                    self.processor = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.serialNo = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.platform = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.sysDescr = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I32:
                    self.neLogLevel = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.STRING:
                    self.versionId = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.STRING:
                    self.udi = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.STRING:
                    self.sysObjectId = iprot.readString()
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
        oprot.writeStructBegin('ElementPropertyIDL')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.processor != None:
            oprot.writeFieldBegin('processor', TType.STRING, 2)
            oprot.writeString(self.processor)
            oprot.writeFieldEnd()
        if self.serialNo != None:
            oprot.writeFieldBegin('serialNo', TType.STRING, 3)
            oprot.writeString(self.serialNo)
            oprot.writeFieldEnd()
        if self.platform != None:
            oprot.writeFieldBegin('platform', TType.STRING, 4)
            oprot.writeString(self.platform)
            oprot.writeFieldEnd()
        if self.sysDescr != None:
            oprot.writeFieldBegin('sysDescr', TType.STRING, 5)
            oprot.writeString(self.sysDescr)
            oprot.writeFieldEnd()
        if self.neLogLevel != None:
            oprot.writeFieldBegin('neLogLevel', TType.I32, 6)
            oprot.writeI32(self.neLogLevel)
            oprot.writeFieldEnd()
        if self.versionId != None:
            oprot.writeFieldBegin('versionId', TType.STRING, 7)
            oprot.writeString(self.versionId)
            oprot.writeFieldEnd()
        if self.udi != None:
            oprot.writeFieldBegin('udi', TType.STRING, 8)
            oprot.writeString(self.udi)
            oprot.writeFieldEnd()
        if self.sysObjectId != None:
            oprot.writeFieldBegin('sysObjectId', TType.STRING, 9)
            oprot.writeString(self.sysObjectId)
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




class ElementFruIDL(object):
    """
      Element FRU property information
    
      Attributes:
       - slot
       - alarm_type
       - product_id
       - serial_no
       - part_no
       - sw_version
       - fw_version
       - hw_version
      """

    thrift_spec = (None,
     (1,
      TType.I16,
      'slot',
      None,
      -1),
     (2,
      TType.STRING,
      'alarm_type',
      None,
      ''),
     (3,
      TType.STRING,
      'product_id',
      None,
      ''),
     (4,
      TType.STRING,
      'serial_no',
      None,
      ''),
     (5,
      TType.STRING,
      'part_no',
      None,
      ''),
     (6,
      TType.STRING,
      'sw_version',
      None,
      ''),
     (7,
      TType.STRING,
      'fw_version',
      None,
      ''),
     (8,
      TType.STRING,
      'hw_version',
      None,
      ''))

    def __init__(self, slot = thrift_spec[1][4], alarm_type = thrift_spec[2][4], product_id = thrift_spec[3][4], serial_no = thrift_spec[4][4], part_no = thrift_spec[5][4], sw_version = thrift_spec[6][4], fw_version = thrift_spec[7][4], hw_version = thrift_spec[8][4]):
        self.slot = slot
        self.alarm_type = alarm_type
        self.product_id = product_id
        self.serial_no = serial_no
        self.part_no = part_no
        self.sw_version = sw_version
        self.fw_version = fw_version
        self.hw_version = hw_version



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
                    self.slot = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.alarm_type = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.product_id = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.serial_no = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.part_no = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRING:
                    self.sw_version = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.STRING:
                    self.fw_version = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.STRING:
                    self.hw_version = iprot.readString()
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
        oprot.writeStructBegin('ElementFruIDL')
        if self.slot != None:
            oprot.writeFieldBegin('slot', TType.I16, 1)
            oprot.writeI16(self.slot)
            oprot.writeFieldEnd()
        if self.alarm_type != None:
            oprot.writeFieldBegin('alarm_type', TType.STRING, 2)
            oprot.writeString(self.alarm_type)
            oprot.writeFieldEnd()
        if self.product_id != None:
            oprot.writeFieldBegin('product_id', TType.STRING, 3)
            oprot.writeString(self.product_id)
            oprot.writeFieldEnd()
        if self.serial_no != None:
            oprot.writeFieldBegin('serial_no', TType.STRING, 4)
            oprot.writeString(self.serial_no)
            oprot.writeFieldEnd()
        if self.part_no != None:
            oprot.writeFieldBegin('part_no', TType.STRING, 5)
            oprot.writeString(self.part_no)
            oprot.writeFieldEnd()
        if self.sw_version != None:
            oprot.writeFieldBegin('sw_version', TType.STRING, 6)
            oprot.writeString(self.sw_version)
            oprot.writeFieldEnd()
        if self.fw_version != None:
            oprot.writeFieldBegin('fw_version', TType.STRING, 7)
            oprot.writeString(self.fw_version)
            oprot.writeFieldEnd()
        if self.hw_version != None:
            oprot.writeFieldBegin('hw_version', TType.STRING, 8)
            oprot.writeString(self.hw_version)
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




class InterfaceCreateDeleteFilterIDL(object):
    """
      InterfaceCreateDeleteFilterIDL
    
    
      Attributes:
       - interfaceType
       - interfaceXOSHandle
       - includeSubinterfaces
       - encap
      """

    thrift_spec = (None,
     (1,
      TType.I32,
      'interfaceType',
      None,
      None),
     (2,
      TType.I64,
      'interfaceXOSHandle',
      None,
      None),
     (3,
      TType.I32,
      'includeSubinterfaces',
      None,
      None),
     (4,
      TType.I32,
      'encap',
      None,
      None))

    def __init__(self, interfaceType = None, interfaceXOSHandle = None, includeSubinterfaces = None, encap = None):
        self.interfaceType = interfaceType
        self.interfaceXOSHandle = interfaceXOSHandle
        self.includeSubinterfaces = includeSubinterfaces
        self.encap = encap



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
                    self.interfaceType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.interfaceXOSHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.includeSubinterfaces = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.encap = iprot.readI32()
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
        oprot.writeStructBegin('InterfaceCreateDeleteFilterIDL')
        if self.interfaceType != None:
            oprot.writeFieldBegin('interfaceType', TType.I32, 1)
            oprot.writeI32(self.interfaceType)
            oprot.writeFieldEnd()
        if self.interfaceXOSHandle != None:
            oprot.writeFieldBegin('interfaceXOSHandle', TType.I64, 2)
            oprot.writeI64(self.interfaceXOSHandle)
            oprot.writeFieldEnd()
        if self.includeSubinterfaces != None:
            oprot.writeFieldBegin('includeSubinterfaces', TType.I32, 3)
            oprot.writeI32(self.includeSubinterfaces)
            oprot.writeFieldEnd()
        if self.encap != None:
            oprot.writeFieldBegin('encap', TType.I32, 4)
            oprot.writeI32(self.encap)
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




class InterfaceCTXEnableDisableFilterIDL(object):
    """
      InterfaceCTXEnableDisableIDL
    
    
      Attributes:
       - interfaceType
       - interfaceXOSHandle
       - tag
      """

    thrift_spec = (None,
     (1,
      TType.I32,
      'interfaceType',
      None,
      None),
     (2,
      TType.I64,
      'interfaceXOSHandle',
      None,
      None),
     (3,
      TType.I32,
      'tag',
      None,
      None))

    def __init__(self, interfaceType = None, interfaceXOSHandle = None, tag = None):
        self.interfaceType = interfaceType
        self.interfaceXOSHandle = interfaceXOSHandle
        self.tag = tag



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
                    self.interfaceType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.interfaceXOSHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.tag = iprot.readI32()
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
        oprot.writeStructBegin('InterfaceCTXEnableDisableFilterIDL')
        if self.interfaceType != None:
            oprot.writeFieldBegin('interfaceType', TType.I32, 1)
            oprot.writeI32(self.interfaceType)
            oprot.writeFieldEnd()
        if self.interfaceXOSHandle != None:
            oprot.writeFieldBegin('interfaceXOSHandle', TType.I64, 2)
            oprot.writeI64(self.interfaceXOSHandle)
            oprot.writeFieldEnd()
        if self.tag != None:
            oprot.writeFieldBegin('tag', TType.I32, 3)
            oprot.writeI32(self.tag)
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




class HsrpInstanceFilterIDL(object):
    """
      HsrpInstanceFilterIDL
    
      Attributes:
       - groupid
       - family
       - xosHandle
       - priority
      """

    thrift_spec = (None,
     (1,
      TType.I32,
      'groupid',
      None,
      None),
     (2,
      TType.I32,
      'family',
      None,
      None),
     (3,
      TType.I64,
      'xosHandle',
      None,
      None),
     (4,
      TType.I32,
      'priority',
      None,
      None))

    def __init__(self, groupid = None, family = None, xosHandle = None, priority = None):
        self.groupid = groupid
        self.family = family
        self.xosHandle = xosHandle
        self.priority = priority



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
                    self.groupid = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.family = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I64:
                    self.xosHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.priority = iprot.readI32()
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
        oprot.writeStructBegin('HsrpInstanceFilterIDL')
        if self.groupid != None:
            oprot.writeFieldBegin('groupid', TType.I32, 1)
            oprot.writeI32(self.groupid)
            oprot.writeFieldEnd()
        if self.family != None:
            oprot.writeFieldBegin('family', TType.I32, 2)
            oprot.writeI32(self.family)
            oprot.writeFieldEnd()
        if self.xosHandle != None:
            oprot.writeFieldBegin('xosHandle', TType.I64, 3)
            oprot.writeI64(self.xosHandle)
            oprot.writeFieldEnd()
        if self.priority != None:
            oprot.writeFieldBegin('priority', TType.I32, 4)
            oprot.writeI32(self.priority)
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




class BDFilterIDL(object):
    """
      BDFilterIDL
    
      Attributes:
       - isset
       - cr_del_enable
       - membership_enable
       - id
      """

    thrift_spec = (None,
     (1,
      TType.I32,
      'isset',
      None,
      None),
     (2,
      TType.I32,
      'cr_del_enable',
      None,
      None),
     (3,
      TType.I32,
      'membership_enable',
      None,
      None),
     (4,
      TType.I32,
      'id',
      None,
      None))

    def __init__(self, isset = None, cr_del_enable = None, membership_enable = None, id = None):
        self.isset = isset
        self.cr_del_enable = cr_del_enable
        self.membership_enable = membership_enable
        self.id = id



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
                    self.isset = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.cr_del_enable = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.membership_enable = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.id = iprot.readI32()
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
        oprot.writeStructBegin('BDFilterIDL')
        if self.isset != None:
            oprot.writeFieldBegin('isset', TType.I32, 1)
            oprot.writeI32(self.isset)
            oprot.writeFieldEnd()
        if self.cr_del_enable != None:
            oprot.writeFieldBegin('cr_del_enable', TType.I32, 2)
            oprot.writeI32(self.cr_del_enable)
            oprot.writeFieldEnd()
        if self.membership_enable != None:
            oprot.writeFieldBegin('membership_enable', TType.I32, 3)
            oprot.writeI32(self.membership_enable)
            oprot.writeFieldEnd()
        if self.id != None:
            oprot.writeFieldBegin('id', TType.I32, 4)
            oprot.writeI32(self.id)
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




class PortChannelFilterIDL(object):
    """
      PortChannelFilterIDL
    
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
        oprot.writeStructBegin('PortChannelFilterIDL')
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




class VmCredentialIDL(object):
    """
      VmCredentialIDL
    
    
      Attributes:
       - credentials
      """

    thrift_spec = (None, (1,
      TType.LIST,
      'credentials',
      (TType.BYTE, None),
      None))

    def __init__(self, credentials = None):
        self.credentials = credentials



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
                    self.credentials = []
                    (_etype3, _size0,) = iprot.readListBegin()
                    for _i4 in xrange(_size0):
                        _elem5 = iprot.readByte()
                        self.credentials.append(_elem5)

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
        oprot.writeStructBegin('VmCredentialIDL')
        if self.credentials != None:
            oprot.writeFieldBegin('credentials', TType.LIST, 1)
            oprot.writeListBegin(TType.BYTE, len(self.credentials))
            for iter6 in self.credentials:
                oprot.writeByte(iter6)

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
# 2015.02.05 17:21:49 IST
