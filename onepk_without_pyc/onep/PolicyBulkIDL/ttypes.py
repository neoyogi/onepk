# 2015.02.05 17:22:21 IST
from thrift.Thrift import *
import PolicyCommonTypes.ttypes
import Shared.ttypes
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
    from thrift.protocol import fastbinary
except:
    fastbinary = None

class ActionOutInterfaceIDL(object):
    """
      Output Interface action
    
      Attributes:
       - ifHandle
      """

    thrift_spec = (None, (1,
      TType.LIST,
      'ifHandle',
      (TType.I64, None),
      None))

    def __init__(self, ifHandle = None):
        self.ifHandle = ifHandle



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
                    self.ifHandle = []
                    (_etype3, _size0,) = iprot.readListBegin()
                    for _i4 in xrange(_size0):
                        _elem5 = iprot.readI64()
                        self.ifHandle.append(_elem5)

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
        oprot.writeStructBegin('ActionOutInterfaceIDL')
        if self.ifHandle != None:
            oprot.writeFieldBegin('ifHandle', TType.LIST, 1)
            oprot.writeListBegin(TType.I64, len(self.ifHandle))
            for iter6 in self.ifHandle:
                oprot.writeI64(iter6)

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




class ActionMarkIDL(object):
    """
      Packet Marking action
    
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
        oprot.writeStructBegin('ActionMarkIDL')
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




class ActionPoliceIDL(object):
    """
      Policing action
    
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
      TType.I64,
      'conformColor',
      None,
      None),
     (14,
      TType.I64,
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
                if ftype == TType.I64:
                    self.conformColor = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 14:
                if ftype == TType.I64:
                    self.exceedColor = iprot.readI64()
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
        oprot.writeStructBegin('ActionPoliceIDL')
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
            oprot.writeFieldBegin('conformColor', TType.I64, 13)
            oprot.writeI64(self.conformColor)
            oprot.writeFieldEnd()
        if self.exceedColor != None:
            oprot.writeFieldBegin('exceedColor', TType.I64, 14)
            oprot.writeI64(self.exceedColor)
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




class ActionShapeIDL(object):
    """
       * Shape parameters
      *
      *  Ideally, need to isolate burst params, and use 3:optional burstSpecs bsp;
      *  struct burst_params {1:burstUnits, 2:cbs, 3:optional ebs} i.e. if burst unit is
      *   specified cbs is must, and ebs is optional, but ebs can only be specified if cbs is specified.
    
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
        oprot.writeStructBegin('ActionShapeIDL')
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




class ActionPriorityQueueIDL(object):
    """
      Priority Queue action
    
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
      TType.I32,
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
                if ftype == TType.I32:
                    self.burst = iprot.readI32()
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
        oprot.writeStructBegin('ActionPriorityQueueIDL')
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
            oprot.writeFieldBegin('burst', TType.I32, 4)
            oprot.writeI32(self.burst)
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




class ActionClassQueueIDL(object):
    """
      Class-based Queue action
    
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
        oprot.writeStructBegin('ActionClassQueueIDL')
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




class ActionFairQueueIDL(object):
    """
      Fair Queue action
    
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
        oprot.writeStructBegin('ActionFairQueueIDL')
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




class ActionQueueLimitIDL(object):
    """
      Queue Limit action
    
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
        oprot.writeStructBegin('ActionQueueLimitIDL')
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




class ActionWredProfileIDL(object):
    """
      WRED profile
    
      Attributes:
       - type
       - value
       - minThreshold
       - maxThreshold
       - dropProb
       - thresholdUnits
      """

    thrift_spec = (None,
     (1,
      TType.I32,
      'type',
      None,
      None),
     (2,
      TType.I32,
      'value',
      None,
      None),
     (3,
      TType.I32,
      'minThreshold',
      None,
      None),
     (4,
      TType.I32,
      'maxThreshold',
      None,
      None),
     (5,
      TType.I32,
      'dropProb',
      None,
      None),
     (6,
      TType.I32,
      'thresholdUnits',
      None,
      None))

    def __init__(self, type = None, value = None, minThreshold = None, maxThreshold = None, dropProb = None, thresholdUnits = None):
        self.type = type
        self.value = value
        self.minThreshold = minThreshold
        self.maxThreshold = maxThreshold
        self.dropProb = dropProb
        self.thresholdUnits = thresholdUnits



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
            elif fid == 3:
                if ftype == TType.I32:
                    self.minThreshold = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.maxThreshold = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.dropProb = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I32:
                    self.thresholdUnits = iprot.readI32()
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
        oprot.writeStructBegin('ActionWredProfileIDL')
        if self.type != None:
            oprot.writeFieldBegin('type', TType.I32, 1)
            oprot.writeI32(self.type)
            oprot.writeFieldEnd()
        if self.value != None:
            oprot.writeFieldBegin('value', TType.I32, 2)
            oprot.writeI32(self.value)
            oprot.writeFieldEnd()
        if self.minThreshold != None:
            oprot.writeFieldBegin('minThreshold', TType.I32, 3)
            oprot.writeI32(self.minThreshold)
            oprot.writeFieldEnd()
        if self.maxThreshold != None:
            oprot.writeFieldBegin('maxThreshold', TType.I32, 4)
            oprot.writeI32(self.maxThreshold)
            oprot.writeFieldEnd()
        if self.dropProb != None:
            oprot.writeFieldBegin('dropProb', TType.I32, 5)
            oprot.writeI32(self.dropProb)
            oprot.writeFieldEnd()
        if self.thresholdUnits != None:
            oprot.writeFieldBegin('thresholdUnits', TType.I32, 6)
            oprot.writeI32(self.thresholdUnits)
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




class ActionWredParamIDL(object):
    """
      WRED action parameters
    
      Attributes:
       - type
       - ecnEnabled
       - exponWeight
       - thresholdUnits
      """

    thrift_spec = (None,
     (1,
      TType.I32,
      'type',
      None,
      None),
     (2,
      TType.I32,
      'ecnEnabled',
      None,
      None),
     (3,
      TType.I32,
      'exponWeight',
      None,
      None),
     (4,
      TType.I32,
      'thresholdUnits',
      None,
      None))

    def __init__(self, type = None, ecnEnabled = None, exponWeight = None, thresholdUnits = None):
        self.type = type
        self.ecnEnabled = ecnEnabled
        self.exponWeight = exponWeight
        self.thresholdUnits = thresholdUnits



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
                    self.ecnEnabled = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.exponWeight = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.thresholdUnits = iprot.readI32()
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
        oprot.writeStructBegin('ActionWredParamIDL')
        if self.type != None:
            oprot.writeFieldBegin('type', TType.I32, 1)
            oprot.writeI32(self.type)
            oprot.writeFieldEnd()
        if self.ecnEnabled != None:
            oprot.writeFieldBegin('ecnEnabled', TType.I32, 2)
            oprot.writeI32(self.ecnEnabled)
            oprot.writeFieldEnd()
        if self.exponWeight != None:
            oprot.writeFieldBegin('exponWeight', TType.I32, 3)
            oprot.writeI32(self.exponWeight)
            oprot.writeFieldEnd()
        if self.thresholdUnits != None:
            oprot.writeFieldBegin('thresholdUnits', TType.I32, 4)
            oprot.writeI32(self.thresholdUnits)
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




class ActionPktCopyIDL(object):
    """
      Packet Copy action
    
      Attributes:
       - remoteSn
       - appId
       - localId
       - size
       - sampleType
       - sampleRate
      """

    thrift_spec = (None,
     (1,
      TType.I32,
      'remoteSn',
      None,
      None),
     (2,
      TType.I32,
      'appId',
      None,
      None),
     (3,
      TType.I32,
      'localId',
      None,
      None),
     (4,
      TType.I32,
      'size',
      None,
      None),
     (5,
      TType.I32,
      'sampleType',
      None,
      None),
     (6,
      TType.I32,
      'sampleRate',
      None,
      None))

    def __init__(self, remoteSn = None, appId = None, localId = None, size = None, sampleType = None, sampleRate = None):
        self.remoteSn = remoteSn
        self.appId = appId
        self.localId = localId
        self.size = size
        self.sampleType = sampleType
        self.sampleRate = sampleRate



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
                    self.remoteSn = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.appId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.localId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.size = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.sampleType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I32:
                    self.sampleRate = iprot.readI32()
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
        oprot.writeStructBegin('ActionPktCopyIDL')
        if self.remoteSn != None:
            oprot.writeFieldBegin('remoteSn', TType.I32, 1)
            oprot.writeI32(self.remoteSn)
            oprot.writeFieldEnd()
        if self.appId != None:
            oprot.writeFieldBegin('appId', TType.I32, 2)
            oprot.writeI32(self.appId)
            oprot.writeFieldEnd()
        if self.localId != None:
            oprot.writeFieldBegin('localId', TType.I32, 3)
            oprot.writeI32(self.localId)
            oprot.writeFieldEnd()
        if self.size != None:
            oprot.writeFieldBegin('size', TType.I32, 4)
            oprot.writeI32(self.size)
            oprot.writeFieldEnd()
        if self.sampleType != None:
            oprot.writeFieldBegin('sampleType', TType.I32, 5)
            oprot.writeI32(self.sampleType)
            oprot.writeFieldEnd()
        if self.sampleRate != None:
            oprot.writeFieldBegin('sampleRate', TType.I32, 6)
            oprot.writeI32(self.sampleRate)
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




class ActionPktDivertIDL(object):
    """
      Packet Divert action
    
      Attributes:
       - remoteSn
       - appId
       - localId
       - state
      """

    thrift_spec = (None,
     (1,
      TType.I32,
      'remoteSn',
      None,
      None),
     (2,
      TType.I32,
      'appId',
      None,
      None),
     (3,
      TType.I32,
      'localId',
      None,
      None),
     (4,
      TType.I32,
      'state',
      None,
      None))

    def __init__(self, remoteSn = None, appId = None, localId = None, state = None):
        self.remoteSn = remoteSn
        self.appId = appId
        self.localId = localId
        self.state = state



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
                    self.remoteSn = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.appId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.localId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.state = iprot.readI32()
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
        oprot.writeStructBegin('ActionPktDivertIDL')
        if self.remoteSn != None:
            oprot.writeFieldBegin('remoteSn', TType.I32, 1)
            oprot.writeI32(self.remoteSn)
            oprot.writeFieldEnd()
        if self.appId != None:
            oprot.writeFieldBegin('appId', TType.I32, 2)
            oprot.writeI32(self.appId)
            oprot.writeFieldEnd()
        if self.localId != None:
            oprot.writeFieldBegin('localId', TType.I32, 3)
            oprot.writeI32(self.localId)
            oprot.writeFieldEnd()
        if self.state != None:
            oprot.writeFieldBegin('state', TType.I32, 4)
            oprot.writeI32(self.state)
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




class ActionVlanIDL(object):
    """
      VLAN action
    
      Attributes:
       - type
       - vlan
      """

    thrift_spec = (None, (1,
      TType.I16,
      'type',
      None,
      None), (2,
      TType.I16,
      'vlan',
      None,
      None))

    def __init__(self, type = None, vlan = None):
        self.type = type
        self.vlan = vlan



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
                if ftype == TType.I16:
                    self.vlan = iprot.readI16()
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
        oprot.writeStructBegin('ActionVlanIDL')
        if self.type != None:
            oprot.writeFieldBegin('type', TType.I16, 1)
            oprot.writeI16(self.type)
            oprot.writeFieldEnd()
        if self.vlan != None:
            oprot.writeFieldBegin('vlan', TType.I16, 2)
            oprot.writeI16(self.vlan)
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




class ActionTtlIDL(object):
    """
      TTL action
    
      Attributes:
       - type
       - ttl
      """

    thrift_spec = (None, (1,
      TType.I16,
      'type',
      None,
      None), (2,
      TType.BYTE,
      'ttl',
      None,
      None))

    def __init__(self, type = None, ttl = None):
        self.type = type
        self.ttl = ttl



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
                if ftype == TType.BYTE:
                    self.ttl = iprot.readByte()
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
        oprot.writeStructBegin('ActionTtlIDL')
        if self.type != None:
            oprot.writeFieldBegin('type', TType.I16, 1)
            oprot.writeI16(self.type)
            oprot.writeFieldEnd()
        if self.ttl != None:
            oprot.writeFieldBegin('ttl', TType.BYTE, 2)
            oprot.writeByte(self.ttl)
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




class ActionMplsIDL(object):
    """
      MPLS action
    
      Attributes:
       - type
       - label
       - tc
      """

    thrift_spec = (None,
     (1,
      TType.I16,
      'type',
      None,
      None),
     (2,
      TType.I32,
      'label',
      None,
      None),
     (3,
      TType.BYTE,
      'tc',
      None,
      None))

    def __init__(self, type = None, label = None, tc = None):
        self.type = type
        self.label = label
        self.tc = tc



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
                if ftype == TType.I32:
                    self.label = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.BYTE:
                    self.tc = iprot.readByte()
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
        oprot.writeStructBegin('ActionMplsIDL')
        if self.type != None:
            oprot.writeFieldBegin('type', TType.I16, 1)
            oprot.writeI16(self.type)
            oprot.writeFieldEnd()
        if self.label != None:
            oprot.writeFieldBegin('label', TType.I32, 2)
            oprot.writeI32(self.label)
            oprot.writeFieldEnd()
        if self.tc != None:
            oprot.writeFieldBegin('tc', TType.BYTE, 3)
            oprot.writeByte(self.tc)
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




class ActionOutputIDL(object):
    """
      Output action
    
      Attributes:
       - type
      """

    thrift_spec = (None, (1,
      TType.I16,
      'type',
      None,
      None))

    def __init__(self, type = None):
        self.type = type



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
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()

        iprot.readStructEnd()



    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return 
        oprot.writeStructBegin('ActionOutputIDL')
        if self.type != None:
            oprot.writeFieldBegin('type', TType.I16, 1)
            oprot.writeI16(self.type)
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




class ActionFwdClassIdIDL(object):
    """
      Forward Class ID
    
      Attributes:
       - id
      """

    thrift_spec = (None, (1,
      TType.I16,
      'id',
      None,
      None))

    def __init__(self, id = None):
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
                if ftype == TType.I16:
                    self.id = iprot.readI16()
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
        oprot.writeStructBegin('ActionFwdClassIdIDL')
        if self.id != None:
            oprot.writeFieldBegin('id', TType.I16, 1)
            oprot.writeI16(self.id)
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




class ActionMacAddressIDL(object):
    """
      MAC Address action
    
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
                    (_etype10, _size7,) = iprot.readListBegin()
                    for _i11 in xrange(_size7):
                        _elem12 = iprot.readByte()
                        self.addr.append(_elem12)

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
        oprot.writeStructBegin('ActionMacAddressIDL')
        if self.type != None:
            oprot.writeFieldBegin('type', TType.I16, 1)
            oprot.writeI16(self.type)
            oprot.writeFieldEnd()
        if self.addr != None:
            oprot.writeFieldBegin('addr', TType.LIST, 2)
            oprot.writeListBegin(TType.BYTE, len(self.addr))
            for iter13 in self.addr:
                oprot.writeByte(iter13)

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




class ActionIpAddressIDL(object):
    """
      IP Address action
      Either a mask or a prefix can be used for the match but not both
    
      Attributes:
       - sense
       - type
       - srcDst
       - family
       - addr
       - prefixLen
      """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sense',
      None,
      None),
     (2,
      TType.I16,
      'type',
      None,
      None),
     (3,
      TType.I16,
      'srcDst',
      None,
      None),
     (4,
      TType.I32,
      'family',
      None,
      None),
     (5,
      TType.LIST,
      'addr',
      (TType.BYTE, None),
      None),
     (6,
      TType.I16,
      'prefixLen',
      None,
      None))

    def __init__(self, sense = None, type = None, srcDst = None, family = None, addr = None, prefixLen = None):
        self.sense = sense
        self.type = type
        self.srcDst = srcDst
        self.family = family
        self.addr = addr
        self.prefixLen = prefixLen



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
                    self.sense = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I16:
                    self.type = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I16:
                    self.srcDst = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.family = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.LIST:
                    self.addr = []
                    (_etype17, _size14,) = iprot.readListBegin()
                    for _i18 in xrange(_size14):
                        _elem19 = iprot.readByte()
                        self.addr.append(_elem19)

                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I16:
                    self.prefixLen = iprot.readI16()
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
        oprot.writeStructBegin('ActionIpAddressIDL')
        if self.sense != None:
            oprot.writeFieldBegin('sense', TType.I32, 1)
            oprot.writeI32(self.sense)
            oprot.writeFieldEnd()
        if self.type != None:
            oprot.writeFieldBegin('type', TType.I16, 2)
            oprot.writeI16(self.type)
            oprot.writeFieldEnd()
        if self.srcDst != None:
            oprot.writeFieldBegin('srcDst', TType.I16, 3)
            oprot.writeI16(self.srcDst)
            oprot.writeFieldEnd()
        if self.family != None:
            oprot.writeFieldBegin('family', TType.I32, 4)
            oprot.writeI32(self.family)
            oprot.writeFieldEnd()
        if self.addr != None:
            oprot.writeFieldBegin('addr', TType.LIST, 5)
            oprot.writeListBegin(TType.BYTE, len(self.addr))
            for iter20 in self.addr:
                oprot.writeByte(iter20)

            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.prefixLen != None:
            oprot.writeFieldBegin('prefixLen', TType.I16, 6)
            oprot.writeI16(self.prefixLen)
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




class ActionTcpPortIDL(object):
    """
      TCP/UDP Port Action
    
      Attributes:
       - sense
       - srcDst
       - oper
       - port1
       - port2
      """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sense',
      None,
      None),
     (2,
      TType.I16,
      'srcDst',
      None,
      None),
     (3,
      TType.BYTE,
      'oper',
      None,
      None),
     (4,
      TType.I16,
      'port1',
      None,
      None),
     (5,
      TType.I16,
      'port2',
      None,
      None))

    def __init__(self, sense = None, srcDst = None, oper = None, port1 = None, port2 = None):
        self.sense = sense
        self.srcDst = srcDst
        self.oper = oper
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
                    self.sense = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I16:
                    self.srcDst = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.BYTE:
                    self.oper = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I16:
                    self.port1 = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I16:
                    self.port2 = iprot.readI16()
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
        oprot.writeStructBegin('ActionTcpPortIDL')
        if self.sense != None:
            oprot.writeFieldBegin('sense', TType.I32, 1)
            oprot.writeI32(self.sense)
            oprot.writeFieldEnd()
        if self.srcDst != None:
            oprot.writeFieldBegin('srcDst', TType.I16, 2)
            oprot.writeI16(self.srcDst)
            oprot.writeFieldEnd()
        if self.oper != None:
            oprot.writeFieldBegin('oper', TType.BYTE, 3)
            oprot.writeByte(self.oper)
            oprot.writeFieldEnd()
        if self.port1 != None:
            oprot.writeFieldBegin('port1', TType.I16, 4)
            oprot.writeI16(self.port1)
            oprot.writeFieldEnd()
        if self.port2 != None:
            oprot.writeFieldBegin('port2', TType.I16, 5)
            oprot.writeI16(self.port2)
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




class ActionNextHopIDL(object):
    """
      Next Hop action
    
      Attributes:
       - family
       - addr
      """

    thrift_spec = (None, (1,
      TType.I32,
      'family',
      None,
      None), (2,
      TType.LIST,
      'addr',
      (TType.BYTE, None),
      None))

    def __init__(self, family = None, addr = None):
        self.family = family
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
                if ftype == TType.I32:
                    self.family = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.addr = []
                    (_etype24, _size21,) = iprot.readListBegin()
                    for _i25 in xrange(_size21):
                        _elem26 = iprot.readByte()
                        self.addr.append(_elem26)

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
        oprot.writeStructBegin('ActionNextHopIDL')
        if self.family != None:
            oprot.writeFieldBegin('family', TType.I32, 1)
            oprot.writeI32(self.family)
            oprot.writeFieldEnd()
        if self.addr != None:
            oprot.writeFieldBegin('addr', TType.LIST, 2)
            oprot.writeListBegin(TType.BYTE, len(self.addr))
            for iter27 in self.addr:
                oprot.writeByte(iter27)

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




