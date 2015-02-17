# 2015.02.05 17:19:51 IST
from thrift.Thrift import *
import Shared.ttypes
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
    from thrift.protocol import fastbinary
except:
    fastbinary = None

class MarkParam_IDL(object):
    """
      Packet Marking Parameters
    
      Attributes:
       - type
       - value
      """

    thrift_spec = (None, (1,
      TType.I32,
      'type',
      None,
      None), (2,
      TType.I32,
      'value',
      None,
      None))

    def __init__(self, type = None, value = None):
        self.type = type
        self.value = value



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
                    self.value = iprot.readI32()
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
        oprot.writeStructBegin('MarkParam_IDL')
        if self.type != None:
            oprot.writeFieldBegin('type', TType.I32, 1)
            oprot.writeI32(self.type)
            oprot.writeFieldEnd()
        if self.value != None:
            oprot.writeFieldBegin('value', TType.I32, 2)
            oprot.writeI32(self.value)
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




class PoliceParam_IDL(object):
    """
      Policing Parameters
    
      Attributes:
       - rateUnits
       - burstUnits
       - cir
       - pir
       - cbs
       - ebs
       - conformAction
       - conformValue
       - exceedAction
       - exceedValue
       - violateAction
       - violateValue
       - conformColor
       - exceedColor
      """

    thrift_spec = (None,
     (1,
      TType.I32,
      'rateUnits',
      None,
      None),
     (2,
      TType.I32,
      'burstUnits',
      None,
      None),
     (3,
      TType.I64,
      'cir',
      None,
      None),
     (4,
      TType.I64,
      'pir',
      None,
      None),
     (5,
      TType.I64,
      'cbs',
      None,
      None),
     (6,
      TType.I64,
      'ebs',
      None,
      None),
     (7,
      TType.I32,
      'conformAction',
      None,
      None),
     (8,
      TType.I32,
      'conformValue',
      None,
      None),
     (9,
      TType.I32,
      'exceedAction',
      None,
      None),
     (10,
      TType.I32,
      'exceedValue',
      None,
      None),
     (11,
      TType.I32,
      'violateAction',
      None,
      None),
     (12,
      TType.I32,
      'violateValue',
      None,
      None),
     (13,
      TType.I32,
      'conformColor',
      None,
      None),
     (14,
      TType.I32,
      'exceedColor',
      None,
      None))

    def __init__(self, rateUnits = None, burstUnits = None, cir = None, pir = None, cbs = None, ebs = None, conformAction = None, conformValue = None, exceedAction = None, exceedValue = None, violateAction = None, violateValue = None, conformColor = None, exceedColor = None):
        self.rateUnits = rateUnits
        self.burstUnits = burstUnits
        self.cir = cir
        self.pir = pir
        self.cbs = cbs
        self.ebs = ebs
        self.conformAction = conformAction
        self.conformValue = conformValue
        self.exceedAction = exceedAction
        self.exceedValue = exceedValue
        self.violateAction = violateAction
        self.violateValue = violateValue
        self.conformColor = conformColor
        self.exceedColor = exceedColor



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
                    self.rateUnits = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.burstUnits = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I64:
                    self.cir = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I64:
                    self.pir = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I64:
                    self.cbs = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I64:
                    self.ebs = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I32:
                    self.conformAction = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.I32:
                    self.conformValue = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.I32:
                    self.exceedAction = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.I32:
                    self.exceedValue = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.I32:
                    self.violateAction = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 12:
                if ftype == TType.I32:
                    self.violateValue = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 13:
                if ftype == TType.I32:
                    self.conformColor = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 14:
                if ftype == TType.I32:
                    self.exceedColor = iprot.readI32()
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
        oprot.writeStructBegin('PoliceParam_IDL')
        if self.rateUnits != None:
            oprot.writeFieldBegin('rateUnits', TType.I32, 1)
            oprot.writeI32(self.rateUnits)
            oprot.writeFieldEnd()
        if self.burstUnits != None:
            oprot.writeFieldBegin('burstUnits', TType.I32, 2)
            oprot.writeI32(self.burstUnits)
            oprot.writeFieldEnd()
        if self.cir != None:
            oprot.writeFieldBegin('cir', TType.I64, 3)
            oprot.writeI64(self.cir)
            oprot.writeFieldEnd()
        if self.pir != None:
            oprot.writeFieldBegin('pir', TType.I64, 4)
            oprot.writeI64(self.pir)
            oprot.writeFieldEnd()
        if self.cbs != None:
            oprot.writeFieldBegin('cbs', TType.I64, 5)
            oprot.writeI64(self.cbs)
            oprot.writeFieldEnd()
        if self.ebs != None:
            oprot.writeFieldBegin('ebs', TType.I64, 6)
            oprot.writeI64(self.ebs)
            oprot.writeFieldEnd()
        if self.conformAction != None:
            oprot.writeFieldBegin('conformAction', TType.I32, 7)
            oprot.writeI32(self.conformAction)
            oprot.writeFieldEnd()
        if self.conformValue != None:
            oprot.writeFieldBegin('conformValue', TType.I32, 8)
            oprot.writeI32(self.conformValue)
            oprot.writeFieldEnd()
        if self.exceedAction != None:
            oprot.writeFieldBegin('exceedAction', TType.I32, 9)
            oprot.writeI32(self.exceedAction)
            oprot.writeFieldEnd()
        if self.exceedValue != None:
            oprot.writeFieldBegin('exceedValue', TType.I32, 10)
            oprot.writeI32(self.exceedValue)
            oprot.writeFieldEnd()
        if self.violateAction != None:
            oprot.writeFieldBegin('violateAction', TType.I32, 11)
            oprot.writeI32(self.violateAction)
            oprot.writeFieldEnd()
        if self.violateValue != None:
            oprot.writeFieldBegin('violateValue', TType.I32, 12)
            oprot.writeI32(self.violateValue)
            oprot.writeFieldEnd()
        if self.conformColor != None:
            oprot.writeFieldBegin('conformColor', TType.I32, 13)
            oprot.writeI32(self.conformColor)
            oprot.writeFieldEnd()
        if self.exceedColor != None:
            oprot.writeFieldBegin('exceedColor', TType.I32, 14)
            oprot.writeI32(self.exceedColor)
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




