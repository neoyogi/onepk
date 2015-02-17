# 2015.02.05 17:23:05 IST
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

    def Sanet_Find_By_Attributes_With_Reqd_List_IDL(self, sessionhandle, attr_list, reqd_attr_list):
        """
        Parameters:
         - sessionhandle
         - attr_list
         - reqd_attr_list
        """
        pass



    def Sanet_Find_By_Attributes_IDL(self, sessionhandle, attr_list):
        """
        Parameters:
         - sessionhandle
         - attr_list
        """
        pass



    def Sanet_Get_Attributes_IDL(self, sessionHandle, sessionNum, reqd_attr_list):
        """
        Parameters:
         - sessionHandle
         - sessionNum
         - reqd_attr_list
        """
        pass



    def Sanet_Set_Attributes_IDL(self, sessionHandle, sessionNum, attr_list, isUpdate):
        """
        Parameters:
         - sessionHandle
         - sessionNum
         - attr_list
         - isUpdate
        """
        pass



    def Sanet_Delete_Session_By_Attrs_IDL(self, sessionHandle, attr_list, isMulti):
        """
        Parameters:
         - sessionHandle
         - attr_list
         - isMulti
        """
        pass



    def Sanet_Delete_Session_IDL(self, sessionHandle, sessionNum):
        """
        Parameters:
         - sessionHandle
         - sessionNum
        """
        pass




class Client(Iface):

    def __init__(self, iprot, oprot = None):
        self._iprot = self._oprot = iprot
        if oprot != None:
            self._oprot = oprot
        self._seqid = 0



    def Sanet_Find_By_Attributes_With_Reqd_List_IDL(self, sessionhandle, attr_list, reqd_attr_list):
        """
        Parameters:
         - sessionhandle
         - attr_list
         - reqd_attr_list
        """
        self._oprot.rlock.acquire()
        try:
            self.send_Sanet_Find_By_Attributes_With_Reqd_List_IDL(sessionhandle, attr_list, reqd_attr_list)
            result = self.recv_Sanet_Find_By_Attributes_With_Reqd_List_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_Sanet_Find_By_Attributes_With_Reqd_List_IDL(self, sessionhandle, attr_list, reqd_attr_list):
        self._oprot.writeMessageBegin('Sanet_Find_By_Attributes_With_Reqd_List_IDL', TMessageType.CALL, self._seqid)
        args = Sanet_Find_By_Attributes_With_Reqd_List_IDL_args()
        args.sessionhandle = sessionhandle
        args.attr_list = attr_list
        args.reqd_attr_list = reqd_attr_list
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_Sanet_Find_By_Attributes_With_Reqd_List_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = Sanet_Find_By_Attributes_With_Reqd_List_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'Sanet_Find_By_Attributes_With_Reqd_List_IDL failed: unknown result')



    def Sanet_Find_By_Attributes_IDL(self, sessionhandle, attr_list):
        """
        Parameters:
         - sessionhandle
         - attr_list
        """
        self._oprot.rlock.acquire()
        try:
            self.send_Sanet_Find_By_Attributes_IDL(sessionhandle, attr_list)
            result = self.recv_Sanet_Find_By_Attributes_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_Sanet_Find_By_Attributes_IDL(self, sessionhandle, attr_list):
        self._oprot.writeMessageBegin('Sanet_Find_By_Attributes_IDL', TMessageType.CALL, self._seqid)
        args = Sanet_Find_By_Attributes_IDL_args()
        args.sessionhandle = sessionhandle
        args.attr_list = attr_list
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_Sanet_Find_By_Attributes_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = Sanet_Find_By_Attributes_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'Sanet_Find_By_Attributes_IDL failed: unknown result')



    def Sanet_Get_Attributes_IDL(self, sessionHandle, sessionNum, reqd_attr_list):
        """
        Parameters:
         - sessionHandle
         - sessionNum
         - reqd_attr_list
        """
        self._oprot.rlock.acquire()
        try:
            self.send_Sanet_Get_Attributes_IDL(sessionHandle, sessionNum, reqd_attr_list)
            result = self.recv_Sanet_Get_Attributes_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_Sanet_Get_Attributes_IDL(self, sessionHandle, sessionNum, reqd_attr_list):
        self._oprot.writeMessageBegin('Sanet_Get_Attributes_IDL', TMessageType.CALL, self._seqid)
        args = Sanet_Get_Attributes_IDL_args()
        args.sessionHandle = sessionHandle
        args.sessionNum = sessionNum
        args.reqd_attr_list = reqd_attr_list
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_Sanet_Get_Attributes_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = Sanet_Get_Attributes_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'Sanet_Get_Attributes_IDL failed: unknown result')



    def Sanet_Set_Attributes_IDL(self, sessionHandle, sessionNum, attr_list, isUpdate):
        """
        Parameters:
         - sessionHandle
         - sessionNum
         - attr_list
         - isUpdate
        """
        self._oprot.rlock.acquire()
        try:
            self.send_Sanet_Set_Attributes_IDL(sessionHandle, sessionNum, attr_list, isUpdate)
            result = self.recv_Sanet_Set_Attributes_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_Sanet_Set_Attributes_IDL(self, sessionHandle, sessionNum, attr_list, isUpdate):
        self._oprot.writeMessageBegin('Sanet_Set_Attributes_IDL', TMessageType.CALL, self._seqid)
        args = Sanet_Set_Attributes_IDL_args()
        args.sessionHandle = sessionHandle
        args.sessionNum = sessionNum
        args.attr_list = attr_list
        args.isUpdate = isUpdate
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_Sanet_Set_Attributes_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = Sanet_Set_Attributes_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'Sanet_Set_Attributes_IDL failed: unknown result')



    def Sanet_Delete_Session_By_Attrs_IDL(self, sessionHandle, attr_list, isMulti):
        """
        Parameters:
         - sessionHandle
         - attr_list
         - isMulti
        """
        self._oprot.rlock.acquire()
        try:
            self.send_Sanet_Delete_Session_By_Attrs_IDL(sessionHandle, attr_list, isMulti)
            result = self.recv_Sanet_Delete_Session_By_Attrs_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_Sanet_Delete_Session_By_Attrs_IDL(self, sessionHandle, attr_list, isMulti):
        self._oprot.writeMessageBegin('Sanet_Delete_Session_By_Attrs_IDL', TMessageType.CALL, self._seqid)
        args = Sanet_Delete_Session_By_Attrs_IDL_args()
        args.sessionHandle = sessionHandle
        args.attr_list = attr_list
        args.isMulti = isMulti
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_Sanet_Delete_Session_By_Attrs_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = Sanet_Delete_Session_By_Attrs_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'Sanet_Delete_Session_By_Attrs_IDL failed: unknown result')



    def Sanet_Delete_Session_IDL(self, sessionHandle, sessionNum):
        """
        Parameters:
         - sessionHandle
         - sessionNum
        """
        self._oprot.rlock.acquire()
        try:
            self.send_Sanet_Delete_Session_IDL(sessionHandle, sessionNum)
            result = self.recv_Sanet_Delete_Session_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_Sanet_Delete_Session_IDL(self, sessionHandle, sessionNum):
        self._oprot.writeMessageBegin('Sanet_Delete_Session_IDL', TMessageType.CALL, self._seqid)
        args = Sanet_Delete_Session_IDL_args()
        args.sessionHandle = sessionHandle
        args.sessionNum = sessionNum
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_Sanet_Delete_Session_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = Sanet_Delete_Session_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'Sanet_Delete_Session_IDL failed: unknown result')




