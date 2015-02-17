# 2015.02.05 17:17:50 IST
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

    def authenticate_IDL(self, sessionHandle, username, password, in_attr_list):
        """
        Parameters:
         - sessionHandle
         - username
         - password
         - in_attr_list
        """
        pass



    def account_IDL(self, aaa_user_id, acct_action_type, in_attr_list):
        """
        Parameters:
         - aaa_user_id
         - acct_action_type
         - in_attr_list
        """
        pass



    def deallocate_aaa_user_IDL(self, aaa_user_id, auto_acct_enabled):
        """
        Parameters:
         - aaa_user_id
         - auto_acct_enabled
        """
        pass




class Client(Iface):

    def __init__(self, iprot, oprot = None):
        self._iprot = self._oprot = iprot
        if oprot != None:
            self._oprot = oprot
        self._seqid = 0



    def authenticate_IDL(self, sessionHandle, username, password, in_attr_list):
        """
        Parameters:
         - sessionHandle
         - username
         - password
         - in_attr_list
        """
        self._oprot.rlock.acquire()
        try:
            self.send_authenticate_IDL(sessionHandle, username, password, in_attr_list)
            result = self.recv_authenticate_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_authenticate_IDL(self, sessionHandle, username, password, in_attr_list):
        self._oprot.writeMessageBegin('authenticate_IDL', TMessageType.CALL, self._seqid)
        args = authenticate_IDL_args()
        args.sessionHandle = sessionHandle
        args.username = username
        args.password = password
        args.in_attr_list = in_attr_list
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_authenticate_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = authenticate_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'authenticate_IDL failed: unknown result')



    def account_IDL(self, aaa_user_id, acct_action_type, in_attr_list):
        """
        Parameters:
         - aaa_user_id
         - acct_action_type
         - in_attr_list
        """
        self._oprot.rlock.acquire()
        try:
            self.send_account_IDL(aaa_user_id, acct_action_type, in_attr_list)
            result = self.recv_account_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_account_IDL(self, aaa_user_id, acct_action_type, in_attr_list):
        self._oprot.writeMessageBegin('account_IDL', TMessageType.CALL, self._seqid)
        args = account_IDL_args()
        args.aaa_user_id = aaa_user_id
        args.acct_action_type = acct_action_type
        args.in_attr_list = in_attr_list
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_account_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = account_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'account_IDL failed: unknown result')



    def deallocate_aaa_user_IDL(self, aaa_user_id, auto_acct_enabled):
        """
        Parameters:
         - aaa_user_id
         - auto_acct_enabled
        """
        self._oprot.rlock.acquire()
        try:
            self.send_deallocate_aaa_user_IDL(aaa_user_id, auto_acct_enabled)
            result = self.recv_deallocate_aaa_user_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_deallocate_aaa_user_IDL(self, aaa_user_id, auto_acct_enabled):
        self._oprot.writeMessageBegin('deallocate_aaa_user_IDL', TMessageType.CALL, self._seqid)
        args = deallocate_aaa_user_IDL_args()
        args.aaa_user_id = aaa_user_id
        args.auto_acct_enabled = auto_acct_enabled
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_deallocate_aaa_user_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = deallocate_aaa_user_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'deallocate_aaa_user_IDL failed: unknown result')




