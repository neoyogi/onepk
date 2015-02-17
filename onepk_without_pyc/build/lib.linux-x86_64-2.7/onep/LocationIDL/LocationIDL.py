# 2015.02.05 17:18:41 IST
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

    def Location_getLocationIDL(self, handleType, handle):
        """
        Parameters:
         - handleType
         - handle
        """
        pass



    def Location_setLocationIDL(self, handleType, handle, loc):
        """
        Parameters:
         - handleType
         - handle
         - loc
        """
        pass



    def LocationChangeEvent_registerIDL(self, sessionID, handleType, handle, locationHandle, lofIDL):
        """
        Parameters:
         - sessionID
         - handleType
         - handle
         - locationHandle
         - lofIDL
        """
        pass




class Client(Iface):

    def __init__(self, iprot, oprot = None):
        self._iprot = self._oprot = iprot
        if oprot != None:
            self._oprot = oprot
        self._seqid = 0



    def Location_getLocationIDL(self, handleType, handle):
        """
        Parameters:
         - handleType
         - handle
        """
        self._oprot.rlock.acquire()
        try:
            self.send_Location_getLocationIDL(handleType, handle)
            result = self.recv_Location_getLocationIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_Location_getLocationIDL(self, handleType, handle):
        self._oprot.writeMessageBegin('Location_getLocationIDL', TMessageType.CALL, self._seqid)
        args = Location_getLocationIDL_args()
        args.handleType = handleType
        args.handle = handle
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_Location_getLocationIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = Location_getLocationIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'Location_getLocationIDL failed: unknown result')



    def Location_setLocationIDL(self, handleType, handle, loc):
        """
        Parameters:
         - handleType
         - handle
         - loc
        """
        self._oprot.rlock.acquire()
        try:
            self.send_Location_setLocationIDL(handleType, handle, loc)
            result = self.recv_Location_setLocationIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_Location_setLocationIDL(self, handleType, handle, loc):
        self._oprot.writeMessageBegin('Location_setLocationIDL', TMessageType.CALL, self._seqid)
        args = Location_setLocationIDL_args()
        args.handleType = handleType
        args.handle = handle
        args.loc = loc
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_Location_setLocationIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = Location_setLocationIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'Location_setLocationIDL failed: unknown result')



    def LocationChangeEvent_registerIDL(self, sessionID, handleType, handle, locationHandle, lofIDL):
        """
        Parameters:
         - sessionID
         - handleType
         - handle
         - locationHandle
         - lofIDL
        """
        self._oprot.rlock.acquire()
        try:
            self.send_LocationChangeEvent_registerIDL(sessionID, handleType, handle, locationHandle, lofIDL)
            result = self.recv_LocationChangeEvent_registerIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_LocationChangeEvent_registerIDL(self, sessionID, handleType, handle, locationHandle, lofIDL):
        self._oprot.writeMessageBegin('LocationChangeEvent_registerIDL', TMessageType.CALL, self._seqid)
        args = LocationChangeEvent_registerIDL_args()
        args.sessionID = sessionID
        args.handleType = handleType
        args.handle = handle
        args.locationHandle = locationHandle
        args.lofIDL = lofIDL
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_LocationChangeEvent_registerIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = LocationChangeEvent_registerIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'LocationChangeEvent_registerIDL failed: unknown result')




