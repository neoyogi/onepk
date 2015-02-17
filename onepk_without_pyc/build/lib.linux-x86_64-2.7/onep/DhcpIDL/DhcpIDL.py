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

    def addDhcpPoolIDL(self, sessionId, poolName, vrfName):
        """
        Parameters:
         - sessionId
         - poolName
         - vrfName
        """
        pass



    def deleteDhcpPoolIDL(self, sessionId, poolName):
        """
        Parameters:
         - sessionId
         - poolName
        """
        pass



    def getDhcpPoolListIDL(self, sessionId):
        """
        Parameters:
         - sessionId
        """
        pass



    def setDhcpDbAgentIDL(self, sessionId, url, writeDelay, timeOut):
        """
        Parameters:
         - sessionId
         - url
         - writeDelay
         - timeOut
        """
        pass



    def getDhcpDbAgentListIDL(self, sessionId):
        """
        Parameters:
         - sessionId
        """
        pass



    def deleteDhcpDbAgentIDL(self, sessionId, url):
        """
        Parameters:
         - sessionId
         - url
        """
        pass



    def setDhcpExclusionIDL(self, sessionId, vrfName, exclude):
        """
        Parameters:
         - sessionId
         - vrfName
         - exclude
        """
        pass



    def getDhcpExclusionIDL(self, sessionId, vrfName):
        """
        Parameters:
         - sessionId
         - vrfName
        """
        pass



    def deleteDhcpExclusionIDL(self, sessionId, vrfName, exclude):
        """
        Parameters:
         - sessionId
         - vrfName
         - exclude
        """
        pass



    def setDhcpLeaseIDL(self, sessionId, poolName, infinite, lease):
        """
        Parameters:
         - sessionId
         - poolName
         - infinite
         - lease
        """
        pass



    def getDhcpLeaseIDL(self, sessionId, poolName):
        """
        Parameters:
         - sessionId
         - poolName
        """
        pass



    def addDeleteDhcpServerOptionIDL(self, sessionId, poolName, ipList, option, action):
        """
        Parameters:
         - sessionId
         - poolName
         - ipList
         - option
         - action
        """
        pass



    def getDhcpServerOptionIDL(self, sessionId, poolName, option):
        """
        Parameters:
         - sessionId
         - poolName
         - option
        """
        pass



    def addDeleteDhcpNetbiosNodeIDL(self, sessionId, poolName, type, action):
        """
        Parameters:
         - sessionId
         - poolName
         - type
         - action
        """
        pass



    def getDhcpNetbiosNodeIDL(self, sessionId, poolName):
        """
        Parameters:
         - sessionId
         - poolName
        """
        pass



    def addDeleteDhcpPoolDomainIDL(self, sessionId, poolName, domainName, action):
        """
        Parameters:
         - sessionId
         - poolName
         - domainName
         - action
        """
        pass



    def getDhcpPoolDomainIDL(self, sessionId, poolName):
        """
        Parameters:
         - sessionId
         - poolName
        """
        pass



    def addDeleteDhcpPoolHostIDL(self, sessionId, poolName, prefix, action):
        """
        Parameters:
         - sessionId
         - poolName
         - prefix
         - action
        """
        pass



    def getDhcpPoolHostIDL(self, sessionId, poolName):
        """
        Parameters:
         - sessionId
         - poolName
        """
        pass



    def addDeleteDhcpPoolNetworkIDL(self, sessionId, poolName, network, nwType, action):
        """
        Parameters:
         - sessionId
         - poolName
         - network
         - nwType
         - action
        """
        pass



    def getDhcpPoolNetworkIDL(self, sessionId, poolName):
        """
        Parameters:
         - sessionId
         - poolName
        """
        pass



    def addDeleteDhcpPoolClientNameIDL(self, sessionId, poolName, clientName, action):
        """
        Parameters:
         - sessionId
         - poolName
         - clientName
         - action
        """
        pass



    def getDhcpPoolClientNameIDL(self, sessionId, poolName):
        """
        Parameters:
         - sessionId
         - poolName
        """
        pass



    def addDeleteDhcpPoolHwAddrIDL(self, sessionId, poolName, hwAddr, action):
        """
        Parameters:
         - sessionId
         - poolName
         - hwAddr
         - action
        """
        pass



    def getDhcpPoolHwAddrIDL(self, sessionId, poolName):
        """
        Parameters:
         - sessionId
         - poolName
        """
        pass



    def setUnsetDhcpConflictLoggingIDL(self, sessionId, action):
        """
        Parameters:
         - sessionId
         - action
        """
        pass



    def getDHCPBindingListIDL(self, vrfName, addr, maxCount):
        """
        Parameters:
         - vrfName
         - addr
         - maxCount
        """
        pass



    def getDHCPBindingByIpAddrIDL(self, vrfName, addr):
        """
        Parameters:
         - vrfName
         - addr
        """
        pass



    def deleteDhcpAllBindingsIDL(self, sessionId, vrf):
        """
        Parameters:
         - sessionId
         - vrf
        """
        pass




