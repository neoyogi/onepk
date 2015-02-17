# 2015.02.05 17:17:54 IST
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

    def ApplManagedData_setConfigIDL(self, sessionHandle, app_version, app_instance, app_config_domain):
        """
            API to set the App's CLI version, instance, and config_domain
        
            Parameters:
             - sessionHandle
             - app_version
             - app_instance
             - app_config_domain
            """
        pass



    def ApplManagedData_getConfigIDL(self, sessionHandle, app_data_name):
        """
            API to retrieve App's own config
        
            Parameters:
             - sessionHandle
             - app_data_name
            """
        pass



    def ApplManagedData_getKeyedDataIDL(self, sessionHandle, app_data_request):
        """
            API to retrieve App's own config using a key
        
            Parameters:
             - sessionHandle
             - app_data_request
            """
        pass



    def ApplManagedData_setShowDataIDL(self, sessionHandle, private_show_data_name, private_show_data_value):
        """
            API to retrieve App's own config using a key
        
            Parameters:
             - sessionHandle
             - private_show_data_name
             - private_show_data_value
            """
        pass



    def ApplManagedData_installXsdIDL(self, sessionHandle, XSD_contents, config_domain, overwrite):
        """
            API to install extensions to the network element's CLI parse tree
        
            Parameters:
             - sessionHandle
             - XSD_contents
             - config_domain
             - overwrite
            """
        pass



    def ApplManagedData_uninstallXsdIDL(self, sessionHandle, app_name, version, config_domain):
        """
            API to uninstall extensions to the network element's CLI parse tree
        
            Parameters:
             - sessionHandle
             - app_name
             - version
             - config_domain
            """
        pass



    def ApplManagedData_isXsdInstalledIDL(self, sessionHandle, app_name, version, config_domain):
        """
            API to query extensions to the network element's CLI parse tree
        
            Parameters:
             - sessionHandle
             - app_name
             - version
             - config_domain
            """
        pass