class MacAddress_IDL(object):
    """
      MAC Address
    
      Attributes:
       - type
       - addr
      """

    thrift_spec = (None, (1,
      TType.I16,
      'type',
      None,
      None), (2,
      TType.LIST,
      'addr',
      (TType.BYTE, None),
      [1,
       2,
       3,
       4,
       5,
       6]))

    def __init__(self, type = None, addr = thrift_spec[2][4]):
        self.type = type
        if addr is self.thrift_spec[2][4]:
            addr = [1,
             2,
             3,
             4,
             5,
             6]
        self.addr = addr



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
                    self.type = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.addr = []
                    (_etype3, _size0,) = iprot.readListBegin()
                    for _i4 in xrange(_size0):
                        _elem5 = iprot.readByte()
                        self.addr.append(_elem5)

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
        oprot.writeStructBegin('MacAddress_IDL')
        if self.type != None:
            oprot.writeFieldBegin('type', TType.I16, 1)
            oprot.writeI16(self.type)
            oprot.writeFieldEnd()
        if self.addr != None:
            oprot.writeFieldBegin('addr', TType.LIST, 2)
            oprot.writeListBegin(TType.BYTE, len(self.addr))
            for iter6 in self.addr:
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




class ShapeParam_IDL(object):
    """
      Shape parameters
    
      Attributes:
       - type
       - rateUnits
       - burstUnits
       - cir
       - cbs
       - ebs
      """

    thrift_spec = (None,
     (1,
      TType.I32,
      'type',
      None,
      None),
     (2,
      TType.I32,
      'rateUnits',
      None,
      None),
     (3,
      TType.I32,
      'burstUnits',
      None,
      None),
     (4,
      TType.I64,
      'cir',
      None,
      None),
     (5,
      TType.I64,
      'cbs',
      None,
      None),
     (6,
      TType.I64,
      'ebs',
      None,
      None))

    def __init__(self, type = None, rateUnits = None, burstUnits = None, cir = None, cbs = None, ebs = None):
        self.type = type
        self.rateUnits = rateUnits
        self.burstUnits = burstUnits
        self.cir = cir
        self.cbs = cbs
        self.ebs = ebs



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
                    self.rateUnits = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.burstUnits = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I64:
                    self.cir = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I64:
                    self.cbs = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I64:
                    self.ebs = iprot.readI64()
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
        oprot.writeStructBegin('ShapeParam_IDL')
        if self.type != None:
            oprot.writeFieldBegin('type', TType.I32, 1)
            oprot.writeI32(self.type)
            oprot.writeFieldEnd()
        if self.rateUnits != None:
            oprot.writeFieldBegin('rateUnits', TType.I32, 2)
            oprot.writeI32(self.rateUnits)
            oprot.writeFieldEnd()
        if self.burstUnits != None:
            oprot.writeFieldBegin('burstUnits', TType.I32, 3)
            oprot.writeI32(self.burstUnits)
            oprot.writeFieldEnd()
        if self.cir != None:
            oprot.writeFieldBegin('cir', TType.I64, 4)
            oprot.writeI64(self.cir)
            oprot.writeFieldEnd()
        if self.cbs != None:
            oprot.writeFieldBegin('cbs', TType.I64, 5)
            oprot.writeI64(self.cbs)
            oprot.writeFieldEnd()
        if self.ebs != None:
            oprot.writeFieldBegin('ebs', TType.I64, 6)
            oprot.writeI64(self.ebs)
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




class PriorityQueueParam_IDL(object):
    """
      Priority Queue Parameters
    
      Attributes:
       - bandwidth
       - bandwidthUnits
       - level
       - burst
       - queueSize
       - queueSizeUnits
      """

    thrift_spec = (None,
     (1,
      TType.I64,
      'bandwidth',
      None,
      None),
     (2,
      TType.I32,
      'bandwidthUnits',
      None,
      None),
     (3,
      TType.I32,
      'level',
      None,
      None),
     (4,
      TType.I64,
      'burst',
      None,
      None),
     (5,
      TType.I32,
      'queueSize',
      None,
      None),
     (6,
      TType.I32,
      'queueSizeUnits',
      None,
      None))

    def __init__(self, bandwidth = None, bandwidthUnits = None, level = None, burst = None, queueSize = None, queueSizeUnits = None):
        self.bandwidth = bandwidth
        self.bandwidthUnits = bandwidthUnits
        self.level = level
        self.burst = burst
        self.queueSize = queueSize
        self.queueSizeUnits = queueSizeUnits



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
                    self.bandwidth = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.bandwidthUnits = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.level = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I64:
                    self.burst = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.queueSize = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I32:
                    self.queueSizeUnits = iprot.readI32()
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
        oprot.writeStructBegin('PriorityQueueParam_IDL')
        if self.bandwidth != None:
            oprot.writeFieldBegin('bandwidth', TType.I64, 1)
            oprot.writeI64(self.bandwidth)
            oprot.writeFieldEnd()
        if self.bandwidthUnits != None:
            oprot.writeFieldBegin('bandwidthUnits', TType.I32, 2)
            oprot.writeI32(self.bandwidthUnits)
            oprot.writeFieldEnd()
        if self.level != None:
            oprot.writeFieldBegin('level', TType.I32, 3)
            oprot.writeI32(self.level)
            oprot.writeFieldEnd()
        if self.burst != None:
            oprot.writeFieldBegin('burst', TType.I64, 4)
            oprot.writeI64(self.burst)
            oprot.writeFieldEnd()
        if self.queueSize != None:
            oprot.writeFieldBegin('queueSize', TType.I32, 5)
            oprot.writeI32(self.queueSize)
            oprot.writeFieldEnd()
        if self.queueSizeUnits != None:
            oprot.writeFieldBegin('queueSizeUnits', TType.I32, 6)
            oprot.writeI32(self.queueSizeUnits)
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




