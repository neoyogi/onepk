# 2015.02.05 17:19:38 IST
from thrift.Thrift import *
from ttypes import *
from thrift.Thrift import TProcessor
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
    from thrift.protocol import fastbinary
except:
    fastbinary = None

class Iface(object):

    def Policy_submitPmapBulkAsyncRspIDL(self, base, result, type, resList):
        """
        Parameters:
         - base
         - result
         - type
         - resList
        """
        pass



    def Policy_submitCmapBulkAsyncRspIDL(self, base, result, type, resList):
        """
        Parameters:
         - base
         - result
         - type
         - resList
        """
        pass



    def Policy_submitActivateBulkAsyncRspIDL(self, base, result, type, resList):
        """
        Parameters:
         - base
         - result
         - type
         - resList
        """
        pass



    def Policy_StatisticsEventIDL(self, sessionHandle, eventHandle, statsResult):
        """
        Parameters:
         - sessionHandle
         - eventHandle
         - statsResult
        """
        pass




class Client(Iface):

    def __init__(self, iprot, oprot = None):
        self._iprot = self._oprot = iprot
        if oprot != None:
            self._oprot = oprot
        self._seqid = 0



    def Policy_submitPmapBulkAsyncRspIDL(self, base, result, type, resList):
        """
        Parameters:
         - base
         - result
         - type
         - resList
        """
        self._oprot.rlock.acquire()
        try:
            self.send_Policy_submitPmapBulkAsyncRspIDL(base, result, type, resList)
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()



    def send_Policy_submitPmapBulkAsyncRspIDL(self, base, result, type, resList):
        self._oprot.writeMessageBegin('Policy_submitPmapBulkAsyncRspIDL', TMessageType.CALL, self._seqid)
        args = Policy_submitPmapBulkAsyncRspIDL_args()
        args.base = base
        args.result = result
        args.type = type
        args.resList = resList
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def Policy_submitCmapBulkAsyncRspIDL(self, base, result, type, resList):
        """
        Parameters:
         - base
         - result
         - type
         - resList
        """
        self._oprot.rlock.acquire()
        try:
            self.send_Policy_submitCmapBulkAsyncRspIDL(base, result, type, resList)
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()



    def send_Policy_submitCmapBulkAsyncRspIDL(self, base, result, type, resList):
        self._oprot.writeMessageBegin('Policy_submitCmapBulkAsyncRspIDL', TMessageType.CALL, self._seqid)
        args = Policy_submitCmapBulkAsyncRspIDL_args()
        args.base = base
        args.result = result
        args.type = type
        args.resList = resList
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def Policy_submitActivateBulkAsyncRspIDL(self, base, result, type, resList):
        """
        Parameters:
         - base
         - result
         - type
         - resList
        """
        self._oprot.rlock.acquire()
        try:
            self.send_Policy_submitActivateBulkAsyncRspIDL(base, result, type, resList)
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()



    def send_Policy_submitActivateBulkAsyncRspIDL(self, base, result, type, resList):
        self._oprot.writeMessageBegin('Policy_submitActivateBulkAsyncRspIDL', TMessageType.CALL, self._seqid)
        args = Policy_submitActivateBulkAsyncRspIDL_args()
        args.base = base
        args.result = result
        args.type = type
        args.resList = resList
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def Policy_StatisticsEventIDL(self, sessionHandle, eventHandle, statsResult):
        """
        Parameters:
         - sessionHandle
         - eventHandle
         - statsResult
        """
        self._oprot.rlock.acquire()
        try:
            self.send_Policy_StatisticsEventIDL(sessionHandle, eventHandle, statsResult)
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()



    def send_Policy_StatisticsEventIDL(self, sessionHandle, eventHandle, statsResult):
        self._oprot.writeMessageBegin('Policy_StatisticsEventIDL', TMessageType.CALL, self._seqid)
        args = Policy_StatisticsEventIDL_args()
        args.sessionHandle = sessionHandle
        args.eventHandle = eventHandle
        args.statsResult = statsResult
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()