class ActionMplsExpIDL(object):
    """
      MPLS Experimantal tag action
    
      Attributes:
       - sense
       - mplsExp
      """

    thrift_spec = (None, (1,
      TType.I32,
      'sense',
      None,
      None), (2,
      TType.I32,
      'mplsExp',
      None,
      None))

    def __init__(self, sense = None, mplsExp = None):
        self.sense = sense
        self.mplsExp = mplsExp



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
                    self.sense = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.mplsExp = iprot.readI32()
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
        oprot.writeStructBegin('ActionMplsExpIDL')
        if self.sense != None:
            oprot.writeFieldBegin('sense', TType.I32, 1)
            oprot.writeI32(self.sense)
            oprot.writeFieldEnd()
        if self.mplsExp != None:
            oprot.writeFieldBegin('mplsExp', TType.I32, 2)
            oprot.writeI32(self.mplsExp)
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




class ActionGotoTableIDL(object):
    """
      Goto Table action
    
      Attributes:
       - pmapHandle
      """

    thrift_spec = (None, (1,
      TType.I64,
      'pmapHandle',
      None,
      None))

    def __init__(self, pmapHandle = None):
        self.pmapHandle = pmapHandle



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
                    self.pmapHandle = iprot.readI64()
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
        oprot.writeStructBegin('ActionGotoTableIDL')
        if self.pmapHandle != None:
            oprot.writeFieldBegin('pmapHandle', TType.I64, 1)
            oprot.writeI64(self.pmapHandle)
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




class ActionProtocolIDL(object):
    """
      Protocol action
    
      Attributes:
       - sense
       - protocol
      """

    thrift_spec = (None, (1,
      TType.I32,
      'sense',
      None,
      None), (2,
      TType.I32,
      'protocol',
      None,
      None))

    def __init__(self, sense = None, protocol = None):
        self.sense = sense
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
                if ftype == TType.I32:
                    self.sense = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.protocol = iprot.readI32()
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
        oprot.writeStructBegin('ActionProtocolIDL')
        if self.sense != None:
            oprot.writeFieldBegin('sense', TType.I32, 1)
            oprot.writeI32(self.sense)
            oprot.writeFieldEnd()
        if self.protocol != None:
            oprot.writeFieldBegin('protocol', TType.I32, 2)
            oprot.writeI32(self.protocol)
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




class MatchInterfaceIDL(object):
    """
      Interface match
    
      Attributes:
       - sense
       - ifHandle
      """

    thrift_spec = (None, (1,
      TType.I32,
      'sense',
      None,
      None), (2,
      TType.I32,
      'ifHandle',
      None,
      None))

    def __init__(self, sense = None, ifHandle = None):
        self.sense = sense
        self.ifHandle = ifHandle



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
                    self.sense = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.ifHandle = iprot.readI32()
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
        oprot.writeStructBegin('MatchInterfaceIDL')
        if self.sense != None:
            oprot.writeFieldBegin('sense', TType.I32, 1)
            oprot.writeI32(self.sense)
            oprot.writeFieldEnd()
        if self.ifHandle != None:
            oprot.writeFieldBegin('ifHandle', TType.I32, 2)
            oprot.writeI32(self.ifHandle)
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




class MatchAclIDL(object):
    """
      ACL match
    
      Attributes:
       - sense
       - aclHandle
       - name
      """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sense',
      None,
      None),
     (2,
      TType.I64,
      'aclHandle',
      None,
      None),
     (3,
      TType.STRING,
      'name',
      None,
      None))

    def __init__(self, sense = None, aclHandle = None, name = None):
        self.sense = sense
        self.aclHandle = aclHandle
        self.name = name



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
                    self.sense = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.aclHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.name = iprot.readString()
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
        oprot.writeStructBegin('MatchAclIDL')
        if self.sense != None:
            oprot.writeFieldBegin('sense', TType.I32, 1)
            oprot.writeI32(self.sense)
            oprot.writeFieldEnd()
        if self.aclHandle != None:
            oprot.writeFieldBegin('aclHandle', TType.I64, 2)
            oprot.writeI64(self.aclHandle)
            oprot.writeFieldEnd()
        if self.name != None:
            oprot.writeFieldBegin('name', TType.STRING, 3)
            oprot.writeString(self.name)
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




class MatchMacAddressIDL(object):
    """
      MAC Address match
    
      Attributes:
       - sense
       - type
       - addr
       - mask
      """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sense',
      None,
      None),
     (2,
      TType.I16,
      'type',
      None,
      None),
     (3,
      TType.LIST,
      'addr',
      (TType.BYTE, None),
      [1,
       2,
       3,
       4,
       5,
       6]),
     (4,
      TType.LIST,
      'mask',
      (TType.BYTE, None),
      [1,
       2,
       3,
       4,
       5,
       6]))

    def __init__(self, sense = None, type = None, addr = thrift_spec[3][4], mask = thrift_spec[4][4]):
        self.sense = sense
        self.type = type
        if addr is self.thrift_spec[3][4]:
            addr = [1,
             2,
             3,
             4,
             5,
             6]
        self.addr = addr
        if mask is self.thrift_spec[4][4]:
            mask = [1,
             2,
             3,
             4,
             5,
             6]
        self.mask = mask



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
                    self.sense = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I16:
                    self.type = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.LIST:
                    self.addr = []
                    (_etype31, _size28,) = iprot.readListBegin()
                    for _i32 in xrange(_size28):
                        _elem33 = iprot.readByte()
                        self.addr.append(_elem33)

                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.LIST:
                    self.mask = []
                    (_etype37, _size34,) = iprot.readListBegin()
                    for _i38 in xrange(_size34):
                        _elem39 = iprot.readByte()
                        self.mask.append(_elem39)

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
        oprot.writeStructBegin('MatchMacAddressIDL')
        if self.sense != None:
            oprot.writeFieldBegin('sense', TType.I32, 1)
            oprot.writeI32(self.sense)
            oprot.writeFieldEnd()
        if self.type != None:
            oprot.writeFieldBegin('type', TType.I16, 2)
            oprot.writeI16(self.type)
            oprot.writeFieldEnd()
        if self.addr != None:
            oprot.writeFieldBegin('addr', TType.LIST, 3)
            oprot.writeListBegin(TType.BYTE, len(self.addr))
            for iter40 in self.addr:
                oprot.writeByte(iter40)

            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.mask != None:
            oprot.writeFieldBegin('mask', TType.LIST, 4)
            oprot.writeListBegin(TType.BYTE, len(self.mask))
            for iter41 in self.mask:
                oprot.writeByte(iter41)

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




class MatchIpAddressIDL(object):
    """
      IP Address match
      Either a mask or a prefix can be used for the match but not both
    
      Attributes:
       - sense
       - type
       - srcDst
       - family
       - addr
       - mask
       - prefixLen
      """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sense',
      None,
      None),
     (2,
      TType.I16,
      'type',
      None,
      None),
     (3,
      TType.I16,
      'srcDst',
      None,
      None),
     (4,
      TType.I32,
      'family',
      None,
      None),
     (5,
      TType.LIST,
      'addr',
      (TType.BYTE, None),
      None),
     (6,
      TType.LIST,
      'mask',
      (TType.BYTE, None),
      None),
     (7,
      TType.I16,
      'prefixLen',
      None,
      None))

    def __init__(self, sense = None, type = None, srcDst = None, family = None, addr = None, mask = None, prefixLen = None):
        self.sense = sense
        self.type = type
        self.srcDst = srcDst
        self.family = family
        self.addr = addr
        self.mask = mask
        self.prefixLen = prefixLen



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
                    self.sense = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I16:
                    self.type = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I16:
                    self.srcDst = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.family = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.LIST:
                    self.addr = []
                    (_etype45, _size42,) = iprot.readListBegin()
                    for _i46 in xrange(_size42):
                        _elem47 = iprot.readByte()
                        self.addr.append(_elem47)

                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.LIST:
                    self.mask = []
                    (_etype51, _size48,) = iprot.readListBegin()
                    for _i52 in xrange(_size48):
                        _elem53 = iprot.readByte()
                        self.mask.append(_elem53)

                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I16:
                    self.prefixLen = iprot.readI16()
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
        oprot.writeStructBegin('MatchIpAddressIDL')
        if self.sense != None:
            oprot.writeFieldBegin('sense', TType.I32, 1)
            oprot.writeI32(self.sense)
            oprot.writeFieldEnd()
        if self.type != None:
            oprot.writeFieldBegin('type', TType.I16, 2)
            oprot.writeI16(self.type)
            oprot.writeFieldEnd()
        if self.srcDst != None:
            oprot.writeFieldBegin('srcDst', TType.I16, 3)
            oprot.writeI16(self.srcDst)
            oprot.writeFieldEnd()
        if self.family != None:
            oprot.writeFieldBegin('family', TType.I32, 4)
            oprot.writeI32(self.family)
            oprot.writeFieldEnd()
        if self.addr != None:
            oprot.writeFieldBegin('addr', TType.LIST, 5)
            oprot.writeListBegin(TType.BYTE, len(self.addr))
            for iter54 in self.addr:
                oprot.writeByte(iter54)

            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.mask != None:
            oprot.writeFieldBegin('mask', TType.LIST, 6)
            oprot.writeListBegin(TType.BYTE, len(self.mask))
            for iter55 in self.mask:
                oprot.writeByte(iter55)

            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.prefixLen != None:
            oprot.writeFieldBegin('prefixLen', TType.I16, 7)
            oprot.writeI16(self.prefixLen)
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




class MatchTcpPortIDL(object):
    """
      TCP/UDP Port match
    
      Attributes:
       - sense
       - srcDst
       - oper
       - port1
       - port2
      """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sense',
      None,
      None),
     (2,
      TType.I16,
      'srcDst',
      None,
      None),
     (3,
      TType.BYTE,
      'oper',
      None,
      None),
     (4,
      TType.I16,
      'port1',
      None,
      None),
     (5,
      TType.I16,
      'port2',
      None,
      None))

    def __init__(self, sense = None, srcDst = None, oper = None, port1 = None, port2 = None):
        self.sense = sense
        self.srcDst = srcDst
        self.oper = oper
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
                    self.sense = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I16:
                    self.srcDst = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.BYTE:
                    self.oper = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I16:
                    self.port1 = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I16:
                    self.port2 = iprot.readI16()
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
        oprot.writeStructBegin('MatchTcpPortIDL')
        if self.sense != None:
            oprot.writeFieldBegin('sense', TType.I32, 1)
            oprot.writeI32(self.sense)
            oprot.writeFieldEnd()
        if self.srcDst != None:
            oprot.writeFieldBegin('srcDst', TType.I16, 2)
            oprot.writeI16(self.srcDst)
            oprot.writeFieldEnd()
        if self.oper != None:
            oprot.writeFieldBegin('oper', TType.BYTE, 3)
            oprot.writeByte(self.oper)
            oprot.writeFieldEnd()
        if self.port1 != None:
            oprot.writeFieldBegin('port1', TType.I16, 4)
            oprot.writeI16(self.port1)
            oprot.writeFieldEnd()
        if self.port2 != None:
            oprot.writeFieldBegin('port2', TType.I16, 5)
            oprot.writeI16(self.port2)
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




class MatchTcpFlagsIDL(object):
    """
      TCP flags match
    
      Attributes:
       - sense
       - value
       - mask
       - match
      """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sense',
      None,
      None),
     (2,
      TType.I32,
      'value',
      None,
      None),
     (3,
      TType.I32,
      'mask',
      None,
      None),
     (4,
      TType.I32,
      'match',
      None,
      None))

    def __init__(self, sense = None, value = None, mask = None, match = None):
        self.sense = sense
        self.value = value
        self.mask = mask
        self.match = match



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
                    self.sense = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.value = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.mask = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.match = iprot.readI32()
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
        oprot.writeStructBegin('MatchTcpFlagsIDL')
        if self.sense != None:
            oprot.writeFieldBegin('sense', TType.I32, 1)
            oprot.writeI32(self.sense)
            oprot.writeFieldEnd()
        if self.value != None:
            oprot.writeFieldBegin('value', TType.I32, 2)
            oprot.writeI32(self.value)
            oprot.writeFieldEnd()
        if self.mask != None:
            oprot.writeFieldBegin('mask', TType.I32, 3)
            oprot.writeI32(self.mask)
            oprot.writeFieldEnd()
        if self.match != None:
            oprot.writeFieldBegin('match', TType.I32, 4)
            oprot.writeI32(self.match)
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




class MatchIcmpIDL(object):
    """
      ICMP match
    
      Attributes:
       - sense
       - type
       - code
       - protocol
      """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sense',
      None,
      None),
     (2,
      TType.I32,
      'type',
      None,
      None),
     (3,
      TType.I32,
      'code',
      None,
      None),
     (4,
      TType.I32,
      'protocol',
      None,
      None))

    def __init__(self, sense = None, type = None, code = None, protocol = None):
        self.sense = sense
        self.type = type
        self.code = code
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
                if ftype == TType.I32:
                    self.sense = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.code = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.protocol = iprot.readI32()
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
        oprot.writeStructBegin('MatchIcmpIDL')
        if self.sense != None:
            oprot.writeFieldBegin('sense', TType.I32, 1)
            oprot.writeI32(self.sense)
            oprot.writeFieldEnd()
        if self.type != None:
            oprot.writeFieldBegin('type', TType.I32, 2)
            oprot.writeI32(self.type)
            oprot.writeFieldEnd()
        if self.code != None:
            oprot.writeFieldBegin('code', TType.I32, 3)
            oprot.writeI32(self.code)
            oprot.writeFieldEnd()
        if self.protocol != None:
            oprot.writeFieldBegin('protocol', TType.I32, 4)
            oprot.writeI32(self.protocol)
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




class MatchTosIDL(object):
    """
      TOS match
    
      Attributes:
       - sense
       - tos
      """

    thrift_spec = (None, (1,
      TType.I32,
      'sense',
      None,
      None), (2,
      TType.LIST,
      'tos',
      (TType.BYTE, None),
      None))

    def __init__(self, sense = None, tos = None):
        self.sense = sense
        self.tos = tos



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
                    self.sense = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.tos = []
                    (_etype59, _size56,) = iprot.readListBegin()
                    for _i60 in xrange(_size56):
                        _elem61 = iprot.readByte()
                        self.tos.append(_elem61)

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
        oprot.writeStructBegin('MatchTosIDL')
        if self.sense != None:
            oprot.writeFieldBegin('sense', TType.I32, 1)
            oprot.writeI32(self.sense)
            oprot.writeFieldEnd()
        if self.tos != None:
            oprot.writeFieldBegin('tos', TType.LIST, 2)
            oprot.writeListBegin(TType.BYTE, len(self.tos))
            for iter62 in self.tos:
                oprot.writeByte(iter62)

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




class MatchPktLenIDL(object):
    """
      Packet Length match
    
      Attributes:
       - sense
       - min
       - max
      """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sense',
      None,
      None),
     (2,
      TType.I32,
      'min',
      None,
      None),
     (3,
      TType.I32,
      'max',
      None,
      None))

    def __init__(self, sense = None, min = None, max = None):
        self.sense = sense
        self.min = min
        self.max = max



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
                    self.sense = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.min = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.max = iprot.readI32()
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
        oprot.writeStructBegin('MatchPktLenIDL')
        if self.sense != None:
            oprot.writeFieldBegin('sense', TType.I32, 1)
            oprot.writeI32(self.sense)
            oprot.writeFieldEnd()
        if self.min != None:
            oprot.writeFieldBegin('min', TType.I32, 2)
            oprot.writeI32(self.min)
            oprot.writeFieldEnd()
        if self.max != None:
            oprot.writeFieldBegin('max', TType.I32, 3)
            oprot.writeI32(self.max)
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




class MatchQosGroupIDL(object):
    """
      QOS Group match
    
      Attributes:
       - sense
       - group
      """

    thrift_spec = (None, (1,
      TType.I32,
      'sense',
      None,
      None), (2,
      TType.I16,
      'group',
      None,
      None))

    def __init__(self, sense = None, group = None):
        self.sense = sense
        self.group = group



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
                    self.sense = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I16:
                    self.group = iprot.readI16()
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
        oprot.writeStructBegin('MatchQosGroupIDL')
        if self.sense != None:
            oprot.writeFieldBegin('sense', TType.I32, 1)
            oprot.writeI32(self.sense)
            oprot.writeFieldEnd()
        if self.group != None:
            oprot.writeFieldBegin('group', TType.I16, 2)
            oprot.writeI16(self.group)
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




class MatchDscpIDL(object):
    """
      DSCP match
    
      Attributes:
       - sense
       - dscp
      """

    thrift_spec = (None, (1,
      TType.I32,
      'sense',
      None,
      None), (2,
      TType.LIST,
      'dscp',
      (TType.BYTE, None),
      None))

    def __init__(self, sense = None, dscp = None):
        self.sense = sense
        self.dscp = dscp



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
                    self.sense = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.dscp = []
                    (_etype66, _size63,) = iprot.readListBegin()
                    for _i67 in xrange(_size63):
                        _elem68 = iprot.readByte()
                        self.dscp.append(_elem68)

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
        oprot.writeStructBegin('MatchDscpIDL')
        if self.sense != None:
            oprot.writeFieldBegin('sense', TType.I32, 1)
            oprot.writeI32(self.sense)
            oprot.writeFieldEnd()
        if self.dscp != None:
            oprot.writeFieldBegin('dscp', TType.LIST, 2)
            oprot.writeListBegin(TType.BYTE, len(self.dscp))
            for iter69 in self.dscp:
                oprot.writeByte(iter69)

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




class MatchL2CosIDL(object):
    """
      L2 COS match
    
      Attributes:
       - sense
       - l2cos
      """

    thrift_spec = (None, (1,
      TType.I32,
      'sense',
      None,
      None), (2,
      TType.LIST,
      'l2cos',
      (TType.BYTE, None),
      None))

    def __init__(self, sense = None, l2cos = None):
        self.sense = sense
        self.l2cos = l2cos



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
                    self.sense = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.l2cos = []
                    (_etype73, _size70,) = iprot.readListBegin()
                    for _i74 in xrange(_size70):
                        _elem75 = iprot.readByte()
                        self.l2cos.append(_elem75)

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
        oprot.writeStructBegin('MatchL2CosIDL')
        if self.sense != None:
            oprot.writeFieldBegin('sense', TType.I32, 1)
            oprot.writeI32(self.sense)
            oprot.writeFieldEnd()
        if self.l2cos != None:
            oprot.writeFieldBegin('l2cos', TType.LIST, 2)
            oprot.writeListBegin(TType.BYTE, len(self.l2cos))
            for iter76 in self.l2cos:
                oprot.writeByte(iter76)

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




class MatchMplsExpIDL(object):
    """
      MPLS Experimantal tag match
    
      Attributes:
       - sense
       - mplsExp
      """

    thrift_spec = (None, (1,
      TType.I32,
      'sense',
      None,
      None), (2,
      TType.LIST,
      'mplsExp',
      (TType.I32, None),
      None))

    def __init__(self, sense = None, mplsExp = None):
        self.sense = sense
        self.mplsExp = mplsExp



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
                    self.sense = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.mplsExp = []
                    (_etype80, _size77,) = iprot.readListBegin()
                    for _i81 in xrange(_size77):
                        _elem82 = iprot.readI32()
                        self.mplsExp.append(_elem82)

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
        oprot.writeStructBegin('MatchMplsExpIDL')
        if self.sense != None:
            oprot.writeFieldBegin('sense', TType.I32, 1)
            oprot.writeI32(self.sense)
            oprot.writeFieldEnd()
        if self.mplsExp != None:
            oprot.writeFieldBegin('mplsExp', TType.LIST, 2)
            oprot.writeListBegin(TType.I32, len(self.mplsExp))
            for iter83 in self.mplsExp:
                oprot.writeI32(iter83)

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




class MatchProtocolIDL(object):
    """
      Protocol match
    
      Attributes:
       - sense
       - protocol
      """

    thrift_spec = (None, (1,
      TType.I32,
      'sense',
      None,
      None), (2,
      TType.I16,
      'protocol',
      None,
      None))

    def __init__(self, sense = None, protocol = None):
        self.sense = sense
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
                if ftype == TType.I32:
                    self.sense = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
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
        oprot.writeStructBegin('MatchProtocolIDL')
        if self.sense != None:
            oprot.writeFieldBegin('sense', TType.I32, 1)
            oprot.writeI32(self.sense)
            oprot.writeFieldEnd()
        if self.protocol != None:
            oprot.writeFieldBegin('protocol', TType.I16, 2)
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




