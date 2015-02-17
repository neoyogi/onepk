# 2015.02.05 17:21:23 IST
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

    def getLicenseDetailIDL(self, sessionHandle):
        """
        Parameters:
         - sessionHandle
        """
        pass



    def getLicenseSummaryIDL(self, sessionHandle):
        """
        Parameters:
         - sessionHandle
        """
        pass



    def setCallHomeIDL(self, sessionHandle, username, password, url, email, operType):
        """
        Parameters:
         - sessionHandle
         - username
         - password
         - url
         - email
         - operType
        """
        pass



    def installByPakIDL(self, sessionHandle, pakId):
        """
        Parameters:
         - sessionHandle
         - pakId
        """
        pass



    def installByFileIDL(self, sessionHandle, sourceUrl):
        """
        Parameters:
         - sessionHandle
         - sourceUrl
        """
        pass



    def getNewUdiIDL(self, sessionHandle):
        """
        Parameters:
         - sessionHandle
        """
        pass



    def setEulaIDL(self, sessionHandle, accept):
        """
        Parameters:
         - sessionHandle
         - accept
        """
        pass



    def getEulaIDL(self, sessionHandle):
        """
        Parameters:
         - sessionHandle
        """
        pass



    def getLicenseBootLevelIDL(self, nextboot):
        """
        Parameters:
         - nextboot
        """
        pass



    def setLicenseNextBootLevelIDL(self, bootlevel):
        """
        Parameters:
         - bootlevel
        """
        pass



    def clearLicenseNextBootLevelIDL(self):
        pass



    def getLicenseImageLevelsIDL(self):
        pass




