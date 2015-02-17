# 2015.02.05 17:18:47 IST
from thrift.Thrift import *
import Shared.ttypes
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
    from thrift.protocol import fastbinary
except:
    fastbinary = None

class CmdExecutionResultsIDL(object):
    """
      Command Execution results
    
      Attributes:
       - inputLine
       - parseReturnCode
       - errorLocation
      """

    thrift_spec = (None,
     (1,
      TType.STRING,
      'inputLine',
      None,
      None),
     (2,
      TType.I32,
      'parseReturnCode',
      None,
      None),
     (3,
      TType.I32,
      'errorLocation',
      None,
      None))

    def __init__(self, inputLine = None, parseReturnCode = None, errorLocation = None):
        self.inputLine = inputLine
        self.parseReturnCode = parseReturnCode
        self.errorLocation = errorLocation



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
                    self.inputLine = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.parseReturnCode = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.errorLocation = iprot.readI32()
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
        oprot.writeStructBegin('CmdExecutionResultsIDL')
        if self.inputLine != None:
            oprot.writeFieldBegin('inputLine', TType.STRING, 1)
            oprot.writeString(self.inputLine)
            oprot.writeFieldEnd()
        if self.parseReturnCode != None:
            oprot.writeFieldBegin('parseReturnCode', TType.I32, 2)
            oprot.writeI32(self.parseReturnCode)
            oprot.writeFieldEnd()
        if self.errorLocation != None:
            oprot.writeFieldBegin('errorLocation', TType.I32, 3)
            oprot.writeI32(self.errorLocation)
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




class ExecutionStateIDL(object):
    """
      Execution state structure
    
      Attributes:
       - prompt
       - overallReturnCode
       - cmdResults
      """

    thrift_spec = (None,
     (1,
      TType.STRING,
      'prompt',
      None,
      None),
     (2,
      TType.I32,
      'overallReturnCode',
      None,
      None),
     (3,
      TType.LIST,
      'cmdResults',
      (TType.STRUCT, (CmdExecutionResultsIDL, CmdExecutionResultsIDL.thrift_spec)),
      None))

    def __init__(self, prompt = None, overallReturnCode = None, cmdResults = None):
        self.prompt = prompt
        self.overallReturnCode = overallReturnCode
        self.cmdResults = cmdResults



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
                    self.prompt = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.overallReturnCode = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.LIST:
                    self.cmdResults = []
                    (_etype3, _size0,) = iprot.readListBegin()
                    for _i4 in xrange(_size0):
                        _elem5 = CmdExecutionResultsIDL()
                        _elem5.read(iprot)
                        self.cmdResults.append(_elem5)

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
        oprot.writeStructBegin('ExecutionStateIDL')
        if self.prompt != None:
            oprot.writeFieldBegin('prompt', TType.STRING, 1)
            oprot.writeString(self.prompt)
            oprot.writeFieldEnd()
        if self.overallReturnCode != None:
            oprot.writeFieldBegin('overallReturnCode', TType.I32, 2)
            oprot.writeI32(self.overallReturnCode)
            oprot.writeFieldEnd()
        if self.cmdResults != None:
            oprot.writeFieldBegin('cmdResults', TType.LIST, 3)
            oprot.writeListBegin(TType.STRUCT, len(self.cmdResults))
            for iter6 in self.cmdResults:
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




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:18:48 IST
