# 2015.02.05 17:20:36 IST
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

    def AdvancedRouting_Get_Protocol_List_IDL(self, filter):
        """
        Parameters:
         - filter
        """
        pass



    def AdvancedRouting_Get_Adjacency_List_IDL(self, protocol, filter):
        """
        Parameters:
         - protocol
         - filter
        """
        pass



    def AdvancedRouting_AdjacencyEvent_Register_IDL(self, pfilter, afilter):
        """
        Parameters:
         - pfilter
         - afilter
        """
        pass




class Client(Iface):

    def __init__(self, iprot, oprot = None):
        self._iprot = self._oprot = iprot
        if oprot != None:
            self._oprot = oprot
        self._seqid = 0



    def AdvancedRouting_Get_Protocol_List_IDL(self, filter):
        """
        Parameters:
         - filter
        """
        self._oprot.rlock.acquire()
        try:
            self.send_AdvancedRouting_Get_Protocol_List_IDL(filter)
            result = self.recv_AdvancedRouting_Get_Protocol_List_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_AdvancedRouting_Get_Protocol_List_IDL(self, filter):
        self._oprot.writeMessageBegin('AdvancedRouting_Get_Protocol_List_IDL', TMessageType.CALL, self._seqid)
        args = AdvancedRouting_Get_Protocol_List_IDL_args()
        args.filter = filter
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_AdvancedRouting_Get_Protocol_List_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = AdvancedRouting_Get_Protocol_List_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'AdvancedRouting_Get_Protocol_List_IDL failed: unknown result')



    def AdvancedRouting_Get_Adjacency_List_IDL(self, protocol, filter):
        """
        Parameters:
         - protocol
         - filter
        """
        self._oprot.rlock.acquire()
        try:
            self.send_AdvancedRouting_Get_Adjacency_List_IDL(protocol, filter)
            result = self.recv_AdvancedRouting_Get_Adjacency_List_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_AdvancedRouting_Get_Adjacency_List_IDL(self, protocol, filter):
        self._oprot.writeMessageBegin('AdvancedRouting_Get_Adjacency_List_IDL', TMessageType.CALL, self._seqid)
        args = AdvancedRouting_Get_Adjacency_List_IDL_args()
        args.protocol = protocol
        args.filter = filter
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_AdvancedRouting_Get_Adjacency_List_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = AdvancedRouting_Get_Adjacency_List_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'AdvancedRouting_Get_Adjacency_List_IDL failed: unknown result')



    def AdvancedRouting_AdjacencyEvent_Register_IDL(self, pfilter, afilter):
        """
        Parameters:
         - pfilter
         - afilter
        """
        self._oprot.rlock.acquire()
        try:
            self.send_AdvancedRouting_AdjacencyEvent_Register_IDL(pfilter, afilter)
            result = self.recv_AdvancedRouting_AdjacencyEvent_Register_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_AdvancedRouting_AdjacencyEvent_Register_IDL(self, pfilter, afilter):
        self._oprot.writeMessageBegin('AdvancedRouting_AdjacencyEvent_Register_IDL', TMessageType.CALL, self._seqid)
        args = AdvancedRouting_AdjacencyEvent_Register_IDL_args()
        args.pfilter = pfilter
        args.afilter = afilter
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_AdvancedRouting_AdjacencyEvent_Register_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = AdvancedRouting_AdjacencyEvent_Register_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'AdvancedRouting_AdjacencyEvent_Register_IDL failed: unknown result')