class ClassBasedQueueParam_IDL(object):
    """
      Class-based Queue Parameters
    
      Attributes:
       - bandwidth
       - bandwidthUnits
       - queueSize
       - queueSizeUnits
      """

    thrift_spec = (None,
     (1,
      TType.I64,
      'bandwidth',
      None,
      None),
     (2,
      TType.I32,
      'bandwidthUnits',
      None,
      None),
     (3,
      TType.I32,
      'queueSize',
      None,
      None),
     (4,
      TType.I32,
      'queueSizeUnits',
      None,
      None))

    def __init__(self, bandwidth = None, bandwidthUnits = None, queueSize = None, queueSizeUnits = None):
        self.bandwidth = bandwidth
        self.bandwidthUnits = bandwidthUnits
        self.queueSize = queueSize
        self.queueSizeUnits = queueSizeUnits



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
                    self.bandwidth = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.bandwidthUnits = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.queueSize = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.queueSizeUnits = iprot.readI32()
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
        oprot.writeStructBegin('ClassBasedQueueParam_IDL')
        if self.bandwidth != None:
            oprot.writeFieldBegin('bandwidth', TType.I64, 1)
            oprot.writeI64(self.bandwidth)
            oprot.writeFieldEnd()
        if self.bandwidthUnits != None:
            oprot.writeFieldBegin('bandwidthUnits', TType.I32, 2)
            oprot.writeI32(self.bandwidthUnits)
            oprot.writeFieldEnd()
        if self.queueSize != None:
            oprot.writeFieldBegin('queueSize', TType.I32, 3)
            oprot.writeI32(self.queueSize)
            oprot.writeFieldEnd()
        if self.queueSizeUnits != None:
            oprot.writeFieldBegin('queueSizeUnits', TType.I32, 4)
            oprot.writeI32(self.queueSizeUnits)
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




class FairQueueParam_IDL(object):
    """
      Fair Queue Parameters
    
      Attributes:
       - numFlowQueues
       - queueSize
       - queueSizeUnits
      """

    thrift_spec = (None,
     (1,
      TType.I32,
      'numFlowQueues',
      None,
      None),
     (2,
      TType.I32,
      'queueSize',
      None,
      None),
     (3,
      TType.I32,
      'queueSizeUnits',
      None,
      None))

    def __init__(self, numFlowQueues = None, queueSize = None, queueSizeUnits = None):
        self.numFlowQueues = numFlowQueues
        self.queueSize = queueSize
        self.queueSizeUnits = queueSizeUnits



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
                    self.numFlowQueues = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.queueSize = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.queueSizeUnits = iprot.readI32()
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
        oprot.writeStructBegin('FairQueueParam_IDL')
        if self.numFlowQueues != None:
            oprot.writeFieldBegin('numFlowQueues', TType.I32, 1)
            oprot.writeI32(self.numFlowQueues)
            oprot.writeFieldEnd()
        if self.queueSize != None:
            oprot.writeFieldBegin('queueSize', TType.I32, 2)
            oprot.writeI32(self.queueSize)
            oprot.writeFieldEnd()
        if self.queueSizeUnits != None:
            oprot.writeFieldBegin('queueSizeUnits', TType.I32, 3)
            oprot.writeI32(self.queueSizeUnits)
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




class QueueLimitParam_IDL(object):
    """
      Queue Limit Parameters
    
      Attributes:
       - queueSize
       - queueSizeUnits
      """

    thrift_spec = (None, (1,
      TType.I32,
      'queueSize',
      None,
      None), (2,
      TType.I32,
      'queueSizeUnits',
      None,
      None))

    def __init__(self, queueSize = None, queueSizeUnits = None):
        self.queueSize = queueSize
        self.queueSizeUnits = queueSizeUnits



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
                    self.queueSize = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.queueSizeUnits = iprot.readI32()
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
        oprot.writeStructBegin('QueueLimitParam_IDL')
        if self.queueSize != None:
            oprot.writeFieldBegin('queueSize', TType.I32, 1)
            oprot.writeI32(self.queueSize)
            oprot.writeFieldEnd()
        if self.queueSizeUnits != None:
            oprot.writeFieldBegin('queueSizeUnits', TType.I32, 2)
            oprot.writeI32(self.queueSizeUnits)
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




class RtpPort_IDL(object):
    """
      RTP Port
    
      Attributes:
       - port1
       - port2
      """

    thrift_spec = (None, (1,
      TType.I32,
      'port1',
      None,
      None), (2,
      TType.I32,
      'port2',
      None,
      None))

    def __init__(self, port1 = None, port2 = None):
        self.port1 = port1
        self.port2 = port2



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
                    self.port1 = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.port2 = iprot.readI32()
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
        oprot.writeStructBegin('RtpPort_IDL')
        if self.port1 != None:
            oprot.writeFieldBegin('port1', TType.I32, 1)
            oprot.writeI32(self.port1)
            oprot.writeFieldEnd()
        if self.port2 != None:
            oprot.writeFieldBegin('port2', TType.I32, 2)
            oprot.writeI32(self.port2)
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