class Client(Iface):

    def __init__(self, iprot, oprot = None):
        self._iprot = self._oprot = iprot
        if oprot != None:
            self._oprot = oprot
        self._seqid = 0



    def getLicenseDetailIDL(self, sessionHandle):
        """
        Parameters:
         - sessionHandle
        """
        self._oprot.rlock.acquire()
        try:
            self.send_getLicenseDetailIDL(sessionHandle)
            result = self.recv_getLicenseDetailIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_getLicenseDetailIDL(self, sessionHandle):
        self._oprot.writeMessageBegin('getLicenseDetailIDL', TMessageType.CALL, self._seqid)
        args = getLicenseDetailIDL_args()
        args.sessionHandle = sessionHandle
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_getLicenseDetailIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = getLicenseDetailIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'getLicenseDetailIDL failed: unknown result')



    def getLicenseSummaryIDL(self, sessionHandle):
        """
        Parameters:
         - sessionHandle
        """
        self._oprot.rlock.acquire()
        try:
            self.send_getLicenseSummaryIDL(sessionHandle)
            result = self.recv_getLicenseSummaryIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_getLicenseSummaryIDL(self, sessionHandle):
        self._oprot.writeMessageBegin('getLicenseSummaryIDL', TMessageType.CALL, self._seqid)
        args = getLicenseSummaryIDL_args()
        args.sessionHandle = sessionHandle
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_getLicenseSummaryIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = getLicenseSummaryIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'getLicenseSummaryIDL failed: unknown result')



    def setCallHomeIDL(self, sessionHandle, username, password, url, email, operType):
        """
        Parameters:
         - sessionHandle
         - username
         - password
         - url
         - email
         - operType
        """
        self._oprot.rlock.acquire()
        try:
            self.send_setCallHomeIDL(sessionHandle, username, password, url, email, operType)
            result = self.recv_setCallHomeIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_setCallHomeIDL(self, sessionHandle, username, password, url, email, operType):
        self._oprot.writeMessageBegin('setCallHomeIDL', TMessageType.CALL, self._seqid)
        args = setCallHomeIDL_args()
        args.sessionHandle = sessionHandle
        args.username = username
        args.password = password
        args.url = url
        args.email = email
        args.operType = operType
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_setCallHomeIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = setCallHomeIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'setCallHomeIDL failed: unknown result')



    def installByPakIDL(self, sessionHandle, pakId):
        """
        Parameters:
         - sessionHandle
         - pakId
        """
        self._oprot.rlock.acquire()
        try:
            self.send_installByPakIDL(sessionHandle, pakId)
            result = self.recv_installByPakIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_installByPakIDL(self, sessionHandle, pakId):
        self._oprot.writeMessageBegin('installByPakIDL', TMessageType.CALL, self._seqid)
        args = installByPakIDL_args()
        args.sessionHandle = sessionHandle
        args.pakId = pakId
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_installByPakIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = installByPakIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'installByPakIDL failed: unknown result')



    def installByFileIDL(self, sessionHandle, sourceUrl):
        """
        Parameters:
         - sessionHandle
         - sourceUrl
        """
        self._oprot.rlock.acquire()
        try:
            self.send_installByFileIDL(sessionHandle, sourceUrl)
            result = self.recv_installByFileIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_installByFileIDL(self, sessionHandle, sourceUrl):
        self._oprot.writeMessageBegin('installByFileIDL', TMessageType.CALL, self._seqid)
        args = installByFileIDL_args()
        args.sessionHandle = sessionHandle
        args.sourceUrl = sourceUrl
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_installByFileIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = installByFileIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'installByFileIDL failed: unknown result')



    def getNewUdiIDL(self, sessionHandle):
        """
        Parameters:
         - sessionHandle
        """
        self._oprot.rlock.acquire()
        try:
            self.send_getNewUdiIDL(sessionHandle)
            result = self.recv_getNewUdiIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_getNewUdiIDL(self, sessionHandle):
        self._oprot.writeMessageBegin('getNewUdiIDL', TMessageType.CALL, self._seqid)
        args = getNewUdiIDL_args()
        args.sessionHandle = sessionHandle
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_getNewUdiIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = getNewUdiIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'getNewUdiIDL failed: unknown result')



    def setEulaIDL(self, sessionHandle, accept):
        """
        Parameters:
         - sessionHandle
         - accept
        """
        self._oprot.rlock.acquire()
        try:
            self.send_setEulaIDL(sessionHandle, accept)
            result = self.recv_setEulaIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_setEulaIDL(self, sessionHandle, accept):
        self._oprot.writeMessageBegin('setEulaIDL', TMessageType.CALL, self._seqid)
        args = setEulaIDL_args()
        args.sessionHandle = sessionHandle
        args.accept = accept
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_setEulaIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = setEulaIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'setEulaIDL failed: unknown result')



    def getEulaIDL(self, sessionHandle):
        """
        Parameters:
         - sessionHandle
        """
        self._oprot.rlock.acquire()
        try:
            self.send_getEulaIDL(sessionHandle)
            result = self.recv_getEulaIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_getEulaIDL(self, sessionHandle):
        self._oprot.writeMessageBegin('getEulaIDL', TMessageType.CALL, self._seqid)
        args = getEulaIDL_args()
        args.sessionHandle = sessionHandle
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_getEulaIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = getEulaIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'getEulaIDL failed: unknown result')



    def getLicenseBootLevelIDL(self, nextboot):
        """
        Parameters:
         - nextboot
        """
        self._oprot.rlock.acquire()
        try:
            self.send_getLicenseBootLevelIDL(nextboot)
            result = self.recv_getLicenseBootLevelIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_getLicenseBootLevelIDL(self, nextboot):
        self._oprot.writeMessageBegin('getLicenseBootLevelIDL', TMessageType.CALL, self._seqid)
        args = getLicenseBootLevelIDL_args()
        args.nextboot = nextboot
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_getLicenseBootLevelIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = getLicenseBootLevelIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'getLicenseBootLevelIDL failed: unknown result')



    def setLicenseNextBootLevelIDL(self, bootlevel):
        """
        Parameters:
         - bootlevel
        """
        self._oprot.rlock.acquire()
        try:
            self.send_setLicenseNextBootLevelIDL(bootlevel)
            result = self.recv_setLicenseNextBootLevelIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_setLicenseNextBootLevelIDL(self, bootlevel):
        self._oprot.writeMessageBegin('setLicenseNextBootLevelIDL', TMessageType.CALL, self._seqid)
        args = setLicenseNextBootLevelIDL_args()
        args.bootlevel = bootlevel
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_setLicenseNextBootLevelIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = setLicenseNextBootLevelIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'setLicenseNextBootLevelIDL failed: unknown result')



    def clearLicenseNextBootLevelIDL(self):
        self._oprot.rlock.acquire()
        try:
            self.send_clearLicenseNextBootLevelIDL()
            result = self.recv_clearLicenseNextBootLevelIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_clearLicenseNextBootLevelIDL(self):
        self._oprot.writeMessageBegin('clearLicenseNextBootLevelIDL', TMessageType.CALL, self._seqid)
        args = clearLicenseNextBootLevelIDL_args()
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_clearLicenseNextBootLevelIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = clearLicenseNextBootLevelIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'clearLicenseNextBootLevelIDL failed: unknown result')



    def getLicenseImageLevelsIDL(self):
        self._oprot.rlock.acquire()
        try:
            self.send_getLicenseImageLevelsIDL()
            result = self.recv_getLicenseImageLevelsIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_getLicenseImageLevelsIDL(self):
        self._oprot.writeMessageBegin('getLicenseImageLevelsIDL', TMessageType.CALL, self._seqid)
        args = getLicenseImageLevelsIDL_args()
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_getLicenseImageLevelsIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = getLicenseImageLevelsIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'getLicenseImageLevelsIDL failed: unknown result')




