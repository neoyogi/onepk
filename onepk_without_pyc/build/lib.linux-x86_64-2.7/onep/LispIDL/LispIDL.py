# 2015.02.05 17:18:32 IST
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

    def createLisp_IDL(self, lispHandle, vrf):
        """
            Create a LISP Top object
        
            Parameters:
             - lispHandle
             - vrf
            """
        pass



    def deleteLisp_IDL(self, lispHandle):
        """
            Delete a LISP Top object
        
            Parameters:
             - lispHandle
            """
        pass



    def enableMapServer_IDL(self, lispHandle, addrFamily):
        """
            Enable a Map-server
        
            Parameters:
             - lispHandle
             - addrFamily
            """
        pass



    def disableMapServer_IDL(self, lispHandle, addrFamily):
        """
            Disable a Map-server
        
            Parameters:
             - lispHandle
             - addrFamily
            """
        pass



    def createSite_IDL(self, lispHandle, siteHandle):
        """
            Create a Site
        
            Parameters:
             - lispHandle
             - siteHandle
            """
        pass



    def deleteSite_IDL(self, lispHandle, siteHandle):
        """
            Delete a Site
        
            Parameters:
             - lispHandle
             - siteHandle
            """
        pass



    def enableMapResolver_IDL(self, lispHandle, addrFamily):
        """
            Enable a Map-resolver
        
            Parameters:
             - lispHandle
             - addrFamily
            """
        pass



    def disableMapResolver_IDL(self, lispHandle, addrFamily):
        """
            Disable a Map-resolver
        
            Parameters:
             - lispHandle
             - addrFamily
            """
        pass



    def createEidTable_IDL(self, lispHandle, eidInstanceId, vrf):
        """
            Create a EID table
        
            Parameters:
             - lispHandle
             - eidInstanceId
             - vrf
            """
        pass



    def deleteEidTable_IDL(self, lispHandle, eidInstanceId):
        """
            Delete an EID table
        
            Parameters:
             - lispHandle
             - eidInstanceId
            """
        pass



    def enableXtr_IDL(self, lispHandle, eidInstanceId, type, addrFamily):
        """
            Enable a P/xTR
        
            Parameters:
             - lispHandle
             - eidInstanceId
             - type
             - addrFamily
            """
        pass



    def disableXtr_IDL(self, lispHandle, eidInstanceId, type, addrFamily):
        """
            Disable a P/xTR
        
            Parameters:
             - lispHandle
             - eidInstanceId
             - type
             - addrFamily
            """
        pass



    def enablePitr_IDL(self, lispHandle, eidInstanceId, addrFamily, address):
        """
            Enable a PITR
        
            Parameters:
             - lispHandle
             - eidInstanceId
             - addrFamily
             - address
            """
        pass



    def addItrMapResolver_IDL(self, lispHandle, eidInstanceId, eidAF, addressAF, address):
        """
            Add Map Server to an ITR
        
            Parameters:
             - lispHandle
             - eidInstanceId
             - eidAF
             - addressAF
             - address
            """
        pass



    def removeItrMapResolver_IDL(self, lispHandle, eidInstanceId, eidAF, addressAF, address):
        """
            Remove Map Server from an ITR
        
            Parameters:
             - lispHandle
             - eidInstanceId
             - eidAF
             - addressAF
             - address
            """
        pass



    def addEtrMapServer_IDL(self, lispHandle, eidInstanceId, eidAF, addressAF, address, key):
        """
            Add Map Server to an ETR
        
            Parameters:
             - lispHandle
             - eidInstanceId
             - eidAF
             - addressAF
             - address
             - key
            """
        pass



    def removeEtrMapServer_IDL(self, lispHandle, eidInstanceId, eidAF, addressAF, address):
        """
            Remove Map Server from an ETR
        
            Parameters:
             - lispHandle
             - eidInstanceId
             - eidAF
             - addressAF
             - address
            """
        pass



    def addLocalPrefix_IDL(self, lispHandle, eidInstanceId, prefixAF, prefix, prefixLen):
        """
            Add Local EID Prefix
        
            Parameters:
             - lispHandle
             - eidInstanceId
             - prefixAF
             - prefix
             - prefixLen
            """
        pass



    def removeLocalPrefix_IDL(self, lispHandle, eidInstanceId, prefixAF, prefix, prefixLen):
        """
            Remove Local EID Prefix
        
            Parameters:
             - lispHandle
             - eidInstanceId
             - prefixAF
             - prefix
             - prefixLen
            """
        pass



    def addLocalPrefixRlocMap_IDL(self, lispHandle, eidInstanceId, prefixAF, prefix, prefixLen, localRlocs):
        """
            Add Local EID Prefix-RLOC Database-mapping
        
            Parameters:
             - lispHandle
             - eidInstanceId
             - prefixAF
             - prefix
             - prefixLen
             - localRlocs
            """
        pass



    def removeLocalPrefixRlocMap_IDL(self, lispHandle, eidInstanceId, prefixAF, prefix, prefixLen, rlocAF, rloc):
        """
            Remove Local EID Prefix-RLOC Database-mapping
        
            Parameters:
             - lispHandle
             - eidInstanceId
             - prefixAF
             - prefix
             - prefixLen
             - rlocAF
             - rloc
            """
        pass



    def addLocalPrefixIfcMap_IDL(self, lispHandle, eidInstanceId, prefixAF, prefix, prefixLen, ifHandle, addrFamily, priority, weight):
        """
            Add Local EID Prefix-Interface Database-mapping
        
            Parameters:
             - lispHandle
             - eidInstanceId
             - prefixAF
             - prefix
             - prefixLen
             - ifHandle
             - addrFamily
             - priority
             - weight
            """
        pass



    def removeLocalPrefixIfcMap_IDL(self, lispHandle, eidInstanceId, prefixAF, prefix, prefixLen, ifHandle, addrFamily):
        """
            Remove Local EID Prefix-Interface Database-mapping
        
            Parameters:
             - lispHandle
             - eidInstanceId
             - prefixAF
             - prefix
             - prefixLen
             - ifHandle
             - addrFamily
            """
        pass



    def addRemotePrefix_IDL(self, lispHandle, eidInstanceId, prefixAF, prefix, prefixLen):
        """
            Add Remote EID Prefix
        
            Parameters:
             - lispHandle
             - eidInstanceId
             - prefixAF
             - prefix
             - prefixLen
            """
        pass



    def removeRemotePrefix_IDL(self, lispHandle, eidInstanceId, prefixAF, prefix, prefixLen):
        """
            Remove Remote EID Prefix
        
            Parameters:
             - lispHandle
             - eidInstanceId
             - prefixAF
             - prefix
             - prefixLen
            """
        pass



    def addMapServerAddressToEtr_IDL(self, lispHandle, eidInstanceId, addrFamily, addr, key):
        """
            Add Map-server address to an ETR
        
            Parameters:
             - lispHandle
             - eidInstanceId
             - addrFamily
             - addr
             - key
            """
        pass



    def addRemotePrefixRlocMap_IDL(self, lispHandle, eidInstanceId, prefixAF, prefix, prefixLen, state, remoteRlocs):
        """
            Add Remote EID Prefix-RLOC Database-mapping
        
            Parameters:
             - lispHandle
             - eidInstanceId
             - prefixAF
             - prefix
             - prefixLen
             - state
             - remoteRlocs
            """
        pass



    def removeRemotePrefixRlocMap_IDL(self, lispHandle, eidInstanceId, prefixAF, prefix, prefixLen, rlocAF, rloc):
        """
            Remove Remote EID Prefix-RLOC Database-mapping
        
            Parameters:
             - lispHandle
             - eidInstanceId
             - prefixAF
             - prefix
             - prefixLen
             - rlocAF
             - rloc
            """
        pass



    def addPrefixToSite_IDL(self, lispHandle, siteHandle, eidInstanceId, prefixAF, prefix, prefixLen):
        """
            Add Prefix to a Map-server Site
        
            Parameters:
             - lispHandle
             - siteHandle
             - eidInstanceId
             - prefixAF
             - prefix
             - prefixLen
            """
        pass



    def removePrefixFromSite_IDL(self, lispHandle, siteHandle, eidInstanceId, prefixAF, prefix, prefixLen):
        """
            Remove Prefix from a Map-server Site
        
            Parameters:
             - lispHandle
             - siteHandle
             - eidInstanceId
             - prefixAF
             - prefix
             - prefixLen
            """
        pass



    def setMapServerKey_IDL(self, lispHandle, siteHandle, key):
        """
            Set a Map-server Key
        
            Parameters:
             - lispHandle
             - siteHandle
             - key
            """
        pass



    def clearMapServerReg_IDL(self, lispHandle, siteHandle, eidInstanceId, prefixAF, prefix, prefixLen):
        """
            Clear Map-server Registration
        
            Parameters:
             - lispHandle
             - siteHandle
             - eidInstanceId
             - prefixAF
             - prefix
             - prefixLen
            """
        pass



    def clearMapCacheEntry_IDL(self, lispHandle, eidInstanceId, prefixAF, prefix, prefixLen):
        """
            Clear Map Cache Entry
        
            Parameters:
             - lispHandle
             - eidInstanceId
             - prefixAF
             - prefix
             - prefixLen
            """
        pass



    def findMapCacheEntry_IDL(self, lispHandle, eidInstanceId, prefixAF, prefix, prefixLen):
        """
            Find Map Cache Entry
        
            Parameters:
             - lispHandle
             - eidInstanceId
             - prefixAF
             - prefix
             - prefixLen
            """
        pass



    def findMapCacheLongestMatchEntry_IDL(self, lispHandle, eidInstanceId, addrAF, addr):
        """
            Find Longest in Map Cache
        
            Parameters:
             - lispHandle
             - eidInstanceId
             - addrAF
             - addr
            """
        pass



    def signalMapCache_IDL(self, lispHandle, eidInstanceId, addrAF, addr):
        """
            Signal
        
            Parameters:
             - lispHandle
             - eidInstanceId
             - addrAF
             - addr
            """
        pass



    def enableProbe_IDL(self, lispHandle, eidInstanceId):
        """
            Enable Probe
        
            Parameters:
             - lispHandle
             - eidInstanceId
            """
        pass



    def disableProbe_IDL(self, lispHandle, eidInstanceId):
        """
            Disable Probe
        
            Parameters:
             - lispHandle
             - eidInstanceId
            """
        pass