class Class_IDL(object):
    """
      Class
    
      Attributes:
       - classOper
       - numFilters
       - numActions
      """

    thrift_spec = (None,
     (1,
      TType.I32,
      'classOper',
      None,
      None),
     (2,
      TType.I32,
      'numFilters',
      None,
      None),
     (3,
      TType.I32,
      'numActions',
      None,
      None))

    def __init__(self, classOper = None, numFilters = None, numActions = None):
        self.classOper = classOper
        self.numFilters = numFilters
        self.numActions = numActions



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
                    self.classOper = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.numFilters = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.numActions = iprot.readI32()
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
        oprot.writeStructBegin('Class_IDL')
        if self.classOper != None:
            oprot.writeFieldBegin('classOper', TType.I32, 1)
            oprot.writeI32(self.classOper)
            oprot.writeFieldEnd()
        if self.numFilters != None:
            oprot.writeFieldBegin('numFilters', TType.I32, 2)
            oprot.writeI32(self.numFilters)
            oprot.writeFieldEnd()
        if self.numActions != None:
            oprot.writeFieldBegin('numActions', TType.I32, 3)
            oprot.writeI32(self.numActions)
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




class FilterCapabilityIDL(object):
    """
      Filter Capability
    
      Attributes:
       - maxFilters
       - maxFilterAcl
       - maxFilterDscp
       - maxFilterMplsExp
       - maxFilterMacAddress
       - maxFilterVlan
       - maxFilterL2Cos
       - maxFilterRtpPort
       - maxFilterPktLen
       - maxFilterProtocol
       - maxFilterPrecedence
       - maxFilterFrDlci
       - maxFilterFrDe
      """

    thrift_spec = (None,
     (1,
      TType.I16,
      'maxFilters',
      None,
      None),
     (2,
      TType.I16,
      'maxFilterAcl',
      None,
      None),
     (3,
      TType.I16,
      'maxFilterDscp',
      None,
      None),
     (4,
      TType.I16,
      'maxFilterMplsExp',
      None,
      None),
     (5,
      TType.I16,
      'maxFilterMacAddress',
      None,
      None),
     (6,
      TType.I16,
      'maxFilterVlan',
      None,
      None),
     (7,
      TType.I16,
      'maxFilterL2Cos',
      None,
      None),
     (8,
      TType.I16,
      'maxFilterRtpPort',
      None,
      None),
     (9,
      TType.I16,
      'maxFilterPktLen',
      None,
      None),
     (10,
      TType.I16,
      'maxFilterProtocol',
      None,
      None),
     (11,
      TType.I16,
      'maxFilterPrecedence',
      None,
      None),
     (12,
      TType.I16,
      'maxFilterFrDlci',
      None,
      None),
     (13,
      TType.I16,
      'maxFilterFrDe',
      None,
      None))

    def __init__(self, maxFilters = None, maxFilterAcl = None, maxFilterDscp = None, maxFilterMplsExp = None, maxFilterMacAddress = None, maxFilterVlan = None, maxFilterL2Cos = None, maxFilterRtpPort = None, maxFilterPktLen = None, maxFilterProtocol = None, maxFilterPrecedence = None, maxFilterFrDlci = None, maxFilterFrDe = None):
        self.maxFilters = maxFilters
        self.maxFilterAcl = maxFilterAcl
        self.maxFilterDscp = maxFilterDscp
        self.maxFilterMplsExp = maxFilterMplsExp
        self.maxFilterMacAddress = maxFilterMacAddress
        self.maxFilterVlan = maxFilterVlan
        self.maxFilterL2Cos = maxFilterL2Cos
        self.maxFilterRtpPort = maxFilterRtpPort
        self.maxFilterPktLen = maxFilterPktLen
        self.maxFilterProtocol = maxFilterProtocol
        self.maxFilterPrecedence = maxFilterPrecedence
        self.maxFilterFrDlci = maxFilterFrDlci
        self.maxFilterFrDe = maxFilterFrDe



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
                    self.maxFilters = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I16:
                    self.maxFilterAcl = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I16:
                    self.maxFilterDscp = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I16:
                    self.maxFilterMplsExp = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I16:
                    self.maxFilterMacAddress = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I16:
                    self.maxFilterVlan = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I16:
                    self.maxFilterL2Cos = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.I16:
                    self.maxFilterRtpPort = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.I16:
                    self.maxFilterPktLen = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.I16:
                    self.maxFilterProtocol = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.I16:
                    self.maxFilterPrecedence = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 12:
                if ftype == TType.I16:
                    self.maxFilterFrDlci = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 13:
                if ftype == TType.I16:
                    self.maxFilterFrDe = iprot.readI16()
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
        oprot.writeStructBegin('FilterCapabilityIDL')
        if self.maxFilters != None:
            oprot.writeFieldBegin('maxFilters', TType.I16, 1)
            oprot.writeI16(self.maxFilters)
            oprot.writeFieldEnd()
        if self.maxFilterAcl != None:
            oprot.writeFieldBegin('maxFilterAcl', TType.I16, 2)
            oprot.writeI16(self.maxFilterAcl)
            oprot.writeFieldEnd()
        if self.maxFilterDscp != None:
            oprot.writeFieldBegin('maxFilterDscp', TType.I16, 3)
            oprot.writeI16(self.maxFilterDscp)
            oprot.writeFieldEnd()
        if self.maxFilterMplsExp != None:
            oprot.writeFieldBegin('maxFilterMplsExp', TType.I16, 4)
            oprot.writeI16(self.maxFilterMplsExp)
            oprot.writeFieldEnd()
        if self.maxFilterMacAddress != None:
            oprot.writeFieldBegin('maxFilterMacAddress', TType.I16, 5)
            oprot.writeI16(self.maxFilterMacAddress)
            oprot.writeFieldEnd()
        if self.maxFilterVlan != None:
            oprot.writeFieldBegin('maxFilterVlan', TType.I16, 6)
            oprot.writeI16(self.maxFilterVlan)
            oprot.writeFieldEnd()
        if self.maxFilterL2Cos != None:
            oprot.writeFieldBegin('maxFilterL2Cos', TType.I16, 7)
            oprot.writeI16(self.maxFilterL2Cos)
            oprot.writeFieldEnd()
        if self.maxFilterRtpPort != None:
            oprot.writeFieldBegin('maxFilterRtpPort', TType.I16, 8)
            oprot.writeI16(self.maxFilterRtpPort)
            oprot.writeFieldEnd()
        if self.maxFilterPktLen != None:
            oprot.writeFieldBegin('maxFilterPktLen', TType.I16, 9)
            oprot.writeI16(self.maxFilterPktLen)
            oprot.writeFieldEnd()
        if self.maxFilterProtocol != None:
            oprot.writeFieldBegin('maxFilterProtocol', TType.I16, 10)
            oprot.writeI16(self.maxFilterProtocol)
            oprot.writeFieldEnd()
        if self.maxFilterPrecedence != None:
            oprot.writeFieldBegin('maxFilterPrecedence', TType.I16, 11)
            oprot.writeI16(self.maxFilterPrecedence)
            oprot.writeFieldEnd()
        if self.maxFilterFrDlci != None:
            oprot.writeFieldBegin('maxFilterFrDlci', TType.I16, 12)
            oprot.writeI16(self.maxFilterFrDlci)
            oprot.writeFieldEnd()
        if self.maxFilterFrDe != None:
            oprot.writeFieldBegin('maxFilterFrDe', TType.I16, 13)
            oprot.writeI16(self.maxFilterFrDe)
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