class MatchApplicationIDL(object):
    """
      NBAR Application match
    
      Attributes:
       - sense
       - protocol
       - subProtocol
       - param
      """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sense',
      None,
      None),
     (2,
      TType.STRING,
      'protocol',
      None,
      None),
     (3,
      TType.STRING,
      'subProtocol',
      None,
      None),
     (4,
      TType.STRING,
      'param',
      None,
      None))

    def __init__(self, sense = None, protocol = None, subProtocol = None, param = None):
        self.sense = sense
        self.protocol = protocol
        self.subProtocol = subProtocol
        self.param = param



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
                    self.sense = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.protocol = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.subProtocol = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.param = iprot.readString()
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
        oprot.writeStructBegin('MatchApplicationIDL')
        if self.sense != None:
            oprot.writeFieldBegin('sense', TType.I32, 1)
            oprot.writeI32(self.sense)
            oprot.writeFieldEnd()
        if self.protocol != None:
            oprot.writeFieldBegin('protocol', TType.STRING, 2)
            oprot.writeString(self.protocol)
            oprot.writeFieldEnd()
        if self.subProtocol != None:
            oprot.writeFieldBegin('subProtocol', TType.STRING, 3)
            oprot.writeString(self.subProtocol)
            oprot.writeFieldEnd()
        if self.param != None:
            oprot.writeFieldBegin('param', TType.STRING, 4)
            oprot.writeString(self.param)
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




class MatchRtpPortIDL(object):
    """
      RTP Port match
    
      Attributes:
       - sense
       - port1
       - port2
      """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sense',
      None,
      None),
     (2,
      TType.I32,
      'port1',
      None,
      None),
     (3,
      TType.I32,
      'port2',
      None,
      None))

    def __init__(self, sense = None, port1 = None, port2 = None):
        self.sense = sense
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
                    self.sense = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.port1 = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
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
        oprot.writeStructBegin('MatchRtpPortIDL')
        if self.sense != None:
            oprot.writeFieldBegin('sense', TType.I32, 1)
            oprot.writeI32(self.sense)
            oprot.writeFieldEnd()
        if self.port1 != None:
            oprot.writeFieldBegin('port1', TType.I32, 2)
            oprot.writeI32(self.port1)
            oprot.writeFieldEnd()
        if self.port2 != None:
            oprot.writeFieldBegin('port2', TType.I32, 3)
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




class MatchVlanIDL(object):
    """
      VLAN match
    
      Attributes:
       - sense
       - vlan
      """

    thrift_spec = (None, (1,
      TType.I32,
      'sense',
      None,
      None), (2,
      TType.LIST,
      'vlan',
      (TType.I16, None),
      None))

    def __init__(self, sense = None, vlan = None):
        self.sense = sense
        self.vlan = vlan



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
                    self.sense = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.vlan = []
                    (_etype87, _size84,) = iprot.readListBegin()
                    for _i88 in xrange(_size84):
                        _elem89 = iprot.readI16()
                        self.vlan.append(_elem89)

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
        oprot.writeStructBegin('MatchVlanIDL')
        if self.sense != None:
            oprot.writeFieldBegin('sense', TType.I32, 1)
            oprot.writeI32(self.sense)
            oprot.writeFieldEnd()
        if self.vlan != None:
            oprot.writeFieldBegin('vlan', TType.LIST, 2)
            oprot.writeListBegin(TType.I16, len(self.vlan))
            for iter90 in self.vlan:
                oprot.writeI16(iter90)

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




class MatchMplsLblIDL(object):
    """
      MPLS Label match
    
      Attributes:
       - sense
       - mplsLbl
      """

    thrift_spec = (None, (1,
      TType.I32,
      'sense',
      None,
      None), (2,
      TType.LIST,
      'mplsLbl',
      (TType.I32, None),
      None))

    def __init__(self, sense = None, mplsLbl = None):
        self.sense = sense
        self.mplsLbl = mplsLbl



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
                    self.sense = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.mplsLbl = []
                    (_etype94, _size91,) = iprot.readListBegin()
                    for _i95 in xrange(_size91):
                        _elem96 = iprot.readI32()
                        self.mplsLbl.append(_elem96)

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
        oprot.writeStructBegin('MatchMplsLblIDL')
        if self.sense != None:
            oprot.writeFieldBegin('sense', TType.I32, 1)
            oprot.writeI32(self.sense)
            oprot.writeFieldEnd()
        if self.mplsLbl != None:
            oprot.writeFieldBegin('mplsLbl', TType.LIST, 2)
            oprot.writeListBegin(TType.I32, len(self.mplsLbl))
            for iter97 in self.mplsLbl:
                oprot.writeI32(iter97)

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




class MatchMplsTcIDL(object):
    """
      MPLS Traffic Class match
    
      Attributes:
       - sense
       - mplsTc
      """

    thrift_spec = (None, (1,
      TType.I32,
      'sense',
      None,
      None), (2,
      TType.LIST,
      'mplsTc',
      (TType.BYTE, None),
      None))

    def __init__(self, sense = None, mplsTc = None):
        self.sense = sense
        self.mplsTc = mplsTc



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
                    self.sense = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.mplsTc = []
                    (_etype101, _size98,) = iprot.readListBegin()
                    for _i102 in xrange(_size98):
                        _elem103 = iprot.readByte()
                        self.mplsTc.append(_elem103)

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
        oprot.writeStructBegin('MatchMplsTcIDL')
        if self.sense != None:
            oprot.writeFieldBegin('sense', TType.I32, 1)
            oprot.writeI32(self.sense)
            oprot.writeFieldEnd()
        if self.mplsTc != None:
            oprot.writeFieldBegin('mplsTc', TType.LIST, 2)
            oprot.writeListBegin(TType.BYTE, len(self.mplsTc))
            for iter104 in self.mplsTc:
                oprot.writeByte(iter104)

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




class MatchFlowLabelIDL(object):
    """
      Flow Label match
    
      Attributes:
       - sense
       - flowLbl
      """

    thrift_spec = (None, (1,
      TType.I32,
      'sense',
      None,
      None), (2,
      TType.LIST,
      'flowLbl',
      (TType.I32, None),
      None))

    def __init__(self, sense = None, flowLbl = None):
        self.sense = sense
        self.flowLbl = flowLbl



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
                    self.sense = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.flowLbl = []
                    (_etype108, _size105,) = iprot.readListBegin()
                    for _i109 in xrange(_size105):
                        _elem110 = iprot.readI32()
                        self.flowLbl.append(_elem110)

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
        oprot.writeStructBegin('MatchFlowLabelIDL')
        if self.sense != None:
            oprot.writeFieldBegin('sense', TType.I32, 1)
            oprot.writeI32(self.sense)
            oprot.writeFieldEnd()
        if self.flowLbl != None:
            oprot.writeFieldBegin('flowLbl', TType.LIST, 2)
            oprot.writeListBegin(TType.I32, len(self.flowLbl))
            for iter111 in self.flowLbl:
                oprot.writeI32(iter111)

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




class MatchNdTargetAddrIDL(object):
    """
      ND Target Address match
    
      Attributes:
       - sense
       - targetAddr
      """

    thrift_spec = (None, (1,
      TType.I32,
      'sense',
      None,
      None), (2,
      TType.LIST,
      'targetAddr',
      (TType.BYTE, None),
      None))

    def __init__(self, sense = None, targetAddr = None):
        self.sense = sense
        self.targetAddr = targetAddr



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
                    self.sense = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.targetAddr = []
                    (_etype115, _size112,) = iprot.readListBegin()
                    for _i116 in xrange(_size112):
                        _elem117 = iprot.readByte()
                        self.targetAddr.append(_elem117)

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
        oprot.writeStructBegin('MatchNdTargetAddrIDL')
        if self.sense != None:
            oprot.writeFieldBegin('sense', TType.I32, 1)
            oprot.writeI32(self.sense)
            oprot.writeFieldEnd()
        if self.targetAddr != None:
            oprot.writeFieldBegin('targetAddr', TType.LIST, 2)
            oprot.writeListBegin(TType.BYTE, len(self.targetAddr))
            for iter118 in self.targetAddr:
                oprot.writeByte(iter118)

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




class MatchEtypeIDL(object):
    """
      Ethertype match
    
      Attributes:
       - sense
       - etype
      """

    thrift_spec = (None, (1,
      TType.I32,
      'sense',
      None,
      None), (2,
      TType.I32,
      'etype',
      None,
      None))

    def __init__(self, sense = None, etype = None):
        self.sense = sense
        self.etype = etype



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
                    self.sense = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.etype = iprot.readI32()
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
        oprot.writeStructBegin('MatchEtypeIDL')
        if self.sense != None:
            oprot.writeFieldBegin('sense', TType.I32, 1)
            oprot.writeI32(self.sense)
            oprot.writeFieldEnd()
        if self.etype != None:
            oprot.writeFieldBegin('etype', TType.I32, 2)
            oprot.writeI32(self.etype)
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




class MatchTtlIDL(object):
    """
      TTL match
    
      Attributes:
       - sense
       - ttl
       - mask
      """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sense',
      None,
      None),
     (2,
      TType.BYTE,
      'ttl',
      None,
      None),
     (3,
      TType.BYTE,
      'mask',
      None,
      None))

    def __init__(self, sense = None, ttl = None, mask = None):
        self.sense = sense
        self.ttl = ttl
        self.mask = mask



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
                    self.sense = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.BYTE:
                    self.ttl = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.BYTE:
                    self.mask = iprot.readByte()
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
        oprot.writeStructBegin('MatchTtlIDL')
        if self.sense != None:
            oprot.writeFieldBegin('sense', TType.I32, 1)
            oprot.writeI32(self.sense)
            oprot.writeFieldEnd()
        if self.ttl != None:
            oprot.writeFieldBegin('ttl', TType.BYTE, 2)
            oprot.writeByte(self.ttl)
            oprot.writeFieldEnd()
        if self.mask != None:
            oprot.writeFieldBegin('mask', TType.BYTE, 3)
            oprot.writeByte(self.mask)
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




class MatchIDL(object):
    """
      Match
    
      Attributes:
       - dsid
       - matchHandle
       - opCode
       - opId
       - matchType
       - ifcMatch
       - aclMatch
       - qosGroupMatch
       - dscpMatch
       - mplsExpMatch
       - l2cosMatch
       - macAddressMatch
       - ipAddressMatch
       - pktLenMatch
       - protocolMatch
       - appMatch
       - rtpPortMatch
       - vlanMatch
       - tcpPortMatch
       - tcpMatch
       - etypeMatch
       - ttlMatch
       - icmpMatch
       - tosMatch
       - mplsLblMatch
       - mplsTcMatch
       - flowLabelMatch
       - ndTargetAddrMatch
      """

    thrift_spec = (None,
     (1,
      TType.I32,
      'dsid',
      None,
      None),
     (2,
      TType.I64,
      'matchHandle',
      None,
      None),
     (3,
      TType.I16,
      'opCode',
      None,
      None),
     (4,
      TType.I32,
      'opId',
      None,
      None),
     (5,
      TType.I32,
      'matchType',
      None,
      None),
     (6,
      TType.STRUCT,
      'ifcMatch',
      (MatchInterfaceIDL, MatchInterfaceIDL.thrift_spec),
      None),
     (7,
      TType.STRUCT,
      'aclMatch',
      (MatchAclIDL, MatchAclIDL.thrift_spec),
      None),
     (8,
      TType.STRUCT,
      'qosGroupMatch',
      (MatchQosGroupIDL, MatchQosGroupIDL.thrift_spec),
      None),
     (9,
      TType.STRUCT,
      'dscpMatch',
      (MatchDscpIDL, MatchDscpIDL.thrift_spec),
      None),
     (10,
      TType.STRUCT,
      'mplsExpMatch',
      (MatchMplsExpIDL, MatchMplsExpIDL.thrift_spec),
      None),
     (11,
      TType.STRUCT,
      'l2cosMatch',
      (MatchL2CosIDL, MatchL2CosIDL.thrift_spec),
      None),
     (12,
      TType.STRUCT,
      'macAddressMatch',
      (MatchMacAddressIDL, MatchMacAddressIDL.thrift_spec),
      None),
     (13,
      TType.STRUCT,
      'ipAddressMatch',
      (MatchIpAddressIDL, MatchIpAddressIDL.thrift_spec),
      None),
     (14,
      TType.STRUCT,
      'pktLenMatch',
      (MatchPktLenIDL, MatchPktLenIDL.thrift_spec),
      None),
     (15,
      TType.STRUCT,
      'protocolMatch',
      (MatchProtocolIDL, MatchProtocolIDL.thrift_spec),
      None),
     (16,
      TType.STRUCT,
      'appMatch',
      (MatchApplicationIDL, MatchApplicationIDL.thrift_spec),
      None),
     (17,
      TType.STRUCT,
      'rtpPortMatch',
      (MatchRtpPortIDL, MatchRtpPortIDL.thrift_spec),
      None),
     (18,
      TType.STRUCT,
      'vlanMatch',
      (MatchVlanIDL, MatchVlanIDL.thrift_spec),
      None),
     (19,
      TType.STRUCT,
      'tcpPortMatch',
      (MatchTcpPortIDL, MatchTcpPortIDL.thrift_spec),
      None),
     (20,
      TType.STRUCT,
      'tcpMatch',
      (MatchTcpFlagsIDL, MatchTcpFlagsIDL.thrift_spec),
      None),
     (21,
      TType.STRUCT,
      'etypeMatch',
      (MatchEtypeIDL, MatchEtypeIDL.thrift_spec),
      None),
     (22,
      TType.STRUCT,
      'ttlMatch',
      (MatchTtlIDL, MatchTtlIDL.thrift_spec),
      None),
     (23,
      TType.STRUCT,
      'icmpMatch',
      (MatchIcmpIDL, MatchIcmpIDL.thrift_spec),
      None),
     (24,
      TType.STRUCT,
      'tosMatch',
      (MatchTosIDL, MatchTosIDL.thrift_spec),
      None),
     (25,
      TType.STRUCT,
      'mplsLblMatch',
      (MatchMplsLblIDL, MatchMplsLblIDL.thrift_spec),
      None),
     (26,
      TType.STRUCT,
      'mplsTcMatch',
      (MatchMplsTcIDL, MatchMplsTcIDL.thrift_spec),
      None),
     (27,
      TType.STRUCT,
      'flowLabelMatch',
      (MatchFlowLabelIDL, MatchFlowLabelIDL.thrift_spec),
      None),
     (28,
      TType.STRUCT,
      'ndTargetAddrMatch',
      (MatchNdTargetAddrIDL, MatchNdTargetAddrIDL.thrift_spec),
      None))

    def __init__(self, dsid = None, matchHandle = None, opCode = None, opId = None, matchType = None, ifcMatch = None, aclMatch = None, qosGroupMatch = None, dscpMatch = None, mplsExpMatch = None, l2cosMatch = None, macAddressMatch = None, ipAddressMatch = None, pktLenMatch = None, protocolMatch = None, appMatch = None, rtpPortMatch = None, vlanMatch = None, tcpPortMatch = None, tcpMatch = None, etypeMatch = None, ttlMatch = None, icmpMatch = None, tosMatch = None, mplsLblMatch = None, mplsTcMatch = None, flowLabelMatch = None, ndTargetAddrMatch = None):
        self.dsid = dsid
        self.matchHandle = matchHandle
        self.opCode = opCode
        self.opId = opId
        self.matchType = matchType
        self.ifcMatch = ifcMatch
        self.aclMatch = aclMatch
        self.qosGroupMatch = qosGroupMatch
        self.dscpMatch = dscpMatch
        self.mplsExpMatch = mplsExpMatch
        self.l2cosMatch = l2cosMatch
        self.macAddressMatch = macAddressMatch
        self.ipAddressMatch = ipAddressMatch
        self.pktLenMatch = pktLenMatch
        self.protocolMatch = protocolMatch
        self.appMatch = appMatch
        self.rtpPortMatch = rtpPortMatch
        self.vlanMatch = vlanMatch
        self.tcpPortMatch = tcpPortMatch
        self.tcpMatch = tcpMatch
        self.etypeMatch = etypeMatch
        self.ttlMatch = ttlMatch
        self.icmpMatch = icmpMatch
        self.tosMatch = tosMatch
        self.mplsLblMatch = mplsLblMatch
        self.mplsTcMatch = mplsTcMatch
        self.flowLabelMatch = flowLabelMatch
        self.ndTargetAddrMatch = ndTargetAddrMatch



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
                    self.dsid = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.matchHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I16:
                    self.opCode = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.opId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.matchType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRUCT:
                    self.ifcMatch = MatchInterfaceIDL()
                    self.ifcMatch.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.STRUCT:
                    self.aclMatch = MatchAclIDL()
                    self.aclMatch.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.STRUCT:
                    self.qosGroupMatch = MatchQosGroupIDL()
                    self.qosGroupMatch.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.STRUCT:
                    self.dscpMatch = MatchDscpIDL()
                    self.dscpMatch.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.STRUCT:
                    self.mplsExpMatch = MatchMplsExpIDL()
                    self.mplsExpMatch.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.STRUCT:
                    self.l2cosMatch = MatchL2CosIDL()
                    self.l2cosMatch.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 12:
                if ftype == TType.STRUCT:
                    self.macAddressMatch = MatchMacAddressIDL()
                    self.macAddressMatch.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 13:
                if ftype == TType.STRUCT:
                    self.ipAddressMatch = MatchIpAddressIDL()
                    self.ipAddressMatch.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 14:
                if ftype == TType.STRUCT:
                    self.pktLenMatch = MatchPktLenIDL()
                    self.pktLenMatch.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 15:
                if ftype == TType.STRUCT:
                    self.protocolMatch = MatchProtocolIDL()
                    self.protocolMatch.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 16:
                if ftype == TType.STRUCT:
                    self.appMatch = MatchApplicationIDL()
                    self.appMatch.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 17:
                if ftype == TType.STRUCT:
                    self.rtpPortMatch = MatchRtpPortIDL()
                    self.rtpPortMatch.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 18:
                if ftype == TType.STRUCT:
                    self.vlanMatch = MatchVlanIDL()
                    self.vlanMatch.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 19:
                if ftype == TType.STRUCT:
                    self.tcpPortMatch = MatchTcpPortIDL()
                    self.tcpPortMatch.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 20:
                if ftype == TType.STRUCT:
                    self.tcpMatch = MatchTcpFlagsIDL()
                    self.tcpMatch.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 21:
                if ftype == TType.STRUCT:
                    self.etypeMatch = MatchEtypeIDL()
                    self.etypeMatch.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 22:
                if ftype == TType.STRUCT:
                    self.ttlMatch = MatchTtlIDL()
                    self.ttlMatch.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 23:
                if ftype == TType.STRUCT:
                    self.icmpMatch = MatchIcmpIDL()
                    self.icmpMatch.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 24:
                if ftype == TType.STRUCT:
                    self.tosMatch = MatchTosIDL()
                    self.tosMatch.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 25:
                if ftype == TType.STRUCT:
                    self.mplsLblMatch = MatchMplsLblIDL()
                    self.mplsLblMatch.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 26:
                if ftype == TType.STRUCT:
                    self.mplsTcMatch = MatchMplsTcIDL()
                    self.mplsTcMatch.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 27:
                if ftype == TType.STRUCT:
                    self.flowLabelMatch = MatchFlowLabelIDL()
                    self.flowLabelMatch.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 28:
                if ftype == TType.STRUCT:
                    self.ndTargetAddrMatch = MatchNdTargetAddrIDL()
                    self.ndTargetAddrMatch.read(iprot)
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
        oprot.writeStructBegin('MatchIDL')
        if self.dsid != None:
            oprot.writeFieldBegin('dsid', TType.I32, 1)
            oprot.writeI32(self.dsid)
            oprot.writeFieldEnd()
        if self.matchHandle != None:
            oprot.writeFieldBegin('matchHandle', TType.I64, 2)
            oprot.writeI64(self.matchHandle)
            oprot.writeFieldEnd()
        if self.opCode != None:
            oprot.writeFieldBegin('opCode', TType.I16, 3)
            oprot.writeI16(self.opCode)
            oprot.writeFieldEnd()
        if self.opId != None:
            oprot.writeFieldBegin('opId', TType.I32, 4)
            oprot.writeI32(self.opId)
            oprot.writeFieldEnd()
        if self.matchType != None:
            oprot.writeFieldBegin('matchType', TType.I32, 5)
            oprot.writeI32(self.matchType)
            oprot.writeFieldEnd()
        if self.ifcMatch != None:
            oprot.writeFieldBegin('ifcMatch', TType.STRUCT, 6)
            self.ifcMatch.write(oprot)
            oprot.writeFieldEnd()
        if self.aclMatch != None:
            oprot.writeFieldBegin('aclMatch', TType.STRUCT, 7)
            self.aclMatch.write(oprot)
            oprot.writeFieldEnd()
        if self.qosGroupMatch != None:
            oprot.writeFieldBegin('qosGroupMatch', TType.STRUCT, 8)
            self.qosGroupMatch.write(oprot)
            oprot.writeFieldEnd()
        if self.dscpMatch != None:
            oprot.writeFieldBegin('dscpMatch', TType.STRUCT, 9)
            self.dscpMatch.write(oprot)
            oprot.writeFieldEnd()
        if self.mplsExpMatch != None:
            oprot.writeFieldBegin('mplsExpMatch', TType.STRUCT, 10)
            self.mplsExpMatch.write(oprot)
            oprot.writeFieldEnd()
        if self.l2cosMatch != None:
            oprot.writeFieldBegin('l2cosMatch', TType.STRUCT, 11)
            self.l2cosMatch.write(oprot)
            oprot.writeFieldEnd()
        if self.macAddressMatch != None:
            oprot.writeFieldBegin('macAddressMatch', TType.STRUCT, 12)
            self.macAddressMatch.write(oprot)
            oprot.writeFieldEnd()
        if self.ipAddressMatch != None:
            oprot.writeFieldBegin('ipAddressMatch', TType.STRUCT, 13)
            self.ipAddressMatch.write(oprot)
            oprot.writeFieldEnd()
        if self.pktLenMatch != None:
            oprot.writeFieldBegin('pktLenMatch', TType.STRUCT, 14)
            self.pktLenMatch.write(oprot)
            oprot.writeFieldEnd()
        if self.protocolMatch != None:
            oprot.writeFieldBegin('protocolMatch', TType.STRUCT, 15)
            self.protocolMatch.write(oprot)
            oprot.writeFieldEnd()
        if self.appMatch != None:
            oprot.writeFieldBegin('appMatch', TType.STRUCT, 16)
            self.appMatch.write(oprot)
            oprot.writeFieldEnd()
        if self.rtpPortMatch != None:
            oprot.writeFieldBegin('rtpPortMatch', TType.STRUCT, 17)
            self.rtpPortMatch.write(oprot)
            oprot.writeFieldEnd()
        if self.vlanMatch != None:
            oprot.writeFieldBegin('vlanMatch', TType.STRUCT, 18)
            self.vlanMatch.write(oprot)
            oprot.writeFieldEnd()
        if self.tcpPortMatch != None:
            oprot.writeFieldBegin('tcpPortMatch', TType.STRUCT, 19)
            self.tcpPortMatch.write(oprot)
            oprot.writeFieldEnd()
        if self.tcpMatch != None:
            oprot.writeFieldBegin('tcpMatch', TType.STRUCT, 20)
            self.tcpMatch.write(oprot)
            oprot.writeFieldEnd()
        if self.etypeMatch != None:
            oprot.writeFieldBegin('etypeMatch', TType.STRUCT, 21)
            self.etypeMatch.write(oprot)
            oprot.writeFieldEnd()
        if self.ttlMatch != None:
            oprot.writeFieldBegin('ttlMatch', TType.STRUCT, 22)
            self.ttlMatch.write(oprot)
            oprot.writeFieldEnd()
        if self.icmpMatch != None:
            oprot.writeFieldBegin('icmpMatch', TType.STRUCT, 23)
            self.icmpMatch.write(oprot)
            oprot.writeFieldEnd()
        if self.tosMatch != None:
            oprot.writeFieldBegin('tosMatch', TType.STRUCT, 24)
            self.tosMatch.write(oprot)
            oprot.writeFieldEnd()
        if self.mplsLblMatch != None:
            oprot.writeFieldBegin('mplsLblMatch', TType.STRUCT, 25)
            self.mplsLblMatch.write(oprot)
            oprot.writeFieldEnd()
        if self.mplsTcMatch != None:
            oprot.writeFieldBegin('mplsTcMatch', TType.STRUCT, 26)
            self.mplsTcMatch.write(oprot)
            oprot.writeFieldEnd()
        if self.flowLabelMatch != None:
            oprot.writeFieldBegin('flowLabelMatch', TType.STRUCT, 27)
            self.flowLabelMatch.write(oprot)
            oprot.writeFieldEnd()
        if self.ndTargetAddrMatch != None:
            oprot.writeFieldBegin('ndTargetAddrMatch', TType.STRUCT, 28)
            self.ndTargetAddrMatch.write(oprot)
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