class Client(Iface):

    def __init__(self, iprot, oprot = None):
        self._iprot = self._oprot = iprot
        if oprot != None:
            self._oprot = oprot
        self._seqid = 0



    def createLisp_IDL(self, lispHandle, vrf):
        """
            Create a LISP Top object
        
            Parameters:
             - lispHandle
             - vrf
            """
        self._oprot.rlock.acquire()
        try:
            self.send_createLisp_IDL(lispHandle, vrf)
            result = self.recv_createLisp_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_createLisp_IDL(self, lispHandle, vrf):
        self._oprot.writeMessageBegin('createLisp_IDL', TMessageType.CALL, self._seqid)
        args = createLisp_IDL_args()
        args.lispHandle = lispHandle
        args.vrf = vrf
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_createLisp_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = createLisp_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'createLisp_IDL failed: unknown result')



    def deleteLisp_IDL(self, lispHandle):
        """
            Delete a LISP Top object
        
            Parameters:
             - lispHandle
            """
        self._oprot.rlock.acquire()
        try:
            self.send_deleteLisp_IDL(lispHandle)
            result = self.recv_deleteLisp_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_deleteLisp_IDL(self, lispHandle):
        self._oprot.writeMessageBegin('deleteLisp_IDL', TMessageType.CALL, self._seqid)
        args = deleteLisp_IDL_args()
        args.lispHandle = lispHandle
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_deleteLisp_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = deleteLisp_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'deleteLisp_IDL failed: unknown result')



    def enableMapServer_IDL(self, lispHandle, addrFamily):
        """
            Enable a Map-server
        
            Parameters:
             - lispHandle
             - addrFamily
            """
        self._oprot.rlock.acquire()
        try:
            self.send_enableMapServer_IDL(lispHandle, addrFamily)
            result = self.recv_enableMapServer_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_enableMapServer_IDL(self, lispHandle, addrFamily):
        self._oprot.writeMessageBegin('enableMapServer_IDL', TMessageType.CALL, self._seqid)
        args = enableMapServer_IDL_args()
        args.lispHandle = lispHandle
        args.addrFamily = addrFamily
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_enableMapServer_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = enableMapServer_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'enableMapServer_IDL failed: unknown result')



    def disableMapServer_IDL(self, lispHandle, addrFamily):
        """
            Disable a Map-server
        
            Parameters:
             - lispHandle
             - addrFamily
            """
        self._oprot.rlock.acquire()
        try:
            self.send_disableMapServer_IDL(lispHandle, addrFamily)
            result = self.recv_disableMapServer_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_disableMapServer_IDL(self, lispHandle, addrFamily):
        self._oprot.writeMessageBegin('disableMapServer_IDL', TMessageType.CALL, self._seqid)
        args = disableMapServer_IDL_args()
        args.lispHandle = lispHandle
        args.addrFamily = addrFamily
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_disableMapServer_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = disableMapServer_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'disableMapServer_IDL failed: unknown result')



    def createSite_IDL(self, lispHandle, siteHandle):
        """
            Create a Site
        
            Parameters:
             - lispHandle
             - siteHandle
            """
        self._oprot.rlock.acquire()
        try:
            self.send_createSite_IDL(lispHandle, siteHandle)
            result = self.recv_createSite_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_createSite_IDL(self, lispHandle, siteHandle):
        self._oprot.writeMessageBegin('createSite_IDL', TMessageType.CALL, self._seqid)
        args = createSite_IDL_args()
        args.lispHandle = lispHandle
        args.siteHandle = siteHandle
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_createSite_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = createSite_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'createSite_IDL failed: unknown result')



    def deleteSite_IDL(self, lispHandle, siteHandle):
        """
            Delete a Site
        
            Parameters:
             - lispHandle
             - siteHandle
            """
        self._oprot.rlock.acquire()
        try:
            self.send_deleteSite_IDL(lispHandle, siteHandle)
            result = self.recv_deleteSite_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_deleteSite_IDL(self, lispHandle, siteHandle):
        self._oprot.writeMessageBegin('deleteSite_IDL', TMessageType.CALL, self._seqid)
        args = deleteSite_IDL_args()
        args.lispHandle = lispHandle
        args.siteHandle = siteHandle
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_deleteSite_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = deleteSite_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'deleteSite_IDL failed: unknown result')



    def enableMapResolver_IDL(self, lispHandle, addrFamily):
        """
            Enable a Map-resolver
        
            Parameters:
             - lispHandle
             - addrFamily
            """
        self._oprot.rlock.acquire()
        try:
            self.send_enableMapResolver_IDL(lispHandle, addrFamily)
            result = self.recv_enableMapResolver_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_enableMapResolver_IDL(self, lispHandle, addrFamily):
        self._oprot.writeMessageBegin('enableMapResolver_IDL', TMessageType.CALL, self._seqid)
        args = enableMapResolver_IDL_args()
        args.lispHandle = lispHandle
        args.addrFamily = addrFamily
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_enableMapResolver_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = enableMapResolver_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'enableMapResolver_IDL failed: unknown result')



    def disableMapResolver_IDL(self, lispHandle, addrFamily):
        """
            Disable a Map-resolver
        
            Parameters:
             - lispHandle
             - addrFamily
            """
        self._oprot.rlock.acquire()
        try:
            self.send_disableMapResolver_IDL(lispHandle, addrFamily)
            result = self.recv_disableMapResolver_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_disableMapResolver_IDL(self, lispHandle, addrFamily):
        self._oprot.writeMessageBegin('disableMapResolver_IDL', TMessageType.CALL, self._seqid)
        args = disableMapResolver_IDL_args()
        args.lispHandle = lispHandle
        args.addrFamily = addrFamily
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_disableMapResolver_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = disableMapResolver_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'disableMapResolver_IDL failed: unknown result')



    def createEidTable_IDL(self, lispHandle, eidInstanceId, vrf):
        """
            Create a EID table
        
            Parameters:
             - lispHandle
             - eidInstanceId
             - vrf
            """
        self._oprot.rlock.acquire()
        try:
            self.send_createEidTable_IDL(lispHandle, eidInstanceId, vrf)
            result = self.recv_createEidTable_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_createEidTable_IDL(self, lispHandle, eidInstanceId, vrf):
        self._oprot.writeMessageBegin('createEidTable_IDL', TMessageType.CALL, self._seqid)
        args = createEidTable_IDL_args()
        args.lispHandle = lispHandle
        args.eidInstanceId = eidInstanceId
        args.vrf = vrf
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_createEidTable_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = createEidTable_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'createEidTable_IDL failed: unknown result')



    def deleteEidTable_IDL(self, lispHandle, eidInstanceId):
        """
            Delete an EID table
        
            Parameters:
             - lispHandle
             - eidInstanceId
            """
        self._oprot.rlock.acquire()
        try:
            self.send_deleteEidTable_IDL(lispHandle, eidInstanceId)
            result = self.recv_deleteEidTable_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_deleteEidTable_IDL(self, lispHandle, eidInstanceId):
        self._oprot.writeMessageBegin('deleteEidTable_IDL', TMessageType.CALL, self._seqid)
        args = deleteEidTable_IDL_args()
        args.lispHandle = lispHandle
        args.eidInstanceId = eidInstanceId
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_deleteEidTable_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = deleteEidTable_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'deleteEidTable_IDL failed: unknown result')



    def enableXtr_IDL(self, lispHandle, eidInstanceId, type, addrFamily):
        """
            Enable a P/xTR
        
            Parameters:
             - lispHandle
             - eidInstanceId
             - type
             - addrFamily
            """
        self._oprot.rlock.acquire()
        try:
            self.send_enableXtr_IDL(lispHandle, eidInstanceId, type, addrFamily)
            result = self.recv_enableXtr_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_enableXtr_IDL(self, lispHandle, eidInstanceId, type, addrFamily):
        self._oprot.writeMessageBegin('enableXtr_IDL', TMessageType.CALL, self._seqid)
        args = enableXtr_IDL_args()
        args.lispHandle = lispHandle
        args.eidInstanceId = eidInstanceId
        args.type = type
        args.addrFamily = addrFamily
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_enableXtr_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = enableXtr_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'enableXtr_IDL failed: unknown result')



    def disableXtr_IDL(self, lispHandle, eidInstanceId, type, addrFamily):
        """
            Disable a P/xTR
        
            Parameters:
             - lispHandle
             - eidInstanceId
             - type
             - addrFamily
            """
        self._oprot.rlock.acquire()
        try:
            self.send_disableXtr_IDL(lispHandle, eidInstanceId, type, addrFamily)
            result = self.recv_disableXtr_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_disableXtr_IDL(self, lispHandle, eidInstanceId, type, addrFamily):
        self._oprot.writeMessageBegin('disableXtr_IDL', TMessageType.CALL, self._seqid)
        args = disableXtr_IDL_args()
        args.lispHandle = lispHandle
        args.eidInstanceId = eidInstanceId
        args.type = type
        args.addrFamily = addrFamily
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_disableXtr_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = disableXtr_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'disableXtr_IDL failed: unknown result')



    def enablePitr_IDL(self, lispHandle, eidInstanceId, addrFamily, address):
        """
            Enable a PITR
        
            Parameters:
             - lispHandle
             - eidInstanceId
             - addrFamily
             - address
            """
        self._oprot.rlock.acquire()
        try:
            self.send_enablePitr_IDL(lispHandle, eidInstanceId, addrFamily, address)
            result = self.recv_enablePitr_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_enablePitr_IDL(self, lispHandle, eidInstanceId, addrFamily, address):
        self._oprot.writeMessageBegin('enablePitr_IDL', TMessageType.CALL, self._seqid)
        args = enablePitr_IDL_args()
        args.lispHandle = lispHandle
        args.eidInstanceId = eidInstanceId
        args.addrFamily = addrFamily
        args.address = address
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_enablePitr_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = enablePitr_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'enablePitr_IDL failed: unknown result')



    def addItrMapResolver_IDL(self, lispHandle, eidInstanceId, eidAF, addressAF, address):
        """
            Add Map Server to an ITR
        
            Parameters:
             - lispHandle
             - eidInstanceId
             - eidAF
             - addressAF
             - address
            """
        self._oprot.rlock.acquire()
        try:
            self.send_addItrMapResolver_IDL(lispHandle, eidInstanceId, eidAF, addressAF, address)
            result = self.recv_addItrMapResolver_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_addItrMapResolver_IDL(self, lispHandle, eidInstanceId, eidAF, addressAF, address):
        self._oprot.writeMessageBegin('addItrMapResolver_IDL', TMessageType.CALL, self._seqid)
        args = addItrMapResolver_IDL_args()
        args.lispHandle = lispHandle
        args.eidInstanceId = eidInstanceId
        args.eidAF = eidAF
        args.addressAF = addressAF
        args.address = address
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_addItrMapResolver_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = addItrMapResolver_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'addItrMapResolver_IDL failed: unknown result')



    def removeItrMapResolver_IDL(self, lispHandle, eidInstanceId, eidAF, addressAF, address):
        """
            Remove Map Server from an ITR
        
            Parameters:
             - lispHandle
             - eidInstanceId
             - eidAF
             - addressAF
             - address
            """
        self._oprot.rlock.acquire()
        try:
            self.send_removeItrMapResolver_IDL(lispHandle, eidInstanceId, eidAF, addressAF, address)
            result = self.recv_removeItrMapResolver_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_removeItrMapResolver_IDL(self, lispHandle, eidInstanceId, eidAF, addressAF, address):
        self._oprot.writeMessageBegin('removeItrMapResolver_IDL', TMessageType.CALL, self._seqid)
        args = removeItrMapResolver_IDL_args()
        args.lispHandle = lispHandle
        args.eidInstanceId = eidInstanceId
        args.eidAF = eidAF
        args.addressAF = addressAF
        args.address = address
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_removeItrMapResolver_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = removeItrMapResolver_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'removeItrMapResolver_IDL failed: unknown result')



    def addEtrMapServer_IDL(self, lispHandle, eidInstanceId, eidAF, addressAF, address, key):
        """
            Add Map Server to an ETR
        
            Parameters:
             - lispHandle
             - eidInstanceId
             - eidAF
             - addressAF
             - address
             - key
            """
        self._oprot.rlock.acquire()
        try:
            self.send_addEtrMapServer_IDL(lispHandle, eidInstanceId, eidAF, addressAF, address, key)
            result = self.recv_addEtrMapServer_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_addEtrMapServer_IDL(self, lispHandle, eidInstanceId, eidAF, addressAF, address, key):
        self._oprot.writeMessageBegin('addEtrMapServer_IDL', TMessageType.CALL, self._seqid)
        args = addEtrMapServer_IDL_args()
        args.lispHandle = lispHandle
        args.eidInstanceId = eidInstanceId
        args.eidAF = eidAF
        args.addressAF = addressAF
        args.address = address
        args.key = key
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_addEtrMapServer_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = addEtrMapServer_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'addEtrMapServer_IDL failed: unknown result')



    def removeEtrMapServer_IDL(self, lispHandle, eidInstanceId, eidAF, addressAF, address):
        """
            Remove Map Server from an ETR
        
            Parameters:
             - lispHandle
             - eidInstanceId
             - eidAF
             - addressAF
             - address
            """
        self._oprot.rlock.acquire()
        try:
            self.send_removeEtrMapServer_IDL(lispHandle, eidInstanceId, eidAF, addressAF, address)
            result = self.recv_removeEtrMapServer_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_removeEtrMapServer_IDL(self, lispHandle, eidInstanceId, eidAF, addressAF, address):
        self._oprot.writeMessageBegin('removeEtrMapServer_IDL', TMessageType.CALL, self._seqid)
        args = removeEtrMapServer_IDL_args()
        args.lispHandle = lispHandle
        args.eidInstanceId = eidInstanceId
        args.eidAF = eidAF
        args.addressAF = addressAF
        args.address = address
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_removeEtrMapServer_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = removeEtrMapServer_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'removeEtrMapServer_IDL failed: unknown result')



    def addLocalPrefix_IDL(self, lispHandle, eidInstanceId, prefixAF, prefix, prefixLen):
        """
            Add Local EID Prefix
        
            Parameters:
             - lispHandle
             - eidInstanceId
             - prefixAF
             - prefix
             - prefixLen
            """
        self._oprot.rlock.acquire()
        try:
            self.send_addLocalPrefix_IDL(lispHandle, eidInstanceId, prefixAF, prefix, prefixLen)
            result = self.recv_addLocalPrefix_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_addLocalPrefix_IDL(self, lispHandle, eidInstanceId, prefixAF, prefix, prefixLen):
        self._oprot.writeMessageBegin('addLocalPrefix_IDL', TMessageType.CALL, self._seqid)
        args = addLocalPrefix_IDL_args()
        args.lispHandle = lispHandle
        args.eidInstanceId = eidInstanceId
        args.prefixAF = prefixAF
        args.prefix = prefix
        args.prefixLen = prefixLen
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_addLocalPrefix_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = addLocalPrefix_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'addLocalPrefix_IDL failed: unknown result')



    def removeLocalPrefix_IDL(self, lispHandle, eidInstanceId, prefixAF, prefix, prefixLen):
        """
            Remove Local EID Prefix
        
            Parameters:
             - lispHandle
             - eidInstanceId
             - prefixAF
             - prefix
             - prefixLen
            """
        self._oprot.rlock.acquire()
        try:
            self.send_removeLocalPrefix_IDL(lispHandle, eidInstanceId, prefixAF, prefix, prefixLen)
            result = self.recv_removeLocalPrefix_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_removeLocalPrefix_IDL(self, lispHandle, eidInstanceId, prefixAF, prefix, prefixLen):
        self._oprot.writeMessageBegin('removeLocalPrefix_IDL', TMessageType.CALL, self._seqid)
        args = removeLocalPrefix_IDL_args()
        args.lispHandle = lispHandle
        args.eidInstanceId = eidInstanceId
        args.prefixAF = prefixAF
        args.prefix = prefix
        args.prefixLen = prefixLen
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_removeLocalPrefix_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = removeLocalPrefix_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'removeLocalPrefix_IDL failed: unknown result')



    def addLocalPrefixRlocMap_IDL(self, lispHandle, eidInstanceId, prefixAF, prefix, prefixLen, localRlocs):
        """
            Add Local EID Prefix-RLOC Database-mapping
        
            Parameters:
             - lispHandle
             - eidInstanceId
             - prefixAF
             - prefix
             - prefixLen
             - localRlocs
            """
        self._oprot.rlock.acquire()
        try:
            self.send_addLocalPrefixRlocMap_IDL(lispHandle, eidInstanceId, prefixAF, prefix, prefixLen, localRlocs)
            result = self.recv_addLocalPrefixRlocMap_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_addLocalPrefixRlocMap_IDL(self, lispHandle, eidInstanceId, prefixAF, prefix, prefixLen, localRlocs):
        self._oprot.writeMessageBegin('addLocalPrefixRlocMap_IDL', TMessageType.CALL, self._seqid)
        args = addLocalPrefixRlocMap_IDL_args()
        args.lispHandle = lispHandle
        args.eidInstanceId = eidInstanceId
        args.prefixAF = prefixAF
        args.prefix = prefix
        args.prefixLen = prefixLen
        args.localRlocs = localRlocs
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_addLocalPrefixRlocMap_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = addLocalPrefixRlocMap_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'addLocalPrefixRlocMap_IDL failed: unknown result')



    def removeLocalPrefixRlocMap_IDL(self, lispHandle, eidInstanceId, prefixAF, prefix, prefixLen, rlocAF, rloc):
        """
            Remove Local EID Prefix-RLOC Database-mapping
        
            Parameters:
             - lispHandle
             - eidInstanceId
             - prefixAF
             - prefix
             - prefixLen
             - rlocAF
             - rloc
            """
        self._oprot.rlock.acquire()
        try:
            self.send_removeLocalPrefixRlocMap_IDL(lispHandle, eidInstanceId, prefixAF, prefix, prefixLen, rlocAF, rloc)
            result = self.recv_removeLocalPrefixRlocMap_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_removeLocalPrefixRlocMap_IDL(self, lispHandle, eidInstanceId, prefixAF, prefix, prefixLen, rlocAF, rloc):
        self._oprot.writeMessageBegin('removeLocalPrefixRlocMap_IDL', TMessageType.CALL, self._seqid)
        args = removeLocalPrefixRlocMap_IDL_args()
        args.lispHandle = lispHandle
        args.eidInstanceId = eidInstanceId
        args.prefixAF = prefixAF
        args.prefix = prefix
        args.prefixLen = prefixLen
        args.rlocAF = rlocAF
        args.rloc = rloc
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_removeLocalPrefixRlocMap_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = removeLocalPrefixRlocMap_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'removeLocalPrefixRlocMap_IDL failed: unknown result')



    def addLocalPrefixIfcMap_IDL(self, lispHandle, eidInstanceId, prefixAF, prefix, prefixLen, ifHandle, addrFamily, priority, weight):
        """
            Add Local EID Prefix-Interface Database-mapping
        
            Parameters:
             - lispHandle
             - eidInstanceId
             - prefixAF
             - prefix
             - prefixLen
             - ifHandle
             - addrFamily
             - priority
             - weight
            """
        self._oprot.rlock.acquire()
        try:
            self.send_addLocalPrefixIfcMap_IDL(lispHandle, eidInstanceId, prefixAF, prefix, prefixLen, ifHandle, addrFamily, priority, weight)
            result = self.recv_addLocalPrefixIfcMap_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_addLocalPrefixIfcMap_IDL(self, lispHandle, eidInstanceId, prefixAF, prefix, prefixLen, ifHandle, addrFamily, priority, weight):
        self._oprot.writeMessageBegin('addLocalPrefixIfcMap_IDL', TMessageType.CALL, self._seqid)
        args = addLocalPrefixIfcMap_IDL_args()
        args.lispHandle = lispHandle
        args.eidInstanceId = eidInstanceId
        args.prefixAF = prefixAF
        args.prefix = prefix
        args.prefixLen = prefixLen
        args.ifHandle = ifHandle
        args.addrFamily = addrFamily
        args.priority = priority
        args.weight = weight
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_addLocalPrefixIfcMap_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = addLocalPrefixIfcMap_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'addLocalPrefixIfcMap_IDL failed: unknown result')



    def removeLocalPrefixIfcMap_IDL(self, lispHandle, eidInstanceId, prefixAF, prefix, prefixLen, ifHandle, addrFamily):
        """
            Remove Local EID Prefix-Interface Database-mapping
        
            Parameters:
             - lispHandle
             - eidInstanceId
             - prefixAF
             - prefix
             - prefixLen
             - ifHandle
             - addrFamily
            """
        self._oprot.rlock.acquire()
        try:
            self.send_removeLocalPrefixIfcMap_IDL(lispHandle, eidInstanceId, prefixAF, prefix, prefixLen, ifHandle, addrFamily)
            result = self.recv_removeLocalPrefixIfcMap_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_removeLocalPrefixIfcMap_IDL(self, lispHandle, eidInstanceId, prefixAF, prefix, prefixLen, ifHandle, addrFamily):
        self._oprot.writeMessageBegin('removeLocalPrefixIfcMap_IDL', TMessageType.CALL, self._seqid)
        args = removeLocalPrefixIfcMap_IDL_args()
        args.lispHandle = lispHandle
        args.eidInstanceId = eidInstanceId
        args.prefixAF = prefixAF
        args.prefix = prefix
        args.prefixLen = prefixLen
        args.ifHandle = ifHandle
        args.addrFamily = addrFamily
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_removeLocalPrefixIfcMap_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = removeLocalPrefixIfcMap_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'removeLocalPrefixIfcMap_IDL failed: unknown result')



    def addRemotePrefix_IDL(self, lispHandle, eidInstanceId, prefixAF, prefix, prefixLen):
        """
            Add Remote EID Prefix
        
            Parameters:
             - lispHandle
             - eidInstanceId
             - prefixAF
             - prefix
             - prefixLen
            """
        self._oprot.rlock.acquire()
        try:
            self.send_addRemotePrefix_IDL(lispHandle, eidInstanceId, prefixAF, prefix, prefixLen)
            result = self.recv_addRemotePrefix_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_addRemotePrefix_IDL(self, lispHandle, eidInstanceId, prefixAF, prefix, prefixLen):
        self._oprot.writeMessageBegin('addRemotePrefix_IDL', TMessageType.CALL, self._seqid)
        args = addRemotePrefix_IDL_args()
        args.lispHandle = lispHandle
        args.eidInstanceId = eidInstanceId
        args.prefixAF = prefixAF
        args.prefix = prefix
        args.prefixLen = prefixLen
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_addRemotePrefix_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = addRemotePrefix_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'addRemotePrefix_IDL failed: unknown result')



    def removeRemotePrefix_IDL(self, lispHandle, eidInstanceId, prefixAF, prefix, prefixLen):
        """
            Remove Remote EID Prefix
        
            Parameters:
             - lispHandle
             - eidInstanceId
             - prefixAF
             - prefix
             - prefixLen
            """
        self._oprot.rlock.acquire()
        try:
            self.send_removeRemotePrefix_IDL(lispHandle, eidInstanceId, prefixAF, prefix, prefixLen)
            result = self.recv_removeRemotePrefix_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_removeRemotePrefix_IDL(self, lispHandle, eidInstanceId, prefixAF, prefix, prefixLen):
        self._oprot.writeMessageBegin('removeRemotePrefix_IDL', TMessageType.CALL, self._seqid)
        args = removeRemotePrefix_IDL_args()
        args.lispHandle = lispHandle
        args.eidInstanceId = eidInstanceId
        args.prefixAF = prefixAF
        args.prefix = prefix
        args.prefixLen = prefixLen
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_removeRemotePrefix_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = removeRemotePrefix_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'removeRemotePrefix_IDL failed: unknown result')



    def addMapServerAddressToEtr_IDL(self, lispHandle, eidInstanceId, addrFamily, addr, key):
        """
            Add Map-server address to an ETR
        
            Parameters:
             - lispHandle
             - eidInstanceId
             - addrFamily
             - addr
             - key
            """
        self._oprot.rlock.acquire()
        try:
            self.send_addMapServerAddressToEtr_IDL(lispHandle, eidInstanceId, addrFamily, addr, key)
            result = self.recv_addMapServerAddressToEtr_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_addMapServerAddressToEtr_IDL(self, lispHandle, eidInstanceId, addrFamily, addr, key):
        self._oprot.writeMessageBegin('addMapServerAddressToEtr_IDL', TMessageType.CALL, self._seqid)
        args = addMapServerAddressToEtr_IDL_args()
        args.lispHandle = lispHandle
        args.eidInstanceId = eidInstanceId
        args.addrFamily = addrFamily
        args.addr = addr
        args.key = key
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_addMapServerAddressToEtr_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = addMapServerAddressToEtr_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'addMapServerAddressToEtr_IDL failed: unknown result')



    def addRemotePrefixRlocMap_IDL(self, lispHandle, eidInstanceId, prefixAF, prefix, prefixLen, state, remoteRlocs):
        """
            Add Remote EID Prefix-RLOC Database-mapping
        
            Parameters:
             - lispHandle
             - eidInstanceId
             - prefixAF
             - prefix
             - prefixLen
             - state
             - remoteRlocs
            """
        self._oprot.rlock.acquire()
        try:
            self.send_addRemotePrefixRlocMap_IDL(lispHandle, eidInstanceId, prefixAF, prefix, prefixLen, state, remoteRlocs)
            result = self.recv_addRemotePrefixRlocMap_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_addRemotePrefixRlocMap_IDL(self, lispHandle, eidInstanceId, prefixAF, prefix, prefixLen, state, remoteRlocs):
        self._oprot.writeMessageBegin('addRemotePrefixRlocMap_IDL', TMessageType.CALL, self._seqid)
        args = addRemotePrefixRlocMap_IDL_args()
        args.lispHandle = lispHandle
        args.eidInstanceId = eidInstanceId
        args.prefixAF = prefixAF
        args.prefix = prefix
        args.prefixLen = prefixLen
        args.state = state
        args.remoteRlocs = remoteRlocs
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_addRemotePrefixRlocMap_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = addRemotePrefixRlocMap_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'addRemotePrefixRlocMap_IDL failed: unknown result')



    def removeRemotePrefixRlocMap_IDL(self, lispHandle, eidInstanceId, prefixAF, prefix, prefixLen, rlocAF, rloc):
        """
            Remove Remote EID Prefix-RLOC Database-mapping
        
            Parameters:
             - lispHandle
             - eidInstanceId
             - prefixAF
             - prefix
             - prefixLen
             - rlocAF
             - rloc
            """
        self._oprot.rlock.acquire()
        try:
            self.send_removeRemotePrefixRlocMap_IDL(lispHandle, eidInstanceId, prefixAF, prefix, prefixLen, rlocAF, rloc)
            result = self.recv_removeRemotePrefixRlocMap_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_removeRemotePrefixRlocMap_IDL(self, lispHandle, eidInstanceId, prefixAF, prefix, prefixLen, rlocAF, rloc):
        self._oprot.writeMessageBegin('removeRemotePrefixRlocMap_IDL', TMessageType.CALL, self._seqid)
        args = removeRemotePrefixRlocMap_IDL_args()
        args.lispHandle = lispHandle
        args.eidInstanceId = eidInstanceId
        args.prefixAF = prefixAF
        args.prefix = prefix
        args.prefixLen = prefixLen
        args.rlocAF = rlocAF
        args.rloc = rloc
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_removeRemotePrefixRlocMap_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = removeRemotePrefixRlocMap_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'removeRemotePrefixRlocMap_IDL failed: unknown result')



    def addPrefixToSite_IDL(self, lispHandle, siteHandle, eidInstanceId, prefixAF, prefix, prefixLen):
        """
            Add Prefix to a Map-server Site
        
            Parameters:
             - lispHandle
             - siteHandle
             - eidInstanceId
             - prefixAF
             - prefix
             - prefixLen
            """
        self._oprot.rlock.acquire()
        try:
            self.send_addPrefixToSite_IDL(lispHandle, siteHandle, eidInstanceId, prefixAF, prefix, prefixLen)
            result = self.recv_addPrefixToSite_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_addPrefixToSite_IDL(self, lispHandle, siteHandle, eidInstanceId, prefixAF, prefix, prefixLen):
        self._oprot.writeMessageBegin('addPrefixToSite_IDL', TMessageType.CALL, self._seqid)
        args = addPrefixToSite_IDL_args()
        args.lispHandle = lispHandle
        args.siteHandle = siteHandle
        args.eidInstanceId = eidInstanceId
        args.prefixAF = prefixAF
        args.prefix = prefix
        args.prefixLen = prefixLen
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_addPrefixToSite_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = addPrefixToSite_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'addPrefixToSite_IDL failed: unknown result')



    def removePrefixFromSite_IDL(self, lispHandle, siteHandle, eidInstanceId, prefixAF, prefix, prefixLen):
        """
            Remove Prefix from a Map-server Site
        
            Parameters:
             - lispHandle
             - siteHandle
             - eidInstanceId
             - prefixAF
             - prefix
             - prefixLen
            """
        self._oprot.rlock.acquire()
        try:
            self.send_removePrefixFromSite_IDL(lispHandle, siteHandle, eidInstanceId, prefixAF, prefix, prefixLen)
            result = self.recv_removePrefixFromSite_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_removePrefixFromSite_IDL(self, lispHandle, siteHandle, eidInstanceId, prefixAF, prefix, prefixLen):
        self._oprot.writeMessageBegin('removePrefixFromSite_IDL', TMessageType.CALL, self._seqid)
        args = removePrefixFromSite_IDL_args()
        args.lispHandle = lispHandle
        args.siteHandle = siteHandle
        args.eidInstanceId = eidInstanceId
        args.prefixAF = prefixAF
        args.prefix = prefix
        args.prefixLen = prefixLen
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_removePrefixFromSite_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = removePrefixFromSite_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'removePrefixFromSite_IDL failed: unknown result')



    def setMapServerKey_IDL(self, lispHandle, siteHandle, key):
        """
            Set a Map-server Key
        
            Parameters:
             - lispHandle
             - siteHandle
             - key
            """
        self._oprot.rlock.acquire()
        try:
            self.send_setMapServerKey_IDL(lispHandle, siteHandle, key)
            result = self.recv_setMapServerKey_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_setMapServerKey_IDL(self, lispHandle, siteHandle, key):
        self._oprot.writeMessageBegin('setMapServerKey_IDL', TMessageType.CALL, self._seqid)
        args = setMapServerKey_IDL_args()
        args.lispHandle = lispHandle
        args.siteHandle = siteHandle
        args.key = key
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_setMapServerKey_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = setMapServerKey_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'setMapServerKey_IDL failed: unknown result')



    def clearMapServerReg_IDL(self, lispHandle, siteHandle, eidInstanceId, prefixAF, prefix, prefixLen):
        """
            Clear Map-server Registration
        
            Parameters:
             - lispHandle
             - siteHandle
             - eidInstanceId
             - prefixAF
             - prefix
             - prefixLen
            """
        self._oprot.rlock.acquire()
        try:
            self.send_clearMapServerReg_IDL(lispHandle, siteHandle, eidInstanceId, prefixAF, prefix, prefixLen)
            result = self.recv_clearMapServerReg_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_clearMapServerReg_IDL(self, lispHandle, siteHandle, eidInstanceId, prefixAF, prefix, prefixLen):
        self._oprot.writeMessageBegin('clearMapServerReg_IDL', TMessageType.CALL, self._seqid)
        args = clearMapServerReg_IDL_args()
        args.lispHandle = lispHandle
        args.siteHandle = siteHandle
        args.eidInstanceId = eidInstanceId
        args.prefixAF = prefixAF
        args.prefix = prefix
        args.prefixLen = prefixLen
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_clearMapServerReg_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = clearMapServerReg_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'clearMapServerReg_IDL failed: unknown result')



    def clearMapCacheEntry_IDL(self, lispHandle, eidInstanceId, prefixAF, prefix, prefixLen):
        """
            Clear Map Cache Entry
        
            Parameters:
             - lispHandle
             - eidInstanceId
             - prefixAF
             - prefix
             - prefixLen
            """
        self._oprot.rlock.acquire()
        try:
            self.send_clearMapCacheEntry_IDL(lispHandle, eidInstanceId, prefixAF, prefix, prefixLen)
            result = self.recv_clearMapCacheEntry_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_clearMapCacheEntry_IDL(self, lispHandle, eidInstanceId, prefixAF, prefix, prefixLen):
        self._oprot.writeMessageBegin('clearMapCacheEntry_IDL', TMessageType.CALL, self._seqid)
        args = clearMapCacheEntry_IDL_args()
        args.lispHandle = lispHandle
        args.eidInstanceId = eidInstanceId
        args.prefixAF = prefixAF
        args.prefix = prefix
        args.prefixLen = prefixLen
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_clearMapCacheEntry_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = clearMapCacheEntry_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'clearMapCacheEntry_IDL failed: unknown result')



    def findMapCacheEntry_IDL(self, lispHandle, eidInstanceId, prefixAF, prefix, prefixLen):
        """
            Find Map Cache Entry
        
            Parameters:
             - lispHandle
             - eidInstanceId
             - prefixAF
             - prefix
             - prefixLen
            """
        self._oprot.rlock.acquire()
        try:
            self.send_findMapCacheEntry_IDL(lispHandle, eidInstanceId, prefixAF, prefix, prefixLen)
            result = self.recv_findMapCacheEntry_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_findMapCacheEntry_IDL(self, lispHandle, eidInstanceId, prefixAF, prefix, prefixLen):
        self._oprot.writeMessageBegin('findMapCacheEntry_IDL', TMessageType.CALL, self._seqid)
        args = findMapCacheEntry_IDL_args()
        args.lispHandle = lispHandle
        args.eidInstanceId = eidInstanceId
        args.prefixAF = prefixAF
        args.prefix = prefix
        args.prefixLen = prefixLen
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_findMapCacheEntry_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = findMapCacheEntry_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'findMapCacheEntry_IDL failed: unknown result')



    def findMapCacheLongestMatchEntry_IDL(self, lispHandle, eidInstanceId, addrAF, addr):
        """
            Find Longest in Map Cache
        
            Parameters:
             - lispHandle
             - eidInstanceId
             - addrAF
             - addr
            """
        self._oprot.rlock.acquire()
        try:
            self.send_findMapCacheLongestMatchEntry_IDL(lispHandle, eidInstanceId, addrAF, addr)
            result = self.recv_findMapCacheLongestMatchEntry_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_findMapCacheLongestMatchEntry_IDL(self, lispHandle, eidInstanceId, addrAF, addr):
        self._oprot.writeMessageBegin('findMapCacheLongestMatchEntry_IDL', TMessageType.CALL, self._seqid)
        args = findMapCacheLongestMatchEntry_IDL_args()
        args.lispHandle = lispHandle
        args.eidInstanceId = eidInstanceId
        args.addrAF = addrAF
        args.addr = addr
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_findMapCacheLongestMatchEntry_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = findMapCacheLongestMatchEntry_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'findMapCacheLongestMatchEntry_IDL failed: unknown result')



    def signalMapCache_IDL(self, lispHandle, eidInstanceId, addrAF, addr):
        """
            Signal
        
            Parameters:
             - lispHandle
             - eidInstanceId
             - addrAF
             - addr
            """
        self._oprot.rlock.acquire()
        try:
            self.send_signalMapCache_IDL(lispHandle, eidInstanceId, addrAF, addr)
            result = self.recv_signalMapCache_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_signalMapCache_IDL(self, lispHandle, eidInstanceId, addrAF, addr):
        self._oprot.writeMessageBegin('signalMapCache_IDL', TMessageType.CALL, self._seqid)
        args = signalMapCache_IDL_args()
        args.lispHandle = lispHandle
        args.eidInstanceId = eidInstanceId
        args.addrAF = addrAF
        args.addr = addr
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_signalMapCache_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = signalMapCache_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'signalMapCache_IDL failed: unknown result')



    def enableProbe_IDL(self, lispHandle, eidInstanceId):
        """
            Enable Probe
        
            Parameters:
             - lispHandle
             - eidInstanceId
            """
        self._oprot.rlock.acquire()
        try:
            self.send_enableProbe_IDL(lispHandle, eidInstanceId)
            result = self.recv_enableProbe_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_enableProbe_IDL(self, lispHandle, eidInstanceId):
        self._oprot.writeMessageBegin('enableProbe_IDL', TMessageType.CALL, self._seqid)
        args = enableProbe_IDL_args()
        args.lispHandle = lispHandle
        args.eidInstanceId = eidInstanceId
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_enableProbe_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = enableProbe_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'enableProbe_IDL failed: unknown result')



    def disableProbe_IDL(self, lispHandle, eidInstanceId):
        """
            Disable Probe
        
            Parameters:
             - lispHandle
             - eidInstanceId
            """
        self._oprot.rlock.acquire()
        try:
            self.send_disableProbe_IDL(lispHandle, eidInstanceId)
            result = self.recv_disableProbe_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_disableProbe_IDL(self, lispHandle, eidInstanceId):
        self._oprot.writeMessageBegin('disableProbe_IDL', TMessageType.CALL, self._seqid)
        args = disableProbe_IDL_args()
        args.lispHandle = lispHandle
        args.eidInstanceId = eidInstanceId
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_disableProbe_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = disableProbe_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'disableProbe_IDL failed: unknown result')