class ActionCapabilityIDL(object):
    """
      Action Capability
    
      Attributes:
       - maxActions
       - maxActionDrop
       - maxActionMark
       - maxActionPolice
       - maxActionShape
       - maxActionQueue
      """

    thrift_spec = (None,
     (1,
      TType.I16,
      'maxActions',
      None,
      None),
     (2,
      TType.I16,
      'maxActionDrop',
      None,
      None),
     (3,
      TType.I16,
      'maxActionMark',
      None,
      None),
     (4,
      TType.I16,
      'maxActionPolice',
      None,
      None),
     (5,
      TType.I16,
      'maxActionShape',
      None,
      None),
     (6,
      TType.I16,
      'maxActionQueue',
      None,
      None))

    def __init__(self, maxActions = None, maxActionDrop = None, maxActionMark = None, maxActionPolice = None, maxActionShape = None, maxActionQueue = None):
        self.maxActions = maxActions
        self.maxActionDrop = maxActionDrop
        self.maxActionMark = maxActionMark
        self.maxActionPolice = maxActionPolice
        self.maxActionShape = maxActionShape
        self.maxActionQueue = maxActionQueue



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
                    self.maxActions = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I16:
                    self.maxActionDrop = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I16:
                    self.maxActionMark = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I16:
                    self.maxActionPolice = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I16:
                    self.maxActionShape = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I16:
                    self.maxActionQueue = iprot.readI16()
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
        oprot.writeStructBegin('ActionCapabilityIDL')
        if self.maxActions != None:
            oprot.writeFieldBegin('maxActions', TType.I16, 1)
            oprot.writeI16(self.maxActions)
            oprot.writeFieldEnd()
        if self.maxActionDrop != None:
            oprot.writeFieldBegin('maxActionDrop', TType.I16, 2)
            oprot.writeI16(self.maxActionDrop)
            oprot.writeFieldEnd()
        if self.maxActionMark != None:
            oprot.writeFieldBegin('maxActionMark', TType.I16, 3)
            oprot.writeI16(self.maxActionMark)
            oprot.writeFieldEnd()
        if self.maxActionPolice != None:
            oprot.writeFieldBegin('maxActionPolice', TType.I16, 4)
            oprot.writeI16(self.maxActionPolice)
            oprot.writeFieldEnd()
        if self.maxActionShape != None:
            oprot.writeFieldBegin('maxActionShape', TType.I16, 5)
            oprot.writeI16(self.maxActionShape)
            oprot.writeFieldEnd()
        if self.maxActionQueue != None:
            oprot.writeFieldBegin('maxActionQueue', TType.I16, 6)
            oprot.writeI16(self.maxActionQueue)
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




class ProtocolCapabilityIDL(object):
    """
      NBAR Protocol Capability
    
      Attributes:
       - protocolId
       - name
       - fullName
       - subProtocolSupported
      """

    thrift_spec = (None,
     (1,
      TType.I32,
      'protocolId',
      None,
      None),
     (2,
      TType.STRING,
      'name',
      None,
      None),
     (3,
      TType.STRING,
      'fullName',
      None,
      None),
     (4,
      TType.I32,
      'subProtocolSupported',
      None,
      None))

    def __init__(self, protocolId = None, name = None, fullName = None, subProtocolSupported = None):
        self.protocolId = protocolId
        self.name = name
        self.fullName = fullName
        self.subProtocolSupported = subProtocolSupported



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
                    self.protocolId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.name = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.fullName = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.subProtocolSupported = iprot.readI32()
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
        oprot.writeStructBegin('ProtocolCapabilityIDL')
        if self.protocolId != None:
            oprot.writeFieldBegin('protocolId', TType.I32, 1)
            oprot.writeI32(self.protocolId)
            oprot.writeFieldEnd()
        if self.name != None:
            oprot.writeFieldBegin('name', TType.STRING, 2)
            oprot.writeString(self.name)
            oprot.writeFieldEnd()
        if self.fullName != None:
            oprot.writeFieldBegin('fullName', TType.STRING, 3)
            oprot.writeString(self.fullName)
            oprot.writeFieldEnd()
        if self.subProtocolSupported != None:
            oprot.writeFieldBegin('subProtocolSupported', TType.I32, 4)
            oprot.writeI32(self.subProtocolSupported)
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




