# 2015.02.05 17:23:17 IST
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

    def NetworkElement_getEdgeListIDL(self, sessionHandle, config):
        """
        Parameters:
         - sessionHandle
         - config
        """
        pass



    def TopologyChange_Event_registerIDL(self, sessionHandle, TopologyKey, config):
        """
        Parameters:
         - sessionHandle
         - TopologyKey
         - config
        """
        pass




class Client(Iface):

    def __init__(self, iprot, oprot = None):
        self._iprot = self._oprot = iprot
        if oprot != None:
            self._oprot = oprot
        self._seqid = 0



    def NetworkElement_getEdgeListIDL(self, sessionHandle, config):
        """
        Parameters:
         - sessionHandle
         - config
        """
        self._oprot.rlock.acquire()
        try:
            self.send_NetworkElement_getEdgeListIDL(sessionHandle, config)
            result = self.recv_NetworkElement_getEdgeListIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_NetworkElement_getEdgeListIDL(self, sessionHandle, config):
        self._oprot.writeMessageBegin('NetworkElement_getEdgeListIDL', TMessageType.CALL, self._seqid)
        args = NetworkElement_getEdgeListIDL_args()
        args.sessionHandle = sessionHandle
        args.config = config
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_NetworkElement_getEdgeListIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = NetworkElement_getEdgeListIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'NetworkElement_getEdgeListIDL failed: unknown result')



    def TopologyChange_Event_registerIDL(self, sessionHandle, TopologyKey, config):
        """
        Parameters:
         - sessionHandle
         - TopologyKey
         - config
        """
        self._oprot.rlock.acquire()
        try:
            self.send_TopologyChange_Event_registerIDL(sessionHandle, TopologyKey, config)
            result = self.recv_TopologyChange_Event_registerIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_TopologyChange_Event_registerIDL(self, sessionHandle, TopologyKey, config):
        self._oprot.writeMessageBegin('TopologyChange_Event_registerIDL', TMessageType.CALL, self._seqid)
        args = TopologyChange_Event_registerIDL_args()
        args.sessionHandle = sessionHandle
        args.TopologyKey = TopologyKey
        args.config = config
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_TopologyChange_Event_registerIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = TopologyChange_Event_registerIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'TopologyChange_Event_registerIDL failed: unknown result')




class Processor(Iface, TProcessor):

    def __init__(self, handler):
        self._handler = handler
        self._processMap = {}
        self._processMap['NetworkElement_getEdgeListIDL'] = Processor.process_NetworkElement_getEdgeListIDL
        self._processMap['TopologyChange_Event_registerIDL'] = Processor.process_TopologyChange_Event_registerIDL



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



    def process_NetworkElement_getEdgeListIDL(self, seqid, iprot, oprot):
        args = NetworkElement_getEdgeListIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = NetworkElement_getEdgeListIDL_result()
        try:
            result.success = self._handler.NetworkElement_getEdgeListIDL(args.sessionHandle, args.config)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('NetworkElement_getEdgeListIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_TopologyChange_Event_registerIDL(self, seqid, iprot, oprot):
        args = TopologyChange_Event_registerIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = TopologyChange_Event_registerIDL_result()
        try:
            result.success = self._handler.TopologyChange_Event_registerIDL(args.sessionHandle, args.TopologyKey, args.config)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('TopologyChange_Event_registerIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()




class NetworkElement_getEdgeListIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - config
    """

    thrift_spec = (None, (1,
      TType.I32,
      'sessionHandle',
      None,
      None), (2,
      TType.STRUCT,
      'config',
      (TopologyConfigIDL, TopologyConfigIDL.thrift_spec),
      None))

    def __init__(self, sessionHandle = None, config = None):
        self.sessionHandle = sessionHandle
        self.config = config



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
                if ftype == TType.STRUCT:
                    self.config = TopologyConfigIDL()
                    self.config.read(iprot)
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
        oprot.writeStructBegin('NetworkElement_getEdgeListIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.config != None:
            oprot.writeFieldBegin('config', TType.STRUCT, 2)
            self.config.write(oprot)
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




class NetworkElement_getEdgeListIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.LIST,
      'success',
      (TType.STRUCT, (TopologyEdgeIDL, TopologyEdgeIDL.thrift_spec)),
      None), (1,
      TType.STRUCT,
      'e',
      (Shared.ttypes.ExceptionIDL, Shared.ttypes.ExceptionIDL.thrift_spec),
      None))

    def __init__(self, success = None, e = None):
        self.success = success
        self.e = e



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.LIST:
                    self.success = []
                    (_etype17, _size14,) = iprot.readListBegin()
                    for _i18 in xrange(_size14):
                        _elem19 = TopologyEdgeIDL()
                        _elem19.read(iprot)
                        self.success.append(_elem19)

                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = Shared.ttypes.ExceptionIDL()
                    self.e.read(iprot)
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
        oprot.writeStructBegin('NetworkElement_getEdgeListIDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.STRUCT, len(self.success))
            for iter20 in self.success:
                iter20.write(oprot)

            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.e != None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
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




class TopologyChange_Event_registerIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - TopologyKey
     - config
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionHandle',
      None,
      None),
     (2,
      TType.I32,
      'TopologyKey',
      None,
      None),
     (3,
      TType.STRUCT,
      'config',
      (TopologyConfigIDL, TopologyConfigIDL.thrift_spec),
      None))

    def __init__(self, sessionHandle = None, TopologyKey = None, config = None):
        self.sessionHandle = sessionHandle
        self.TopologyKey = TopologyKey
        self.config = config



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
                    self.TopologyKey = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRUCT:
                    self.config = TopologyConfigIDL()
                    self.config.read(iprot)
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
        oprot.writeStructBegin('TopologyChange_Event_registerIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.TopologyKey != None:
            oprot.writeFieldBegin('TopologyKey', TType.I32, 2)
            oprot.writeI32(self.TopologyKey)
            oprot.writeFieldEnd()
        if self.config != None:
            oprot.writeFieldBegin('config', TType.STRUCT, 3)
            self.config.write(oprot)
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




class TopologyChange_Event_registerIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.STRUCT,
      'success',
      (Shared.ttypes.EventHandleIDL, Shared.ttypes.EventHandleIDL.thrift_spec),
      None), (1,
      TType.STRUCT,
      'e',
      (Shared.ttypes.ExceptionIDL, Shared.ttypes.ExceptionIDL.thrift_spec),
      None))

    def __init__(self, success = None, e = None):
        self.success = success
        self.e = e



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = Shared.ttypes.EventHandleIDL()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = Shared.ttypes.ExceptionIDL()
                    self.e.read(iprot)
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
        oprot.writeStructBegin('TopologyChange_Event_registerIDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e != None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
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
# 2015.02.05 17:23:18 IST
