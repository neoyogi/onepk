# 2015.02.05 17:21:34 IST
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

    def OnepEvent_locationChangeEventIDL(self, sessionID, eventHandle, subtype, changer, locationHandle):
        """
        Parameters:
         - sessionID
         - eventHandle
         - subtype
         - changer
         - locationHandle
        """
        pass




class Client(Iface):

    def __init__(self, iprot, oprot = None):
        self._iprot = self._oprot = iprot
        if oprot != None:
            self._oprot = oprot
        self._seqid = 0



    def OnepEvent_locationChangeEventIDL(self, sessionID, eventHandle, subtype, changer, locationHandle):
        """
        Parameters:
         - sessionID
         - eventHandle
         - subtype
         - changer
         - locationHandle
        """
        self._oprot.rlock.acquire()
        try:
            self.send_OnepEvent_locationChangeEventIDL(sessionID, eventHandle, subtype, changer, locationHandle)
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()



    def send_OnepEvent_locationChangeEventIDL(self, sessionID, eventHandle, subtype, changer, locationHandle):
        self._oprot.writeMessageBegin('OnepEvent_locationChangeEventIDL', TMessageType.CALL, self._seqid)
        args = OnepEvent_locationChangeEventIDL_args()
        args.sessionID = sessionID
        args.eventHandle = eventHandle
        args.subtype = subtype
        args.changer = changer
        args.locationHandle = locationHandle
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()




class Processor(Iface, TProcessor):

    def __init__(self, handler):
        self._handler = handler
        self._processMap = {}
        self._processMap['OnepEvent_locationChangeEventIDL'] = Processor.process_OnepEvent_locationChangeEventIDL



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



    def process_OnepEvent_locationChangeEventIDL(self, seqid, iprot, oprot):
        args = OnepEvent_locationChangeEventIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        self._handler.OnepEvent_locationChangeEventIDL(args.sessionID, args.eventHandle, args.subtype, args.changer, args.locationHandle)




class OnepEvent_locationChangeEventIDL_args(object):
    """
    Attributes:
     - sessionID
     - eventHandle
     - subtype
     - changer
     - locationHandle
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
      'subtype',
      None,
      None),
     (4,
      TType.I32,
      'changer',
      None,
      None),
     (5,
      TType.I32,
      'locationHandle',
      None,
      None))

    def __init__(self, sessionID = None, eventHandle = None, subtype = None, changer = None, locationHandle = None):
        self.sessionID = sessionID
        self.eventHandle = eventHandle
        self.subtype = subtype
        self.changer = changer
        self.locationHandle = locationHandle



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
                    self.subtype = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.changer = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.locationHandle = iprot.readI32()
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
        oprot.writeStructBegin('OnepEvent_locationChangeEventIDL_args')
        if self.sessionID != None:
            oprot.writeFieldBegin('sessionID', TType.I32, 1)
            oprot.writeI32(self.sessionID)
            oprot.writeFieldEnd()
        if self.eventHandle != None:
            oprot.writeFieldBegin('eventHandle', TType.I32, 2)
            oprot.writeI32(self.eventHandle)
            oprot.writeFieldEnd()
        if self.subtype != None:
            oprot.writeFieldBegin('subtype', TType.I32, 3)
            oprot.writeI32(self.subtype)
            oprot.writeFieldEnd()
        if self.changer != None:
            oprot.writeFieldBegin('changer', TType.I32, 4)
            oprot.writeI32(self.changer)
            oprot.writeFieldEnd()
        if self.locationHandle != None:
            oprot.writeFieldBegin('locationHandle', TType.I32, 5)
            oprot.writeI32(self.locationHandle)
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
# 2015.02.05 17:21:35 IST
