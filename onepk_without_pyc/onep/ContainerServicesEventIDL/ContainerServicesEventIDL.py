# 2015.02.05 17:20:53 IST
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

    def OnepEvent_ContainerSrv_ext_send_guest_updateIDL(self, sessionHandle, eventtype, update_info):
        """
        Parameters:
         - sessionHandle
         - eventtype
         - update_info
        """
        pass



    def OnepEvent_ContainerSrv_ext_send_query_to_guestIDL(self, sessionHandle, transactionID, eventtype, query):
        """
        Parameters:
         - sessionHandle
         - transactionID
         - eventtype
         - query
        """
        pass




class Client(Iface):

    def __init__(self, iprot, oprot = None):
        self._iprot = self._oprot = iprot
        if oprot != None:
            self._oprot = oprot
        self._seqid = 0



    def OnepEvent_ContainerSrv_ext_send_guest_updateIDL(self, sessionHandle, eventtype, update_info):
        """
        Parameters:
         - sessionHandle
         - eventtype
         - update_info
        """
        self._oprot.rlock.acquire()
        try:
            self.send_OnepEvent_ContainerSrv_ext_send_guest_updateIDL(sessionHandle, eventtype, update_info)
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()



    def send_OnepEvent_ContainerSrv_ext_send_guest_updateIDL(self, sessionHandle, eventtype, update_info):
        self._oprot.writeMessageBegin('OnepEvent_ContainerSrv_ext_send_guest_updateIDL', TMessageType.CALL, self._seqid)
        args = OnepEvent_ContainerSrv_ext_send_guest_updateIDL_args()
        args.sessionHandle = sessionHandle
        args.eventtype = eventtype
        args.update_info = update_info
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def OnepEvent_ContainerSrv_ext_send_query_to_guestIDL(self, sessionHandle, transactionID, eventtype, query):
        """
        Parameters:
         - sessionHandle
         - transactionID
         - eventtype
         - query
        """
        self._oprot.rlock.acquire()
        try:
            self.send_OnepEvent_ContainerSrv_ext_send_query_to_guestIDL(sessionHandle, transactionID, eventtype, query)
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()



    def send_OnepEvent_ContainerSrv_ext_send_query_to_guestIDL(self, sessionHandle, transactionID, eventtype, query):
        self._oprot.writeMessageBegin('OnepEvent_ContainerSrv_ext_send_query_to_guestIDL', TMessageType.CALL, self._seqid)
        args = OnepEvent_ContainerSrv_ext_send_query_to_guestIDL_args()
        args.sessionHandle = sessionHandle
        args.transactionID = transactionID
        args.eventtype = eventtype
        args.query = query
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()




class Processor(Iface, TProcessor):

    def __init__(self, handler):
        self._handler = handler
        self._processMap = {}
        self._processMap['OnepEvent_ContainerSrv_ext_send_guest_updateIDL'] = Processor.process_OnepEvent_ContainerSrv_ext_send_guest_updateIDL
        self._processMap['OnepEvent_ContainerSrv_ext_send_query_to_guestIDL'] = Processor.process_OnepEvent_ContainerSrv_ext_send_query_to_guestIDL



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



    def process_OnepEvent_ContainerSrv_ext_send_guest_updateIDL(self, seqid, iprot, oprot):
        args = OnepEvent_ContainerSrv_ext_send_guest_updateIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        self._handler.OnepEvent_ContainerSrv_ext_send_guest_updateIDL(args.sessionHandle, args.eventtype, args.update_info)



    def process_OnepEvent_ContainerSrv_ext_send_query_to_guestIDL(self, seqid, iprot, oprot):
        args = OnepEvent_ContainerSrv_ext_send_query_to_guestIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        self._handler.OnepEvent_ContainerSrv_ext_send_query_to_guestIDL(args.sessionHandle, args.transactionID, args.eventtype, args.query)




class OnepEvent_ContainerSrv_ext_send_guest_updateIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - eventtype
     - update_info
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionHandle',
      None,
      None),
     (2,
      TType.I32,
      'eventtype',
      None,
      None),
     (3,
      TType.STRUCT,
      'update_info',
      (CS_ext_update_IDL, CS_ext_update_IDL.thrift_spec),
      None))

    def __init__(self, sessionHandle = None, eventtype = None, update_info = None):
        self.sessionHandle = sessionHandle
        self.eventtype = eventtype
        self.update_info = update_info



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
                    self.eventtype = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRUCT:
                    self.update_info = CS_ext_update_IDL()
                    self.update_info.read(iprot)
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
        oprot.writeStructBegin('OnepEvent_ContainerSrv_ext_send_guest_updateIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.eventtype != None:
            oprot.writeFieldBegin('eventtype', TType.I32, 2)
            oprot.writeI32(self.eventtype)
            oprot.writeFieldEnd()
        if self.update_info != None:
            oprot.writeFieldBegin('update_info', TType.STRUCT, 3)
            self.update_info.write(oprot)
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




class OnepEvent_ContainerSrv_ext_send_query_to_guestIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - transactionID
     - eventtype
     - query
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionHandle',
      None,
      None),
     (2,
      TType.I32,
      'transactionID',
      None,
      None),
     (3,
      TType.I32,
      'eventtype',
      None,
      None),
     (4,
      TType.STRUCT,
      'query',
      (CS_ext_query_IDL, CS_ext_query_IDL.thrift_spec),
      None))

    def __init__(self, sessionHandle = None, transactionID = None, eventtype = None, query = None):
        self.sessionHandle = sessionHandle
        self.transactionID = transactionID
        self.eventtype = eventtype
        self.query = query



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
                    self.transactionID = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.eventtype = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRUCT:
                    self.query = CS_ext_query_IDL()
                    self.query.read(iprot)
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
        oprot.writeStructBegin('OnepEvent_ContainerSrv_ext_send_query_to_guestIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.transactionID != None:
            oprot.writeFieldBegin('transactionID', TType.I32, 2)
            oprot.writeI32(self.transactionID)
            oprot.writeFieldEnd()
        if self.eventtype != None:
            oprot.writeFieldBegin('eventtype', TType.I32, 3)
            oprot.writeI32(self.eventtype)
            oprot.writeFieldEnd()
        if self.query != None:
            oprot.writeFieldBegin('query', TType.STRUCT, 4)
            self.query.write(oprot)
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
# 2015.02.05 17:20:54 IST