class Processor(Iface, TProcessor):

    def __init__(self, handler):
        self._handler = handler
        self._processMap = {}
        self._processMap['Sanet_Find_By_Attributes_With_Reqd_List_IDL'] = Processor.process_Sanet_Find_By_Attributes_With_Reqd_List_IDL
        self._processMap['Sanet_Find_By_Attributes_IDL'] = Processor.process_Sanet_Find_By_Attributes_IDL
        self._processMap['Sanet_Get_Attributes_IDL'] = Processor.process_Sanet_Get_Attributes_IDL
        self._processMap['Sanet_Set_Attributes_IDL'] = Processor.process_Sanet_Set_Attributes_IDL
        self._processMap['Sanet_Delete_Session_By_Attrs_IDL'] = Processor.process_Sanet_Delete_Session_By_Attrs_IDL
        self._processMap['Sanet_Delete_Session_IDL'] = Processor.process_Sanet_Delete_Session_IDL



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



    def process_Sanet_Find_By_Attributes_With_Reqd_List_IDL(self, seqid, iprot, oprot):
        args = Sanet_Find_By_Attributes_With_Reqd_List_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = Sanet_Find_By_Attributes_With_Reqd_List_IDL_result()
        try:
            result.success = self._handler.Sanet_Find_By_Attributes_With_Reqd_List_IDL(args.sessionhandle, args.attr_list, args.reqd_attr_list)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('Sanet_Find_By_Attributes_With_Reqd_List_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_Sanet_Find_By_Attributes_IDL(self, seqid, iprot, oprot):
        args = Sanet_Find_By_Attributes_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = Sanet_Find_By_Attributes_IDL_result()
        try:
            result.success = self._handler.Sanet_Find_By_Attributes_IDL(args.sessionhandle, args.attr_list)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('Sanet_Find_By_Attributes_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_Sanet_Get_Attributes_IDL(self, seqid, iprot, oprot):
        args = Sanet_Get_Attributes_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = Sanet_Get_Attributes_IDL_result()
        try:
            result.success = self._handler.Sanet_Get_Attributes_IDL(args.sessionHandle, args.sessionNum, args.reqd_attr_list)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('Sanet_Get_Attributes_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_Sanet_Set_Attributes_IDL(self, seqid, iprot, oprot):
        args = Sanet_Set_Attributes_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = Sanet_Set_Attributes_IDL_result()
        try:
            result.success = self._handler.Sanet_Set_Attributes_IDL(args.sessionHandle, args.sessionNum, args.attr_list, args.isUpdate)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('Sanet_Set_Attributes_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_Sanet_Delete_Session_By_Attrs_IDL(self, seqid, iprot, oprot):
        args = Sanet_Delete_Session_By_Attrs_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = Sanet_Delete_Session_By_Attrs_IDL_result()
        try:
            result.success = self._handler.Sanet_Delete_Session_By_Attrs_IDL(args.sessionHandle, args.attr_list, args.isMulti)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('Sanet_Delete_Session_By_Attrs_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_Sanet_Delete_Session_IDL(self, seqid, iprot, oprot):
        args = Sanet_Delete_Session_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = Sanet_Delete_Session_IDL_result()
        try:
            result.success = self._handler.Sanet_Delete_Session_IDL(args.sessionHandle, args.sessionNum)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('Sanet_Delete_Session_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()




class Sanet_Find_By_Attributes_With_Reqd_List_IDL_args(object):
    """
    Attributes:
     - sessionhandle
     - attr_list
     - reqd_attr_list
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionhandle',
      None,
      None),
     (2,
      TType.LIST,
      'attr_list',
      (TType.STRUCT, (AaaIDL.ttypes.Attribute_IDL, AaaIDL.ttypes.Attribute_IDL.thrift_spec)),
      None),
     (3,
      TType.LIST,
      'reqd_attr_list',
      (TType.STRUCT, (AaaIDL.ttypes.Attribute_IDL, AaaIDL.ttypes.Attribute_IDL.thrift_spec)),
      None))

    def __init__(self, sessionhandle = None, attr_list = None, reqd_attr_list = None):
        self.sessionhandle = sessionhandle
        self.attr_list = attr_list
        self.reqd_attr_list = reqd_attr_list



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
                    self.sessionhandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.attr_list = []
                    (_etype10, _size7,) = iprot.readListBegin()
                    for _i11 in xrange(_size7):
                        _elem12 = AaaIDL.ttypes.Attribute_IDL()
                        _elem12.read(iprot)
                        self.attr_list.append(_elem12)

                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.LIST:
                    self.reqd_attr_list = []
                    (_etype16, _size13,) = iprot.readListBegin()
                    for _i17 in xrange(_size13):
                        _elem18 = AaaIDL.ttypes.Attribute_IDL()
                        _elem18.read(iprot)
                        self.reqd_attr_list.append(_elem18)

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
        oprot.writeStructBegin('Sanet_Find_By_Attributes_With_Reqd_List_IDL_args')
        if self.sessionhandle != None:
            oprot.writeFieldBegin('sessionhandle', TType.I32, 1)
            oprot.writeI32(self.sessionhandle)
            oprot.writeFieldEnd()
        if self.attr_list != None:
            oprot.writeFieldBegin('attr_list', TType.LIST, 2)
            oprot.writeListBegin(TType.STRUCT, len(self.attr_list))
            for iter19 in self.attr_list:
                iter19.write(oprot)

            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.reqd_attr_list != None:
            oprot.writeFieldBegin('reqd_attr_list', TType.LIST, 3)
            oprot.writeListBegin(TType.STRUCT, len(self.reqd_attr_list))
            for iter20 in self.reqd_attr_list:
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




class Sanet_Find_By_Attributes_With_Reqd_List_IDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.LIST,
      'success',
      (TType.STRUCT, (SanetSessionListIDL, SanetSessionListIDL.thrift_spec)),
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
                    (_etype24, _size21,) = iprot.readListBegin()
                    for _i25 in xrange(_size21):
                        _elem26 = SanetSessionListIDL()
                        _elem26.read(iprot)
                        self.success.append(_elem26)

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
        oprot.writeStructBegin('Sanet_Find_By_Attributes_With_Reqd_List_IDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.STRUCT, len(self.success))
            for iter27 in self.success:
                iter27.write(oprot)

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




class Sanet_Find_By_Attributes_IDL_args(object):
    """
    Attributes:
     - sessionhandle
     - attr_list
    """

    thrift_spec = (None, (1,
      TType.I32,
      'sessionhandle',
      None,
      None), (2,
      TType.LIST,
      'attr_list',
      (TType.STRUCT, (AaaIDL.ttypes.Attribute_IDL, AaaIDL.ttypes.Attribute_IDL.thrift_spec)),
      None))

    def __init__(self, sessionhandle = None, attr_list = None):
        self.sessionhandle = sessionhandle
        self.attr_list = attr_list



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
                    self.sessionhandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.attr_list = []
                    (_etype31, _size28,) = iprot.readListBegin()
                    for _i32 in xrange(_size28):
                        _elem33 = AaaIDL.ttypes.Attribute_IDL()
                        _elem33.read(iprot)
                        self.attr_list.append(_elem33)

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
        oprot.writeStructBegin('Sanet_Find_By_Attributes_IDL_args')
        if self.sessionhandle != None:
            oprot.writeFieldBegin('sessionhandle', TType.I32, 1)
            oprot.writeI32(self.sessionhandle)
            oprot.writeFieldEnd()
        if self.attr_list != None:
            oprot.writeFieldBegin('attr_list', TType.LIST, 2)
            oprot.writeListBegin(TType.STRUCT, len(self.attr_list))
            for iter34 in self.attr_list:
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




class Sanet_Find_By_Attributes_IDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.LIST,
      'success',
      (TType.STRUCT, (SanetSessionListIDL, SanetSessionListIDL.thrift_spec)),
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
                    (_etype38, _size35,) = iprot.readListBegin()
                    for _i39 in xrange(_size35):
                        _elem40 = SanetSessionListIDL()
                        _elem40.read(iprot)
                        self.success.append(_elem40)

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
        oprot.writeStructBegin('Sanet_Find_By_Attributes_IDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.STRUCT, len(self.success))
            for iter41 in self.success:
                iter41.write(oprot)

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




class Sanet_Get_Attributes_IDL_args(object):
    """
    Attributes:
     - sessionHandle
     - sessionNum
     - reqd_attr_list
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionHandle',
      None,
      None),
     (2,
      TType.I32,
      'sessionNum',
      None,
      None),
     (3,
      TType.LIST,
      'reqd_attr_list',
      (TType.STRUCT, (AaaIDL.ttypes.Attribute_IDL, AaaIDL.ttypes.Attribute_IDL.thrift_spec)),
      None))

    def __init__(self, sessionHandle = None, sessionNum = None, reqd_attr_list = None):
        self.sessionHandle = sessionHandle
        self.sessionNum = sessionNum
        self.reqd_attr_list = reqd_attr_list



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
                    self.sessionNum = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.LIST:
                    self.reqd_attr_list = []
                    (_etype45, _size42,) = iprot.readListBegin()
                    for _i46 in xrange(_size42):
                        _elem47 = AaaIDL.ttypes.Attribute_IDL()
                        _elem47.read(iprot)
                        self.reqd_attr_list.append(_elem47)

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
        oprot.writeStructBegin('Sanet_Get_Attributes_IDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.sessionNum != None:
            oprot.writeFieldBegin('sessionNum', TType.I32, 2)
            oprot.writeI32(self.sessionNum)
            oprot.writeFieldEnd()
        if self.reqd_attr_list != None:
            oprot.writeFieldBegin('reqd_attr_list', TType.LIST, 3)
            oprot.writeListBegin(TType.STRUCT, len(self.reqd_attr_list))
            for iter48 in self.reqd_attr_list:
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




class Sanet_Get_Attributes_IDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.LIST,
      'success',
      (TType.STRUCT, (AaaIDL.ttypes.Attribute_IDL, AaaIDL.ttypes.Attribute_IDL.thrift_spec)),
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
                    (_etype52, _size49,) = iprot.readListBegin()
                    for _i53 in xrange(_size49):
                        _elem54 = AaaIDL.ttypes.Attribute_IDL()
                        _elem54.read(iprot)
                        self.success.append(_elem54)

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
        oprot.writeStructBegin('Sanet_Get_Attributes_IDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.STRUCT, len(self.success))
            for iter55 in self.success:
                iter55.write(oprot)

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




class Sanet_Set_Attributes_IDL_args(object):
    """
    Attributes:
     - sessionHandle
     - sessionNum
     - attr_list
     - isUpdate
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionHandle',
      None,
      None),
     (2,
      TType.I32,
      'sessionNum',
      None,
      None),
     (3,
      TType.LIST,
      'attr_list',
      (TType.STRUCT, (AaaIDL.ttypes.Attribute_IDL, AaaIDL.ttypes.Attribute_IDL.thrift_spec)),
      None),
     (4,
      TType.I32,
      'isUpdate',
      None,
      None))

    def __init__(self, sessionHandle = None, sessionNum = None, attr_list = None, isUpdate = None):
        self.sessionHandle = sessionHandle
        self.sessionNum = sessionNum
        self.attr_list = attr_list
        self.isUpdate = isUpdate



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
                    self.sessionNum = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.LIST:
                    self.attr_list = []
                    (_etype59, _size56,) = iprot.readListBegin()
                    for _i60 in xrange(_size56):
                        _elem61 = AaaIDL.ttypes.Attribute_IDL()
                        _elem61.read(iprot)
                        self.attr_list.append(_elem61)

                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.isUpdate = iprot.readI32()
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
        oprot.writeStructBegin('Sanet_Set_Attributes_IDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.sessionNum != None:
            oprot.writeFieldBegin('sessionNum', TType.I32, 2)
            oprot.writeI32(self.sessionNum)
            oprot.writeFieldEnd()
        if self.attr_list != None:
            oprot.writeFieldBegin('attr_list', TType.LIST, 3)
            oprot.writeListBegin(TType.STRUCT, len(self.attr_list))
            for iter62 in self.attr_list:
                iter62.write(oprot)

            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.isUpdate != None:
            oprot.writeFieldBegin('isUpdate', TType.I32, 4)
            oprot.writeI32(self.isUpdate)
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




class Sanet_Set_Attributes_IDL_result(object):
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
        oprot.writeStructBegin('Sanet_Set_Attributes_IDL_result')
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




class Sanet_Delete_Session_By_Attrs_IDL_args(object):
    """
    Attributes:
     - sessionHandle
     - attr_list
     - isMulti
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionHandle',
      None,
      None),
     (2,
      TType.LIST,
      'attr_list',
      (TType.STRUCT, (AaaIDL.ttypes.Attribute_IDL, AaaIDL.ttypes.Attribute_IDL.thrift_spec)),
      None),
     (3,
      TType.I32,
      'isMulti',
      None,
      None))

    def __init__(self, sessionHandle = None, attr_list = None, isMulti = None):
        self.sessionHandle = sessionHandle
        self.attr_list = attr_list
        self.isMulti = isMulti



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
                if ftype == TType.LIST:
                    self.attr_list = []
                    (_etype66, _size63,) = iprot.readListBegin()
                    for _i67 in xrange(_size63):
                        _elem68 = AaaIDL.ttypes.Attribute_IDL()
                        _elem68.read(iprot)
                        self.attr_list.append(_elem68)

                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.isMulti = iprot.readI32()
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
        oprot.writeStructBegin('Sanet_Delete_Session_By_Attrs_IDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.attr_list != None:
            oprot.writeFieldBegin('attr_list', TType.LIST, 2)
            oprot.writeListBegin(TType.STRUCT, len(self.attr_list))
            for iter69 in self.attr_list:
                iter69.write(oprot)

            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.isMulti != None:
            oprot.writeFieldBegin('isMulti', TType.I32, 3)
            oprot.writeI32(self.isMulti)
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




class Sanet_Delete_Session_By_Attrs_IDL_result(object):
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
        oprot.writeStructBegin('Sanet_Delete_Session_By_Attrs_IDL_result')
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




class Sanet_Delete_Session_IDL_args(object):
    """
    Attributes:
     - sessionHandle
     - sessionNum
    """

    thrift_spec = (None, (1,
      TType.I32,
      'sessionHandle',
      None,
      None), (2,
      TType.I32,
      'sessionNum',
      None,
      None))

    def __init__(self, sessionHandle = None, sessionNum = None):
        self.sessionHandle = sessionHandle
        self.sessionNum = sessionNum



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
                    self.sessionNum = iprot.readI32()
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
        oprot.writeStructBegin('Sanet_Delete_Session_IDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.sessionNum != None:
            oprot.writeFieldBegin('sessionNum', TType.I32, 2)
            oprot.writeI32(self.sessionNum)
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




class Sanet_Delete_Session_IDL_result(object):
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
        oprot.writeStructBegin('Sanet_Delete_Session_IDL_result')
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
# 2015.02.05 17:23:07 IST