class Processor(Iface, TProcessor):

    def __init__(self, handler):
        self._handler = handler
        self._processMap = {}
        self._processMap['Policy_submitPmapBulkAsyncRspIDL'] = Processor.process_Policy_submitPmapBulkAsyncRspIDL
        self._processMap['Policy_submitCmapBulkAsyncRspIDL'] = Processor.process_Policy_submitCmapBulkAsyncRspIDL
        self._processMap['Policy_submitActivateBulkAsyncRspIDL'] = Processor.process_Policy_submitActivateBulkAsyncRspIDL
        self._processMap['Policy_StatisticsEventIDL'] = Processor.process_Policy_StatisticsEventIDL



    def process(self, iprot, oprot):
        (name, type, seqid,) = iprot.readMessageBegin()
        if name not in self._processMap:
            iprot.skip(TType.STRUCT)
            iprot.readMessageEnd()
            x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % name)
            oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
            x.write(oprot)
            oprot.writeMessageEnd()
            oprot.trans.flush()
            return 
        self._processMap[name](self, seqid, iprot, oprot)
        return True



    def process_Policy_submitPmapBulkAsyncRspIDL(self, seqid, iprot, oprot):
        args = Policy_submitPmapBulkAsyncRspIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        self._handler.Policy_submitPmapBulkAsyncRspIDL(args.base, args.result, args.type, args.resList)



    def process_Policy_submitCmapBulkAsyncRspIDL(self, seqid, iprot, oprot):
        args = Policy_submitCmapBulkAsyncRspIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        self._handler.Policy_submitCmapBulkAsyncRspIDL(args.base, args.result, args.type, args.resList)



    def process_Policy_submitActivateBulkAsyncRspIDL(self, seqid, iprot, oprot):
        args = Policy_submitActivateBulkAsyncRspIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        self._handler.Policy_submitActivateBulkAsyncRspIDL(args.base, args.result, args.type, args.resList)



    def process_Policy_StatisticsEventIDL(self, seqid, iprot, oprot):
        args = Policy_StatisticsEventIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        self._handler.Policy_StatisticsEventIDL(args.sessionHandle, args.eventHandle, args.statsResult)




class Policy_submitPmapBulkAsyncRspIDL_args(object):
    """
    Attributes:
     - base
     - result
     - type
     - resList
    """

    thrift_spec = (None,
     (1,
      TType.STRUCT,
      'base',
      (AsyncMessageIDL.ttypes.AsyncBaseOutIDL, AsyncMessageIDL.ttypes.AsyncBaseOutIDL.thrift_spec),
      None),
     (2,
      TType.I32,
      'result',
      None,
      None),
     (3,
      TType.I32,
      'type',
      None,
      None),
     (4,
      TType.LIST,
      'resList',
      (TType.STRUCT, (PmapResultAsyncIDL, PmapResultAsyncIDL.thrift_spec)),
      None))

    def __init__(self, base = None, result = None, type = None, resList = None):
        self.base = base
        self.result = result
        self.type = type
        self.resList = resList



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
                    self.base = AsyncMessageIDL.ttypes.AsyncBaseOutIDL()
                    self.base.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.result = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.LIST:
                    self.resList = []
                    (_etype31, _size28,) = iprot.readListBegin()
                    for _i32 in xrange(_size28):
                        _elem33 = PmapResultAsyncIDL()
                        _elem33.read(iprot)
                        self.resList.append(_elem33)

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
        oprot.writeStructBegin('Policy_submitPmapBulkAsyncRspIDL_args')
        if self.base != None:
            oprot.writeFieldBegin('base', TType.STRUCT, 1)
            self.base.write(oprot)
            oprot.writeFieldEnd()
        if self.result != None:
            oprot.writeFieldBegin('result', TType.I32, 2)
            oprot.writeI32(self.result)
            oprot.writeFieldEnd()
        if self.type != None:
            oprot.writeFieldBegin('type', TType.I32, 3)
            oprot.writeI32(self.type)
            oprot.writeFieldEnd()
        if self.resList != None:
            oprot.writeFieldBegin('resList', TType.LIST, 4)
            oprot.writeListBegin(TType.STRUCT, len(self.resList))
            for iter34 in self.resList:
                iter34.write(oprot)

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