class ActionIDL(object):
    """
      Action
    
      Attributes:
       - dsid
       - actionHandle
       - opCode
       - opId
       - actionType
       - outIfAction
       - markAction
       - macAction
       - nhAction
       - policeAction
       - shapeAction
       - pqAction
       - cqAction
       - fqAction
       - wredProfile
       - pktCopyAction
       - pktDivertAction
       - vlanAction
       - parameterMapName
       - wredParam
       - fwdClassIdAction
       - ipAddressAction
       - mplsExpAction
       - tcpPortAction
       - queueLimitAction
       - protocolAction
       - ttlAction
       - mplsAction
       - outputAction
       - gotoTableAction
      """

    thrift_spec = (None,
     (1,
      TType.I32,
      'dsid',
      None,
      None),
     (2,
      TType.I64,
      'actionHandle',
      None,
      None),
     (3,
      TType.I16,
      'opCode',
      None,
      None),
     (4,
      TType.I32,
      'opId',
      None,
      None),
     (5,
      TType.I32,
      'actionType',
      None,
      None),
     (6,
      TType.STRUCT,
      'outIfAction',
      (ActionOutInterfaceIDL, ActionOutInterfaceIDL.thrift_spec),
      None),
     (7,
      TType.STRUCT,
      'markAction',
      (ActionMarkIDL, ActionMarkIDL.thrift_spec),
      None),
     (8,
      TType.STRUCT,
      'macAction',
      (ActionMacAddressIDL, ActionMacAddressIDL.thrift_spec),
      None),
     (9,
      TType.STRUCT,
      'nhAction',
      (ActionNextHopIDL, ActionNextHopIDL.thrift_spec),
      None),
     (10,
      TType.STRUCT,
      'policeAction',
      (ActionPoliceIDL, ActionPoliceIDL.thrift_spec),
      None),
     (11,
      TType.STRUCT,
      'shapeAction',
      (ActionShapeIDL, ActionShapeIDL.thrift_spec),
      None),
     (12,
      TType.STRUCT,
      'pqAction',
      (ActionPriorityQueueIDL, ActionPriorityQueueIDL.thrift_spec),
      None),
     (13,
      TType.STRUCT,
      'cqAction',
      (ActionClassQueueIDL, ActionClassQueueIDL.thrift_spec),
      None),
     (14,
      TType.STRUCT,
      'fqAction',
      (ActionFairQueueIDL, ActionFairQueueIDL.thrift_spec),
      None),
     (15,
      TType.STRUCT,
      'wredProfile',
      (ActionWredProfileIDL, ActionWredProfileIDL.thrift_spec),
      None),
     (16,
      TType.STRUCT,
      'pktCopyAction',
      (ActionPktCopyIDL, ActionPktCopyIDL.thrift_spec),
      None),
     (17,
      TType.STRUCT,
      'pktDivertAction',
      (ActionPktDivertIDL, ActionPktDivertIDL.thrift_spec),
      None),
     (18,
      TType.STRUCT,
      'vlanAction',
      (ActionVlanIDL, ActionVlanIDL.thrift_spec),
      None),
     (19,
      TType.STRING,
      'parameterMapName',
      None,
      None),
     (20,
      TType.STRUCT,
      'wredParam',
      (ActionWredParamIDL, ActionWredParamIDL.thrift_spec),
      None),
     (21,
      TType.STRUCT,
      'fwdClassIdAction',
      (ActionFwdClassIdIDL, ActionFwdClassIdIDL.thrift_spec),
      None),
     (22,
      TType.STRUCT,
      'ipAddressAction',
      (ActionIpAddressIDL, ActionIpAddressIDL.thrift_spec),
      None),
     (23,
      TType.STRUCT,
      'mplsExpAction',
      (ActionMplsExpIDL, ActionMplsExpIDL.thrift_spec),
      None),
     (24,
      TType.STRUCT,
      'tcpPortAction',
      (ActionTcpPortIDL, ActionTcpPortIDL.thrift_spec),
      None),
     (25,
      TType.STRUCT,
      'queueLimitAction',
      (ActionQueueLimitIDL, ActionQueueLimitIDL.thrift_spec),
      None),
     (26,
      TType.STRUCT,
      'protocolAction',
      (ActionProtocolIDL, ActionProtocolIDL.thrift_spec),
      None),
     (27,
      TType.STRUCT,
      'ttlAction',
      (ActionTtlIDL, ActionTtlIDL.thrift_spec),
      None),
     (28,
      TType.STRUCT,
      'mplsAction',
      (ActionMplsIDL, ActionMplsIDL.thrift_spec),
      None),
     (29,
      TType.STRUCT,
      'outputAction',
      (ActionOutputIDL, ActionOutputIDL.thrift_spec),
      None),
     (30,
      TType.STRUCT,
      'gotoTableAction',
      (ActionGotoTableIDL, ActionGotoTableIDL.thrift_spec),
      None))

    def __init__(self, dsid = None, actionHandle = None, opCode = None, opId = None, actionType = None, outIfAction = None, markAction = None, macAction = None, nhAction = None, policeAction = None, shapeAction = None, pqAction = None, cqAction = None, fqAction = None, wredProfile = None, pktCopyAction = None, pktDivertAction = None, vlanAction = None, parameterMapName = None, wredParam = None, fwdClassIdAction = None, ipAddressAction = None, mplsExpAction = None, tcpPortAction = None, queueLimitAction = None, protocolAction = None, ttlAction = None, mplsAction = None, outputAction = None, gotoTableAction = None):
        self.dsid = dsid
        self.actionHandle = actionHandle
        self.opCode = opCode
        self.opId = opId
        self.actionType = actionType
        self.outIfAction = outIfAction
        self.markAction = markAction
        self.macAction = macAction
        self.nhAction = nhAction
        self.policeAction = policeAction
        self.shapeAction = shapeAction
        self.pqAction = pqAction
        self.cqAction = cqAction
        self.fqAction = fqAction
        self.wredProfile = wredProfile
        self.pktCopyAction = pktCopyAction
        self.pktDivertAction = pktDivertAction
        self.vlanAction = vlanAction
        self.parameterMapName = parameterMapName
        self.wredParam = wredParam
        self.fwdClassIdAction = fwdClassIdAction
        self.ipAddressAction = ipAddressAction
        self.mplsExpAction = mplsExpAction
        self.tcpPortAction = tcpPortAction
        self.queueLimitAction = queueLimitAction
        self.protocolAction = protocolAction
        self.ttlAction = ttlAction
        self.mplsAction = mplsAction
        self.outputAction = outputAction
        self.gotoTableAction = gotoTableAction



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
                    self.dsid = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.actionHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I16:
                    self.opCode = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.opId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.actionType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRUCT:
                    self.outIfAction = ActionOutInterfaceIDL()
                    self.outIfAction.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.STRUCT:
                    self.markAction = ActionMarkIDL()
                    self.markAction.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.STRUCT:
                    self.macAction = ActionMacAddressIDL()
                    self.macAction.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.STRUCT:
                    self.nhAction = ActionNextHopIDL()
                    self.nhAction.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.STRUCT:
                    self.policeAction = ActionPoliceIDL()
                    self.policeAction.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.STRUCT:
                    self.shapeAction = ActionShapeIDL()
                    self.shapeAction.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 12:
                if ftype == TType.STRUCT:
                    self.pqAction = ActionPriorityQueueIDL()
                    self.pqAction.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 13:
                if ftype == TType.STRUCT:
                    self.cqAction = ActionClassQueueIDL()
                    self.cqAction.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 14:
                if ftype == TType.STRUCT:
                    self.fqAction = ActionFairQueueIDL()
                    self.fqAction.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 15:
                if ftype == TType.STRUCT:
                    self.wredProfile = ActionWredProfileIDL()
                    self.wredProfile.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 16:
                if ftype == TType.STRUCT:
                    self.pktCopyAction = ActionPktCopyIDL()
                    self.pktCopyAction.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 17:
                if ftype == TType.STRUCT:
                    self.pktDivertAction = ActionPktDivertIDL()
                    self.pktDivertAction.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 18:
                if ftype == TType.STRUCT:
                    self.vlanAction = ActionVlanIDL()
                    self.vlanAction.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 19:
                if ftype == TType.STRING:
                    self.parameterMapName = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 20:
                if ftype == TType.STRUCT:
                    self.wredParam = ActionWredParamIDL()
                    self.wredParam.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 21:
                if ftype == TType.STRUCT:
                    self.fwdClassIdAction = ActionFwdClassIdIDL()
                    self.fwdClassIdAction.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 22:
                if ftype == TType.STRUCT:
                    self.ipAddressAction = ActionIpAddressIDL()
                    self.ipAddressAction.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 23:
                if ftype == TType.STRUCT:
                    self.mplsExpAction = ActionMplsExpIDL()
                    self.mplsExpAction.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 24:
                if ftype == TType.STRUCT:
                    self.tcpPortAction = ActionTcpPortIDL()
                    self.tcpPortAction.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 25:
                if ftype == TType.STRUCT:
                    self.queueLimitAction = ActionQueueLimitIDL()
                    self.queueLimitAction.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 26:
                if ftype == TType.STRUCT:
                    self.protocolAction = ActionProtocolIDL()
                    self.protocolAction.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 27:
                if ftype == TType.STRUCT:
                    self.ttlAction = ActionTtlIDL()
                    self.ttlAction.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 28:
                if ftype == TType.STRUCT:
                    self.mplsAction = ActionMplsIDL()
                    self.mplsAction.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 29:
                if ftype == TType.STRUCT:
                    self.outputAction = ActionOutputIDL()
                    self.outputAction.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 30:
                if ftype == TType.STRUCT:
                    self.gotoTableAction = ActionGotoTableIDL()
                    self.gotoTableAction.read(iprot)
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
        oprot.writeStructBegin('ActionIDL')
        if self.dsid != None:
            oprot.writeFieldBegin('dsid', TType.I32, 1)
            oprot.writeI32(self.dsid)
            oprot.writeFieldEnd()
        if self.actionHandle != None:
            oprot.writeFieldBegin('actionHandle', TType.I64, 2)
            oprot.writeI64(self.actionHandle)
            oprot.writeFieldEnd()
        if self.opCode != None:
            oprot.writeFieldBegin('opCode', TType.I16, 3)
            oprot.writeI16(self.opCode)
            oprot.writeFieldEnd()
        if self.opId != None:
            oprot.writeFieldBegin('opId', TType.I32, 4)
            oprot.writeI32(self.opId)
            oprot.writeFieldEnd()
        if self.actionType != None:
            oprot.writeFieldBegin('actionType', TType.I32, 5)
            oprot.writeI32(self.actionType)
            oprot.writeFieldEnd()
        if self.outIfAction != None:
            oprot.writeFieldBegin('outIfAction', TType.STRUCT, 6)
            self.outIfAction.write(oprot)
            oprot.writeFieldEnd()
        if self.markAction != None:
            oprot.writeFieldBegin('markAction', TType.STRUCT, 7)
            self.markAction.write(oprot)
            oprot.writeFieldEnd()
        if self.macAction != None:
            oprot.writeFieldBegin('macAction', TType.STRUCT, 8)
            self.macAction.write(oprot)
            oprot.writeFieldEnd()
        if self.nhAction != None:
            oprot.writeFieldBegin('nhAction', TType.STRUCT, 9)
            self.nhAction.write(oprot)
            oprot.writeFieldEnd()
        if self.policeAction != None:
            oprot.writeFieldBegin('policeAction', TType.STRUCT, 10)
            self.policeAction.write(oprot)
            oprot.writeFieldEnd()
        if self.shapeAction != None:
            oprot.writeFieldBegin('shapeAction', TType.STRUCT, 11)
            self.shapeAction.write(oprot)
            oprot.writeFieldEnd()
        if self.pqAction != None:
            oprot.writeFieldBegin('pqAction', TType.STRUCT, 12)
            self.pqAction.write(oprot)
            oprot.writeFieldEnd()
        if self.cqAction != None:
            oprot.writeFieldBegin('cqAction', TType.STRUCT, 13)
            self.cqAction.write(oprot)
            oprot.writeFieldEnd()
        if self.fqAction != None:
            oprot.writeFieldBegin('fqAction', TType.STRUCT, 14)
            self.fqAction.write(oprot)
            oprot.writeFieldEnd()
        if self.wredProfile != None:
            oprot.writeFieldBegin('wredProfile', TType.STRUCT, 15)
            self.wredProfile.write(oprot)
            oprot.writeFieldEnd()
        if self.pktCopyAction != None:
            oprot.writeFieldBegin('pktCopyAction', TType.STRUCT, 16)
            self.pktCopyAction.write(oprot)
            oprot.writeFieldEnd()
        if self.pktDivertAction != None:
            oprot.writeFieldBegin('pktDivertAction', TType.STRUCT, 17)
            self.pktDivertAction.write(oprot)
            oprot.writeFieldEnd()
        if self.vlanAction != None:
            oprot.writeFieldBegin('vlanAction', TType.STRUCT, 18)
            self.vlanAction.write(oprot)
            oprot.writeFieldEnd()
        if self.parameterMapName != None:
            oprot.writeFieldBegin('parameterMapName', TType.STRING, 19)
            oprot.writeString(self.parameterMapName)
            oprot.writeFieldEnd()
        if self.wredParam != None:
            oprot.writeFieldBegin('wredParam', TType.STRUCT, 20)
            self.wredParam.write(oprot)
            oprot.writeFieldEnd()
        if self.fwdClassIdAction != None:
            oprot.writeFieldBegin('fwdClassIdAction', TType.STRUCT, 21)
            self.fwdClassIdAction.write(oprot)
            oprot.writeFieldEnd()
        if self.ipAddressAction != None:
            oprot.writeFieldBegin('ipAddressAction', TType.STRUCT, 22)
            self.ipAddressAction.write(oprot)
            oprot.writeFieldEnd()
        if self.mplsExpAction != None:
            oprot.writeFieldBegin('mplsExpAction', TType.STRUCT, 23)
            self.mplsExpAction.write(oprot)
            oprot.writeFieldEnd()
        if self.tcpPortAction != None:
            oprot.writeFieldBegin('tcpPortAction', TType.STRUCT, 24)
            self.tcpPortAction.write(oprot)
            oprot.writeFieldEnd()
        if self.queueLimitAction != None:
            oprot.writeFieldBegin('queueLimitAction', TType.STRUCT, 25)
            self.queueLimitAction.write(oprot)
            oprot.writeFieldEnd()
        if self.protocolAction != None:
            oprot.writeFieldBegin('protocolAction', TType.STRUCT, 26)
            self.protocolAction.write(oprot)
            oprot.writeFieldEnd()
        if self.ttlAction != None:
            oprot.writeFieldBegin('ttlAction', TType.STRUCT, 27)
            self.ttlAction.write(oprot)
            oprot.writeFieldEnd()
        if self.mplsAction != None:
            oprot.writeFieldBegin('mplsAction', TType.STRUCT, 28)
            self.mplsAction.write(oprot)
            oprot.writeFieldEnd()
        if self.outputAction != None:
            oprot.writeFieldBegin('outputAction', TType.STRUCT, 29)
            self.outputAction.write(oprot)
            oprot.writeFieldEnd()
        if self.gotoTableAction != None:
            oprot.writeFieldBegin('gotoTableAction', TType.STRUCT, 30)
            self.gotoTableAction.write(oprot)
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