class Processor(Iface, TProcessor):

    def __init__(self, handler):
        self._handler = handler
        self._processMap = {}
        self._processMap['createLisp_IDL'] = Processor.process_createLisp_IDL
        self._processMap['deleteLisp_IDL'] = Processor.process_deleteLisp_IDL
        self._processMap['enableMapServer_IDL'] = Processor.process_enableMapServer_IDL
        self._processMap['disableMapServer_IDL'] = Processor.process_disableMapServer_IDL
        self._processMap['createSite_IDL'] = Processor.process_createSite_IDL
        self._processMap['deleteSite_IDL'] = Processor.process_deleteSite_IDL
        self._processMap['enableMapResolver_IDL'] = Processor.process_enableMapResolver_IDL
        self._processMap['disableMapResolver_IDL'] = Processor.process_disableMapResolver_IDL
        self._processMap['createEidTable_IDL'] = Processor.process_createEidTable_IDL
        self._processMap['deleteEidTable_IDL'] = Processor.process_deleteEidTable_IDL
        self._processMap['enableXtr_IDL'] = Processor.process_enableXtr_IDL
        self._processMap['disableXtr_IDL'] = Processor.process_disableXtr_IDL
        self._processMap['enablePitr_IDL'] = Processor.process_enablePitr_IDL
        self._processMap['addItrMapResolver_IDL'] = Processor.process_addItrMapResolver_IDL
        self._processMap['removeItrMapResolver_IDL'] = Processor.process_removeItrMapResolver_IDL
        self._processMap['addEtrMapServer_IDL'] = Processor.process_addEtrMapServer_IDL
        self._processMap['removeEtrMapServer_IDL'] = Processor.process_removeEtrMapServer_IDL
        self._processMap['addLocalPrefix_IDL'] = Processor.process_addLocalPrefix_IDL
        self._processMap['removeLocalPrefix_IDL'] = Processor.process_removeLocalPrefix_IDL
        self._processMap['addLocalPrefixRlocMap_IDL'] = Processor.process_addLocalPrefixRlocMap_IDL
        self._processMap['removeLocalPrefixRlocMap_IDL'] = Processor.process_removeLocalPrefixRlocMap_IDL
        self._processMap['addLocalPrefixIfcMap_IDL'] = Processor.process_addLocalPrefixIfcMap_IDL
        self._processMap['removeLocalPrefixIfcMap_IDL'] = Processor.process_removeLocalPrefixIfcMap_IDL
        self._processMap['addRemotePrefix_IDL'] = Processor.process_addRemotePrefix_IDL
        self._processMap['removeRemotePrefix_IDL'] = Processor.process_removeRemotePrefix_IDL
        self._processMap['addMapServerAddressToEtr_IDL'] = Processor.process_addMapServerAddressToEtr_IDL
        self._processMap['addRemotePrefixRlocMap_IDL'] = Processor.process_addRemotePrefixRlocMap_IDL
        self._processMap['removeRemotePrefixRlocMap_IDL'] = Processor.process_removeRemotePrefixRlocMap_IDL
        self._processMap['addPrefixToSite_IDL'] = Processor.process_addPrefixToSite_IDL
        self._processMap['removePrefixFromSite_IDL'] = Processor.process_removePrefixFromSite_IDL
        self._processMap['setMapServerKey_IDL'] = Processor.process_setMapServerKey_IDL
        self._processMap['clearMapServerReg_IDL'] = Processor.process_clearMapServerReg_IDL
        self._processMap['clearMapCacheEntry_IDL'] = Processor.process_clearMapCacheEntry_IDL
        self._processMap['findMapCacheEntry_IDL'] = Processor.process_findMapCacheEntry_IDL
        self._processMap['findMapCacheLongestMatchEntry_IDL'] = Processor.process_findMapCacheLongestMatchEntry_IDL
        self._processMap['signalMapCache_IDL'] = Processor.process_signalMapCache_IDL
        self._processMap['enableProbe_IDL'] = Processor.process_enableProbe_IDL
        self._processMap['disableProbe_IDL'] = Processor.process_disableProbe_IDL



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



    def process_createLisp_IDL(self, seqid, iprot, oprot):
        args = createLisp_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = createLisp_IDL_result()
        try:
            result.success = self._handler.createLisp_IDL(args.lispHandle, args.vrf)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('createLisp_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_deleteLisp_IDL(self, seqid, iprot, oprot):
        args = deleteLisp_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = deleteLisp_IDL_result()
        try:
            result.success = self._handler.deleteLisp_IDL(args.lispHandle)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('deleteLisp_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_enableMapServer_IDL(self, seqid, iprot, oprot):
        args = enableMapServer_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = enableMapServer_IDL_result()
        try:
            result.success = self._handler.enableMapServer_IDL(args.lispHandle, args.addrFamily)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('enableMapServer_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_disableMapServer_IDL(self, seqid, iprot, oprot):
        args = disableMapServer_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = disableMapServer_IDL_result()
        try:
            result.success = self._handler.disableMapServer_IDL(args.lispHandle, args.addrFamily)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('disableMapServer_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_createSite_IDL(self, seqid, iprot, oprot):
        args = createSite_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = createSite_IDL_result()
        try:
            result.success = self._handler.createSite_IDL(args.lispHandle, args.siteHandle)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('createSite_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_deleteSite_IDL(self, seqid, iprot, oprot):
        args = deleteSite_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = deleteSite_IDL_result()
        try:
            result.success = self._handler.deleteSite_IDL(args.lispHandle, args.siteHandle)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('deleteSite_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_enableMapResolver_IDL(self, seqid, iprot, oprot):
        args = enableMapResolver_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = enableMapResolver_IDL_result()
        try:
            result.success = self._handler.enableMapResolver_IDL(args.lispHandle, args.addrFamily)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('enableMapResolver_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_disableMapResolver_IDL(self, seqid, iprot, oprot):
        args = disableMapResolver_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = disableMapResolver_IDL_result()
        try:
            result.success = self._handler.disableMapResolver_IDL(args.lispHandle, args.addrFamily)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('disableMapResolver_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_createEidTable_IDL(self, seqid, iprot, oprot):
        args = createEidTable_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = createEidTable_IDL_result()
        try:
            result.success = self._handler.createEidTable_IDL(args.lispHandle, args.eidInstanceId, args.vrf)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('createEidTable_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_deleteEidTable_IDL(self, seqid, iprot, oprot):
        args = deleteEidTable_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = deleteEidTable_IDL_result()
        try:
            result.success = self._handler.deleteEidTable_IDL(args.lispHandle, args.eidInstanceId)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('deleteEidTable_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_enableXtr_IDL(self, seqid, iprot, oprot):
        args = enableXtr_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = enableXtr_IDL_result()
        try:
            result.success = self._handler.enableXtr_IDL(args.lispHandle, args.eidInstanceId, args.type, args.addrFamily)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('enableXtr_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_disableXtr_IDL(self, seqid, iprot, oprot):
        args = disableXtr_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = disableXtr_IDL_result()
        try:
            result.success = self._handler.disableXtr_IDL(args.lispHandle, args.eidInstanceId, args.type, args.addrFamily)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('disableXtr_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_enablePitr_IDL(self, seqid, iprot, oprot):
        args = enablePitr_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = enablePitr_IDL_result()
        try:
            result.success = self._handler.enablePitr_IDL(args.lispHandle, args.eidInstanceId, args.addrFamily, args.address)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('enablePitr_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_addItrMapResolver_IDL(self, seqid, iprot, oprot):
        args = addItrMapResolver_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = addItrMapResolver_IDL_result()
        try:
            result.success = self._handler.addItrMapResolver_IDL(args.lispHandle, args.eidInstanceId, args.eidAF, args.addressAF, args.address)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('addItrMapResolver_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_removeItrMapResolver_IDL(self, seqid, iprot, oprot):
        args = removeItrMapResolver_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = removeItrMapResolver_IDL_result()
        try:
            result.success = self._handler.removeItrMapResolver_IDL(args.lispHandle, args.eidInstanceId, args.eidAF, args.addressAF, args.address)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('removeItrMapResolver_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_addEtrMapServer_IDL(self, seqid, iprot, oprot):
        args = addEtrMapServer_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = addEtrMapServer_IDL_result()
        try:
            result.success = self._handler.addEtrMapServer_IDL(args.lispHandle, args.eidInstanceId, args.eidAF, args.addressAF, args.address, args.key)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('addEtrMapServer_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_removeEtrMapServer_IDL(self, seqid, iprot, oprot):
        args = removeEtrMapServer_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = removeEtrMapServer_IDL_result()
        try:
            result.success = self._handler.removeEtrMapServer_IDL(args.lispHandle, args.eidInstanceId, args.eidAF, args.addressAF, args.address)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('removeEtrMapServer_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_addLocalPrefix_IDL(self, seqid, iprot, oprot):
        args = addLocalPrefix_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = addLocalPrefix_IDL_result()
        try:
            result.success = self._handler.addLocalPrefix_IDL(args.lispHandle, args.eidInstanceId, args.prefixAF, args.prefix, args.prefixLen)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('addLocalPrefix_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_removeLocalPrefix_IDL(self, seqid, iprot, oprot):
        args = removeLocalPrefix_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = removeLocalPrefix_IDL_result()
        try:
            result.success = self._handler.removeLocalPrefix_IDL(args.lispHandle, args.eidInstanceId, args.prefixAF, args.prefix, args.prefixLen)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('removeLocalPrefix_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_addLocalPrefixRlocMap_IDL(self, seqid, iprot, oprot):
        args = addLocalPrefixRlocMap_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = addLocalPrefixRlocMap_IDL_result()
        try:
            result.success = self._handler.addLocalPrefixRlocMap_IDL(args.lispHandle, args.eidInstanceId, args.prefixAF, args.prefix, args.prefixLen, args.localRlocs)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('addLocalPrefixRlocMap_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_removeLocalPrefixRlocMap_IDL(self, seqid, iprot, oprot):
        args = removeLocalPrefixRlocMap_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = removeLocalPrefixRlocMap_IDL_result()
        try:
            result.success = self._handler.removeLocalPrefixRlocMap_IDL(args.lispHandle, args.eidInstanceId, args.prefixAF, args.prefix, args.prefixLen, args.rlocAF, args.rloc)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('removeLocalPrefixRlocMap_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_addLocalPrefixIfcMap_IDL(self, seqid, iprot, oprot):
        args = addLocalPrefixIfcMap_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = addLocalPrefixIfcMap_IDL_result()
        try:
            result.success = self._handler.addLocalPrefixIfcMap_IDL(args.lispHandle, args.eidInstanceId, args.prefixAF, args.prefix, args.prefixLen, args.ifHandle, args.addrFamily, args.priority, args.weight)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('addLocalPrefixIfcMap_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_removeLocalPrefixIfcMap_IDL(self, seqid, iprot, oprot):
        args = removeLocalPrefixIfcMap_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = removeLocalPrefixIfcMap_IDL_result()
        try:
            result.success = self._handler.removeLocalPrefixIfcMap_IDL(args.lispHandle, args.eidInstanceId, args.prefixAF, args.prefix, args.prefixLen, args.ifHandle, args.addrFamily)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('removeLocalPrefixIfcMap_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_addRemotePrefix_IDL(self, seqid, iprot, oprot):
        args = addRemotePrefix_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = addRemotePrefix_IDL_result()
        try:
            result.success = self._handler.addRemotePrefix_IDL(args.lispHandle, args.eidInstanceId, args.prefixAF, args.prefix, args.prefixLen)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('addRemotePrefix_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_removeRemotePrefix_IDL(self, seqid, iprot, oprot):
        args = removeRemotePrefix_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = removeRemotePrefix_IDL_result()
        try:
            result.success = self._handler.removeRemotePrefix_IDL(args.lispHandle, args.eidInstanceId, args.prefixAF, args.prefix, args.prefixLen)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('removeRemotePrefix_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_addMapServerAddressToEtr_IDL(self, seqid, iprot, oprot):
        args = addMapServerAddressToEtr_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = addMapServerAddressToEtr_IDL_result()
        try:
            result.success = self._handler.addMapServerAddressToEtr_IDL(args.lispHandle, args.eidInstanceId, args.addrFamily, args.addr, args.key)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('addMapServerAddressToEtr_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_addRemotePrefixRlocMap_IDL(self, seqid, iprot, oprot):
        args = addRemotePrefixRlocMap_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = addRemotePrefixRlocMap_IDL_result()
        try:
            result.success = self._handler.addRemotePrefixRlocMap_IDL(args.lispHandle, args.eidInstanceId, args.prefixAF, args.prefix, args.prefixLen, args.state, args.remoteRlocs)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('addRemotePrefixRlocMap_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_removeRemotePrefixRlocMap_IDL(self, seqid, iprot, oprot):
        args = removeRemotePrefixRlocMap_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = removeRemotePrefixRlocMap_IDL_result()
        try:
            result.success = self._handler.removeRemotePrefixRlocMap_IDL(args.lispHandle, args.eidInstanceId, args.prefixAF, args.prefix, args.prefixLen, args.rlocAF, args.rloc)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('removeRemotePrefixRlocMap_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_addPrefixToSite_IDL(self, seqid, iprot, oprot):
        args = addPrefixToSite_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = addPrefixToSite_IDL_result()
        try:
            result.success = self._handler.addPrefixToSite_IDL(args.lispHandle, args.siteHandle, args.eidInstanceId, args.prefixAF, args.prefix, args.prefixLen)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('addPrefixToSite_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_removePrefixFromSite_IDL(self, seqid, iprot, oprot):
        args = removePrefixFromSite_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = removePrefixFromSite_IDL_result()
        try:
            result.success = self._handler.removePrefixFromSite_IDL(args.lispHandle, args.siteHandle, args.eidInstanceId, args.prefixAF, args.prefix, args.prefixLen)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('removePrefixFromSite_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_setMapServerKey_IDL(self, seqid, iprot, oprot):
        args = setMapServerKey_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = setMapServerKey_IDL_result()
        try:
            result.success = self._handler.setMapServerKey_IDL(args.lispHandle, args.siteHandle, args.key)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('setMapServerKey_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_clearMapServerReg_IDL(self, seqid, iprot, oprot):
        args = clearMapServerReg_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = clearMapServerReg_IDL_result()
        try:
            result.success = self._handler.clearMapServerReg_IDL(args.lispHandle, args.siteHandle, args.eidInstanceId, args.prefixAF, args.prefix, args.prefixLen)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('clearMapServerReg_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_clearMapCacheEntry_IDL(self, seqid, iprot, oprot):
        args = clearMapCacheEntry_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = clearMapCacheEntry_IDL_result()
        try:
            result.success = self._handler.clearMapCacheEntry_IDL(args.lispHandle, args.eidInstanceId, args.prefixAF, args.prefix, args.prefixLen)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('clearMapCacheEntry_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_findMapCacheEntry_IDL(self, seqid, iprot, oprot):
        args = findMapCacheEntry_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = findMapCacheEntry_IDL_result()
        try:
            result.success = self._handler.findMapCacheEntry_IDL(args.lispHandle, args.eidInstanceId, args.prefixAF, args.prefix, args.prefixLen)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('findMapCacheEntry_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_findMapCacheLongestMatchEntry_IDL(self, seqid, iprot, oprot):
        args = findMapCacheLongestMatchEntry_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = findMapCacheLongestMatchEntry_IDL_result()
        try:
            result.success = self._handler.findMapCacheLongestMatchEntry_IDL(args.lispHandle, args.eidInstanceId, args.addrAF, args.addr)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('findMapCacheLongestMatchEntry_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_signalMapCache_IDL(self, seqid, iprot, oprot):
        args = signalMapCache_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = signalMapCache_IDL_result()
        try:
            result.success = self._handler.signalMapCache_IDL(args.lispHandle, args.eidInstanceId, args.addrAF, args.addr)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('signalMapCache_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_enableProbe_IDL(self, seqid, iprot, oprot):
        args = enableProbe_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = enableProbe_IDL_result()
        try:
            result.success = self._handler.enableProbe_IDL(args.lispHandle, args.eidInstanceId)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('enableProbe_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_disableProbe_IDL(self, seqid, iprot, oprot):
        args = disableProbe_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = disableProbe_IDL_result()
        try:
            result.success = self._handler.disableProbe_IDL(args.lispHandle, args.eidInstanceId)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('disableProbe_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()




class createLisp_IDL_args(object):
    """
    Attributes:
     - lispHandle
     - vrf
    """

    thrift_spec = (None, (1,
      TType.I32,
      'lispHandle',
      None,
      None), (2,
      TType.I32,
      'vrf',
      None,
      None))

    def __init__(self, lispHandle = None, vrf = None):
        self.lispHandle = lispHandle
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
                    self.lispHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.vrf = iprot.readI32()
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
        oprot.writeStructBegin('createLisp_IDL_args')
        if self.lispHandle != None:
            oprot.writeFieldBegin('lispHandle', TType.I32, 1)
            oprot.writeI32(self.lispHandle)
            oprot.writeFieldEnd()
        if self.vrf != None:
            oprot.writeFieldBegin('vrf', TType.I32, 2)
            oprot.writeI32(self.vrf)
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




class createLisp_IDL_result(object):
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
        oprot.writeStructBegin('createLisp_IDL_result')
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




class deleteLisp_IDL_args(object):
    """
    Attributes:
     - lispHandle
    """

    thrift_spec = (None, (1,
      TType.I32,
      'lispHandle',
      None,
      None))

    def __init__(self, lispHandle = None):
        self.lispHandle = lispHandle



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
                    self.lispHandle = iprot.readI32()
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
        oprot.writeStructBegin('deleteLisp_IDL_args')
        if self.lispHandle != None:
            oprot.writeFieldBegin('lispHandle', TType.I32, 1)
            oprot.writeI32(self.lispHandle)
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




class deleteLisp_IDL_result(object):
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
        oprot.writeStructBegin('deleteLisp_IDL_result')
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




class enableMapServer_IDL_args(object):
    """
    Attributes:
     - lispHandle
     - addrFamily
    """

    thrift_spec = (None, (1,
      TType.I32,
      'lispHandle',
      None,
      None), (2,
      TType.I32,
      'addrFamily',
      None,
      None))

    def __init__(self, lispHandle = None, addrFamily = None):
        self.lispHandle = lispHandle
        self.addrFamily = addrFamily



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
                    self.lispHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.addrFamily = iprot.readI32()
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
        oprot.writeStructBegin('enableMapServer_IDL_args')
        if self.lispHandle != None:
            oprot.writeFieldBegin('lispHandle', TType.I32, 1)
            oprot.writeI32(self.lispHandle)
            oprot.writeFieldEnd()
        if self.addrFamily != None:
            oprot.writeFieldBegin('addrFamily', TType.I32, 2)
            oprot.writeI32(self.addrFamily)
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




class enableMapServer_IDL_result(object):
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
        oprot.writeStructBegin('enableMapServer_IDL_result')
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




class disableMapServer_IDL_args(object):
    """
    Attributes:
     - lispHandle
     - addrFamily
    """

    thrift_spec = (None, (1,
      TType.I32,
      'lispHandle',
      None,
      None), (2,
      TType.I32,
      'addrFamily',
      None,
      None))

    def __init__(self, lispHandle = None, addrFamily = None):
        self.lispHandle = lispHandle
        self.addrFamily = addrFamily



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
                    self.lispHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.addrFamily = iprot.readI32()
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
        oprot.writeStructBegin('disableMapServer_IDL_args')
        if self.lispHandle != None:
            oprot.writeFieldBegin('lispHandle', TType.I32, 1)
            oprot.writeI32(self.lispHandle)
            oprot.writeFieldEnd()
        if self.addrFamily != None:
            oprot.writeFieldBegin('addrFamily', TType.I32, 2)
            oprot.writeI32(self.addrFamily)
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




class disableMapServer_IDL_result(object):
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
        oprot.writeStructBegin('disableMapServer_IDL_result')
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




class createSite_IDL_args(object):
    """
    Attributes:
     - lispHandle
     - siteHandle
    """

    thrift_spec = (None, (1,
      TType.I32,
      'lispHandle',
      None,
      None), (2,
      TType.I32,
      'siteHandle',
      None,
      None))

    def __init__(self, lispHandle = None, siteHandle = None):
        self.lispHandle = lispHandle
        self.siteHandle = siteHandle



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
                    self.lispHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.siteHandle = iprot.readI32()
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
        oprot.writeStructBegin('createSite_IDL_args')
        if self.lispHandle != None:
            oprot.writeFieldBegin('lispHandle', TType.I32, 1)
            oprot.writeI32(self.lispHandle)
            oprot.writeFieldEnd()
        if self.siteHandle != None:
            oprot.writeFieldBegin('siteHandle', TType.I32, 2)
            oprot.writeI32(self.siteHandle)
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




class createSite_IDL_result(object):
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
        oprot.writeStructBegin('createSite_IDL_result')
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




class deleteSite_IDL_args(object):
    """
    Attributes:
     - lispHandle
     - siteHandle
    """

    thrift_spec = (None, (1,
      TType.I32,
      'lispHandle',
      None,
      None), (2,
      TType.I32,
      'siteHandle',
      None,
      None))

    def __init__(self, lispHandle = None, siteHandle = None):
        self.lispHandle = lispHandle
        self.siteHandle = siteHandle



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
                    self.lispHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.siteHandle = iprot.readI32()
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
        oprot.writeStructBegin('deleteSite_IDL_args')
        if self.lispHandle != None:
            oprot.writeFieldBegin('lispHandle', TType.I32, 1)
            oprot.writeI32(self.lispHandle)
            oprot.writeFieldEnd()
        if self.siteHandle != None:
            oprot.writeFieldBegin('siteHandle', TType.I32, 2)
            oprot.writeI32(self.siteHandle)
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




class deleteSite_IDL_result(object):
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
        oprot.writeStructBegin('deleteSite_IDL_result')
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




class enableMapResolver_IDL_args(object):
    """
    Attributes:
     - lispHandle
     - addrFamily
    """

    thrift_spec = (None, (1,
      TType.I32,
      'lispHandle',
      None,
      None), (2,
      TType.I32,
      'addrFamily',
      None,
      None))

    def __init__(self, lispHandle = None, addrFamily = None):
        self.lispHandle = lispHandle
        self.addrFamily = addrFamily



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
                    self.lispHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.addrFamily = iprot.readI32()
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
        oprot.writeStructBegin('enableMapResolver_IDL_args')
        if self.lispHandle != None:
            oprot.writeFieldBegin('lispHandle', TType.I32, 1)
            oprot.writeI32(self.lispHandle)
            oprot.writeFieldEnd()
        if self.addrFamily != None:
            oprot.writeFieldBegin('addrFamily', TType.I32, 2)
            oprot.writeI32(self.addrFamily)
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




class enableMapResolver_IDL_result(object):
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
        oprot.writeStructBegin('enableMapResolver_IDL_result')
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




class disableMapResolver_IDL_args(object):
    """
    Attributes:
     - lispHandle
     - addrFamily
    """

    thrift_spec = (None, (1,
      TType.I32,
      'lispHandle',
      None,
      None), (2,
      TType.I32,
      'addrFamily',
      None,
      None))

    def __init__(self, lispHandle = None, addrFamily = None):
        self.lispHandle = lispHandle
        self.addrFamily = addrFamily



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
                    self.lispHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.addrFamily = iprot.readI32()
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
        oprot.writeStructBegin('disableMapResolver_IDL_args')
        if self.lispHandle != None:
            oprot.writeFieldBegin('lispHandle', TType.I32, 1)
            oprot.writeI32(self.lispHandle)
            oprot.writeFieldEnd()
        if self.addrFamily != None:
            oprot.writeFieldBegin('addrFamily', TType.I32, 2)
            oprot.writeI32(self.addrFamily)
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




class disableMapResolver_IDL_result(object):
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
        oprot.writeStructBegin('disableMapResolver_IDL_result')
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




class createEidTable_IDL_args(object):
    """
    Attributes:
     - lispHandle
     - eidInstanceId
     - vrf
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'lispHandle',
      None,
      None),
     (2,
      TType.I32,
      'eidInstanceId',
      None,
      None),
     (3,
      TType.I32,
      'vrf',
      None,
      None))

    def __init__(self, lispHandle = None, eidInstanceId = None, vrf = None):
        self.lispHandle = lispHandle
        self.eidInstanceId = eidInstanceId
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
                    self.lispHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.eidInstanceId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.vrf = iprot.readI32()
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
        oprot.writeStructBegin('createEidTable_IDL_args')
        if self.lispHandle != None:
            oprot.writeFieldBegin('lispHandle', TType.I32, 1)
            oprot.writeI32(self.lispHandle)
            oprot.writeFieldEnd()
        if self.eidInstanceId != None:
            oprot.writeFieldBegin('eidInstanceId', TType.I32, 2)
            oprot.writeI32(self.eidInstanceId)
            oprot.writeFieldEnd()
        if self.vrf != None:
            oprot.writeFieldBegin('vrf', TType.I32, 3)
            oprot.writeI32(self.vrf)
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




class createEidTable_IDL_result(object):
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
        oprot.writeStructBegin('createEidTable_IDL_result')
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




class deleteEidTable_IDL_args(object):
    """
    Attributes:
     - lispHandle
     - eidInstanceId
    """

    thrift_spec = (None, (1,
      TType.I32,
      'lispHandle',
      None,
      None), (2,
      TType.I32,
      'eidInstanceId',
      None,
      None))

    def __init__(self, lispHandle = None, eidInstanceId = None):
        self.lispHandle = lispHandle
        self.eidInstanceId = eidInstanceId



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
                    self.lispHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.eidInstanceId = iprot.readI32()
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
        oprot.writeStructBegin('deleteEidTable_IDL_args')
        if self.lispHandle != None:
            oprot.writeFieldBegin('lispHandle', TType.I32, 1)
            oprot.writeI32(self.lispHandle)
            oprot.writeFieldEnd()
        if self.eidInstanceId != None:
            oprot.writeFieldBegin('eidInstanceId', TType.I32, 2)
            oprot.writeI32(self.eidInstanceId)
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




class deleteEidTable_IDL_result(object):
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
        oprot.writeStructBegin('deleteEidTable_IDL_result')
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




class enableXtr_IDL_args(object):
    """
    Attributes:
     - lispHandle
     - eidInstanceId
     - type
     - addrFamily
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'lispHandle',
      None,
      None),
     (2,
      TType.I32,
      'eidInstanceId',
      None,
      None),
     (3,
      TType.I32,
      'type',
      None,
      None),
     (4,
      TType.I32,
      'addrFamily',
      None,
      None))

    def __init__(self, lispHandle = None, eidInstanceId = None, type = None, addrFamily = None):
        self.lispHandle = lispHandle
        self.eidInstanceId = eidInstanceId
        self.type = type
        self.addrFamily = addrFamily



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
                    self.lispHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.eidInstanceId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.addrFamily = iprot.readI32()
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
        oprot.writeStructBegin('enableXtr_IDL_args')
        if self.lispHandle != None:
            oprot.writeFieldBegin('lispHandle', TType.I32, 1)
            oprot.writeI32(self.lispHandle)
            oprot.writeFieldEnd()
        if self.eidInstanceId != None:
            oprot.writeFieldBegin('eidInstanceId', TType.I32, 2)
            oprot.writeI32(self.eidInstanceId)
            oprot.writeFieldEnd()
        if self.type != None:
            oprot.writeFieldBegin('type', TType.I32, 3)
            oprot.writeI32(self.type)
            oprot.writeFieldEnd()
        if self.addrFamily != None:
            oprot.writeFieldBegin('addrFamily', TType.I32, 4)
            oprot.writeI32(self.addrFamily)
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




class enableXtr_IDL_result(object):
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
        oprot.writeStructBegin('enableXtr_IDL_result')
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




class disableXtr_IDL_args(object):
    """
    Attributes:
     - lispHandle
     - eidInstanceId
     - type
     - addrFamily
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'lispHandle',
      None,
      None),
     (2,
      TType.I32,
      'eidInstanceId',
      None,
      None),
     (3,
      TType.I32,
      'type',
      None,
      None),
     (4,
      TType.I32,
      'addrFamily',
      None,
      None))

    def __init__(self, lispHandle = None, eidInstanceId = None, type = None, addrFamily = None):
        self.lispHandle = lispHandle
        self.eidInstanceId = eidInstanceId
        self.type = type
        self.addrFamily = addrFamily



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
                    self.lispHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.eidInstanceId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.addrFamily = iprot.readI32()
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
        oprot.writeStructBegin('disableXtr_IDL_args')
        if self.lispHandle != None:
            oprot.writeFieldBegin('lispHandle', TType.I32, 1)
            oprot.writeI32(self.lispHandle)
            oprot.writeFieldEnd()
        if self.eidInstanceId != None:
            oprot.writeFieldBegin('eidInstanceId', TType.I32, 2)
            oprot.writeI32(self.eidInstanceId)
            oprot.writeFieldEnd()
        if self.type != None:
            oprot.writeFieldBegin('type', TType.I32, 3)
            oprot.writeI32(self.type)
            oprot.writeFieldEnd()
        if self.addrFamily != None:
            oprot.writeFieldBegin('addrFamily', TType.I32, 4)
            oprot.writeI32(self.addrFamily)
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




class disableXtr_IDL_result(object):
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
        oprot.writeStructBegin('disableXtr_IDL_result')
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




class enablePitr_IDL_args(object):
    """
    Attributes:
     - lispHandle
     - eidInstanceId
     - addrFamily
     - address
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'lispHandle',
      None,
      None),
     (2,
      TType.I32,
      'eidInstanceId',
      None,
      None),
     (3,
      TType.I32,
      'addrFamily',
      None,
      None),
     (4,
      TType.LIST,
      'address',
      (TType.STRUCT, (RlocIDL, RlocIDL.thrift_spec)),
      None))

    def __init__(self, lispHandle = None, eidInstanceId = None, addrFamily = None, address = None):
        self.lispHandle = lispHandle
        self.eidInstanceId = eidInstanceId
        self.addrFamily = addrFamily
        self.address = address



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
                    self.lispHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.eidInstanceId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.addrFamily = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.LIST:
                    self.address = []
                    (_etype10, _size7,) = iprot.readListBegin()
                    for _i11 in xrange(_size7):
                        _elem12 = RlocIDL()
                        _elem12.read(iprot)
                        self.address.append(_elem12)

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
        oprot.writeStructBegin('enablePitr_IDL_args')
        if self.lispHandle != None:
            oprot.writeFieldBegin('lispHandle', TType.I32, 1)
            oprot.writeI32(self.lispHandle)
            oprot.writeFieldEnd()
        if self.eidInstanceId != None:
            oprot.writeFieldBegin('eidInstanceId', TType.I32, 2)
            oprot.writeI32(self.eidInstanceId)
            oprot.writeFieldEnd()
        if self.addrFamily != None:
            oprot.writeFieldBegin('addrFamily', TType.I32, 3)
            oprot.writeI32(self.addrFamily)
            oprot.writeFieldEnd()
        if self.address != None:
            oprot.writeFieldBegin('address', TType.LIST, 4)
            oprot.writeListBegin(TType.STRUCT, len(self.address))
            for iter13 in self.address:
                iter13.write(oprot)

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




class enablePitr_IDL_result(object):
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
        oprot.writeStructBegin('enablePitr_IDL_result')
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




class addItrMapResolver_IDL_args(object):
    """
    Attributes:
     - lispHandle
     - eidInstanceId
     - eidAF
     - addressAF
     - address
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'lispHandle',
      None,
      None),
     (2,
      TType.I32,
      'eidInstanceId',
      None,
      None),
     (3,
      TType.I32,
      'eidAF',
      None,
      None),
     (4,
      TType.I32,
      'addressAF',
      None,
      None),
     (5,
      TType.STRING,
      'address',
      None,
      None))

    def __init__(self, lispHandle = None, eidInstanceId = None, eidAF = None, addressAF = None, address = None):
        self.lispHandle = lispHandle
        self.eidInstanceId = eidInstanceId
        self.eidAF = eidAF
        self.addressAF = addressAF
        self.address = address



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
                    self.lispHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.eidInstanceId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.eidAF = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.addressAF = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.address = iprot.readString()
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
        oprot.writeStructBegin('addItrMapResolver_IDL_args')
        if self.lispHandle != None:
            oprot.writeFieldBegin('lispHandle', TType.I32, 1)
            oprot.writeI32(self.lispHandle)
            oprot.writeFieldEnd()
        if self.eidInstanceId != None:
            oprot.writeFieldBegin('eidInstanceId', TType.I32, 2)
            oprot.writeI32(self.eidInstanceId)
            oprot.writeFieldEnd()
        if self.eidAF != None:
            oprot.writeFieldBegin('eidAF', TType.I32, 3)
            oprot.writeI32(self.eidAF)
            oprot.writeFieldEnd()
        if self.addressAF != None:
            oprot.writeFieldBegin('addressAF', TType.I32, 4)
            oprot.writeI32(self.addressAF)
            oprot.writeFieldEnd()
        if self.address != None:
            oprot.writeFieldBegin('address', TType.STRING, 5)
            oprot.writeString(self.address)
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




class addItrMapResolver_IDL_result(object):
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
        oprot.writeStructBegin('addItrMapResolver_IDL_result')
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




class removeItrMapResolver_IDL_args(object):
    """
    Attributes:
     - lispHandle
     - eidInstanceId
     - eidAF
     - addressAF
     - address
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'lispHandle',
      None,
      None),
     (2,
      TType.I32,
      'eidInstanceId',
      None,
      None),
     (3,
      TType.I32,
      'eidAF',
      None,
      None),
     (4,
      TType.I32,
      'addressAF',
      None,
      None),
     (5,
      TType.STRING,
      'address',
      None,
      None))

    def __init__(self, lispHandle = None, eidInstanceId = None, eidAF = None, addressAF = None, address = None):
        self.lispHandle = lispHandle
        self.eidInstanceId = eidInstanceId
        self.eidAF = eidAF
        self.addressAF = addressAF
        self.address = address



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
                    self.lispHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.eidInstanceId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.eidAF = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.addressAF = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.address = iprot.readString()
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
        oprot.writeStructBegin('removeItrMapResolver_IDL_args')
        if self.lispHandle != None:
            oprot.writeFieldBegin('lispHandle', TType.I32, 1)
            oprot.writeI32(self.lispHandle)
            oprot.writeFieldEnd()
        if self.eidInstanceId != None:
            oprot.writeFieldBegin('eidInstanceId', TType.I32, 2)
            oprot.writeI32(self.eidInstanceId)
            oprot.writeFieldEnd()
        if self.eidAF != None:
            oprot.writeFieldBegin('eidAF', TType.I32, 3)
            oprot.writeI32(self.eidAF)
            oprot.writeFieldEnd()
        if self.addressAF != None:
            oprot.writeFieldBegin('addressAF', TType.I32, 4)
            oprot.writeI32(self.addressAF)
            oprot.writeFieldEnd()
        if self.address != None:
            oprot.writeFieldBegin('address', TType.STRING, 5)
            oprot.writeString(self.address)
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




class removeItrMapResolver_IDL_result(object):
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
        oprot.writeStructBegin('removeItrMapResolver_IDL_result')
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




class addEtrMapServer_IDL_args(object):
    """
    Attributes:
     - lispHandle
     - eidInstanceId
     - eidAF
     - addressAF
     - address
     - key
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'lispHandle',
      None,
      None),
     (2,
      TType.I32,
      'eidInstanceId',
      None,
      None),
     (3,
      TType.I32,
      'eidAF',
      None,
      None),
     (4,
      TType.I32,
      'addressAF',
      None,
      None),
     (5,
      TType.STRING,
      'address',
      None,
      None),
     (6,
      TType.STRING,
      'key',
      None,
      None))

    def __init__(self, lispHandle = None, eidInstanceId = None, eidAF = None, addressAF = None, address = None, key = None):
        self.lispHandle = lispHandle
        self.eidInstanceId = eidInstanceId
        self.eidAF = eidAF
        self.addressAF = addressAF
        self.address = address
        self.key = key



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
                    self.lispHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.eidInstanceId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.eidAF = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.addressAF = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.address = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRING:
                    self.key = iprot.readString()
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
        oprot.writeStructBegin('addEtrMapServer_IDL_args')
        if self.lispHandle != None:
            oprot.writeFieldBegin('lispHandle', TType.I32, 1)
            oprot.writeI32(self.lispHandle)
            oprot.writeFieldEnd()
        if self.eidInstanceId != None:
            oprot.writeFieldBegin('eidInstanceId', TType.I32, 2)
            oprot.writeI32(self.eidInstanceId)
            oprot.writeFieldEnd()
        if self.eidAF != None:
            oprot.writeFieldBegin('eidAF', TType.I32, 3)
            oprot.writeI32(self.eidAF)
            oprot.writeFieldEnd()
        if self.addressAF != None:
            oprot.writeFieldBegin('addressAF', TType.I32, 4)
            oprot.writeI32(self.addressAF)
            oprot.writeFieldEnd()
        if self.address != None:
            oprot.writeFieldBegin('address', TType.STRING, 5)
            oprot.writeString(self.address)
            oprot.writeFieldEnd()
        if self.key != None:
            oprot.writeFieldBegin('key', TType.STRING, 6)
            oprot.writeString(self.key)
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




class addEtrMapServer_IDL_result(object):
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
        oprot.writeStructBegin('addEtrMapServer_IDL_result')
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




class removeEtrMapServer_IDL_args(object):
    """
    Attributes:
     - lispHandle
     - eidInstanceId
     - eidAF
     - addressAF
     - address
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'lispHandle',
      None,
      None),
     (2,
      TType.I32,
      'eidInstanceId',
      None,
      None),
     (3,
      TType.I32,
      'eidAF',
      None,
      None),
     (4,
      TType.I32,
      'addressAF',
      None,
      None),
     (5,
      TType.STRING,
      'address',
      None,
      None))

    def __init__(self, lispHandle = None, eidInstanceId = None, eidAF = None, addressAF = None, address = None):
        self.lispHandle = lispHandle
        self.eidInstanceId = eidInstanceId
        self.eidAF = eidAF
        self.addressAF = addressAF
        self.address = address



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
                    self.lispHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.eidInstanceId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.eidAF = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.addressAF = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.address = iprot.readString()
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
        oprot.writeStructBegin('removeEtrMapServer_IDL_args')
        if self.lispHandle != None:
            oprot.writeFieldBegin('lispHandle', TType.I32, 1)
            oprot.writeI32(self.lispHandle)
            oprot.writeFieldEnd()
        if self.eidInstanceId != None:
            oprot.writeFieldBegin('eidInstanceId', TType.I32, 2)
            oprot.writeI32(self.eidInstanceId)
            oprot.writeFieldEnd()
        if self.eidAF != None:
            oprot.writeFieldBegin('eidAF', TType.I32, 3)
            oprot.writeI32(self.eidAF)
            oprot.writeFieldEnd()
        if self.addressAF != None:
            oprot.writeFieldBegin('addressAF', TType.I32, 4)
            oprot.writeI32(self.addressAF)
            oprot.writeFieldEnd()
        if self.address != None:
            oprot.writeFieldBegin('address', TType.STRING, 5)
            oprot.writeString(self.address)
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




class removeEtrMapServer_IDL_result(object):
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
        oprot.writeStructBegin('removeEtrMapServer_IDL_result')
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




class addLocalPrefix_IDL_args(object):
    """
    Attributes:
     - lispHandle
     - eidInstanceId
     - prefixAF
     - prefix
     - prefixLen
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'lispHandle',
      None,
      None),
     (2,
      TType.I32,
      'eidInstanceId',
      None,
      None),
     (3,
      TType.I32,
      'prefixAF',
      None,
      None),
     (4,
      TType.STRING,
      'prefix',
      None,
      None),
     (5,
      TType.I16,
      'prefixLen',
      None,
      None))

    def __init__(self, lispHandle = None, eidInstanceId = None, prefixAF = None, prefix = None, prefixLen = None):
        self.lispHandle = lispHandle
        self.eidInstanceId = eidInstanceId
        self.prefixAF = prefixAF
        self.prefix = prefix
        self.prefixLen = prefixLen



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
                    self.lispHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.eidInstanceId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.prefixAF = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.prefix = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I16:
                    self.prefixLen = iprot.readI16()
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
        oprot.writeStructBegin('addLocalPrefix_IDL_args')
        if self.lispHandle != None:
            oprot.writeFieldBegin('lispHandle', TType.I32, 1)
            oprot.writeI32(self.lispHandle)
            oprot.writeFieldEnd()
        if self.eidInstanceId != None:
            oprot.writeFieldBegin('eidInstanceId', TType.I32, 2)
            oprot.writeI32(self.eidInstanceId)
            oprot.writeFieldEnd()
        if self.prefixAF != None:
            oprot.writeFieldBegin('prefixAF', TType.I32, 3)
            oprot.writeI32(self.prefixAF)
            oprot.writeFieldEnd()
        if self.prefix != None:
            oprot.writeFieldBegin('prefix', TType.STRING, 4)
            oprot.writeString(self.prefix)
            oprot.writeFieldEnd()
        if self.prefixLen != None:
            oprot.writeFieldBegin('prefixLen', TType.I16, 5)
            oprot.writeI16(self.prefixLen)
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




class addLocalPrefix_IDL_result(object):
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
        oprot.writeStructBegin('addLocalPrefix_IDL_result')
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




class removeLocalPrefix_IDL_args(object):
    """
    Attributes:
     - lispHandle
     - eidInstanceId
     - prefixAF
     - prefix
     - prefixLen
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'lispHandle',
      None,
      None),
     (2,
      TType.I32,
      'eidInstanceId',
      None,
      None),
     (3,
      TType.I32,
      'prefixAF',
      None,
      None),
     (4,
      TType.STRING,
      'prefix',
      None,
      None),
     (5,
      TType.I16,
      'prefixLen',
      None,
      None))

    def __init__(self, lispHandle = None, eidInstanceId = None, prefixAF = None, prefix = None, prefixLen = None):
        self.lispHandle = lispHandle
        self.eidInstanceId = eidInstanceId
        self.prefixAF = prefixAF
        self.prefix = prefix
        self.prefixLen = prefixLen



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
                    self.lispHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.eidInstanceId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.prefixAF = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.prefix = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I16:
                    self.prefixLen = iprot.readI16()
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
        oprot.writeStructBegin('removeLocalPrefix_IDL_args')
        if self.lispHandle != None:
            oprot.writeFieldBegin('lispHandle', TType.I32, 1)
            oprot.writeI32(self.lispHandle)
            oprot.writeFieldEnd()
        if self.eidInstanceId != None:
            oprot.writeFieldBegin('eidInstanceId', TType.I32, 2)
            oprot.writeI32(self.eidInstanceId)
            oprot.writeFieldEnd()
        if self.prefixAF != None:
            oprot.writeFieldBegin('prefixAF', TType.I32, 3)
            oprot.writeI32(self.prefixAF)
            oprot.writeFieldEnd()
        if self.prefix != None:
            oprot.writeFieldBegin('prefix', TType.STRING, 4)
            oprot.writeString(self.prefix)
            oprot.writeFieldEnd()
        if self.prefixLen != None:
            oprot.writeFieldBegin('prefixLen', TType.I16, 5)
            oprot.writeI16(self.prefixLen)
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




class removeLocalPrefix_IDL_result(object):
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
        oprot.writeStructBegin('removeLocalPrefix_IDL_result')
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




class addLocalPrefixRlocMap_IDL_args(object):
    """
    Attributes:
     - lispHandle
     - eidInstanceId
     - prefixAF
     - prefix
     - prefixLen
     - localRlocs
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'lispHandle',
      None,
      None),
     (2,
      TType.I32,
      'eidInstanceId',
      None,
      None),
     (3,
      TType.I32,
      'prefixAF',
      None,
      None),
     (4,
      TType.STRING,
      'prefix',
      None,
      None),
     (5,
      TType.I16,
      'prefixLen',
      None,
      None),
     (6,
      TType.LIST,
      'localRlocs',
      (TType.STRUCT, (LocalRlocIDL, LocalRlocIDL.thrift_spec)),
      None))

    def __init__(self, lispHandle = None, eidInstanceId = None, prefixAF = None, prefix = None, prefixLen = None, localRlocs = None):
        self.lispHandle = lispHandle
        self.eidInstanceId = eidInstanceId
        self.prefixAF = prefixAF
        self.prefix = prefix
        self.prefixLen = prefixLen
        self.localRlocs = localRlocs



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
                    self.lispHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.eidInstanceId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.prefixAF = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.prefix = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I16:
                    self.prefixLen = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.LIST:
                    self.localRlocs = []
                    (_etype17, _size14,) = iprot.readListBegin()
                    for _i18 in xrange(_size14):
                        _elem19 = LocalRlocIDL()
                        _elem19.read(iprot)
                        self.localRlocs.append(_elem19)

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
        oprot.writeStructBegin('addLocalPrefixRlocMap_IDL_args')
        if self.lispHandle != None:
            oprot.writeFieldBegin('lispHandle', TType.I32, 1)
            oprot.writeI32(self.lispHandle)
            oprot.writeFieldEnd()
        if self.eidInstanceId != None:
            oprot.writeFieldBegin('eidInstanceId', TType.I32, 2)
            oprot.writeI32(self.eidInstanceId)
            oprot.writeFieldEnd()
        if self.prefixAF != None:
            oprot.writeFieldBegin('prefixAF', TType.I32, 3)
            oprot.writeI32(self.prefixAF)
            oprot.writeFieldEnd()
        if self.prefix != None:
            oprot.writeFieldBegin('prefix', TType.STRING, 4)
            oprot.writeString(self.prefix)
            oprot.writeFieldEnd()
        if self.prefixLen != None:
            oprot.writeFieldBegin('prefixLen', TType.I16, 5)
            oprot.writeI16(self.prefixLen)
            oprot.writeFieldEnd()
        if self.localRlocs != None:
            oprot.writeFieldBegin('localRlocs', TType.LIST, 6)
            oprot.writeListBegin(TType.STRUCT, len(self.localRlocs))
            for iter20 in self.localRlocs:
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




class addLocalPrefixRlocMap_IDL_result(object):
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
        oprot.writeStructBegin('addLocalPrefixRlocMap_IDL_result')
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




class removeLocalPrefixRlocMap_IDL_args(object):
    """
    Attributes:
     - lispHandle
     - eidInstanceId
     - prefixAF
     - prefix
     - prefixLen
     - rlocAF
     - rloc
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'lispHandle',
      None,
      None),
     (2,
      TType.I32,
      'eidInstanceId',
      None,
      None),
     (3,
      TType.I32,
      'prefixAF',
      None,
      None),
     (4,
      TType.STRING,
      'prefix',
      None,
      None),
     (5,
      TType.I16,
      'prefixLen',
      None,
      None),
     (6,
      TType.I32,
      'rlocAF',
      None,
      None),
     (7,
      TType.STRING,
      'rloc',
      None,
      None))

    def __init__(self, lispHandle = None, eidInstanceId = None, prefixAF = None, prefix = None, prefixLen = None, rlocAF = None, rloc = None):
        self.lispHandle = lispHandle
        self.eidInstanceId = eidInstanceId
        self.prefixAF = prefixAF
        self.prefix = prefix
        self.prefixLen = prefixLen
        self.rlocAF = rlocAF
        self.rloc = rloc



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
                    self.lispHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.eidInstanceId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.prefixAF = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.prefix = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I16:
                    self.prefixLen = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I32:
                    self.rlocAF = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.STRING:
                    self.rloc = iprot.readString()
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
        oprot.writeStructBegin('removeLocalPrefixRlocMap_IDL_args')
        if self.lispHandle != None:
            oprot.writeFieldBegin('lispHandle', TType.I32, 1)
            oprot.writeI32(self.lispHandle)
            oprot.writeFieldEnd()
        if self.eidInstanceId != None:
            oprot.writeFieldBegin('eidInstanceId', TType.I32, 2)
            oprot.writeI32(self.eidInstanceId)
            oprot.writeFieldEnd()
        if self.prefixAF != None:
            oprot.writeFieldBegin('prefixAF', TType.I32, 3)
            oprot.writeI32(self.prefixAF)
            oprot.writeFieldEnd()
        if self.prefix != None:
            oprot.writeFieldBegin('prefix', TType.STRING, 4)
            oprot.writeString(self.prefix)
            oprot.writeFieldEnd()
        if self.prefixLen != None:
            oprot.writeFieldBegin('prefixLen', TType.I16, 5)
            oprot.writeI16(self.prefixLen)
            oprot.writeFieldEnd()
        if self.rlocAF != None:
            oprot.writeFieldBegin('rlocAF', TType.I32, 6)
            oprot.writeI32(self.rlocAF)
            oprot.writeFieldEnd()
        if self.rloc != None:
            oprot.writeFieldBegin('rloc', TType.STRING, 7)
            oprot.writeString(self.rloc)
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




class removeLocalPrefixRlocMap_IDL_result(object):
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
        oprot.writeStructBegin('removeLocalPrefixRlocMap_IDL_result')
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




class addLocalPrefixIfcMap_IDL_args(object):
    """
    Attributes:
     - lispHandle
     - eidInstanceId
     - prefixAF
     - prefix
     - prefixLen
     - ifHandle
     - addrFamily
     - priority
     - weight
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'lispHandle',
      None,
      None),
     (2,
      TType.I32,
      'eidInstanceId',
      None,
      None),
     (3,
      TType.I32,
      'prefixAF',
      None,
      None),
     (4,
      TType.STRING,
      'prefix',
      None,
      None),
     (5,
      TType.I16,
      'prefixLen',
      None,
      None),
     (6,
      TType.I64,
      'ifHandle',
      None,
      None),
     (7,
      TType.I32,
      'addrFamily',
      None,
      None),
     (8,
      TType.BYTE,
      'priority',
      None,
      None),
     (9,
      TType.BYTE,
      'weight',
      None,
      None))

    def __init__(self, lispHandle = None, eidInstanceId = None, prefixAF = None, prefix = None, prefixLen = None, ifHandle = None, addrFamily = None, priority = None, weight = None):
        self.lispHandle = lispHandle
        self.eidInstanceId = eidInstanceId
        self.prefixAF = prefixAF
        self.prefix = prefix
        self.prefixLen = prefixLen
        self.ifHandle = ifHandle
        self.addrFamily = addrFamily
        self.priority = priority
        self.weight = weight



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
                    self.lispHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.eidInstanceId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.prefixAF = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.prefix = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I16:
                    self.prefixLen = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I64:
                    self.ifHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I32:
                    self.addrFamily = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.BYTE:
                    self.priority = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.BYTE:
                    self.weight = iprot.readByte()
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
        oprot.writeStructBegin('addLocalPrefixIfcMap_IDL_args')
        if self.lispHandle != None:
            oprot.writeFieldBegin('lispHandle', TType.I32, 1)
            oprot.writeI32(self.lispHandle)
            oprot.writeFieldEnd()
        if self.eidInstanceId != None:
            oprot.writeFieldBegin('eidInstanceId', TType.I32, 2)
            oprot.writeI32(self.eidInstanceId)
            oprot.writeFieldEnd()
        if self.prefixAF != None:
            oprot.writeFieldBegin('prefixAF', TType.I32, 3)
            oprot.writeI32(self.prefixAF)
            oprot.writeFieldEnd()
        if self.prefix != None:
            oprot.writeFieldBegin('prefix', TType.STRING, 4)
            oprot.writeString(self.prefix)
            oprot.writeFieldEnd()
        if self.prefixLen != None:
            oprot.writeFieldBegin('prefixLen', TType.I16, 5)
            oprot.writeI16(self.prefixLen)
            oprot.writeFieldEnd()
        if self.ifHandle != None:
            oprot.writeFieldBegin('ifHandle', TType.I64, 6)
            oprot.writeI64(self.ifHandle)
            oprot.writeFieldEnd()
        if self.addrFamily != None:
            oprot.writeFieldBegin('addrFamily', TType.I32, 7)
            oprot.writeI32(self.addrFamily)
            oprot.writeFieldEnd()
        if self.priority != None:
            oprot.writeFieldBegin('priority', TType.BYTE, 8)
            oprot.writeByte(self.priority)
            oprot.writeFieldEnd()
        if self.weight != None:
            oprot.writeFieldBegin('weight', TType.BYTE, 9)
            oprot.writeByte(self.weight)
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




class addLocalPrefixIfcMap_IDL_result(object):
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
        oprot.writeStructBegin('addLocalPrefixIfcMap_IDL_result')
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




class removeLocalPrefixIfcMap_IDL_args(object):
    """
    Attributes:
     - lispHandle
     - eidInstanceId
     - prefixAF
     - prefix
     - prefixLen
     - ifHandle
     - addrFamily
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'lispHandle',
      None,
      None),
     (2,
      TType.I32,
      'eidInstanceId',
      None,
      None),
     (3,
      TType.I32,
      'prefixAF',
      None,
      None),
     (4,
      TType.STRING,
      'prefix',
      None,
      None),
     (5,
      TType.I16,
      'prefixLen',
      None,
      None),
     (6,
      TType.I64,
      'ifHandle',
      None,
      None),
     (7,
      TType.I32,
      'addrFamily',
      None,
      None))

    def __init__(self, lispHandle = None, eidInstanceId = None, prefixAF = None, prefix = None, prefixLen = None, ifHandle = None, addrFamily = None):
        self.lispHandle = lispHandle
        self.eidInstanceId = eidInstanceId
        self.prefixAF = prefixAF
        self.prefix = prefix
        self.prefixLen = prefixLen
        self.ifHandle = ifHandle
        self.addrFamily = addrFamily



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
                    self.lispHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.eidInstanceId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.prefixAF = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.prefix = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I16:
                    self.prefixLen = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I64:
                    self.ifHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I32:
                    self.addrFamily = iprot.readI32()
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
        oprot.writeStructBegin('removeLocalPrefixIfcMap_IDL_args')
        if self.lispHandle != None:
            oprot.writeFieldBegin('lispHandle', TType.I32, 1)
            oprot.writeI32(self.lispHandle)
            oprot.writeFieldEnd()
        if self.eidInstanceId != None:
            oprot.writeFieldBegin('eidInstanceId', TType.I32, 2)
            oprot.writeI32(self.eidInstanceId)
            oprot.writeFieldEnd()
        if self.prefixAF != None:
            oprot.writeFieldBegin('prefixAF', TType.I32, 3)
            oprot.writeI32(self.prefixAF)
            oprot.writeFieldEnd()
        if self.prefix != None:
            oprot.writeFieldBegin('prefix', TType.STRING, 4)
            oprot.writeString(self.prefix)
            oprot.writeFieldEnd()
        if self.prefixLen != None:
            oprot.writeFieldBegin('prefixLen', TType.I16, 5)
            oprot.writeI16(self.prefixLen)
            oprot.writeFieldEnd()
        if self.ifHandle != None:
            oprot.writeFieldBegin('ifHandle', TType.I64, 6)
            oprot.writeI64(self.ifHandle)
            oprot.writeFieldEnd()
        if self.addrFamily != None:
            oprot.writeFieldBegin('addrFamily', TType.I32, 7)
            oprot.writeI32(self.addrFamily)
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




class removeLocalPrefixIfcMap_IDL_result(object):
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
        oprot.writeStructBegin('removeLocalPrefixIfcMap_IDL_result')
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




class addRemotePrefix_IDL_args(object):
    """
    Attributes:
     - lispHandle
     - eidInstanceId
     - prefixAF
     - prefix
     - prefixLen
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'lispHandle',
      None,
      None),
     (2,
      TType.I32,
      'eidInstanceId',
      None,
      None),
     (3,
      TType.I32,
      'prefixAF',
      None,
      None),
     (4,
      TType.STRING,
      'prefix',
      None,
      None),
     (5,
      TType.I16,
      'prefixLen',
      None,
      None))

    def __init__(self, lispHandle = None, eidInstanceId = None, prefixAF = None, prefix = None, prefixLen = None):
        self.lispHandle = lispHandle
        self.eidInstanceId = eidInstanceId
        self.prefixAF = prefixAF
        self.prefix = prefix
        self.prefixLen = prefixLen



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
                    self.lispHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.eidInstanceId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.prefixAF = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.prefix = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I16:
                    self.prefixLen = iprot.readI16()
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
        oprot.writeStructBegin('addRemotePrefix_IDL_args')
        if self.lispHandle != None:
            oprot.writeFieldBegin('lispHandle', TType.I32, 1)
            oprot.writeI32(self.lispHandle)
            oprot.writeFieldEnd()
        if self.eidInstanceId != None:
            oprot.writeFieldBegin('eidInstanceId', TType.I32, 2)
            oprot.writeI32(self.eidInstanceId)
            oprot.writeFieldEnd()
        if self.prefixAF != None:
            oprot.writeFieldBegin('prefixAF', TType.I32, 3)
            oprot.writeI32(self.prefixAF)
            oprot.writeFieldEnd()
        if self.prefix != None:
            oprot.writeFieldBegin('prefix', TType.STRING, 4)
            oprot.writeString(self.prefix)
            oprot.writeFieldEnd()
        if self.prefixLen != None:
            oprot.writeFieldBegin('prefixLen', TType.I16, 5)
            oprot.writeI16(self.prefixLen)
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




class addRemotePrefix_IDL_result(object):
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
        oprot.writeStructBegin('addRemotePrefix_IDL_result')
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




class removeRemotePrefix_IDL_args(object):
    """
    Attributes:
     - lispHandle
     - eidInstanceId
     - prefixAF
     - prefix
     - prefixLen
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'lispHandle',
      None,
      None),
     (2,
      TType.I32,
      'eidInstanceId',
      None,
      None),
     (3,
      TType.I32,
      'prefixAF',
      None,
      None),
     (4,
      TType.STRING,
      'prefix',
      None,
      None),
     (5,
      TType.I16,
      'prefixLen',
      None,
      None))

    def __init__(self, lispHandle = None, eidInstanceId = None, prefixAF = None, prefix = None, prefixLen = None):
        self.lispHandle = lispHandle
        self.eidInstanceId = eidInstanceId
        self.prefixAF = prefixAF
        self.prefix = prefix
        self.prefixLen = prefixLen



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
                    self.lispHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.eidInstanceId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.prefixAF = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.prefix = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I16:
                    self.prefixLen = iprot.readI16()
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
        oprot.writeStructBegin('removeRemotePrefix_IDL_args')
        if self.lispHandle != None:
            oprot.writeFieldBegin('lispHandle', TType.I32, 1)
            oprot.writeI32(self.lispHandle)
            oprot.writeFieldEnd()
        if self.eidInstanceId != None:
            oprot.writeFieldBegin('eidInstanceId', TType.I32, 2)
            oprot.writeI32(self.eidInstanceId)
            oprot.writeFieldEnd()
        if self.prefixAF != None:
            oprot.writeFieldBegin('prefixAF', TType.I32, 3)
            oprot.writeI32(self.prefixAF)
            oprot.writeFieldEnd()
        if self.prefix != None:
            oprot.writeFieldBegin('prefix', TType.STRING, 4)
            oprot.writeString(self.prefix)
            oprot.writeFieldEnd()
        if self.prefixLen != None:
            oprot.writeFieldBegin('prefixLen', TType.I16, 5)
            oprot.writeI16(self.prefixLen)
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




class removeRemotePrefix_IDL_result(object):
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
        oprot.writeStructBegin('removeRemotePrefix_IDL_result')
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




class addMapServerAddressToEtr_IDL_args(object):
    """
    Attributes:
     - lispHandle
     - eidInstanceId
     - addrFamily
     - addr
     - key
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'lispHandle',
      None,
      None),
     (2,
      TType.I32,
      'eidInstanceId',
      None,
      None),
     (3,
      TType.I32,
      'addrFamily',
      None,
      None),
     (4,
      TType.STRING,
      'addr',
      None,
      None),
     (5,
      TType.STRING,
      'key',
      None,
      None))

    def __init__(self, lispHandle = None, eidInstanceId = None, addrFamily = None, addr = None, key = None):
        self.lispHandle = lispHandle
        self.eidInstanceId = eidInstanceId
        self.addrFamily = addrFamily
        self.addr = addr
        self.key = key



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
                    self.lispHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.eidInstanceId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.addrFamily = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.addr = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.key = iprot.readString()
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
        oprot.writeStructBegin('addMapServerAddressToEtr_IDL_args')
        if self.lispHandle != None:
            oprot.writeFieldBegin('lispHandle', TType.I32, 1)
            oprot.writeI32(self.lispHandle)
            oprot.writeFieldEnd()
        if self.eidInstanceId != None:
            oprot.writeFieldBegin('eidInstanceId', TType.I32, 2)
            oprot.writeI32(self.eidInstanceId)
            oprot.writeFieldEnd()
        if self.addrFamily != None:
            oprot.writeFieldBegin('addrFamily', TType.I32, 3)
            oprot.writeI32(self.addrFamily)
            oprot.writeFieldEnd()
        if self.addr != None:
            oprot.writeFieldBegin('addr', TType.STRING, 4)
            oprot.writeString(self.addr)
            oprot.writeFieldEnd()
        if self.key != None:
            oprot.writeFieldBegin('key', TType.STRING, 5)
            oprot.writeString(self.key)
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




class addMapServerAddressToEtr_IDL_result(object):
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
        oprot.writeStructBegin('addMapServerAddressToEtr_IDL_result')
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




class addRemotePrefixRlocMap_IDL_args(object):
    """
    Attributes:
     - lispHandle
     - eidInstanceId
     - prefixAF
     - prefix
     - prefixLen
     - state
     - remoteRlocs
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'lispHandle',
      None,
      None),
     (2,
      TType.I32,
      'eidInstanceId',
      None,
      None),
     (3,
      TType.I32,
      'prefixAF',
      None,
      None),
     (4,
      TType.STRING,
      'prefix',
      None,
      None),
     (5,
      TType.I16,
      'prefixLen',
      None,
      None),
     (6,
      TType.I32,
      'state',
      None,
      None),
     (7,
      TType.LIST,
      'remoteRlocs',
      (TType.STRUCT, (RemoteRlocIDL, RemoteRlocIDL.thrift_spec)),
      None))

    def __init__(self, lispHandle = None, eidInstanceId = None, prefixAF = None, prefix = None, prefixLen = None, state = None, remoteRlocs = None):
        self.lispHandle = lispHandle
        self.eidInstanceId = eidInstanceId
        self.prefixAF = prefixAF
        self.prefix = prefix
        self.prefixLen = prefixLen
        self.state = state
        self.remoteRlocs = remoteRlocs



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
                    self.lispHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.eidInstanceId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.prefixAF = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.prefix = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I16:
                    self.prefixLen = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I32:
                    self.state = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.LIST:
                    self.remoteRlocs = []
                    (_etype24, _size21,) = iprot.readListBegin()
                    for _i25 in xrange(_size21):
                        _elem26 = RemoteRlocIDL()
                        _elem26.read(iprot)
                        self.remoteRlocs.append(_elem26)

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
        oprot.writeStructBegin('addRemotePrefixRlocMap_IDL_args')
        if self.lispHandle != None:
            oprot.writeFieldBegin('lispHandle', TType.I32, 1)
            oprot.writeI32(self.lispHandle)
            oprot.writeFieldEnd()
        if self.eidInstanceId != None:
            oprot.writeFieldBegin('eidInstanceId', TType.I32, 2)
            oprot.writeI32(self.eidInstanceId)
            oprot.writeFieldEnd()
        if self.prefixAF != None:
            oprot.writeFieldBegin('prefixAF', TType.I32, 3)
            oprot.writeI32(self.prefixAF)
            oprot.writeFieldEnd()
        if self.prefix != None:
            oprot.writeFieldBegin('prefix', TType.STRING, 4)
            oprot.writeString(self.prefix)
            oprot.writeFieldEnd()
        if self.prefixLen != None:
            oprot.writeFieldBegin('prefixLen', TType.I16, 5)
            oprot.writeI16(self.prefixLen)
            oprot.writeFieldEnd()
        if self.state != None:
            oprot.writeFieldBegin('state', TType.I32, 6)
            oprot.writeI32(self.state)
            oprot.writeFieldEnd()
        if self.remoteRlocs != None:
            oprot.writeFieldBegin('remoteRlocs', TType.LIST, 7)
            oprot.writeListBegin(TType.STRUCT, len(self.remoteRlocs))
            for iter27 in self.remoteRlocs:
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




class addRemotePrefixRlocMap_IDL_result(object):
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
        oprot.writeStructBegin('addRemotePrefixRlocMap_IDL_result')
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




class removeRemotePrefixRlocMap_IDL_args(object):
    """
    Attributes:
     - lispHandle
     - eidInstanceId
     - prefixAF
     - prefix
     - prefixLen
     - rlocAF
     - rloc
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'lispHandle',
      None,
      None),
     (2,
      TType.I32,
      'eidInstanceId',
      None,
      None),
     (3,
      TType.I32,
      'prefixAF',
      None,
      None),
     (4,
      TType.STRING,
      'prefix',
      None,
      None),
     (5,
      TType.I16,
      'prefixLen',
      None,
      None),
     (6,
      TType.I32,
      'rlocAF',
      None,
      None),
     (7,
      TType.STRING,
      'rloc',
      None,
      None))

    def __init__(self, lispHandle = None, eidInstanceId = None, prefixAF = None, prefix = None, prefixLen = None, rlocAF = None, rloc = None):
        self.lispHandle = lispHandle
        self.eidInstanceId = eidInstanceId
        self.prefixAF = prefixAF
        self.prefix = prefix
        self.prefixLen = prefixLen
        self.rlocAF = rlocAF
        self.rloc = rloc



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
                    self.lispHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.eidInstanceId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.prefixAF = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.prefix = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I16:
                    self.prefixLen = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I32:
                    self.rlocAF = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.STRING:
                    self.rloc = iprot.readString()
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
        oprot.writeStructBegin('removeRemotePrefixRlocMap_IDL_args')
        if self.lispHandle != None:
            oprot.writeFieldBegin('lispHandle', TType.I32, 1)
            oprot.writeI32(self.lispHandle)
            oprot.writeFieldEnd()
        if self.eidInstanceId != None:
            oprot.writeFieldBegin('eidInstanceId', TType.I32, 2)
            oprot.writeI32(self.eidInstanceId)
            oprot.writeFieldEnd()
        if self.prefixAF != None:
            oprot.writeFieldBegin('prefixAF', TType.I32, 3)
            oprot.writeI32(self.prefixAF)
            oprot.writeFieldEnd()
        if self.prefix != None:
            oprot.writeFieldBegin('prefix', TType.STRING, 4)
            oprot.writeString(self.prefix)
            oprot.writeFieldEnd()
        if self.prefixLen != None:
            oprot.writeFieldBegin('prefixLen', TType.I16, 5)
            oprot.writeI16(self.prefixLen)
            oprot.writeFieldEnd()
        if self.rlocAF != None:
            oprot.writeFieldBegin('rlocAF', TType.I32, 6)
            oprot.writeI32(self.rlocAF)
            oprot.writeFieldEnd()
        if self.rloc != None:
            oprot.writeFieldBegin('rloc', TType.STRING, 7)
            oprot.writeString(self.rloc)
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




class removeRemotePrefixRlocMap_IDL_result(object):
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
        oprot.writeStructBegin('removeRemotePrefixRlocMap_IDL_result')
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




class addPrefixToSite_IDL_args(object):
    """
    Attributes:
     - lispHandle
     - siteHandle
     - eidInstanceId
     - prefixAF
     - prefix
     - prefixLen
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'lispHandle',
      None,
      None),
     (2,
      TType.I32,
      'siteHandle',
      None,
      None),
     (3,
      TType.I32,
      'eidInstanceId',
      None,
      None),
     (4,
      TType.I32,
      'prefixAF',
      None,
      None),
     (5,
      TType.STRING,
      'prefix',
      None,
      None),
     (6,
      TType.I16,
      'prefixLen',
      None,
      None))

    def __init__(self, lispHandle = None, siteHandle = None, eidInstanceId = None, prefixAF = None, prefix = None, prefixLen = None):
        self.lispHandle = lispHandle
        self.siteHandle = siteHandle
        self.eidInstanceId = eidInstanceId
        self.prefixAF = prefixAF
        self.prefix = prefix
        self.prefixLen = prefixLen



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
                    self.lispHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.siteHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.eidInstanceId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.prefixAF = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.prefix = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I16:
                    self.prefixLen = iprot.readI16()
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
        oprot.writeStructBegin('addPrefixToSite_IDL_args')
        if self.lispHandle != None:
            oprot.writeFieldBegin('lispHandle', TType.I32, 1)
            oprot.writeI32(self.lispHandle)
            oprot.writeFieldEnd()
        if self.siteHandle != None:
            oprot.writeFieldBegin('siteHandle', TType.I32, 2)
            oprot.writeI32(self.siteHandle)
            oprot.writeFieldEnd()
        if self.eidInstanceId != None:
            oprot.writeFieldBegin('eidInstanceId', TType.I32, 3)
            oprot.writeI32(self.eidInstanceId)
            oprot.writeFieldEnd()
        if self.prefixAF != None:
            oprot.writeFieldBegin('prefixAF', TType.I32, 4)
            oprot.writeI32(self.prefixAF)
            oprot.writeFieldEnd()
        if self.prefix != None:
            oprot.writeFieldBegin('prefix', TType.STRING, 5)
            oprot.writeString(self.prefix)
            oprot.writeFieldEnd()
        if self.prefixLen != None:
            oprot.writeFieldBegin('prefixLen', TType.I16, 6)
            oprot.writeI16(self.prefixLen)
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




class addPrefixToSite_IDL_result(object):
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
        oprot.writeStructBegin('addPrefixToSite_IDL_result')
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




class removePrefixFromSite_IDL_args(object):
    """
    Attributes:
     - lispHandle
     - siteHandle
     - eidInstanceId
     - prefixAF
     - prefix
     - prefixLen
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'lispHandle',
      None,
      None),
     (2,
      TType.I32,
      'siteHandle',
      None,
      None),
     (3,
      TType.I32,
      'eidInstanceId',
      None,
      None),
     (4,
      TType.I32,
      'prefixAF',
      None,
      None),
     (5,
      TType.STRING,
      'prefix',
      None,
      None),
     (6,
      TType.I16,
      'prefixLen',
      None,
      None))

    def __init__(self, lispHandle = None, siteHandle = None, eidInstanceId = None, prefixAF = None, prefix = None, prefixLen = None):
        self.lispHandle = lispHandle
        self.siteHandle = siteHandle
        self.eidInstanceId = eidInstanceId
        self.prefixAF = prefixAF
        self.prefix = prefix
        self.prefixLen = prefixLen



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
                    self.lispHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.siteHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.eidInstanceId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.prefixAF = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.prefix = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I16:
                    self.prefixLen = iprot.readI16()
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
        oprot.writeStructBegin('removePrefixFromSite_IDL_args')
        if self.lispHandle != None:
            oprot.writeFieldBegin('lispHandle', TType.I32, 1)
            oprot.writeI32(self.lispHandle)
            oprot.writeFieldEnd()
        if self.siteHandle != None:
            oprot.writeFieldBegin('siteHandle', TType.I32, 2)
            oprot.writeI32(self.siteHandle)
            oprot.writeFieldEnd()
        if self.eidInstanceId != None:
            oprot.writeFieldBegin('eidInstanceId', TType.I32, 3)
            oprot.writeI32(self.eidInstanceId)
            oprot.writeFieldEnd()
        if self.prefixAF != None:
            oprot.writeFieldBegin('prefixAF', TType.I32, 4)
            oprot.writeI32(self.prefixAF)
            oprot.writeFieldEnd()
        if self.prefix != None:
            oprot.writeFieldBegin('prefix', TType.STRING, 5)
            oprot.writeString(self.prefix)
            oprot.writeFieldEnd()
        if self.prefixLen != None:
            oprot.writeFieldBegin('prefixLen', TType.I16, 6)
            oprot.writeI16(self.prefixLen)
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




class removePrefixFromSite_IDL_result(object):
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
        oprot.writeStructBegin('removePrefixFromSite_IDL_result')
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




class setMapServerKey_IDL_args(object):
    """
    Attributes:
     - lispHandle
     - siteHandle
     - key
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'lispHandle',
      None,
      None),
     (2,
      TType.I32,
      'siteHandle',
      None,
      None),
     (3,
      TType.STRING,
      'key',
      None,
      None))

    def __init__(self, lispHandle = None, siteHandle = None, key = None):
        self.lispHandle = lispHandle
        self.siteHandle = siteHandle
        self.key = key



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
                    self.lispHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.siteHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.key = iprot.readString()
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
        oprot.writeStructBegin('setMapServerKey_IDL_args')
        if self.lispHandle != None:
            oprot.writeFieldBegin('lispHandle', TType.I32, 1)
            oprot.writeI32(self.lispHandle)
            oprot.writeFieldEnd()
        if self.siteHandle != None:
            oprot.writeFieldBegin('siteHandle', TType.I32, 2)
            oprot.writeI32(self.siteHandle)
            oprot.writeFieldEnd()
        if self.key != None:
            oprot.writeFieldBegin('key', TType.STRING, 3)
            oprot.writeString(self.key)
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




class setMapServerKey_IDL_result(object):
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
        oprot.writeStructBegin('setMapServerKey_IDL_result')
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




class clearMapServerReg_IDL_args(object):
    """
    Attributes:
     - lispHandle
     - siteHandle
     - eidInstanceId
     - prefixAF
     - prefix
     - prefixLen
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'lispHandle',
      None,
      None),
     (2,
      TType.I32,
      'siteHandle',
      None,
      None),
     (3,
      TType.I32,
      'eidInstanceId',
      None,
      None),
     (4,
      TType.I32,
      'prefixAF',
      None,
      None),
     (5,
      TType.STRING,
      'prefix',
      None,
      None),
     (6,
      TType.I16,
      'prefixLen',
      None,
      None))

    def __init__(self, lispHandle = None, siteHandle = None, eidInstanceId = None, prefixAF = None, prefix = None, prefixLen = None):
        self.lispHandle = lispHandle
        self.siteHandle = siteHandle
        self.eidInstanceId = eidInstanceId
        self.prefixAF = prefixAF
        self.prefix = prefix
        self.prefixLen = prefixLen



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
                    self.lispHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.siteHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.eidInstanceId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.prefixAF = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.prefix = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I16:
                    self.prefixLen = iprot.readI16()
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
        oprot.writeStructBegin('clearMapServerReg_IDL_args')
        if self.lispHandle != None:
            oprot.writeFieldBegin('lispHandle', TType.I32, 1)
            oprot.writeI32(self.lispHandle)
            oprot.writeFieldEnd()
        if self.siteHandle != None:
            oprot.writeFieldBegin('siteHandle', TType.I32, 2)
            oprot.writeI32(self.siteHandle)
            oprot.writeFieldEnd()
        if self.eidInstanceId != None:
            oprot.writeFieldBegin('eidInstanceId', TType.I32, 3)
            oprot.writeI32(self.eidInstanceId)
            oprot.writeFieldEnd()
        if self.prefixAF != None:
            oprot.writeFieldBegin('prefixAF', TType.I32, 4)
            oprot.writeI32(self.prefixAF)
            oprot.writeFieldEnd()
        if self.prefix != None:
            oprot.writeFieldBegin('prefix', TType.STRING, 5)
            oprot.writeString(self.prefix)
            oprot.writeFieldEnd()
        if self.prefixLen != None:
            oprot.writeFieldBegin('prefixLen', TType.I16, 6)
            oprot.writeI16(self.prefixLen)
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




class clearMapServerReg_IDL_result(object):
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
        oprot.writeStructBegin('clearMapServerReg_IDL_result')
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




class clearMapCacheEntry_IDL_args(object):
    """
    Attributes:
     - lispHandle
     - eidInstanceId
     - prefixAF
     - prefix
     - prefixLen
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'lispHandle',
      None,
      None),
     (2,
      TType.I32,
      'eidInstanceId',
      None,
      None),
     (3,
      TType.I32,
      'prefixAF',
      None,
      None),
     (4,
      TType.STRING,
      'prefix',
      None,
      None),
     (5,
      TType.I16,
      'prefixLen',
      None,
      None))

    def __init__(self, lispHandle = None, eidInstanceId = None, prefixAF = None, prefix = None, prefixLen = None):
        self.lispHandle = lispHandle
        self.eidInstanceId = eidInstanceId
        self.prefixAF = prefixAF
        self.prefix = prefix
        self.prefixLen = prefixLen



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
                    self.lispHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.eidInstanceId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.prefixAF = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.prefix = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I16:
                    self.prefixLen = iprot.readI16()
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
        oprot.writeStructBegin('clearMapCacheEntry_IDL_args')
        if self.lispHandle != None:
            oprot.writeFieldBegin('lispHandle', TType.I32, 1)
            oprot.writeI32(self.lispHandle)
            oprot.writeFieldEnd()
        if self.eidInstanceId != None:
            oprot.writeFieldBegin('eidInstanceId', TType.I32, 2)
            oprot.writeI32(self.eidInstanceId)
            oprot.writeFieldEnd()
        if self.prefixAF != None:
            oprot.writeFieldBegin('prefixAF', TType.I32, 3)
            oprot.writeI32(self.prefixAF)
            oprot.writeFieldEnd()
        if self.prefix != None:
            oprot.writeFieldBegin('prefix', TType.STRING, 4)
            oprot.writeString(self.prefix)
            oprot.writeFieldEnd()
        if self.prefixLen != None:
            oprot.writeFieldBegin('prefixLen', TType.I16, 5)
            oprot.writeI16(self.prefixLen)
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




class clearMapCacheEntry_IDL_result(object):
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
        oprot.writeStructBegin('clearMapCacheEntry_IDL_result')
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




class findMapCacheEntry_IDL_args(object):
    """
    Attributes:
     - lispHandle
     - eidInstanceId
     - prefixAF
     - prefix
     - prefixLen
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'lispHandle',
      None,
      None),
     (2,
      TType.I32,
      'eidInstanceId',
      None,
      None),
     (3,
      TType.I32,
      'prefixAF',
      None,
      None),
     (4,
      TType.STRING,
      'prefix',
      None,
      None),
     (5,
      TType.I16,
      'prefixLen',
      None,
      None))

    def __init__(self, lispHandle = None, eidInstanceId = None, prefixAF = None, prefix = None, prefixLen = None):
        self.lispHandle = lispHandle
        self.eidInstanceId = eidInstanceId
        self.prefixAF = prefixAF
        self.prefix = prefix
        self.prefixLen = prefixLen



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
                    self.lispHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.eidInstanceId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.prefixAF = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.prefix = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I16:
                    self.prefixLen = iprot.readI16()
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
        oprot.writeStructBegin('findMapCacheEntry_IDL_args')
        if self.lispHandle != None:
            oprot.writeFieldBegin('lispHandle', TType.I32, 1)
            oprot.writeI32(self.lispHandle)
            oprot.writeFieldEnd()
        if self.eidInstanceId != None:
            oprot.writeFieldBegin('eidInstanceId', TType.I32, 2)
            oprot.writeI32(self.eidInstanceId)
            oprot.writeFieldEnd()
        if self.prefixAF != None:
            oprot.writeFieldBegin('prefixAF', TType.I32, 3)
            oprot.writeI32(self.prefixAF)
            oprot.writeFieldEnd()
        if self.prefix != None:
            oprot.writeFieldBegin('prefix', TType.STRING, 4)
            oprot.writeString(self.prefix)
            oprot.writeFieldEnd()
        if self.prefixLen != None:
            oprot.writeFieldBegin('prefixLen', TType.I16, 5)
            oprot.writeI16(self.prefixLen)
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




class findMapCacheEntry_IDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.STRUCT,
      'success',
      (RemoteEidPrefixIDL, RemoteEidPrefixIDL.thrift_spec),
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
                    self.success = RemoteEidPrefixIDL()
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
        oprot.writeStructBegin('findMapCacheEntry_IDL_result')
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




class findMapCacheLongestMatchEntry_IDL_args(object):
    """
    Attributes:
     - lispHandle
     - eidInstanceId
     - addrAF
     - addr
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'lispHandle',
      None,
      None),
     (2,
      TType.I32,
      'eidInstanceId',
      None,
      None),
     (3,
      TType.I32,
      'addrAF',
      None,
      None),
     (4,
      TType.STRING,
      'addr',
      None,
      None))

    def __init__(self, lispHandle = None, eidInstanceId = None, addrAF = None, addr = None):
        self.lispHandle = lispHandle
        self.eidInstanceId = eidInstanceId
        self.addrAF = addrAF
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
                if ftype == TType.I32:
                    self.lispHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.eidInstanceId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.addrAF = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.addr = iprot.readString()
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
        oprot.writeStructBegin('findMapCacheLongestMatchEntry_IDL_args')
        if self.lispHandle != None:
            oprot.writeFieldBegin('lispHandle', TType.I32, 1)
            oprot.writeI32(self.lispHandle)
            oprot.writeFieldEnd()
        if self.eidInstanceId != None:
            oprot.writeFieldBegin('eidInstanceId', TType.I32, 2)
            oprot.writeI32(self.eidInstanceId)
            oprot.writeFieldEnd()
        if self.addrAF != None:
            oprot.writeFieldBegin('addrAF', TType.I32, 3)
            oprot.writeI32(self.addrAF)
            oprot.writeFieldEnd()
        if self.addr != None:
            oprot.writeFieldBegin('addr', TType.STRING, 4)
            oprot.writeString(self.addr)
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




class findMapCacheLongestMatchEntry_IDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.STRUCT,
      'success',
      (RemoteEidPrefixIDL, RemoteEidPrefixIDL.thrift_spec),
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
                    self.success = RemoteEidPrefixIDL()
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
        oprot.writeStructBegin('findMapCacheLongestMatchEntry_IDL_result')
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




class signalMapCache_IDL_args(object):
    """
    Attributes:
     - lispHandle
     - eidInstanceId
     - addrAF
     - addr
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'lispHandle',
      None,
      None),
     (2,
      TType.I32,
      'eidInstanceId',
      None,
      None),
     (3,
      TType.I32,
      'addrAF',
      None,
      None),
     (4,
      TType.STRING,
      'addr',
      None,
      None))

    def __init__(self, lispHandle = None, eidInstanceId = None, addrAF = None, addr = None):
        self.lispHandle = lispHandle
        self.eidInstanceId = eidInstanceId
        self.addrAF = addrAF
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
                if ftype == TType.I32:
                    self.lispHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.eidInstanceId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.addrAF = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.addr = iprot.readString()
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
        oprot.writeStructBegin('signalMapCache_IDL_args')
        if self.lispHandle != None:
            oprot.writeFieldBegin('lispHandle', TType.I32, 1)
            oprot.writeI32(self.lispHandle)
            oprot.writeFieldEnd()
        if self.eidInstanceId != None:
            oprot.writeFieldBegin('eidInstanceId', TType.I32, 2)
            oprot.writeI32(self.eidInstanceId)
            oprot.writeFieldEnd()
        if self.addrAF != None:
            oprot.writeFieldBegin('addrAF', TType.I32, 3)
            oprot.writeI32(self.addrAF)
            oprot.writeFieldEnd()
        if self.addr != None:
            oprot.writeFieldBegin('addr', TType.STRING, 4)
            oprot.writeString(self.addr)
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




class signalMapCache_IDL_result(object):
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
        oprot.writeStructBegin('signalMapCache_IDL_result')
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




class enableProbe_IDL_args(object):
    """
    Attributes:
     - lispHandle
     - eidInstanceId
    """

    thrift_spec = (None, (1,
      TType.I32,
      'lispHandle',
      None,
      None), (2,
      TType.I32,
      'eidInstanceId',
      None,
      None))

    def __init__(self, lispHandle = None, eidInstanceId = None):
        self.lispHandle = lispHandle
        self.eidInstanceId = eidInstanceId



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
                    self.lispHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.eidInstanceId = iprot.readI32()
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
        oprot.writeStructBegin('enableProbe_IDL_args')
        if self.lispHandle != None:
            oprot.writeFieldBegin('lispHandle', TType.I32, 1)
            oprot.writeI32(self.lispHandle)
            oprot.writeFieldEnd()
        if self.eidInstanceId != None:
            oprot.writeFieldBegin('eidInstanceId', TType.I32, 2)
            oprot.writeI32(self.eidInstanceId)
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




class enableProbe_IDL_result(object):
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
        oprot.writeStructBegin('enableProbe_IDL_result')
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




class disableProbe_IDL_args(object):
    """
    Attributes:
     - lispHandle
     - eidInstanceId
    """

    thrift_spec = (None, (1,
      TType.I32,
      'lispHandle',
      None,
      None), (2,
      TType.I32,
      'eidInstanceId',
      None,
      None))

    def __init__(self, lispHandle = None, eidInstanceId = None):
        self.lispHandle = lispHandle
        self.eidInstanceId = eidInstanceId



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
                    self.lispHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.eidInstanceId = iprot.readI32()
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
        oprot.writeStructBegin('disableProbe_IDL_args')
        if self.lispHandle != None:
            oprot.writeFieldBegin('lispHandle', TType.I32, 1)
            oprot.writeI32(self.lispHandle)
            oprot.writeFieldEnd()
        if self.eidInstanceId != None:
            oprot.writeFieldBegin('eidInstanceId', TType.I32, 2)
            oprot.writeI32(self.eidInstanceId)
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




class disableProbe_IDL_result(object):
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
        oprot.writeStructBegin('disableProbe_IDL_result')
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
# 2015.02.05 17:18:39 IST