class Policy_submitCmapBulkAsyncRspIDL_args(object):
    """
    Attributes:
     - base
     - result
     - type
     - resList
    """

    thrift_spec = (None,
     (1,
      TType.STRUCT,
      'base',
      (AsyncMessageIDL.ttypes.AsyncBaseOutIDL, AsyncMessageIDL.ttypes.AsyncBaseOutIDL.thrift_spec),
      None),
     (2,
      TType.I32,
      'result',
      None,
      None),
     (3,
      TType.I32,
      'type',
      None,
      None),
     (4,
      TType.LIST,
      'resList',
      (TType.STRUCT, (CmapResultAsyncIDL, CmapResultAsyncIDL.thrift_spec)),
      None))

    def __init__(self, base = None, result = None, type = None, resList = None):
        self.base = base
        self.result = result
        self.type = type
        self.resList = resList



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
                    self.base = AsyncMessageIDL.ttypes.AsyncBaseOutIDL()
                    self.base.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.result = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.LIST:
                    self.resList = []
                    (_etype38, _size35,) = iprot.readListBegin()
                    for _i39 in xrange(_size35):
                        _elem40 = CmapResultAsyncIDL()
                        _elem40.read(iprot)
                        self.resList.append(_elem40)

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
        oprot.writeStructBegin('Policy_submitCmapBulkAsyncRspIDL_args')
        if self.base != None:
            oprot.writeFieldBegin('base', TType.STRUCT, 1)
            self.base.write(oprot)
            oprot.writeFieldEnd()
        if self.result != None:
            oprot.writeFieldBegin('result', TType.I32, 2)
            oprot.writeI32(self.result)
            oprot.writeFieldEnd()
        if self.type != None:
            oprot.writeFieldBegin('type', TType.I32, 3)
            oprot.writeI32(self.type)
            oprot.writeFieldEnd()
        if self.resList != None:
            oprot.writeFieldBegin('resList', TType.LIST, 4)
            oprot.writeListBegin(TType.STRUCT, len(self.resList))
            for iter41 in self.resList:
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




class Policy_submitActivateBulkAsyncRspIDL_args(object):
    """
    Attributes:
     - base
     - result
     - type
     - resList
    """

    thrift_spec = (None,
     (1,
      TType.STRUCT,
      'base',
      (AsyncMessageIDL.ttypes.AsyncBaseOutIDL, AsyncMessageIDL.ttypes.AsyncBaseOutIDL.thrift_spec),
      None),
     (2,
      TType.I32,
      'result',
      None,
      None),
     (3,
      TType.I32,
      'type',
      None,
      None),
     (4,
      TType.LIST,
      'resList',
      (TType.STRUCT, (PolicyCommonTypes.ttypes.PmapActivateResultIDL, PolicyCommonTypes.ttypes.PmapActivateResultIDL.thrift_spec)),
      None))

    def __init__(self, base = None, result = None, type = None, resList = None):
        self.base = base
        self.result = result
        self.type = type
        self.resList = resList



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
                    self.base = AsyncMessageIDL.ttypes.AsyncBaseOutIDL()
                    self.base.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.result = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.LIST:
                    self.resList = []
                    (_etype45, _size42,) = iprot.readListBegin()
                    for _i46 in xrange(_size42):
                        _elem47 = PolicyCommonTypes.ttypes.PmapActivateResultIDL()
                        _elem47.read(iprot)
                        self.resList.append(_elem47)

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
        oprot.writeStructBegin('Policy_submitActivateBulkAsyncRspIDL_args')
        if self.base != None:
            oprot.writeFieldBegin('base', TType.STRUCT, 1)
            self.base.write(oprot)
            oprot.writeFieldEnd()
        if self.result != None:
            oprot.writeFieldBegin('result', TType.I32, 2)
            oprot.writeI32(self.result)
            oprot.writeFieldEnd()
        if self.type != None:
            oprot.writeFieldBegin('type', TType.I32, 3)
            oprot.writeI32(self.type)
            oprot.writeFieldEnd()
        if self.resList != None:
            oprot.writeFieldBegin('resList', TType.LIST, 4)
            oprot.writeListBegin(TType.STRUCT, len(self.resList))
            for iter48 in self.resList:
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




class Policy_StatisticsEventIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - eventHandle
     - statsResult
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
      TType.STRUCT,
      'statsResult',
      (PolicyCommonTypes.ttypes.PolicyStatsResultIDL, PolicyCommonTypes.ttypes.PolicyStatsResultIDL.thrift_spec),
      None))

    def __init__(self, sessionHandle = None, eventHandle = None, statsResult = None):
        self.sessionHandle = sessionHandle
        self.eventHandle = eventHandle
        self.statsResult = statsResult



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
                if ftype == TType.STRUCT:
                    self.statsResult = PolicyCommonTypes.ttypes.PolicyStatsResultIDL()
                    self.statsResult.read(iprot)
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
        oprot.writeStructBegin('Policy_StatisticsEventIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.eventHandle != None:
            oprot.writeFieldBegin('eventHandle', TType.I32, 2)
            oprot.writeI32(self.eventHandle)
            oprot.writeFieldEnd()
        if self.statsResult != None:
            oprot.writeFieldBegin('statsResult', TType.STRUCT, 3)
            self.statsResult.write(oprot)
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
# 2015.02.05 17:19:39 IST