class MatchGroupIDL(object):
    """
      Match Group
    
      Attributes:
       - opcode
       - opId
       - type
       - addrFamily
       - name
       - matchList
      """

    thrift_spec = (None,
     (1,
      TType.I16,
      'opcode',
      None,
      None),
     (2,
      TType.I32,
      'opId',
      None,
      None),
     (3,
      TType.I32,
      'type',
      None,
      None),
     (4,
      TType.I32,
      'addrFamily',
      None,
      None),
     (5,
      TType.STRING,
      'name',
      None,
      None),
     (6,
      TType.LIST,
      'matchList',
      (TType.STRUCT, (MatchIDL, MatchIDL.thrift_spec)),
      None))

    def __init__(self, opcode = None, opId = None, type = None, addrFamily = None, name = None, matchList = None):
        self.opcode = opcode
        self.opId = opId
        self.type = type
        self.addrFamily = addrFamily
        self.name = name
        self.matchList = matchList



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
                    self.opcode = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.opId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.addrFamily = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.name = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.LIST:
                    self.matchList = []
                    (_etype122, _size119,) = iprot.readListBegin()
                    for _i123 in xrange(_size119):
                        _elem124 = MatchIDL()
                        _elem124.read(iprot)
                        self.matchList.append(_elem124)

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
        oprot.writeStructBegin('MatchGroupIDL')
        if self.opcode != None:
            oprot.writeFieldBegin('opcode', TType.I16, 1)
            oprot.writeI16(self.opcode)
            oprot.writeFieldEnd()
        if self.opId != None:
            oprot.writeFieldBegin('opId', TType.I32, 2)
            oprot.writeI32(self.opId)
            oprot.writeFieldEnd()
        if self.type != None:
            oprot.writeFieldBegin('type', TType.I32, 3)
            oprot.writeI32(self.type)
            oprot.writeFieldEnd()
        if self.addrFamily != None:
            oprot.writeFieldBegin('addrFamily', TType.I32, 4)
            oprot.writeI32(self.addrFamily)
            oprot.writeFieldEnd()
        if self.name != None:
            oprot.writeFieldBegin('name', TType.STRING, 5)
            oprot.writeString(self.name)
            oprot.writeFieldEnd()
        if self.matchList != None:
            oprot.writeFieldBegin('matchList', TType.LIST, 6)
            oprot.writeListBegin(TType.STRUCT, len(self.matchList))
            for iter125 in self.matchList:
                iter125.write(oprot)

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




class PolicyFilterIDL(object):
    """
      Filter
    
      Attributes:
       - dsid
       - opCode
       - opId
       - pollIntervalSec
       - pollIntervalMsec
       - tableType
       - ifHandle
       - maxEntryCount
       - persistent
       - lastEntryHandle
       - statsCategory
       - target_direction
      """

    thrift_spec = (None,
     (1,
      TType.I32,
      'dsid',
      None,
      None),
     (2,
      TType.I16,
      'opCode',
      None,
      None),
     (3,
      TType.I32,
      'opId',
      None,
      None),
     (4,
      TType.I32,
      'pollIntervalSec',
      None,
      None),
     (5,
      TType.I32,
      'pollIntervalMsec',
      None,
      None),
     (6,
      TType.I32,
      'tableType',
      None,
      None),
     (7,
      TType.LIST,
      'ifHandle',
      (TType.I64, None),
      None),
     (8,
      TType.I32,
      'maxEntryCount',
      None,
      None),
     (9,
      TType.I32,
      'persistent',
      None,
      None),
     (10,
      TType.I64,
      'lastEntryHandle',
      None,
      None),
     (11,
      TType.I32,
      'statsCategory',
      None,
      None),
     (12,
      TType.I16,
      'target_direction',
      None,
      None))

    def __init__(self, dsid = None, opCode = None, opId = None, pollIntervalSec = None, pollIntervalMsec = None, tableType = None, ifHandle = None, maxEntryCount = None, persistent = None, lastEntryHandle = None, statsCategory = None, target_direction = None):
        self.dsid = dsid
        self.opCode = opCode
        self.opId = opId
        self.pollIntervalSec = pollIntervalSec
        self.pollIntervalMsec = pollIntervalMsec
        self.tableType = tableType
        self.ifHandle = ifHandle
        self.maxEntryCount = maxEntryCount
        self.persistent = persistent
        self.lastEntryHandle = lastEntryHandle
        self.statsCategory = statsCategory
        self.target_direction = target_direction



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
                    self.dsid = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I16:
                    self.opCode = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.opId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.pollIntervalSec = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.pollIntervalMsec = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I32:
                    self.tableType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.LIST:
                    self.ifHandle = []
                    (_etype129, _size126,) = iprot.readListBegin()
                    for _i130 in xrange(_size126):
                        _elem131 = iprot.readI64()
                        self.ifHandle.append(_elem131)

                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.I32:
                    self.maxEntryCount = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.I32:
                    self.persistent = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.I64:
                    self.lastEntryHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.I32:
                    self.statsCategory = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 12:
                if ftype == TType.I16:
                    self.target_direction = iprot.readI16()
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
        oprot.writeStructBegin('PolicyFilterIDL')
        if self.dsid != None:
            oprot.writeFieldBegin('dsid', TType.I32, 1)
            oprot.writeI32(self.dsid)
            oprot.writeFieldEnd()
        if self.opCode != None:
            oprot.writeFieldBegin('opCode', TType.I16, 2)
            oprot.writeI16(self.opCode)
            oprot.writeFieldEnd()
        if self.opId != None:
            oprot.writeFieldBegin('opId', TType.I32, 3)
            oprot.writeI32(self.opId)
            oprot.writeFieldEnd()
        if self.pollIntervalSec != None:
            oprot.writeFieldBegin('pollIntervalSec', TType.I32, 4)
            oprot.writeI32(self.pollIntervalSec)
            oprot.writeFieldEnd()
        if self.pollIntervalMsec != None:
            oprot.writeFieldBegin('pollIntervalMsec', TType.I32, 5)
            oprot.writeI32(self.pollIntervalMsec)
            oprot.writeFieldEnd()
        if self.tableType != None:
            oprot.writeFieldBegin('tableType', TType.I32, 6)
            oprot.writeI32(self.tableType)
            oprot.writeFieldEnd()
        if self.ifHandle != None:
            oprot.writeFieldBegin('ifHandle', TType.LIST, 7)
            oprot.writeListBegin(TType.I64, len(self.ifHandle))
            for iter132 in self.ifHandle:
                oprot.writeI64(iter132)

            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.maxEntryCount != None:
            oprot.writeFieldBegin('maxEntryCount', TType.I32, 8)
            oprot.writeI32(self.maxEntryCount)
            oprot.writeFieldEnd()
        if self.persistent != None:
            oprot.writeFieldBegin('persistent', TType.I32, 9)
            oprot.writeI32(self.persistent)
            oprot.writeFieldEnd()
        if self.lastEntryHandle != None:
            oprot.writeFieldBegin('lastEntryHandle', TType.I64, 10)
            oprot.writeI64(self.lastEntryHandle)
            oprot.writeFieldEnd()
        if self.statsCategory != None:
            oprot.writeFieldBegin('statsCategory', TType.I32, 11)
            oprot.writeI32(self.statsCategory)
            oprot.writeFieldEnd()
        if self.target_direction != None:
            oprot.writeFieldBegin('target_direction', TType.I16, 12)
            oprot.writeI16(self.target_direction)
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




class CmapIDL(object):
    """
      CMAP
    
      Attributes:
       - dsid
       - cmapHandle
       - opcode
       - opId
       - cmapOper
       - matchList
       - matchGroupList
       - filter
       - name
      """

    thrift_spec = (None,
     (1,
      TType.I32,
      'dsid',
      None,
      None),
     (2,
      TType.I64,
      'cmapHandle',
      None,
      None),
     (3,
      TType.I16,
      'opcode',
      None,
      None),
     (4,
      TType.I32,
      'opId',
      None,
      None),
     (5,
      TType.I32,
      'cmapOper',
      None,
      None),
     (6,
      TType.LIST,
      'matchList',
      (TType.STRUCT, (MatchIDL, MatchIDL.thrift_spec)),
      None),
     (7,
      TType.LIST,
      'matchGroupList',
      (TType.STRUCT, (MatchGroupIDL, MatchGroupIDL.thrift_spec)),
      None),
     (8,
      TType.STRUCT,
      'filter',
      (PolicyFilterIDL, PolicyFilterIDL.thrift_spec),
      None),
     (9,
      TType.STRING,
      'name',
      None,
      None))

    def __init__(self, dsid = None, cmapHandle = None, opcode = None, opId = None, cmapOper = None, matchList = None, matchGroupList = None, filter = None, name = None):
        self.dsid = dsid
        self.cmapHandle = cmapHandle
        self.opcode = opcode
        self.opId = opId
        self.cmapOper = cmapOper
        self.matchList = matchList
        self.matchGroupList = matchGroupList
        self.filter = filter
        self.name = name



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
                    self.dsid = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.cmapHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I16:
                    self.opcode = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.opId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.cmapOper = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.LIST:
                    self.matchList = []
                    (_etype136, _size133,) = iprot.readListBegin()
                    for _i137 in xrange(_size133):
                        _elem138 = MatchIDL()
                        _elem138.read(iprot)
                        self.matchList.append(_elem138)

                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.LIST:
                    self.matchGroupList = []
                    (_etype142, _size139,) = iprot.readListBegin()
                    for _i143 in xrange(_size139):
                        _elem144 = MatchGroupIDL()
                        _elem144.read(iprot)
                        self.matchGroupList.append(_elem144)

                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.STRUCT:
                    self.filter = PolicyFilterIDL()
                    self.filter.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.STRING:
                    self.name = iprot.readString()
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
        oprot.writeStructBegin('CmapIDL')
        if self.dsid != None:
            oprot.writeFieldBegin('dsid', TType.I32, 1)
            oprot.writeI32(self.dsid)
            oprot.writeFieldEnd()
        if self.cmapHandle != None:
            oprot.writeFieldBegin('cmapHandle', TType.I64, 2)
            oprot.writeI64(self.cmapHandle)
            oprot.writeFieldEnd()
        if self.opcode != None:
            oprot.writeFieldBegin('opcode', TType.I16, 3)
            oprot.writeI16(self.opcode)
            oprot.writeFieldEnd()
        if self.opId != None:
            oprot.writeFieldBegin('opId', TType.I32, 4)
            oprot.writeI32(self.opId)
            oprot.writeFieldEnd()
        if self.cmapOper != None:
            oprot.writeFieldBegin('cmapOper', TType.I32, 5)
            oprot.writeI32(self.cmapOper)
            oprot.writeFieldEnd()
        if self.matchList != None:
            oprot.writeFieldBegin('matchList', TType.LIST, 6)
            oprot.writeListBegin(TType.STRUCT, len(self.matchList))
            for iter145 in self.matchList:
                iter145.write(oprot)

            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.matchGroupList != None:
            oprot.writeFieldBegin('matchGroupList', TType.LIST, 7)
            oprot.writeListBegin(TType.STRUCT, len(self.matchGroupList))
            for iter146 in self.matchGroupList:
                iter146.write(oprot)

            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.filter != None:
            oprot.writeFieldBegin('filter', TType.STRUCT, 8)
            self.filter.write(oprot)
            oprot.writeFieldEnd()
        if self.name != None:
            oprot.writeFieldBegin('name', TType.STRING, 9)
            oprot.writeString(self.name)
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




class CmapGetResultIDL(object):
    """
      CMAP Get Result
    
      Attributes:
       - dsid
       - cmap_list
      """

    thrift_spec = (None, (1,
      TType.I32,
      'dsid',
      None,
      None), (2,
      TType.LIST,
      'cmap_list',
      (TType.STRUCT, (CmapIDL, CmapIDL.thrift_spec)),
      None))

    def __init__(self, dsid = None, cmap_list = None):
        self.dsid = dsid
        self.cmap_list = cmap_list



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
                    self.dsid = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.cmap_list = []
                    (_etype150, _size147,) = iprot.readListBegin()
                    for _i151 in xrange(_size147):
                        _elem152 = CmapIDL()
                        _elem152.read(iprot)
                        self.cmap_list.append(_elem152)

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
        oprot.writeStructBegin('CmapGetResultIDL')
        if self.dsid != None:
            oprot.writeFieldBegin('dsid', TType.I32, 1)
            oprot.writeI32(self.dsid)
            oprot.writeFieldEnd()
        if self.cmap_list != None:
            oprot.writeFieldBegin('cmap_list', TType.LIST, 2)
            oprot.writeListBegin(TType.STRUCT, len(self.cmap_list))
            for iter153 in self.cmap_list:
                iter153.write(oprot)

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




class CmapResultIDL(object):
    """
      CMAP Result
    
      Attributes:
       - dsid
       - cmapHandle
       - opId
       - opCode
       - resultCode
       - matchResultList
       - getResult
      """

    thrift_spec = (None,
     (1,
      TType.I32,
      'dsid',
      None,
      None),
     (2,
      TType.I64,
      'cmapHandle',
      None,
      None),
     (3,
      TType.I32,
      'opId',
      None,
      None),
     (4,
      TType.I16,
      'opCode',
      None,
      None),
     (5,
      TType.I16,
      'resultCode',
      None,
      None),
     (6,
      TType.LIST,
      'matchResultList',
      (TType.STRUCT, (PolicyCommonTypes.ttypes.ResultIDL, PolicyCommonTypes.ttypes.ResultIDL.thrift_spec)),
      None),
     (7,
      TType.STRUCT,
      'getResult',
      (CmapGetResultIDL, CmapGetResultIDL.thrift_spec),
      None))

    def __init__(self, dsid = None, cmapHandle = None, opId = None, opCode = None, resultCode = None, matchResultList = None, getResult = None):
        self.dsid = dsid
        self.cmapHandle = cmapHandle
        self.opId = opId
        self.opCode = opCode
        self.resultCode = resultCode
        self.matchResultList = matchResultList
        self.getResult = getResult



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
                    self.dsid = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.cmapHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.opId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I16:
                    self.opCode = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I16:
                    self.resultCode = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.LIST:
                    self.matchResultList = []
                    (_etype157, _size154,) = iprot.readListBegin()
                    for _i158 in xrange(_size154):
                        _elem159 = PolicyCommonTypes.ttypes.ResultIDL()
                        _elem159.read(iprot)
                        self.matchResultList.append(_elem159)

                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.STRUCT:
                    self.getResult = CmapGetResultIDL()
                    self.getResult.read(iprot)
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
        oprot.writeStructBegin('CmapResultIDL')
        if self.dsid != None:
            oprot.writeFieldBegin('dsid', TType.I32, 1)
            oprot.writeI32(self.dsid)
            oprot.writeFieldEnd()
        if self.cmapHandle != None:
            oprot.writeFieldBegin('cmapHandle', TType.I64, 2)
            oprot.writeI64(self.cmapHandle)
            oprot.writeFieldEnd()
        if self.opId != None:
            oprot.writeFieldBegin('opId', TType.I32, 3)
            oprot.writeI32(self.opId)
            oprot.writeFieldEnd()
        if self.opCode != None:
            oprot.writeFieldBegin('opCode', TType.I16, 4)
            oprot.writeI16(self.opCode)
            oprot.writeFieldEnd()
        if self.resultCode != None:
            oprot.writeFieldBegin('resultCode', TType.I16, 5)
            oprot.writeI16(self.resultCode)
            oprot.writeFieldEnd()
        if self.matchResultList != None:
            oprot.writeFieldBegin('matchResultList', TType.LIST, 6)
            oprot.writeListBegin(TType.STRUCT, len(self.matchResultList))
            for iter160 in self.matchResultList:
                iter160.write(oprot)

            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.getResult != None:
            oprot.writeFieldBegin('getResult', TType.STRUCT, 7)
            self.getResult.write(oprot)
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




class EntryIDL(object):
    """
      Entry
    
      Attributes:
       - dsid
       - entryHandle
       - opCode
       - order
       - opId
       - entryOper
       - priority
       - sequence
       - cmapHandle
       - policy_op_index
       - matchList
       - actionList
      """

    thrift_spec = (None,
     (1,
      TType.I32,
      'dsid',
      None,
      None),
     (2,
      TType.I64,
      'entryHandle',
      None,
      None),
     (3,
      TType.I16,
      'opCode',
      None,
      None),
     (4,
      TType.I16,
      'order',
      None,
      None),
     (5,
      TType.I32,
      'opId',
      None,
      None),
     (6,
      TType.I32,
      'entryOper',
      None,
      None),
     (7,
      TType.I64,
      'priority',
      None,
      None),
     (8,
      TType.I32,
      'sequence',
      None,
      None),
     (9,
      TType.I64,
      'cmapHandle',
      None,
      None),
     (10,
      TType.I32,
      'policy_op_index',
      None,
      None),
     (11,
      TType.LIST,
      'matchList',
      (TType.STRUCT, (MatchIDL, MatchIDL.thrift_spec)),
      None),
     (12,
      TType.LIST,
      'actionList',
      (TType.STRUCT, (ActionIDL, ActionIDL.thrift_spec)),
      None))

    def __init__(self, dsid = None, entryHandle = None, opCode = None, order = None, opId = None, entryOper = None, priority = None, sequence = None, cmapHandle = None, policy_op_index = None, matchList = None, actionList = None):
        self.dsid = dsid
        self.entryHandle = entryHandle
        self.opCode = opCode
        self.order = order
        self.opId = opId
        self.entryOper = entryOper
        self.priority = priority
        self.sequence = sequence
        self.cmapHandle = cmapHandle
        self.policy_op_index = policy_op_index
        self.matchList = matchList
        self.actionList = actionList



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
                    self.dsid = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.entryHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I16:
                    self.opCode = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I16:
                    self.order = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.opId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I32:
                    self.entryOper = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I64:
                    self.priority = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.I32:
                    self.sequence = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.I64:
                    self.cmapHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.I32:
                    self.policy_op_index = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.LIST:
                    self.matchList = []
                    (_etype164, _size161,) = iprot.readListBegin()
                    for _i165 in xrange(_size161):
                        _elem166 = MatchIDL()
                        _elem166.read(iprot)
                        self.matchList.append(_elem166)

                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 12:
                if ftype == TType.LIST:
                    self.actionList = []
                    (_etype170, _size167,) = iprot.readListBegin()
                    for _i171 in xrange(_size167):
                        _elem172 = ActionIDL()
                        _elem172.read(iprot)
                        self.actionList.append(_elem172)

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
        oprot.writeStructBegin('EntryIDL')
        if self.dsid != None:
            oprot.writeFieldBegin('dsid', TType.I32, 1)
            oprot.writeI32(self.dsid)
            oprot.writeFieldEnd()
        if self.entryHandle != None:
            oprot.writeFieldBegin('entryHandle', TType.I64, 2)
            oprot.writeI64(self.entryHandle)
            oprot.writeFieldEnd()
        if self.opCode != None:
            oprot.writeFieldBegin('opCode', TType.I16, 3)
            oprot.writeI16(self.opCode)
            oprot.writeFieldEnd()
        if self.order != None:
            oprot.writeFieldBegin('order', TType.I16, 4)
            oprot.writeI16(self.order)
            oprot.writeFieldEnd()
        if self.opId != None:
            oprot.writeFieldBegin('opId', TType.I32, 5)
            oprot.writeI32(self.opId)
            oprot.writeFieldEnd()
        if self.entryOper != None:
            oprot.writeFieldBegin('entryOper', TType.I32, 6)
            oprot.writeI32(self.entryOper)
            oprot.writeFieldEnd()
        if self.priority != None:
            oprot.writeFieldBegin('priority', TType.I64, 7)
            oprot.writeI64(self.priority)
            oprot.writeFieldEnd()
        if self.sequence != None:
            oprot.writeFieldBegin('sequence', TType.I32, 8)
            oprot.writeI32(self.sequence)
            oprot.writeFieldEnd()
        if self.cmapHandle != None:
            oprot.writeFieldBegin('cmapHandle', TType.I64, 9)
            oprot.writeI64(self.cmapHandle)
            oprot.writeFieldEnd()
        if self.policy_op_index != None:
            oprot.writeFieldBegin('policy_op_index', TType.I32, 10)
            oprot.writeI32(self.policy_op_index)
            oprot.writeFieldEnd()
        if self.matchList != None:
            oprot.writeFieldBegin('matchList', TType.LIST, 11)
            oprot.writeListBegin(TType.STRUCT, len(self.matchList))
            for iter173 in self.matchList:
                iter173.write(oprot)

            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.actionList != None:
            oprot.writeFieldBegin('actionList', TType.LIST, 12)
            oprot.writeListBegin(TType.STRUCT, len(self.actionList))
            for iter174 in self.actionList:
                iter174.write(oprot)

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