class PolicyCapabilityIDL(object):
    """
      Policy Capability
    
      Attributes:
       - maxPolicies
       - maxClasses
       - filterCapab
       - actionCapab
      """

    thrift_spec = (None,
     (1,
      TType.I16,
      'maxPolicies',
      None,
      None),
     (2,
      TType.I16,
      'maxClasses',
      None,
      None),
     (3,
      TType.STRUCT,
      'filterCapab',
      (FilterCapabilityIDL, FilterCapabilityIDL.thrift_spec),
      None),
     (4,
      TType.STRUCT,
      'actionCapab',
      (ActionCapabilityIDL, ActionCapabilityIDL.thrift_spec),
      None))

    def __init__(self, maxPolicies = None, maxClasses = None, filterCapab = None, actionCapab = None):
        self.maxPolicies = maxPolicies
        self.maxClasses = maxClasses
        self.filterCapab = filterCapab
        self.actionCapab = actionCapab



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
                    self.maxPolicies = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I16:
                    self.maxClasses = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRUCT:
                    self.filterCapab = FilterCapabilityIDL()
                    self.filterCapab.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRUCT:
                    self.actionCapab = ActionCapabilityIDL()
                    self.actionCapab.read(iprot)
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
        oprot.writeStructBegin('PolicyCapabilityIDL')
        if self.maxPolicies != None:
            oprot.writeFieldBegin('maxPolicies', TType.I16, 1)
            oprot.writeI16(self.maxPolicies)
            oprot.writeFieldEnd()
        if self.maxClasses != None:
            oprot.writeFieldBegin('maxClasses', TType.I16, 2)
            oprot.writeI16(self.maxClasses)
            oprot.writeFieldEnd()
        if self.filterCapab != None:
            oprot.writeFieldBegin('filterCapab', TType.STRUCT, 3)
            self.filterCapab.write(oprot)
            oprot.writeFieldEnd()
        if self.actionCapab != None:
            oprot.writeFieldBegin('actionCapab', TType.STRUCT, 4)
            self.actionCapab.write(oprot)
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