class Client(Iface):

    def __init__(self, iprot, oprot = None):
        self._iprot = self._oprot = iprot
        if oprot != None:
            self._oprot = oprot
        self._seqid = 0



    def ApplManagedData_setConfigIDL(self, sessionHandle, app_version, app_instance, app_config_domain):
        """
            API to set the App's CLI version, instance, and config_domain
        
            Parameters:
             - sessionHandle
             - app_version
             - app_instance
             - app_config_domain
            """
        self._oprot.rlock.acquire()
        try:
            self.send_ApplManagedData_setConfigIDL(sessionHandle, app_version, app_instance, app_config_domain)
            result = self.recv_ApplManagedData_setConfigIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_ApplManagedData_setConfigIDL(self, sessionHandle, app_version, app_instance, app_config_domain):
        self._oprot.writeMessageBegin('ApplManagedData_setConfigIDL', TMessageType.CALL, self._seqid)
        args = ApplManagedData_setConfigIDL_args()
        args.sessionHandle = sessionHandle
        args.app_version = app_version
        args.app_instance = app_instance
        args.app_config_domain = app_config_domain
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_ApplManagedData_setConfigIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = ApplManagedData_setConfigIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'ApplManagedData_setConfigIDL failed: unknown result')



    def ApplManagedData_getConfigIDL(self, sessionHandle, app_data_name):
        """
            API to retrieve App's own config
        
            Parameters:
             - sessionHandle
             - app_data_name
            """
        self._oprot.rlock.acquire()
        try:
            self.send_ApplManagedData_getConfigIDL(sessionHandle, app_data_name)
            result = self.recv_ApplManagedData_getConfigIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_ApplManagedData_getConfigIDL(self, sessionHandle, app_data_name):
        self._oprot.writeMessageBegin('ApplManagedData_getConfigIDL', TMessageType.CALL, self._seqid)
        args = ApplManagedData_getConfigIDL_args()
        args.sessionHandle = sessionHandle
        args.app_data_name = app_data_name
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_ApplManagedData_getConfigIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = ApplManagedData_getConfigIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'ApplManagedData_getConfigIDL failed: unknown result')



    def ApplManagedData_getKeyedDataIDL(self, sessionHandle, app_data_request):
        """
            API to retrieve App's own config using a key
        
            Parameters:
             - sessionHandle
             - app_data_request
            """
        self._oprot.rlock.acquire()
        try:
            self.send_ApplManagedData_getKeyedDataIDL(sessionHandle, app_data_request)
            result = self.recv_ApplManagedData_getKeyedDataIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_ApplManagedData_getKeyedDataIDL(self, sessionHandle, app_data_request):
        self._oprot.writeMessageBegin('ApplManagedData_getKeyedDataIDL', TMessageType.CALL, self._seqid)
        args = ApplManagedData_getKeyedDataIDL_args()
        args.sessionHandle = sessionHandle
        args.app_data_request = app_data_request
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_ApplManagedData_getKeyedDataIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = ApplManagedData_getKeyedDataIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'ApplManagedData_getKeyedDataIDL failed: unknown result')



    def ApplManagedData_setShowDataIDL(self, sessionHandle, private_show_data_name, private_show_data_value):
        """
            API to retrieve App's own config using a key
        
            Parameters:
             - sessionHandle
             - private_show_data_name
             - private_show_data_value
            """
        self._oprot.rlock.acquire()
        try:
            self.send_ApplManagedData_setShowDataIDL(sessionHandle, private_show_data_name, private_show_data_value)
            result = self.recv_ApplManagedData_setShowDataIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_ApplManagedData_setShowDataIDL(self, sessionHandle, private_show_data_name, private_show_data_value):
        self._oprot.writeMessageBegin('ApplManagedData_setShowDataIDL', TMessageType.CALL, self._seqid)
        args = ApplManagedData_setShowDataIDL_args()
        args.sessionHandle = sessionHandle
        args.private_show_data_name = private_show_data_name
        args.private_show_data_value = private_show_data_value
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_ApplManagedData_setShowDataIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = ApplManagedData_setShowDataIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'ApplManagedData_setShowDataIDL failed: unknown result')



    def ApplManagedData_installXsdIDL(self, sessionHandle, XSD_contents, config_domain, overwrite):
        """
            API to install extensions to the network element's CLI parse tree
        
            Parameters:
             - sessionHandle
             - XSD_contents
             - config_domain
             - overwrite
            """
        self._oprot.rlock.acquire()
        try:
            self.send_ApplManagedData_installXsdIDL(sessionHandle, XSD_contents, config_domain, overwrite)
            result = self.recv_ApplManagedData_installXsdIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_ApplManagedData_installXsdIDL(self, sessionHandle, XSD_contents, config_domain, overwrite):
        self._oprot.writeMessageBegin('ApplManagedData_installXsdIDL', TMessageType.CALL, self._seqid)
        args = ApplManagedData_installXsdIDL_args()
        args.sessionHandle = sessionHandle
        args.XSD_contents = XSD_contents
        args.config_domain = config_domain
        args.overwrite = overwrite
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_ApplManagedData_installXsdIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = ApplManagedData_installXsdIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'ApplManagedData_installXsdIDL failed: unknown result')



    def ApplManagedData_uninstallXsdIDL(self, sessionHandle, app_name, version, config_domain):
        """
            API to uninstall extensions to the network element's CLI parse tree
        
            Parameters:
             - sessionHandle
             - app_name
             - version
             - config_domain
            """
        self._oprot.rlock.acquire()
        try:
            self.send_ApplManagedData_uninstallXsdIDL(sessionHandle, app_name, version, config_domain)
            result = self.recv_ApplManagedData_uninstallXsdIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_ApplManagedData_uninstallXsdIDL(self, sessionHandle, app_name, version, config_domain):
        self._oprot.writeMessageBegin('ApplManagedData_uninstallXsdIDL', TMessageType.CALL, self._seqid)
        args = ApplManagedData_uninstallXsdIDL_args()
        args.sessionHandle = sessionHandle
        args.app_name = app_name
        args.version = version
        args.config_domain = config_domain
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_ApplManagedData_uninstallXsdIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = ApplManagedData_uninstallXsdIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'ApplManagedData_uninstallXsdIDL failed: unknown result')



    def ApplManagedData_isXsdInstalledIDL(self, sessionHandle, app_name, version, config_domain):
        """
            API to query extensions to the network element's CLI parse tree
        
            Parameters:
             - sessionHandle
             - app_name
             - version
             - config_domain
            """
        self._oprot.rlock.acquire()
        try:
            self.send_ApplManagedData_isXsdInstalledIDL(sessionHandle, app_name, version, config_domain)
            result = self.recv_ApplManagedData_isXsdInstalledIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_ApplManagedData_isXsdInstalledIDL(self, sessionHandle, app_name, version, config_domain):
        self._oprot.writeMessageBegin('ApplManagedData_isXsdInstalledIDL', TMessageType.CALL, self._seqid)
        args = ApplManagedData_isXsdInstalledIDL_args()
        args.sessionHandle = sessionHandle
        args.app_name = app_name
        args.version = version
        args.config_domain = config_domain
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_ApplManagedData_isXsdInstalledIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = ApplManagedData_isXsdInstalledIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'ApplManagedData_isXsdInstalledIDL failed: unknown result')