class EntryResultIDL(object):
    """
      Entry Result
    
      Attributes:
       - dsid
       - entryHandle
       - opId
       - opCode
       - policy_op_index
       - resultCode
       - cmapResult
       - matchResultList
       - actionResultList
      """

    thrift_spec = (None,
     (1,
      TType.I32,
      'dsid',
      None,
      None),
     (2,
      TType.I64,
      'entryHandle',
      None,
      None),
     (3,
      TType.I32,
      'opId',
      None,
      None),
     (4,
      TType.I16,
      'opCode',
      None,
      None),
     (5,
      TType.I32,
      'policy_op_index',
      None,
      None),
     (6,
      TType.I16,
      'resultCode',
      None,
      None),
     (7,
      TType.STRUCT,
      'cmapResult',
      (CmapResultIDL, CmapResultIDL.thrift_spec),
      None),
     (8,
      TType.LIST,
      'matchResultList',
      (TType.STRUCT, (PolicyCommonTypes.ttypes.ResultIDL, PolicyCommonTypes.ttypes.ResultIDL.thrift_spec)),
      None),
     (9,
      TType.LIST,
      'actionResultList',
      (TType.STRUCT, (PolicyCommonTypes.ttypes.ResultIDL, PolicyCommonTypes.ttypes.ResultIDL.thrift_spec)),
      None))

    def __init__(self, dsid = None, entryHandle = None, opId = None, opCode = None, policy_op_index = None, resultCode = None, cmapResult = None, matchResultList = None, actionResultList = None):
        self.dsid = dsid
        self.entryHandle = entryHandle
        self.opId = opId
        self.opCode = opCode
        self.policy_op_index = policy_op_index
        self.resultCode = resultCode
        self.cmapResult = cmapResult
        self.matchResultList = matchResultList
        self.actionResultList = actionResultList



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
                    self.dsid = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.entryHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.opId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I16:
                    self.opCode = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.policy_op_index = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I16:
                    self.resultCode = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.STRUCT:
                    self.cmapResult = CmapResultIDL()
                    self.cmapResult.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.LIST:
                    self.matchResultList = []
                    (_etype178, _size175,) = iprot.readListBegin()
                    for _i179 in xrange(_size175):
                        _elem180 = PolicyCommonTypes.ttypes.ResultIDL()
                        _elem180.read(iprot)
                        self.matchResultList.append(_elem180)

                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.LIST:
                    self.actionResultList = []
                    (_etype184, _size181,) = iprot.readListBegin()
                    for _i185 in xrange(_size181):
                        _elem186 = PolicyCommonTypes.ttypes.ResultIDL()
                        _elem186.read(iprot)
                        self.actionResultList.append(_elem186)

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
        oprot.writeStructBegin('EntryResultIDL')
        if self.dsid != None:
            oprot.writeFieldBegin('dsid', TType.I32, 1)
            oprot.writeI32(self.dsid)
            oprot.writeFieldEnd()
        if self.entryHandle != None:
            oprot.writeFieldBegin('entryHandle', TType.I64, 2)
            oprot.writeI64(self.entryHandle)
            oprot.writeFieldEnd()
        if self.opId != None:
            oprot.writeFieldBegin('opId', TType.I32, 3)
            oprot.writeI32(self.opId)
            oprot.writeFieldEnd()
        if self.opCode != None:
            oprot.writeFieldBegin('opCode', TType.I16, 4)
            oprot.writeI16(self.opCode)
            oprot.writeFieldEnd()
        if self.policy_op_index != None:
            oprot.writeFieldBegin('policy_op_index', TType.I32, 5)
            oprot.writeI32(self.policy_op_index)
            oprot.writeFieldEnd()
        if self.resultCode != None:
            oprot.writeFieldBegin('resultCode', TType.I16, 6)
            oprot.writeI16(self.resultCode)
            oprot.writeFieldEnd()
        if self.cmapResult != None:
            oprot.writeFieldBegin('cmapResult', TType.STRUCT, 7)
            self.cmapResult.write(oprot)
            oprot.writeFieldEnd()
        if self.matchResultList != None:
            oprot.writeFieldBegin('matchResultList', TType.LIST, 8)
            oprot.writeListBegin(TType.STRUCT, len(self.matchResultList))
            for iter187 in self.matchResultList:
                iter187.write(oprot)

            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.actionResultList != None:
            oprot.writeFieldBegin('actionResultList', TType.LIST, 9)
            oprot.writeListBegin(TType.STRUCT, len(self.actionResultList))
            for iter188 in self.actionResultList:
                iter188.write(oprot)

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




class PmapIDL(object):
    """
      PMAP
    
      Attributes:
       - dsid
       - pmapHandle
       - opCode
       - opId
       - entryList
       - filter
       - pmap_name
       - table_handle
      """

    thrift_spec = (None,
     (1,
      TType.I32,
      'dsid',
      None,
      None),
     (2,
      TType.I64,
      'pmapHandle',
      None,
      None),
     (3,
      TType.I16,
      'opCode',
      None,
      None),
     (4,
      TType.I32,
      'opId',
      None,
      None),
     (5,
      TType.LIST,
      'entryList',
      (TType.STRUCT, (EntryIDL, EntryIDL.thrift_spec)),
      None),
     (6,
      TType.STRUCT,
      'filter',
      (PolicyFilterIDL, PolicyFilterIDL.thrift_spec),
      None),
     (7,
      TType.STRING,
      'pmap_name',
      None,
      None),
     (8,
      TType.I64,
      'table_handle',
      None,
      None))

    def __init__(self, dsid = None, pmapHandle = None, opCode = None, opId = None, entryList = None, filter = None, pmap_name = None, table_handle = None):
        self.dsid = dsid
        self.pmapHandle = pmapHandle
        self.opCode = opCode
        self.opId = opId
        self.entryList = entryList
        self.filter = filter
        self.pmap_name = pmap_name
        self.table_handle = table_handle



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
                    self.dsid = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.pmapHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I16:
                    self.opCode = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.opId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.LIST:
                    self.entryList = []
                    (_etype192, _size189,) = iprot.readListBegin()
                    for _i193 in xrange(_size189):
                        _elem194 = EntryIDL()
                        _elem194.read(iprot)
                        self.entryList.append(_elem194)

                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRUCT:
                    self.filter = PolicyFilterIDL()
                    self.filter.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.STRING:
                    self.pmap_name = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.I64:
                    self.table_handle = iprot.readI64()
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
        oprot.writeStructBegin('PmapIDL')
        if self.dsid != None:
            oprot.writeFieldBegin('dsid', TType.I32, 1)
            oprot.writeI32(self.dsid)
            oprot.writeFieldEnd()
        if self.pmapHandle != None:
            oprot.writeFieldBegin('pmapHandle', TType.I64, 2)
            oprot.writeI64(self.pmapHandle)
            oprot.writeFieldEnd()
        if self.opCode != None:
            oprot.writeFieldBegin('opCode', TType.I16, 3)
            oprot.writeI16(self.opCode)
            oprot.writeFieldEnd()
        if self.opId != None:
            oprot.writeFieldBegin('opId', TType.I32, 4)
            oprot.writeI32(self.opId)
            oprot.writeFieldEnd()
        if self.entryList != None:
            oprot.writeFieldBegin('entryList', TType.LIST, 5)
            oprot.writeListBegin(TType.STRUCT, len(self.entryList))
            for iter195 in self.entryList:
                iter195.write(oprot)

            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.filter != None:
            oprot.writeFieldBegin('filter', TType.STRUCT, 6)
            self.filter.write(oprot)
            oprot.writeFieldEnd()
        if self.pmap_name != None:
            oprot.writeFieldBegin('pmap_name', TType.STRING, 7)
            oprot.writeString(self.pmap_name)
            oprot.writeFieldEnd()
        if self.table_handle != None:
            oprot.writeFieldBegin('table_handle', TType.I64, 8)
            oprot.writeI64(self.table_handle)
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




class PmapGetResultIDL(object):
    """
      Get PMAP Result
    
      Attributes:
       - dsid
       - entry_count
       - more
       - pmap_list
      """

    thrift_spec = (None,
     (1,
      TType.I32,
      'dsid',
      None,
      None),
     (2,
      TType.I32,
      'entry_count',
      None,
      None),
     (3,
      TType.I16,
      'more',
      None,
      None),
     (4,
      TType.LIST,
      'pmap_list',
      (TType.STRUCT, (PmapIDL, PmapIDL.thrift_spec)),
      None))

    def __init__(self, dsid = None, entry_count = None, more = None, pmap_list = None):
        self.dsid = dsid
        self.entry_count = entry_count
        self.more = more
        self.pmap_list = pmap_list



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
                    self.dsid = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.entry_count = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I16:
                    self.more = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.LIST:
                    self.pmap_list = []
                    (_etype199, _size196,) = iprot.readListBegin()
                    for _i200 in xrange(_size196):
                        _elem201 = PmapIDL()
                        _elem201.read(iprot)
                        self.pmap_list.append(_elem201)

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
        oprot.writeStructBegin('PmapGetResultIDL')
        if self.dsid != None:
            oprot.writeFieldBegin('dsid', TType.I32, 1)
            oprot.writeI32(self.dsid)
            oprot.writeFieldEnd()
        if self.entry_count != None:
            oprot.writeFieldBegin('entry_count', TType.I32, 2)
            oprot.writeI32(self.entry_count)
            oprot.writeFieldEnd()
        if self.more != None:
            oprot.writeFieldBegin('more', TType.I16, 3)
            oprot.writeI16(self.more)
            oprot.writeFieldEnd()
        if self.pmap_list != None:
            oprot.writeFieldBegin('pmap_list', TType.LIST, 4)
            oprot.writeListBegin(TType.STRUCT, len(self.pmap_list))
            for iter202 in self.pmap_list:
                iter202.write(oprot)

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




class PmapResultIDL(object):
    """
      PMAP Result
    
      Attributes:
       - dsid
       - pmapHandle
       - opId
       - opCode
       - resultCode
       - entryResult
       - statsResult
       - statsResultEventHandle
       - getResult
      """

    thrift_spec = (None,
     (1,
      TType.I32,
      'dsid',
      None,
      None),
     (2,
      TType.I64,
      'pmapHandle',
      None,
      None),
     (3,
      TType.I32,
      'opId',
      None,
      None),
     (4,
      TType.I16,
      'opCode',
      None,
      None),
     (5,
      TType.I16,
      'resultCode',
      None,
      None),
     (6,
      TType.LIST,
      'entryResult',
      (TType.STRUCT, (EntryResultIDL, EntryResultIDL.thrift_spec)),
      None),
     (7,
      TType.STRUCT,
      'statsResult',
      (PolicyCommonTypes.ttypes.PolicyStatsResultIDL, PolicyCommonTypes.ttypes.PolicyStatsResultIDL.thrift_spec),
      None),
     (8,
      TType.I32,
      'statsResultEventHandle',
      None,
      None),
     (9,
      TType.STRUCT,
      'getResult',
      (PmapGetResultIDL, PmapGetResultIDL.thrift_spec),
      None))

    def __init__(self, dsid = None, pmapHandle = None, opId = None, opCode = None, resultCode = None, entryResult = None, statsResult = None, statsResultEventHandle = None, getResult = None):
        self.dsid = dsid
        self.pmapHandle = pmapHandle
        self.opId = opId
        self.opCode = opCode
        self.resultCode = resultCode
        self.entryResult = entryResult
        self.statsResult = statsResult
        self.statsResultEventHandle = statsResultEventHandle
        self.getResult = getResult



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
                    self.dsid = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.pmapHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.opId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I16:
                    self.opCode = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I16:
                    self.resultCode = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.LIST:
                    self.entryResult = []
                    (_etype206, _size203,) = iprot.readListBegin()
                    for _i207 in xrange(_size203):
                        _elem208 = EntryResultIDL()
                        _elem208.read(iprot)
                        self.entryResult.append(_elem208)

                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.STRUCT:
                    self.statsResult = PolicyCommonTypes.ttypes.PolicyStatsResultIDL()
                    self.statsResult.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.I32:
                    self.statsResultEventHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.STRUCT:
                    self.getResult = PmapGetResultIDL()
                    self.getResult.read(iprot)
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
        oprot.writeStructBegin('PmapResultIDL')
        if self.dsid != None:
            oprot.writeFieldBegin('dsid', TType.I32, 1)
            oprot.writeI32(self.dsid)
            oprot.writeFieldEnd()
        if self.pmapHandle != None:
            oprot.writeFieldBegin('pmapHandle', TType.I64, 2)
            oprot.writeI64(self.pmapHandle)
            oprot.writeFieldEnd()
        if self.opId != None:
            oprot.writeFieldBegin('opId', TType.I32, 3)
            oprot.writeI32(self.opId)
            oprot.writeFieldEnd()
        if self.opCode != None:
            oprot.writeFieldBegin('opCode', TType.I16, 4)
            oprot.writeI16(self.opCode)
            oprot.writeFieldEnd()
        if self.resultCode != None:
            oprot.writeFieldBegin('resultCode', TType.I16, 5)
            oprot.writeI16(self.resultCode)
            oprot.writeFieldEnd()
        if self.entryResult != None:
            oprot.writeFieldBegin('entryResult', TType.LIST, 6)
            oprot.writeListBegin(TType.STRUCT, len(self.entryResult))
            for iter209 in self.entryResult:
                iter209.write(oprot)

            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.statsResult != None:
            oprot.writeFieldBegin('statsResult', TType.STRUCT, 7)
            self.statsResult.write(oprot)
            oprot.writeFieldEnd()
        if self.statsResultEventHandle != None:
            oprot.writeFieldBegin('statsResultEventHandle', TType.I32, 8)
            oprot.writeI32(self.statsResultEventHandle)
            oprot.writeFieldEnd()
        if self.getResult != None:
            oprot.writeFieldBegin('getResult', TType.STRUCT, 9)
            self.getResult.write(oprot)
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




class PmapActivateIDL(object):
    """
      PMAP Activate
    
      Attributes:
       - dsid
       - pmapHandle
       - opCode
       - opId
       - ifHandle
       - location
       - zpName
       - attribute
      """

    thrift_spec = (None,
     (1,
      TType.I32,
      'dsid',
      None,
      None),
     (2,
      TType.I64,
      'pmapHandle',
      None,
      None),
     (3,
      TType.I16,
      'opCode',
      None,
      None),
     (4,
      TType.I32,
      'opId',
      None,
      None),
     (5,
      TType.LIST,
      'ifHandle',
      (TType.I64, None),
      None),
     (6,
      TType.LIST,
      'location',
      (TType.BYTE, None),
      None),
     (7,
      TType.LIST,
      'zpName',
      (TType.STRING, None),
      None),
     (8,
      TType.I16,
      'attribute',
      None,
      None))

    def __init__(self, dsid = None, pmapHandle = None, opCode = None, opId = None, ifHandle = None, location = None, zpName = None, attribute = None):
        self.dsid = dsid
        self.pmapHandle = pmapHandle
        self.opCode = opCode
        self.opId = opId
        self.ifHandle = ifHandle
        self.location = location
        self.zpName = zpName
        self.attribute = attribute



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
                    self.dsid = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.pmapHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I16:
                    self.opCode = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.opId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.LIST:
                    self.ifHandle = []
                    (_etype213, _size210,) = iprot.readListBegin()
                    for _i214 in xrange(_size210):
                        _elem215 = iprot.readI64()
                        self.ifHandle.append(_elem215)

                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.LIST:
                    self.location = []
                    (_etype219, _size216,) = iprot.readListBegin()
                    for _i220 in xrange(_size216):
                        _elem221 = iprot.readByte()
                        self.location.append(_elem221)

                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.LIST:
                    self.zpName = []
                    (_etype225, _size222,) = iprot.readListBegin()
                    for _i226 in xrange(_size222):
                        _elem227 = iprot.readString()
                        self.zpName.append(_elem227)

                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.I16:
                    self.attribute = iprot.readI16()
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
        oprot.writeStructBegin('PmapActivateIDL')
        if self.dsid != None:
            oprot.writeFieldBegin('dsid', TType.I32, 1)
            oprot.writeI32(self.dsid)
            oprot.writeFieldEnd()
        if self.pmapHandle != None:
            oprot.writeFieldBegin('pmapHandle', TType.I64, 2)
            oprot.writeI64(self.pmapHandle)
            oprot.writeFieldEnd()
        if self.opCode != None:
            oprot.writeFieldBegin('opCode', TType.I16, 3)
            oprot.writeI16(self.opCode)
            oprot.writeFieldEnd()
        if self.opId != None:
            oprot.writeFieldBegin('opId', TType.I32, 4)
            oprot.writeI32(self.opId)
            oprot.writeFieldEnd()
        if self.ifHandle != None:
            oprot.writeFieldBegin('ifHandle', TType.LIST, 5)
            oprot.writeListBegin(TType.I64, len(self.ifHandle))
            for iter228 in self.ifHandle:
                oprot.writeI64(iter228)

            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.location != None:
            oprot.writeFieldBegin('location', TType.LIST, 6)
            oprot.writeListBegin(TType.BYTE, len(self.location))
            for iter229 in self.location:
                oprot.writeByte(iter229)

            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.zpName != None:
            oprot.writeFieldBegin('zpName', TType.LIST, 7)
            oprot.writeListBegin(TType.STRING, len(self.zpName))
            for iter230 in self.zpName:
                oprot.writeString(iter230)

            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.attribute != None:
            oprot.writeFieldBegin('attribute', TType.I16, 8)
            oprot.writeI16(self.attribute)
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




class PssTableGotoCapIDL(object):
    """
      Table goto info
    
      Attributes:
       - handle
       - gotoHandles
      """

    thrift_spec = (None, (1,
      TType.I64,
      'handle',
      None,
      None), (2,
      TType.LIST,
      'gotoHandles',
      (TType.I64, None),
      None))

    def __init__(self, handle = None, gotoHandles = None):
        self.handle = handle
        self.gotoHandles = gotoHandles



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
                    self.handle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.gotoHandles = []
                    (_etype234, _size231,) = iprot.readListBegin()
                    for _i235 in xrange(_size231):
                        _elem236 = iprot.readI64()
                        self.gotoHandles.append(_elem236)

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
        oprot.writeStructBegin('PssTableGotoCapIDL')
        if self.handle != None:
            oprot.writeFieldBegin('handle', TType.I64, 1)
            oprot.writeI64(self.handle)
            oprot.writeFieldEnd()
        if self.gotoHandles != None:
            oprot.writeFieldBegin('gotoHandles', TType.LIST, 2)
            oprot.writeListBegin(TType.I64, len(self.gotoHandles))
            for iter237 in self.gotoHandles:
                oprot.writeI64(iter237)

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