class Client(Iface):

    def __init__(self, iprot, oprot = None):
        self._iprot = self._oprot = iprot
        if oprot != None:
            self._oprot = oprot
        self._seqid = 0



    def addDhcpPoolIDL(self, sessionId, poolName, vrfName):
        """
        Parameters:
         - sessionId
         - poolName
         - vrfName
        """
        self._oprot.rlock.acquire()
        try:
            self.send_addDhcpPoolIDL(sessionId, poolName, vrfName)
            result = self.recv_addDhcpPoolIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_addDhcpPoolIDL(self, sessionId, poolName, vrfName):
        self._oprot.writeMessageBegin('addDhcpPoolIDL', TMessageType.CALL, self._seqid)
        args = addDhcpPoolIDL_args()
        args.sessionId = sessionId
        args.poolName = poolName
        args.vrfName = vrfName
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_addDhcpPoolIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = addDhcpPoolIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'addDhcpPoolIDL failed: unknown result')



    def deleteDhcpPoolIDL(self, sessionId, poolName):
        """
        Parameters:
         - sessionId
         - poolName
        """
        self._oprot.rlock.acquire()
        try:
            self.send_deleteDhcpPoolIDL(sessionId, poolName)
            result = self.recv_deleteDhcpPoolIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_deleteDhcpPoolIDL(self, sessionId, poolName):
        self._oprot.writeMessageBegin('deleteDhcpPoolIDL', TMessageType.CALL, self._seqid)
        args = deleteDhcpPoolIDL_args()
        args.sessionId = sessionId
        args.poolName = poolName
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_deleteDhcpPoolIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = deleteDhcpPoolIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'deleteDhcpPoolIDL failed: unknown result')



    def getDhcpPoolListIDL(self, sessionId):
        """
        Parameters:
         - sessionId
        """
        self._oprot.rlock.acquire()
        try:
            self.send_getDhcpPoolListIDL(sessionId)
            result = self.recv_getDhcpPoolListIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_getDhcpPoolListIDL(self, sessionId):
        self._oprot.writeMessageBegin('getDhcpPoolListIDL', TMessageType.CALL, self._seqid)
        args = getDhcpPoolListIDL_args()
        args.sessionId = sessionId
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_getDhcpPoolListIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = getDhcpPoolListIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'getDhcpPoolListIDL failed: unknown result')



    def setDhcpDbAgentIDL(self, sessionId, url, writeDelay, timeOut):
        """
        Parameters:
         - sessionId
         - url
         - writeDelay
         - timeOut
        """
        self._oprot.rlock.acquire()
        try:
            self.send_setDhcpDbAgentIDL(sessionId, url, writeDelay, timeOut)
            result = self.recv_setDhcpDbAgentIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_setDhcpDbAgentIDL(self, sessionId, url, writeDelay, timeOut):
        self._oprot.writeMessageBegin('setDhcpDbAgentIDL', TMessageType.CALL, self._seqid)
        args = setDhcpDbAgentIDL_args()
        args.sessionId = sessionId
        args.url = url
        args.writeDelay = writeDelay
        args.timeOut = timeOut
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_setDhcpDbAgentIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = setDhcpDbAgentIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'setDhcpDbAgentIDL failed: unknown result')



    def getDhcpDbAgentListIDL(self, sessionId):
        """
        Parameters:
         - sessionId
        """
        self._oprot.rlock.acquire()
        try:
            self.send_getDhcpDbAgentListIDL(sessionId)
            result = self.recv_getDhcpDbAgentListIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_getDhcpDbAgentListIDL(self, sessionId):
        self._oprot.writeMessageBegin('getDhcpDbAgentListIDL', TMessageType.CALL, self._seqid)
        args = getDhcpDbAgentListIDL_args()
        args.sessionId = sessionId
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_getDhcpDbAgentListIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = getDhcpDbAgentListIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'getDhcpDbAgentListIDL failed: unknown result')



    def deleteDhcpDbAgentIDL(self, sessionId, url):
        """
        Parameters:
         - sessionId
         - url
        """
        self._oprot.rlock.acquire()
        try:
            self.send_deleteDhcpDbAgentIDL(sessionId, url)
            result = self.recv_deleteDhcpDbAgentIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_deleteDhcpDbAgentIDL(self, sessionId, url):
        self._oprot.writeMessageBegin('deleteDhcpDbAgentIDL', TMessageType.CALL, self._seqid)
        args = deleteDhcpDbAgentIDL_args()
        args.sessionId = sessionId
        args.url = url
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_deleteDhcpDbAgentIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = deleteDhcpDbAgentIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'deleteDhcpDbAgentIDL failed: unknown result')



    def setDhcpExclusionIDL(self, sessionId, vrfName, exclude):
        """
        Parameters:
         - sessionId
         - vrfName
         - exclude
        """
        self._oprot.rlock.acquire()
        try:
            self.send_setDhcpExclusionIDL(sessionId, vrfName, exclude)
            result = self.recv_setDhcpExclusionIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_setDhcpExclusionIDL(self, sessionId, vrfName, exclude):
        self._oprot.writeMessageBegin('setDhcpExclusionIDL', TMessageType.CALL, self._seqid)
        args = setDhcpExclusionIDL_args()
        args.sessionId = sessionId
        args.vrfName = vrfName
        args.exclude = exclude
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_setDhcpExclusionIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = setDhcpExclusionIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'setDhcpExclusionIDL failed: unknown result')



    def getDhcpExclusionIDL(self, sessionId, vrfName):
        """
        Parameters:
         - sessionId
         - vrfName
        """
        self._oprot.rlock.acquire()
        try:
            self.send_getDhcpExclusionIDL(sessionId, vrfName)
            result = self.recv_getDhcpExclusionIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_getDhcpExclusionIDL(self, sessionId, vrfName):
        self._oprot.writeMessageBegin('getDhcpExclusionIDL', TMessageType.CALL, self._seqid)
        args = getDhcpExclusionIDL_args()
        args.sessionId = sessionId
        args.vrfName = vrfName
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_getDhcpExclusionIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = getDhcpExclusionIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'getDhcpExclusionIDL failed: unknown result')



    def deleteDhcpExclusionIDL(self, sessionId, vrfName, exclude):
        """
        Parameters:
         - sessionId
         - vrfName
         - exclude
        """
        self._oprot.rlock.acquire()
        try:
            self.send_deleteDhcpExclusionIDL(sessionId, vrfName, exclude)
            result = self.recv_deleteDhcpExclusionIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_deleteDhcpExclusionIDL(self, sessionId, vrfName, exclude):
        self._oprot.writeMessageBegin('deleteDhcpExclusionIDL', TMessageType.CALL, self._seqid)
        args = deleteDhcpExclusionIDL_args()
        args.sessionId = sessionId
        args.vrfName = vrfName
        args.exclude = exclude
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_deleteDhcpExclusionIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = deleteDhcpExclusionIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'deleteDhcpExclusionIDL failed: unknown result')



    def setDhcpLeaseIDL(self, sessionId, poolName, infinite, lease):
        """
        Parameters:
         - sessionId
         - poolName
         - infinite
         - lease
        """
        self._oprot.rlock.acquire()
        try:
            self.send_setDhcpLeaseIDL(sessionId, poolName, infinite, lease)
            result = self.recv_setDhcpLeaseIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_setDhcpLeaseIDL(self, sessionId, poolName, infinite, lease):
        self._oprot.writeMessageBegin('setDhcpLeaseIDL', TMessageType.CALL, self._seqid)
        args = setDhcpLeaseIDL_args()
        args.sessionId = sessionId
        args.poolName = poolName
        args.infinite = infinite
        args.lease = lease
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_setDhcpLeaseIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = setDhcpLeaseIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'setDhcpLeaseIDL failed: unknown result')



    def getDhcpLeaseIDL(self, sessionId, poolName):
        """
        Parameters:
         - sessionId
         - poolName
        """
        self._oprot.rlock.acquire()
        try:
            self.send_getDhcpLeaseIDL(sessionId, poolName)
            result = self.recv_getDhcpLeaseIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_getDhcpLeaseIDL(self, sessionId, poolName):
        self._oprot.writeMessageBegin('getDhcpLeaseIDL', TMessageType.CALL, self._seqid)
        args = getDhcpLeaseIDL_args()
        args.sessionId = sessionId
        args.poolName = poolName
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_getDhcpLeaseIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = getDhcpLeaseIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'getDhcpLeaseIDL failed: unknown result')



    def addDeleteDhcpServerOptionIDL(self, sessionId, poolName, ipList, option, action):
        """
        Parameters:
         - sessionId
         - poolName
         - ipList
         - option
         - action
        """
        self._oprot.rlock.acquire()
        try:
            self.send_addDeleteDhcpServerOptionIDL(sessionId, poolName, ipList, option, action)
            result = self.recv_addDeleteDhcpServerOptionIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_addDeleteDhcpServerOptionIDL(self, sessionId, poolName, ipList, option, action):
        self._oprot.writeMessageBegin('addDeleteDhcpServerOptionIDL', TMessageType.CALL, self._seqid)
        args = addDeleteDhcpServerOptionIDL_args()
        args.sessionId = sessionId
        args.poolName = poolName
        args.ipList = ipList
        args.option = option
        args.action = action
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_addDeleteDhcpServerOptionIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = addDeleteDhcpServerOptionIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'addDeleteDhcpServerOptionIDL failed: unknown result')



    def getDhcpServerOptionIDL(self, sessionId, poolName, option):
        """
        Parameters:
         - sessionId
         - poolName
         - option
        """
        self._oprot.rlock.acquire()
        try:
            self.send_getDhcpServerOptionIDL(sessionId, poolName, option)
            result = self.recv_getDhcpServerOptionIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_getDhcpServerOptionIDL(self, sessionId, poolName, option):
        self._oprot.writeMessageBegin('getDhcpServerOptionIDL', TMessageType.CALL, self._seqid)
        args = getDhcpServerOptionIDL_args()
        args.sessionId = sessionId
        args.poolName = poolName
        args.option = option
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_getDhcpServerOptionIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = getDhcpServerOptionIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'getDhcpServerOptionIDL failed: unknown result')



    def addDeleteDhcpNetbiosNodeIDL(self, sessionId, poolName, type, action):
        """
        Parameters:
         - sessionId
         - poolName
         - type
         - action
        """
        self._oprot.rlock.acquire()
        try:
            self.send_addDeleteDhcpNetbiosNodeIDL(sessionId, poolName, type, action)
            result = self.recv_addDeleteDhcpNetbiosNodeIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_addDeleteDhcpNetbiosNodeIDL(self, sessionId, poolName, type, action):
        self._oprot.writeMessageBegin('addDeleteDhcpNetbiosNodeIDL', TMessageType.CALL, self._seqid)
        args = addDeleteDhcpNetbiosNodeIDL_args()
        args.sessionId = sessionId
        args.poolName = poolName
        args.type = type
        args.action = action
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_addDeleteDhcpNetbiosNodeIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = addDeleteDhcpNetbiosNodeIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'addDeleteDhcpNetbiosNodeIDL failed: unknown result')



    def getDhcpNetbiosNodeIDL(self, sessionId, poolName):
        """
        Parameters:
         - sessionId
         - poolName
        """
        self._oprot.rlock.acquire()
        try:
            self.send_getDhcpNetbiosNodeIDL(sessionId, poolName)
            result = self.recv_getDhcpNetbiosNodeIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_getDhcpNetbiosNodeIDL(self, sessionId, poolName):
        self._oprot.writeMessageBegin('getDhcpNetbiosNodeIDL', TMessageType.CALL, self._seqid)
        args = getDhcpNetbiosNodeIDL_args()
        args.sessionId = sessionId
        args.poolName = poolName
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_getDhcpNetbiosNodeIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = getDhcpNetbiosNodeIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'getDhcpNetbiosNodeIDL failed: unknown result')



    def addDeleteDhcpPoolDomainIDL(self, sessionId, poolName, domainName, action):
        """
        Parameters:
         - sessionId
         - poolName
         - domainName
         - action
        """
        self._oprot.rlock.acquire()
        try:
            self.send_addDeleteDhcpPoolDomainIDL(sessionId, poolName, domainName, action)
            result = self.recv_addDeleteDhcpPoolDomainIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_addDeleteDhcpPoolDomainIDL(self, sessionId, poolName, domainName, action):
        self._oprot.writeMessageBegin('addDeleteDhcpPoolDomainIDL', TMessageType.CALL, self._seqid)
        args = addDeleteDhcpPoolDomainIDL_args()
        args.sessionId = sessionId
        args.poolName = poolName
        args.domainName = domainName
        args.action = action
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_addDeleteDhcpPoolDomainIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = addDeleteDhcpPoolDomainIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'addDeleteDhcpPoolDomainIDL failed: unknown result')



    def getDhcpPoolDomainIDL(self, sessionId, poolName):
        """
        Parameters:
         - sessionId
         - poolName
        """
        self._oprot.rlock.acquire()
        try:
            self.send_getDhcpPoolDomainIDL(sessionId, poolName)
            result = self.recv_getDhcpPoolDomainIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_getDhcpPoolDomainIDL(self, sessionId, poolName):
        self._oprot.writeMessageBegin('getDhcpPoolDomainIDL', TMessageType.CALL, self._seqid)
        args = getDhcpPoolDomainIDL_args()
        args.sessionId = sessionId
        args.poolName = poolName
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_getDhcpPoolDomainIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = getDhcpPoolDomainIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'getDhcpPoolDomainIDL failed: unknown result')



    def addDeleteDhcpPoolHostIDL(self, sessionId, poolName, prefix, action):
        """
        Parameters:
         - sessionId
         - poolName
         - prefix
         - action
        """
        self._oprot.rlock.acquire()
        try:
            self.send_addDeleteDhcpPoolHostIDL(sessionId, poolName, prefix, action)
            result = self.recv_addDeleteDhcpPoolHostIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_addDeleteDhcpPoolHostIDL(self, sessionId, poolName, prefix, action):
        self._oprot.writeMessageBegin('addDeleteDhcpPoolHostIDL', TMessageType.CALL, self._seqid)
        args = addDeleteDhcpPoolHostIDL_args()
        args.sessionId = sessionId
        args.poolName = poolName
        args.prefix = prefix
        args.action = action
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_addDeleteDhcpPoolHostIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = addDeleteDhcpPoolHostIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'addDeleteDhcpPoolHostIDL failed: unknown result')



    def getDhcpPoolHostIDL(self, sessionId, poolName):
        """
        Parameters:
         - sessionId
         - poolName
        """
        self._oprot.rlock.acquire()
        try:
            self.send_getDhcpPoolHostIDL(sessionId, poolName)
            result = self.recv_getDhcpPoolHostIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_getDhcpPoolHostIDL(self, sessionId, poolName):
        self._oprot.writeMessageBegin('getDhcpPoolHostIDL', TMessageType.CALL, self._seqid)
        args = getDhcpPoolHostIDL_args()
        args.sessionId = sessionId
        args.poolName = poolName
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_getDhcpPoolHostIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = getDhcpPoolHostIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'getDhcpPoolHostIDL failed: unknown result')



    def addDeleteDhcpPoolNetworkIDL(self, sessionId, poolName, network, nwType, action):
        """
        Parameters:
         - sessionId
         - poolName
         - network
         - nwType
         - action
        """
        self._oprot.rlock.acquire()
        try:
            self.send_addDeleteDhcpPoolNetworkIDL(sessionId, poolName, network, nwType, action)
            result = self.recv_addDeleteDhcpPoolNetworkIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_addDeleteDhcpPoolNetworkIDL(self, sessionId, poolName, network, nwType, action):
        self._oprot.writeMessageBegin('addDeleteDhcpPoolNetworkIDL', TMessageType.CALL, self._seqid)
        args = addDeleteDhcpPoolNetworkIDL_args()
        args.sessionId = sessionId
        args.poolName = poolName
        args.network = network
        args.nwType = nwType
        args.action = action
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_addDeleteDhcpPoolNetworkIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = addDeleteDhcpPoolNetworkIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'addDeleteDhcpPoolNetworkIDL failed: unknown result')



    def getDhcpPoolNetworkIDL(self, sessionId, poolName):
        """
        Parameters:
         - sessionId
         - poolName
        """
        self._oprot.rlock.acquire()
        try:
            self.send_getDhcpPoolNetworkIDL(sessionId, poolName)
            result = self.recv_getDhcpPoolNetworkIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_getDhcpPoolNetworkIDL(self, sessionId, poolName):
        self._oprot.writeMessageBegin('getDhcpPoolNetworkIDL', TMessageType.CALL, self._seqid)
        args = getDhcpPoolNetworkIDL_args()
        args.sessionId = sessionId
        args.poolName = poolName
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_getDhcpPoolNetworkIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = getDhcpPoolNetworkIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'getDhcpPoolNetworkIDL failed: unknown result')



    def addDeleteDhcpPoolClientNameIDL(self, sessionId, poolName, clientName, action):
        """
        Parameters:
         - sessionId
         - poolName
         - clientName
         - action
        """
        self._oprot.rlock.acquire()
        try:
            self.send_addDeleteDhcpPoolClientNameIDL(sessionId, poolName, clientName, action)
            result = self.recv_addDeleteDhcpPoolClientNameIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_addDeleteDhcpPoolClientNameIDL(self, sessionId, poolName, clientName, action):
        self._oprot.writeMessageBegin('addDeleteDhcpPoolClientNameIDL', TMessageType.CALL, self._seqid)
        args = addDeleteDhcpPoolClientNameIDL_args()
        args.sessionId = sessionId
        args.poolName = poolName
        args.clientName = clientName
        args.action = action
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_addDeleteDhcpPoolClientNameIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = addDeleteDhcpPoolClientNameIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'addDeleteDhcpPoolClientNameIDL failed: unknown result')



    def getDhcpPoolClientNameIDL(self, sessionId, poolName):
        """
        Parameters:
         - sessionId
         - poolName
        """
        self._oprot.rlock.acquire()
        try:
            self.send_getDhcpPoolClientNameIDL(sessionId, poolName)
            result = self.recv_getDhcpPoolClientNameIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_getDhcpPoolClientNameIDL(self, sessionId, poolName):
        self._oprot.writeMessageBegin('getDhcpPoolClientNameIDL', TMessageType.CALL, self._seqid)
        args = getDhcpPoolClientNameIDL_args()
        args.sessionId = sessionId
        args.poolName = poolName
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_getDhcpPoolClientNameIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = getDhcpPoolClientNameIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'getDhcpPoolClientNameIDL failed: unknown result')



    def addDeleteDhcpPoolHwAddrIDL(self, sessionId, poolName, hwAddr, action):
        """
        Parameters:
         - sessionId
         - poolName
         - hwAddr
         - action
        """
        self._oprot.rlock.acquire()
        try:
            self.send_addDeleteDhcpPoolHwAddrIDL(sessionId, poolName, hwAddr, action)
            result = self.recv_addDeleteDhcpPoolHwAddrIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_addDeleteDhcpPoolHwAddrIDL(self, sessionId, poolName, hwAddr, action):
        self._oprot.writeMessageBegin('addDeleteDhcpPoolHwAddrIDL', TMessageType.CALL, self._seqid)
        args = addDeleteDhcpPoolHwAddrIDL_args()
        args.sessionId = sessionId
        args.poolName = poolName
        args.hwAddr = hwAddr
        args.action = action
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_addDeleteDhcpPoolHwAddrIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = addDeleteDhcpPoolHwAddrIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'addDeleteDhcpPoolHwAddrIDL failed: unknown result')



    def getDhcpPoolHwAddrIDL(self, sessionId, poolName):
        """
        Parameters:
         - sessionId
         - poolName
        """
        self._oprot.rlock.acquire()
        try:
            self.send_getDhcpPoolHwAddrIDL(sessionId, poolName)
            result = self.recv_getDhcpPoolHwAddrIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_getDhcpPoolHwAddrIDL(self, sessionId, poolName):
        self._oprot.writeMessageBegin('getDhcpPoolHwAddrIDL', TMessageType.CALL, self._seqid)
        args = getDhcpPoolHwAddrIDL_args()
        args.sessionId = sessionId
        args.poolName = poolName
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_getDhcpPoolHwAddrIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = getDhcpPoolHwAddrIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'getDhcpPoolHwAddrIDL failed: unknown result')



    def setUnsetDhcpConflictLoggingIDL(self, sessionId, action):
        """
        Parameters:
         - sessionId
         - action
        """
        self._oprot.rlock.acquire()
        try:
            self.send_setUnsetDhcpConflictLoggingIDL(sessionId, action)
            result = self.recv_setUnsetDhcpConflictLoggingIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_setUnsetDhcpConflictLoggingIDL(self, sessionId, action):
        self._oprot.writeMessageBegin('setUnsetDhcpConflictLoggingIDL', TMessageType.CALL, self._seqid)
        args = setUnsetDhcpConflictLoggingIDL_args()
        args.sessionId = sessionId
        args.action = action
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_setUnsetDhcpConflictLoggingIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = setUnsetDhcpConflictLoggingIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'setUnsetDhcpConflictLoggingIDL failed: unknown result')



    def getDHCPBindingListIDL(self, vrfName, addr, maxCount):
        """
        Parameters:
         - vrfName
         - addr
         - maxCount
        """
        self._oprot.rlock.acquire()
        try:
            self.send_getDHCPBindingListIDL(vrfName, addr, maxCount)
            result = self.recv_getDHCPBindingListIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_getDHCPBindingListIDL(self, vrfName, addr, maxCount):
        self._oprot.writeMessageBegin('getDHCPBindingListIDL', TMessageType.CALL, self._seqid)
        args = getDHCPBindingListIDL_args()
        args.vrfName = vrfName
        args.addr = addr
        args.maxCount = maxCount
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_getDHCPBindingListIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = getDHCPBindingListIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'getDHCPBindingListIDL failed: unknown result')



    def getDHCPBindingByIpAddrIDL(self, vrfName, addr):
        """
        Parameters:
         - vrfName
         - addr
        """
        self._oprot.rlock.acquire()
        try:
            self.send_getDHCPBindingByIpAddrIDL(vrfName, addr)
            result = self.recv_getDHCPBindingByIpAddrIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_getDHCPBindingByIpAddrIDL(self, vrfName, addr):
        self._oprot.writeMessageBegin('getDHCPBindingByIpAddrIDL', TMessageType.CALL, self._seqid)
        args = getDHCPBindingByIpAddrIDL_args()
        args.vrfName = vrfName
        args.addr = addr
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_getDHCPBindingByIpAddrIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = getDHCPBindingByIpAddrIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'getDHCPBindingByIpAddrIDL failed: unknown result')



    def deleteDhcpAllBindingsIDL(self, sessionId, vrf):
        """
        Parameters:
         - sessionId
         - vrf
        """
        self._oprot.rlock.acquire()
        try:
            self.send_deleteDhcpAllBindingsIDL(sessionId, vrf)
            result = self.recv_deleteDhcpAllBindingsIDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_deleteDhcpAllBindingsIDL(self, sessionId, vrf):
        self._oprot.writeMessageBegin('deleteDhcpAllBindingsIDL', TMessageType.CALL, self._seqid)
        args = deleteDhcpAllBindingsIDL_args()
        args.sessionId = sessionId
        args.vrf = vrf
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_deleteDhcpAllBindingsIDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = deleteDhcpAllBindingsIDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'deleteDhcpAllBindingsIDL failed: unknown result')




