# 2015.02.05 17:19:59 IST
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

    def OnepEvent_ProbeStatsEventIDL(self, sessionHandle, eventHandle, stats):
        """
        Parameters:
         - sessionHandle
         - eventHandle
         - stats
        """
        pass




class Client(Iface):

    def __init__(self, iprot, oprot = None):
        self._iprot = self._oprot = iprot
        if oprot != None:
            self._oprot = oprot
        self._seqid = 0



    def OnepEvent_ProbeStatsEventIDL(self, sessionHandle, eventHandle, stats):
        """
        Parameters:
         - sessionHandle
         - eventHandle
         - stats
        """
        self._oprot.rlock.acquire()
        try:
            self.send_OnepEvent_ProbeStatsEventIDL(sessionHandle, eventHandle, stats)
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()



    def send_OnepEvent_ProbeStatsEventIDL(self, sessionHandle, eventHandle, stats):
        self._oprot.writeMessageBegin('OnepEvent_ProbeStatsEventIDL', TMessageType.CALL, self._seqid)
        args = OnepEvent_ProbeStatsEventIDL_args()
        args.sessionHandle = sessionHandle
        args.eventHandle = eventHandle
        args.stats = stats
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()




class Processor(Iface, TProcessor):

    def __init__(self, handler):
        self._handler = handler
        self._processMap = {}
        self._processMap['OnepEvent_ProbeStatsEventIDL'] = Processor.process_OnepEvent_ProbeStatsEventIDL



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



    def process_OnepEvent_ProbeStatsEventIDL(self, seqid, iprot, oprot):
        args = OnepEvent_ProbeStatsEventIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        self._handler.OnepEvent_ProbeStatsEventIDL(args.sessionHandle, args.eventHandle, args.stats)




class OnepEvent_ProbeStatsEventIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - eventHandle
     - stats
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
      'stats',
      (ProbeStatsOutIDL, ProbeStatsOutIDL.thrift_spec),
      None))

    def __init__(self, sessionHandle = None, eventHandle = None, stats = None):
        self.sessionHandle = sessionHandle
        self.eventHandle = eventHandle
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
                    self.stats = ProbeStatsOutIDL()
                    self.stats.read(iprot)
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
        oprot.writeStructBegin('OnepEvent_ProbeStatsEventIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.eventHandle != None:
            oprot.writeFieldBegin('eventHandle', TType.I32, 2)
            oprot.writeI32(self.eventHandle)
            oprot.writeFieldEnd()
        if self.stats != None:
            oprot.writeFieldBegin('stats', TType.STRUCT, 3)
            self.stats.write(oprot)
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
# 2015.02.05 17:20:00 IST