class Processor(Iface, TProcessor):

    def __init__(self, handler):
        self._handler = handler
        self._processMap = {}
        self._processMap['getLicenseDetailIDL'] = Processor.process_getLicenseDetailIDL
        self._processMap['getLicenseSummaryIDL'] = Processor.process_getLicenseSummaryIDL
        self._processMap['setCallHomeIDL'] = Processor.process_setCallHomeIDL
        self._processMap['installByPakIDL'] = Processor.process_installByPakIDL
        self._processMap['installByFileIDL'] = Processor.process_installByFileIDL
        self._processMap['getNewUdiIDL'] = Processor.process_getNewUdiIDL
        self._processMap['setEulaIDL'] = Processor.process_setEulaIDL
        self._processMap['getEulaIDL'] = Processor.process_getEulaIDL
        self._processMap['getLicenseBootLevelIDL'] = Processor.process_getLicenseBootLevelIDL
        self._processMap['setLicenseNextBootLevelIDL'] = Processor.process_setLicenseNextBootLevelIDL
        self._processMap['clearLicenseNextBootLevelIDL'] = Processor.process_clearLicenseNextBootLevelIDL
        self._processMap['getLicenseImageLevelsIDL'] = Processor.process_getLicenseImageLevelsIDL



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



    def process_getLicenseDetailIDL(self, seqid, iprot, oprot):
        args = getLicenseDetailIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getLicenseDetailIDL_result()
        try:
            result.success = self._handler.getLicenseDetailIDL(args.sessionHandle)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('getLicenseDetailIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_getLicenseSummaryIDL(self, seqid, iprot, oprot):
        args = getLicenseSummaryIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getLicenseSummaryIDL_result()
        try:
            result.success = self._handler.getLicenseSummaryIDL(args.sessionHandle)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('getLicenseSummaryIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_setCallHomeIDL(self, seqid, iprot, oprot):
        args = setCallHomeIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = setCallHomeIDL_result()
        try:
            result.success = self._handler.setCallHomeIDL(args.sessionHandle, args.username, args.password, args.url, args.email, args.operType)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('setCallHomeIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_installByPakIDL(self, seqid, iprot, oprot):
        args = installByPakIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = installByPakIDL_result()
        try:
            result.success = self._handler.installByPakIDL(args.sessionHandle, args.pakId)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('installByPakIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_installByFileIDL(self, seqid, iprot, oprot):
        args = installByFileIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = installByFileIDL_result()
        try:
            result.success = self._handler.installByFileIDL(args.sessionHandle, args.sourceUrl)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('installByFileIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_getNewUdiIDL(self, seqid, iprot, oprot):
        args = getNewUdiIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getNewUdiIDL_result()
        try:
            result.success = self._handler.getNewUdiIDL(args.sessionHandle)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('getNewUdiIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_setEulaIDL(self, seqid, iprot, oprot):
        args = setEulaIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = setEulaIDL_result()
        try:
            result.success = self._handler.setEulaIDL(args.sessionHandle, args.accept)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('setEulaIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_getEulaIDL(self, seqid, iprot, oprot):
        args = getEulaIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getEulaIDL_result()
        try:
            result.success = self._handler.getEulaIDL(args.sessionHandle)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('getEulaIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_getLicenseBootLevelIDL(self, seqid, iprot, oprot):
        args = getLicenseBootLevelIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getLicenseBootLevelIDL_result()
        try:
            result.success = self._handler.getLicenseBootLevelIDL(args.nextboot)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('getLicenseBootLevelIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_setLicenseNextBootLevelIDL(self, seqid, iprot, oprot):
        args = setLicenseNextBootLevelIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = setLicenseNextBootLevelIDL_result()
        try:
            result.success = self._handler.setLicenseNextBootLevelIDL(args.bootlevel)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('setLicenseNextBootLevelIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_clearLicenseNextBootLevelIDL(self, seqid, iprot, oprot):
        args = clearLicenseNextBootLevelIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = clearLicenseNextBootLevelIDL_result()
        try:
            result.success = self._handler.clearLicenseNextBootLevelIDL()
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('clearLicenseNextBootLevelIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_getLicenseImageLevelsIDL(self, seqid, iprot, oprot):
        args = getLicenseImageLevelsIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getLicenseImageLevelsIDL_result()
        try:
            result.success = self._handler.getLicenseImageLevelsIDL()
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('getLicenseImageLevelsIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()




class getLicenseDetailIDL_args(object):
    """
    Attributes:
     - sessionHandle
    """

    thrift_spec = (None, (1,
      TType.I32,
      'sessionHandle',
      None,
      None))

    def __init__(self, sessionHandle = None):
        self.sessionHandle = sessionHandle



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
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()

        iprot.readStructEnd()



    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return 
        oprot.writeStructBegin('getLicenseDetailIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
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




class getLicenseDetailIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.LIST,
      'success',
      (TType.STRUCT, (LicenseDetailIDL, LicenseDetailIDL.thrift_spec)),
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
                        _elem12 = LicenseDetailIDL()
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
        oprot.writeStructBegin('getLicenseDetailIDL_result')
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




class getLicenseSummaryIDL_args(object):
    """
    Attributes:
     - sessionHandle
    """

    thrift_spec = (None, (1,
      TType.I32,
      'sessionHandle',
      None,
      None))

    def __init__(self, sessionHandle = None):
        self.sessionHandle = sessionHandle



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
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()

        iprot.readStructEnd()



    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return 
        oprot.writeStructBegin('getLicenseSummaryIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
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




class getLicenseSummaryIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.LIST,
      'success',
      (TType.STRUCT, (LicenseInfoIDL, LicenseInfoIDL.thrift_spec)),
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
                        _elem19 = LicenseInfoIDL()
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
        oprot.writeStructBegin('getLicenseSummaryIDL_result')
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




class setCallHomeIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - username
     - password
     - url
     - email
     - operType
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
      TType.STRING,
      'url',
      None,
      None),
     (5,
      TType.STRING,
      'email',
      None,
      None),
     (6,
      TType.I32,
      'operType',
      None,
      None))

    def __init__(self, sessionHandle = None, username = None, password = None, url = None, email = None, operType = None):
        self.sessionHandle = sessionHandle
        self.username = username
        self.password = password
        self.url = url
        self.email = email
        self.operType = operType



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
                if ftype == TType.STRING:
                    self.url = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.email = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I32:
                    self.operType = iprot.readI32()
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
        oprot.writeStructBegin('setCallHomeIDL_args')
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
        if self.url != None:
            oprot.writeFieldBegin('url', TType.STRING, 4)
            oprot.writeString(self.url)
            oprot.writeFieldEnd()
        if self.email != None:
            oprot.writeFieldBegin('email', TType.STRING, 5)
            oprot.writeString(self.email)
            oprot.writeFieldEnd()
        if self.operType != None:
            oprot.writeFieldBegin('operType', TType.I32, 6)
            oprot.writeI32(self.operType)
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




class setCallHomeIDL_result(object):
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
        oprot.writeStructBegin('setCallHomeIDL_result')
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




class installByPakIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - pakId
    """

    thrift_spec = (None, (1,
      TType.I32,
      'sessionHandle',
      None,
      None), (2,
      TType.STRING,
      'pakId',
      None,
      None))

    def __init__(self, sessionHandle = None, pakId = None):
        self.sessionHandle = sessionHandle
        self.pakId = pakId



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
                    self.pakId = iprot.readString()
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
        oprot.writeStructBegin('installByPakIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.pakId != None:
            oprot.writeFieldBegin('pakId', TType.STRING, 2)
            oprot.writeString(self.pakId)
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




class installByPakIDL_result(object):
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
        oprot.writeStructBegin('installByPakIDL_result')
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




class installByFileIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - sourceUrl
    """

    thrift_spec = (None, (1,
      TType.I32,
      'sessionHandle',
      None,
      None), (2,
      TType.STRING,
      'sourceUrl',
      None,
      None))

    def __init__(self, sessionHandle = None, sourceUrl = None):
        self.sessionHandle = sessionHandle
        self.sourceUrl = sourceUrl



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
                    self.sourceUrl = iprot.readString()
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
        oprot.writeStructBegin('installByFileIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.sourceUrl != None:
            oprot.writeFieldBegin('sourceUrl', TType.STRING, 2)
            oprot.writeString(self.sourceUrl)
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




class installByFileIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.STRUCT,
      'success',
      (LicenseInstallStatusIDL, LicenseInstallStatusIDL.thrift_spec),
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
                    self.success = LicenseInstallStatusIDL()
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
        oprot.writeStructBegin('installByFileIDL_result')
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




class getNewUdiIDL_args(object):
    """
    Attributes:
     - sessionHandle
    """

    thrift_spec = (None, (1,
      TType.I32,
      'sessionHandle',
      None,
      None))

    def __init__(self, sessionHandle = None):
        self.sessionHandle = sessionHandle



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
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()

        iprot.readStructEnd()



    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return 
        oprot.writeStructBegin('getNewUdiIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
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




class getNewUdiIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.STRUCT,
      'success',
      (LicenseUDIIDL, LicenseUDIIDL.thrift_spec),
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
                    self.success = LicenseUDIIDL()
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
        oprot.writeStructBegin('getNewUdiIDL_result')
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




class setEulaIDL_args(object):
    """
    Attributes:
     - sessionHandle
     - accept
    """

    thrift_spec = (None, (1,
      TType.I32,
      'sessionHandle',
      None,
      None), (2,
      TType.I32,
      'accept',
      None,
      None))

    def __init__(self, sessionHandle = None, accept = None):
        self.sessionHandle = sessionHandle
        self.accept = accept



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
                    self.accept = iprot.readI32()
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
        oprot.writeStructBegin('setEulaIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.accept != None:
            oprot.writeFieldBegin('accept', TType.I32, 2)
            oprot.writeI32(self.accept)
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




class setEulaIDL_result(object):
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
        oprot.writeStructBegin('setEulaIDL_result')
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




class getEulaIDL_args(object):
    """
    Attributes:
     - sessionHandle
    """

    thrift_spec = (None, (1,
      TType.I32,
      'sessionHandle',
      None,
      None))

    def __init__(self, sessionHandle = None):
        self.sessionHandle = sessionHandle



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
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()

        iprot.readStructEnd()



    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return 
        oprot.writeStructBegin('getEulaIDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
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




class getEulaIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.STRUCT,
      'success',
      (LicenseEulaIDL, LicenseEulaIDL.thrift_spec),
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
                    self.success = LicenseEulaIDL()
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
        oprot.writeStructBegin('getEulaIDL_result')
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




class getLicenseBootLevelIDL_args(object):
    """
    Attributes:
     - nextboot
    """

    thrift_spec = (None, (1,
      TType.I32,
      'nextboot',
      None,
      None))

    def __init__(self, nextboot = None):
        self.nextboot = nextboot



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
                    self.nextboot = iprot.readI32()
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
        oprot.writeStructBegin('getLicenseBootLevelIDL_args')
        if self.nextboot != None:
            oprot.writeFieldBegin('nextboot', TType.I32, 1)
            oprot.writeI32(self.nextboot)
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




class getLicenseBootLevelIDL_result(object):
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
        oprot.writeStructBegin('getLicenseBootLevelIDL_result')
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




class setLicenseNextBootLevelIDL_args(object):
    """
    Attributes:
     - bootlevel
    """

    thrift_spec = (None, (1,
      TType.STRING,
      'bootlevel',
      None,
      None))

    def __init__(self, bootlevel = None):
        self.bootlevel = bootlevel



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
                if ftype == TType.STRING:
                    self.bootlevel = iprot.readString()
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
        oprot.writeStructBegin('setLicenseNextBootLevelIDL_args')
        if self.bootlevel != None:
            oprot.writeFieldBegin('bootlevel', TType.STRING, 1)
            oprot.writeString(self.bootlevel)
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




class setLicenseNextBootLevelIDL_result(object):
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
        oprot.writeStructBegin('setLicenseNextBootLevelIDL_result')
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




class clearLicenseNextBootLevelIDL_args(object):
    thrift_spec = ()

    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()

        iprot.readStructEnd()



    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return 
        oprot.writeStructBegin('clearLicenseNextBootLevelIDL_args')
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




class clearLicenseNextBootLevelIDL_result(object):
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
        oprot.writeStructBegin('clearLicenseNextBootLevelIDL_result')
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




class getLicenseImageLevelsIDL_args(object):
    thrift_spec = ()

    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()

        iprot.readStructEnd()



    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return 
        oprot.writeStructBegin('getLicenseImageLevelsIDL_args')
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




class getLicenseImageLevelsIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.LIST,
      'success',
      (TType.STRING, None),
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
                        _elem26 = iprot.readString()
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
        oprot.writeStructBegin('getLicenseImageLevelsIDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.STRING, len(self.success))
            for iter27 in self.success:
                oprot.writeString(iter27)

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




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:21:25 IST