class Processor(Iface, TProcessor):

    def __init__(self, handler):
        self._handler = handler
        self._processMap = {}
        self._processMap['authenticate_IDL'] = Processor.process_authenticate_IDL
        self._processMap['account_IDL'] = Processor.process_account_IDL
        self._processMap['deallocate_aaa_user_IDL'] = Processor.process_deallocate_aaa_user_IDL



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



    def process_authenticate_IDL(self, seqid, iprot, oprot):
        args = authenticate_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = authenticate_IDL_result()
        try:
            result.success = self._handler.authenticate_IDL(args.sessionHandle, args.username, args.password, args.in_attr_list)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('authenticate_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_account_IDL(self, seqid, iprot, oprot):
        args = account_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = account_IDL_result()
        try:
            result.success = self._handler.account_IDL(args.aaa_user_id, args.acct_action_type, args.in_attr_list)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('account_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_deallocate_aaa_user_IDL(self, seqid, iprot, oprot):
        args = deallocate_aaa_user_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = deallocate_aaa_user_IDL_result()
        try:
            result.success = self._handler.deallocate_aaa_user_IDL(args.aaa_user_id, args.auto_acct_enabled)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('deallocate_aaa_user_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()




class authenticate_IDL_args(object):
    """
    Attributes:
     - sessionHandle
     - username
     - password
     - in_attr_list
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionHandle',
      None,
      None),
     (2,
      TType.STRING,
      'username',
      None,
      None),
     (3,
      TType.STRING,
      'password',
      None,
      None),
     (4,
      TType.LIST,
      'in_attr_list',
      (TType.STRUCT, (Attribute_IDL, Attribute_IDL.thrift_spec)),
      None))

    def __init__(self, sessionHandle = None, username = None, password = None, in_attr_list = None):
        self.sessionHandle = sessionHandle
        self.username = username
        self.password = password
        self.in_attr_list = in_attr_list



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
                    self.username = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.password = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.LIST:
                    self.in_attr_list = []
                    (_etype17, _size14,) = iprot.readListBegin()
                    for _i18 in xrange(_size14):
                        _elem19 = Attribute_IDL()
                        _elem19.read(iprot)
                        self.in_attr_list.append(_elem19)

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
        oprot.writeStructBegin('authenticate_IDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.username != None:
            oprot.writeFieldBegin('username', TType.STRING, 2)
            oprot.writeString(self.username)
            oprot.writeFieldEnd()
        if self.password != None:
            oprot.writeFieldBegin('password', TType.STRING, 3)
            oprot.writeString(self.password)
            oprot.writeFieldEnd()
        if self.in_attr_list != None:
            oprot.writeFieldBegin('in_attr_list', TType.LIST, 4)
            oprot.writeListBegin(TType.STRUCT, len(self.in_attr_list))
            for iter20 in self.in_attr_list:
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




class authenticate_IDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.STRUCT,
      'success',
      (AuthenResult_IDL, AuthenResult_IDL.thrift_spec),
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
                    self.success = AuthenResult_IDL()
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
        oprot.writeStructBegin('authenticate_IDL_result')
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




class account_IDL_args(object):
    """
    Attributes:
     - aaa_user_id
     - acct_action_type
     - in_attr_list
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'aaa_user_id',
      None,
      None),
     (2,
      TType.I32,
      'acct_action_type',
      None,
      None),
     (3,
      TType.LIST,
      'in_attr_list',
      (TType.STRUCT, (Attribute_IDL, Attribute_IDL.thrift_spec)),
      None))

    def __init__(self, aaa_user_id = None, acct_action_type = None, in_attr_list = None):
        self.aaa_user_id = aaa_user_id
        self.acct_action_type = acct_action_type
        self.in_attr_list = in_attr_list



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
                    self.aaa_user_id = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.acct_action_type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.LIST:
                    self.in_attr_list = []
                    (_etype24, _size21,) = iprot.readListBegin()
                    for _i25 in xrange(_size21):
                        _elem26 = Attribute_IDL()
                        _elem26.read(iprot)
                        self.in_attr_list.append(_elem26)

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
        oprot.writeStructBegin('account_IDL_args')
        if self.aaa_user_id != None:
            oprot.writeFieldBegin('aaa_user_id', TType.I32, 1)
            oprot.writeI32(self.aaa_user_id)
            oprot.writeFieldEnd()
        if self.acct_action_type != None:
            oprot.writeFieldBegin('acct_action_type', TType.I32, 2)
            oprot.writeI32(self.acct_action_type)
            oprot.writeFieldEnd()
        if self.in_attr_list != None:
            oprot.writeFieldBegin('in_attr_list', TType.LIST, 3)
            oprot.writeListBegin(TType.STRUCT, len(self.in_attr_list))
            for iter27 in self.in_attr_list:
                iter27.write(oprot)

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




class account_IDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.STRUCT,
      'success',
      (AcctResult_IDL, AcctResult_IDL.thrift_spec),
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
                    self.success = AcctResult_IDL()
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
        oprot.writeStructBegin('account_IDL_result')
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




class deallocate_aaa_user_IDL_args(object):
    """
    Attributes:
     - aaa_user_id
     - auto_acct_enabled
    """

    thrift_spec = (None, (1,
      TType.I32,
      'aaa_user_id',
      None,
      None), (2,
      TType.I32,
      'auto_acct_enabled',
      None,
      None))

    def __init__(self, aaa_user_id = None, auto_acct_enabled = None):
        self.aaa_user_id = aaa_user_id
        self.auto_acct_enabled = auto_acct_enabled



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
                    self.aaa_user_id = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.auto_acct_enabled = iprot.readI32()
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
        oprot.writeStructBegin('deallocate_aaa_user_IDL_args')
        if self.aaa_user_id != None:
            oprot.writeFieldBegin('aaa_user_id', TType.I32, 1)
            oprot.writeI32(self.aaa_user_id)
            oprot.writeFieldEnd()
        if self.auto_acct_enabled != None:
            oprot.writeFieldBegin('auto_acct_enabled', TType.I32, 2)
            oprot.writeI32(self.auto_acct_enabled)
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




class deallocate_aaa_user_IDL_result(object):
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
        oprot.writeStructBegin('deallocate_aaa_user_IDL_result')
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
# 2015.02.05 17:17:51 IST