class L2AceParam_IDL(object):
    """
    Attributes:
     - seqNum
     - permit
     - srcMac
     - srcMacMask
     - dstMac
     - dstMacMask
     - seqNum_v2
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'seqNum',
      None,
      None),
     (2,
      TType.I32,
      'permit',
      None,
      None),
     (3,
      TType.LIST,
      'srcMac',
      (TType.BYTE, None),
      None),
     (4,
      TType.LIST,
      'srcMacMask',
      (TType.BYTE, None),
      None),
     (5,
      TType.LIST,
      'dstMac',
      (TType.BYTE, None),
      None),
     (6,
      TType.LIST,
      'dstMacMask',
      (TType.BYTE, None),
      None),
     (7,
      TType.I64,
      'seqNum_v2',
      None,
      None))

    def __init__(self, seqNum = None, permit = None, srcMac = None, srcMacMask = None, dstMac = None, dstMacMask = None, seqNum_v2 = None):
        self.seqNum = seqNum
        self.permit = permit
        self.srcMac = srcMac
        self.srcMacMask = srcMacMask
        self.dstMac = dstMac
        self.dstMacMask = dstMacMask
        self.seqNum_v2 = seqNum_v2



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
                    self.seqNum = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.permit = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.LIST:
                    self.srcMac = []
                    (_etype10, _size7,) = iprot.readListBegin()
                    for _i11 in xrange(_size7):
                        _elem12 = iprot.readByte()
                        self.srcMac.append(_elem12)

                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.LIST:
                    self.srcMacMask = []
                    (_etype16, _size13,) = iprot.readListBegin()
                    for _i17 in xrange(_size13):
                        _elem18 = iprot.readByte()
                        self.srcMacMask.append(_elem18)

                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.LIST:
                    self.dstMac = []
                    (_etype22, _size19,) = iprot.readListBegin()
                    for _i23 in xrange(_size19):
                        _elem24 = iprot.readByte()
                        self.dstMac.append(_elem24)

                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.LIST:
                    self.dstMacMask = []
                    (_etype28, _size25,) = iprot.readListBegin()
                    for _i29 in xrange(_size25):
                        _elem30 = iprot.readByte()
                        self.dstMacMask.append(_elem30)

                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I64:
                    self.seqNum_v2 = iprot.readI64()
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
        oprot.writeStructBegin('L2AceParam_IDL')
        if self.seqNum != None:
            oprot.writeFieldBegin('seqNum', TType.I32, 1)
            oprot.writeI32(self.seqNum)
            oprot.writeFieldEnd()
        if self.permit != None:
            oprot.writeFieldBegin('permit', TType.I32, 2)
            oprot.writeI32(self.permit)
            oprot.writeFieldEnd()
        if self.srcMac != None:
            oprot.writeFieldBegin('srcMac', TType.LIST, 3)
            oprot.writeListBegin(TType.BYTE, len(self.srcMac))
            for iter31 in self.srcMac:
                oprot.writeByte(iter31)

            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.srcMacMask != None:
            oprot.writeFieldBegin('srcMacMask', TType.LIST, 4)
            oprot.writeListBegin(TType.BYTE, len(self.srcMacMask))
            for iter32 in self.srcMacMask:
                oprot.writeByte(iter32)

            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.dstMac != None:
            oprot.writeFieldBegin('dstMac', TType.LIST, 5)
            oprot.writeListBegin(TType.BYTE, len(self.dstMac))
            for iter33 in self.dstMac:
                oprot.writeByte(iter33)

            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.dstMacMask != None:
            oprot.writeFieldBegin('dstMacMask', TType.LIST, 6)
            oprot.writeListBegin(TType.BYTE, len(self.dstMacMask))
            for iter34 in self.dstMacMask:
                oprot.writeByte(iter34)

            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.seqNum_v2 != None:
            oprot.writeFieldBegin('seqNum_v2', TType.I64, 7)
            oprot.writeI64(self.seqNum_v2)
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




class L3AceParam_IDL(object):
    """
    Attributes:
     - seqNum
     - permit
     - addrAF
     - srcPrefix
     - srcPrefixLen
     - dstPrefix
     - dstPrefixLen
     - protocol
     - srcOper
     - srcPort1
     - srcPort2
     - dstOper
     - dstPort1
     - dstPort2
     - tcpFlag
     - tcpFlagMask
     - tcpFlagMatch
     - dscp
     - flags
     - ttl
     - app_id
     - remoteSn
     - dscp_v2
     - seqNum_v2
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'seqNum',
      None,
      None),
     (2,
      TType.I32,
      'permit',
      None,
      None),
     (3,
      TType.I32,
      'addrAF',
      None,
      None),
     (4,
      TType.STRING,
      'srcPrefix',
      None,
      None),
     (5,
      TType.I16,
      'srcPrefixLen',
      None,
      None),
     (6,
      TType.STRING,
      'dstPrefix',
      None,
      None),
     (7,
      TType.I16,
      'dstPrefixLen',
      None,
      None),
     (8,
      TType.I16,
      'protocol',
      None,
      None),
     (9,
      TType.BYTE,
      'srcOper',
      None,
      None),
     (10,
      TType.I16,
      'srcPort1',
      None,
      None),
     (11,
      TType.I16,
      'srcPort2',
      None,
      None),
     (12,
      TType.BYTE,
      'dstOper',
      None,
      None),
     (13,
      TType.I16,
      'dstPort1',
      None,
      None),
     (14,
      TType.I16,
      'dstPort2',
      None,
      None),
     (15,
      TType.I32,
      'tcpFlag',
      None,
      None),
     (16,
      TType.I32,
      'tcpFlagMask',
      None,
      None),
     (17,
      TType.I32,
      'tcpFlagMatch',
      None,
      None),
     (18,
      TType.BYTE,
      'dscp',
      None,
      None),
     (19,
      TType.I32,
      'flags',
      None,
      None),
     (20,
      TType.I16,
      'ttl',
      None,
      None),
     (21,
      TType.I32,
      'app_id',
      None,
      None),
     (22,
      TType.I32,
      'remoteSn',
      None,
      None),
     (23,
      TType.I32,
      'dscp_v2',
      None,
      None),
     (24,
      TType.I64,
      'seqNum_v2',
      None,
      None))

    def __init__(self, seqNum = None, permit = None, addrAF = None, srcPrefix = None, srcPrefixLen = None, dstPrefix = None, dstPrefixLen = None, protocol = None, srcOper = None, srcPort1 = None, srcPort2 = None, dstOper = None, dstPort1 = None, dstPort2 = None, tcpFlag = None, tcpFlagMask = None, tcpFlagMatch = None, dscp = None, flags = None, ttl = None, app_id = None, remoteSn = None, dscp_v2 = None, seqNum_v2 = None):
        self.seqNum = seqNum
        self.permit = permit
        self.addrAF = addrAF
        self.srcPrefix = srcPrefix
        self.srcPrefixLen = srcPrefixLen
        self.dstPrefix = dstPrefix
        self.dstPrefixLen = dstPrefixLen
        self.protocol = protocol
        self.srcOper = srcOper
        self.srcPort1 = srcPort1
        self.srcPort2 = srcPort2
        self.dstOper = dstOper
        self.dstPort1 = dstPort1
        self.dstPort2 = dstPort2
        self.tcpFlag = tcpFlag
        self.tcpFlagMask = tcpFlagMask
        self.tcpFlagMatch = tcpFlagMatch
        self.dscp = dscp
        self.flags = flags
        self.ttl = ttl
        self.app_id = app_id
        self.remoteSn = remoteSn
        self.dscp_v2 = dscp_v2
        self.seqNum_v2 = seqNum_v2



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
                    self.seqNum = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.permit = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.addrAF = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.srcPrefix = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I16:
                    self.srcPrefixLen = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRING:
                    self.dstPrefix = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I16:
                    self.dstPrefixLen = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.I16:
                    self.protocol = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.BYTE:
                    self.srcOper = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.I16:
                    self.srcPort1 = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.I16:
                    self.srcPort2 = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 12:
                if ftype == TType.BYTE:
                    self.dstOper = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 13:
                if ftype == TType.I16:
                    self.dstPort1 = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 14:
                if ftype == TType.I16:
                    self.dstPort2 = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 15:
                if ftype == TType.I32:
                    self.tcpFlag = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 16:
                if ftype == TType.I32:
                    self.tcpFlagMask = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 17:
                if ftype == TType.I32:
                    self.tcpFlagMatch = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 18:
                if ftype == TType.BYTE:
                    self.dscp = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 19:
                if ftype == TType.I32:
                    self.flags = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 20:
                if ftype == TType.I16:
                    self.ttl = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 21:
                if ftype == TType.I32:
                    self.app_id = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 22:
                if ftype == TType.I32:
                    self.remoteSn = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 23:
                if ftype == TType.I32:
                    self.dscp_v2 = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 24:
                if ftype == TType.I64:
                    self.seqNum_v2 = iprot.readI64()
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
        oprot.writeStructBegin('L3AceParam_IDL')
        if self.seqNum != None:
            oprot.writeFieldBegin('seqNum', TType.I32, 1)
            oprot.writeI32(self.seqNum)
            oprot.writeFieldEnd()
        if self.permit != None:
            oprot.writeFieldBegin('permit', TType.I32, 2)
            oprot.writeI32(self.permit)
            oprot.writeFieldEnd()
        if self.addrAF != None:
            oprot.writeFieldBegin('addrAF', TType.I32, 3)
            oprot.writeI32(self.addrAF)
            oprot.writeFieldEnd()
        if self.srcPrefix != None:
            oprot.writeFieldBegin('srcPrefix', TType.STRING, 4)
            oprot.writeString(self.srcPrefix)
            oprot.writeFieldEnd()
        if self.srcPrefixLen != None:
            oprot.writeFieldBegin('srcPrefixLen', TType.I16, 5)
            oprot.writeI16(self.srcPrefixLen)
            oprot.writeFieldEnd()
        if self.dstPrefix != None:
            oprot.writeFieldBegin('dstPrefix', TType.STRING, 6)
            oprot.writeString(self.dstPrefix)
            oprot.writeFieldEnd()
        if self.dstPrefixLen != None:
            oprot.writeFieldBegin('dstPrefixLen', TType.I16, 7)
            oprot.writeI16(self.dstPrefixLen)
            oprot.writeFieldEnd()
        if self.protocol != None:
            oprot.writeFieldBegin('protocol', TType.I16, 8)
            oprot.writeI16(self.protocol)
            oprot.writeFieldEnd()
        if self.srcOper != None:
            oprot.writeFieldBegin('srcOper', TType.BYTE, 9)
            oprot.writeByte(self.srcOper)
            oprot.writeFieldEnd()
        if self.srcPort1 != None:
            oprot.writeFieldBegin('srcPort1', TType.I16, 10)
            oprot.writeI16(self.srcPort1)
            oprot.writeFieldEnd()
        if self.srcPort2 != None:
            oprot.writeFieldBegin('srcPort2', TType.I16, 11)
            oprot.writeI16(self.srcPort2)
            oprot.writeFieldEnd()
        if self.dstOper != None:
            oprot.writeFieldBegin('dstOper', TType.BYTE, 12)
            oprot.writeByte(self.dstOper)
            oprot.writeFieldEnd()
        if self.dstPort1 != None:
            oprot.writeFieldBegin('dstPort1', TType.I16, 13)
            oprot.writeI16(self.dstPort1)
            oprot.writeFieldEnd()
        if self.dstPort2 != None:
            oprot.writeFieldBegin('dstPort2', TType.I16, 14)
            oprot.writeI16(self.dstPort2)
            oprot.writeFieldEnd()
        if self.tcpFlag != None:
            oprot.writeFieldBegin('tcpFlag', TType.I32, 15)
            oprot.writeI32(self.tcpFlag)
            oprot.writeFieldEnd()
        if self.tcpFlagMask != None:
            oprot.writeFieldBegin('tcpFlagMask', TType.I32, 16)
            oprot.writeI32(self.tcpFlagMask)
            oprot.writeFieldEnd()
        if self.tcpFlagMatch != None:
            oprot.writeFieldBegin('tcpFlagMatch', TType.I32, 17)
            oprot.writeI32(self.tcpFlagMatch)
            oprot.writeFieldEnd()
        if self.dscp != None:
            oprot.writeFieldBegin('dscp', TType.BYTE, 18)
            oprot.writeByte(self.dscp)
            oprot.writeFieldEnd()
        if self.flags != None:
            oprot.writeFieldBegin('flags', TType.I32, 19)
            oprot.writeI32(self.flags)
            oprot.writeFieldEnd()
        if self.ttl != None:
            oprot.writeFieldBegin('ttl', TType.I16, 20)
            oprot.writeI16(self.ttl)
            oprot.writeFieldEnd()
        if self.app_id != None:
            oprot.writeFieldBegin('app_id', TType.I32, 21)
            oprot.writeI32(self.app_id)
            oprot.writeFieldEnd()
        if self.remoteSn != None:
            oprot.writeFieldBegin('remoteSn', TType.I32, 22)
            oprot.writeI32(self.remoteSn)
            oprot.writeFieldEnd()
        if self.dscp_v2 != None:
            oprot.writeFieldBegin('dscp_v2', TType.I32, 23)
            oprot.writeI32(self.dscp_v2)
            oprot.writeFieldEnd()
        if self.seqNum_v2 != None:
            oprot.writeFieldBegin('seqNum_v2', TType.I64, 24)
            oprot.writeI64(self.seqNum_v2)
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