class Processor(Iface, TProcessor):

    def __init__(self, handler):
        self._handler = handler
        self._processMap = {}
        self._processMap['AdvancedRouting_Get_Protocol_List_IDL'] = Processor.process_AdvancedRouting_Get_Protocol_List_IDL
        self._processMap['AdvancedRouting_Get_Adjacency_List_IDL'] = Processor.process_AdvancedRouting_Get_Adjacency_List_IDL
        self._processMap['AdvancedRouting_AdjacencyEvent_Register_IDL'] = Processor.process_AdvancedRouting_AdjacencyEvent_Register_IDL



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



    def process_AdvancedRouting_Get_Protocol_List_IDL(self, seqid, iprot, oprot):
        args = AdvancedRouting_Get_Protocol_List_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = AdvancedRouting_Get_Protocol_List_IDL_result()
        try:
            result.success = self._handler.AdvancedRouting_Get_Protocol_List_IDL(args.filter)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('AdvancedRouting_Get_Protocol_List_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_AdvancedRouting_Get_Adjacency_List_IDL(self, seqid, iprot, oprot):
        args = AdvancedRouting_Get_Adjacency_List_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = AdvancedRouting_Get_Adjacency_List_IDL_result()
        try:
            result.success = self._handler.AdvancedRouting_Get_Adjacency_List_IDL(args.protocol, args.filter)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('AdvancedRouting_Get_Adjacency_List_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_AdvancedRouting_AdjacencyEvent_Register_IDL(self, seqid, iprot, oprot):
        args = AdvancedRouting_AdjacencyEvent_Register_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = AdvancedRouting_AdjacencyEvent_Register_IDL_result()
        try:
            result.success = self._handler.AdvancedRouting_AdjacencyEvent_Register_IDL(args.pfilter, args.afilter)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('AdvancedRouting_AdjacencyEvent_Register_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()




class AdvancedRouting_Get_Protocol_List_IDL_args(object):
    """
    Attributes:
     - filter
    """

    thrift_spec = (None, (1,
      TType.STRUCT,
      'filter',
      (RoutingProtocolFilterIDL, RoutingProtocolFilterIDL.thrift_spec),
      None))

    def __init__(self, filter = None):
        self.filter = filter



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
                    self.filter = RoutingProtocolFilterIDL()
                    self.filter.read(iprot)
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
        oprot.writeStructBegin('AdvancedRouting_Get_Protocol_List_IDL_args')
        if self.filter != None:
            oprot.writeFieldBegin('filter', TType.STRUCT, 1)
            self.filter.write(oprot)
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




class AdvancedRouting_Get_Protocol_List_IDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.LIST,
      'success',
      (TType.STRUCT, (RoutingProtocolIDL, RoutingProtocolIDL.thrift_spec)),
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
                    (_etype3, _size0,) = iprot.readListBegin()
                    for _i4 in xrange(_size0):
                        _elem5 = RoutingProtocolIDL()
                        _elem5.read(iprot)
                        self.success.append(_elem5)

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
        oprot.writeStructBegin('AdvancedRouting_Get_Protocol_List_IDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.STRUCT, len(self.success))
            for iter6 in self.success:
                iter6.write(oprot)

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




class AdvancedRouting_Get_Adjacency_List_IDL_args(object):
    """
    Attributes:
     - protocol
     - filter
    """

    thrift_spec = (None, (1,
      TType.STRUCT,
      'protocol',
      (RoutingProtocolIDL, RoutingProtocolIDL.thrift_spec),
      None), (2,
      TType.STRUCT,
      'filter',
      (RoutingAdjacencyFilterIDL, RoutingAdjacencyFilterIDL.thrift_spec),
      None))

    def __init__(self, protocol = None, filter = None):
        self.protocol = protocol
        self.filter = filter



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
                    self.protocol = RoutingProtocolIDL()
                    self.protocol.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.filter = RoutingAdjacencyFilterIDL()
                    self.filter.read(iprot)
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
        oprot.writeStructBegin('AdvancedRouting_Get_Adjacency_List_IDL_args')
        if self.protocol != None:
            oprot.writeFieldBegin('protocol', TType.STRUCT, 1)
            self.protocol.write(oprot)
            oprot.writeFieldEnd()
        if self.filter != None:
            oprot.writeFieldBegin('filter', TType.STRUCT, 2)
            self.filter.write(oprot)
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




class AdvancedRouting_Get_Adjacency_List_IDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.LIST,
      'success',
      (TType.STRUCT, (RoutingAdjacencyIDL, RoutingAdjacencyIDL.thrift_spec)),
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
                    (_etype10, _size7,) = iprot.readListBegin()
                    for _i11 in xrange(_size7):
                        _elem12 = RoutingAdjacencyIDL()
                        _elem12.read(iprot)
                        self.success.append(_elem12)

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
        oprot.writeStructBegin('AdvancedRouting_Get_Adjacency_List_IDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.STRUCT, len(self.success))
            for iter13 in self.success:
                iter13.write(oprot)

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




class AdvancedRouting_AdjacencyEvent_Register_IDL_args(object):
    """
    Attributes:
     - pfilter
     - afilter
    """

    thrift_spec = (None, (1,
      TType.STRUCT,
      'pfilter',
      (RoutingProtocolFilterIDL, RoutingProtocolFilterIDL.thrift_spec),
      None), (2,
      TType.STRUCT,
      'afilter',
      (RoutingAdjacencyFilterIDL, RoutingAdjacencyFilterIDL.thrift_spec),
      None))

    def __init__(self, pfilter = None, afilter = None):
        self.pfilter = pfilter
        self.afilter = afilter



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
                    self.pfilter = RoutingProtocolFilterIDL()
                    self.pfilter.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.afilter = RoutingAdjacencyFilterIDL()
                    self.afilter.read(iprot)
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
        oprot.writeStructBegin('AdvancedRouting_AdjacencyEvent_Register_IDL_args')
        if self.pfilter != None:
            oprot.writeFieldBegin('pfilter', TType.STRUCT, 1)
            self.pfilter.write(oprot)
            oprot.writeFieldEnd()
        if self.afilter != None:
            oprot.writeFieldBegin('afilter', TType.STRUCT, 2)
            self.afilter.write(oprot)
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




class AdvancedRouting_AdjacencyEvent_Register_IDL_result(object):
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
        oprot.writeStructBegin('AdvancedRouting_AdjacencyEvent_Register_IDL_result')
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
# 2015.02.05 17:20:37 IST