class PssPipelineCapIDL(object):
    """
      ---------------------------
      Policy Capability Pipelines
      ----------------------------
    
      Attributes:
       - name
       - desc
       - handle
       - tableChain
       - id
       - tableGraph
      """

    thrift_spec = (None,
     (1,
      TType.STRING,
      'name',
      None,
      None),
     (2,
      TType.STRING,
      'desc',
      None,
      None),
     (3,
      TType.I64,
      'handle',
      None,
      None),
     (4,
      TType.LIST,
      'tableChain',
      (TType.I64, None),
      None),
     (5,
      TType.I16,
      'id',
      None,
      None),
     (6,
      TType.LIST,
      'tableGraph',
      (TType.STRUCT, (PssTableGotoCapIDL, PssTableGotoCapIDL.thrift_spec)),
      None))

    def __init__(self, name = None, desc = None, handle = None, tableChain = None, id = None, tableGraph = None):
        self.name = name
        self.desc = desc
        self.handle = handle
        self.tableChain = tableChain
        self.id = id
        self.tableGraph = tableGraph



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
                if ftype == TType.STRING:
                    self.desc = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I64:
                    self.handle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.LIST:
                    self.tableChain = []
                    (_etype241, _size238,) = iprot.readListBegin()
                    for _i242 in xrange(_size238):
                        _elem243 = iprot.readI64()
                        self.tableChain.append(_elem243)

                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I16:
                    self.id = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.LIST:
                    self.tableGraph = []
                    (_etype247, _size244,) = iprot.readListBegin()
                    for _i248 in xrange(_size244):
                        _elem249 = PssTableGotoCapIDL()
                        _elem249.read(iprot)
                        self.tableGraph.append(_elem249)

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
        oprot.writeStructBegin('PssPipelineCapIDL')
        if self.name != None:
            oprot.writeFieldBegin('name', TType.STRING, 1)
            oprot.writeString(self.name)
            oprot.writeFieldEnd()
        if self.desc != None:
            oprot.writeFieldBegin('desc', TType.STRING, 2)
            oprot.writeString(self.desc)
            oprot.writeFieldEnd()
        if self.handle != None:
            oprot.writeFieldBegin('handle', TType.I64, 3)
            oprot.writeI64(self.handle)
            oprot.writeFieldEnd()
        if self.tableChain != None:
            oprot.writeFieldBegin('tableChain', TType.LIST, 4)
            oprot.writeListBegin(TType.I64, len(self.tableChain))
            for iter250 in self.tableChain:
                oprot.writeI64(iter250)

            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.id != None:
            oprot.writeFieldBegin('id', TType.I16, 5)
            oprot.writeI16(self.id)
            oprot.writeFieldEnd()
        if self.tableGraph != None:
            oprot.writeFieldBegin('tableGraph', TType.LIST, 6)
            oprot.writeListBegin(TType.STRUCT, len(self.tableGraph))
            for iter251 in self.tableGraph:
                iter251.write(oprot)

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




class PssValueIDL(object):
    """
      Table Capability: list of one or more values.
      If single value min=max, otherwise, a range of value
    
      Attributes:
       - min
       - max
      """

    thrift_spec = (None, (1,
      TType.I64,
      'min',
      None,
      None), (2,
      TType.I64,
      'max',
      None,
      None))

    def __init__(self, min = None, max = None):
        self.min = min
        self.max = max



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
                    self.min = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.max = iprot.readI64()
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
        oprot.writeStructBegin('PssValueIDL')
        if self.min != None:
            oprot.writeFieldBegin('min', TType.I64, 1)
            oprot.writeI64(self.min)
            oprot.writeFieldEnd()
        if self.max != None:
            oprot.writeFieldBegin('max', TType.I64, 2)
            oprot.writeI64(self.max)
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




class PssValueAttrIDL(object):
    """
      Table Capability: match list of values attribute
    
      Attributes:
       - values
      """

    thrift_spec = (None, (1,
      TType.LIST,
      'values',
      (TType.STRUCT, (PssValueIDL, PssValueIDL.thrift_spec)),
      None))

    def __init__(self, values = None):
        self.values = values



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
                    self.values = []
                    (_etype255, _size252,) = iprot.readListBegin()
                    for _i256 in xrange(_size252):
                        _elem257 = PssValueIDL()
                        _elem257.read(iprot)
                        self.values.append(_elem257)

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
        oprot.writeStructBegin('PssValueAttrIDL')
        if self.values != None:
            oprot.writeFieldBegin('values', TType.LIST, 1)
            oprot.writeListBegin(TType.STRUCT, len(self.values))
            for iter258 in self.values:
                iter258.write(oprot)

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




class PssMaskAttrIDL(object):
    """
      Table Capability: match mask attributes
    
      Attributes:
       - subnet
       - arbitary
       - wildcard
      """

    thrift_spec = (None,
     (1,
      TType.BYTE,
      'subnet',
      None,
      None),
     (2,
      TType.BYTE,
      'arbitary',
      None,
      None),
     (3,
      TType.BYTE,
      'wildcard',
      None,
      None))

    def __init__(self, subnet = None, arbitary = None, wildcard = None):
        self.subnet = subnet
        self.arbitary = arbitary
        self.wildcard = wildcard



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
                    self.subnet = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.BYTE:
                    self.arbitary = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.BYTE:
                    self.wildcard = iprot.readByte()
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
        oprot.writeStructBegin('PssMaskAttrIDL')
        if self.subnet != None:
            oprot.writeFieldBegin('subnet', TType.BYTE, 1)
            oprot.writeByte(self.subnet)
            oprot.writeFieldEnd()
        if self.arbitary != None:
            oprot.writeFieldBegin('arbitary', TType.BYTE, 2)
            oprot.writeByte(self.arbitary)
            oprot.writeFieldEnd()
        if self.wildcard != None:
            oprot.writeFieldBegin('wildcard', TType.BYTE, 3)
            oprot.writeByte(self.wildcard)
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




class PssMatchAttrIDL(object):
    """
      Table Capability: match attribute
    
      Attributes:
       - type
       - attrVal
       - attrMask
      """

    thrift_spec = (None,
     (1,
      TType.I16,
      'type',
      None,
      None),
     (2,
      TType.STRUCT,
      'attrVal',
      (PssValueAttrIDL, PssValueAttrIDL.thrift_spec),
      None),
     (3,
      TType.STRUCT,
      'attrMask',
      (PssMaskAttrIDL, PssMaskAttrIDL.thrift_spec),
      None))

    def __init__(self, type = None, attrVal = None, attrMask = None):
        self.type = type
        self.attrVal = attrVal
        self.attrMask = attrMask



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
                if ftype == TType.STRUCT:
                    self.attrVal = PssValueAttrIDL()
                    self.attrVal.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRUCT:
                    self.attrMask = PssMaskAttrIDL()
                    self.attrMask.read(iprot)
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
        oprot.writeStructBegin('PssMatchAttrIDL')
        if self.type != None:
            oprot.writeFieldBegin('type', TType.I16, 1)
            oprot.writeI16(self.type)
            oprot.writeFieldEnd()
        if self.attrVal != None:
            oprot.writeFieldBegin('attrVal', TType.STRUCT, 2)
            self.attrVal.write(oprot)
            oprot.writeFieldEnd()
        if self.attrMask != None:
            oprot.writeFieldBegin('attrMask', TType.STRUCT, 3)
            self.attrMask.write(oprot)
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




class PssMatchCapIDL(object):
    """
      Table Capability: match capability
    
      Attributes:
       - type
       - supported
       - attr
      """

    thrift_spec = (None,
     (1,
      TType.I16,
      'type',
      None,
      None),
     (2,
      TType.BYTE,
      'supported',
      None,
      None),
     (3,
      TType.STRUCT,
      'attr',
      (PssMatchAttrIDL, PssMatchAttrIDL.thrift_spec),
      None))

    def __init__(self, type = None, supported = None, attr = None):
        self.type = type
        self.supported = supported
        self.attr = attr



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
                if ftype == TType.BYTE:
                    self.supported = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRUCT:
                    self.attr = PssMatchAttrIDL()
                    self.attr.read(iprot)
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
        oprot.writeStructBegin('PssMatchCapIDL')
        if self.type != None:
            oprot.writeFieldBegin('type', TType.I16, 1)
            oprot.writeI16(self.type)
            oprot.writeFieldEnd()
        if self.supported != None:
            oprot.writeFieldBegin('supported', TType.BYTE, 2)
            oprot.writeByte(self.supported)
            oprot.writeFieldEnd()
        if self.attr != None:
            oprot.writeFieldBegin('attr', TType.STRUCT, 3)
            self.attr.write(oprot)
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




class PssActionAttrIDL(object):
    """
      Table Capability: action attribute capability
    
      Attributes:
       - execType
       - forced
      """

    thrift_spec = (None, (1,
      TType.I16,
      'execType',
      None,
      None), (2,
      TType.BYTE,
      'forced',
      None,
      None))

    def __init__(self, execType = None, forced = None):
        self.execType = execType
        self.forced = forced



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
                    self.execType = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.BYTE:
                    self.forced = iprot.readByte()
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
        oprot.writeStructBegin('PssActionAttrIDL')
        if self.execType != None:
            oprot.writeFieldBegin('execType', TType.I16, 1)
            oprot.writeI16(self.execType)
            oprot.writeFieldEnd()
        if self.forced != None:
            oprot.writeFieldBegin('forced', TType.BYTE, 2)
            oprot.writeByte(self.forced)
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




class PssActionCapIDL(object):
    """
      Table Capability: action capability
      based on xos_plc_action_capability_t
    
      Attributes:
       - type
       - supported
       - attr
       - maxCount
       - order
      """

    thrift_spec = (None,
     (1,
      TType.I16,
      'type',
      None,
      None),
     (2,
      TType.BYTE,
      'supported',
      None,
      None),
     (3,
      TType.STRUCT,
      'attr',
      (PssActionAttrIDL, PssActionAttrIDL.thrift_spec),
      None),
     (4,
      TType.I16,
      'maxCount',
      None,
      None),
     (5,
      TType.I16,
      'order',
      None,
      None))

    def __init__(self, type = None, supported = None, attr = None, maxCount = None, order = None):
        self.type = type
        self.supported = supported
        self.attr = attr
        self.maxCount = maxCount
        self.order = order



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
                if ftype == TType.BYTE:
                    self.supported = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRUCT:
                    self.attr = PssActionAttrIDL()
                    self.attr.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I16:
                    self.maxCount = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I16:
                    self.order = iprot.readI16()
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
        oprot.writeStructBegin('PssActionCapIDL')
        if self.type != None:
            oprot.writeFieldBegin('type', TType.I16, 1)
            oprot.writeI16(self.type)
            oprot.writeFieldEnd()
        if self.supported != None:
            oprot.writeFieldBegin('supported', TType.BYTE, 2)
            oprot.writeByte(self.supported)
            oprot.writeFieldEnd()
        if self.attr != None:
            oprot.writeFieldBegin('attr', TType.STRUCT, 3)
            self.attr.write(oprot)
            oprot.writeFieldEnd()
        if self.maxCount != None:
            oprot.writeFieldBegin('maxCount', TType.I16, 4)
            oprot.writeI16(self.maxCount)
            oprot.writeFieldEnd()
        if self.order != None:
            oprot.writeFieldBegin('order', TType.I16, 5)
            oprot.writeI16(self.order)
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




class PssTblStatsCapIDL(object):
    """
      Table Capability:  stats cap
      based on xos_plc_stats_cap_t
    
      Attributes:
       - clsAggTgtAggStats
       - clsTgtAggStats
       - clsTgtStats
       - tblTgtStats
       - actTgtStats
      """

    thrift_spec = (None,
     (1,
      TType.BYTE,
      'clsAggTgtAggStats',
      None,
      None),
     (2,
      TType.BYTE,
      'clsTgtAggStats',
      None,
      None),
     (3,
      TType.BYTE,
      'clsTgtStats',
      None,
      None),
     (4,
      TType.BYTE,
      'tblTgtStats',
      None,
      None),
     (5,
      TType.BYTE,
      'actTgtStats',
      None,
      None))

    def __init__(self, clsAggTgtAggStats = None, clsTgtAggStats = None, clsTgtStats = None, tblTgtStats = None, actTgtStats = None):
        self.clsAggTgtAggStats = clsAggTgtAggStats
        self.clsTgtAggStats = clsTgtAggStats
        self.clsTgtStats = clsTgtStats
        self.tblTgtStats = tblTgtStats
        self.actTgtStats = actTgtStats



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
                    self.clsAggTgtAggStats = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.BYTE:
                    self.clsTgtAggStats = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.BYTE:
                    self.clsTgtStats = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.BYTE:
                    self.tblTgtStats = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.BYTE:
                    self.actTgtStats = iprot.readByte()
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
        oprot.writeStructBegin('PssTblStatsCapIDL')
        if self.clsAggTgtAggStats != None:
            oprot.writeFieldBegin('clsAggTgtAggStats', TType.BYTE, 1)
            oprot.writeByte(self.clsAggTgtAggStats)
            oprot.writeFieldEnd()
        if self.clsTgtAggStats != None:
            oprot.writeFieldBegin('clsTgtAggStats', TType.BYTE, 2)
            oprot.writeByte(self.clsTgtAggStats)
            oprot.writeFieldEnd()
        if self.clsTgtStats != None:
            oprot.writeFieldBegin('clsTgtStats', TType.BYTE, 3)
            oprot.writeByte(self.clsTgtStats)
            oprot.writeFieldEnd()
        if self.tblTgtStats != None:
            oprot.writeFieldBegin('tblTgtStats', TType.BYTE, 4)
            oprot.writeByte(self.tblTgtStats)
            oprot.writeFieldEnd()
        if self.actTgtStats != None:
            oprot.writeFieldBegin('actTgtStats', TType.BYTE, 5)
            oprot.writeByte(self.actTgtStats)
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




class PssTransientCapIDL(object):
    """
      Table Capability: transient capability
      based on xos_plc_transient_cap_t
    
      Attributes:
       - trans
      """

    thrift_spec = (None, (1,
      TType.BYTE,
      'trans',
      None,
      None))

    def __init__(self, trans = None):
        self.trans = trans



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
                    self.trans = iprot.readByte()
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
        oprot.writeStructBegin('PssTransientCapIDL')
        if self.trans != None:
            oprot.writeFieldBegin('trans', TType.BYTE, 1)
            oprot.writeByte(self.trans)
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




class PssPersistCapIDL(object):
    """
      Table Capability: persistent capability
      based on xos_plc_persistent_cap_t
    
      Attributes:
       - persist
      """

    thrift_spec = (None, (1,
      TType.BYTE,
      'persist',
      None,
      None))

    def __init__(self, persist = None):
        self.persist = persist



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
                    self.persist = iprot.readByte()
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
        oprot.writeStructBegin('PssPersistCapIDL')
        if self.persist != None:
            oprot.writeFieldBegin('persist', TType.BYTE, 1)
            oprot.writeByte(self.persist)
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




class PssTableClassCapIDL(object):
    """
      Table Capability: table class capability
      based on xos_plc_table_class_cap_t
    
      Attributes:
       - cmapClassSupp
       - clsSeqNumSupp
       - clsOrderSupp
       - clsTimeoutSupp
       - inlineClsSupp
       - clsProvRate
       - clsPerTbl
      """

    thrift_spec = (None,
     (1,
      TType.BYTE,
      'cmapClassSupp',
      None,
      None),
     (2,
      TType.BYTE,
      'clsSeqNumSupp',
      None,
      None),
     (3,
      TType.BYTE,
      'clsOrderSupp',
      None,
      None),
     (4,
      TType.BYTE,
      'clsTimeoutSupp',
      None,
      None),
     (5,
      TType.BYTE,
      'inlineClsSupp',
      None,
      None),
     (6,
      TType.I32,
      'clsProvRate',
      None,
      None),
     (7,
      TType.I32,
      'clsPerTbl',
      None,
      None))

    def __init__(self, cmapClassSupp = None, clsSeqNumSupp = None, clsOrderSupp = None, clsTimeoutSupp = None, inlineClsSupp = None, clsProvRate = None, clsPerTbl = None):
        self.cmapClassSupp = cmapClassSupp
        self.clsSeqNumSupp = clsSeqNumSupp
        self.clsOrderSupp = clsOrderSupp
        self.clsTimeoutSupp = clsTimeoutSupp
        self.inlineClsSupp = inlineClsSupp
        self.clsProvRate = clsProvRate
        self.clsPerTbl = clsPerTbl



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
                    self.cmapClassSupp = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.BYTE:
                    self.clsSeqNumSupp = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.BYTE:
                    self.clsOrderSupp = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.BYTE:
                    self.clsTimeoutSupp = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.BYTE:
                    self.inlineClsSupp = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I32:
                    self.clsProvRate = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I32:
                    self.clsPerTbl = iprot.readI32()
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
        oprot.writeStructBegin('PssTableClassCapIDL')
        if self.cmapClassSupp != None:
            oprot.writeFieldBegin('cmapClassSupp', TType.BYTE, 1)
            oprot.writeByte(self.cmapClassSupp)
            oprot.writeFieldEnd()
        if self.clsSeqNumSupp != None:
            oprot.writeFieldBegin('clsSeqNumSupp', TType.BYTE, 2)
            oprot.writeByte(self.clsSeqNumSupp)
            oprot.writeFieldEnd()
        if self.clsOrderSupp != None:
            oprot.writeFieldBegin('clsOrderSupp', TType.BYTE, 3)
            oprot.writeByte(self.clsOrderSupp)
            oprot.writeFieldEnd()
        if self.clsTimeoutSupp != None:
            oprot.writeFieldBegin('clsTimeoutSupp', TType.BYTE, 4)
            oprot.writeByte(self.clsTimeoutSupp)
            oprot.writeFieldEnd()
        if self.inlineClsSupp != None:
            oprot.writeFieldBegin('inlineClsSupp', TType.BYTE, 5)
            oprot.writeByte(self.inlineClsSupp)
            oprot.writeFieldEnd()
        if self.clsProvRate != None:
            oprot.writeFieldBegin('clsProvRate', TType.I32, 6)
            oprot.writeI32(self.clsProvRate)
            oprot.writeFieldEnd()
        if self.clsPerTbl != None:
            oprot.writeFieldBegin('clsPerTbl', TType.I32, 7)
            oprot.writeI32(self.clsPerTbl)
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




class PssStaticEntryCapIDL(object):
    """
      Table Capability: static entry capability
      based on xos_plc_static_class_info_t
    
      Attributes:
       - seqNum
       - matchList
       - actionList
      """

    thrift_spec = (None,
     (1,
      TType.I32,
      'seqNum',
      None,
      None),
     (2,
      TType.LIST,
      'matchList',
      (TType.STRUCT, (MatchIDL, MatchIDL.thrift_spec)),
      None),
     (3,
      TType.LIST,
      'actionList',
      (TType.STRUCT, (ActionIDL, ActionIDL.thrift_spec)),
      None))

    def __init__(self, seqNum = None, matchList = None, actionList = None):
        self.seqNum = seqNum
        self.matchList = matchList
        self.actionList = actionList



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
                if ftype == TType.LIST:
                    self.matchList = []
                    (_etype262, _size259,) = iprot.readListBegin()
                    for _i263 in xrange(_size259):
                        _elem264 = MatchIDL()
                        _elem264.read(iprot)
                        self.matchList.append(_elem264)

                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.LIST:
                    self.actionList = []
                    (_etype268, _size265,) = iprot.readListBegin()
                    for _i269 in xrange(_size265):
                        _elem270 = ActionIDL()
                        _elem270.read(iprot)
                        self.actionList.append(_elem270)

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
        oprot.writeStructBegin('PssStaticEntryCapIDL')
        if self.seqNum != None:
            oprot.writeFieldBegin('seqNum', TType.I32, 1)
            oprot.writeI32(self.seqNum)
            oprot.writeFieldEnd()
        if self.matchList != None:
            oprot.writeFieldBegin('matchList', TType.LIST, 2)
            oprot.writeListBegin(TType.STRUCT, len(self.matchList))
            for iter271 in self.matchList:
                iter271.write(oprot)

            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.actionList != None:
            oprot.writeFieldBegin('actionList', TType.LIST, 3)
            oprot.writeListBegin(TType.STRUCT, len(self.actionList))
            for iter272 in self.actionList:
                iter272.write(oprot)

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




