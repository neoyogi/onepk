# 2015.02.05 17:18:09 IST
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

    def DPSS_setupIDL(self, sessionHandle, transport_type, transport_address, onep_sender_id):
        """
            API to CEF in NE to setup the transport of sending
            unsolicited packets to the NE from DPSS.
        
            Parameters:
             - sessionHandle
             - transport_type
             - transport_address
             - onep_sender_id
            """
        pass



    def DPSS_teardownIDL(self, sessionHandle, onep_sender_id, elem_sender_id):
        """
            API to CEF in NE to setup the transport of sending
            unsolicited packets to the NE from DPSS.
        
            Parameters:
             - sessionHandle
             - onep_sender_id
             - elem_sender_id
            """
        pass




class Client(Iface):

    def __init__(self, iprot, oprot = None):
        self._iprot = self._oprot = iprot
        if oprot != None:
            self._oprot = oprot
        self._seqid = 0



    def DPSS_setupIDL(self, sessionHandle, transport_type, transport_address, onep_sender_id):
        """
            API to CEF in NE to setup the transport of sending
            unsolicited packets to the NE from DPSS.
        
            Parameters:
             - sessionHandle
             - transport_type
             - transport_address
             - onep_sender_id
            """
        self._oprot.rlock.acquire()
        try:
            self.send_DPSS_setupIDL(sessionHandle, transport_type, transport_address, onep_sender_id)
            result = self.recv_DPSS_setupIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_DPSS_setupIDL(self, sessionHandle, transport_type, transport_address, onep_sender_id):
        self._oprot.writeMessageBegin('DPSS_setupIDL', TMessageType.CALL, self._seqid)
        args = DPSS_setupIDL_args()
        args.sessionHandle = sessionHandle
        args.transport_type = transport_type
        args.transport_address = transport_address
        args.onep_sender_id = onep_sender_id
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_DPSS_setupIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = DPSS_setupIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'DPSS_setupIDL failed: unknown result')



    def DPSS_teardownIDL(self, sessionHandle, onep_sender_id, elem_sender_id):
        """
            API to CEF in NE to setup the transport of sending
            unsolicited packets to the NE from DPSS.
        
            Parameters:
             - sessionHandle
             - onep_sender_id
             - elem_sender_id
            """
        self._oprot.rlock.acquire()
        try:
            self.send_DPSS_teardownIDL(sessionHandle, onep_sender_id, elem_sender_id)
            result = self.recv_DPSS_teardownIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_DPSS_teardownIDL(self, sessionHandle, onep_sender_id, elem_sender_id):
        self._oprot.writeMessageBegin('DPSS_teardownIDL', TMessageType.CALL, self._seqid)
        args = DPSS_teardownIDL_args()
        args.sessionHandle = sessionHandle
        args.onep_sender_id = onep_sender_id
        args.elem_sender_id = elem_sender_id
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_DPSS_teardownIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = DPSS_teardownIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'DPSS_teardownIDL failed: unknown result')




class Processor(Iface, TProcessor):

    def __init__(self, handler):
        self._handler = handler
        self._processMap = {}
        self._processMap['DPSS_setupIDL'] = Processor.process_DPSS_setupIDL
        self._processMap['DPSS_teardownIDL'] = Processor.process_DPSS_teardownIDL



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



    def process_DPSS_setupIDL(self, seqid, iprot, oprot):
        args = DPSS_setupIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = DPSS_setupIDL_result()
        try:
            result.success = self._handler.DPSS_setupIDL(args.sessionHandle, args.transport_type, args.transport_address, args.onep_sender_id)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('DPSS_setupIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_DPSS_teardownIDL(self, seqid, iprot, oprot):
        args = DPSS_teardownIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = DPSS_teardownIDL_result()
        try:
            result.success = self._handler.DPSS_teardownIDL(args.sessionHandle, args.onep_sender_id, args.elem_sender_id)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('DPSS_teardownIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()




class DPSS_setupIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - transport_type
     - transport_address
     - onep_sender_id
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionHandle',
      None,
      None),
     (2,
      TType.STRING,
      'transport_type',
      None,
      None),
     (3,
      TType.STRING,
      'transport_address',
      None,
      None),
     (4,
      TType.I32,
      'onep_sender_id',
      None,
      None))

    def __init__(self, sessionHandle = None, transport_type = None, transport_address = None, onep_sender_id = None):
        self.sessionHandle = sessionHandle
        self.transport_type = transport_type
        self.transport_address = transport_address
        self.onep_sender_id = onep_sender_id



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
                if ftype == TType.STRING:
                    self.transport_type = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.transport_address = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.onep_sender_id = iprot.readI32()
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
        oprot.writeStructBegin('DPSS_setupIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.transport_type != None:
            oprot.writeFieldBegin('transport_type', TType.STRING, 2)
            oprot.writeString(self.transport_type)
            oprot.writeFieldEnd()
        if self.transport_address != None:
            oprot.writeFieldBegin('transport_address', TType.STRING, 3)
            oprot.writeString(self.transport_address)
            oprot.writeFieldEnd()
        if self.onep_sender_id != None:
            oprot.writeFieldBegin('onep_sender_id', TType.I32, 4)
            oprot.writeI32(self.onep_sender_id)
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




class DPSS_setupIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.STRUCT,
      'success',
      (onep_element_provisioning_params_t, onep_element_provisioning_params_t.thrift_spec),
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
                    self.success = onep_element_provisioning_params_t()
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
        oprot.writeStructBegin('DPSS_setupIDL_result')
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




class DPSS_teardownIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - onep_sender_id
     - elem_sender_id
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionHandle',
      None,
      None),
     (2,
      TType.I32,
      'onep_sender_id',
      None,
      None),
     (3,
      TType.I32,
      'elem_sender_id',
      None,
      None))

    def __init__(self, sessionHandle = None, onep_sender_id = None, elem_sender_id = None):
        self.sessionHandle = sessionHandle
        self.onep_sender_id = onep_sender_id
        self.elem_sender_id = elem_sender_id



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
                    self.onep_sender_id = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.elem_sender_id = iprot.readI32()
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
        oprot.writeStructBegin('DPSS_teardownIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.onep_sender_id != None:
            oprot.writeFieldBegin('onep_sender_id', TType.I32, 2)
            oprot.writeI32(self.onep_sender_id)
            oprot.writeFieldEnd()
        if self.elem_sender_id != None:
            oprot.writeFieldBegin('elem_sender_id', TType.I32, 3)
            oprot.writeI32(self.elem_sender_id)
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




class DPSS_teardownIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.I32,
      'success',
      None,
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
                if ftype == TType.I32:
                    self.success = iprot.readI32()
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
        oprot.writeStructBegin('DPSS_teardownIDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.I32, 0)
            oprot.writeI32(self.success)
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
# 2015.02.05 17:18:09 IST
