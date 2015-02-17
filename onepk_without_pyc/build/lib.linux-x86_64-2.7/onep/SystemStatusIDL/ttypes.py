# 2015.02.05 17:20:15 IST
from thrift.Thrift import *
import Shared.ttypes
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
    from thrift.protocol import fastbinary
except:
    fastbinary = None

class ProcessIDL(object):
    """
      ----------------------------
      Process related information
      ---------------------------
    
      Attributes:
       - processID
       - processName
       - allocatedMemory
       - freedMemory
       - heldMemory
       - cpuUsage
      """

    thrift_spec = (None,
     (1,
      TType.I32,
      'processID',
      None,
      -1),
     (2,
      TType.STRING,
      'processName',
      None,
      ''),
     (3,
      TType.I64,
      'allocatedMemory',
      None,
      0),
     (4,
      TType.I64,
      'freedMemory',
      None,
      0),
     (5,
      TType.I64,
      'heldMemory',
      None,
      0),
     (6,
      TType.STRING,
      'cpuUsage',
      None,
      ''))

    def __init__(self, processID = thrift_spec[1][4], processName = thrift_spec[2][4], allocatedMemory = thrift_spec[3][4], freedMemory = thrift_spec[4][4], heldMemory = thrift_spec[5][4], cpuUsage = thrift_spec[6][4]):
        self.processID = processID
        self.processName = processName
        self.allocatedMemory = allocatedMemory
        self.freedMemory = freedMemory
        self.heldMemory = heldMemory
        self.cpuUsage = cpuUsage



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
                    self.processID = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.processName = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I64:
                    self.allocatedMemory = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I64:
                    self.freedMemory = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I64:
                    self.heldMemory = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRING:
                    self.cpuUsage = iprot.readString()
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
        oprot.writeStructBegin('ProcessIDL')
        if self.processID != None:
            oprot.writeFieldBegin('processID', TType.I32, 1)
            oprot.writeI32(self.processID)
            oprot.writeFieldEnd()
        if self.processName != None:
            oprot.writeFieldBegin('processName', TType.STRING, 2)
            oprot.writeString(self.processName)
            oprot.writeFieldEnd()
        if self.allocatedMemory != None:
            oprot.writeFieldBegin('allocatedMemory', TType.I64, 3)
            oprot.writeI64(self.allocatedMemory)
            oprot.writeFieldEnd()
        if self.freedMemory != None:
            oprot.writeFieldBegin('freedMemory', TType.I64, 4)
            oprot.writeI64(self.freedMemory)
            oprot.writeFieldEnd()
        if self.heldMemory != None:
            oprot.writeFieldBegin('heldMemory', TType.I64, 5)
            oprot.writeI64(self.heldMemory)
            oprot.writeFieldEnd()
        if self.cpuUsage != None:
            oprot.writeFieldBegin('cpuUsage', TType.STRING, 6)
            oprot.writeString(self.cpuUsage)
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




class ProcessDetailIDL(object):
    """
    Attributes:
     - samplingInterval
     - processList
    """

    thrift_spec = (None, (1,
      TType.I32,
      'samplingInterval',
      None,
      0), (2,
      TType.LIST,
      'processList',
      (TType.STRUCT, (ProcessIDL, ProcessIDL.thrift_spec)),
      None))

    def __init__(self, samplingInterval = thrift_spec[1][4], processList = None):
        self.samplingInterval = samplingInterval
        self.processList = processList



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
                    self.samplingInterval = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.processList = []
                    (_etype3, _size0,) = iprot.readListBegin()
                    for _i4 in xrange(_size0):
                        _elem5 = ProcessIDL()
                        _elem5.read(iprot)
                        self.processList.append(_elem5)

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
        oprot.writeStructBegin('ProcessDetailIDL')
        if self.samplingInterval != None:
            oprot.writeFieldBegin('samplingInterval', TType.I32, 1)
            oprot.writeI32(self.samplingInterval)
            oprot.writeFieldEnd()
        if self.processList != None:
            oprot.writeFieldBegin('processList', TType.LIST, 2)
            oprot.writeListBegin(TType.STRUCT, len(self.processList))
            for iter6 in self.processList:
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




class CPUUsageIDL(object):
    """
      ------------------------------------------
        System CPU Usage containing
        cpu utilization and time period
        for which CPU utilization is retrieved
      ------------------------------------------
    
      Attributes:
       - samplingInterval
       - cpu_usage
      """

    thrift_spec = (None, (1,
      TType.I32,
      'samplingInterval',
      None,
      0), (2,
      TType.I32,
      'cpu_usage',
      None,
      None))

    def __init__(self, samplingInterval = thrift_spec[1][4], cpu_usage = None):
        self.samplingInterval = samplingInterval
        self.cpu_usage = cpu_usage



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
                    self.samplingInterval = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.cpu_usage = iprot.readI32()
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
        oprot.writeStructBegin('CPUUsageIDL')
        if self.samplingInterval != None:
            oprot.writeFieldBegin('samplingInterval', TType.I32, 1)
            oprot.writeI32(self.samplingInterval)
            oprot.writeFieldEnd()
        if self.cpu_usage != None:
            oprot.writeFieldBegin('cpu_usage', TType.I32, 2)
            oprot.writeI32(self.cpu_usage)
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
# 2015.02.05 17:20:16 IST