class AclHeader_IDL(object):
    """
    Attributes:
     - sessionId
     - type
     - lifetime
     - name
     - addrFamily
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionId',
      None,
      None),
     (2,
      TType.I32,
      'type',
      None,
      None),
     (3,
      TType.I32,
      'lifetime',
      None,
      None),
     (4,
      TType.STRING,
      'name',
      None,
      None),
     (5,
      TType.I32,
      'addrFamily',
      None,
      None))

    def __init__(self, sessionId = None, type = None, lifetime = None, name = None, addrFamily = None):
        self.sessionId = sessionId
        self.type = type
        self.lifetime = lifetime
        self.name = name
        self.addrFamily = addrFamily



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
                    self.sessionId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.lifetime = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.name = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.addrFamily = iprot.readI32()
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
        oprot.writeStructBegin('AclHeader_IDL')
        if self.sessionId != None:
            oprot.writeFieldBegin('sessionId', TType.I32, 1)
            oprot.writeI32(self.sessionId)
            oprot.writeFieldEnd()
        if self.type != None:
            oprot.writeFieldBegin('type', TType.I32, 2)
            oprot.writeI32(self.type)
            oprot.writeFieldEnd()
        if self.lifetime != None:
            oprot.writeFieldBegin('lifetime', TType.I32, 3)
            oprot.writeI32(self.lifetime)
            oprot.writeFieldEnd()
        if self.name != None:
            oprot.writeFieldBegin('name', TType.STRING, 4)
            oprot.writeString(self.name)
            oprot.writeFieldEnd()
        if self.addrFamily != None:
            oprot.writeFieldBegin('addrFamily', TType.I32, 5)
            oprot.writeI32(self.addrFamily)
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
# 2015.02.05 17:19:53 IST