class Processor(Iface, TProcessor):

    def __init__(self, handler):
        self._handler = handler
        self._processMap = {}
        self._processMap['ApplManagedData_setConfigIDL'] = Processor.process_ApplManagedData_setConfigIDL
        self._processMap['ApplManagedData_getConfigIDL'] = Processor.process_ApplManagedData_getConfigIDL
        self._processMap['ApplManagedData_getKeyedDataIDL'] = Processor.process_ApplManagedData_getKeyedDataIDL
        self._processMap['ApplManagedData_setShowDataIDL'] = Processor.process_ApplManagedData_setShowDataIDL
        self._processMap['ApplManagedData_installXsdIDL'] = Processor.process_ApplManagedData_installXsdIDL
        self._processMap['ApplManagedData_uninstallXsdIDL'] = Processor.process_ApplManagedData_uninstallXsdIDL
        self._processMap['ApplManagedData_isXsdInstalledIDL'] = Processor.process_ApplManagedData_isXsdInstalledIDL



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



    def process_ApplManagedData_setConfigIDL(self, seqid, iprot, oprot):
        args = ApplManagedData_setConfigIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = ApplManagedData_setConfigIDL_result()
        try:
            result.success = self._handler.ApplManagedData_setConfigIDL(args.sessionHandle, args.app_version, args.app_instance, args.app_config_domain)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('ApplManagedData_setConfigIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_ApplManagedData_getConfigIDL(self, seqid, iprot, oprot):
        args = ApplManagedData_getConfigIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = ApplManagedData_getConfigIDL_result()
        try:
            result.success = self._handler.ApplManagedData_getConfigIDL(args.sessionHandle, args.app_data_name)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('ApplManagedData_getConfigIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_ApplManagedData_getKeyedDataIDL(self, seqid, iprot, oprot):
        args = ApplManagedData_getKeyedDataIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = ApplManagedData_getKeyedDataIDL_result()
        try:
            result.success = self._handler.ApplManagedData_getKeyedDataIDL(args.sessionHandle, args.app_data_request)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('ApplManagedData_getKeyedDataIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_ApplManagedData_setShowDataIDL(self, seqid, iprot, oprot):
        args = ApplManagedData_setShowDataIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = ApplManagedData_setShowDataIDL_result()
        try:
            result.success = self._handler.ApplManagedData_setShowDataIDL(args.sessionHandle, args.private_show_data_name, args.private_show_data_value)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('ApplManagedData_setShowDataIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_ApplManagedData_installXsdIDL(self, seqid, iprot, oprot):
        args = ApplManagedData_installXsdIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = ApplManagedData_installXsdIDL_result()
        try:
            result.success = self._handler.ApplManagedData_installXsdIDL(args.sessionHandle, args.XSD_contents, args.config_domain, args.overwrite)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('ApplManagedData_installXsdIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_ApplManagedData_uninstallXsdIDL(self, seqid, iprot, oprot):
        args = ApplManagedData_uninstallXsdIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = ApplManagedData_uninstallXsdIDL_result()
        try:
            result.success = self._handler.ApplManagedData_uninstallXsdIDL(args.sessionHandle, args.app_name, args.version, args.config_domain)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('ApplManagedData_uninstallXsdIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_ApplManagedData_isXsdInstalledIDL(self, seqid, iprot, oprot):
        args = ApplManagedData_isXsdInstalledIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = ApplManagedData_isXsdInstalledIDL_result()
        try:
            result.success = self._handler.ApplManagedData_isXsdInstalledIDL(args.sessionHandle, args.app_name, args.version, args.config_domain)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('ApplManagedData_isXsdInstalledIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()




class ApplManagedData_setConfigIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - app_version
     - app_instance
     - app_config_domain
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionHandle',
      None,
      None),
     (2,
      TType.STRING,
      'app_version',
      None,
      None),
     (3,
      TType.STRING,
      'app_instance',
      None,
      None),
     (4,
      TType.STRING,
      'app_config_domain',
      None,
      None))

    def __init__(self, sessionHandle = None, app_version = None, app_instance = None, app_config_domain = None):
        self.sessionHandle = sessionHandle
        self.app_version = app_version
        self.app_instance = app_instance
        self.app_config_domain = app_config_domain



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
                    self.app_version = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.app_instance = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.app_config_domain = iprot.readString()
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
        oprot.writeStructBegin('ApplManagedData_setConfigIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.app_version != None:
            oprot.writeFieldBegin('app_version', TType.STRING, 2)
            oprot.writeString(self.app_version)
            oprot.writeFieldEnd()
        if self.app_instance != None:
            oprot.writeFieldBegin('app_instance', TType.STRING, 3)
            oprot.writeString(self.app_instance)
            oprot.writeFieldEnd()
        if self.app_config_domain != None:
            oprot.writeFieldBegin('app_config_domain', TType.STRING, 4)
            oprot.writeString(self.app_config_domain)
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




class ApplManagedData_setConfigIDL_result(object):
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
        oprot.writeStructBegin('ApplManagedData_setConfigIDL_result')
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




class ApplManagedData_getConfigIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - app_data_name
    """

    thrift_spec = (None, (1,
      TType.I32,
      'sessionHandle',
      None,
      None), (2,
      TType.STRING,
      'app_data_name',
      None,
      None))

    def __init__(self, sessionHandle = None, app_data_name = None):
        self.sessionHandle = sessionHandle
        self.app_data_name = app_data_name



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
                    self.app_data_name = iprot.readString()
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
        oprot.writeStructBegin('ApplManagedData_getConfigIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.app_data_name != None:
            oprot.writeFieldBegin('app_data_name', TType.STRING, 2)
            oprot.writeString(self.app_data_name)
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




class ApplManagedData_getConfigIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.STRING,
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
                if ftype == TType.STRING:
                    self.success = iprot.readString()
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
        oprot.writeStructBegin('ApplManagedData_getConfigIDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.STRING, 0)
            oprot.writeString(self.success)
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




class ApplManagedData_getKeyedDataIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - app_data_request
    """

    thrift_spec = (None, (1,
      TType.I32,
      'sessionHandle',
      None,
      None), (2,
      TType.STRING,
      'app_data_request',
      None,
      None))

    def __init__(self, sessionHandle = None, app_data_request = None):
        self.sessionHandle = sessionHandle
        self.app_data_request = app_data_request



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
                    self.app_data_request = iprot.readString()
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
        oprot.writeStructBegin('ApplManagedData_getKeyedDataIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.app_data_request != None:
            oprot.writeFieldBegin('app_data_request', TType.STRING, 2)
            oprot.writeString(self.app_data_request)
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




class ApplManagedData_getKeyedDataIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.STRING,
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
                if ftype == TType.STRING:
                    self.success = iprot.readString()
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
        oprot.writeStructBegin('ApplManagedData_getKeyedDataIDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.STRING, 0)
            oprot.writeString(self.success)
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




class ApplManagedData_setShowDataIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - private_show_data_name
     - private_show_data_value
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionHandle',
      None,
      None),
     (2,
      TType.STRING,
      'private_show_data_name',
      None,
      None),
     (3,
      TType.STRING,
      'private_show_data_value',
      None,
      None))

    def __init__(self, sessionHandle = None, private_show_data_name = None, private_show_data_value = None):
        self.sessionHandle = sessionHandle
        self.private_show_data_name = private_show_data_name
        self.private_show_data_value = private_show_data_value



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
                    self.private_show_data_name = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.private_show_data_value = iprot.readString()
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
        oprot.writeStructBegin('ApplManagedData_setShowDataIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.private_show_data_name != None:
            oprot.writeFieldBegin('private_show_data_name', TType.STRING, 2)
            oprot.writeString(self.private_show_data_name)
            oprot.writeFieldEnd()
        if self.private_show_data_value != None:
            oprot.writeFieldBegin('private_show_data_value', TType.STRING, 3)
            oprot.writeString(self.private_show_data_value)
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




class ApplManagedData_setShowDataIDL_result(object):
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
        oprot.writeStructBegin('ApplManagedData_setShowDataIDL_result')
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




class ApplManagedData_installXsdIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - XSD_contents
     - config_domain
     - overwrite
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionHandle',
      None,
      None),
     (2,
      TType.STRING,
      'XSD_contents',
      None,
      None),
     (3,
      TType.STRING,
      'config_domain',
      None,
      None),
     (4,
      TType.I32,
      'overwrite',
      None,
      None))

    def __init__(self, sessionHandle = None, XSD_contents = None, config_domain = None, overwrite = None):
        self.sessionHandle = sessionHandle
        self.XSD_contents = XSD_contents
        self.config_domain = config_domain
        self.overwrite = overwrite



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
                    self.XSD_contents = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.config_domain = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.overwrite = iprot.readI32()
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
        oprot.writeStructBegin('ApplManagedData_installXsdIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.XSD_contents != None:
            oprot.writeFieldBegin('XSD_contents', TType.STRING, 2)
            oprot.writeString(self.XSD_contents)
            oprot.writeFieldEnd()
        if self.config_domain != None:
            oprot.writeFieldBegin('config_domain', TType.STRING, 3)
            oprot.writeString(self.config_domain)
            oprot.writeFieldEnd()
        if self.overwrite != None:
            oprot.writeFieldBegin('overwrite', TType.I32, 4)
            oprot.writeI32(self.overwrite)
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




class ApplManagedData_installXsdIDL_result(object):
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
        oprot.writeStructBegin('ApplManagedData_installXsdIDL_result')
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




class ApplManagedData_uninstallXsdIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - app_name
     - version
     - config_domain
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionHandle',
      None,
      None),
     (2,
      TType.STRING,
      'app_name',
      None,
      None),
     (3,
      TType.STRING,
      'version',
      None,
      None),
     (4,
      TType.STRING,
      'config_domain',
      None,
      None))

    def __init__(self, sessionHandle = None, app_name = None, version = None, config_domain = None):
        self.sessionHandle = sessionHandle
        self.app_name = app_name
        self.version = version
        self.config_domain = config_domain



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
                    self.app_name = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.version = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.config_domain = iprot.readString()
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
        oprot.writeStructBegin('ApplManagedData_uninstallXsdIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.app_name != None:
            oprot.writeFieldBegin('app_name', TType.STRING, 2)
            oprot.writeString(self.app_name)
            oprot.writeFieldEnd()
        if self.version != None:
            oprot.writeFieldBegin('version', TType.STRING, 3)
            oprot.writeString(self.version)
            oprot.writeFieldEnd()
        if self.config_domain != None:
            oprot.writeFieldBegin('config_domain', TType.STRING, 4)
            oprot.writeString(self.config_domain)
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




class ApplManagedData_uninstallXsdIDL_result(object):
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
        oprot.writeStructBegin('ApplManagedData_uninstallXsdIDL_result')
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




class ApplManagedData_isXsdInstalledIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - app_name
     - version
     - config_domain
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionHandle',
      None,
      None),
     (2,
      TType.STRING,
      'app_name',
      None,
      None),
     (3,
      TType.STRING,
      'version',
      None,
      None),
     (4,
      TType.STRING,
      'config_domain',
      None,
      None))

    def __init__(self, sessionHandle = None, app_name = None, version = None, config_domain = None):
        self.sessionHandle = sessionHandle
        self.app_name = app_name
        self.version = version
        self.config_domain = config_domain



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
                    self.app_name = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.version = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.config_domain = iprot.readString()
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
        oprot.writeStructBegin('ApplManagedData_isXsdInstalledIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.app_name != None:
            oprot.writeFieldBegin('app_name', TType.STRING, 2)
            oprot.writeString(self.app_name)
            oprot.writeFieldEnd()
        if self.version != None:
            oprot.writeFieldBegin('version', TType.STRING, 3)
            oprot.writeString(self.version)
            oprot.writeFieldEnd()
        if self.config_domain != None:
            oprot.writeFieldBegin('config_domain', TType.STRING, 4)
            oprot.writeString(self.config_domain)
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




class ApplManagedData_isXsdInstalledIDL_result(object):
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
        oprot.writeStructBegin('ApplManagedData_isXsdInstalledIDL_result')
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
# 2015.02.05 17:17:56 IST