class Processor(Iface, TProcessor):

    def __init__(self, handler):
        self._handler = handler
        self._processMap = {}
        self._processMap['addDhcpPoolIDL'] = Processor.process_addDhcpPoolIDL
        self._processMap['deleteDhcpPoolIDL'] = Processor.process_deleteDhcpPoolIDL
        self._processMap['getDhcpPoolListIDL'] = Processor.process_getDhcpPoolListIDL
        self._processMap['setDhcpDbAgentIDL'] = Processor.process_setDhcpDbAgentIDL
        self._processMap['getDhcpDbAgentListIDL'] = Processor.process_getDhcpDbAgentListIDL
        self._processMap['deleteDhcpDbAgentIDL'] = Processor.process_deleteDhcpDbAgentIDL
        self._processMap['setDhcpExclusionIDL'] = Processor.process_setDhcpExclusionIDL
        self._processMap['getDhcpExclusionIDL'] = Processor.process_getDhcpExclusionIDL
        self._processMap['deleteDhcpExclusionIDL'] = Processor.process_deleteDhcpExclusionIDL
        self._processMap['setDhcpLeaseIDL'] = Processor.process_setDhcpLeaseIDL
        self._processMap['getDhcpLeaseIDL'] = Processor.process_getDhcpLeaseIDL
        self._processMap['addDeleteDhcpServerOptionIDL'] = Processor.process_addDeleteDhcpServerOptionIDL
        self._processMap['getDhcpServerOptionIDL'] = Processor.process_getDhcpServerOptionIDL
        self._processMap['addDeleteDhcpNetbiosNodeIDL'] = Processor.process_addDeleteDhcpNetbiosNodeIDL
        self._processMap['getDhcpNetbiosNodeIDL'] = Processor.process_getDhcpNetbiosNodeIDL
        self._processMap['addDeleteDhcpPoolDomainIDL'] = Processor.process_addDeleteDhcpPoolDomainIDL
        self._processMap['getDhcpPoolDomainIDL'] = Processor.process_getDhcpPoolDomainIDL
        self._processMap['addDeleteDhcpPoolHostIDL'] = Processor.process_addDeleteDhcpPoolHostIDL
        self._processMap['getDhcpPoolHostIDL'] = Processor.process_getDhcpPoolHostIDL
        self._processMap['addDeleteDhcpPoolNetworkIDL'] = Processor.process_addDeleteDhcpPoolNetworkIDL
        self._processMap['getDhcpPoolNetworkIDL'] = Processor.process_getDhcpPoolNetworkIDL
        self._processMap['addDeleteDhcpPoolClientNameIDL'] = Processor.process_addDeleteDhcpPoolClientNameIDL
        self._processMap['getDhcpPoolClientNameIDL'] = Processor.process_getDhcpPoolClientNameIDL
        self._processMap['addDeleteDhcpPoolHwAddrIDL'] = Processor.process_addDeleteDhcpPoolHwAddrIDL
        self._processMap['getDhcpPoolHwAddrIDL'] = Processor.process_getDhcpPoolHwAddrIDL
        self._processMap['setUnsetDhcpConflictLoggingIDL'] = Processor.process_setUnsetDhcpConflictLoggingIDL
        self._processMap['getDHCPBindingListIDL'] = Processor.process_getDHCPBindingListIDL
        self._processMap['getDHCPBindingByIpAddrIDL'] = Processor.process_getDHCPBindingByIpAddrIDL
        self._processMap['deleteDhcpAllBindingsIDL'] = Processor.process_deleteDhcpAllBindingsIDL



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



    def process_addDhcpPoolIDL(self, seqid, iprot, oprot):
        args = addDhcpPoolIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = addDhcpPoolIDL_result()
        try:
            result.success = self._handler.addDhcpPoolIDL(args.sessionId, args.poolName, args.vrfName)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('addDhcpPoolIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_deleteDhcpPoolIDL(self, seqid, iprot, oprot):
        args = deleteDhcpPoolIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = deleteDhcpPoolIDL_result()
        try:
            result.success = self._handler.deleteDhcpPoolIDL(args.sessionId, args.poolName)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('deleteDhcpPoolIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_getDhcpPoolListIDL(self, seqid, iprot, oprot):
        args = getDhcpPoolListIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getDhcpPoolListIDL_result()
        try:
            result.success = self._handler.getDhcpPoolListIDL(args.sessionId)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('getDhcpPoolListIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_setDhcpDbAgentIDL(self, seqid, iprot, oprot):
        args = setDhcpDbAgentIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = setDhcpDbAgentIDL_result()
        try:
            result.success = self._handler.setDhcpDbAgentIDL(args.sessionId, args.url, args.writeDelay, args.timeOut)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('setDhcpDbAgentIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_getDhcpDbAgentListIDL(self, seqid, iprot, oprot):
        args = getDhcpDbAgentListIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getDhcpDbAgentListIDL_result()
        try:
            result.success = self._handler.getDhcpDbAgentListIDL(args.sessionId)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('getDhcpDbAgentListIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_deleteDhcpDbAgentIDL(self, seqid, iprot, oprot):
        args = deleteDhcpDbAgentIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = deleteDhcpDbAgentIDL_result()
        try:
            result.success = self._handler.deleteDhcpDbAgentIDL(args.sessionId, args.url)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('deleteDhcpDbAgentIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_setDhcpExclusionIDL(self, seqid, iprot, oprot):
        args = setDhcpExclusionIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = setDhcpExclusionIDL_result()
        try:
            result.success = self._handler.setDhcpExclusionIDL(args.sessionId, args.vrfName, args.exclude)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('setDhcpExclusionIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_getDhcpExclusionIDL(self, seqid, iprot, oprot):
        args = getDhcpExclusionIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getDhcpExclusionIDL_result()
        try:
            result.success = self._handler.getDhcpExclusionIDL(args.sessionId, args.vrfName)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('getDhcpExclusionIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_deleteDhcpExclusionIDL(self, seqid, iprot, oprot):
        args = deleteDhcpExclusionIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = deleteDhcpExclusionIDL_result()
        try:
            result.success = self._handler.deleteDhcpExclusionIDL(args.sessionId, args.vrfName, args.exclude)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('deleteDhcpExclusionIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_setDhcpLeaseIDL(self, seqid, iprot, oprot):
        args = setDhcpLeaseIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = setDhcpLeaseIDL_result()
        try:
            result.success = self._handler.setDhcpLeaseIDL(args.sessionId, args.poolName, args.infinite, args.lease)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('setDhcpLeaseIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_getDhcpLeaseIDL(self, seqid, iprot, oprot):
        args = getDhcpLeaseIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getDhcpLeaseIDL_result()
        try:
            result.success = self._handler.getDhcpLeaseIDL(args.sessionId, args.poolName)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('getDhcpLeaseIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_addDeleteDhcpServerOptionIDL(self, seqid, iprot, oprot):
        args = addDeleteDhcpServerOptionIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = addDeleteDhcpServerOptionIDL_result()
        try:
            result.success = self._handler.addDeleteDhcpServerOptionIDL(args.sessionId, args.poolName, args.ipList, args.option, args.action)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('addDeleteDhcpServerOptionIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_getDhcpServerOptionIDL(self, seqid, iprot, oprot):
        args = getDhcpServerOptionIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getDhcpServerOptionIDL_result()
        try:
            result.success = self._handler.getDhcpServerOptionIDL(args.sessionId, args.poolName, args.option)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('getDhcpServerOptionIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_addDeleteDhcpNetbiosNodeIDL(self, seqid, iprot, oprot):
        args = addDeleteDhcpNetbiosNodeIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = addDeleteDhcpNetbiosNodeIDL_result()
        try:
            result.success = self._handler.addDeleteDhcpNetbiosNodeIDL(args.sessionId, args.poolName, args.type, args.action)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('addDeleteDhcpNetbiosNodeIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_getDhcpNetbiosNodeIDL(self, seqid, iprot, oprot):
        args = getDhcpNetbiosNodeIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getDhcpNetbiosNodeIDL_result()
        try:
            result.success = self._handler.getDhcpNetbiosNodeIDL(args.sessionId, args.poolName)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('getDhcpNetbiosNodeIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_addDeleteDhcpPoolDomainIDL(self, seqid, iprot, oprot):
        args = addDeleteDhcpPoolDomainIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = addDeleteDhcpPoolDomainIDL_result()
        try:
            result.success = self._handler.addDeleteDhcpPoolDomainIDL(args.sessionId, args.poolName, args.domainName, args.action)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('addDeleteDhcpPoolDomainIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_getDhcpPoolDomainIDL(self, seqid, iprot, oprot):
        args = getDhcpPoolDomainIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getDhcpPoolDomainIDL_result()
        try:
            result.success = self._handler.getDhcpPoolDomainIDL(args.sessionId, args.poolName)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('getDhcpPoolDomainIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_addDeleteDhcpPoolHostIDL(self, seqid, iprot, oprot):
        args = addDeleteDhcpPoolHostIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = addDeleteDhcpPoolHostIDL_result()
        try:
            result.success = self._handler.addDeleteDhcpPoolHostIDL(args.sessionId, args.poolName, args.prefix, args.action)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('addDeleteDhcpPoolHostIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_getDhcpPoolHostIDL(self, seqid, iprot, oprot):
        args = getDhcpPoolHostIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getDhcpPoolHostIDL_result()
        try:
            result.success = self._handler.getDhcpPoolHostIDL(args.sessionId, args.poolName)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('getDhcpPoolHostIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_addDeleteDhcpPoolNetworkIDL(self, seqid, iprot, oprot):
        args = addDeleteDhcpPoolNetworkIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = addDeleteDhcpPoolNetworkIDL_result()
        try:
            result.success = self._handler.addDeleteDhcpPoolNetworkIDL(args.sessionId, args.poolName, args.network, args.nwType, args.action)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('addDeleteDhcpPoolNetworkIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_getDhcpPoolNetworkIDL(self, seqid, iprot, oprot):
        args = getDhcpPoolNetworkIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getDhcpPoolNetworkIDL_result()
        try:
            result.success = self._handler.getDhcpPoolNetworkIDL(args.sessionId, args.poolName)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('getDhcpPoolNetworkIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_addDeleteDhcpPoolClientNameIDL(self, seqid, iprot, oprot):
        args = addDeleteDhcpPoolClientNameIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = addDeleteDhcpPoolClientNameIDL_result()
        try:
            result.success = self._handler.addDeleteDhcpPoolClientNameIDL(args.sessionId, args.poolName, args.clientName, args.action)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('addDeleteDhcpPoolClientNameIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_getDhcpPoolClientNameIDL(self, seqid, iprot, oprot):
        args = getDhcpPoolClientNameIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getDhcpPoolClientNameIDL_result()
        try:
            result.success = self._handler.getDhcpPoolClientNameIDL(args.sessionId, args.poolName)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('getDhcpPoolClientNameIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_addDeleteDhcpPoolHwAddrIDL(self, seqid, iprot, oprot):
        args = addDeleteDhcpPoolHwAddrIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = addDeleteDhcpPoolHwAddrIDL_result()
        try:
            result.success = self._handler.addDeleteDhcpPoolHwAddrIDL(args.sessionId, args.poolName, args.hwAddr, args.action)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('addDeleteDhcpPoolHwAddrIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_getDhcpPoolHwAddrIDL(self, seqid, iprot, oprot):
        args = getDhcpPoolHwAddrIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getDhcpPoolHwAddrIDL_result()
        try:
            result.success = self._handler.getDhcpPoolHwAddrIDL(args.sessionId, args.poolName)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('getDhcpPoolHwAddrIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_setUnsetDhcpConflictLoggingIDL(self, seqid, iprot, oprot):
        args = setUnsetDhcpConflictLoggingIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = setUnsetDhcpConflictLoggingIDL_result()
        try:
            result.success = self._handler.setUnsetDhcpConflictLoggingIDL(args.sessionId, args.action)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('setUnsetDhcpConflictLoggingIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_getDHCPBindingListIDL(self, seqid, iprot, oprot):
        args = getDHCPBindingListIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getDHCPBindingListIDL_result()
        try:
            result.success = self._handler.getDHCPBindingListIDL(args.vrfName, args.addr, args.maxCount)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('getDHCPBindingListIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_getDHCPBindingByIpAddrIDL(self, seqid, iprot, oprot):
        args = getDHCPBindingByIpAddrIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getDHCPBindingByIpAddrIDL_result()
        try:
            result.success = self._handler.getDHCPBindingByIpAddrIDL(args.vrfName, args.addr)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('getDHCPBindingByIpAddrIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_deleteDhcpAllBindingsIDL(self, seqid, iprot, oprot):
        args = deleteDhcpAllBindingsIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = deleteDhcpAllBindingsIDL_result()
        try:
            result.success = self._handler.deleteDhcpAllBindingsIDL(args.sessionId, args.vrf)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('deleteDhcpAllBindingsIDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()




class addDhcpPoolIDL_args(object):
    """
    Attributes:
     - sessionId
     - poolName
     - vrfName
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionId',
      None,
      None),
     (2,
      TType.STRING,
      'poolName',
      None,
      None),
     (3,
      TType.STRING,
      'vrfName',
      None,
      None))

    def __init__(self, sessionId = None, poolName = None, vrfName = None):
        self.sessionId = sessionId
        self.poolName = poolName
        self.vrfName = vrfName



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
                    self.sessionId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.poolName = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.vrfName = iprot.readString()
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
        oprot.writeStructBegin('addDhcpPoolIDL_args')
        if self.sessionId != None:
            oprot.writeFieldBegin('sessionId', TType.I32, 1)
            oprot.writeI32(self.sessionId)
            oprot.writeFieldEnd()
        if self.poolName != None:
            oprot.writeFieldBegin('poolName', TType.STRING, 2)
            oprot.writeString(self.poolName)
            oprot.writeFieldEnd()
        if self.vrfName != None:
            oprot.writeFieldBegin('vrfName', TType.STRING, 3)
            oprot.writeString(self.vrfName)
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




class addDhcpPoolIDL_result(object):
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
        oprot.writeStructBegin('addDhcpPoolIDL_result')
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




class deleteDhcpPoolIDL_args(object):
    """
    Attributes:
     - sessionId
     - poolName
    """

    thrift_spec = (None, (1,
      TType.I32,
      'sessionId',
      None,
      None), (2,
      TType.STRING,
      'poolName',
      None,
      None))

    def __init__(self, sessionId = None, poolName = None):
        self.sessionId = sessionId
        self.poolName = poolName



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
                    self.sessionId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.poolName = iprot.readString()
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
        oprot.writeStructBegin('deleteDhcpPoolIDL_args')
        if self.sessionId != None:
            oprot.writeFieldBegin('sessionId', TType.I32, 1)
            oprot.writeI32(self.sessionId)
            oprot.writeFieldEnd()
        if self.poolName != None:
            oprot.writeFieldBegin('poolName', TType.STRING, 2)
            oprot.writeString(self.poolName)
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




class deleteDhcpPoolIDL_result(object):
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
        oprot.writeStructBegin('deleteDhcpPoolIDL_result')
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




class getDhcpPoolListIDL_args(object):
    """
    Attributes:
     - sessionId
    """

    thrift_spec = (None, (1,
      TType.I32,
      'sessionId',
      None,
      None))

    def __init__(self, sessionId = None):
        self.sessionId = sessionId



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
                    self.sessionId = iprot.readI32()
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
        oprot.writeStructBegin('getDhcpPoolListIDL_args')
        if self.sessionId != None:
            oprot.writeFieldBegin('sessionId', TType.I32, 1)
            oprot.writeI32(self.sessionId)
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




class getDhcpPoolListIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.LIST,
      'success',
      (TType.STRUCT, (DhcpPoolParamIDL, DhcpPoolParamIDL.thrift_spec)),
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
                        _elem5 = DhcpPoolParamIDL()
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
        oprot.writeStructBegin('getDhcpPoolListIDL_result')
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




class setDhcpDbAgentIDL_args(object):
    """
    Attributes:
     - sessionId
     - url
     - writeDelay
     - timeOut
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionId',
      None,
      None),
     (2,
      TType.STRING,
      'url',
      None,
      None),
     (3,
      TType.I32,
      'writeDelay',
      None,
      None),
     (4,
      TType.I32,
      'timeOut',
      None,
      None))

    def __init__(self, sessionId = None, url = None, writeDelay = None, timeOut = None):
        self.sessionId = sessionId
        self.url = url
        self.writeDelay = writeDelay
        self.timeOut = timeOut



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
                    self.sessionId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.url = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.writeDelay = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.timeOut = iprot.readI32()
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
        oprot.writeStructBegin('setDhcpDbAgentIDL_args')
        if self.sessionId != None:
            oprot.writeFieldBegin('sessionId', TType.I32, 1)
            oprot.writeI32(self.sessionId)
            oprot.writeFieldEnd()
        if self.url != None:
            oprot.writeFieldBegin('url', TType.STRING, 2)
            oprot.writeString(self.url)
            oprot.writeFieldEnd()
        if self.writeDelay != None:
            oprot.writeFieldBegin('writeDelay', TType.I32, 3)
            oprot.writeI32(self.writeDelay)
            oprot.writeFieldEnd()
        if self.timeOut != None:
            oprot.writeFieldBegin('timeOut', TType.I32, 4)
            oprot.writeI32(self.timeOut)
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




class setDhcpDbAgentIDL_result(object):
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
        oprot.writeStructBegin('setDhcpDbAgentIDL_result')
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




class getDhcpDbAgentListIDL_args(object):
    """
    Attributes:
     - sessionId
    """

    thrift_spec = (None, (1,
      TType.I32,
      'sessionId',
      None,
      None))

    def __init__(self, sessionId = None):
        self.sessionId = sessionId



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
                    self.sessionId = iprot.readI32()
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
        oprot.writeStructBegin('getDhcpDbAgentListIDL_args')
        if self.sessionId != None:
            oprot.writeFieldBegin('sessionId', TType.I32, 1)
            oprot.writeI32(self.sessionId)
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




class getDhcpDbAgentListIDL_result(object):
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
                    (_etype10, _size7,) = iprot.readListBegin()
                    for _i11 in xrange(_size7):
                        _elem12 = iprot.readString()
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
        oprot.writeStructBegin('getDhcpDbAgentListIDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.STRING, len(self.success))
            for iter13 in self.success:
                oprot.writeString(iter13)

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




class deleteDhcpDbAgentIDL_args(object):
    """
    Attributes:
     - sessionId
     - url
    """

    thrift_spec = (None, (1,
      TType.I32,
      'sessionId',
      None,
      None), (2,
      TType.STRING,
      'url',
      None,
      None))

    def __init__(self, sessionId = None, url = None):
        self.sessionId = sessionId
        self.url = url



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
                    self.sessionId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.url = iprot.readString()
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
        oprot.writeStructBegin('deleteDhcpDbAgentIDL_args')
        if self.sessionId != None:
            oprot.writeFieldBegin('sessionId', TType.I32, 1)
            oprot.writeI32(self.sessionId)
            oprot.writeFieldEnd()
        if self.url != None:
            oprot.writeFieldBegin('url', TType.STRING, 2)
            oprot.writeString(self.url)
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




class deleteDhcpDbAgentIDL_result(object):
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
        oprot.writeStructBegin('deleteDhcpDbAgentIDL_result')
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




class setDhcpExclusionIDL_args(object):
    """
    Attributes:
     - sessionId
     - vrfName
     - exclude
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionId',
      None,
      None),
     (2,
      TType.STRING,
      'vrfName',
      None,
      None),
     (3,
      TType.STRUCT,
      'exclude',
      (DhcpExclusionIDL, DhcpExclusionIDL.thrift_spec),
      None))

    def __init__(self, sessionId = None, vrfName = None, exclude = None):
        self.sessionId = sessionId
        self.vrfName = vrfName
        self.exclude = exclude



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
                    self.sessionId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.vrfName = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRUCT:
                    self.exclude = DhcpExclusionIDL()
                    self.exclude.read(iprot)
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
        oprot.writeStructBegin('setDhcpExclusionIDL_args')
        if self.sessionId != None:
            oprot.writeFieldBegin('sessionId', TType.I32, 1)
            oprot.writeI32(self.sessionId)
            oprot.writeFieldEnd()
        if self.vrfName != None:
            oprot.writeFieldBegin('vrfName', TType.STRING, 2)
            oprot.writeString(self.vrfName)
            oprot.writeFieldEnd()
        if self.exclude != None:
            oprot.writeFieldBegin('exclude', TType.STRUCT, 3)
            self.exclude.write(oprot)
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




class setDhcpExclusionIDL_result(object):
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
        oprot.writeStructBegin('setDhcpExclusionIDL_result')
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




class getDhcpExclusionIDL_args(object):
    """
    Attributes:
     - sessionId
     - vrfName
    """

    thrift_spec = (None, (1,
      TType.I32,
      'sessionId',
      None,
      None), (2,
      TType.STRING,
      'vrfName',
      None,
      None))

    def __init__(self, sessionId = None, vrfName = None):
        self.sessionId = sessionId
        self.vrfName = vrfName



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
                    self.sessionId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.vrfName = iprot.readString()
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
        oprot.writeStructBegin('getDhcpExclusionIDL_args')
        if self.sessionId != None:
            oprot.writeFieldBegin('sessionId', TType.I32, 1)
            oprot.writeI32(self.sessionId)
            oprot.writeFieldEnd()
        if self.vrfName != None:
            oprot.writeFieldBegin('vrfName', TType.STRING, 2)
            oprot.writeString(self.vrfName)
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




class getDhcpExclusionIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.LIST,
      'success',
      (TType.STRUCT, (DhcpExclusionIDL, DhcpExclusionIDL.thrift_spec)),
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
                        _elem19 = DhcpExclusionIDL()
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
        oprot.writeStructBegin('getDhcpExclusionIDL_result')
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




class deleteDhcpExclusionIDL_args(object):
    """
    Attributes:
     - sessionId
     - vrfName
     - exclude
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionId',
      None,
      None),
     (2,
      TType.STRING,
      'vrfName',
      None,
      None),
     (3,
      TType.STRUCT,
      'exclude',
      (DhcpExclusionIDL, DhcpExclusionIDL.thrift_spec),
      None))

    def __init__(self, sessionId = None, vrfName = None, exclude = None):
        self.sessionId = sessionId
        self.vrfName = vrfName
        self.exclude = exclude



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
                    self.sessionId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.vrfName = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRUCT:
                    self.exclude = DhcpExclusionIDL()
                    self.exclude.read(iprot)
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
        oprot.writeStructBegin('deleteDhcpExclusionIDL_args')
        if self.sessionId != None:
            oprot.writeFieldBegin('sessionId', TType.I32, 1)
            oprot.writeI32(self.sessionId)
            oprot.writeFieldEnd()
        if self.vrfName != None:
            oprot.writeFieldBegin('vrfName', TType.STRING, 2)
            oprot.writeString(self.vrfName)
            oprot.writeFieldEnd()
        if self.exclude != None:
            oprot.writeFieldBegin('exclude', TType.STRUCT, 3)
            self.exclude.write(oprot)
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




class deleteDhcpExclusionIDL_result(object):
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
        oprot.writeStructBegin('deleteDhcpExclusionIDL_result')
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




class setDhcpLeaseIDL_args(object):
    """
    Attributes:
     - sessionId
     - poolName
     - infinite
     - lease
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionId',
      None,
      None),
     (2,
      TType.STRING,
      'poolName',
      None,
      None),
     (3,
      TType.I32,
      'infinite',
      None,
      None),
     (4,
      TType.STRUCT,
      'lease',
      (Shared.ttypes.DateTimeIDL, Shared.ttypes.DateTimeIDL.thrift_spec),
      None))

    def __init__(self, sessionId = None, poolName = None, infinite = None, lease = None):
        self.sessionId = sessionId
        self.poolName = poolName
        self.infinite = infinite
        self.lease = lease



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
                    self.sessionId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.poolName = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.infinite = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRUCT:
                    self.lease = Shared.ttypes.DateTimeIDL()
                    self.lease.read(iprot)
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
        oprot.writeStructBegin('setDhcpLeaseIDL_args')
        if self.sessionId != None:
            oprot.writeFieldBegin('sessionId', TType.I32, 1)
            oprot.writeI32(self.sessionId)
            oprot.writeFieldEnd()
        if self.poolName != None:
            oprot.writeFieldBegin('poolName', TType.STRING, 2)
            oprot.writeString(self.poolName)
            oprot.writeFieldEnd()
        if self.infinite != None:
            oprot.writeFieldBegin('infinite', TType.I32, 3)
            oprot.writeI32(self.infinite)
            oprot.writeFieldEnd()
        if self.lease != None:
            oprot.writeFieldBegin('lease', TType.STRUCT, 4)
            self.lease.write(oprot)
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




class setDhcpLeaseIDL_result(object):
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
        oprot.writeStructBegin('setDhcpLeaseIDL_result')
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




class getDhcpLeaseIDL_args(object):
    """
    Attributes:
     - sessionId
     - poolName
    """

    thrift_spec = (None, (1,
      TType.I32,
      'sessionId',
      None,
      None), (2,
      TType.STRING,
      'poolName',
      None,
      None))

    def __init__(self, sessionId = None, poolName = None):
        self.sessionId = sessionId
        self.poolName = poolName



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
                    self.sessionId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.poolName = iprot.readString()
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
        oprot.writeStructBegin('getDhcpLeaseIDL_args')
        if self.sessionId != None:
            oprot.writeFieldBegin('sessionId', TType.I32, 1)
            oprot.writeI32(self.sessionId)
            oprot.writeFieldEnd()
        if self.poolName != None:
            oprot.writeFieldBegin('poolName', TType.STRING, 2)
            oprot.writeString(self.poolName)
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




class getDhcpLeaseIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.STRUCT,
      'success',
      (Shared.ttypes.DateTimeIDL, Shared.ttypes.DateTimeIDL.thrift_spec),
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
                    self.success = Shared.ttypes.DateTimeIDL()
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
        oprot.writeStructBegin('getDhcpLeaseIDL_result')
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




class addDeleteDhcpServerOptionIDL_args(object):
    """
    Attributes:
     - sessionId
     - poolName
     - ipList
     - option
     - action
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionId',
      None,
      None),
     (2,
      TType.STRING,
      'poolName',
      None,
      None),
     (3,
      TType.LIST,
      'ipList',
      (TType.STRUCT, (Shared.ttypes.NetworkAddressIDL, Shared.ttypes.NetworkAddressIDL.thrift_spec)),
      None),
     (4,
      TType.I32,
      'option',
      None,
      None),
     (5,
      TType.I32,
      'action',
      None,
      None))

    def __init__(self, sessionId = None, poolName = None, ipList = None, option = None, action = None):
        self.sessionId = sessionId
        self.poolName = poolName
        self.ipList = ipList
        self.option = option
        self.action = action



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
                    self.sessionId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.poolName = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.LIST:
                    self.ipList = []
                    (_etype24, _size21,) = iprot.readListBegin()
                    for _i25 in xrange(_size21):
                        _elem26 = Shared.ttypes.NetworkAddressIDL()
                        _elem26.read(iprot)
                        self.ipList.append(_elem26)

                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.option = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.action = iprot.readI32()
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
        oprot.writeStructBegin('addDeleteDhcpServerOptionIDL_args')
        if self.sessionId != None:
            oprot.writeFieldBegin('sessionId', TType.I32, 1)
            oprot.writeI32(self.sessionId)
            oprot.writeFieldEnd()
        if self.poolName != None:
            oprot.writeFieldBegin('poolName', TType.STRING, 2)
            oprot.writeString(self.poolName)
            oprot.writeFieldEnd()
        if self.ipList != None:
            oprot.writeFieldBegin('ipList', TType.LIST, 3)
            oprot.writeListBegin(TType.STRUCT, len(self.ipList))
            for iter27 in self.ipList:
                iter27.write(oprot)

            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.option != None:
            oprot.writeFieldBegin('option', TType.I32, 4)
            oprot.writeI32(self.option)
            oprot.writeFieldEnd()
        if self.action != None:
            oprot.writeFieldBegin('action', TType.I32, 5)
            oprot.writeI32(self.action)
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




class addDeleteDhcpServerOptionIDL_result(object):
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
        oprot.writeStructBegin('addDeleteDhcpServerOptionIDL_result')
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




class getDhcpServerOptionIDL_args(object):
    """
    Attributes:
     - sessionId
     - poolName
     - option
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionId',
      None,
      None),
     (2,
      TType.STRING,
      'poolName',
      None,
      None),
     (3,
      TType.I32,
      'option',
      None,
      None))

    def __init__(self, sessionId = None, poolName = None, option = None):
        self.sessionId = sessionId
        self.poolName = poolName
        self.option = option



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
                    self.sessionId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.poolName = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.option = iprot.readI32()
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
        oprot.writeStructBegin('getDhcpServerOptionIDL_args')
        if self.sessionId != None:
            oprot.writeFieldBegin('sessionId', TType.I32, 1)
            oprot.writeI32(self.sessionId)
            oprot.writeFieldEnd()
        if self.poolName != None:
            oprot.writeFieldBegin('poolName', TType.STRING, 2)
            oprot.writeString(self.poolName)
            oprot.writeFieldEnd()
        if self.option != None:
            oprot.writeFieldBegin('option', TType.I32, 3)
            oprot.writeI32(self.option)
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




class getDhcpServerOptionIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.LIST,
      'success',
      (TType.STRUCT, (Shared.ttypes.NetworkAddressIDL, Shared.ttypes.NetworkAddressIDL.thrift_spec)),
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
                    (_etype31, _size28,) = iprot.readListBegin()
                    for _i32 in xrange(_size28):
                        _elem33 = Shared.ttypes.NetworkAddressIDL()
                        _elem33.read(iprot)
                        self.success.append(_elem33)

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
        oprot.writeStructBegin('getDhcpServerOptionIDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.STRUCT, len(self.success))
            for iter34 in self.success:
                iter34.write(oprot)

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




class addDeleteDhcpNetbiosNodeIDL_args(object):
    """
    Attributes:
     - sessionId
     - poolName
     - type
     - action
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionId',
      None,
      None),
     (2,
      TType.STRING,
      'poolName',
      None,
      None),
     (3,
      TType.I32,
      'type',
      None,
      None),
     (4,
      TType.I32,
      'action',
      None,
      None))

    def __init__(self, sessionId = None, poolName = None, type = None, action = None):
        self.sessionId = sessionId
        self.poolName = poolName
        self.type = type
        self.action = action



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
                    self.sessionId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.poolName = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.action = iprot.readI32()
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
        oprot.writeStructBegin('addDeleteDhcpNetbiosNodeIDL_args')
        if self.sessionId != None:
            oprot.writeFieldBegin('sessionId', TType.I32, 1)
            oprot.writeI32(self.sessionId)
            oprot.writeFieldEnd()
        if self.poolName != None:
            oprot.writeFieldBegin('poolName', TType.STRING, 2)
            oprot.writeString(self.poolName)
            oprot.writeFieldEnd()
        if self.type != None:
            oprot.writeFieldBegin('type', TType.I32, 3)
            oprot.writeI32(self.type)
            oprot.writeFieldEnd()
        if self.action != None:
            oprot.writeFieldBegin('action', TType.I32, 4)
            oprot.writeI32(self.action)
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




class addDeleteDhcpNetbiosNodeIDL_result(object):
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
        oprot.writeStructBegin('addDeleteDhcpNetbiosNodeIDL_result')
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




class getDhcpNetbiosNodeIDL_args(object):
    """
    Attributes:
     - sessionId
     - poolName
    """

    thrift_spec = (None, (1,
      TType.I32,
      'sessionId',
      None,
      None), (2,
      TType.STRING,
      'poolName',
      None,
      None))

    def __init__(self, sessionId = None, poolName = None):
        self.sessionId = sessionId
        self.poolName = poolName



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
                    self.sessionId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.poolName = iprot.readString()
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
        oprot.writeStructBegin('getDhcpNetbiosNodeIDL_args')
        if self.sessionId != None:
            oprot.writeFieldBegin('sessionId', TType.I32, 1)
            oprot.writeI32(self.sessionId)
            oprot.writeFieldEnd()
        if self.poolName != None:
            oprot.writeFieldBegin('poolName', TType.STRING, 2)
            oprot.writeString(self.poolName)
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




class getDhcpNetbiosNodeIDL_result(object):
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
        oprot.writeStructBegin('getDhcpNetbiosNodeIDL_result')
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




class addDeleteDhcpPoolDomainIDL_args(object):
    """
    Attributes:
     - sessionId
     - poolName
     - domainName
     - action
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionId',
      None,
      None),
     (2,
      TType.STRING,
      'poolName',
      None,
      None),
     (3,
      TType.STRING,
      'domainName',
      None,
      None),
     (4,
      TType.I32,
      'action',
      None,
      None))

    def __init__(self, sessionId = None, poolName = None, domainName = None, action = None):
        self.sessionId = sessionId
        self.poolName = poolName
        self.domainName = domainName
        self.action = action



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
                    self.sessionId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.poolName = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.domainName = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.action = iprot.readI32()
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
        oprot.writeStructBegin('addDeleteDhcpPoolDomainIDL_args')
        if self.sessionId != None:
            oprot.writeFieldBegin('sessionId', TType.I32, 1)
            oprot.writeI32(self.sessionId)
            oprot.writeFieldEnd()
        if self.poolName != None:
            oprot.writeFieldBegin('poolName', TType.STRING, 2)
            oprot.writeString(self.poolName)
            oprot.writeFieldEnd()
        if self.domainName != None:
            oprot.writeFieldBegin('domainName', TType.STRING, 3)
            oprot.writeString(self.domainName)
            oprot.writeFieldEnd()
        if self.action != None:
            oprot.writeFieldBegin('action', TType.I32, 4)
            oprot.writeI32(self.action)
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




class addDeleteDhcpPoolDomainIDL_result(object):
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
        oprot.writeStructBegin('addDeleteDhcpPoolDomainIDL_result')
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




class getDhcpPoolDomainIDL_args(object):
    """
    Attributes:
     - sessionId
     - poolName
    """

    thrift_spec = (None, (1,
      TType.I32,
      'sessionId',
      None,
      None), (2,
      TType.STRING,
      'poolName',
      None,
      None))

    def __init__(self, sessionId = None, poolName = None):
        self.sessionId = sessionId
        self.poolName = poolName



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
                    self.sessionId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.poolName = iprot.readString()
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
        oprot.writeStructBegin('getDhcpPoolDomainIDL_args')
        if self.sessionId != None:
            oprot.writeFieldBegin('sessionId', TType.I32, 1)
            oprot.writeI32(self.sessionId)
            oprot.writeFieldEnd()
        if self.poolName != None:
            oprot.writeFieldBegin('poolName', TType.STRING, 2)
            oprot.writeString(self.poolName)
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




class getDhcpPoolDomainIDL_result(object):
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
        oprot.writeStructBegin('getDhcpPoolDomainIDL_result')
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




class addDeleteDhcpPoolHostIDL_args(object):
    """
    Attributes:
     - sessionId
     - poolName
     - prefix
     - action
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionId',
      None,
      None),
     (2,
      TType.STRING,
      'poolName',
      None,
      None),
     (3,
      TType.STRUCT,
      'prefix',
      (Shared.ttypes.NetworkPrefixIDL, Shared.ttypes.NetworkPrefixIDL.thrift_spec),
      None),
     (4,
      TType.I32,
      'action',
      None,
      None))

    def __init__(self, sessionId = None, poolName = None, prefix = None, action = None):
        self.sessionId = sessionId
        self.poolName = poolName
        self.prefix = prefix
        self.action = action



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
                    self.sessionId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.poolName = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRUCT:
                    self.prefix = Shared.ttypes.NetworkPrefixIDL()
                    self.prefix.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.action = iprot.readI32()
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
        oprot.writeStructBegin('addDeleteDhcpPoolHostIDL_args')
        if self.sessionId != None:
            oprot.writeFieldBegin('sessionId', TType.I32, 1)
            oprot.writeI32(self.sessionId)
            oprot.writeFieldEnd()
        if self.poolName != None:
            oprot.writeFieldBegin('poolName', TType.STRING, 2)
            oprot.writeString(self.poolName)
            oprot.writeFieldEnd()
        if self.prefix != None:
            oprot.writeFieldBegin('prefix', TType.STRUCT, 3)
            self.prefix.write(oprot)
            oprot.writeFieldEnd()
        if self.action != None:
            oprot.writeFieldBegin('action', TType.I32, 4)
            oprot.writeI32(self.action)
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




class addDeleteDhcpPoolHostIDL_result(object):
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
        oprot.writeStructBegin('addDeleteDhcpPoolHostIDL_result')
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




class getDhcpPoolHostIDL_args(object):
    """
    Attributes:
     - sessionId
     - poolName
    """

    thrift_spec = (None, (1,
      TType.I32,
      'sessionId',
      None,
      None), (2,
      TType.STRING,
      'poolName',
      None,
      None))

    def __init__(self, sessionId = None, poolName = None):
        self.sessionId = sessionId
        self.poolName = poolName



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
                    self.sessionId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.poolName = iprot.readString()
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
        oprot.writeStructBegin('getDhcpPoolHostIDL_args')
        if self.sessionId != None:
            oprot.writeFieldBegin('sessionId', TType.I32, 1)
            oprot.writeI32(self.sessionId)
            oprot.writeFieldEnd()
        if self.poolName != None:
            oprot.writeFieldBegin('poolName', TType.STRING, 2)
            oprot.writeString(self.poolName)
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




class getDhcpPoolHostIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.STRUCT,
      'success',
      (Shared.ttypes.NetworkPrefixIDL, Shared.ttypes.NetworkPrefixIDL.thrift_spec),
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
                    self.success = Shared.ttypes.NetworkPrefixIDL()
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
        oprot.writeStructBegin('getDhcpPoolHostIDL_result')
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




class addDeleteDhcpPoolNetworkIDL_args(object):
    """
    Attributes:
     - sessionId
     - poolName
     - network
     - nwType
     - action
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionId',
      None,
      None),
     (2,
      TType.STRING,
      'poolName',
      None,
      None),
     (3,
      TType.STRUCT,
      'network',
      (Shared.ttypes.NetworkPrefixIDL, Shared.ttypes.NetworkPrefixIDL.thrift_spec),
      None),
     (4,
      TType.I32,
      'nwType',
      None,
      None),
     (5,
      TType.I32,
      'action',
      None,
      None))

    def __init__(self, sessionId = None, poolName = None, network = None, nwType = None, action = None):
        self.sessionId = sessionId
        self.poolName = poolName
        self.network = network
        self.nwType = nwType
        self.action = action



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
                    self.sessionId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.poolName = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRUCT:
                    self.network = Shared.ttypes.NetworkPrefixIDL()
                    self.network.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.nwType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.action = iprot.readI32()
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
        oprot.writeStructBegin('addDeleteDhcpPoolNetworkIDL_args')
        if self.sessionId != None:
            oprot.writeFieldBegin('sessionId', TType.I32, 1)
            oprot.writeI32(self.sessionId)
            oprot.writeFieldEnd()
        if self.poolName != None:
            oprot.writeFieldBegin('poolName', TType.STRING, 2)
            oprot.writeString(self.poolName)
            oprot.writeFieldEnd()
        if self.network != None:
            oprot.writeFieldBegin('network', TType.STRUCT, 3)
            self.network.write(oprot)
            oprot.writeFieldEnd()
        if self.nwType != None:
            oprot.writeFieldBegin('nwType', TType.I32, 4)
            oprot.writeI32(self.nwType)
            oprot.writeFieldEnd()
        if self.action != None:
            oprot.writeFieldBegin('action', TType.I32, 5)
            oprot.writeI32(self.action)
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




class addDeleteDhcpPoolNetworkIDL_result(object):
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
        oprot.writeStructBegin('addDeleteDhcpPoolNetworkIDL_result')
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




class getDhcpPoolNetworkIDL_args(object):
    """
    Attributes:
     - sessionId
     - poolName
    """

    thrift_spec = (None, (1,
      TType.I32,
      'sessionId',
      None,
      None), (2,
      TType.STRING,
      'poolName',
      None,
      None))

    def __init__(self, sessionId = None, poolName = None):
        self.sessionId = sessionId
        self.poolName = poolName



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
                    self.sessionId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.poolName = iprot.readString()
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
        oprot.writeStructBegin('getDhcpPoolNetworkIDL_args')
        if self.sessionId != None:
            oprot.writeFieldBegin('sessionId', TType.I32, 1)
            oprot.writeI32(self.sessionId)
            oprot.writeFieldEnd()
        if self.poolName != None:
            oprot.writeFieldBegin('poolName', TType.STRING, 2)
            oprot.writeString(self.poolName)
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




class getDhcpPoolNetworkIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.LIST,
      'success',
      (TType.STRUCT, (DhcpNwNodeIDL, DhcpNwNodeIDL.thrift_spec)),
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
                        _elem40 = DhcpNwNodeIDL()
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
        oprot.writeStructBegin('getDhcpPoolNetworkIDL_result')
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




class addDeleteDhcpPoolClientNameIDL_args(object):
    """
    Attributes:
     - sessionId
     - poolName
     - clientName
     - action
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionId',
      None,
      None),
     (2,
      TType.STRING,
      'poolName',
      None,
      None),
     (3,
      TType.STRING,
      'clientName',
      None,
      None),
     (4,
      TType.I32,
      'action',
      None,
      None))

    def __init__(self, sessionId = None, poolName = None, clientName = None, action = None):
        self.sessionId = sessionId
        self.poolName = poolName
        self.clientName = clientName
        self.action = action



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
                    self.sessionId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.poolName = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.clientName = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.action = iprot.readI32()
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
        oprot.writeStructBegin('addDeleteDhcpPoolClientNameIDL_args')
        if self.sessionId != None:
            oprot.writeFieldBegin('sessionId', TType.I32, 1)
            oprot.writeI32(self.sessionId)
            oprot.writeFieldEnd()
        if self.poolName != None:
            oprot.writeFieldBegin('poolName', TType.STRING, 2)
            oprot.writeString(self.poolName)
            oprot.writeFieldEnd()
        if self.clientName != None:
            oprot.writeFieldBegin('clientName', TType.STRING, 3)
            oprot.writeString(self.clientName)
            oprot.writeFieldEnd()
        if self.action != None:
            oprot.writeFieldBegin('action', TType.I32, 4)
            oprot.writeI32(self.action)
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




class addDeleteDhcpPoolClientNameIDL_result(object):
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
        oprot.writeStructBegin('addDeleteDhcpPoolClientNameIDL_result')
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




class getDhcpPoolClientNameIDL_args(object):
    """
    Attributes:
     - sessionId
     - poolName
    """

    thrift_spec = (None, (1,
      TType.I32,
      'sessionId',
      None,
      None), (2,
      TType.STRING,
      'poolName',
      None,
      None))

    def __init__(self, sessionId = None, poolName = None):
        self.sessionId = sessionId
        self.poolName = poolName



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
                    self.sessionId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.poolName = iprot.readString()
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
        oprot.writeStructBegin('getDhcpPoolClientNameIDL_args')
        if self.sessionId != None:
            oprot.writeFieldBegin('sessionId', TType.I32, 1)
            oprot.writeI32(self.sessionId)
            oprot.writeFieldEnd()
        if self.poolName != None:
            oprot.writeFieldBegin('poolName', TType.STRING, 2)
            oprot.writeString(self.poolName)
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




class getDhcpPoolClientNameIDL_result(object):
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
        oprot.writeStructBegin('getDhcpPoolClientNameIDL_result')
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




class addDeleteDhcpPoolHwAddrIDL_args(object):
    """
    Attributes:
     - sessionId
     - poolName
     - hwAddr
     - action
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionId',
      None,
      None),
     (2,
      TType.STRING,
      'poolName',
      None,
      None),
     (3,
      TType.STRING,
      'hwAddr',
      None,
      None),
     (4,
      TType.I32,
      'action',
      None,
      None))

    def __init__(self, sessionId = None, poolName = None, hwAddr = None, action = None):
        self.sessionId = sessionId
        self.poolName = poolName
        self.hwAddr = hwAddr
        self.action = action



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
                    self.sessionId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.poolName = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.hwAddr = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.action = iprot.readI32()
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
        oprot.writeStructBegin('addDeleteDhcpPoolHwAddrIDL_args')
        if self.sessionId != None:
            oprot.writeFieldBegin('sessionId', TType.I32, 1)
            oprot.writeI32(self.sessionId)
            oprot.writeFieldEnd()
        if self.poolName != None:
            oprot.writeFieldBegin('poolName', TType.STRING, 2)
            oprot.writeString(self.poolName)
            oprot.writeFieldEnd()
        if self.hwAddr != None:
            oprot.writeFieldBegin('hwAddr', TType.STRING, 3)
            oprot.writeString(self.hwAddr)
            oprot.writeFieldEnd()
        if self.action != None:
            oprot.writeFieldBegin('action', TType.I32, 4)
            oprot.writeI32(self.action)
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




class addDeleteDhcpPoolHwAddrIDL_result(object):
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
        oprot.writeStructBegin('addDeleteDhcpPoolHwAddrIDL_result')
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




class getDhcpPoolHwAddrIDL_args(object):
    """
    Attributes:
     - sessionId
     - poolName
    """

    thrift_spec = (None, (1,
      TType.I32,
      'sessionId',
      None,
      None), (2,
      TType.STRING,
      'poolName',
      None,
      None))

    def __init__(self, sessionId = None, poolName = None):
        self.sessionId = sessionId
        self.poolName = poolName



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
                    self.sessionId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.poolName = iprot.readString()
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
        oprot.writeStructBegin('getDhcpPoolHwAddrIDL_args')
        if self.sessionId != None:
            oprot.writeFieldBegin('sessionId', TType.I32, 1)
            oprot.writeI32(self.sessionId)
            oprot.writeFieldEnd()
        if self.poolName != None:
            oprot.writeFieldBegin('poolName', TType.STRING, 2)
            oprot.writeString(self.poolName)
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




class getDhcpPoolHwAddrIDL_result(object):
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
        oprot.writeStructBegin('getDhcpPoolHwAddrIDL_result')
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




class setUnsetDhcpConflictLoggingIDL_args(object):
    """
    Attributes:
     - sessionId
     - action
    """

    thrift_spec = (None, (1,
      TType.I32,
      'sessionId',
      None,
      None), (2,
      TType.I32,
      'action',
      None,
      None))

    def __init__(self, sessionId = None, action = None):
        self.sessionId = sessionId
        self.action = action



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
                    self.sessionId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.action = iprot.readI32()
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
        oprot.writeStructBegin('setUnsetDhcpConflictLoggingIDL_args')
        if self.sessionId != None:
            oprot.writeFieldBegin('sessionId', TType.I32, 1)
            oprot.writeI32(self.sessionId)
            oprot.writeFieldEnd()
        if self.action != None:
            oprot.writeFieldBegin('action', TType.I32, 2)
            oprot.writeI32(self.action)
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




class setUnsetDhcpConflictLoggingIDL_result(object):
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
        oprot.writeStructBegin('setUnsetDhcpConflictLoggingIDL_result')
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




class getDHCPBindingListIDL_args(object):
    """
    Attributes:
     - vrfName
     - addr
     - maxCount
    """

    thrift_spec = (None,
     (1,
      TType.STRING,
      'vrfName',
      None,
      None),
     (2,
      TType.STRUCT,
      'addr',
      (Shared.ttypes.NetworkAddressIDL, Shared.ttypes.NetworkAddressIDL.thrift_spec),
      None),
     (3,
      TType.I32,
      'maxCount',
      None,
      None))

    def __init__(self, vrfName = None, addr = None, maxCount = None):
        self.vrfName = vrfName
        self.addr = addr
        self.maxCount = maxCount



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
                    self.vrfName = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.addr = Shared.ttypes.NetworkAddressIDL()
                    self.addr.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.maxCount = iprot.readI32()
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
        oprot.writeStructBegin('getDHCPBindingListIDL_args')
        if self.vrfName != None:
            oprot.writeFieldBegin('vrfName', TType.STRING, 1)
            oprot.writeString(self.vrfName)
            oprot.writeFieldEnd()
        if self.addr != None:
            oprot.writeFieldBegin('addr', TType.STRUCT, 2)
            self.addr.write(oprot)
            oprot.writeFieldEnd()
        if self.maxCount != None:
            oprot.writeFieldBegin('maxCount', TType.I32, 3)
            oprot.writeI32(self.maxCount)
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




class getDHCPBindingListIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.LIST,
      'success',
      (TType.STRUCT, (DhcpBindParamIDL, DhcpBindParamIDL.thrift_spec)),
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
                    (_etype45, _size42,) = iprot.readListBegin()
                    for _i46 in xrange(_size42):
                        _elem47 = DhcpBindParamIDL()
                        _elem47.read(iprot)
                        self.success.append(_elem47)

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
        oprot.writeStructBegin('getDHCPBindingListIDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.STRUCT, len(self.success))
            for iter48 in self.success:
                iter48.write(oprot)

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




class getDHCPBindingByIpAddrIDL_args(object):
    """
    Attributes:
     - vrfName
     - addr
    """

    thrift_spec = (None, (1,
      TType.STRING,
      'vrfName',
      None,
      None), (2,
      TType.STRUCT,
      'addr',
      (Shared.ttypes.NetworkAddressIDL, Shared.ttypes.NetworkAddressIDL.thrift_spec),
      None))

    def __init__(self, vrfName = None, addr = None):
        self.vrfName = vrfName
        self.addr = addr



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
                    self.vrfName = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.addr = Shared.ttypes.NetworkAddressIDL()
                    self.addr.read(iprot)
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
        oprot.writeStructBegin('getDHCPBindingByIpAddrIDL_args')
        if self.vrfName != None:
            oprot.writeFieldBegin('vrfName', TType.STRING, 1)
            oprot.writeString(self.vrfName)
            oprot.writeFieldEnd()
        if self.addr != None:
            oprot.writeFieldBegin('addr', TType.STRUCT, 2)
            self.addr.write(oprot)
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




class getDHCPBindingByIpAddrIDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.STRUCT,
      'success',
      (DhcpBindParamIDL, DhcpBindParamIDL.thrift_spec),
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
                    self.success = DhcpBindParamIDL()
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
        oprot.writeStructBegin('getDHCPBindingByIpAddrIDL_result')
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




class deleteDhcpAllBindingsIDL_args(object):
    """
    Attributes:
     - sessionId
     - vrf
    """

    thrift_spec = (None, (1,
      TType.I32,
      'sessionId',
      None,
      None), (2,
      TType.STRING,
      'vrf',
      None,
      None))

    def __init__(self, sessionId = None, vrf = None):
        self.sessionId = sessionId
        self.vrf = vrf



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
                    self.sessionId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.vrf = iprot.readString()
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
        oprot.writeStructBegin('deleteDhcpAllBindingsIDL_args')
        if self.sessionId != None:
            oprot.writeFieldBegin('sessionId', TType.I32, 1)
            oprot.writeI32(self.sessionId)
            oprot.writeFieldEnd()
        if self.vrf != None:
            oprot.writeFieldBegin('vrf', TType.STRING, 2)
            oprot.writeString(self.vrf)
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




class deleteDhcpAllBindingsIDL_result(object):
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
        oprot.writeStructBegin('deleteDhcpAllBindingsIDL_result')
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
# 2015.02.05 17:18:14 IST