class Processor(Iface, TProcessor):

    def __init__(self, handler):
        self._handler = handler
        self._processMap = {}
        self._processMap['Location_getLocationIDL'] = Processor.process_Location_getLocationIDL
        self._processMap['Location_setLocationIDL'] = Processor.process_Location_setLocationIDL
        self._processMap['LocationChangeEvent_registerIDL'] = Processor.process_LocationChangeEvent_registerIDL



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



    def process_Location_getLocationIDL(self, seqid, iprot, oprot):
        args = Location_getLocationIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = Location_getLocationIDL_result()
        try:
            result.success = self._handler.Location_getLocationIDL(args.handleType, args.handle)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('Location_getLocationIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_Location_setLocationIDL(self, seqid, iprot, oprot):
        args = Location_setLocationIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = Location_setLocationIDL_result()
        try:
            result.success = self._handler.Location_setLocationIDL(args.handleType, args.handle, args.loc)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('Location_setLocationIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_LocationChangeEvent_registerIDL(self, seqid, iprot, oprot):
        args = LocationChangeEvent_registerIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = LocationChangeEvent_registerIDL_result()
        try:
            result.success = self._handler.LocationChangeEvent_registerIDL(args.sessionID, args.handleType, args.handle, args.locationHandle, args.lofIDL)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('LocationChangeEvent_registerIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()




class Location_getLocationIDL_args(object):
    """
    Attributes:
     - handleType
     - handle
    """

    thrift_spec = (None, (1,
      TType.I32,
      'handleType',
      None,
      None), (2,
      TType.I64,
      'handle',
      None,
      None))

    def __init__(self, handleType = None, handle = None):
        self.handleType = handleType
        self.handle = handle



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
                    self.handleType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.handle = iprot.readI64()
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
        oprot.writeStructBegin('Location_getLocationIDL_args')
        if self.handleType != None:
            oprot.writeFieldBegin('handleType', TType.I32, 1)
            oprot.writeI32(self.handleType)
            oprot.writeFieldEnd()
        if self.handle != None:
            oprot.writeFieldBegin('handle', TType.I64, 2)
            oprot.writeI64(self.handle)
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




class Location_getLocationIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.STRUCT,
      'success',
      (NetworkLocationIDL, NetworkLocationIDL.thrift_spec),
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
                    self.success = NetworkLocationIDL()
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
        oprot.writeStructBegin('Location_getLocationIDL_result')
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




class Location_setLocationIDL_args(object):
    """
    Attributes:
     - handleType
     - handle
     - loc
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'handleType',
      None,
      None),
     (2,
      TType.I64,
      'handle',
      None,
      None),
     (3,
      TType.STRUCT,
      'loc',
      (NetworkLocationIDL, NetworkLocationIDL.thrift_spec),
      None))

    def __init__(self, handleType = None, handle = None, loc = None):
        self.handleType = handleType
        self.handle = handle
        self.loc = loc



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
                    self.handleType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.handle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRUCT:
                    self.loc = NetworkLocationIDL()
                    self.loc.read(iprot)
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
        oprot.writeStructBegin('Location_setLocationIDL_args')
        if self.handleType != None:
            oprot.writeFieldBegin('handleType', TType.I32, 1)
            oprot.writeI32(self.handleType)
            oprot.writeFieldEnd()
        if self.handle != None:
            oprot.writeFieldBegin('handle', TType.I64, 2)
            oprot.writeI64(self.handle)
            oprot.writeFieldEnd()
        if self.loc != None:
            oprot.writeFieldBegin('loc', TType.STRUCT, 3)
            self.loc.write(oprot)
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




class Location_setLocationIDL_result(object):
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
        oprot.writeStructBegin('Location_setLocationIDL_result')
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




class LocationChangeEvent_registerIDL_args(object):
    """
    Attributes:
     - sessionID
     - handleType
     - handle
     - locationHandle
     - lofIDL
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionID',
      None,
      None),
     (2,
      TType.I32,
      'handleType',
      None,
      None),
     (3,
      TType.I64,
      'handle',
      None,
      None),
     (4,
      TType.I32,
      'locationHandle',
      None,
      None),
     (5,
      TType.STRUCT,
      'lofIDL',
      (LocationFilterIDL, LocationFilterIDL.thrift_spec),
      None))

    def __init__(self, sessionID = None, handleType = None, handle = None, locationHandle = None, lofIDL = None):
        self.sessionID = sessionID
        self.handleType = handleType
        self.handle = handle
        self.locationHandle = locationHandle
        self.lofIDL = lofIDL



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
                    self.handleType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I64:
                    self.handle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.locationHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRUCT:
                    self.lofIDL = LocationFilterIDL()
                    self.lofIDL.read(iprot)
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
        oprot.writeStructBegin('LocationChangeEvent_registerIDL_args')
        if self.sessionID != None:
            oprot.writeFieldBegin('sessionID', TType.I32, 1)
            oprot.writeI32(self.sessionID)
            oprot.writeFieldEnd()
        if self.handleType != None:
            oprot.writeFieldBegin('handleType', TType.I32, 2)
            oprot.writeI32(self.handleType)
            oprot.writeFieldEnd()
        if self.handle != None:
            oprot.writeFieldBegin('handle', TType.I64, 3)
            oprot.writeI64(self.handle)
            oprot.writeFieldEnd()
        if self.locationHandle != None:
            oprot.writeFieldBegin('locationHandle', TType.I32, 4)
            oprot.writeI32(self.locationHandle)
            oprot.writeFieldEnd()
        if self.lofIDL != None:
            oprot.writeFieldBegin('lofIDL', TType.STRUCT, 5)
            self.lofIDL.write(oprot)
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




class LocationChangeEvent_registerIDL_result(object):
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
        oprot.writeStructBegin('LocationChangeEvent_registerIDL_result')
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
# 2015.02.05 17:18:42 IST