class PssTableCapIDL(object):
    """
      Policy Table capability
      based on xos_plc_table_caps_t
    
      Attributes:
       - name
       - type
       - handle
       - seqNum
       - maxEntries
       - pktPerSec
       - updPerSec
       - trans
       - persist
       - actions
       - matches
       - forwards
       - stats
       - classcap
       - programmable
       - defaultActions
       - staticEntries
       - defEntActions
       - bindToSubintf
       - perOplistMaxPmapEntries
      """

    thrift_spec = (None,
     (1,
      TType.STRING,
      'name',
      None,
      None),
     (2,
      TType.I16,
      'type',
      None,
      None),
     (3,
      TType.I64,
      'handle',
      None,
      None),
     (4,
      TType.I32,
      'seqNum',
      None,
      None),
     (5,
      TType.I32,
      'maxEntries',
      None,
      None),
     (6,
      TType.I64,
      'pktPerSec',
      None,
      None),
     (7,
      TType.I64,
      'updPerSec',
      None,
      None),
     (8,
      TType.BYTE,
      'trans',
      None,
      None),
     (9,
      TType.BYTE,
      'persist',
      None,
      None),
     (10,
      TType.LIST,
      'actions',
      (TType.STRUCT, (PssActionCapIDL, PssActionCapIDL.thrift_spec)),
      None),
     (11,
      TType.LIST,
      'matches',
      (TType.STRUCT, (PssMatchCapIDL, PssMatchCapIDL.thrift_spec)),
      None),
     (12,
      TType.LIST,
      'forwards',
      (TType.I16, None),
      None),
     (13,
      TType.STRUCT,
      'stats',
      (PssTblStatsCapIDL, PssTblStatsCapIDL.thrift_spec),
      None),
     (14,
      TType.STRUCT,
      'classcap',
      (PssTableClassCapIDL, PssTableClassCapIDL.thrift_spec),
      None),
     (15,
      TType.BYTE,
      'programmable',
      None,
      None),
     (16,
      TType.LIST,
      'defaultActions',
      (TType.STRUCT, (ActionIDL, ActionIDL.thrift_spec)),
      None),
     (17,
      TType.LIST,
      'staticEntries',
      (TType.STRUCT, (PssStaticEntryCapIDL, PssStaticEntryCapIDL.thrift_spec)),
      None),
     (18,
      TType.LIST,
      'defEntActions',
      (TType.STRUCT, (PssActionCapIDL, PssActionCapIDL.thrift_spec)),
      None),
     (19,
      TType.BYTE,
      'bindToSubintf',
      None,
      None),
     (20,
      TType.I32,
      'perOplistMaxPmapEntries',
      None,
      None))

    def __init__(self, name = None, type = None, handle = None, seqNum = None, maxEntries = None, pktPerSec = None, updPerSec = None, trans = None, persist = None, actions = None, matches = None, forwards = None, stats = None, classcap = None, programmable = None, defaultActions = None, staticEntries = None, defEntActions = None, bindToSubintf = None, perOplistMaxPmapEntries = None):
        self.name = name
        self.type = type
        self.handle = handle
        self.seqNum = seqNum
        self.maxEntries = maxEntries
        self.pktPerSec = pktPerSec
        self.updPerSec = updPerSec
        self.trans = trans
        self.persist = persist
        self.actions = actions
        self.matches = matches
        self.forwards = forwards
        self.stats = stats
        self.classcap = classcap
        self.programmable = programmable
        self.defaultActions = defaultActions
        self.staticEntries = staticEntries
        self.defEntActions = defEntActions
        self.bindToSubintf = bindToSubintf
        self.perOplistMaxPmapEntries = perOplistMaxPmapEntries



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
                if ftype == TType.I16:
                    self.type = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I64:
                    self.handle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.seqNum = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.maxEntries = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I64:
                    self.pktPerSec = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I64:
                    self.updPerSec = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.BYTE:
                    self.trans = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.BYTE:
                    self.persist = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.LIST:
                    self.actions = []
                    (_etype276, _size273,) = iprot.readListBegin()
                    for _i277 in xrange(_size273):
                        _elem278 = PssActionCapIDL()
                        _elem278.read(iprot)
                        self.actions.append(_elem278)

                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.LIST:
                    self.matches = []
                    (_etype282, _size279,) = iprot.readListBegin()
                    for _i283 in xrange(_size279):
                        _elem284 = PssMatchCapIDL()
                        _elem284.read(iprot)
                        self.matches.append(_elem284)

                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 12:
                if ftype == TType.LIST:
                    self.forwards = []
                    (_etype288, _size285,) = iprot.readListBegin()
                    for _i289 in xrange(_size285):
                        _elem290 = iprot.readI16()
                        self.forwards.append(_elem290)

                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 13:
                if ftype == TType.STRUCT:
                    self.stats = PssTblStatsCapIDL()
                    self.stats.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 14:
                if ftype == TType.STRUCT:
                    self.classcap = PssTableClassCapIDL()
                    self.classcap.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 15:
                if ftype == TType.BYTE:
                    self.programmable = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 16:
                if ftype == TType.LIST:
                    self.defaultActions = []
                    (_etype294, _size291,) = iprot.readListBegin()
                    for _i295 in xrange(_size291):
                        _elem296 = ActionIDL()
                        _elem296.read(iprot)
                        self.defaultActions.append(_elem296)

                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 17:
                if ftype == TType.LIST:
                    self.staticEntries = []
                    (_etype300, _size297,) = iprot.readListBegin()
                    for _i301 in xrange(_size297):
                        _elem302 = PssStaticEntryCapIDL()
                        _elem302.read(iprot)
                        self.staticEntries.append(_elem302)

                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 18:
                if ftype == TType.LIST:
                    self.defEntActions = []
                    (_etype306, _size303,) = iprot.readListBegin()
                    for _i307 in xrange(_size303):
                        _elem308 = PssActionCapIDL()
                        _elem308.read(iprot)
                        self.defEntActions.append(_elem308)

                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 19:
                if ftype == TType.BYTE:
                    self.bindToSubintf = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 20:
                if ftype == TType.I32:
                    self.perOplistMaxPmapEntries = iprot.readI32()
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
        oprot.writeStructBegin('PssTableCapIDL')
        if self.name != None:
            oprot.writeFieldBegin('name', TType.STRING, 1)
            oprot.writeString(self.name)
            oprot.writeFieldEnd()
        if self.type != None:
            oprot.writeFieldBegin('type', TType.I16, 2)
            oprot.writeI16(self.type)
            oprot.writeFieldEnd()
        if self.handle != None:
            oprot.writeFieldBegin('handle', TType.I64, 3)
            oprot.writeI64(self.handle)
            oprot.writeFieldEnd()
        if self.seqNum != None:
            oprot.writeFieldBegin('seqNum', TType.I32, 4)
            oprot.writeI32(self.seqNum)
            oprot.writeFieldEnd()
        if self.maxEntries != None:
            oprot.writeFieldBegin('maxEntries', TType.I32, 5)
            oprot.writeI32(self.maxEntries)
            oprot.writeFieldEnd()
        if self.pktPerSec != None:
            oprot.writeFieldBegin('pktPerSec', TType.I64, 6)
            oprot.writeI64(self.pktPerSec)
            oprot.writeFieldEnd()
        if self.updPerSec != None:
            oprot.writeFieldBegin('updPerSec', TType.I64, 7)
            oprot.writeI64(self.updPerSec)
            oprot.writeFieldEnd()
        if self.trans != None:
            oprot.writeFieldBegin('trans', TType.BYTE, 8)
            oprot.writeByte(self.trans)
            oprot.writeFieldEnd()
        if self.persist != None:
            oprot.writeFieldBegin('persist', TType.BYTE, 9)
            oprot.writeByte(self.persist)
            oprot.writeFieldEnd()
        if self.actions != None:
            oprot.writeFieldBegin('actions', TType.LIST, 10)
            oprot.writeListBegin(TType.STRUCT, len(self.actions))
            for iter309 in self.actions:
                iter309.write(oprot)

            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.matches != None:
            oprot.writeFieldBegin('matches', TType.LIST, 11)
            oprot.writeListBegin(TType.STRUCT, len(self.matches))
            for iter310 in self.matches:
                iter310.write(oprot)

            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.forwards != None:
            oprot.writeFieldBegin('forwards', TType.LIST, 12)
            oprot.writeListBegin(TType.I16, len(self.forwards))
            for iter311 in self.forwards:
                oprot.writeI16(iter311)

            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.stats != None:
            oprot.writeFieldBegin('stats', TType.STRUCT, 13)
            self.stats.write(oprot)
            oprot.writeFieldEnd()
        if self.classcap != None:
            oprot.writeFieldBegin('classcap', TType.STRUCT, 14)
            self.classcap.write(oprot)
            oprot.writeFieldEnd()
        if self.programmable != None:
            oprot.writeFieldBegin('programmable', TType.BYTE, 15)
            oprot.writeByte(self.programmable)
            oprot.writeFieldEnd()
        if self.defaultActions != None:
            oprot.writeFieldBegin('defaultActions', TType.LIST, 16)
            oprot.writeListBegin(TType.STRUCT, len(self.defaultActions))
            for iter312 in self.defaultActions:
                iter312.write(oprot)

            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.staticEntries != None:
            oprot.writeFieldBegin('staticEntries', TType.LIST, 17)
            oprot.writeListBegin(TType.STRUCT, len(self.staticEntries))
            for iter313 in self.staticEntries:
                iter313.write(oprot)

            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.defEntActions != None:
            oprot.writeFieldBegin('defEntActions', TType.LIST, 18)
            oprot.writeListBegin(TType.STRUCT, len(self.defEntActions))
            for iter314 in self.defEntActions:
                iter314.write(oprot)

            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.bindToSubintf != None:
            oprot.writeFieldBegin('bindToSubintf', TType.BYTE, 19)
            oprot.writeByte(self.bindToSubintf)
            oprot.writeFieldEnd()
        if self.perOplistMaxPmapEntries != None:
            oprot.writeFieldBegin('perOplistMaxPmapEntries', TType.I32, 20)
            oprot.writeI32(self.perOplistMaxPmapEntries)
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




class PssSysCapIDL(object):
    """
      Global capability: system cap
    
      Attributes:
       - maxInlineClasses
       - maxPolicyMaps
      """

    thrift_spec = (None, (1,
      TType.I32,
      'maxInlineClasses',
      None,
      None), (2,
      TType.I32,
      'maxPolicyMaps',
      None,
      None))

    def __init__(self, maxInlineClasses = None, maxPolicyMaps = None):
        self.maxInlineClasses = maxInlineClasses
        self.maxPolicyMaps = maxPolicyMaps



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
                    self.maxInlineClasses = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.maxPolicyMaps = iprot.readI32()
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
        oprot.writeStructBegin('PssSysCapIDL')
        if self.maxInlineClasses != None:
            oprot.writeFieldBegin('maxInlineClasses', TType.I32, 1)
            oprot.writeI32(self.maxInlineClasses)
            oprot.writeFieldEnd()
        if self.maxPolicyMaps != None:
            oprot.writeFieldBegin('maxPolicyMaps', TType.I32, 2)
            oprot.writeI32(self.maxPolicyMaps)
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




class PssAtomicCapIDL(object):
    """
      Global capability: atomicity cap
    
      Attributes:
       - bulkInstance
       - inlineClass
       - policyMap
      """

    thrift_spec = (None,
     (1,
      TType.BYTE,
      'bulkInstance',
      None,
      None),
     (2,
      TType.BYTE,
      'inlineClass',
      None,
      None),
     (3,
      TType.BYTE,
      'policyMap',
      None,
      None))

    def __init__(self, bulkInstance = None, inlineClass = None, policyMap = None):
        self.bulkInstance = bulkInstance
        self.inlineClass = inlineClass
        self.policyMap = policyMap



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
                    self.bulkInstance = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.BYTE:
                    self.inlineClass = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.BYTE:
                    self.policyMap = iprot.readByte()
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
        oprot.writeStructBegin('PssAtomicCapIDL')
        if self.bulkInstance != None:
            oprot.writeFieldBegin('bulkInstance', TType.BYTE, 1)
            oprot.writeByte(self.bulkInstance)
            oprot.writeFieldEnd()
        if self.inlineClass != None:
            oprot.writeFieldBegin('inlineClass', TType.BYTE, 2)
            oprot.writeByte(self.inlineClass)
            oprot.writeFieldEnd()
        if self.policyMap != None:
            oprot.writeFieldBegin('policyMap', TType.BYTE, 3)
            oprot.writeByte(self.policyMap)
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




class PssStatsCapIDL(object):
    """
      Global capability: stats cap
    
      Attributes:
       - pollingRate
      """

    thrift_spec = (None, (1,
      TType.I32,
      'pollingRate',
      None,
      None))

    def __init__(self, pollingRate = None):
        self.pollingRate = pollingRate



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
                    self.pollingRate = iprot.readI32()
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
        oprot.writeStructBegin('PssStatsCapIDL')
        if self.pollingRate != None:
            oprot.writeFieldBegin('pollingRate', TType.I32, 1)
            oprot.writeI32(self.pollingRate)
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




class PssCookieCapIDL(object):
    """
      Global capability: cookie cap
    
      Attributes:
       - pmapCookieSupp
       - inlineClassCookieSupp
      """

    thrift_spec = (None, (1,
      TType.BYTE,
      'pmapCookieSupp',
      None,
      None), (2,
      TType.BYTE,
      'inlineClassCookieSupp',
      None,
      None))

    def __init__(self, pmapCookieSupp = None, inlineClassCookieSupp = None):
        self.pmapCookieSupp = pmapCookieSupp
        self.inlineClassCookieSupp = inlineClassCookieSupp



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
                    self.pmapCookieSupp = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.BYTE:
                    self.inlineClassCookieSupp = iprot.readByte()
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
        oprot.writeStructBegin('PssCookieCapIDL')
        if self.pmapCookieSupp != None:
            oprot.writeFieldBegin('pmapCookieSupp', TType.BYTE, 1)
            oprot.writeByte(self.pmapCookieSupp)
            oprot.writeFieldEnd()
        if self.inlineClassCookieSupp != None:
            oprot.writeFieldBegin('inlineClassCookieSupp', TType.BYTE, 2)
            oprot.writeByte(self.inlineClassCookieSupp)
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




class PssStatusCapIDL(object):
    """
      Global capability: status cap
    
      Attributes:
       - matchOp
       - actionOp
       - inlineClassOp
       - cmapOp
       - pmapOp
       - bulkOp
      """

    thrift_spec = (None,
     (1,
      TType.BYTE,
      'matchOp',
      None,
      None),
     (2,
      TType.BYTE,
      'actionOp',
      None,
      None),
     (3,
      TType.BYTE,
      'inlineClassOp',
      None,
      None),
     (4,
      TType.BYTE,
      'cmapOp',
      None,
      None),
     (5,
      TType.BYTE,
      'pmapOp',
      None,
      None),
     (6,
      TType.BYTE,
      'bulkOp',
      None,
      None))

    def __init__(self, matchOp = None, actionOp = None, inlineClassOp = None, cmapOp = None, pmapOp = None, bulkOp = None):
        self.matchOp = matchOp
        self.actionOp = actionOp
        self.inlineClassOp = inlineClassOp
        self.cmapOp = cmapOp
        self.pmapOp = pmapOp
        self.bulkOp = bulkOp



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
                    self.matchOp = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.BYTE:
                    self.actionOp = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.BYTE:
                    self.inlineClassOp = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.BYTE:
                    self.cmapOp = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.BYTE:
                    self.pmapOp = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.BYTE:
                    self.bulkOp = iprot.readByte()
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
        oprot.writeStructBegin('PssStatusCapIDL')
        if self.matchOp != None:
            oprot.writeFieldBegin('matchOp', TType.BYTE, 1)
            oprot.writeByte(self.matchOp)
            oprot.writeFieldEnd()
        if self.actionOp != None:
            oprot.writeFieldBegin('actionOp', TType.BYTE, 2)
            oprot.writeByte(self.actionOp)
            oprot.writeFieldEnd()
        if self.inlineClassOp != None:
            oprot.writeFieldBegin('inlineClassOp', TType.BYTE, 3)
            oprot.writeByte(self.inlineClassOp)
            oprot.writeFieldEnd()
        if self.cmapOp != None:
            oprot.writeFieldBegin('cmapOp', TType.BYTE, 4)
            oprot.writeByte(self.cmapOp)
            oprot.writeFieldEnd()
        if self.pmapOp != None:
            oprot.writeFieldBegin('pmapOp', TType.BYTE, 5)
            oprot.writeByte(self.pmapOp)
            oprot.writeFieldEnd()
        if self.bulkOp != None:
            oprot.writeFieldBegin('bulkOp', TType.BYTE, 6)
            oprot.writeByte(self.bulkOp)
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




class PssEffortCapIDL(object):
    """
      Global capability: best effort cap
    
      Attributes:
       - bulkEffort
      """

    thrift_spec = (None, (1,
      TType.BYTE,
      'bulkEffort',
      None,
      None))

    def __init__(self, bulkEffort = None):
        self.bulkEffort = bulkEffort



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
                    self.bulkEffort = iprot.readByte()
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
        oprot.writeStructBegin('PssEffortCapIDL')
        if self.bulkEffort != None:
            oprot.writeFieldBegin('bulkEffort', TType.BYTE, 1)
            oprot.writeByte(self.bulkEffort)
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




class PssGlobalCapIDL(object):
    """
      Policy Global capability
      based on xos_plc_gl_cap_t
    
      Attributes:
       - system
       - atomicity
       - stats
       - cookie
       - status
       - effort
       - tables
       - pipelines
      """

    thrift_spec = (None,
     (1,
      TType.STRUCT,
      'system',
      (PssSysCapIDL, PssSysCapIDL.thrift_spec),
      None),
     (2,
      TType.STRUCT,
      'atomicity',
      (PssAtomicCapIDL, PssAtomicCapIDL.thrift_spec),
      None),
     (3,
      TType.STRUCT,
      'stats',
      (PssStatsCapIDL, PssStatsCapIDL.thrift_spec),
      None),
     (4,
      TType.STRUCT,
      'cookie',
      (PssCookieCapIDL, PssCookieCapIDL.thrift_spec),
      None),
     (5,
      TType.STRUCT,
      'status',
      (PssStatusCapIDL, PssStatusCapIDL.thrift_spec),
      None),
     (6,
      TType.STRUCT,
      'effort',
      (PssEffortCapIDL, PssEffortCapIDL.thrift_spec),
      None),
     (7,
      TType.LIST,
      'tables',
      (TType.STRUCT, (PssTableCapIDL, PssTableCapIDL.thrift_spec)),
      None),
     (8,
      TType.LIST,
      'pipelines',
      (TType.STRUCT, (PssPipelineCapIDL, PssPipelineCapIDL.thrift_spec)),
      None))

    def __init__(self, system = None, atomicity = None, stats = None, cookie = None, status = None, effort = None, tables = None, pipelines = None):
        self.system = system
        self.atomicity = atomicity
        self.stats = stats
        self.cookie = cookie
        self.status = status
        self.effort = effort
        self.tables = tables
        self.pipelines = pipelines



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
                    self.system = PssSysCapIDL()
                    self.system.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.atomicity = PssAtomicCapIDL()
                    self.atomicity.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRUCT:
                    self.stats = PssStatsCapIDL()
                    self.stats.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRUCT:
                    self.cookie = PssCookieCapIDL()
                    self.cookie.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRUCT:
                    self.status = PssStatusCapIDL()
                    self.status.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRUCT:
                    self.effort = PssEffortCapIDL()
                    self.effort.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.LIST:
                    self.tables = []
                    (_etype318, _size315,) = iprot.readListBegin()
                    for _i319 in xrange(_size315):
                        _elem320 = PssTableCapIDL()
                        _elem320.read(iprot)
                        self.tables.append(_elem320)

                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.LIST:
                    self.pipelines = []
                    (_etype324, _size321,) = iprot.readListBegin()
                    for _i325 in xrange(_size321):
                        _elem326 = PssPipelineCapIDL()
                        _elem326.read(iprot)
                        self.pipelines.append(_elem326)

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
        oprot.writeStructBegin('PssGlobalCapIDL')
        if self.system != None:
            oprot.writeFieldBegin('system', TType.STRUCT, 1)
            self.system.write(oprot)
            oprot.writeFieldEnd()
        if self.atomicity != None:
            oprot.writeFieldBegin('atomicity', TType.STRUCT, 2)
            self.atomicity.write(oprot)
            oprot.writeFieldEnd()
        if self.stats != None:
            oprot.writeFieldBegin('stats', TType.STRUCT, 3)
            self.stats.write(oprot)
            oprot.writeFieldEnd()
        if self.cookie != None:
            oprot.writeFieldBegin('cookie', TType.STRUCT, 4)
            self.cookie.write(oprot)
            oprot.writeFieldEnd()
        if self.status != None:
            oprot.writeFieldBegin('status', TType.STRUCT, 5)
            self.status.write(oprot)
            oprot.writeFieldEnd()
        if self.effort != None:
            oprot.writeFieldBegin('effort', TType.STRUCT, 6)
            self.effort.write(oprot)
            oprot.writeFieldEnd()
        if self.tables != None:
            oprot.writeFieldBegin('tables', TType.LIST, 7)
            oprot.writeListBegin(TType.STRUCT, len(self.tables))
            for iter327 in self.tables:
                iter327.write(oprot)

            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.pipelines != None:
            oprot.writeFieldBegin('pipelines', TType.LIST, 8)
            oprot.writeListBegin(TType.STRUCT, len(self.pipelines))
            for iter328 in self.pipelines:
                iter328.write(oprot)

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
# 2015.02.05 17:22:30 IST
