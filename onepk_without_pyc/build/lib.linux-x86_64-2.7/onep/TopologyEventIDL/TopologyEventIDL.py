# 2015.02.05 17:20:24 IST
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

    def OnepEvent_TopologyChangeEventIDL(self, sessionID, eventHandle, TopologyKey, eventType, outconfig, edgeIDL_list):
        """
        Parameters:
         - sessionID
         - eventHandle
         - TopologyKey
         - eventType
         - outconfig
         - edgeIDL_list
        """
        pass




class Client(Iface):

    def __init__(self, iprot, oprot = None):
        self._iprot = self._oprot = iprot
        if oprot != None:
            self._oprot = oprot
        self._seqid = 0



    def OnepEvent_TopologyChangeEventIDL(self, sessionID, eventHandle, TopologyKey, eventType, outconfig, edgeIDL_list):
        """
        Parameters:
         - sessionID
         - eventHandle
         - TopologyKey
         - eventType
         - outconfig
         - edgeIDL_list
        """
        self._oprot.rlock.acquire()
        try:
            self.send_OnepEvent_TopologyChangeEventIDL(sessionID, eventHandle, TopologyKey, eventType, outconfig, edgeIDL_list)
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()



    def send_OnepEvent_TopologyChangeEventIDL(self, sessionID, eventHandle, TopologyKey, eventType, outconfig, edgeIDL_list):
        self._oprot.writeMessageBegin('OnepEvent_TopologyChangeEventIDL', TMessageType.CALL, self._seqid)
        args = OnepEvent_TopologyChangeEventIDL_args()
        args.sessionID = sessionID
        args.eventHandle = eventHandle
        args.TopologyKey = TopologyKey
        args.eventType = eventType
        args.outconfig = outconfig
        args.edgeIDL_list = edgeIDL_list
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()




class Processor(Iface, TProcessor):

    def __init__(self, handler):
        self._handler = handler
        self._processMap = {}
        self._processMap['OnepEvent_TopologyChangeEventIDL'] = Processor.process_OnepEvent_TopologyChangeEventIDL



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



    def process_OnepEvent_TopologyChangeEventIDL(self, seqid, iprot, oprot):
        args = OnepEvent_TopologyChangeEventIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        self._handler.OnepEvent_TopologyChangeEventIDL(args.sessionID, args.eventHandle, args.TopologyKey, args.eventType, args.outconfig, args.edgeIDL_list)




class OnepEvent_TopologyChangeEventIDL_args(object):
    """
    Attributes:
     - sessionID
     - eventHandle
     - TopologyKey
     - eventType
     - outconfig
     - edgeIDL_list
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionID',
      None,
      None),
     (2,
      TType.I32,
      'eventHandle',
      None,
      None),
     (3,
      TType.I32,
      'TopologyKey',
      None,
      None),
     (4,
      TType.I32,
      'eventType',
      None,
      None),
     (5,
      TType.STRUCT,
      'outconfig',
      (TopologyConfigOutIDL, TopologyConfigOutIDL.thrift_spec),
      None),
     (6,
      TType.LIST,
      'edgeIDL_list',
      (TType.STRUCT, (TopologyEdgeOutIDL, TopologyEdgeOutIDL.thrift_spec)),
      None))

    def __init__(self, sessionID = None, eventHandle = None, TopologyKey = None, eventType = None, outconfig = None, edgeIDL_list = None):
        self.sessionID = sessionID
        self.eventHandle = eventHandle
        self.TopologyKey = TopologyKey
        self.eventType = eventType
        self.outconfig = outconfig
        self.edgeIDL_list = edgeIDL_list



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
                    self.sessionID = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.eventHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.TopologyKey = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.eventType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRUCT:
                    self.outconfig = TopologyConfigOutIDL()
                    self.outconfig.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.LIST:
                    self.edgeIDL_list = []
                    (_etype17, _size14,) = iprot.readListBegin()
                    for _i18 in xrange(_size14):
                        _elem19 = TopologyEdgeOutIDL()
                        _elem19.read(iprot)
                        self.edgeIDL_list.append(_elem19)

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
        oprot.writeStructBegin('OnepEvent_TopologyChangeEventIDL_args')
        if self.sessionID != None:
            oprot.writeFieldBegin('sessionID', TType.I32, 1)
            oprot.writeI32(self.sessionID)
            oprot.writeFieldEnd()
        if self.eventHandle != None:
            oprot.writeFieldBegin('eventHandle', TType.I32, 2)
            oprot.writeI32(self.eventHandle)
            oprot.writeFieldEnd()
        if self.TopologyKey != None:
            oprot.writeFieldBegin('TopologyKey', TType.I32, 3)
            oprot.writeI32(self.TopologyKey)
            oprot.writeFieldEnd()
        if self.eventType != None:
            oprot.writeFieldBegin('eventType', TType.I32, 4)
            oprot.writeI32(self.eventType)
            oprot.writeFieldEnd()
        if self.outconfig != None:
            oprot.writeFieldBegin('outconfig', TType.STRUCT, 5)
            self.outconfig.write(oprot)
            oprot.writeFieldEnd()
        if self.edgeIDL_list != None:
            oprot.writeFieldBegin('edgeIDL_list', TType.LIST, 6)
            oprot.writeListBegin(TType.STRUCT, len(self.edgeIDL_list))
            for iter20 in self.edgeIDL_list:
                iter20.write(oprot)

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
# 2015.02.05 17:20:25 IST
