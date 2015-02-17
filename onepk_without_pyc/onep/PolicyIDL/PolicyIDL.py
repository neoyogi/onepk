# 2015.02.05 17:22:33 IST
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

    def createPolicy_IDL(self, sessionId, type, policyHandle):
        """
            Create a Policy object
        
            Parameters:
             - sessionId
             - type
             - policyHandle
            """
        pass



    def deletePolicy_IDL(self, sessionId, policyHandle):
        """
            Delete a Policy object
        
            Parameters:
             - sessionId
             - policyHandle
            """
        pass



    def deleteAllPolicies_IDL(self, sessionId):
        """
            Delete all Policies
        
            Parameters:
             - sessionId
            """
        pass



    def createClass_IDL(self, sessionId, classOper):
        """
            Create a Class object
        
            Parameters:
             - sessionId
             - classOper
            """
        pass



    def deleteClass_IDL(self, sessionId, classHandle):
        """
            Delete a Class object
        
            Parameters:
             - sessionId
             - classHandle
            """
        pass



    def addClassToPolicy_IDL(self, policyHandle, classHandle, sequence):
        """
            Add a Class object to a Policy
        
            Parameters:
             - policyHandle
             - classHandle
             - sequence
            """
        pass



    def removeClassFromPolicy_IDL(self, policyHandle, classHandle):
        """
            Remove a Class object from a Policy
        
            Parameters:
             - policyHandle
             - classHandle
            """
        pass



    def addChildToPolicy_IDL(self, parentHandle, childHandle, classHandle):
        """
            Add a Child Policy object to a Policy
        
            Parameters:
             - parentHandle
             - childHandle
             - classHandle
            """
        pass



    def removeChildFromPolicy_IDL(self, parentHandle, childHandle, classHandle):
        """
            Remove a Child Policy object from a Policy
        
            Parameters:
             - parentHandle
             - childHandle
             - classHandle
            """
        pass



    def removeFilterFromClass_IDL(self, classHandle, filterHandle):
        """
            Remove a Filter object from a Class
        
            Parameters:
             - classHandle
             - filterHandle
            """
        pass



    def setFilterSense_IDL(self, classHandle, filterHandle, sense):
        """
            Set Filter sense
        
            Parameters:
             - classHandle
             - filterHandle
             - sense
            """
        pass



    def addFilterAclToClass_IDL(self, classHandle, sense, aclHandle):
        """
            Add ACL Filter object to a Class
        
            Parameters:
             - classHandle
             - sense
             - aclHandle
            """
        pass



    def addFilterDscpToClass_IDL(self, classHandle, sense, dscp):
        """
            Add DSCP Filter object to a Class
        
            Parameters:
             - classHandle
             - sense
             - dscp
            """
        pass



    def addFilterMplsToClass_IDL(self, classHandle, sense, mplsExp):
        """
            Add MPLS Exp Filter object to a Class
        
            Parameters:
             - classHandle
             - sense
             - mplsExp
            """
        pass



    def addFilterDlciToClass_IDL(self, classHandle, sense, dlci):
        """
            Add Frame Relay DLCI Filter object to a Class
        
            Parameters:
             - classHandle
             - sense
             - dlci
            """
        pass



    def addFilterDeToClass_IDL(self, classHandle, sense):
        """
            Add Frame Relay DE Filter object to a Class
        
            Parameters:
             - classHandle
             - sense
            """
        pass



    def addFilterL2CosToClass_IDL(self, classHandle, sense, l2cos):
        """
            Add L2 COS Filter object to a Class
        
            Parameters:
             - classHandle
             - sense
             - l2cos
            """
        pass



    def addFilterMacAddressToClass_IDL(self, classHandle, sense, macAddress):
        """
            Add MAC Address Filter object to a Class
        
            Parameters:
             - classHandle
             - sense
             - macAddress
            """
        pass



    def addFilterPktLenToClass_IDL(self, classHandle, sense, min, max):
        """
            Add Packet Length Filter object to a Class
        
            Parameters:
             - classHandle
             - sense
             - min
             - max
            """
        pass



    def addFilterProtocolToClass_IDL(self, classHandle, sense, protocol, subProtocol, param):
        """
            Add Protocol Filter object to a Class
        
            Parameters:
             - classHandle
             - sense
             - protocol
             - subProtocol
             - param
            """
        pass



    def addFilterQosGroupToClass_IDL(self, classHandle, sense, group):
        """
            Add QOS Group Filter object to a Class
        
            Parameters:
             - classHandle
             - sense
             - group
            """
        pass



    def addFilterRtpPortToClass_IDL(self, classHandle, sense, rtpPort):
        """
            Add RTP Port Filter object to a Class
        
            Parameters:
             - classHandle
             - sense
             - rtpPort
            """
        pass



    def addFilterVlanToClass_IDL(self, classHandle, sense, vlan):
        """
            Add VLAN Filter object to a Class
        
            Parameters:
             - classHandle
             - sense
             - vlan
            """
        pass



    def removeActionFromClass_IDL(self, policyHandle, classHandle, actionHandle):
        """
            Remove an Action object from a Class
        
            Parameters:
             - policyHandle
             - classHandle
             - actionHandle
            """
        pass



    def addActionDropToClass_IDL(self, policyHandle, classHandle, remoteSn, appId, localId):
        """
            Add Drop Action object to a Class
        
            Parameters:
             - policyHandle
             - classHandle
             - remoteSn
             - appId
             - localId
            """
        pass



    def addActionIfcToClass_IDL(self, policyHandle, classHandle, ifHandle):
        """
            Add Set Outgoing Interface Action object to a Class
        
            Parameters:
             - policyHandle
             - classHandle
             - ifHandle
            """
        pass



    def addActionNextHopToClass_IDL(self, policyHandle, classHandle, addrAF, nextHopAddress):
        """
            Add Set Next Hop Action object to a Class
        
            Parameters:
             - policyHandle
             - classHandle
             - addrAF
             - nextHopAddress
            """
        pass



    def addActionMarkToClass_IDL(self, policyHandle, classHandle, markParam):
        """
            Add Mark Action object to a Class
        
            Parameters:
             - policyHandle
             - classHandle
             - markParam
            """
        pass



    def addActionPoliceToClass_IDL(self, policyHandle, classHandle, policeParam):
        """
            Add Police Action object to a Class
        
            Parameters:
             - policyHandle
             - classHandle
             - policeParam
            """
        pass



    def addActionShapeToClass_IDL(self, policyHandle, classHandle, shapeParam):
        """
            Add Shape Action object to a Class
        
            Parameters:
             - policyHandle
             - classHandle
             - shapeParam
            """
        pass



    def addActionPriorityQueueToClass_IDL(self, policyHandle, classHandle, queueParam):
        """
            Add Priority Queue Action object to a Class
        
            Parameters:
             - policyHandle
             - classHandle
             - queueParam
            """
        pass



    def addActionClassBasedQueueToClass_IDL(self, policyHandle, classHandle, queueParam):
        """
            Add Class-Based WFQ Queue Action object to a Class
        
            Parameters:
             - policyHandle
             - classHandle
             - queueParam
            """
        pass



    def addActionFairQueueToClass_IDL(self, policyHandle, classHandle, queueParam):
        """
            Add Fair Queue Action object to a Class
        
            Parameters:
             - policyHandle
             - classHandle
             - queueParam
            """
        pass



    def addActionQueueLimitToClass_IDL(self, policyHandle, classHandle, queueParam):
        """
            Add Queue Limit Action object to a Class
        
            Parameters:
             - policyHandle
             - classHandle
             - queueParam
            """
        pass



    def addActionWredToClass_IDL(self, policyHandle, classHandle, type, ecnEnabled, exponWeight, thresholdUnits):
        """
            Add WRED Action object to a Class
        
            Parameters:
             - policyHandle
             - classHandle
             - type
             - ecnEnabled
             - exponWeight
             - thresholdUnits
            """
        pass



    def addWredProfileToClass_IDL(self, policyHandle, classHandle, type, value, minThreshold, maxThreshold, thresholdUnits, dropProb):
        """
            Add WRED Profile object to a Class
        
            Parameters:
             - policyHandle
             - classHandle
             - type
             - value
             - minThreshold
             - maxThreshold
             - thresholdUnits
             - dropProb
            """
        pass



    def removeWredProfileFromClass_IDL(self, policyHandle, classHandle, type, value, minThreshold, maxThreshold, thresholdUnits, dropProb):
        """
            Remove WRED Profile object to a Class
        
            Parameters:
             - policyHandle
             - classHandle
             - type
             - value
             - minThreshold
             - maxThreshold
             - thresholdUnits
             - dropProb
            """
        pass



    def addActionCopyToClass_IDL(self, policyHandle, classHandle, remoteSn, appId, localId, size, sampleType, sampleRate):
        """
            Add Datapath Copy Action object to a Class
        
            Parameters:
             - policyHandle
             - classHandle
             - remoteSn
             - appId
             - localId
             - size
             - sampleType
             - sampleRate
            """
        pass



    def addActionDivertToClass_IDL(self, policyHandle, classHandle, remoteSn, appId, localId, stateless):
        """
            Add Datapath Divert Action object to a Class
        
            Parameters:
             - policyHandle
             - classHandle
             - remoteSn
             - appId
             - localId
             - stateless
            """
        pass



    def addActionCopyToAce_IDL(self, aclHandle, aceHandle, remoteSn, appId, localId, size, sampleType, sampleRate):
        """
            Add Datapath Copy Action object to an ACE
        
            Parameters:
             - aclHandle
             - aceHandle
             - remoteSn
             - appId
             - localId
             - size
             - sampleType
             - sampleRate
            """
        pass



    def addActionDivertToAce_IDL(self, aclHandle, aceHandle, remoteSn, appId, localId):
        """
            Add Datapath Divert Action object to an ACE
        
            Parameters:
             - aclHandle
             - aceHandle
             - remoteSn
             - appId
             - localId
            """
        pass



    def removeActionFromAce_IDL(self, aclHandle, aceHandle, actionHandle):
        """
            Remove a Datapath Action object from an ACE
        
            Parameters:
             - aclHandle
             - aceHandle
             - actionHandle
            """
        pass



    def applyPolicyToTarget_IDL(self, policyHandle, ifHandle, location):
        """
            Apply Policy to Target
        
            Parameters:
             - policyHandle
             - ifHandle
             - location
            """
        pass



    def removePolicyFromTarget_IDL(self, policyHandle, ifHandle, location):
        """
            Remove Policy from Target
        
            Parameters:
             - policyHandle
             - ifHandle
             - location
            """
        pass



    def createAcl_IDL(self, sessionId, type, persistent, addrFamily):
        """
            Create ACL
        
            Parameters:
             - sessionId
             - type
             - persistent
             - addrFamily
            """
        pass



    def deleteAcl_IDL(self, sessionId, aclHandle):
        """
            Delete ACL
        
            Parameters:
             - sessionId
             - aclHandle
            """
        pass



    def getL3AceList_IDL(self, aclHandle, lifetime, aclName, addrFamily):
        """
            Get L3 ACE list
        
            Parameters:
             - aclHandle
             - lifetime
             - aclName
             - addrFamily
            """
        pass



    def getAceList_IDL(self, aclHandle):
        """
        Parameters:
         - aclHandle
        """
        pass



    def getL2AceList_IDL(self, aclHandle, aclName):
        """
            Get L2 ACE List
        
            Parameters:
             - aclHandle
             - aclName
            """
        pass



    def getAclList_IDL(self, aclType):
        """
            Get list of all ACLs on Network Element
        
            Parameters:
             - aclType
            """
        pass



    def getIfcAclList_IDL(self, ifHandle, direction, aclType):
        """
            Get list of all ACLs on Network Interface
        
            Parameters:
             - ifHandle
             - direction
             - aclType
            """
        pass



    def getAclByName_IDL(self, aclName):
        """
            Get ACL by name on Network Element
        
            Parameters:
             - aclName
            """
        pass



    def getAclName_IDL(self, aclHandle):
        """
            Get ACL name
        
            Parameters:
             - aclHandle
            """
        pass



    def addL3Ace_IDL(self, aclHandle, aceParam):
        """
            Add L3 ACE to ACL
        
            Parameters:
             - aclHandle
             - aceParam
            """
        pass



    def addL2Ace_IDL(self, aclHandle, aceParam):
        """
            Add L2 ACE to ACL
        
            Parameters:
             - aclHandle
             - aceParam
            """
        pass



    def deleteAce_IDL(self, aclHandle, elemHandle):
        """
            Delete ACE from ACL
        
            Parameters:
             - aclHandle
             - elemHandle
            """
        pass



    def applyAclToInterface_IDL(self, aclHandle, ifHandle, direction):
        """
            Apply ACL to Interface
        
            Parameters:
             - aclHandle
             - ifHandle
             - direction
            """
        pass



    def removeAclFromInterface_IDL(self, aclHandle, ifHandle, direction):
        """
            Remove ACL from Interface
        
            Parameters:
             - aclHandle
             - ifHandle
             - direction
            """
        pass



    def getAceMatch_IDL(self, aclHandle, elemHandle):
        """
            Get ACE match count
        
            Parameters:
             - aclHandle
             - elemHandle
            """
        pass



    def clearAclMatch_IDL(self, aclHandle):
        """
            Clear ACL match counters
        
            Parameters:
             - aclHandle
            """
        pass



    def getPolicyCapability_IDL(self, handle):
        """
            Get Policy capability
        
            Parameters:
             - handle
            """
        pass



    def getProtocolCapability_IDL(self, handle):
        """
            Get Protocol capability
        
            Parameters:
             - handle
            """
        pass



    def getSubProtocolCapability_IDL(self, protocol):
        """
            Get Sub-Protocol capability
        
            Parameters:
             - protocol
            """
        pass



    def createNamedAcl_IDL(self, sessionId, type, persistent, addrFamily):
        """
            Create Named ACL
        
            Parameters:
             - sessionId
             - type
             - persistent
             - addrFamily
            """
        pass



    def deleteNamedAcl_IDL(self, sessionId, name, aclHandle, lifetime, addrFamily):
        """
            Delete Named ACL
        
            Parameters:
             - sessionId
             - name
             - aclHandle
             - lifetime
             - addrFamily
            """
        pass



    def addNamedL3Ace_IDL(self, name, aclHandle, lifetime, addrFamily, aceParam):
        """
            Add L3 ACE to Named ACL
        
            Parameters:
             - name
             - aclHandle
             - lifetime
             - addrFamily
             - aceParam
            """
        pass



    def deleteNamedAce_IDL(self, name, aclHandle, elemHandle, lifetime, addrFamily):
        """
            Delete ACE from Named ACL
        
            Parameters:
             - name
             - aclHandle
             - elemHandle
             - lifetime
             - addrFamily
            """
        pass



    def applyNamedAclToInterface_IDL(self, name, aclType, ifHandle, direction, addrFamily):
        """
            Apply Named ACL to Interface
        
            Parameters:
             - name
             - aclType
             - ifHandle
             - direction
             - addrFamily
            """
        pass



    def removeNamedAclFromInterface_IDL(self, name, aclType, ifHandle, direction, addrFamily):
        """
            Remove Named ACL from Interface
        
            Parameters:
             - name
             - aclType
             - ifHandle
             - direction
             - addrFamily
            """
        pass



    def getNamedAceMatch_IDL(self, name, aclHandle, elemHandle, lifetime, addrFamily):
        """
            Get ACE match count
        
            Parameters:
             - name
             - aclHandle
             - elemHandle
             - lifetime
             - addrFamily
            """
        pass




class Client(Iface):

    def __init__(self, iprot, oprot = None):
        self._iprot = self._oprot = iprot
        if oprot != None:
            self._oprot = oprot
        self._seqid = 0



    def createPolicy_IDL(self, sessionId, type, policyHandle):
        """
            Create a Policy object
        
            Parameters:
             - sessionId
             - type
             - policyHandle
            """
        self._oprot.rlock.acquire()
        try:
            self.send_createPolicy_IDL(sessionId, type, policyHandle)
            result = self.recv_createPolicy_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_createPolicy_IDL(self, sessionId, type, policyHandle):
        self._oprot.writeMessageBegin('createPolicy_IDL', TMessageType.CALL, self._seqid)
        args = createPolicy_IDL_args()
        args.sessionId = sessionId
        args.type = type
        args.policyHandle = policyHandle
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_createPolicy_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = createPolicy_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'createPolicy_IDL failed: unknown result')



    def deletePolicy_IDL(self, sessionId, policyHandle):
        """
            Delete a Policy object
        
            Parameters:
             - sessionId
             - policyHandle
            """
        self._oprot.rlock.acquire()
        try:
            self.send_deletePolicy_IDL(sessionId, policyHandle)
            result = self.recv_deletePolicy_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_deletePolicy_IDL(self, sessionId, policyHandle):
        self._oprot.writeMessageBegin('deletePolicy_IDL', TMessageType.CALL, self._seqid)
        args = deletePolicy_IDL_args()
        args.sessionId = sessionId
        args.policyHandle = policyHandle
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_deletePolicy_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = deletePolicy_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'deletePolicy_IDL failed: unknown result')



    def deleteAllPolicies_IDL(self, sessionId):
        """
            Delete all Policies
        
            Parameters:
             - sessionId
            """
        self._oprot.rlock.acquire()
        try:
            self.send_deleteAllPolicies_IDL(sessionId)
            result = self.recv_deleteAllPolicies_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_deleteAllPolicies_IDL(self, sessionId):
        self._oprot.writeMessageBegin('deleteAllPolicies_IDL', TMessageType.CALL, self._seqid)
        args = deleteAllPolicies_IDL_args()
        args.sessionId = sessionId
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_deleteAllPolicies_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = deleteAllPolicies_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'deleteAllPolicies_IDL failed: unknown result')



    def createClass_IDL(self, sessionId, classOper):
        """
            Create a Class object
        
            Parameters:
             - sessionId
             - classOper
            """
        self._oprot.rlock.acquire()
        try:
            self.send_createClass_IDL(sessionId, classOper)
            result = self.recv_createClass_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_createClass_IDL(self, sessionId, classOper):
        self._oprot.writeMessageBegin('createClass_IDL', TMessageType.CALL, self._seqid)
        args = createClass_IDL_args()
        args.sessionId = sessionId
        args.classOper = classOper
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_createClass_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = createClass_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'createClass_IDL failed: unknown result')



    def deleteClass_IDL(self, sessionId, classHandle):
        """
            Delete a Class object
        
            Parameters:
             - sessionId
             - classHandle
            """
        self._oprot.rlock.acquire()
        try:
            self.send_deleteClass_IDL(sessionId, classHandle)
            result = self.recv_deleteClass_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_deleteClass_IDL(self, sessionId, classHandle):
        self._oprot.writeMessageBegin('deleteClass_IDL', TMessageType.CALL, self._seqid)
        args = deleteClass_IDL_args()
        args.sessionId = sessionId
        args.classHandle = classHandle
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_deleteClass_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = deleteClass_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'deleteClass_IDL failed: unknown result')



    def addClassToPolicy_IDL(self, policyHandle, classHandle, sequence):
        """
            Add a Class object to a Policy
        
            Parameters:
             - policyHandle
             - classHandle
             - sequence
            """
        self._oprot.rlock.acquire()
        try:
            self.send_addClassToPolicy_IDL(policyHandle, classHandle, sequence)
            result = self.recv_addClassToPolicy_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_addClassToPolicy_IDL(self, policyHandle, classHandle, sequence):
        self._oprot.writeMessageBegin('addClassToPolicy_IDL', TMessageType.CALL, self._seqid)
        args = addClassToPolicy_IDL_args()
        args.policyHandle = policyHandle
        args.classHandle = classHandle
        args.sequence = sequence
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_addClassToPolicy_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = addClassToPolicy_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'addClassToPolicy_IDL failed: unknown result')



    def removeClassFromPolicy_IDL(self, policyHandle, classHandle):
        """
            Remove a Class object from a Policy
        
            Parameters:
             - policyHandle
             - classHandle
            """
        self._oprot.rlock.acquire()
        try:
            self.send_removeClassFromPolicy_IDL(policyHandle, classHandle)
            result = self.recv_removeClassFromPolicy_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_removeClassFromPolicy_IDL(self, policyHandle, classHandle):
        self._oprot.writeMessageBegin('removeClassFromPolicy_IDL', TMessageType.CALL, self._seqid)
        args = removeClassFromPolicy_IDL_args()
        args.policyHandle = policyHandle
        args.classHandle = classHandle
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_removeClassFromPolicy_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = removeClassFromPolicy_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'removeClassFromPolicy_IDL failed: unknown result')



    def addChildToPolicy_IDL(self, parentHandle, childHandle, classHandle):
        """
            Add a Child Policy object to a Policy
        
            Parameters:
             - parentHandle
             - childHandle
             - classHandle
            """
        self._oprot.rlock.acquire()
        try:
            self.send_addChildToPolicy_IDL(parentHandle, childHandle, classHandle)
            result = self.recv_addChildToPolicy_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_addChildToPolicy_IDL(self, parentHandle, childHandle, classHandle):
        self._oprot.writeMessageBegin('addChildToPolicy_IDL', TMessageType.CALL, self._seqid)
        args = addChildToPolicy_IDL_args()
        args.parentHandle = parentHandle
        args.childHandle = childHandle
        args.classHandle = classHandle
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_addChildToPolicy_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = addChildToPolicy_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'addChildToPolicy_IDL failed: unknown result')



    def removeChildFromPolicy_IDL(self, parentHandle, childHandle, classHandle):
        """
            Remove a Child Policy object from a Policy
        
            Parameters:
             - parentHandle
             - childHandle
             - classHandle
            """
        self._oprot.rlock.acquire()
        try:
            self.send_removeChildFromPolicy_IDL(parentHandle, childHandle, classHandle)
            result = self.recv_removeChildFromPolicy_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_removeChildFromPolicy_IDL(self, parentHandle, childHandle, classHandle):
        self._oprot.writeMessageBegin('removeChildFromPolicy_IDL', TMessageType.CALL, self._seqid)
        args = removeChildFromPolicy_IDL_args()
        args.parentHandle = parentHandle
        args.childHandle = childHandle
        args.classHandle = classHandle
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_removeChildFromPolicy_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = removeChildFromPolicy_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'removeChildFromPolicy_IDL failed: unknown result')



    def removeFilterFromClass_IDL(self, classHandle, filterHandle):
        """
            Remove a Filter object from a Class
        
            Parameters:
             - classHandle
             - filterHandle
            """
        self._oprot.rlock.acquire()
        try:
            self.send_removeFilterFromClass_IDL(classHandle, filterHandle)
            result = self.recv_removeFilterFromClass_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_removeFilterFromClass_IDL(self, classHandle, filterHandle):
        self._oprot.writeMessageBegin('removeFilterFromClass_IDL', TMessageType.CALL, self._seqid)
        args = removeFilterFromClass_IDL_args()
        args.classHandle = classHandle
        args.filterHandle = filterHandle
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_removeFilterFromClass_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = removeFilterFromClass_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'removeFilterFromClass_IDL failed: unknown result')



    def setFilterSense_IDL(self, classHandle, filterHandle, sense):
        """
            Set Filter sense
        
            Parameters:
             - classHandle
             - filterHandle
             - sense
            """
        self._oprot.rlock.acquire()
        try:
            self.send_setFilterSense_IDL(classHandle, filterHandle, sense)
            result = self.recv_setFilterSense_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_setFilterSense_IDL(self, classHandle, filterHandle, sense):
        self._oprot.writeMessageBegin('setFilterSense_IDL', TMessageType.CALL, self._seqid)
        args = setFilterSense_IDL_args()
        args.classHandle = classHandle
        args.filterHandle = filterHandle
        args.sense = sense
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_setFilterSense_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = setFilterSense_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'setFilterSense_IDL failed: unknown result')



    def addFilterAclToClass_IDL(self, classHandle, sense, aclHandle):
        """
            Add ACL Filter object to a Class
        
            Parameters:
             - classHandle
             - sense
             - aclHandle
            """
        self._oprot.rlock.acquire()
        try:
            self.send_addFilterAclToClass_IDL(classHandle, sense, aclHandle)
            result = self.recv_addFilterAclToClass_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_addFilterAclToClass_IDL(self, classHandle, sense, aclHandle):
        self._oprot.writeMessageBegin('addFilterAclToClass_IDL', TMessageType.CALL, self._seqid)
        args = addFilterAclToClass_IDL_args()
        args.classHandle = classHandle
        args.sense = sense
        args.aclHandle = aclHandle
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_addFilterAclToClass_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = addFilterAclToClass_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'addFilterAclToClass_IDL failed: unknown result')



    def addFilterDscpToClass_IDL(self, classHandle, sense, dscp):
        """
            Add DSCP Filter object to a Class
        
            Parameters:
             - classHandle
             - sense
             - dscp
            """
        self._oprot.rlock.acquire()
        try:
            self.send_addFilterDscpToClass_IDL(classHandle, sense, dscp)
            result = self.recv_addFilterDscpToClass_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_addFilterDscpToClass_IDL(self, classHandle, sense, dscp):
        self._oprot.writeMessageBegin('addFilterDscpToClass_IDL', TMessageType.CALL, self._seqid)
        args = addFilterDscpToClass_IDL_args()
        args.classHandle = classHandle
        args.sense = sense
        args.dscp = dscp
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_addFilterDscpToClass_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = addFilterDscpToClass_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'addFilterDscpToClass_IDL failed: unknown result')



    def addFilterMplsToClass_IDL(self, classHandle, sense, mplsExp):
        """
            Add MPLS Exp Filter object to a Class
        
            Parameters:
             - classHandle
             - sense
             - mplsExp
            """
        self._oprot.rlock.acquire()
        try:
            self.send_addFilterMplsToClass_IDL(classHandle, sense, mplsExp)
            result = self.recv_addFilterMplsToClass_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_addFilterMplsToClass_IDL(self, classHandle, sense, mplsExp):
        self._oprot.writeMessageBegin('addFilterMplsToClass_IDL', TMessageType.CALL, self._seqid)
        args = addFilterMplsToClass_IDL_args()
        args.classHandle = classHandle
        args.sense = sense
        args.mplsExp = mplsExp
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_addFilterMplsToClass_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = addFilterMplsToClass_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'addFilterMplsToClass_IDL failed: unknown result')



    def addFilterDlciToClass_IDL(self, classHandle, sense, dlci):
        """
            Add Frame Relay DLCI Filter object to a Class
        
            Parameters:
             - classHandle
             - sense
             - dlci
            """
        self._oprot.rlock.acquire()
        try:
            self.send_addFilterDlciToClass_IDL(classHandle, sense, dlci)
            result = self.recv_addFilterDlciToClass_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_addFilterDlciToClass_IDL(self, classHandle, sense, dlci):
        self._oprot.writeMessageBegin('addFilterDlciToClass_IDL', TMessageType.CALL, self._seqid)
        args = addFilterDlciToClass_IDL_args()
        args.classHandle = classHandle
        args.sense = sense
        args.dlci = dlci
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_addFilterDlciToClass_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = addFilterDlciToClass_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'addFilterDlciToClass_IDL failed: unknown result')



    def addFilterDeToClass_IDL(self, classHandle, sense):
        """
            Add Frame Relay DE Filter object to a Class
        
            Parameters:
             - classHandle
             - sense
            """
        self._oprot.rlock.acquire()
        try:
            self.send_addFilterDeToClass_IDL(classHandle, sense)
            result = self.recv_addFilterDeToClass_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_addFilterDeToClass_IDL(self, classHandle, sense):
        self._oprot.writeMessageBegin('addFilterDeToClass_IDL', TMessageType.CALL, self._seqid)
        args = addFilterDeToClass_IDL_args()
        args.classHandle = classHandle
        args.sense = sense
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_addFilterDeToClass_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = addFilterDeToClass_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'addFilterDeToClass_IDL failed: unknown result')



    def addFilterL2CosToClass_IDL(self, classHandle, sense, l2cos):
        """
            Add L2 COS Filter object to a Class
        
            Parameters:
             - classHandle
             - sense
             - l2cos
            """
        self._oprot.rlock.acquire()
        try:
            self.send_addFilterL2CosToClass_IDL(classHandle, sense, l2cos)
            result = self.recv_addFilterL2CosToClass_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_addFilterL2CosToClass_IDL(self, classHandle, sense, l2cos):
        self._oprot.writeMessageBegin('addFilterL2CosToClass_IDL', TMessageType.CALL, self._seqid)
        args = addFilterL2CosToClass_IDL_args()
        args.classHandle = classHandle
        args.sense = sense
        args.l2cos = l2cos
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_addFilterL2CosToClass_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = addFilterL2CosToClass_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'addFilterL2CosToClass_IDL failed: unknown result')



    def addFilterMacAddressToClass_IDL(self, classHandle, sense, macAddress):
        """
            Add MAC Address Filter object to a Class
        
            Parameters:
             - classHandle
             - sense
             - macAddress
            """
        self._oprot.rlock.acquire()
        try:
            self.send_addFilterMacAddressToClass_IDL(classHandle, sense, macAddress)
            result = self.recv_addFilterMacAddressToClass_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_addFilterMacAddressToClass_IDL(self, classHandle, sense, macAddress):
        self._oprot.writeMessageBegin('addFilterMacAddressToClass_IDL', TMessageType.CALL, self._seqid)
        args = addFilterMacAddressToClass_IDL_args()
        args.classHandle = classHandle
        args.sense = sense
        args.macAddress = macAddress
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_addFilterMacAddressToClass_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = addFilterMacAddressToClass_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'addFilterMacAddressToClass_IDL failed: unknown result')



    def addFilterPktLenToClass_IDL(self, classHandle, sense, min, max):
        """
            Add Packet Length Filter object to a Class
        
            Parameters:
             - classHandle
             - sense
             - min
             - max
            """
        self._oprot.rlock.acquire()
        try:
            self.send_addFilterPktLenToClass_IDL(classHandle, sense, min, max)
            result = self.recv_addFilterPktLenToClass_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_addFilterPktLenToClass_IDL(self, classHandle, sense, min, max):
        self._oprot.writeMessageBegin('addFilterPktLenToClass_IDL', TMessageType.CALL, self._seqid)
        args = addFilterPktLenToClass_IDL_args()
        args.classHandle = classHandle
        args.sense = sense
        args.min = min
        args.max = max
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_addFilterPktLenToClass_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = addFilterPktLenToClass_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'addFilterPktLenToClass_IDL failed: unknown result')



    def addFilterProtocolToClass_IDL(self, classHandle, sense, protocol, subProtocol, param):
        """
            Add Protocol Filter object to a Class
        
            Parameters:
             - classHandle
             - sense
             - protocol
             - subProtocol
             - param
            """
        self._oprot.rlock.acquire()
        try:
            self.send_addFilterProtocolToClass_IDL(classHandle, sense, protocol, subProtocol, param)
            result = self.recv_addFilterProtocolToClass_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_addFilterProtocolToClass_IDL(self, classHandle, sense, protocol, subProtocol, param):
        self._oprot.writeMessageBegin('addFilterProtocolToClass_IDL', TMessageType.CALL, self._seqid)
        args = addFilterProtocolToClass_IDL_args()
        args.classHandle = classHandle
        args.sense = sense
        args.protocol = protocol
        args.subProtocol = subProtocol
        args.param = param
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_addFilterProtocolToClass_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = addFilterProtocolToClass_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'addFilterProtocolToClass_IDL failed: unknown result')



    def addFilterQosGroupToClass_IDL(self, classHandle, sense, group):
        """
            Add QOS Group Filter object to a Class
        
            Parameters:
             - classHandle
             - sense
             - group
            """
        self._oprot.rlock.acquire()
        try:
            self.send_addFilterQosGroupToClass_IDL(classHandle, sense, group)
            result = self.recv_addFilterQosGroupToClass_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_addFilterQosGroupToClass_IDL(self, classHandle, sense, group):
        self._oprot.writeMessageBegin('addFilterQosGroupToClass_IDL', TMessageType.CALL, self._seqid)
        args = addFilterQosGroupToClass_IDL_args()
        args.classHandle = classHandle
        args.sense = sense
        args.group = group
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_addFilterQosGroupToClass_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = addFilterQosGroupToClass_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'addFilterQosGroupToClass_IDL failed: unknown result')



    def addFilterRtpPortToClass_IDL(self, classHandle, sense, rtpPort):
        """
            Add RTP Port Filter object to a Class
        
            Parameters:
             - classHandle
             - sense
             - rtpPort
            """
        self._oprot.rlock.acquire()
        try:
            self.send_addFilterRtpPortToClass_IDL(classHandle, sense, rtpPort)
            result = self.recv_addFilterRtpPortToClass_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_addFilterRtpPortToClass_IDL(self, classHandle, sense, rtpPort):
        self._oprot.writeMessageBegin('addFilterRtpPortToClass_IDL', TMessageType.CALL, self._seqid)
        args = addFilterRtpPortToClass_IDL_args()
        args.classHandle = classHandle
        args.sense = sense
        args.rtpPort = rtpPort
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_addFilterRtpPortToClass_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = addFilterRtpPortToClass_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'addFilterRtpPortToClass_IDL failed: unknown result')



    def addFilterVlanToClass_IDL(self, classHandle, sense, vlan):
        """
            Add VLAN Filter object to a Class
        
            Parameters:
             - classHandle
             - sense
             - vlan
            """
        self._oprot.rlock.acquire()
        try:
            self.send_addFilterVlanToClass_IDL(classHandle, sense, vlan)
            result = self.recv_addFilterVlanToClass_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_addFilterVlanToClass_IDL(self, classHandle, sense, vlan):
        self._oprot.writeMessageBegin('addFilterVlanToClass_IDL', TMessageType.CALL, self._seqid)
        args = addFilterVlanToClass_IDL_args()
        args.classHandle = classHandle
        args.sense = sense
        args.vlan = vlan
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_addFilterVlanToClass_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = addFilterVlanToClass_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'addFilterVlanToClass_IDL failed: unknown result')



    def removeActionFromClass_IDL(self, policyHandle, classHandle, actionHandle):
        """
            Remove an Action object from a Class
        
            Parameters:
             - policyHandle
             - classHandle
             - actionHandle
            """
        self._oprot.rlock.acquire()
        try:
            self.send_removeActionFromClass_IDL(policyHandle, classHandle, actionHandle)
            result = self.recv_removeActionFromClass_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_removeActionFromClass_IDL(self, policyHandle, classHandle, actionHandle):
        self._oprot.writeMessageBegin('removeActionFromClass_IDL', TMessageType.CALL, self._seqid)
        args = removeActionFromClass_IDL_args()
        args.policyHandle = policyHandle
        args.classHandle = classHandle
        args.actionHandle = actionHandle
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_removeActionFromClass_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = removeActionFromClass_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'removeActionFromClass_IDL failed: unknown result')



    def addActionDropToClass_IDL(self, policyHandle, classHandle, remoteSn, appId, localId):
        """
            Add Drop Action object to a Class
        
            Parameters:
             - policyHandle
             - classHandle
             - remoteSn
             - appId
             - localId
            """
        self._oprot.rlock.acquire()
        try:
            self.send_addActionDropToClass_IDL(policyHandle, classHandle, remoteSn, appId, localId)
            result = self.recv_addActionDropToClass_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_addActionDropToClass_IDL(self, policyHandle, classHandle, remoteSn, appId, localId):
        self._oprot.writeMessageBegin('addActionDropToClass_IDL', TMessageType.CALL, self._seqid)
        args = addActionDropToClass_IDL_args()
        args.policyHandle = policyHandle
        args.classHandle = classHandle
        args.remoteSn = remoteSn
        args.appId = appId
        args.localId = localId
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_addActionDropToClass_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = addActionDropToClass_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'addActionDropToClass_IDL failed: unknown result')



    def addActionIfcToClass_IDL(self, policyHandle, classHandle, ifHandle):
        """
            Add Set Outgoing Interface Action object to a Class
        
            Parameters:
             - policyHandle
             - classHandle
             - ifHandle
            """
        self._oprot.rlock.acquire()
        try:
            self.send_addActionIfcToClass_IDL(policyHandle, classHandle, ifHandle)
            result = self.recv_addActionIfcToClass_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_addActionIfcToClass_IDL(self, policyHandle, classHandle, ifHandle):
        self._oprot.writeMessageBegin('addActionIfcToClass_IDL', TMessageType.CALL, self._seqid)
        args = addActionIfcToClass_IDL_args()
        args.policyHandle = policyHandle
        args.classHandle = classHandle
        args.ifHandle = ifHandle
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_addActionIfcToClass_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = addActionIfcToClass_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'addActionIfcToClass_IDL failed: unknown result')



    def addActionNextHopToClass_IDL(self, policyHandle, classHandle, addrAF, nextHopAddress):
        """
            Add Set Next Hop Action object to a Class
        
            Parameters:
             - policyHandle
             - classHandle
             - addrAF
             - nextHopAddress
            """
        self._oprot.rlock.acquire()
        try:
            self.send_addActionNextHopToClass_IDL(policyHandle, classHandle, addrAF, nextHopAddress)
            result = self.recv_addActionNextHopToClass_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_addActionNextHopToClass_IDL(self, policyHandle, classHandle, addrAF, nextHopAddress):
        self._oprot.writeMessageBegin('addActionNextHopToClass_IDL', TMessageType.CALL, self._seqid)
        args = addActionNextHopToClass_IDL_args()
        args.policyHandle = policyHandle
        args.classHandle = classHandle
        args.addrAF = addrAF
        args.nextHopAddress = nextHopAddress
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_addActionNextHopToClass_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = addActionNextHopToClass_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'addActionNextHopToClass_IDL failed: unknown result')



    def addActionMarkToClass_IDL(self, policyHandle, classHandle, markParam):
        """
            Add Mark Action object to a Class
        
            Parameters:
             - policyHandle
             - classHandle
             - markParam
            """
        self._oprot.rlock.acquire()
        try:
            self.send_addActionMarkToClass_IDL(policyHandle, classHandle, markParam)
            result = self.recv_addActionMarkToClass_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_addActionMarkToClass_IDL(self, policyHandle, classHandle, markParam):
        self._oprot.writeMessageBegin('addActionMarkToClass_IDL', TMessageType.CALL, self._seqid)
        args = addActionMarkToClass_IDL_args()
        args.policyHandle = policyHandle
        args.classHandle = classHandle
        args.markParam = markParam
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_addActionMarkToClass_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = addActionMarkToClass_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'addActionMarkToClass_IDL failed: unknown result')



    def addActionPoliceToClass_IDL(self, policyHandle, classHandle, policeParam):
        """
            Add Police Action object to a Class
        
            Parameters:
             - policyHandle
             - classHandle
             - policeParam
            """
        self._oprot.rlock.acquire()
        try:
            self.send_addActionPoliceToClass_IDL(policyHandle, classHandle, policeParam)
            result = self.recv_addActionPoliceToClass_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_addActionPoliceToClass_IDL(self, policyHandle, classHandle, policeParam):
        self._oprot.writeMessageBegin('addActionPoliceToClass_IDL', TMessageType.CALL, self._seqid)
        args = addActionPoliceToClass_IDL_args()
        args.policyHandle = policyHandle
        args.classHandle = classHandle
        args.policeParam = policeParam
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_addActionPoliceToClass_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = addActionPoliceToClass_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'addActionPoliceToClass_IDL failed: unknown result')



    def addActionShapeToClass_IDL(self, policyHandle, classHandle, shapeParam):
        """
            Add Shape Action object to a Class
        
            Parameters:
             - policyHandle
             - classHandle
             - shapeParam
            """
        self._oprot.rlock.acquire()
        try:
            self.send_addActionShapeToClass_IDL(policyHandle, classHandle, shapeParam)
            result = self.recv_addActionShapeToClass_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_addActionShapeToClass_IDL(self, policyHandle, classHandle, shapeParam):
        self._oprot.writeMessageBegin('addActionShapeToClass_IDL', TMessageType.CALL, self._seqid)
        args = addActionShapeToClass_IDL_args()
        args.policyHandle = policyHandle
        args.classHandle = classHandle
        args.shapeParam = shapeParam
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_addActionShapeToClass_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = addActionShapeToClass_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'addActionShapeToClass_IDL failed: unknown result')



    def addActionPriorityQueueToClass_IDL(self, policyHandle, classHandle, queueParam):
        """
            Add Priority Queue Action object to a Class
        
            Parameters:
             - policyHandle
             - classHandle
             - queueParam
            """
        self._oprot.rlock.acquire()
        try:
            self.send_addActionPriorityQueueToClass_IDL(policyHandle, classHandle, queueParam)
            result = self.recv_addActionPriorityQueueToClass_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_addActionPriorityQueueToClass_IDL(self, policyHandle, classHandle, queueParam):
        self._oprot.writeMessageBegin('addActionPriorityQueueToClass_IDL', TMessageType.CALL, self._seqid)
        args = addActionPriorityQueueToClass_IDL_args()
        args.policyHandle = policyHandle
        args.classHandle = classHandle
        args.queueParam = queueParam
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_addActionPriorityQueueToClass_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = addActionPriorityQueueToClass_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'addActionPriorityQueueToClass_IDL failed: unknown result')



    def addActionClassBasedQueueToClass_IDL(self, policyHandle, classHandle, queueParam):
        """
            Add Class-Based WFQ Queue Action object to a Class
        
            Parameters:
             - policyHandle
             - classHandle
             - queueParam
            """
        self._oprot.rlock.acquire()
        try:
            self.send_addActionClassBasedQueueToClass_IDL(policyHandle, classHandle, queueParam)
            result = self.recv_addActionClassBasedQueueToClass_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_addActionClassBasedQueueToClass_IDL(self, policyHandle, classHandle, queueParam):
        self._oprot.writeMessageBegin('addActionClassBasedQueueToClass_IDL', TMessageType.CALL, self._seqid)
        args = addActionClassBasedQueueToClass_IDL_args()
        args.policyHandle = policyHandle
        args.classHandle = classHandle
        args.queueParam = queueParam
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_addActionClassBasedQueueToClass_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = addActionClassBasedQueueToClass_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'addActionClassBasedQueueToClass_IDL failed: unknown result')



    def addActionFairQueueToClass_IDL(self, policyHandle, classHandle, queueParam):
        """
            Add Fair Queue Action object to a Class
        
            Parameters:
             - policyHandle
             - classHandle
             - queueParam
            """
        self._oprot.rlock.acquire()
        try:
            self.send_addActionFairQueueToClass_IDL(policyHandle, classHandle, queueParam)
            result = self.recv_addActionFairQueueToClass_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_addActionFairQueueToClass_IDL(self, policyHandle, classHandle, queueParam):
        self._oprot.writeMessageBegin('addActionFairQueueToClass_IDL', TMessageType.CALL, self._seqid)
        args = addActionFairQueueToClass_IDL_args()
        args.policyHandle = policyHandle
        args.classHandle = classHandle
        args.queueParam = queueParam
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_addActionFairQueueToClass_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = addActionFairQueueToClass_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'addActionFairQueueToClass_IDL failed: unknown result')



    def addActionQueueLimitToClass_IDL(self, policyHandle, classHandle, queueParam):
        """
            Add Queue Limit Action object to a Class
        
            Parameters:
             - policyHandle
             - classHandle
             - queueParam
            """
        self._oprot.rlock.acquire()
        try:
            self.send_addActionQueueLimitToClass_IDL(policyHandle, classHandle, queueParam)
            result = self.recv_addActionQueueLimitToClass_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_addActionQueueLimitToClass_IDL(self, policyHandle, classHandle, queueParam):
        self._oprot.writeMessageBegin('addActionQueueLimitToClass_IDL', TMessageType.CALL, self._seqid)
        args = addActionQueueLimitToClass_IDL_args()
        args.policyHandle = policyHandle
        args.classHandle = classHandle
        args.queueParam = queueParam
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_addActionQueueLimitToClass_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = addActionQueueLimitToClass_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'addActionQueueLimitToClass_IDL failed: unknown result')



    def addActionWredToClass_IDL(self, policyHandle, classHandle, type, ecnEnabled, exponWeight, thresholdUnits):
        """
            Add WRED Action object to a Class
        
            Parameters:
             - policyHandle
             - classHandle
             - type
             - ecnEnabled
             - exponWeight
             - thresholdUnits
            """
        self._oprot.rlock.acquire()
        try:
            self.send_addActionWredToClass_IDL(policyHandle, classHandle, type, ecnEnabled, exponWeight, thresholdUnits)
            result = self.recv_addActionWredToClass_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_addActionWredToClass_IDL(self, policyHandle, classHandle, type, ecnEnabled, exponWeight, thresholdUnits):
        self._oprot.writeMessageBegin('addActionWredToClass_IDL', TMessageType.CALL, self._seqid)
        args = addActionWredToClass_IDL_args()
        args.policyHandle = policyHandle
        args.classHandle = classHandle
        args.type = type
        args.ecnEnabled = ecnEnabled
        args.exponWeight = exponWeight
        args.thresholdUnits = thresholdUnits
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_addActionWredToClass_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = addActionWredToClass_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'addActionWredToClass_IDL failed: unknown result')



    def addWredProfileToClass_IDL(self, policyHandle, classHandle, type, value, minThreshold, maxThreshold, thresholdUnits, dropProb):
        """
            Add WRED Profile object to a Class
        
            Parameters:
             - policyHandle
             - classHandle
             - type
             - value
             - minThreshold
             - maxThreshold
             - thresholdUnits
             - dropProb
            """
        self._oprot.rlock.acquire()
        try:
            self.send_addWredProfileToClass_IDL(policyHandle, classHandle, type, value, minThreshold, maxThreshold, thresholdUnits, dropProb)
            result = self.recv_addWredProfileToClass_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_addWredProfileToClass_IDL(self, policyHandle, classHandle, type, value, minThreshold, maxThreshold, thresholdUnits, dropProb):
        self._oprot.writeMessageBegin('addWredProfileToClass_IDL', TMessageType.CALL, self._seqid)
        args = addWredProfileToClass_IDL_args()
        args.policyHandle = policyHandle
        args.classHandle = classHandle
        args.type = type
        args.value = value
        args.minThreshold = minThreshold
        args.maxThreshold = maxThreshold
        args.thresholdUnits = thresholdUnits
        args.dropProb = dropProb
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_addWredProfileToClass_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = addWredProfileToClass_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'addWredProfileToClass_IDL failed: unknown result')



    def removeWredProfileFromClass_IDL(self, policyHandle, classHandle, type, value, minThreshold, maxThreshold, thresholdUnits, dropProb):
        """
            Remove WRED Profile object to a Class
        
            Parameters:
             - policyHandle
             - classHandle
             - type
             - value
             - minThreshold
             - maxThreshold
             - thresholdUnits
             - dropProb
            """
        self._oprot.rlock.acquire()
        try:
            self.send_removeWredProfileFromClass_IDL(policyHandle, classHandle, type, value, minThreshold, maxThreshold, thresholdUnits, dropProb)
            result = self.recv_removeWredProfileFromClass_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_removeWredProfileFromClass_IDL(self, policyHandle, classHandle, type, value, minThreshold, maxThreshold, thresholdUnits, dropProb):
        self._oprot.writeMessageBegin('removeWredProfileFromClass_IDL', TMessageType.CALL, self._seqid)
        args = removeWredProfileFromClass_IDL_args()
        args.policyHandle = policyHandle
        args.classHandle = classHandle
        args.type = type
        args.value = value
        args.minThreshold = minThreshold
        args.maxThreshold = maxThreshold
        args.thresholdUnits = thresholdUnits
        args.dropProb = dropProb
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_removeWredProfileFromClass_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = removeWredProfileFromClass_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'removeWredProfileFromClass_IDL failed: unknown result')



    def addActionCopyToClass_IDL(self, policyHandle, classHandle, remoteSn, appId, localId, size, sampleType, sampleRate):
        """
            Add Datapath Copy Action object to a Class
        
            Parameters:
             - policyHandle
             - classHandle
             - remoteSn
             - appId
             - localId
             - size
             - sampleType
             - sampleRate
            """
        self._oprot.rlock.acquire()
        try:
            self.send_addActionCopyToClass_IDL(policyHandle, classHandle, remoteSn, appId, localId, size, sampleType, sampleRate)
            result = self.recv_addActionCopyToClass_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_addActionCopyToClass_IDL(self, policyHandle, classHandle, remoteSn, appId, localId, size, sampleType, sampleRate):
        self._oprot.writeMessageBegin('addActionCopyToClass_IDL', TMessageType.CALL, self._seqid)
        args = addActionCopyToClass_IDL_args()
        args.policyHandle = policyHandle
        args.classHandle = classHandle
        args.remoteSn = remoteSn
        args.appId = appId
        args.localId = localId
        args.size = size
        args.sampleType = sampleType
        args.sampleRate = sampleRate
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_addActionCopyToClass_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = addActionCopyToClass_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'addActionCopyToClass_IDL failed: unknown result')



    def addActionDivertToClass_IDL(self, policyHandle, classHandle, remoteSn, appId, localId, stateless):
        """
            Add Datapath Divert Action object to a Class
        
            Parameters:
             - policyHandle
             - classHandle
             - remoteSn
             - appId
             - localId
             - stateless
            """
        self._oprot.rlock.acquire()
        try:
            self.send_addActionDivertToClass_IDL(policyHandle, classHandle, remoteSn, appId, localId, stateless)
            result = self.recv_addActionDivertToClass_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_addActionDivertToClass_IDL(self, policyHandle, classHandle, remoteSn, appId, localId, stateless):
        self._oprot.writeMessageBegin('addActionDivertToClass_IDL', TMessageType.CALL, self._seqid)
        args = addActionDivertToClass_IDL_args()
        args.policyHandle = policyHandle
        args.classHandle = classHandle
        args.remoteSn = remoteSn
        args.appId = appId
        args.localId = localId
        args.stateless = stateless
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_addActionDivertToClass_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = addActionDivertToClass_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'addActionDivertToClass_IDL failed: unknown result')



    def addActionCopyToAce_IDL(self, aclHandle, aceHandle, remoteSn, appId, localId, size, sampleType, sampleRate):
        """
            Add Datapath Copy Action object to an ACE
        
            Parameters:
             - aclHandle
             - aceHandle
             - remoteSn
             - appId
             - localId
             - size
             - sampleType
             - sampleRate
            """
        self._oprot.rlock.acquire()
        try:
            self.send_addActionCopyToAce_IDL(aclHandle, aceHandle, remoteSn, appId, localId, size, sampleType, sampleRate)
            result = self.recv_addActionCopyToAce_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_addActionCopyToAce_IDL(self, aclHandle, aceHandle, remoteSn, appId, localId, size, sampleType, sampleRate):
        self._oprot.writeMessageBegin('addActionCopyToAce_IDL', TMessageType.CALL, self._seqid)
        args = addActionCopyToAce_IDL_args()
        args.aclHandle = aclHandle
        args.aceHandle = aceHandle
        args.remoteSn = remoteSn
        args.appId = appId
        args.localId = localId
        args.size = size
        args.sampleType = sampleType
        args.sampleRate = sampleRate
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_addActionCopyToAce_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = addActionCopyToAce_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'addActionCopyToAce_IDL failed: unknown result')



    def addActionDivertToAce_IDL(self, aclHandle, aceHandle, remoteSn, appId, localId):
        """
            Add Datapath Divert Action object to an ACE
        
            Parameters:
             - aclHandle
             - aceHandle
             - remoteSn
             - appId
             - localId
            """
        self._oprot.rlock.acquire()
        try:
            self.send_addActionDivertToAce_IDL(aclHandle, aceHandle, remoteSn, appId, localId)
            result = self.recv_addActionDivertToAce_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_addActionDivertToAce_IDL(self, aclHandle, aceHandle, remoteSn, appId, localId):
        self._oprot.writeMessageBegin('addActionDivertToAce_IDL', TMessageType.CALL, self._seqid)
        args = addActionDivertToAce_IDL_args()
        args.aclHandle = aclHandle
        args.aceHandle = aceHandle
        args.remoteSn = remoteSn
        args.appId = appId
        args.localId = localId
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_addActionDivertToAce_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = addActionDivertToAce_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'addActionDivertToAce_IDL failed: unknown result')



    def removeActionFromAce_IDL(self, aclHandle, aceHandle, actionHandle):
        """
            Remove a Datapath Action object from an ACE
        
            Parameters:
             - aclHandle
             - aceHandle
             - actionHandle
            """
        self._oprot.rlock.acquire()
        try:
            self.send_removeActionFromAce_IDL(aclHandle, aceHandle, actionHandle)
            result = self.recv_removeActionFromAce_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_removeActionFromAce_IDL(self, aclHandle, aceHandle, actionHandle):
        self._oprot.writeMessageBegin('removeActionFromAce_IDL', TMessageType.CALL, self._seqid)
        args = removeActionFromAce_IDL_args()
        args.aclHandle = aclHandle
        args.aceHandle = aceHandle
        args.actionHandle = actionHandle
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_removeActionFromAce_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = removeActionFromAce_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'removeActionFromAce_IDL failed: unknown result')



    def applyPolicyToTarget_IDL(self, policyHandle, ifHandle, location):
        """
            Apply Policy to Target
        
            Parameters:
             - policyHandle
             - ifHandle
             - location
            """
        self._oprot.rlock.acquire()
        try:
            self.send_applyPolicyToTarget_IDL(policyHandle, ifHandle, location)
            result = self.recv_applyPolicyToTarget_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_applyPolicyToTarget_IDL(self, policyHandle, ifHandle, location):
        self._oprot.writeMessageBegin('applyPolicyToTarget_IDL', TMessageType.CALL, self._seqid)
        args = applyPolicyToTarget_IDL_args()
        args.policyHandle = policyHandle
        args.ifHandle = ifHandle
        args.location = location
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_applyPolicyToTarget_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = applyPolicyToTarget_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'applyPolicyToTarget_IDL failed: unknown result')



    def removePolicyFromTarget_IDL(self, policyHandle, ifHandle, location):
        """
            Remove Policy from Target
        
            Parameters:
             - policyHandle
             - ifHandle
             - location
            """
        self._oprot.rlock.acquire()
        try:
            self.send_removePolicyFromTarget_IDL(policyHandle, ifHandle, location)
            result = self.recv_removePolicyFromTarget_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_removePolicyFromTarget_IDL(self, policyHandle, ifHandle, location):
        self._oprot.writeMessageBegin('removePolicyFromTarget_IDL', TMessageType.CALL, self._seqid)
        args = removePolicyFromTarget_IDL_args()
        args.policyHandle = policyHandle
        args.ifHandle = ifHandle
        args.location = location
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_removePolicyFromTarget_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = removePolicyFromTarget_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'removePolicyFromTarget_IDL failed: unknown result')



    def createAcl_IDL(self, sessionId, type, persistent, addrFamily):
        """
            Create ACL
        
            Parameters:
             - sessionId
             - type
             - persistent
             - addrFamily
            """
        self._oprot.rlock.acquire()
        try:
            self.send_createAcl_IDL(sessionId, type, persistent, addrFamily)
            result = self.recv_createAcl_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_createAcl_IDL(self, sessionId, type, persistent, addrFamily):
        self._oprot.writeMessageBegin('createAcl_IDL', TMessageType.CALL, self._seqid)
        args = createAcl_IDL_args()
        args.sessionId = sessionId
        args.type = type
        args.persistent = persistent
        args.addrFamily = addrFamily
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_createAcl_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = createAcl_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'createAcl_IDL failed: unknown result')



    def deleteAcl_IDL(self, sessionId, aclHandle):
        """
            Delete ACL
        
            Parameters:
             - sessionId
             - aclHandle
            """
        self._oprot.rlock.acquire()
        try:
            self.send_deleteAcl_IDL(sessionId, aclHandle)
            result = self.recv_deleteAcl_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_deleteAcl_IDL(self, sessionId, aclHandle):
        self._oprot.writeMessageBegin('deleteAcl_IDL', TMessageType.CALL, self._seqid)
        args = deleteAcl_IDL_args()
        args.sessionId = sessionId
        args.aclHandle = aclHandle
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_deleteAcl_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = deleteAcl_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'deleteAcl_IDL failed: unknown result')



    def getL3AceList_IDL(self, aclHandle, lifetime, aclName, addrFamily):
        """
            Get L3 ACE list
        
            Parameters:
             - aclHandle
             - lifetime
             - aclName
             - addrFamily
            """
        self._oprot.rlock.acquire()
        try:
            self.send_getL3AceList_IDL(aclHandle, lifetime, aclName, addrFamily)
            result = self.recv_getL3AceList_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_getL3AceList_IDL(self, aclHandle, lifetime, aclName, addrFamily):
        self._oprot.writeMessageBegin('getL3AceList_IDL', TMessageType.CALL, self._seqid)
        args = getL3AceList_IDL_args()
        args.aclHandle = aclHandle
        args.lifetime = lifetime
        args.aclName = aclName
        args.addrFamily = addrFamily
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_getL3AceList_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = getL3AceList_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'getL3AceList_IDL failed: unknown result')



    def getAceList_IDL(self, aclHandle):
        """
        Parameters:
         - aclHandle
        """
        self._oprot.rlock.acquire()
        try:
            self.send_getAceList_IDL(aclHandle)
            result = self.recv_getAceList_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_getAceList_IDL(self, aclHandle):
        self._oprot.writeMessageBegin('getAceList_IDL', TMessageType.CALL, self._seqid)
        args = getAceList_IDL_args()
        args.aclHandle = aclHandle
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_getAceList_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = getAceList_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'getAceList_IDL failed: unknown result')



    def getL2AceList_IDL(self, aclHandle, aclName):
        """
            Get L2 ACE List
        
            Parameters:
             - aclHandle
             - aclName
            """
        self._oprot.rlock.acquire()
        try:
            self.send_getL2AceList_IDL(aclHandle, aclName)
            result = self.recv_getL2AceList_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_getL2AceList_IDL(self, aclHandle, aclName):
        self._oprot.writeMessageBegin('getL2AceList_IDL', TMessageType.CALL, self._seqid)
        args = getL2AceList_IDL_args()
        args.aclHandle = aclHandle
        args.aclName = aclName
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_getL2AceList_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = getL2AceList_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'getL2AceList_IDL failed: unknown result')



    def getAclList_IDL(self, aclType):
        """
            Get list of all ACLs on Network Element
        
            Parameters:
             - aclType
            """
        self._oprot.rlock.acquire()
        try:
            self.send_getAclList_IDL(aclType)
            result = self.recv_getAclList_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_getAclList_IDL(self, aclType):
        self._oprot.writeMessageBegin('getAclList_IDL', TMessageType.CALL, self._seqid)
        args = getAclList_IDL_args()
        args.aclType = aclType
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_getAclList_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = getAclList_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'getAclList_IDL failed: unknown result')



    def getIfcAclList_IDL(self, ifHandle, direction, aclType):
        """
            Get list of all ACLs on Network Interface
        
            Parameters:
             - ifHandle
             - direction
             - aclType
            """
        self._oprot.rlock.acquire()
        try:
            self.send_getIfcAclList_IDL(ifHandle, direction, aclType)
            result = self.recv_getIfcAclList_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_getIfcAclList_IDL(self, ifHandle, direction, aclType):
        self._oprot.writeMessageBegin('getIfcAclList_IDL', TMessageType.CALL, self._seqid)
        args = getIfcAclList_IDL_args()
        args.ifHandle = ifHandle
        args.direction = direction
        args.aclType = aclType
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_getIfcAclList_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = getIfcAclList_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'getIfcAclList_IDL failed: unknown result')



    def getAclByName_IDL(self, aclName):
        """
            Get ACL by name on Network Element
        
            Parameters:
             - aclName
            """
        self._oprot.rlock.acquire()
        try:
            self.send_getAclByName_IDL(aclName)
            result = self.recv_getAclByName_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_getAclByName_IDL(self, aclName):
        self._oprot.writeMessageBegin('getAclByName_IDL', TMessageType.CALL, self._seqid)
        args = getAclByName_IDL_args()
        args.aclName = aclName
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_getAclByName_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = getAclByName_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'getAclByName_IDL failed: unknown result')



    def getAclName_IDL(self, aclHandle):
        """
            Get ACL name
        
            Parameters:
             - aclHandle
            """
        self._oprot.rlock.acquire()
        try:
            self.send_getAclName_IDL(aclHandle)
            result = self.recv_getAclName_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_getAclName_IDL(self, aclHandle):
        self._oprot.writeMessageBegin('getAclName_IDL', TMessageType.CALL, self._seqid)
        args = getAclName_IDL_args()
        args.aclHandle = aclHandle
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_getAclName_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = getAclName_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'getAclName_IDL failed: unknown result')



    def addL3Ace_IDL(self, aclHandle, aceParam):
        """
            Add L3 ACE to ACL
        
            Parameters:
             - aclHandle
             - aceParam
            """
        self._oprot.rlock.acquire()
        try:
            self.send_addL3Ace_IDL(aclHandle, aceParam)
            result = self.recv_addL3Ace_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_addL3Ace_IDL(self, aclHandle, aceParam):
        self._oprot.writeMessageBegin('addL3Ace_IDL', TMessageType.CALL, self._seqid)
        args = addL3Ace_IDL_args()
        args.aclHandle = aclHandle
        args.aceParam = aceParam
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_addL3Ace_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = addL3Ace_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'addL3Ace_IDL failed: unknown result')



    def addL2Ace_IDL(self, aclHandle, aceParam):
        """
            Add L2 ACE to ACL
        
            Parameters:
             - aclHandle
             - aceParam
            """
        self._oprot.rlock.acquire()
        try:
            self.send_addL2Ace_IDL(aclHandle, aceParam)
            result = self.recv_addL2Ace_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_addL2Ace_IDL(self, aclHandle, aceParam):
        self._oprot.writeMessageBegin('addL2Ace_IDL', TMessageType.CALL, self._seqid)
        args = addL2Ace_IDL_args()
        args.aclHandle = aclHandle
        args.aceParam = aceParam
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_addL2Ace_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = addL2Ace_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'addL2Ace_IDL failed: unknown result')



    def deleteAce_IDL(self, aclHandle, elemHandle):
        """
            Delete ACE from ACL
        
            Parameters:
             - aclHandle
             - elemHandle
            """
        self._oprot.rlock.acquire()
        try:
            self.send_deleteAce_IDL(aclHandle, elemHandle)
            result = self.recv_deleteAce_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_deleteAce_IDL(self, aclHandle, elemHandle):
        self._oprot.writeMessageBegin('deleteAce_IDL', TMessageType.CALL, self._seqid)
        args = deleteAce_IDL_args()
        args.aclHandle = aclHandle
        args.elemHandle = elemHandle
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_deleteAce_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = deleteAce_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'deleteAce_IDL failed: unknown result')



    def applyAclToInterface_IDL(self, aclHandle, ifHandle, direction):
        """
            Apply ACL to Interface
        
            Parameters:
             - aclHandle
             - ifHandle
             - direction
            """
        self._oprot.rlock.acquire()
        try:
            self.send_applyAclToInterface_IDL(aclHandle, ifHandle, direction)
            result = self.recv_applyAclToInterface_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_applyAclToInterface_IDL(self, aclHandle, ifHandle, direction):
        self._oprot.writeMessageBegin('applyAclToInterface_IDL', TMessageType.CALL, self._seqid)
        args = applyAclToInterface_IDL_args()
        args.aclHandle = aclHandle
        args.ifHandle = ifHandle
        args.direction = direction
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_applyAclToInterface_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = applyAclToInterface_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'applyAclToInterface_IDL failed: unknown result')



    def removeAclFromInterface_IDL(self, aclHandle, ifHandle, direction):
        """
            Remove ACL from Interface
        
            Parameters:
             - aclHandle
             - ifHandle
             - direction
            """
        self._oprot.rlock.acquire()
        try:
            self.send_removeAclFromInterface_IDL(aclHandle, ifHandle, direction)
            result = self.recv_removeAclFromInterface_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_removeAclFromInterface_IDL(self, aclHandle, ifHandle, direction):
        self._oprot.writeMessageBegin('removeAclFromInterface_IDL', TMessageType.CALL, self._seqid)
        args = removeAclFromInterface_IDL_args()
        args.aclHandle = aclHandle
        args.ifHandle = ifHandle
        args.direction = direction
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_removeAclFromInterface_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = removeAclFromInterface_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'removeAclFromInterface_IDL failed: unknown result')



    def getAceMatch_IDL(self, aclHandle, elemHandle):
        """
            Get ACE match count
        
            Parameters:
             - aclHandle
             - elemHandle
            """
        self._oprot.rlock.acquire()
        try:
            self.send_getAceMatch_IDL(aclHandle, elemHandle)
            result = self.recv_getAceMatch_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_getAceMatch_IDL(self, aclHandle, elemHandle):
        self._oprot.writeMessageBegin('getAceMatch_IDL', TMessageType.CALL, self._seqid)
        args = getAceMatch_IDL_args()
        args.aclHandle = aclHandle
        args.elemHandle = elemHandle
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_getAceMatch_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = getAceMatch_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'getAceMatch_IDL failed: unknown result')



    def clearAclMatch_IDL(self, aclHandle):
        """
            Clear ACL match counters
        
            Parameters:
             - aclHandle
            """
        self._oprot.rlock.acquire()
        try:
            self.send_clearAclMatch_IDL(aclHandle)
            result = self.recv_clearAclMatch_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_clearAclMatch_IDL(self, aclHandle):
        self._oprot.writeMessageBegin('clearAclMatch_IDL', TMessageType.CALL, self._seqid)
        args = clearAclMatch_IDL_args()
        args.aclHandle = aclHandle
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_clearAclMatch_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = clearAclMatch_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'clearAclMatch_IDL failed: unknown result')



    def getPolicyCapability_IDL(self, handle):
        """
            Get Policy capability
        
            Parameters:
             - handle
            """
        self._oprot.rlock.acquire()
        try:
            self.send_getPolicyCapability_IDL(handle)
            result = self.recv_getPolicyCapability_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_getPolicyCapability_IDL(self, handle):
        self._oprot.writeMessageBegin('getPolicyCapability_IDL', TMessageType.CALL, self._seqid)
        args = getPolicyCapability_IDL_args()
        args.handle = handle
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_getPolicyCapability_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = getPolicyCapability_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'getPolicyCapability_IDL failed: unknown result')



    def getProtocolCapability_IDL(self, handle):
        """
            Get Protocol capability
        
            Parameters:
             - handle
            """
        self._oprot.rlock.acquire()
        try:
            self.send_getProtocolCapability_IDL(handle)
            result = self.recv_getProtocolCapability_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_getProtocolCapability_IDL(self, handle):
        self._oprot.writeMessageBegin('getProtocolCapability_IDL', TMessageType.CALL, self._seqid)
        args = getProtocolCapability_IDL_args()
        args.handle = handle
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_getProtocolCapability_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = getProtocolCapability_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'getProtocolCapability_IDL failed: unknown result')



    def getSubProtocolCapability_IDL(self, protocol):
        """
            Get Sub-Protocol capability
        
            Parameters:
             - protocol
            """
        self._oprot.rlock.acquire()
        try:
            self.send_getSubProtocolCapability_IDL(protocol)
            result = self.recv_getSubProtocolCapability_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_getSubProtocolCapability_IDL(self, protocol):
        self._oprot.writeMessageBegin('getSubProtocolCapability_IDL', TMessageType.CALL, self._seqid)
        args = getSubProtocolCapability_IDL_args()
        args.protocol = protocol
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_getSubProtocolCapability_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = getSubProtocolCapability_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'getSubProtocolCapability_IDL failed: unknown result')



    def createNamedAcl_IDL(self, sessionId, type, persistent, addrFamily):
        """
            Create Named ACL
        
            Parameters:
             - sessionId
             - type
             - persistent
             - addrFamily
            """
        self._oprot.rlock.acquire()
        try:
            self.send_createNamedAcl_IDL(sessionId, type, persistent, addrFamily)
            result = self.recv_createNamedAcl_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_createNamedAcl_IDL(self, sessionId, type, persistent, addrFamily):
        self._oprot.writeMessageBegin('createNamedAcl_IDL', TMessageType.CALL, self._seqid)
        args = createNamedAcl_IDL_args()
        args.sessionId = sessionId
        args.type = type
        args.persistent = persistent
        args.addrFamily = addrFamily
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_createNamedAcl_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = createNamedAcl_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'createNamedAcl_IDL failed: unknown result')



    def deleteNamedAcl_IDL(self, sessionId, name, aclHandle, lifetime, addrFamily):
        """
            Delete Named ACL
        
            Parameters:
             - sessionId
             - name
             - aclHandle
             - lifetime
             - addrFamily
            """
        self._oprot.rlock.acquire()
        try:
            self.send_deleteNamedAcl_IDL(sessionId, name, aclHandle, lifetime, addrFamily)
            result = self.recv_deleteNamedAcl_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_deleteNamedAcl_IDL(self, sessionId, name, aclHandle, lifetime, addrFamily):
        self._oprot.writeMessageBegin('deleteNamedAcl_IDL', TMessageType.CALL, self._seqid)
        args = deleteNamedAcl_IDL_args()
        args.sessionId = sessionId
        args.name = name
        args.aclHandle = aclHandle
        args.lifetime = lifetime
        args.addrFamily = addrFamily
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_deleteNamedAcl_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = deleteNamedAcl_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'deleteNamedAcl_IDL failed: unknown result')



    def addNamedL3Ace_IDL(self, name, aclHandle, lifetime, addrFamily, aceParam):
        """
            Add L3 ACE to Named ACL
        
            Parameters:
             - name
             - aclHandle
             - lifetime
             - addrFamily
             - aceParam
            """
        self._oprot.rlock.acquire()
        try:
            self.send_addNamedL3Ace_IDL(name, aclHandle, lifetime, addrFamily, aceParam)
            result = self.recv_addNamedL3Ace_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_addNamedL3Ace_IDL(self, name, aclHandle, lifetime, addrFamily, aceParam):
        self._oprot.writeMessageBegin('addNamedL3Ace_IDL', TMessageType.CALL, self._seqid)
        args = addNamedL3Ace_IDL_args()
        args.name = name
        args.aclHandle = aclHandle
        args.lifetime = lifetime
        args.addrFamily = addrFamily
        args.aceParam = aceParam
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_addNamedL3Ace_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = addNamedL3Ace_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'addNamedL3Ace_IDL failed: unknown result')



    def deleteNamedAce_IDL(self, name, aclHandle, elemHandle, lifetime, addrFamily):
        """
            Delete ACE from Named ACL
        
            Parameters:
             - name
             - aclHandle
             - elemHandle
             - lifetime
             - addrFamily
            """
        self._oprot.rlock.acquire()
        try:
            self.send_deleteNamedAce_IDL(name, aclHandle, elemHandle, lifetime, addrFamily)
            result = self.recv_deleteNamedAce_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_deleteNamedAce_IDL(self, name, aclHandle, elemHandle, lifetime, addrFamily):
        self._oprot.writeMessageBegin('deleteNamedAce_IDL', TMessageType.CALL, self._seqid)
        args = deleteNamedAce_IDL_args()
        args.name = name
        args.aclHandle = aclHandle
        args.elemHandle = elemHandle
        args.lifetime = lifetime
        args.addrFamily = addrFamily
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_deleteNamedAce_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = deleteNamedAce_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'deleteNamedAce_IDL failed: unknown result')



    def applyNamedAclToInterface_IDL(self, name, aclType, ifHandle, direction, addrFamily):
        """
            Apply Named ACL to Interface
        
            Parameters:
             - name
             - aclType
             - ifHandle
             - direction
             - addrFamily
            """
        self._oprot.rlock.acquire()
        try:
            self.send_applyNamedAclToInterface_IDL(name, aclType, ifHandle, direction, addrFamily)
            result = self.recv_applyNamedAclToInterface_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_applyNamedAclToInterface_IDL(self, name, aclType, ifHandle, direction, addrFamily):
        self._oprot.writeMessageBegin('applyNamedAclToInterface_IDL', TMessageType.CALL, self._seqid)
        args = applyNamedAclToInterface_IDL_args()
        args.name = name
        args.aclType = aclType
        args.ifHandle = ifHandle
        args.direction = direction
        args.addrFamily = addrFamily
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_applyNamedAclToInterface_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = applyNamedAclToInterface_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'applyNamedAclToInterface_IDL failed: unknown result')



    def removeNamedAclFromInterface_IDL(self, name, aclType, ifHandle, direction, addrFamily):
        """
            Remove Named ACL from Interface
        
            Parameters:
             - name
             - aclType
             - ifHandle
             - direction
             - addrFamily
            """
        self._oprot.rlock.acquire()
        try:
            self.send_removeNamedAclFromInterface_IDL(name, aclType, ifHandle, direction, addrFamily)
            result = self.recv_removeNamedAclFromInterface_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_removeNamedAclFromInterface_IDL(self, name, aclType, ifHandle, direction, addrFamily):
        self._oprot.writeMessageBegin('removeNamedAclFromInterface_IDL', TMessageType.CALL, self._seqid)
        args = removeNamedAclFromInterface_IDL_args()
        args.name = name
        args.aclType = aclType
        args.ifHandle = ifHandle
        args.direction = direction
        args.addrFamily = addrFamily
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_removeNamedAclFromInterface_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = removeNamedAclFromInterface_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'removeNamedAclFromInterface_IDL failed: unknown result')



    def getNamedAceMatch_IDL(self, name, aclHandle, elemHandle, lifetime, addrFamily):
        """
            Get ACE match count
        
            Parameters:
             - name
             - aclHandle
             - elemHandle
             - lifetime
             - addrFamily
            """
        self._oprot.rlock.acquire()
        try:
            self.send_getNamedAceMatch_IDL(name, aclHandle, elemHandle, lifetime, addrFamily)
            result = self.recv_getNamedAceMatch_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_getNamedAceMatch_IDL(self, name, aclHandle, elemHandle, lifetime, addrFamily):
        self._oprot.writeMessageBegin('getNamedAceMatch_IDL', TMessageType.CALL, self._seqid)
        args = getNamedAceMatch_IDL_args()
        args.name = name
        args.aclHandle = aclHandle
        args.elemHandle = elemHandle
        args.lifetime = lifetime
        args.addrFamily = addrFamily
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_getNamedAceMatch_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = getNamedAceMatch_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'getNamedAceMatch_IDL failed: unknown result')




class Processor(Iface, TProcessor):

    def __init__(self, handler):
        self._handler = handler
        self._processMap = {}
        self._processMap['createPolicy_IDL'] = Processor.process_createPolicy_IDL
        self._processMap['deletePolicy_IDL'] = Processor.process_deletePolicy_IDL
        self._processMap['deleteAllPolicies_IDL'] = Processor.process_deleteAllPolicies_IDL
        self._processMap['createClass_IDL'] = Processor.process_createClass_IDL
        self._processMap['deleteClass_IDL'] = Processor.process_deleteClass_IDL
        self._processMap['addClassToPolicy_IDL'] = Processor.process_addClassToPolicy_IDL
        self._processMap['removeClassFromPolicy_IDL'] = Processor.process_removeClassFromPolicy_IDL
        self._processMap['addChildToPolicy_IDL'] = Processor.process_addChildToPolicy_IDL
        self._processMap['removeChildFromPolicy_IDL'] = Processor.process_removeChildFromPolicy_IDL
        self._processMap['removeFilterFromClass_IDL'] = Processor.process_removeFilterFromClass_IDL
        self._processMap['setFilterSense_IDL'] = Processor.process_setFilterSense_IDL
        self._processMap['addFilterAclToClass_IDL'] = Processor.process_addFilterAclToClass_IDL
        self._processMap['addFilterDscpToClass_IDL'] = Processor.process_addFilterDscpToClass_IDL
        self._processMap['addFilterMplsToClass_IDL'] = Processor.process_addFilterMplsToClass_IDL
        self._processMap['addFilterDlciToClass_IDL'] = Processor.process_addFilterDlciToClass_IDL
        self._processMap['addFilterDeToClass_IDL'] = Processor.process_addFilterDeToClass_IDL
        self._processMap['addFilterL2CosToClass_IDL'] = Processor.process_addFilterL2CosToClass_IDL
        self._processMap['addFilterMacAddressToClass_IDL'] = Processor.process_addFilterMacAddressToClass_IDL
        self._processMap['addFilterPktLenToClass_IDL'] = Processor.process_addFilterPktLenToClass_IDL
        self._processMap['addFilterProtocolToClass_IDL'] = Processor.process_addFilterProtocolToClass_IDL
        self._processMap['addFilterQosGroupToClass_IDL'] = Processor.process_addFilterQosGroupToClass_IDL
        self._processMap['addFilterRtpPortToClass_IDL'] = Processor.process_addFilterRtpPortToClass_IDL
        self._processMap['addFilterVlanToClass_IDL'] = Processor.process_addFilterVlanToClass_IDL
        self._processMap['removeActionFromClass_IDL'] = Processor.process_removeActionFromClass_IDL
        self._processMap['addActionDropToClass_IDL'] = Processor.process_addActionDropToClass_IDL
        self._processMap['addActionIfcToClass_IDL'] = Processor.process_addActionIfcToClass_IDL
        self._processMap['addActionNextHopToClass_IDL'] = Processor.process_addActionNextHopToClass_IDL
        self._processMap['addActionMarkToClass_IDL'] = Processor.process_addActionMarkToClass_IDL
        self._processMap['addActionPoliceToClass_IDL'] = Processor.process_addActionPoliceToClass_IDL
        self._processMap['addActionShapeToClass_IDL'] = Processor.process_addActionShapeToClass_IDL
        self._processMap['addActionPriorityQueueToClass_IDL'] = Processor.process_addActionPriorityQueueToClass_IDL
        self._processMap['addActionClassBasedQueueToClass_IDL'] = Processor.process_addActionClassBasedQueueToClass_IDL
        self._processMap['addActionFairQueueToClass_IDL'] = Processor.process_addActionFairQueueToClass_IDL
        self._processMap['addActionQueueLimitToClass_IDL'] = Processor.process_addActionQueueLimitToClass_IDL
        self._processMap['addActionWredToClass_IDL'] = Processor.process_addActionWredToClass_IDL
        self._processMap['addWredProfileToClass_IDL'] = Processor.process_addWredProfileToClass_IDL
        self._processMap['removeWredProfileFromClass_IDL'] = Processor.process_removeWredProfileFromClass_IDL
        self._processMap['addActionCopyToClass_IDL'] = Processor.process_addActionCopyToClass_IDL
        self._processMap['addActionDivertToClass_IDL'] = Processor.process_addActionDivertToClass_IDL
        self._processMap['addActionCopyToAce_IDL'] = Processor.process_addActionCopyToAce_IDL
        self._processMap['addActionDivertToAce_IDL'] = Processor.process_addActionDivertToAce_IDL
        self._processMap['removeActionFromAce_IDL'] = Processor.process_removeActionFromAce_IDL
        self._processMap['applyPolicyToTarget_IDL'] = Processor.process_applyPolicyToTarget_IDL
        self._processMap['removePolicyFromTarget_IDL'] = Processor.process_removePolicyFromTarget_IDL
        self._processMap['createAcl_IDL'] = Processor.process_createAcl_IDL
        self._processMap['deleteAcl_IDL'] = Processor.process_deleteAcl_IDL
        self._processMap['getL3AceList_IDL'] = Processor.process_getL3AceList_IDL
        self._processMap['getAceList_IDL'] = Processor.process_getAceList_IDL
        self._processMap['getL2AceList_IDL'] = Processor.process_getL2AceList_IDL
        self._processMap['getAclList_IDL'] = Processor.process_getAclList_IDL
        self._processMap['getIfcAclList_IDL'] = Processor.process_getIfcAclList_IDL
        self._processMap['getAclByName_IDL'] = Processor.process_getAclByName_IDL
        self._processMap['getAclName_IDL'] = Processor.process_getAclName_IDL
        self._processMap['addL3Ace_IDL'] = Processor.process_addL3Ace_IDL
        self._processMap['addL2Ace_IDL'] = Processor.process_addL2Ace_IDL
        self._processMap['deleteAce_IDL'] = Processor.process_deleteAce_IDL
        self._processMap['applyAclToInterface_IDL'] = Processor.process_applyAclToInterface_IDL
        self._processMap['removeAclFromInterface_IDL'] = Processor.process_removeAclFromInterface_IDL
        self._processMap['getAceMatch_IDL'] = Processor.process_getAceMatch_IDL
        self._processMap['clearAclMatch_IDL'] = Processor.process_clearAclMatch_IDL
        self._processMap['getPolicyCapability_IDL'] = Processor.process_getPolicyCapability_IDL
        self._processMap['getProtocolCapability_IDL'] = Processor.process_getProtocolCapability_IDL
        self._processMap['getSubProtocolCapability_IDL'] = Processor.process_getSubProtocolCapability_IDL
        self._processMap['createNamedAcl_IDL'] = Processor.process_createNamedAcl_IDL
        self._processMap['deleteNamedAcl_IDL'] = Processor.process_deleteNamedAcl_IDL
        self._processMap['addNamedL3Ace_IDL'] = Processor.process_addNamedL3Ace_IDL
        self._processMap['deleteNamedAce_IDL'] = Processor.process_deleteNamedAce_IDL
        self._processMap['applyNamedAclToInterface_IDL'] = Processor.process_applyNamedAclToInterface_IDL
        self._processMap['removeNamedAclFromInterface_IDL'] = Processor.process_removeNamedAclFromInterface_IDL
        self._processMap['getNamedAceMatch_IDL'] = Processor.process_getNamedAceMatch_IDL



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



    def process_createPolicy_IDL(self, seqid, iprot, oprot):
        args = createPolicy_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = createPolicy_IDL_result()
        try:
            result.success = self._handler.createPolicy_IDL(args.sessionId, args.type, args.policyHandle)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('createPolicy_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_deletePolicy_IDL(self, seqid, iprot, oprot):
        args = deletePolicy_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = deletePolicy_IDL_result()
        try:
            result.success = self._handler.deletePolicy_IDL(args.sessionId, args.policyHandle)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('deletePolicy_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_deleteAllPolicies_IDL(self, seqid, iprot, oprot):
        args = deleteAllPolicies_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = deleteAllPolicies_IDL_result()
        try:
            result.success = self._handler.deleteAllPolicies_IDL(args.sessionId)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('deleteAllPolicies_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_createClass_IDL(self, seqid, iprot, oprot):
        args = createClass_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = createClass_IDL_result()
        try:
            result.success = self._handler.createClass_IDL(args.sessionId, args.classOper)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('createClass_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_deleteClass_IDL(self, seqid, iprot, oprot):
        args = deleteClass_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = deleteClass_IDL_result()
        try:
            result.success = self._handler.deleteClass_IDL(args.sessionId, args.classHandle)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('deleteClass_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_addClassToPolicy_IDL(self, seqid, iprot, oprot):
        args = addClassToPolicy_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = addClassToPolicy_IDL_result()
        try:
            result.success = self._handler.addClassToPolicy_IDL(args.policyHandle, args.classHandle, args.sequence)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('addClassToPolicy_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_removeClassFromPolicy_IDL(self, seqid, iprot, oprot):
        args = removeClassFromPolicy_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = removeClassFromPolicy_IDL_result()
        try:
            result.success = self._handler.removeClassFromPolicy_IDL(args.policyHandle, args.classHandle)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('removeClassFromPolicy_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_addChildToPolicy_IDL(self, seqid, iprot, oprot):
        args = addChildToPolicy_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = addChildToPolicy_IDL_result()
        try:
            result.success = self._handler.addChildToPolicy_IDL(args.parentHandle, args.childHandle, args.classHandle)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('addChildToPolicy_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_removeChildFromPolicy_IDL(self, seqid, iprot, oprot):
        args = removeChildFromPolicy_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = removeChildFromPolicy_IDL_result()
        try:
            result.success = self._handler.removeChildFromPolicy_IDL(args.parentHandle, args.childHandle, args.classHandle)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('removeChildFromPolicy_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_removeFilterFromClass_IDL(self, seqid, iprot, oprot):
        args = removeFilterFromClass_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = removeFilterFromClass_IDL_result()
        try:
            result.success = self._handler.removeFilterFromClass_IDL(args.classHandle, args.filterHandle)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('removeFilterFromClass_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_setFilterSense_IDL(self, seqid, iprot, oprot):
        args = setFilterSense_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = setFilterSense_IDL_result()
        try:
            result.success = self._handler.setFilterSense_IDL(args.classHandle, args.filterHandle, args.sense)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('setFilterSense_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_addFilterAclToClass_IDL(self, seqid, iprot, oprot):
        args = addFilterAclToClass_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = addFilterAclToClass_IDL_result()
        try:
            result.success = self._handler.addFilterAclToClass_IDL(args.classHandle, args.sense, args.aclHandle)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('addFilterAclToClass_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_addFilterDscpToClass_IDL(self, seqid, iprot, oprot):
        args = addFilterDscpToClass_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = addFilterDscpToClass_IDL_result()
        try:
            result.success = self._handler.addFilterDscpToClass_IDL(args.classHandle, args.sense, args.dscp)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('addFilterDscpToClass_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_addFilterMplsToClass_IDL(self, seqid, iprot, oprot):
        args = addFilterMplsToClass_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = addFilterMplsToClass_IDL_result()
        try:
            result.success = self._handler.addFilterMplsToClass_IDL(args.classHandle, args.sense, args.mplsExp)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('addFilterMplsToClass_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_addFilterDlciToClass_IDL(self, seqid, iprot, oprot):
        args = addFilterDlciToClass_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = addFilterDlciToClass_IDL_result()
        try:
            result.success = self._handler.addFilterDlciToClass_IDL(args.classHandle, args.sense, args.dlci)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('addFilterDlciToClass_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_addFilterDeToClass_IDL(self, seqid, iprot, oprot):
        args = addFilterDeToClass_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = addFilterDeToClass_IDL_result()
        try:
            result.success = self._handler.addFilterDeToClass_IDL(args.classHandle, args.sense)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('addFilterDeToClass_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_addFilterL2CosToClass_IDL(self, seqid, iprot, oprot):
        args = addFilterL2CosToClass_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = addFilterL2CosToClass_IDL_result()
        try:
            result.success = self._handler.addFilterL2CosToClass_IDL(args.classHandle, args.sense, args.l2cos)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('addFilterL2CosToClass_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_addFilterMacAddressToClass_IDL(self, seqid, iprot, oprot):
        args = addFilterMacAddressToClass_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = addFilterMacAddressToClass_IDL_result()
        try:
            result.success = self._handler.addFilterMacAddressToClass_IDL(args.classHandle, args.sense, args.macAddress)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('addFilterMacAddressToClass_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_addFilterPktLenToClass_IDL(self, seqid, iprot, oprot):
        args = addFilterPktLenToClass_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = addFilterPktLenToClass_IDL_result()
        try:
            result.success = self._handler.addFilterPktLenToClass_IDL(args.classHandle, args.sense, args.min, args.max)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('addFilterPktLenToClass_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_addFilterProtocolToClass_IDL(self, seqid, iprot, oprot):
        args = addFilterProtocolToClass_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = addFilterProtocolToClass_IDL_result()
        try:
            result.success = self._handler.addFilterProtocolToClass_IDL(args.classHandle, args.sense, args.protocol, args.subProtocol, args.param)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('addFilterProtocolToClass_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_addFilterQosGroupToClass_IDL(self, seqid, iprot, oprot):
        args = addFilterQosGroupToClass_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = addFilterQosGroupToClass_IDL_result()
        try:
            result.success = self._handler.addFilterQosGroupToClass_IDL(args.classHandle, args.sense, args.group)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('addFilterQosGroupToClass_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_addFilterRtpPortToClass_IDL(self, seqid, iprot, oprot):
        args = addFilterRtpPortToClass_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = addFilterRtpPortToClass_IDL_result()
        try:
            result.success = self._handler.addFilterRtpPortToClass_IDL(args.classHandle, args.sense, args.rtpPort)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('addFilterRtpPortToClass_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_addFilterVlanToClass_IDL(self, seqid, iprot, oprot):
        args = addFilterVlanToClass_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = addFilterVlanToClass_IDL_result()
        try:
            result.success = self._handler.addFilterVlanToClass_IDL(args.classHandle, args.sense, args.vlan)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('addFilterVlanToClass_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_removeActionFromClass_IDL(self, seqid, iprot, oprot):
        args = removeActionFromClass_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = removeActionFromClass_IDL_result()
        try:
            result.success = self._handler.removeActionFromClass_IDL(args.policyHandle, args.classHandle, args.actionHandle)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('removeActionFromClass_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_addActionDropToClass_IDL(self, seqid, iprot, oprot):
        args = addActionDropToClass_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = addActionDropToClass_IDL_result()
        try:
            result.success = self._handler.addActionDropToClass_IDL(args.policyHandle, args.classHandle, args.remoteSn, args.appId, args.localId)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('addActionDropToClass_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_addActionIfcToClass_IDL(self, seqid, iprot, oprot):
        args = addActionIfcToClass_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = addActionIfcToClass_IDL_result()
        try:
            result.success = self._handler.addActionIfcToClass_IDL(args.policyHandle, args.classHandle, args.ifHandle)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('addActionIfcToClass_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_addActionNextHopToClass_IDL(self, seqid, iprot, oprot):
        args = addActionNextHopToClass_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = addActionNextHopToClass_IDL_result()
        try:
            result.success = self._handler.addActionNextHopToClass_IDL(args.policyHandle, args.classHandle, args.addrAF, args.nextHopAddress)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('addActionNextHopToClass_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_addActionMarkToClass_IDL(self, seqid, iprot, oprot):
        args = addActionMarkToClass_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = addActionMarkToClass_IDL_result()
        try:
            result.success = self._handler.addActionMarkToClass_IDL(args.policyHandle, args.classHandle, args.markParam)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('addActionMarkToClass_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_addActionPoliceToClass_IDL(self, seqid, iprot, oprot):
        args = addActionPoliceToClass_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = addActionPoliceToClass_IDL_result()
        try:
            result.success = self._handler.addActionPoliceToClass_IDL(args.policyHandle, args.classHandle, args.policeParam)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('addActionPoliceToClass_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_addActionShapeToClass_IDL(self, seqid, iprot, oprot):
        args = addActionShapeToClass_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = addActionShapeToClass_IDL_result()
        try:
            result.success = self._handler.addActionShapeToClass_IDL(args.policyHandle, args.classHandle, args.shapeParam)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('addActionShapeToClass_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_addActionPriorityQueueToClass_IDL(self, seqid, iprot, oprot):
        args = addActionPriorityQueueToClass_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = addActionPriorityQueueToClass_IDL_result()
        try:
            result.success = self._handler.addActionPriorityQueueToClass_IDL(args.policyHandle, args.classHandle, args.queueParam)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('addActionPriorityQueueToClass_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_addActionClassBasedQueueToClass_IDL(self, seqid, iprot, oprot):
        args = addActionClassBasedQueueToClass_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = addActionClassBasedQueueToClass_IDL_result()
        try:
            result.success = self._handler.addActionClassBasedQueueToClass_IDL(args.policyHandle, args.classHandle, args.queueParam)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('addActionClassBasedQueueToClass_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_addActionFairQueueToClass_IDL(self, seqid, iprot, oprot):
        args = addActionFairQueueToClass_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = addActionFairQueueToClass_IDL_result()
        try:
            result.success = self._handler.addActionFairQueueToClass_IDL(args.policyHandle, args.classHandle, args.queueParam)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('addActionFairQueueToClass_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_addActionQueueLimitToClass_IDL(self, seqid, iprot, oprot):
        args = addActionQueueLimitToClass_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = addActionQueueLimitToClass_IDL_result()
        try:
            result.success = self._handler.addActionQueueLimitToClass_IDL(args.policyHandle, args.classHandle, args.queueParam)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('addActionQueueLimitToClass_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_addActionWredToClass_IDL(self, seqid, iprot, oprot):
        args = addActionWredToClass_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = addActionWredToClass_IDL_result()
        try:
            result.success = self._handler.addActionWredToClass_IDL(args.policyHandle, args.classHandle, args.type, args.ecnEnabled, args.exponWeight, args.thresholdUnits)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('addActionWredToClass_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_addWredProfileToClass_IDL(self, seqid, iprot, oprot):
        args = addWredProfileToClass_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = addWredProfileToClass_IDL_result()
        try:
            result.success = self._handler.addWredProfileToClass_IDL(args.policyHandle, args.classHandle, args.type, args.value, args.minThreshold, args.maxThreshold, args.thresholdUnits, args.dropProb)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('addWredProfileToClass_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_removeWredProfileFromClass_IDL(self, seqid, iprot, oprot):
        args = removeWredProfileFromClass_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = removeWredProfileFromClass_IDL_result()
        try:
            result.success = self._handler.removeWredProfileFromClass_IDL(args.policyHandle, args.classHandle, args.type, args.value, args.minThreshold, args.maxThreshold, args.thresholdUnits, args.dropProb)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('removeWredProfileFromClass_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_addActionCopyToClass_IDL(self, seqid, iprot, oprot):
        args = addActionCopyToClass_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = addActionCopyToClass_IDL_result()
        try:
            result.success = self._handler.addActionCopyToClass_IDL(args.policyHandle, args.classHandle, args.remoteSn, args.appId, args.localId, args.size, args.sampleType, args.sampleRate)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('addActionCopyToClass_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_addActionDivertToClass_IDL(self, seqid, iprot, oprot):
        args = addActionDivertToClass_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = addActionDivertToClass_IDL_result()
        try:
            result.success = self._handler.addActionDivertToClass_IDL(args.policyHandle, args.classHandle, args.remoteSn, args.appId, args.localId, args.stateless)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('addActionDivertToClass_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_addActionCopyToAce_IDL(self, seqid, iprot, oprot):
        args = addActionCopyToAce_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = addActionCopyToAce_IDL_result()
        try:
            result.success = self._handler.addActionCopyToAce_IDL(args.aclHandle, args.aceHandle, args.remoteSn, args.appId, args.localId, args.size, args.sampleType, args.sampleRate)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('addActionCopyToAce_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_addActionDivertToAce_IDL(self, seqid, iprot, oprot):
        args = addActionDivertToAce_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = addActionDivertToAce_IDL_result()
        try:
            result.success = self._handler.addActionDivertToAce_IDL(args.aclHandle, args.aceHandle, args.remoteSn, args.appId, args.localId)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('addActionDivertToAce_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_removeActionFromAce_IDL(self, seqid, iprot, oprot):
        args = removeActionFromAce_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = removeActionFromAce_IDL_result()
        try:
            result.success = self._handler.removeActionFromAce_IDL(args.aclHandle, args.aceHandle, args.actionHandle)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('removeActionFromAce_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_applyPolicyToTarget_IDL(self, seqid, iprot, oprot):
        args = applyPolicyToTarget_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = applyPolicyToTarget_IDL_result()
        try:
            result.success = self._handler.applyPolicyToTarget_IDL(args.policyHandle, args.ifHandle, args.location)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('applyPolicyToTarget_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_removePolicyFromTarget_IDL(self, seqid, iprot, oprot):
        args = removePolicyFromTarget_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = removePolicyFromTarget_IDL_result()
        try:
            result.success = self._handler.removePolicyFromTarget_IDL(args.policyHandle, args.ifHandle, args.location)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('removePolicyFromTarget_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_createAcl_IDL(self, seqid, iprot, oprot):
        args = createAcl_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = createAcl_IDL_result()
        try:
            result.success = self._handler.createAcl_IDL(args.sessionId, args.type, args.persistent, args.addrFamily)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('createAcl_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_deleteAcl_IDL(self, seqid, iprot, oprot):
        args = deleteAcl_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = deleteAcl_IDL_result()
        try:
            result.success = self._handler.deleteAcl_IDL(args.sessionId, args.aclHandle)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('deleteAcl_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_getL3AceList_IDL(self, seqid, iprot, oprot):
        args = getL3AceList_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getL3AceList_IDL_result()
        try:
            result.success = self._handler.getL3AceList_IDL(args.aclHandle, args.lifetime, args.aclName, args.addrFamily)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('getL3AceList_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_getAceList_IDL(self, seqid, iprot, oprot):
        args = getAceList_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getAceList_IDL_result()
        try:
            result.success = self._handler.getAceList_IDL(args.aclHandle)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('getAceList_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_getL2AceList_IDL(self, seqid, iprot, oprot):
        args = getL2AceList_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getL2AceList_IDL_result()
        try:
            result.success = self._handler.getL2AceList_IDL(args.aclHandle, args.aclName)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('getL2AceList_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_getAclList_IDL(self, seqid, iprot, oprot):
        args = getAclList_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getAclList_IDL_result()
        try:
            result.success = self._handler.getAclList_IDL(args.aclType)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('getAclList_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_getIfcAclList_IDL(self, seqid, iprot, oprot):
        args = getIfcAclList_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getIfcAclList_IDL_result()
        try:
            result.success = self._handler.getIfcAclList_IDL(args.ifHandle, args.direction, args.aclType)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('getIfcAclList_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_getAclByName_IDL(self, seqid, iprot, oprot):
        args = getAclByName_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getAclByName_IDL_result()
        try:
            result.success = self._handler.getAclByName_IDL(args.aclName)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('getAclByName_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_getAclName_IDL(self, seqid, iprot, oprot):
        args = getAclName_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getAclName_IDL_result()
        try:
            result.success = self._handler.getAclName_IDL(args.aclHandle)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('getAclName_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_addL3Ace_IDL(self, seqid, iprot, oprot):
        args = addL3Ace_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = addL3Ace_IDL_result()
        try:
            result.success = self._handler.addL3Ace_IDL(args.aclHandle, args.aceParam)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('addL3Ace_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_addL2Ace_IDL(self, seqid, iprot, oprot):
        args = addL2Ace_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = addL2Ace_IDL_result()
        try:
            result.success = self._handler.addL2Ace_IDL(args.aclHandle, args.aceParam)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('addL2Ace_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_deleteAce_IDL(self, seqid, iprot, oprot):
        args = deleteAce_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = deleteAce_IDL_result()
        try:
            result.success = self._handler.deleteAce_IDL(args.aclHandle, args.elemHandle)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('deleteAce_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_applyAclToInterface_IDL(self, seqid, iprot, oprot):
        args = applyAclToInterface_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = applyAclToInterface_IDL_result()
        try:
            result.success = self._handler.applyAclToInterface_IDL(args.aclHandle, args.ifHandle, args.direction)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('applyAclToInterface_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_removeAclFromInterface_IDL(self, seqid, iprot, oprot):
        args = removeAclFromInterface_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = removeAclFromInterface_IDL_result()
        try:
            result.success = self._handler.removeAclFromInterface_IDL(args.aclHandle, args.ifHandle, args.direction)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('removeAclFromInterface_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_getAceMatch_IDL(self, seqid, iprot, oprot):
        args = getAceMatch_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getAceMatch_IDL_result()
        try:
            result.success = self._handler.getAceMatch_IDL(args.aclHandle, args.elemHandle)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('getAceMatch_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_clearAclMatch_IDL(self, seqid, iprot, oprot):
        args = clearAclMatch_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = clearAclMatch_IDL_result()
        try:
            result.success = self._handler.clearAclMatch_IDL(args.aclHandle)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('clearAclMatch_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_getPolicyCapability_IDL(self, seqid, iprot, oprot):
        args = getPolicyCapability_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getPolicyCapability_IDL_result()
        try:
            result.success = self._handler.getPolicyCapability_IDL(args.handle)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('getPolicyCapability_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_getProtocolCapability_IDL(self, seqid, iprot, oprot):
        args = getProtocolCapability_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getProtocolCapability_IDL_result()
        try:
            result.success = self._handler.getProtocolCapability_IDL(args.handle)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('getProtocolCapability_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_getSubProtocolCapability_IDL(self, seqid, iprot, oprot):
        args = getSubProtocolCapability_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getSubProtocolCapability_IDL_result()
        try:
            result.success = self._handler.getSubProtocolCapability_IDL(args.protocol)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('getSubProtocolCapability_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_createNamedAcl_IDL(self, seqid, iprot, oprot):
        args = createNamedAcl_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = createNamedAcl_IDL_result()
        try:
            result.success = self._handler.createNamedAcl_IDL(args.sessionId, args.type, args.persistent, args.addrFamily)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('createNamedAcl_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_deleteNamedAcl_IDL(self, seqid, iprot, oprot):
        args = deleteNamedAcl_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = deleteNamedAcl_IDL_result()
        try:
            result.success = self._handler.deleteNamedAcl_IDL(args.sessionId, args.name, args.aclHandle, args.lifetime, args.addrFamily)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('deleteNamedAcl_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_addNamedL3Ace_IDL(self, seqid, iprot, oprot):
        args = addNamedL3Ace_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = addNamedL3Ace_IDL_result()
        try:
            result.success = self._handler.addNamedL3Ace_IDL(args.name, args.aclHandle, args.lifetime, args.addrFamily, args.aceParam)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('addNamedL3Ace_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_deleteNamedAce_IDL(self, seqid, iprot, oprot):
        args = deleteNamedAce_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = deleteNamedAce_IDL_result()
        try:
            result.success = self._handler.deleteNamedAce_IDL(args.name, args.aclHandle, args.elemHandle, args.lifetime, args.addrFamily)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('deleteNamedAce_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_applyNamedAclToInterface_IDL(self, seqid, iprot, oprot):
        args = applyNamedAclToInterface_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = applyNamedAclToInterface_IDL_result()
        try:
            result.success = self._handler.applyNamedAclToInterface_IDL(args.name, args.aclType, args.ifHandle, args.direction, args.addrFamily)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('applyNamedAclToInterface_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_removeNamedAclFromInterface_IDL(self, seqid, iprot, oprot):
        args = removeNamedAclFromInterface_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = removeNamedAclFromInterface_IDL_result()
        try:
            result.success = self._handler.removeNamedAclFromInterface_IDL(args.name, args.aclType, args.ifHandle, args.direction, args.addrFamily)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('removeNamedAclFromInterface_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_getNamedAceMatch_IDL(self, seqid, iprot, oprot):
        args = getNamedAceMatch_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = getNamedAceMatch_IDL_result()
        try:
            result.success = self._handler.getNamedAceMatch_IDL(args.name, args.aclHandle, args.elemHandle, args.lifetime, args.addrFamily)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('getNamedAceMatch_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()




class createPolicy_IDL_args(object):
    """
    Attributes:
     - sessionId
     - type
     - policyHandle
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionId',
      None,
      None),
     (2,
      TType.I16,
      'type',
      None,
      None),
     (3,
      TType.I32,
      'policyHandle',
      None,
      None))

    def __init__(self, sessionId = None, type = None, policyHandle = None):
        self.sessionId = sessionId
        self.type = type
        self.policyHandle = policyHandle



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
                if ftype == TType.I16:
                    self.type = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.policyHandle = iprot.readI32()
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
        oprot.writeStructBegin('createPolicy_IDL_args')
        if self.sessionId != None:
            oprot.writeFieldBegin('sessionId', TType.I32, 1)
            oprot.writeI32(self.sessionId)
            oprot.writeFieldEnd()
        if self.type != None:
            oprot.writeFieldBegin('type', TType.I16, 2)
            oprot.writeI16(self.type)
            oprot.writeFieldEnd()
        if self.policyHandle != None:
            oprot.writeFieldBegin('policyHandle', TType.I32, 3)
            oprot.writeI32(self.policyHandle)
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




class createPolicy_IDL_result(object):
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
        oprot.writeStructBegin('createPolicy_IDL_result')
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




class deletePolicy_IDL_args(object):
    """
    Attributes:
     - sessionId
     - policyHandle
    """

    thrift_spec = (None, (1,
      TType.I32,
      'sessionId',
      None,
      None), (2,
      TType.I32,
      'policyHandle',
      None,
      None))

    def __init__(self, sessionId = None, policyHandle = None):
        self.sessionId = sessionId
        self.policyHandle = policyHandle



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
                    self.policyHandle = iprot.readI32()
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
        oprot.writeStructBegin('deletePolicy_IDL_args')
        if self.sessionId != None:
            oprot.writeFieldBegin('sessionId', TType.I32, 1)
            oprot.writeI32(self.sessionId)
            oprot.writeFieldEnd()
        if self.policyHandle != None:
            oprot.writeFieldBegin('policyHandle', TType.I32, 2)
            oprot.writeI32(self.policyHandle)
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




class deletePolicy_IDL_result(object):
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
        oprot.writeStructBegin('deletePolicy_IDL_result')
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




class deleteAllPolicies_IDL_args(object):
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
        oprot.writeStructBegin('deleteAllPolicies_IDL_args')
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




class deleteAllPolicies_IDL_result(object):
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
        oprot.writeStructBegin('deleteAllPolicies_IDL_result')
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




class createClass_IDL_args(object):
    """
    Attributes:
     - sessionId
     - classOper
    """

    thrift_spec = (None, (1,
      TType.I32,
      'sessionId',
      None,
      None), (2,
      TType.I32,
      'classOper',
      None,
      None))

    def __init__(self, sessionId = None, classOper = None):
        self.sessionId = sessionId
        self.classOper = classOper



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
                    self.classOper = iprot.readI32()
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
        oprot.writeStructBegin('createClass_IDL_args')
        if self.sessionId != None:
            oprot.writeFieldBegin('sessionId', TType.I32, 1)
            oprot.writeI32(self.sessionId)
            oprot.writeFieldEnd()
        if self.classOper != None:
            oprot.writeFieldBegin('classOper', TType.I32, 2)
            oprot.writeI32(self.classOper)
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




class createClass_IDL_result(object):
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
        oprot.writeStructBegin('createClass_IDL_result')
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




class deleteClass_IDL_args(object):
    """
    Attributes:
     - sessionId
     - classHandle
    """

    thrift_spec = (None, (1,
      TType.I32,
      'sessionId',
      None,
      None), (2,
      TType.I32,
      'classHandle',
      None,
      None))

    def __init__(self, sessionId = None, classHandle = None):
        self.sessionId = sessionId
        self.classHandle = classHandle



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
                    self.classHandle = iprot.readI32()
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
        oprot.writeStructBegin('deleteClass_IDL_args')
        if self.sessionId != None:
            oprot.writeFieldBegin('sessionId', TType.I32, 1)
            oprot.writeI32(self.sessionId)
            oprot.writeFieldEnd()
        if self.classHandle != None:
            oprot.writeFieldBegin('classHandle', TType.I32, 2)
            oprot.writeI32(self.classHandle)
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




class deleteClass_IDL_result(object):
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
        oprot.writeStructBegin('deleteClass_IDL_result')
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




class addClassToPolicy_IDL_args(object):
    """
    Attributes:
     - policyHandle
     - classHandle
     - sequence
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'policyHandle',
      None,
      None),
     (2,
      TType.I32,
      'classHandle',
      None,
      None),
     (3,
      TType.I32,
      'sequence',
      None,
      None))

    def __init__(self, policyHandle = None, classHandle = None, sequence = None):
        self.policyHandle = policyHandle
        self.classHandle = classHandle
        self.sequence = sequence



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
                    self.policyHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.classHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.sequence = iprot.readI32()
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
        oprot.writeStructBegin('addClassToPolicy_IDL_args')
        if self.policyHandle != None:
            oprot.writeFieldBegin('policyHandle', TType.I32, 1)
            oprot.writeI32(self.policyHandle)
            oprot.writeFieldEnd()
        if self.classHandle != None:
            oprot.writeFieldBegin('classHandle', TType.I32, 2)
            oprot.writeI32(self.classHandle)
            oprot.writeFieldEnd()
        if self.sequence != None:
            oprot.writeFieldBegin('sequence', TType.I32, 3)
            oprot.writeI32(self.sequence)
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




class addClassToPolicy_IDL_result(object):
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
        oprot.writeStructBegin('addClassToPolicy_IDL_result')
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




class removeClassFromPolicy_IDL_args(object):
    """
    Attributes:
     - policyHandle
     - classHandle
    """

    thrift_spec = (None, (1,
      TType.I32,
      'policyHandle',
      None,
      None), (2,
      TType.I32,
      'classHandle',
      None,
      None))

    def __init__(self, policyHandle = None, classHandle = None):
        self.policyHandle = policyHandle
        self.classHandle = classHandle



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
                    self.policyHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.classHandle = iprot.readI32()
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
        oprot.writeStructBegin('removeClassFromPolicy_IDL_args')
        if self.policyHandle != None:
            oprot.writeFieldBegin('policyHandle', TType.I32, 1)
            oprot.writeI32(self.policyHandle)
            oprot.writeFieldEnd()
        if self.classHandle != None:
            oprot.writeFieldBegin('classHandle', TType.I32, 2)
            oprot.writeI32(self.classHandle)
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




class removeClassFromPolicy_IDL_result(object):
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
        oprot.writeStructBegin('removeClassFromPolicy_IDL_result')
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




class addChildToPolicy_IDL_args(object):
    """
    Attributes:
     - parentHandle
     - childHandle
     - classHandle
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'parentHandle',
      None,
      None),
     (2,
      TType.I32,
      'childHandle',
      None,
      None),
     (3,
      TType.I32,
      'classHandle',
      None,
      None))

    def __init__(self, parentHandle = None, childHandle = None, classHandle = None):
        self.parentHandle = parentHandle
        self.childHandle = childHandle
        self.classHandle = classHandle



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
                    self.parentHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.childHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.classHandle = iprot.readI32()
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
        oprot.writeStructBegin('addChildToPolicy_IDL_args')
        if self.parentHandle != None:
            oprot.writeFieldBegin('parentHandle', TType.I32, 1)
            oprot.writeI32(self.parentHandle)
            oprot.writeFieldEnd()
        if self.childHandle != None:
            oprot.writeFieldBegin('childHandle', TType.I32, 2)
            oprot.writeI32(self.childHandle)
            oprot.writeFieldEnd()
        if self.classHandle != None:
            oprot.writeFieldBegin('classHandle', TType.I32, 3)
            oprot.writeI32(self.classHandle)
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




class addChildToPolicy_IDL_result(object):
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
        oprot.writeStructBegin('addChildToPolicy_IDL_result')
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




class removeChildFromPolicy_IDL_args(object):
    """
    Attributes:
     - parentHandle
     - childHandle
     - classHandle
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'parentHandle',
      None,
      None),
     (2,
      TType.I32,
      'childHandle',
      None,
      None),
     (3,
      TType.I32,
      'classHandle',
      None,
      None))

    def __init__(self, parentHandle = None, childHandle = None, classHandle = None):
        self.parentHandle = parentHandle
        self.childHandle = childHandle
        self.classHandle = classHandle



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
                    self.parentHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.childHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.classHandle = iprot.readI32()
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
        oprot.writeStructBegin('removeChildFromPolicy_IDL_args')
        if self.parentHandle != None:
            oprot.writeFieldBegin('parentHandle', TType.I32, 1)
            oprot.writeI32(self.parentHandle)
            oprot.writeFieldEnd()
        if self.childHandle != None:
            oprot.writeFieldBegin('childHandle', TType.I32, 2)
            oprot.writeI32(self.childHandle)
            oprot.writeFieldEnd()
        if self.classHandle != None:
            oprot.writeFieldBegin('classHandle', TType.I32, 3)
            oprot.writeI32(self.classHandle)
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




class removeChildFromPolicy_IDL_result(object):
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
        oprot.writeStructBegin('removeChildFromPolicy_IDL_result')
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




class removeFilterFromClass_IDL_args(object):
    """
    Attributes:
     - classHandle
     - filterHandle
    """

    thrift_spec = (None, (1,
      TType.I32,
      'classHandle',
      None,
      None), (2,
      TType.I32,
      'filterHandle',
      None,
      None))

    def __init__(self, classHandle = None, filterHandle = None):
        self.classHandle = classHandle
        self.filterHandle = filterHandle



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
                    self.classHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.filterHandle = iprot.readI32()
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
        oprot.writeStructBegin('removeFilterFromClass_IDL_args')
        if self.classHandle != None:
            oprot.writeFieldBegin('classHandle', TType.I32, 1)
            oprot.writeI32(self.classHandle)
            oprot.writeFieldEnd()
        if self.filterHandle != None:
            oprot.writeFieldBegin('filterHandle', TType.I32, 2)
            oprot.writeI32(self.filterHandle)
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




class removeFilterFromClass_IDL_result(object):
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
        oprot.writeStructBegin('removeFilterFromClass_IDL_result')
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




class setFilterSense_IDL_args(object):
    """
    Attributes:
     - classHandle
     - filterHandle
     - sense
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'classHandle',
      None,
      None),
     (2,
      TType.I32,
      'filterHandle',
      None,
      None),
     (3,
      TType.I32,
      'sense',
      None,
      None))

    def __init__(self, classHandle = None, filterHandle = None, sense = None):
        self.classHandle = classHandle
        self.filterHandle = filterHandle
        self.sense = sense



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
                    self.classHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.filterHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.sense = iprot.readI32()
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
        oprot.writeStructBegin('setFilterSense_IDL_args')
        if self.classHandle != None:
            oprot.writeFieldBegin('classHandle', TType.I32, 1)
            oprot.writeI32(self.classHandle)
            oprot.writeFieldEnd()
        if self.filterHandle != None:
            oprot.writeFieldBegin('filterHandle', TType.I32, 2)
            oprot.writeI32(self.filterHandle)
            oprot.writeFieldEnd()
        if self.sense != None:
            oprot.writeFieldBegin('sense', TType.I32, 3)
            oprot.writeI32(self.sense)
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




class setFilterSense_IDL_result(object):
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
        oprot.writeStructBegin('setFilterSense_IDL_result')
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




class addFilterAclToClass_IDL_args(object):
    """
    Attributes:
     - classHandle
     - sense
     - aclHandle
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'classHandle',
      None,
      None),
     (2,
      TType.I32,
      'sense',
      None,
      None),
     (3,
      TType.I32,
      'aclHandle',
      None,
      None))

    def __init__(self, classHandle = None, sense = None, aclHandle = None):
        self.classHandle = classHandle
        self.sense = sense
        self.aclHandle = aclHandle



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
                    self.classHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.sense = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.aclHandle = iprot.readI32()
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
        oprot.writeStructBegin('addFilterAclToClass_IDL_args')
        if self.classHandle != None:
            oprot.writeFieldBegin('classHandle', TType.I32, 1)
            oprot.writeI32(self.classHandle)
            oprot.writeFieldEnd()
        if self.sense != None:
            oprot.writeFieldBegin('sense', TType.I32, 2)
            oprot.writeI32(self.sense)
            oprot.writeFieldEnd()
        if self.aclHandle != None:
            oprot.writeFieldBegin('aclHandle', TType.I32, 3)
            oprot.writeI32(self.aclHandle)
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




class addFilterAclToClass_IDL_result(object):
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
        oprot.writeStructBegin('addFilterAclToClass_IDL_result')
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




class addFilterDscpToClass_IDL_args(object):
    """
    Attributes:
     - classHandle
     - sense
     - dscp
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'classHandle',
      None,
      None),
     (2,
      TType.I32,
      'sense',
      None,
      None),
     (3,
      TType.LIST,
      'dscp',
      (TType.BYTE, None),
      None))

    def __init__(self, classHandle = None, sense = None, dscp = None):
        self.classHandle = classHandle
        self.sense = sense
        self.dscp = dscp



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
                    self.classHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.sense = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.LIST:
                    self.dscp = []
                    (_etype38, _size35,) = iprot.readListBegin()
                    for _i39 in xrange(_size35):
                        _elem40 = iprot.readByte()
                        self.dscp.append(_elem40)

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
        oprot.writeStructBegin('addFilterDscpToClass_IDL_args')
        if self.classHandle != None:
            oprot.writeFieldBegin('classHandle', TType.I32, 1)
            oprot.writeI32(self.classHandle)
            oprot.writeFieldEnd()
        if self.sense != None:
            oprot.writeFieldBegin('sense', TType.I32, 2)
            oprot.writeI32(self.sense)
            oprot.writeFieldEnd()
        if self.dscp != None:
            oprot.writeFieldBegin('dscp', TType.LIST, 3)
            oprot.writeListBegin(TType.BYTE, len(self.dscp))
            for iter41 in self.dscp:
                oprot.writeByte(iter41)

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




class addFilterDscpToClass_IDL_result(object):
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
        oprot.writeStructBegin('addFilterDscpToClass_IDL_result')
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




class addFilterMplsToClass_IDL_args(object):
    """
    Attributes:
     - classHandle
     - sense
     - mplsExp
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'classHandle',
      None,
      None),
     (2,
      TType.I32,
      'sense',
      None,
      None),
     (3,
      TType.LIST,
      'mplsExp',
      (TType.I32, None),
      None))

    def __init__(self, classHandle = None, sense = None, mplsExp = None):
        self.classHandle = classHandle
        self.sense = sense
        self.mplsExp = mplsExp



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
                    self.classHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.sense = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.LIST:
                    self.mplsExp = []
                    (_etype45, _size42,) = iprot.readListBegin()
                    for _i46 in xrange(_size42):
                        _elem47 = iprot.readI32()
                        self.mplsExp.append(_elem47)

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
        oprot.writeStructBegin('addFilterMplsToClass_IDL_args')
        if self.classHandle != None:
            oprot.writeFieldBegin('classHandle', TType.I32, 1)
            oprot.writeI32(self.classHandle)
            oprot.writeFieldEnd()
        if self.sense != None:
            oprot.writeFieldBegin('sense', TType.I32, 2)
            oprot.writeI32(self.sense)
            oprot.writeFieldEnd()
        if self.mplsExp != None:
            oprot.writeFieldBegin('mplsExp', TType.LIST, 3)
            oprot.writeListBegin(TType.I32, len(self.mplsExp))
            for iter48 in self.mplsExp:
                oprot.writeI32(iter48)

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




class addFilterMplsToClass_IDL_result(object):
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
        oprot.writeStructBegin('addFilterMplsToClass_IDL_result')
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




class addFilterDlciToClass_IDL_args(object):
    """
    Attributes:
     - classHandle
     - sense
     - dlci
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'classHandle',
      None,
      None),
     (2,
      TType.I32,
      'sense',
      None,
      None),
     (3,
      TType.I16,
      'dlci',
      None,
      None))

    def __init__(self, classHandle = None, sense = None, dlci = None):
        self.classHandle = classHandle
        self.sense = sense
        self.dlci = dlci



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
                    self.classHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.sense = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I16:
                    self.dlci = iprot.readI16()
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
        oprot.writeStructBegin('addFilterDlciToClass_IDL_args')
        if self.classHandle != None:
            oprot.writeFieldBegin('classHandle', TType.I32, 1)
            oprot.writeI32(self.classHandle)
            oprot.writeFieldEnd()
        if self.sense != None:
            oprot.writeFieldBegin('sense', TType.I32, 2)
            oprot.writeI32(self.sense)
            oprot.writeFieldEnd()
        if self.dlci != None:
            oprot.writeFieldBegin('dlci', TType.I16, 3)
            oprot.writeI16(self.dlci)
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




class addFilterDlciToClass_IDL_result(object):
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
        oprot.writeStructBegin('addFilterDlciToClass_IDL_result')
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




class addFilterDeToClass_IDL_args(object):
    """
    Attributes:
     - classHandle
     - sense
    """

    thrift_spec = (None, (1,
      TType.I32,
      'classHandle',
      None,
      None), (2,
      TType.I32,
      'sense',
      None,
      None))

    def __init__(self, classHandle = None, sense = None):
        self.classHandle = classHandle
        self.sense = sense



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
                    self.classHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.sense = iprot.readI32()
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
        oprot.writeStructBegin('addFilterDeToClass_IDL_args')
        if self.classHandle != None:
            oprot.writeFieldBegin('classHandle', TType.I32, 1)
            oprot.writeI32(self.classHandle)
            oprot.writeFieldEnd()
        if self.sense != None:
            oprot.writeFieldBegin('sense', TType.I32, 2)
            oprot.writeI32(self.sense)
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




class addFilterDeToClass_IDL_result(object):
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
        oprot.writeStructBegin('addFilterDeToClass_IDL_result')
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




class addFilterL2CosToClass_IDL_args(object):
    """
    Attributes:
     - classHandle
     - sense
     - l2cos
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'classHandle',
      None,
      None),
     (2,
      TType.I32,
      'sense',
      None,
      None),
     (3,
      TType.LIST,
      'l2cos',
      (TType.BYTE, None),
      None))

    def __init__(self, classHandle = None, sense = None, l2cos = None):
        self.classHandle = classHandle
        self.sense = sense
        self.l2cos = l2cos



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
                    self.classHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.sense = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.LIST:
                    self.l2cos = []
                    (_etype52, _size49,) = iprot.readListBegin()
                    for _i53 in xrange(_size49):
                        _elem54 = iprot.readByte()
                        self.l2cos.append(_elem54)

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
        oprot.writeStructBegin('addFilterL2CosToClass_IDL_args')
        if self.classHandle != None:
            oprot.writeFieldBegin('classHandle', TType.I32, 1)
            oprot.writeI32(self.classHandle)
            oprot.writeFieldEnd()
        if self.sense != None:
            oprot.writeFieldBegin('sense', TType.I32, 2)
            oprot.writeI32(self.sense)
            oprot.writeFieldEnd()
        if self.l2cos != None:
            oprot.writeFieldBegin('l2cos', TType.LIST, 3)
            oprot.writeListBegin(TType.BYTE, len(self.l2cos))
            for iter55 in self.l2cos:
                oprot.writeByte(iter55)

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




class addFilterL2CosToClass_IDL_result(object):
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
        oprot.writeStructBegin('addFilterL2CosToClass_IDL_result')
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




class addFilterMacAddressToClass_IDL_args(object):
    """
    Attributes:
     - classHandle
     - sense
     - macAddress
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'classHandle',
      None,
      None),
     (2,
      TType.I32,
      'sense',
      None,
      None),
     (3,
      TType.STRUCT,
      'macAddress',
      (MacAddress_IDL, MacAddress_IDL.thrift_spec),
      None))

    def __init__(self, classHandle = None, sense = None, macAddress = None):
        self.classHandle = classHandle
        self.sense = sense
        self.macAddress = macAddress



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
                    self.classHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.sense = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRUCT:
                    self.macAddress = MacAddress_IDL()
                    self.macAddress.read(iprot)
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
        oprot.writeStructBegin('addFilterMacAddressToClass_IDL_args')
        if self.classHandle != None:
            oprot.writeFieldBegin('classHandle', TType.I32, 1)
            oprot.writeI32(self.classHandle)
            oprot.writeFieldEnd()
        if self.sense != None:
            oprot.writeFieldBegin('sense', TType.I32, 2)
            oprot.writeI32(self.sense)
            oprot.writeFieldEnd()
        if self.macAddress != None:
            oprot.writeFieldBegin('macAddress', TType.STRUCT, 3)
            self.macAddress.write(oprot)
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




class addFilterMacAddressToClass_IDL_result(object):
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
        oprot.writeStructBegin('addFilterMacAddressToClass_IDL_result')
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




class addFilterPktLenToClass_IDL_args(object):
    """
    Attributes:
     - classHandle
     - sense
     - min
     - max
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'classHandle',
      None,
      None),
     (2,
      TType.I32,
      'sense',
      None,
      None),
     (3,
      TType.I32,
      'min',
      None,
      None),
     (4,
      TType.I32,
      'max',
      None,
      None))

    def __init__(self, classHandle = None, sense = None, min = None, max = None):
        self.classHandle = classHandle
        self.sense = sense
        self.min = min
        self.max = max



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
                    self.classHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.sense = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.min = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.max = iprot.readI32()
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
        oprot.writeStructBegin('addFilterPktLenToClass_IDL_args')
        if self.classHandle != None:
            oprot.writeFieldBegin('classHandle', TType.I32, 1)
            oprot.writeI32(self.classHandle)
            oprot.writeFieldEnd()
        if self.sense != None:
            oprot.writeFieldBegin('sense', TType.I32, 2)
            oprot.writeI32(self.sense)
            oprot.writeFieldEnd()
        if self.min != None:
            oprot.writeFieldBegin('min', TType.I32, 3)
            oprot.writeI32(self.min)
            oprot.writeFieldEnd()
        if self.max != None:
            oprot.writeFieldBegin('max', TType.I32, 4)
            oprot.writeI32(self.max)
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




class addFilterPktLenToClass_IDL_result(object):
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
        oprot.writeStructBegin('addFilterPktLenToClass_IDL_result')
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




class addFilterProtocolToClass_IDL_args(object):
    """
    Attributes:
     - classHandle
     - sense
     - protocol
     - subProtocol
     - param
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'classHandle',
      None,
      None),
     (2,
      TType.I32,
      'sense',
      None,
      None),
     (3,
      TType.STRING,
      'protocol',
      None,
      None),
     (4,
      TType.STRING,
      'subProtocol',
      None,
      None),
     (5,
      TType.STRING,
      'param',
      None,
      None))

    def __init__(self, classHandle = None, sense = None, protocol = None, subProtocol = None, param = None):
        self.classHandle = classHandle
        self.sense = sense
        self.protocol = protocol
        self.subProtocol = subProtocol
        self.param = param



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
                    self.classHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.sense = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.protocol = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.subProtocol = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.param = iprot.readString()
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
        oprot.writeStructBegin('addFilterProtocolToClass_IDL_args')
        if self.classHandle != None:
            oprot.writeFieldBegin('classHandle', TType.I32, 1)
            oprot.writeI32(self.classHandle)
            oprot.writeFieldEnd()
        if self.sense != None:
            oprot.writeFieldBegin('sense', TType.I32, 2)
            oprot.writeI32(self.sense)
            oprot.writeFieldEnd()
        if self.protocol != None:
            oprot.writeFieldBegin('protocol', TType.STRING, 3)
            oprot.writeString(self.protocol)
            oprot.writeFieldEnd()
        if self.subProtocol != None:
            oprot.writeFieldBegin('subProtocol', TType.STRING, 4)
            oprot.writeString(self.subProtocol)
            oprot.writeFieldEnd()
        if self.param != None:
            oprot.writeFieldBegin('param', TType.STRING, 5)
            oprot.writeString(self.param)
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




class addFilterProtocolToClass_IDL_result(object):
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
        oprot.writeStructBegin('addFilterProtocolToClass_IDL_result')
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




class addFilterQosGroupToClass_IDL_args(object):
    """
    Attributes:
     - classHandle
     - sense
     - group
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'classHandle',
      None,
      None),
     (2,
      TType.I32,
      'sense',
      None,
      None),
     (3,
      TType.BYTE,
      'group',
      None,
      None))

    def __init__(self, classHandle = None, sense = None, group = None):
        self.classHandle = classHandle
        self.sense = sense
        self.group = group



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
                    self.classHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.sense = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.BYTE:
                    self.group = iprot.readByte()
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
        oprot.writeStructBegin('addFilterQosGroupToClass_IDL_args')
        if self.classHandle != None:
            oprot.writeFieldBegin('classHandle', TType.I32, 1)
            oprot.writeI32(self.classHandle)
            oprot.writeFieldEnd()
        if self.sense != None:
            oprot.writeFieldBegin('sense', TType.I32, 2)
            oprot.writeI32(self.sense)
            oprot.writeFieldEnd()
        if self.group != None:
            oprot.writeFieldBegin('group', TType.BYTE, 3)
            oprot.writeByte(self.group)
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




class addFilterQosGroupToClass_IDL_result(object):
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
        oprot.writeStructBegin('addFilterQosGroupToClass_IDL_result')
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




class addFilterRtpPortToClass_IDL_args(object):
    """
    Attributes:
     - classHandle
     - sense
     - rtpPort
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'classHandle',
      None,
      None),
     (2,
      TType.I32,
      'sense',
      None,
      None),
     (3,
      TType.STRUCT,
      'rtpPort',
      (RtpPort_IDL, RtpPort_IDL.thrift_spec),
      None))

    def __init__(self, classHandle = None, sense = None, rtpPort = None):
        self.classHandle = classHandle
        self.sense = sense
        self.rtpPort = rtpPort



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
                    self.classHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.sense = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRUCT:
                    self.rtpPort = RtpPort_IDL()
                    self.rtpPort.read(iprot)
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
        oprot.writeStructBegin('addFilterRtpPortToClass_IDL_args')
        if self.classHandle != None:
            oprot.writeFieldBegin('classHandle', TType.I32, 1)
            oprot.writeI32(self.classHandle)
            oprot.writeFieldEnd()
        if self.sense != None:
            oprot.writeFieldBegin('sense', TType.I32, 2)
            oprot.writeI32(self.sense)
            oprot.writeFieldEnd()
        if self.rtpPort != None:
            oprot.writeFieldBegin('rtpPort', TType.STRUCT, 3)
            self.rtpPort.write(oprot)
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




class addFilterRtpPortToClass_IDL_result(object):
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
        oprot.writeStructBegin('addFilterRtpPortToClass_IDL_result')
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




class addFilterVlanToClass_IDL_args(object):
    """
    Attributes:
     - classHandle
     - sense
     - vlan
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'classHandle',
      None,
      None),
     (2,
      TType.I32,
      'sense',
      None,
      None),
     (3,
      TType.LIST,
      'vlan',
      (TType.I16, None),
      None))

    def __init__(self, classHandle = None, sense = None, vlan = None):
        self.classHandle = classHandle
        self.sense = sense
        self.vlan = vlan



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
                    self.classHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.sense = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.LIST:
                    self.vlan = []
                    (_etype59, _size56,) = iprot.readListBegin()
                    for _i60 in xrange(_size56):
                        _elem61 = iprot.readI16()
                        self.vlan.append(_elem61)

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
        oprot.writeStructBegin('addFilterVlanToClass_IDL_args')
        if self.classHandle != None:
            oprot.writeFieldBegin('classHandle', TType.I32, 1)
            oprot.writeI32(self.classHandle)
            oprot.writeFieldEnd()
        if self.sense != None:
            oprot.writeFieldBegin('sense', TType.I32, 2)
            oprot.writeI32(self.sense)
            oprot.writeFieldEnd()
        if self.vlan != None:
            oprot.writeFieldBegin('vlan', TType.LIST, 3)
            oprot.writeListBegin(TType.I16, len(self.vlan))
            for iter62 in self.vlan:
                oprot.writeI16(iter62)

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




class addFilterVlanToClass_IDL_result(object):
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
        oprot.writeStructBegin('addFilterVlanToClass_IDL_result')
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




class removeActionFromClass_IDL_args(object):
    """
    Attributes:
     - policyHandle
     - classHandle
     - actionHandle
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'policyHandle',
      None,
      None),
     (2,
      TType.I32,
      'classHandle',
      None,
      None),
     (3,
      TType.I32,
      'actionHandle',
      None,
      None))

    def __init__(self, policyHandle = None, classHandle = None, actionHandle = None):
        self.policyHandle = policyHandle
        self.classHandle = classHandle
        self.actionHandle = actionHandle



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
                    self.policyHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.classHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.actionHandle = iprot.readI32()
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
        oprot.writeStructBegin('removeActionFromClass_IDL_args')
        if self.policyHandle != None:
            oprot.writeFieldBegin('policyHandle', TType.I32, 1)
            oprot.writeI32(self.policyHandle)
            oprot.writeFieldEnd()
        if self.classHandle != None:
            oprot.writeFieldBegin('classHandle', TType.I32, 2)
            oprot.writeI32(self.classHandle)
            oprot.writeFieldEnd()
        if self.actionHandle != None:
            oprot.writeFieldBegin('actionHandle', TType.I32, 3)
            oprot.writeI32(self.actionHandle)
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




class removeActionFromClass_IDL_result(object):
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
        oprot.writeStructBegin('removeActionFromClass_IDL_result')
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




class addActionDropToClass_IDL_args(object):
    """
    Attributes:
     - policyHandle
     - classHandle
     - remoteSn
     - appId
     - localId
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'policyHandle',
      None,
      None),
     (2,
      TType.I32,
      'classHandle',
      None,
      None),
     (3,
      TType.I32,
      'remoteSn',
      None,
      None),
     (4,
      TType.I32,
      'appId',
      None,
      None),
     (5,
      TType.I32,
      'localId',
      None,
      None))

    def __init__(self, policyHandle = None, classHandle = None, remoteSn = None, appId = None, localId = None):
        self.policyHandle = policyHandle
        self.classHandle = classHandle
        self.remoteSn = remoteSn
        self.appId = appId
        self.localId = localId



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
                    self.policyHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.classHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.remoteSn = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.appId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.localId = iprot.readI32()
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
        oprot.writeStructBegin('addActionDropToClass_IDL_args')
        if self.policyHandle != None:
            oprot.writeFieldBegin('policyHandle', TType.I32, 1)
            oprot.writeI32(self.policyHandle)
            oprot.writeFieldEnd()
        if self.classHandle != None:
            oprot.writeFieldBegin('classHandle', TType.I32, 2)
            oprot.writeI32(self.classHandle)
            oprot.writeFieldEnd()
        if self.remoteSn != None:
            oprot.writeFieldBegin('remoteSn', TType.I32, 3)
            oprot.writeI32(self.remoteSn)
            oprot.writeFieldEnd()
        if self.appId != None:
            oprot.writeFieldBegin('appId', TType.I32, 4)
            oprot.writeI32(self.appId)
            oprot.writeFieldEnd()
        if self.localId != None:
            oprot.writeFieldBegin('localId', TType.I32, 5)
            oprot.writeI32(self.localId)
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




class addActionDropToClass_IDL_result(object):
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
        oprot.writeStructBegin('addActionDropToClass_IDL_result')
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




class addActionIfcToClass_IDL_args(object):
    """
    Attributes:
     - policyHandle
     - classHandle
     - ifHandle
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'policyHandle',
      None,
      None),
     (2,
      TType.I32,
      'classHandle',
      None,
      None),
     (3,
      TType.I64,
      'ifHandle',
      None,
      None))

    def __init__(self, policyHandle = None, classHandle = None, ifHandle = None):
        self.policyHandle = policyHandle
        self.classHandle = classHandle
        self.ifHandle = ifHandle



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
                    self.policyHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.classHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I64:
                    self.ifHandle = iprot.readI64()
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
        oprot.writeStructBegin('addActionIfcToClass_IDL_args')
        if self.policyHandle != None:
            oprot.writeFieldBegin('policyHandle', TType.I32, 1)
            oprot.writeI32(self.policyHandle)
            oprot.writeFieldEnd()
        if self.classHandle != None:
            oprot.writeFieldBegin('classHandle', TType.I32, 2)
            oprot.writeI32(self.classHandle)
            oprot.writeFieldEnd()
        if self.ifHandle != None:
            oprot.writeFieldBegin('ifHandle', TType.I64, 3)
            oprot.writeI64(self.ifHandle)
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




class addActionIfcToClass_IDL_result(object):
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
        oprot.writeStructBegin('addActionIfcToClass_IDL_result')
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




class addActionNextHopToClass_IDL_args(object):
    """
    Attributes:
     - policyHandle
     - classHandle
     - addrAF
     - nextHopAddress
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'policyHandle',
      None,
      None),
     (2,
      TType.I32,
      'classHandle',
      None,
      None),
     (3,
      TType.I32,
      'addrAF',
      None,
      None),
     (4,
      TType.STRING,
      'nextHopAddress',
      None,
      None))

    def __init__(self, policyHandle = None, classHandle = None, addrAF = None, nextHopAddress = None):
        self.policyHandle = policyHandle
        self.classHandle = classHandle
        self.addrAF = addrAF
        self.nextHopAddress = nextHopAddress



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
                    self.policyHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.classHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.addrAF = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.nextHopAddress = iprot.readString()
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
        oprot.writeStructBegin('addActionNextHopToClass_IDL_args')
        if self.policyHandle != None:
            oprot.writeFieldBegin('policyHandle', TType.I32, 1)
            oprot.writeI32(self.policyHandle)
            oprot.writeFieldEnd()
        if self.classHandle != None:
            oprot.writeFieldBegin('classHandle', TType.I32, 2)
            oprot.writeI32(self.classHandle)
            oprot.writeFieldEnd()
        if self.addrAF != None:
            oprot.writeFieldBegin('addrAF', TType.I32, 3)
            oprot.writeI32(self.addrAF)
            oprot.writeFieldEnd()
        if self.nextHopAddress != None:
            oprot.writeFieldBegin('nextHopAddress', TType.STRING, 4)
            oprot.writeString(self.nextHopAddress)
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




class addActionNextHopToClass_IDL_result(object):
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
        oprot.writeStructBegin('addActionNextHopToClass_IDL_result')
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




class addActionMarkToClass_IDL_args(object):
    """
    Attributes:
     - policyHandle
     - classHandle
     - markParam
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'policyHandle',
      None,
      None),
     (2,
      TType.I32,
      'classHandle',
      None,
      None),
     (3,
      TType.STRUCT,
      'markParam',
      (MarkParam_IDL, MarkParam_IDL.thrift_spec),
      None))

    def __init__(self, policyHandle = None, classHandle = None, markParam = None):
        self.policyHandle = policyHandle
        self.classHandle = classHandle
        self.markParam = markParam



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
                    self.policyHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.classHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRUCT:
                    self.markParam = MarkParam_IDL()
                    self.markParam.read(iprot)
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
        oprot.writeStructBegin('addActionMarkToClass_IDL_args')
        if self.policyHandle != None:
            oprot.writeFieldBegin('policyHandle', TType.I32, 1)
            oprot.writeI32(self.policyHandle)
            oprot.writeFieldEnd()
        if self.classHandle != None:
            oprot.writeFieldBegin('classHandle', TType.I32, 2)
            oprot.writeI32(self.classHandle)
            oprot.writeFieldEnd()
        if self.markParam != None:
            oprot.writeFieldBegin('markParam', TType.STRUCT, 3)
            self.markParam.write(oprot)
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




class addActionMarkToClass_IDL_result(object):
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
        oprot.writeStructBegin('addActionMarkToClass_IDL_result')
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




class addActionPoliceToClass_IDL_args(object):
    """
    Attributes:
     - policyHandle
     - classHandle
     - policeParam
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'policyHandle',
      None,
      None),
     (2,
      TType.I32,
      'classHandle',
      None,
      None),
     (3,
      TType.STRUCT,
      'policeParam',
      (PoliceParam_IDL, PoliceParam_IDL.thrift_spec),
      None))

    def __init__(self, policyHandle = None, classHandle = None, policeParam = None):
        self.policyHandle = policyHandle
        self.classHandle = classHandle
        self.policeParam = policeParam



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
                    self.policyHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.classHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRUCT:
                    self.policeParam = PoliceParam_IDL()
                    self.policeParam.read(iprot)
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
        oprot.writeStructBegin('addActionPoliceToClass_IDL_args')
        if self.policyHandle != None:
            oprot.writeFieldBegin('policyHandle', TType.I32, 1)
            oprot.writeI32(self.policyHandle)
            oprot.writeFieldEnd()
        if self.classHandle != None:
            oprot.writeFieldBegin('classHandle', TType.I32, 2)
            oprot.writeI32(self.classHandle)
            oprot.writeFieldEnd()
        if self.policeParam != None:
            oprot.writeFieldBegin('policeParam', TType.STRUCT, 3)
            self.policeParam.write(oprot)
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




class addActionPoliceToClass_IDL_result(object):
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
        oprot.writeStructBegin('addActionPoliceToClass_IDL_result')
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




class addActionShapeToClass_IDL_args(object):
    """
    Attributes:
     - policyHandle
     - classHandle
     - shapeParam
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'policyHandle',
      None,
      None),
     (2,
      TType.I32,
      'classHandle',
      None,
      None),
     (3,
      TType.STRUCT,
      'shapeParam',
      (ShapeParam_IDL, ShapeParam_IDL.thrift_spec),
      None))

    def __init__(self, policyHandle = None, classHandle = None, shapeParam = None):
        self.policyHandle = policyHandle
        self.classHandle = classHandle
        self.shapeParam = shapeParam



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
                    self.policyHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.classHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRUCT:
                    self.shapeParam = ShapeParam_IDL()
                    self.shapeParam.read(iprot)
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
        oprot.writeStructBegin('addActionShapeToClass_IDL_args')
        if self.policyHandle != None:
            oprot.writeFieldBegin('policyHandle', TType.I32, 1)
            oprot.writeI32(self.policyHandle)
            oprot.writeFieldEnd()
        if self.classHandle != None:
            oprot.writeFieldBegin('classHandle', TType.I32, 2)
            oprot.writeI32(self.classHandle)
            oprot.writeFieldEnd()
        if self.shapeParam != None:
            oprot.writeFieldBegin('shapeParam', TType.STRUCT, 3)
            self.shapeParam.write(oprot)
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




class addActionShapeToClass_IDL_result(object):
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
        oprot.writeStructBegin('addActionShapeToClass_IDL_result')
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




class addActionPriorityQueueToClass_IDL_args(object):
    """
    Attributes:
     - policyHandle
     - classHandle
     - queueParam
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'policyHandle',
      None,
      None),
     (2,
      TType.I32,
      'classHandle',
      None,
      None),
     (3,
      TType.STRUCT,
      'queueParam',
      (PriorityQueueParam_IDL, PriorityQueueParam_IDL.thrift_spec),
      None))

    def __init__(self, policyHandle = None, classHandle = None, queueParam = None):
        self.policyHandle = policyHandle
        self.classHandle = classHandle
        self.queueParam = queueParam



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
                    self.policyHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.classHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRUCT:
                    self.queueParam = PriorityQueueParam_IDL()
                    self.queueParam.read(iprot)
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
        oprot.writeStructBegin('addActionPriorityQueueToClass_IDL_args')
        if self.policyHandle != None:
            oprot.writeFieldBegin('policyHandle', TType.I32, 1)
            oprot.writeI32(self.policyHandle)
            oprot.writeFieldEnd()
        if self.classHandle != None:
            oprot.writeFieldBegin('classHandle', TType.I32, 2)
            oprot.writeI32(self.classHandle)
            oprot.writeFieldEnd()
        if self.queueParam != None:
            oprot.writeFieldBegin('queueParam', TType.STRUCT, 3)
            self.queueParam.write(oprot)
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




class addActionPriorityQueueToClass_IDL_result(object):
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
        oprot.writeStructBegin('addActionPriorityQueueToClass_IDL_result')
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




class addActionClassBasedQueueToClass_IDL_args(object):
    """
    Attributes:
     - policyHandle
     - classHandle
     - queueParam
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'policyHandle',
      None,
      None),
     (2,
      TType.I32,
      'classHandle',
      None,
      None),
     (3,
      TType.STRUCT,
      'queueParam',
      (ClassBasedQueueParam_IDL, ClassBasedQueueParam_IDL.thrift_spec),
      None))

    def __init__(self, policyHandle = None, classHandle = None, queueParam = None):
        self.policyHandle = policyHandle
        self.classHandle = classHandle
        self.queueParam = queueParam



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
                    self.policyHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.classHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRUCT:
                    self.queueParam = ClassBasedQueueParam_IDL()
                    self.queueParam.read(iprot)
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
        oprot.writeStructBegin('addActionClassBasedQueueToClass_IDL_args')
        if self.policyHandle != None:
            oprot.writeFieldBegin('policyHandle', TType.I32, 1)
            oprot.writeI32(self.policyHandle)
            oprot.writeFieldEnd()
        if self.classHandle != None:
            oprot.writeFieldBegin('classHandle', TType.I32, 2)
            oprot.writeI32(self.classHandle)
            oprot.writeFieldEnd()
        if self.queueParam != None:
            oprot.writeFieldBegin('queueParam', TType.STRUCT, 3)
            self.queueParam.write(oprot)
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




class addActionClassBasedQueueToClass_IDL_result(object):
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
        oprot.writeStructBegin('addActionClassBasedQueueToClass_IDL_result')
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




class addActionFairQueueToClass_IDL_args(object):
    """
    Attributes:
     - policyHandle
     - classHandle
     - queueParam
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'policyHandle',
      None,
      None),
     (2,
      TType.I32,
      'classHandle',
      None,
      None),
     (3,
      TType.STRUCT,
      'queueParam',
      (FairQueueParam_IDL, FairQueueParam_IDL.thrift_spec),
      None))

    def __init__(self, policyHandle = None, classHandle = None, queueParam = None):
        self.policyHandle = policyHandle
        self.classHandle = classHandle
        self.queueParam = queueParam



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
                    self.policyHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.classHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRUCT:
                    self.queueParam = FairQueueParam_IDL()
                    self.queueParam.read(iprot)
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
        oprot.writeStructBegin('addActionFairQueueToClass_IDL_args')
        if self.policyHandle != None:
            oprot.writeFieldBegin('policyHandle', TType.I32, 1)
            oprot.writeI32(self.policyHandle)
            oprot.writeFieldEnd()
        if self.classHandle != None:
            oprot.writeFieldBegin('classHandle', TType.I32, 2)
            oprot.writeI32(self.classHandle)
            oprot.writeFieldEnd()
        if self.queueParam != None:
            oprot.writeFieldBegin('queueParam', TType.STRUCT, 3)
            self.queueParam.write(oprot)
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




class addActionFairQueueToClass_IDL_result(object):
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
        oprot.writeStructBegin('addActionFairQueueToClass_IDL_result')
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




class addActionQueueLimitToClass_IDL_args(object):
    """
    Attributes:
     - policyHandle
     - classHandle
     - queueParam
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'policyHandle',
      None,
      None),
     (2,
      TType.I32,
      'classHandle',
      None,
      None),
     (3,
      TType.STRUCT,
      'queueParam',
      (QueueLimitParam_IDL, QueueLimitParam_IDL.thrift_spec),
      None))

    def __init__(self, policyHandle = None, classHandle = None, queueParam = None):
        self.policyHandle = policyHandle
        self.classHandle = classHandle
        self.queueParam = queueParam



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
                    self.policyHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.classHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRUCT:
                    self.queueParam = QueueLimitParam_IDL()
                    self.queueParam.read(iprot)
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
        oprot.writeStructBegin('addActionQueueLimitToClass_IDL_args')
        if self.policyHandle != None:
            oprot.writeFieldBegin('policyHandle', TType.I32, 1)
            oprot.writeI32(self.policyHandle)
            oprot.writeFieldEnd()
        if self.classHandle != None:
            oprot.writeFieldBegin('classHandle', TType.I32, 2)
            oprot.writeI32(self.classHandle)
            oprot.writeFieldEnd()
        if self.queueParam != None:
            oprot.writeFieldBegin('queueParam', TType.STRUCT, 3)
            self.queueParam.write(oprot)
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




class addActionQueueLimitToClass_IDL_result(object):
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
        oprot.writeStructBegin('addActionQueueLimitToClass_IDL_result')
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




class addActionWredToClass_IDL_args(object):
    """
    Attributes:
     - policyHandle
     - classHandle
     - type
     - ecnEnabled
     - exponWeight
     - thresholdUnits
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'policyHandle',
      None,
      None),
     (2,
      TType.I32,
      'classHandle',
      None,
      None),
     (3,
      TType.I32,
      'type',
      None,
      None),
     (4,
      TType.I32,
      'ecnEnabled',
      None,
      None),
     (5,
      TType.I32,
      'exponWeight',
      None,
      None),
     (6,
      TType.I32,
      'thresholdUnits',
      None,
      None))

    def __init__(self, policyHandle = None, classHandle = None, type = None, ecnEnabled = None, exponWeight = None, thresholdUnits = None):
        self.policyHandle = policyHandle
        self.classHandle = classHandle
        self.type = type
        self.ecnEnabled = ecnEnabled
        self.exponWeight = exponWeight
        self.thresholdUnits = thresholdUnits



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
                    self.policyHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.classHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.ecnEnabled = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.exponWeight = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I32:
                    self.thresholdUnits = iprot.readI32()
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
        oprot.writeStructBegin('addActionWredToClass_IDL_args')
        if self.policyHandle != None:
            oprot.writeFieldBegin('policyHandle', TType.I32, 1)
            oprot.writeI32(self.policyHandle)
            oprot.writeFieldEnd()
        if self.classHandle != None:
            oprot.writeFieldBegin('classHandle', TType.I32, 2)
            oprot.writeI32(self.classHandle)
            oprot.writeFieldEnd()
        if self.type != None:
            oprot.writeFieldBegin('type', TType.I32, 3)
            oprot.writeI32(self.type)
            oprot.writeFieldEnd()
        if self.ecnEnabled != None:
            oprot.writeFieldBegin('ecnEnabled', TType.I32, 4)
            oprot.writeI32(self.ecnEnabled)
            oprot.writeFieldEnd()
        if self.exponWeight != None:
            oprot.writeFieldBegin('exponWeight', TType.I32, 5)
            oprot.writeI32(self.exponWeight)
            oprot.writeFieldEnd()
        if self.thresholdUnits != None:
            oprot.writeFieldBegin('thresholdUnits', TType.I32, 6)
            oprot.writeI32(self.thresholdUnits)
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




class addActionWredToClass_IDL_result(object):
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
        oprot.writeStructBegin('addActionWredToClass_IDL_result')
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




class addWredProfileToClass_IDL_args(object):
    """
    Attributes:
     - policyHandle
     - classHandle
     - type
     - value
     - minThreshold
     - maxThreshold
     - thresholdUnits
     - dropProb
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'policyHandle',
      None,
      None),
     (2,
      TType.I32,
      'classHandle',
      None,
      None),
     (3,
      TType.I32,
      'type',
      None,
      None),
     (4,
      TType.I32,
      'value',
      None,
      None),
     (5,
      TType.I32,
      'minThreshold',
      None,
      None),
     (6,
      TType.I32,
      'maxThreshold',
      None,
      None),
     (7,
      TType.I32,
      'thresholdUnits',
      None,
      None),
     (8,
      TType.I32,
      'dropProb',
      None,
      None))

    def __init__(self, policyHandle = None, classHandle = None, type = None, value = None, minThreshold = None, maxThreshold = None, thresholdUnits = None, dropProb = None):
        self.policyHandle = policyHandle
        self.classHandle = classHandle
        self.type = type
        self.value = value
        self.minThreshold = minThreshold
        self.maxThreshold = maxThreshold
        self.thresholdUnits = thresholdUnits
        self.dropProb = dropProb



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
                    self.policyHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.classHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.value = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.minThreshold = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I32:
                    self.maxThreshold = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I32:
                    self.thresholdUnits = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.I32:
                    self.dropProb = iprot.readI32()
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
        oprot.writeStructBegin('addWredProfileToClass_IDL_args')
        if self.policyHandle != None:
            oprot.writeFieldBegin('policyHandle', TType.I32, 1)
            oprot.writeI32(self.policyHandle)
            oprot.writeFieldEnd()
        if self.classHandle != None:
            oprot.writeFieldBegin('classHandle', TType.I32, 2)
            oprot.writeI32(self.classHandle)
            oprot.writeFieldEnd()
        if self.type != None:
            oprot.writeFieldBegin('type', TType.I32, 3)
            oprot.writeI32(self.type)
            oprot.writeFieldEnd()
        if self.value != None:
            oprot.writeFieldBegin('value', TType.I32, 4)
            oprot.writeI32(self.value)
            oprot.writeFieldEnd()
        if self.minThreshold != None:
            oprot.writeFieldBegin('minThreshold', TType.I32, 5)
            oprot.writeI32(self.minThreshold)
            oprot.writeFieldEnd()
        if self.maxThreshold != None:
            oprot.writeFieldBegin('maxThreshold', TType.I32, 6)
            oprot.writeI32(self.maxThreshold)
            oprot.writeFieldEnd()
        if self.thresholdUnits != None:
            oprot.writeFieldBegin('thresholdUnits', TType.I32, 7)
            oprot.writeI32(self.thresholdUnits)
            oprot.writeFieldEnd()
        if self.dropProb != None:
            oprot.writeFieldBegin('dropProb', TType.I32, 8)
            oprot.writeI32(self.dropProb)
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




class addWredProfileToClass_IDL_result(object):
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
        oprot.writeStructBegin('addWredProfileToClass_IDL_result')
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




class removeWredProfileFromClass_IDL_args(object):
    """
    Attributes:
     - policyHandle
     - classHandle
     - type
     - value
     - minThreshold
     - maxThreshold
     - thresholdUnits
     - dropProb
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'policyHandle',
      None,
      None),
     (2,
      TType.I32,
      'classHandle',
      None,
      None),
     (3,
      TType.I32,
      'type',
      None,
      None),
     (4,
      TType.I32,
      'value',
      None,
      None),
     (5,
      TType.I32,
      'minThreshold',
      None,
      None),
     (6,
      TType.I32,
      'maxThreshold',
      None,
      None),
     (7,
      TType.I32,
      'thresholdUnits',
      None,
      None),
     (8,
      TType.I32,
      'dropProb',
      None,
      None))

    def __init__(self, policyHandle = None, classHandle = None, type = None, value = None, minThreshold = None, maxThreshold = None, thresholdUnits = None, dropProb = None):
        self.policyHandle = policyHandle
        self.classHandle = classHandle
        self.type = type
        self.value = value
        self.minThreshold = minThreshold
        self.maxThreshold = maxThreshold
        self.thresholdUnits = thresholdUnits
        self.dropProb = dropProb



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
                    self.policyHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.classHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.value = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.minThreshold = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I32:
                    self.maxThreshold = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I32:
                    self.thresholdUnits = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.I32:
                    self.dropProb = iprot.readI32()
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
        oprot.writeStructBegin('removeWredProfileFromClass_IDL_args')
        if self.policyHandle != None:
            oprot.writeFieldBegin('policyHandle', TType.I32, 1)
            oprot.writeI32(self.policyHandle)
            oprot.writeFieldEnd()
        if self.classHandle != None:
            oprot.writeFieldBegin('classHandle', TType.I32, 2)
            oprot.writeI32(self.classHandle)
            oprot.writeFieldEnd()
        if self.type != None:
            oprot.writeFieldBegin('type', TType.I32, 3)
            oprot.writeI32(self.type)
            oprot.writeFieldEnd()
        if self.value != None:
            oprot.writeFieldBegin('value', TType.I32, 4)
            oprot.writeI32(self.value)
            oprot.writeFieldEnd()
        if self.minThreshold != None:
            oprot.writeFieldBegin('minThreshold', TType.I32, 5)
            oprot.writeI32(self.minThreshold)
            oprot.writeFieldEnd()
        if self.maxThreshold != None:
            oprot.writeFieldBegin('maxThreshold', TType.I32, 6)
            oprot.writeI32(self.maxThreshold)
            oprot.writeFieldEnd()
        if self.thresholdUnits != None:
            oprot.writeFieldBegin('thresholdUnits', TType.I32, 7)
            oprot.writeI32(self.thresholdUnits)
            oprot.writeFieldEnd()
        if self.dropProb != None:
            oprot.writeFieldBegin('dropProb', TType.I32, 8)
            oprot.writeI32(self.dropProb)
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




class removeWredProfileFromClass_IDL_result(object):
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
        oprot.writeStructBegin('removeWredProfileFromClass_IDL_result')
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




class addActionCopyToClass_IDL_args(object):
    """
    Attributes:
     - policyHandle
     - classHandle
     - remoteSn
     - appId
     - localId
     - size
     - sampleType
     - sampleRate
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'policyHandle',
      None,
      None),
     (2,
      TType.I32,
      'classHandle',
      None,
      None),
     (3,
      TType.I32,
      'remoteSn',
      None,
      None),
     (4,
      TType.I32,
      'appId',
      None,
      None),
     (5,
      TType.I32,
      'localId',
      None,
      None),
     (6,
      TType.I32,
      'size',
      None,
      None),
     (7,
      TType.I32,
      'sampleType',
      None,
      None),
     (8,
      TType.I32,
      'sampleRate',
      None,
      None))

    def __init__(self, policyHandle = None, classHandle = None, remoteSn = None, appId = None, localId = None, size = None, sampleType = None, sampleRate = None):
        self.policyHandle = policyHandle
        self.classHandle = classHandle
        self.remoteSn = remoteSn
        self.appId = appId
        self.localId = localId
        self.size = size
        self.sampleType = sampleType
        self.sampleRate = sampleRate



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
                    self.policyHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.classHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.remoteSn = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.appId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.localId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I32:
                    self.size = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I32:
                    self.sampleType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.I32:
                    self.sampleRate = iprot.readI32()
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
        oprot.writeStructBegin('addActionCopyToClass_IDL_args')
        if self.policyHandle != None:
            oprot.writeFieldBegin('policyHandle', TType.I32, 1)
            oprot.writeI32(self.policyHandle)
            oprot.writeFieldEnd()
        if self.classHandle != None:
            oprot.writeFieldBegin('classHandle', TType.I32, 2)
            oprot.writeI32(self.classHandle)
            oprot.writeFieldEnd()
        if self.remoteSn != None:
            oprot.writeFieldBegin('remoteSn', TType.I32, 3)
            oprot.writeI32(self.remoteSn)
            oprot.writeFieldEnd()
        if self.appId != None:
            oprot.writeFieldBegin('appId', TType.I32, 4)
            oprot.writeI32(self.appId)
            oprot.writeFieldEnd()
        if self.localId != None:
            oprot.writeFieldBegin('localId', TType.I32, 5)
            oprot.writeI32(self.localId)
            oprot.writeFieldEnd()
        if self.size != None:
            oprot.writeFieldBegin('size', TType.I32, 6)
            oprot.writeI32(self.size)
            oprot.writeFieldEnd()
        if self.sampleType != None:
            oprot.writeFieldBegin('sampleType', TType.I32, 7)
            oprot.writeI32(self.sampleType)
            oprot.writeFieldEnd()
        if self.sampleRate != None:
            oprot.writeFieldBegin('sampleRate', TType.I32, 8)
            oprot.writeI32(self.sampleRate)
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




class addActionCopyToClass_IDL_result(object):
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
        oprot.writeStructBegin('addActionCopyToClass_IDL_result')
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




class addActionDivertToClass_IDL_args(object):
    """
    Attributes:
     - policyHandle
     - classHandle
     - remoteSn
     - appId
     - localId
     - stateless
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'policyHandle',
      None,
      None),
     (2,
      TType.I32,
      'classHandle',
      None,
      None),
     (3,
      TType.I32,
      'remoteSn',
      None,
      None),
     (4,
      TType.I32,
      'appId',
      None,
      None),
     (5,
      TType.I32,
      'localId',
      None,
      None),
     (6,
      TType.I32,
      'stateless',
      None,
      None))

    def __init__(self, policyHandle = None, classHandle = None, remoteSn = None, appId = None, localId = None, stateless = None):
        self.policyHandle = policyHandle
        self.classHandle = classHandle
        self.remoteSn = remoteSn
        self.appId = appId
        self.localId = localId
        self.stateless = stateless



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
                    self.policyHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.classHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.remoteSn = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.appId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.localId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I32:
                    self.stateless = iprot.readI32()
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
        oprot.writeStructBegin('addActionDivertToClass_IDL_args')
        if self.policyHandle != None:
            oprot.writeFieldBegin('policyHandle', TType.I32, 1)
            oprot.writeI32(self.policyHandle)
            oprot.writeFieldEnd()
        if self.classHandle != None:
            oprot.writeFieldBegin('classHandle', TType.I32, 2)
            oprot.writeI32(self.classHandle)
            oprot.writeFieldEnd()
        if self.remoteSn != None:
            oprot.writeFieldBegin('remoteSn', TType.I32, 3)
            oprot.writeI32(self.remoteSn)
            oprot.writeFieldEnd()
        if self.appId != None:
            oprot.writeFieldBegin('appId', TType.I32, 4)
            oprot.writeI32(self.appId)
            oprot.writeFieldEnd()
        if self.localId != None:
            oprot.writeFieldBegin('localId', TType.I32, 5)
            oprot.writeI32(self.localId)
            oprot.writeFieldEnd()
        if self.stateless != None:
            oprot.writeFieldBegin('stateless', TType.I32, 6)
            oprot.writeI32(self.stateless)
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




class addActionDivertToClass_IDL_result(object):
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
        oprot.writeStructBegin('addActionDivertToClass_IDL_result')
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




class addActionCopyToAce_IDL_args(object):
    """
    Attributes:
     - aclHandle
     - aceHandle
     - remoteSn
     - appId
     - localId
     - size
     - sampleType
     - sampleRate
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'aclHandle',
      None,
      None),
     (2,
      TType.I32,
      'aceHandle',
      None,
      None),
     (3,
      TType.I32,
      'remoteSn',
      None,
      None),
     (4,
      TType.I32,
      'appId',
      None,
      None),
     (5,
      TType.I32,
      'localId',
      None,
      None),
     (6,
      TType.I32,
      'size',
      None,
      None),
     (7,
      TType.I32,
      'sampleType',
      None,
      None),
     (8,
      TType.I32,
      'sampleRate',
      None,
      None))

    def __init__(self, aclHandle = None, aceHandle = None, remoteSn = None, appId = None, localId = None, size = None, sampleType = None, sampleRate = None):
        self.aclHandle = aclHandle
        self.aceHandle = aceHandle
        self.remoteSn = remoteSn
        self.appId = appId
        self.localId = localId
        self.size = size
        self.sampleType = sampleType
        self.sampleRate = sampleRate



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
                    self.aclHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.aceHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.remoteSn = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.appId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.localId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I32:
                    self.size = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I32:
                    self.sampleType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.I32:
                    self.sampleRate = iprot.readI32()
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
        oprot.writeStructBegin('addActionCopyToAce_IDL_args')
        if self.aclHandle != None:
            oprot.writeFieldBegin('aclHandle', TType.I32, 1)
            oprot.writeI32(self.aclHandle)
            oprot.writeFieldEnd()
        if self.aceHandle != None:
            oprot.writeFieldBegin('aceHandle', TType.I32, 2)
            oprot.writeI32(self.aceHandle)
            oprot.writeFieldEnd()
        if self.remoteSn != None:
            oprot.writeFieldBegin('remoteSn', TType.I32, 3)
            oprot.writeI32(self.remoteSn)
            oprot.writeFieldEnd()
        if self.appId != None:
            oprot.writeFieldBegin('appId', TType.I32, 4)
            oprot.writeI32(self.appId)
            oprot.writeFieldEnd()
        if self.localId != None:
            oprot.writeFieldBegin('localId', TType.I32, 5)
            oprot.writeI32(self.localId)
            oprot.writeFieldEnd()
        if self.size != None:
            oprot.writeFieldBegin('size', TType.I32, 6)
            oprot.writeI32(self.size)
            oprot.writeFieldEnd()
        if self.sampleType != None:
            oprot.writeFieldBegin('sampleType', TType.I32, 7)
            oprot.writeI32(self.sampleType)
            oprot.writeFieldEnd()
        if self.sampleRate != None:
            oprot.writeFieldBegin('sampleRate', TType.I32, 8)
            oprot.writeI32(self.sampleRate)
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




class addActionCopyToAce_IDL_result(object):
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
        oprot.writeStructBegin('addActionCopyToAce_IDL_result')
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




class addActionDivertToAce_IDL_args(object):
    """
    Attributes:
     - aclHandle
     - aceHandle
     - remoteSn
     - appId
     - localId
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'aclHandle',
      None,
      None),
     (2,
      TType.I32,
      'aceHandle',
      None,
      None),
     (3,
      TType.I32,
      'remoteSn',
      None,
      None),
     (4,
      TType.I32,
      'appId',
      None,
      None),
     (5,
      TType.I32,
      'localId',
      None,
      None))

    def __init__(self, aclHandle = None, aceHandle = None, remoteSn = None, appId = None, localId = None):
        self.aclHandle = aclHandle
        self.aceHandle = aceHandle
        self.remoteSn = remoteSn
        self.appId = appId
        self.localId = localId



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
                    self.aclHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.aceHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.remoteSn = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.appId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.localId = iprot.readI32()
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
        oprot.writeStructBegin('addActionDivertToAce_IDL_args')
        if self.aclHandle != None:
            oprot.writeFieldBegin('aclHandle', TType.I32, 1)
            oprot.writeI32(self.aclHandle)
            oprot.writeFieldEnd()
        if self.aceHandle != None:
            oprot.writeFieldBegin('aceHandle', TType.I32, 2)
            oprot.writeI32(self.aceHandle)
            oprot.writeFieldEnd()
        if self.remoteSn != None:
            oprot.writeFieldBegin('remoteSn', TType.I32, 3)
            oprot.writeI32(self.remoteSn)
            oprot.writeFieldEnd()
        if self.appId != None:
            oprot.writeFieldBegin('appId', TType.I32, 4)
            oprot.writeI32(self.appId)
            oprot.writeFieldEnd()
        if self.localId != None:
            oprot.writeFieldBegin('localId', TType.I32, 5)
            oprot.writeI32(self.localId)
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




class addActionDivertToAce_IDL_result(object):
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
        oprot.writeStructBegin('addActionDivertToAce_IDL_result')
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




class removeActionFromAce_IDL_args(object):
    """
    Attributes:
     - aclHandle
     - aceHandle
     - actionHandle
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'aclHandle',
      None,
      None),
     (2,
      TType.I32,
      'aceHandle',
      None,
      None),
     (3,
      TType.I32,
      'actionHandle',
      None,
      None))

    def __init__(self, aclHandle = None, aceHandle = None, actionHandle = None):
        self.aclHandle = aclHandle
        self.aceHandle = aceHandle
        self.actionHandle = actionHandle



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
                    self.aclHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.aceHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.actionHandle = iprot.readI32()
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
        oprot.writeStructBegin('removeActionFromAce_IDL_args')
        if self.aclHandle != None:
            oprot.writeFieldBegin('aclHandle', TType.I32, 1)
            oprot.writeI32(self.aclHandle)
            oprot.writeFieldEnd()
        if self.aceHandle != None:
            oprot.writeFieldBegin('aceHandle', TType.I32, 2)
            oprot.writeI32(self.aceHandle)
            oprot.writeFieldEnd()
        if self.actionHandle != None:
            oprot.writeFieldBegin('actionHandle', TType.I32, 3)
            oprot.writeI32(self.actionHandle)
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




class removeActionFromAce_IDL_result(object):
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
        oprot.writeStructBegin('removeActionFromAce_IDL_result')
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




class applyPolicyToTarget_IDL_args(object):
    """
    Attributes:
     - policyHandle
     - ifHandle
     - location
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'policyHandle',
      None,
      None),
     (2,
      TType.I64,
      'ifHandle',
      None,
      None),
     (3,
      TType.BYTE,
      'location',
      None,
      None))

    def __init__(self, policyHandle = None, ifHandle = None, location = None):
        self.policyHandle = policyHandle
        self.ifHandle = ifHandle
        self.location = location



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
                    self.policyHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.ifHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.BYTE:
                    self.location = iprot.readByte()
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
        oprot.writeStructBegin('applyPolicyToTarget_IDL_args')
        if self.policyHandle != None:
            oprot.writeFieldBegin('policyHandle', TType.I32, 1)
            oprot.writeI32(self.policyHandle)
            oprot.writeFieldEnd()
        if self.ifHandle != None:
            oprot.writeFieldBegin('ifHandle', TType.I64, 2)
            oprot.writeI64(self.ifHandle)
            oprot.writeFieldEnd()
        if self.location != None:
            oprot.writeFieldBegin('location', TType.BYTE, 3)
            oprot.writeByte(self.location)
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




class applyPolicyToTarget_IDL_result(object):
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
        oprot.writeStructBegin('applyPolicyToTarget_IDL_result')
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




class removePolicyFromTarget_IDL_args(object):
    """
    Attributes:
     - policyHandle
     - ifHandle
     - location
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'policyHandle',
      None,
      None),
     (2,
      TType.I64,
      'ifHandle',
      None,
      None),
     (3,
      TType.BYTE,
      'location',
      None,
      None))

    def __init__(self, policyHandle = None, ifHandle = None, location = None):
        self.policyHandle = policyHandle
        self.ifHandle = ifHandle
        self.location = location



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
                    self.policyHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.ifHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.BYTE:
                    self.location = iprot.readByte()
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
        oprot.writeStructBegin('removePolicyFromTarget_IDL_args')
        if self.policyHandle != None:
            oprot.writeFieldBegin('policyHandle', TType.I32, 1)
            oprot.writeI32(self.policyHandle)
            oprot.writeFieldEnd()
        if self.ifHandle != None:
            oprot.writeFieldBegin('ifHandle', TType.I64, 2)
            oprot.writeI64(self.ifHandle)
            oprot.writeFieldEnd()
        if self.location != None:
            oprot.writeFieldBegin('location', TType.BYTE, 3)
            oprot.writeByte(self.location)
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




class removePolicyFromTarget_IDL_result(object):
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
        oprot.writeStructBegin('removePolicyFromTarget_IDL_result')
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




class createAcl_IDL_args(object):
    """
    Attributes:
     - sessionId
     - type
     - persistent
     - addrFamily
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionId',
      None,
      None),
     (2,
      TType.I32,
      'type',
      None,
      None),
     (3,
      TType.I32,
      'persistent',
      None,
      None),
     (4,
      TType.I32,
      'addrFamily',
      None,
      None))

    def __init__(self, sessionId = None, type = None, persistent = None, addrFamily = None):
        self.sessionId = sessionId
        self.type = type
        self.persistent = persistent
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
                    self.sessionId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.persistent = iprot.readI32()
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
        oprot.writeStructBegin('createAcl_IDL_args')
        if self.sessionId != None:
            oprot.writeFieldBegin('sessionId', TType.I32, 1)
            oprot.writeI32(self.sessionId)
            oprot.writeFieldEnd()
        if self.type != None:
            oprot.writeFieldBegin('type', TType.I32, 2)
            oprot.writeI32(self.type)
            oprot.writeFieldEnd()
        if self.persistent != None:
            oprot.writeFieldBegin('persistent', TType.I32, 3)
            oprot.writeI32(self.persistent)
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




class createAcl_IDL_result(object):
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
        oprot.writeStructBegin('createAcl_IDL_result')
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




class deleteAcl_IDL_args(object):
    """
    Attributes:
     - sessionId
     - aclHandle
    """

    thrift_spec = (None, (1,
      TType.I32,
      'sessionId',
      None,
      None), (2,
      TType.I32,
      'aclHandle',
      None,
      None))

    def __init__(self, sessionId = None, aclHandle = None):
        self.sessionId = sessionId
        self.aclHandle = aclHandle



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
                    self.aclHandle = iprot.readI32()
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
        oprot.writeStructBegin('deleteAcl_IDL_args')
        if self.sessionId != None:
            oprot.writeFieldBegin('sessionId', TType.I32, 1)
            oprot.writeI32(self.sessionId)
            oprot.writeFieldEnd()
        if self.aclHandle != None:
            oprot.writeFieldBegin('aclHandle', TType.I32, 2)
            oprot.writeI32(self.aclHandle)
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




class deleteAcl_IDL_result(object):
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
        oprot.writeStructBegin('deleteAcl_IDL_result')
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




class getL3AceList_IDL_args(object):
    """
    Attributes:
     - aclHandle
     - lifetime
     - aclName
     - addrFamily
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'aclHandle',
      None,
      None),
     (2,
      TType.I32,
      'lifetime',
      None,
      None),
     (3,
      TType.STRING,
      'aclName',
      None,
      None),
     (4,
      TType.I32,
      'addrFamily',
      None,
      None))

    def __init__(self, aclHandle = None, lifetime = None, aclName = None, addrFamily = None):
        self.aclHandle = aclHandle
        self.lifetime = lifetime
        self.aclName = aclName
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
                    self.aclHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.lifetime = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.aclName = iprot.readString()
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
        oprot.writeStructBegin('getL3AceList_IDL_args')
        if self.aclHandle != None:
            oprot.writeFieldBegin('aclHandle', TType.I32, 1)
            oprot.writeI32(self.aclHandle)
            oprot.writeFieldEnd()
        if self.lifetime != None:
            oprot.writeFieldBegin('lifetime', TType.I32, 2)
            oprot.writeI32(self.lifetime)
            oprot.writeFieldEnd()
        if self.aclName != None:
            oprot.writeFieldBegin('aclName', TType.STRING, 3)
            oprot.writeString(self.aclName)
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




class getL3AceList_IDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.LIST,
      'success',
      (TType.STRUCT, (L3AceParam_IDL, L3AceParam_IDL.thrift_spec)),
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
                    (_etype66, _size63,) = iprot.readListBegin()
                    for _i67 in xrange(_size63):
                        _elem68 = L3AceParam_IDL()
                        _elem68.read(iprot)
                        self.success.append(_elem68)

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
        oprot.writeStructBegin('getL3AceList_IDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.STRUCT, len(self.success))
            for iter69 in self.success:
                iter69.write(oprot)

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




class getAceList_IDL_args(object):
    """
    Attributes:
     - aclHandle
    """

    thrift_spec = (None, (1,
      TType.I32,
      'aclHandle',
      None,
      None))

    def __init__(self, aclHandle = None):
        self.aclHandle = aclHandle



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
                    self.aclHandle = iprot.readI32()
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
        oprot.writeStructBegin('getAceList_IDL_args')
        if self.aclHandle != None:
            oprot.writeFieldBegin('aclHandle', TType.I32, 1)
            oprot.writeI32(self.aclHandle)
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




class getAceList_IDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.LIST,
      'success',
      (TType.STRUCT, (L3AceParam_IDL, L3AceParam_IDL.thrift_spec)),
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
                    (_etype73, _size70,) = iprot.readListBegin()
                    for _i74 in xrange(_size70):
                        _elem75 = L3AceParam_IDL()
                        _elem75.read(iprot)
                        self.success.append(_elem75)

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
        oprot.writeStructBegin('getAceList_IDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.STRUCT, len(self.success))
            for iter76 in self.success:
                iter76.write(oprot)

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




class getL2AceList_IDL_args(object):
    """
    Attributes:
     - aclHandle
     - aclName
    """

    thrift_spec = (None, (1,
      TType.I32,
      'aclHandle',
      None,
      None), (2,
      TType.STRING,
      'aclName',
      None,
      None))

    def __init__(self, aclHandle = None, aclName = None):
        self.aclHandle = aclHandle
        self.aclName = aclName



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
                    self.aclHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.aclName = iprot.readString()
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
        oprot.writeStructBegin('getL2AceList_IDL_args')
        if self.aclHandle != None:
            oprot.writeFieldBegin('aclHandle', TType.I32, 1)
            oprot.writeI32(self.aclHandle)
            oprot.writeFieldEnd()
        if self.aclName != None:
            oprot.writeFieldBegin('aclName', TType.STRING, 2)
            oprot.writeString(self.aclName)
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




class getL2AceList_IDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.LIST,
      'success',
      (TType.STRUCT, (L2AceParam_IDL, L2AceParam_IDL.thrift_spec)),
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
                    (_etype80, _size77,) = iprot.readListBegin()
                    for _i81 in xrange(_size77):
                        _elem82 = L2AceParam_IDL()
                        _elem82.read(iprot)
                        self.success.append(_elem82)

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
        oprot.writeStructBegin('getL2AceList_IDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.STRUCT, len(self.success))
            for iter83 in self.success:
                iter83.write(oprot)

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




class getAclList_IDL_args(object):
    """
    Attributes:
     - aclType
    """

    thrift_spec = (None, (1,
      TType.I32,
      'aclType',
      None,
      None))

    def __init__(self, aclType = None):
        self.aclType = aclType



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
                    self.aclType = iprot.readI32()
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
        oprot.writeStructBegin('getAclList_IDL_args')
        if self.aclType != None:
            oprot.writeFieldBegin('aclType', TType.I32, 1)
            oprot.writeI32(self.aclType)
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




class getAclList_IDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.LIST,
      'success',
      (TType.STRUCT, (AclHeader_IDL, AclHeader_IDL.thrift_spec)),
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
                    (_etype87, _size84,) = iprot.readListBegin()
                    for _i88 in xrange(_size84):
                        _elem89 = AclHeader_IDL()
                        _elem89.read(iprot)
                        self.success.append(_elem89)

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
        oprot.writeStructBegin('getAclList_IDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.STRUCT, len(self.success))
            for iter90 in self.success:
                iter90.write(oprot)

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




class getIfcAclList_IDL_args(object):
    """
    Attributes:
     - ifHandle
     - direction
     - aclType
    """

    thrift_spec = (None,
     (1,
      TType.I64,
      'ifHandle',
      None,
      None),
     (2,
      TType.I16,
      'direction',
      None,
      None),
     (3,
      TType.I32,
      'aclType',
      None,
      None))

    def __init__(self, ifHandle = None, direction = None, aclType = None):
        self.ifHandle = ifHandle
        self.direction = direction
        self.aclType = aclType



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
                if ftype == TType.I64:
                    self.ifHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I16:
                    self.direction = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.aclType = iprot.readI32()
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
        oprot.writeStructBegin('getIfcAclList_IDL_args')
        if self.ifHandle != None:
            oprot.writeFieldBegin('ifHandle', TType.I64, 1)
            oprot.writeI64(self.ifHandle)
            oprot.writeFieldEnd()
        if self.direction != None:
            oprot.writeFieldBegin('direction', TType.I16, 2)
            oprot.writeI16(self.direction)
            oprot.writeFieldEnd()
        if self.aclType != None:
            oprot.writeFieldBegin('aclType', TType.I32, 3)
            oprot.writeI32(self.aclType)
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




class getIfcAclList_IDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.LIST,
      'success',
      (TType.STRUCT, (AclHeader_IDL, AclHeader_IDL.thrift_spec)),
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
                    (_etype94, _size91,) = iprot.readListBegin()
                    for _i95 in xrange(_size91):
                        _elem96 = AclHeader_IDL()
                        _elem96.read(iprot)
                        self.success.append(_elem96)

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
        oprot.writeStructBegin('getIfcAclList_IDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.STRUCT, len(self.success))
            for iter97 in self.success:
                iter97.write(oprot)

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




class getAclByName_IDL_args(object):
    """
    Attributes:
     - aclName
    """

    thrift_spec = (None, (1,
      TType.STRING,
      'aclName',
      None,
      None))

    def __init__(self, aclName = None):
        self.aclName = aclName



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
                    self.aclName = iprot.readString()
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
        oprot.writeStructBegin('getAclByName_IDL_args')
        if self.aclName != None:
            oprot.writeFieldBegin('aclName', TType.STRING, 1)
            oprot.writeString(self.aclName)
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




class getAclByName_IDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.STRUCT,
      'success',
      (AclHeader_IDL, AclHeader_IDL.thrift_spec),
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
                    self.success = AclHeader_IDL()
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
        oprot.writeStructBegin('getAclByName_IDL_result')
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




class getAclName_IDL_args(object):
    """
    Attributes:
     - aclHandle
    """

    thrift_spec = (None, (1,
      TType.I32,
      'aclHandle',
      None,
      None))

    def __init__(self, aclHandle = None):
        self.aclHandle = aclHandle



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
                    self.aclHandle = iprot.readI32()
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
        oprot.writeStructBegin('getAclName_IDL_args')
        if self.aclHandle != None:
            oprot.writeFieldBegin('aclHandle', TType.I32, 1)
            oprot.writeI32(self.aclHandle)
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




class getAclName_IDL_result(object):
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
        oprot.writeStructBegin('getAclName_IDL_result')
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




class addL3Ace_IDL_args(object):
    """
    Attributes:
     - aclHandle
     - aceParam
    """

    thrift_spec = (None, (1,
      TType.I32,
      'aclHandle',
      None,
      None), (2,
      TType.STRUCT,
      'aceParam',
      (L3AceParam_IDL, L3AceParam_IDL.thrift_spec),
      None))

    def __init__(self, aclHandle = None, aceParam = None):
        self.aclHandle = aclHandle
        self.aceParam = aceParam



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
                    self.aclHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.aceParam = L3AceParam_IDL()
                    self.aceParam.read(iprot)
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
        oprot.writeStructBegin('addL3Ace_IDL_args')
        if self.aclHandle != None:
            oprot.writeFieldBegin('aclHandle', TType.I32, 1)
            oprot.writeI32(self.aclHandle)
            oprot.writeFieldEnd()
        if self.aceParam != None:
            oprot.writeFieldBegin('aceParam', TType.STRUCT, 2)
            self.aceParam.write(oprot)
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




class addL3Ace_IDL_result(object):
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
        oprot.writeStructBegin('addL3Ace_IDL_result')
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




class addL2Ace_IDL_args(object):
    """
    Attributes:
     - aclHandle
     - aceParam
    """

    thrift_spec = (None, (1,
      TType.I32,
      'aclHandle',
      None,
      None), (2,
      TType.STRUCT,
      'aceParam',
      (L2AceParam_IDL, L2AceParam_IDL.thrift_spec),
      None))

    def __init__(self, aclHandle = None, aceParam = None):
        self.aclHandle = aclHandle
        self.aceParam = aceParam



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
                    self.aclHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.aceParam = L2AceParam_IDL()
                    self.aceParam.read(iprot)
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
        oprot.writeStructBegin('addL2Ace_IDL_args')
        if self.aclHandle != None:
            oprot.writeFieldBegin('aclHandle', TType.I32, 1)
            oprot.writeI32(self.aclHandle)
            oprot.writeFieldEnd()
        if self.aceParam != None:
            oprot.writeFieldBegin('aceParam', TType.STRUCT, 2)
            self.aceParam.write(oprot)
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




class addL2Ace_IDL_result(object):
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
        oprot.writeStructBegin('addL2Ace_IDL_result')
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




class deleteAce_IDL_args(object):
    """
    Attributes:
     - aclHandle
     - elemHandle
    """

    thrift_spec = (None, (1,
      TType.I32,
      'aclHandle',
      None,
      None), (2,
      TType.I32,
      'elemHandle',
      None,
      None))

    def __init__(self, aclHandle = None, elemHandle = None):
        self.aclHandle = aclHandle
        self.elemHandle = elemHandle



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
                    self.aclHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.elemHandle = iprot.readI32()
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
        oprot.writeStructBegin('deleteAce_IDL_args')
        if self.aclHandle != None:
            oprot.writeFieldBegin('aclHandle', TType.I32, 1)
            oprot.writeI32(self.aclHandle)
            oprot.writeFieldEnd()
        if self.elemHandle != None:
            oprot.writeFieldBegin('elemHandle', TType.I32, 2)
            oprot.writeI32(self.elemHandle)
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




class deleteAce_IDL_result(object):
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
        oprot.writeStructBegin('deleteAce_IDL_result')
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




class applyAclToInterface_IDL_args(object):
    """
    Attributes:
     - aclHandle
     - ifHandle
     - direction
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'aclHandle',
      None,
      None),
     (2,
      TType.I64,
      'ifHandle',
      None,
      None),
     (3,
      TType.I16,
      'direction',
      None,
      None))

    def __init__(self, aclHandle = None, ifHandle = None, direction = None):
        self.aclHandle = aclHandle
        self.ifHandle = ifHandle
        self.direction = direction



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
                    self.aclHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.ifHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I16:
                    self.direction = iprot.readI16()
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
        oprot.writeStructBegin('applyAclToInterface_IDL_args')
        if self.aclHandle != None:
            oprot.writeFieldBegin('aclHandle', TType.I32, 1)
            oprot.writeI32(self.aclHandle)
            oprot.writeFieldEnd()
        if self.ifHandle != None:
            oprot.writeFieldBegin('ifHandle', TType.I64, 2)
            oprot.writeI64(self.ifHandle)
            oprot.writeFieldEnd()
        if self.direction != None:
            oprot.writeFieldBegin('direction', TType.I16, 3)
            oprot.writeI16(self.direction)
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




class applyAclToInterface_IDL_result(object):
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
        oprot.writeStructBegin('applyAclToInterface_IDL_result')
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




class removeAclFromInterface_IDL_args(object):
    """
    Attributes:
     - aclHandle
     - ifHandle
     - direction
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'aclHandle',
      None,
      None),
     (2,
      TType.I64,
      'ifHandle',
      None,
      None),
     (3,
      TType.I16,
      'direction',
      None,
      None))

    def __init__(self, aclHandle = None, ifHandle = None, direction = None):
        self.aclHandle = aclHandle
        self.ifHandle = ifHandle
        self.direction = direction



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
                    self.aclHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.ifHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I16:
                    self.direction = iprot.readI16()
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
        oprot.writeStructBegin('removeAclFromInterface_IDL_args')
        if self.aclHandle != None:
            oprot.writeFieldBegin('aclHandle', TType.I32, 1)
            oprot.writeI32(self.aclHandle)
            oprot.writeFieldEnd()
        if self.ifHandle != None:
            oprot.writeFieldBegin('ifHandle', TType.I64, 2)
            oprot.writeI64(self.ifHandle)
            oprot.writeFieldEnd()
        if self.direction != None:
            oprot.writeFieldBegin('direction', TType.I16, 3)
            oprot.writeI16(self.direction)
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




class removeAclFromInterface_IDL_result(object):
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
        oprot.writeStructBegin('removeAclFromInterface_IDL_result')
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




class getAceMatch_IDL_args(object):
    """
    Attributes:
     - aclHandle
     - elemHandle
    """

    thrift_spec = (None, (1,
      TType.I32,
      'aclHandle',
      None,
      None), (2,
      TType.I32,
      'elemHandle',
      None,
      None))

    def __init__(self, aclHandle = None, elemHandle = None):
        self.aclHandle = aclHandle
        self.elemHandle = elemHandle



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
                    self.aclHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.elemHandle = iprot.readI32()
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
        oprot.writeStructBegin('getAceMatch_IDL_args')
        if self.aclHandle != None:
            oprot.writeFieldBegin('aclHandle', TType.I32, 1)
            oprot.writeI32(self.aclHandle)
            oprot.writeFieldEnd()
        if self.elemHandle != None:
            oprot.writeFieldBegin('elemHandle', TType.I32, 2)
            oprot.writeI32(self.elemHandle)
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




class getAceMatch_IDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.I64,
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
                if ftype == TType.I64:
                    self.success = iprot.readI64()
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
        oprot.writeStructBegin('getAceMatch_IDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.I64, 0)
            oprot.writeI64(self.success)
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




class clearAclMatch_IDL_args(object):
    """
    Attributes:
     - aclHandle
    """

    thrift_spec = (None, (1,
      TType.I32,
      'aclHandle',
      None,
      None))

    def __init__(self, aclHandle = None):
        self.aclHandle = aclHandle



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
                    self.aclHandle = iprot.readI32()
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
        oprot.writeStructBegin('clearAclMatch_IDL_args')
        if self.aclHandle != None:
            oprot.writeFieldBegin('aclHandle', TType.I32, 1)
            oprot.writeI32(self.aclHandle)
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




class clearAclMatch_IDL_result(object):
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
        oprot.writeStructBegin('clearAclMatch_IDL_result')
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




class getPolicyCapability_IDL_args(object):
    """
    Attributes:
     - handle
    """

    thrift_spec = (None, (1,
      TType.I32,
      'handle',
      None,
      None))

    def __init__(self, handle = None):
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
                    self.handle = iprot.readI32()
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
        oprot.writeStructBegin('getPolicyCapability_IDL_args')
        if self.handle != None:
            oprot.writeFieldBegin('handle', TType.I32, 1)
            oprot.writeI32(self.handle)
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




class getPolicyCapability_IDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.STRUCT,
      'success',
      (PolicyCapabilityIDL, PolicyCapabilityIDL.thrift_spec),
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
                    self.success = PolicyCapabilityIDL()
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
        oprot.writeStructBegin('getPolicyCapability_IDL_result')
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




class getProtocolCapability_IDL_args(object):
    """
    Attributes:
     - handle
    """

    thrift_spec = (None, (1,
      TType.I32,
      'handle',
      None,
      None))

    def __init__(self, handle = None):
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
                    self.handle = iprot.readI32()
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
        oprot.writeStructBegin('getProtocolCapability_IDL_args')
        if self.handle != None:
            oprot.writeFieldBegin('handle', TType.I32, 1)
            oprot.writeI32(self.handle)
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




class getProtocolCapability_IDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.LIST,
      'success',
      (TType.STRUCT, (ProtocolCapabilityIDL, ProtocolCapabilityIDL.thrift_spec)),
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
                    (_etype101, _size98,) = iprot.readListBegin()
                    for _i102 in xrange(_size98):
                        _elem103 = ProtocolCapabilityIDL()
                        _elem103.read(iprot)
                        self.success.append(_elem103)

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
        oprot.writeStructBegin('getProtocolCapability_IDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.STRUCT, len(self.success))
            for iter104 in self.success:
                iter104.write(oprot)

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




class getSubProtocolCapability_IDL_args(object):
    """
    Attributes:
     - protocol
    """

    thrift_spec = (None, (1,
      TType.STRING,
      'protocol',
      None,
      None))

    def __init__(self, protocol = None):
        self.protocol = protocol



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
                    self.protocol = iprot.readString()
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
        oprot.writeStructBegin('getSubProtocolCapability_IDL_args')
        if self.protocol != None:
            oprot.writeFieldBegin('protocol', TType.STRING, 1)
            oprot.writeString(self.protocol)
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




class getSubProtocolCapability_IDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.LIST,
      'success',
      (TType.STRUCT, (ProtocolCapabilityIDL, ProtocolCapabilityIDL.thrift_spec)),
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
                    (_etype108, _size105,) = iprot.readListBegin()
                    for _i109 in xrange(_size105):
                        _elem110 = ProtocolCapabilityIDL()
                        _elem110.read(iprot)
                        self.success.append(_elem110)

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
        oprot.writeStructBegin('getSubProtocolCapability_IDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.STRUCT, len(self.success))
            for iter111 in self.success:
                iter111.write(oprot)

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




class createNamedAcl_IDL_args(object):
    """
    Attributes:
     - sessionId
     - type
     - persistent
     - addrFamily
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionId',
      None,
      None),
     (2,
      TType.I32,
      'type',
      None,
      None),
     (3,
      TType.I32,
      'persistent',
      None,
      None),
     (4,
      TType.I32,
      'addrFamily',
      None,
      None))

    def __init__(self, sessionId = None, type = None, persistent = None, addrFamily = None):
        self.sessionId = sessionId
        self.type = type
        self.persistent = persistent
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
                    self.sessionId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.persistent = iprot.readI32()
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
        oprot.writeStructBegin('createNamedAcl_IDL_args')
        if self.sessionId != None:
            oprot.writeFieldBegin('sessionId', TType.I32, 1)
            oprot.writeI32(self.sessionId)
            oprot.writeFieldEnd()
        if self.type != None:
            oprot.writeFieldBegin('type', TType.I32, 2)
            oprot.writeI32(self.type)
            oprot.writeFieldEnd()
        if self.persistent != None:
            oprot.writeFieldBegin('persistent', TType.I32, 3)
            oprot.writeI32(self.persistent)
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




class createNamedAcl_IDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.STRUCT,
      'success',
      (AclHeader_IDL, AclHeader_IDL.thrift_spec),
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
                    self.success = AclHeader_IDL()
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
        oprot.writeStructBegin('createNamedAcl_IDL_result')
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




class deleteNamedAcl_IDL_args(object):
    """
    Attributes:
     - sessionId
     - name
     - aclHandle
     - lifetime
     - addrFamily
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'sessionId',
      None,
      None),
     (2,
      TType.STRING,
      'name',
      None,
      None),
     (3,
      TType.I32,
      'aclHandle',
      None,
      None),
     (4,
      TType.I32,
      'lifetime',
      None,
      None),
     (5,
      TType.I32,
      'addrFamily',
      None,
      None))

    def __init__(self, sessionId = None, name = None, aclHandle = None, lifetime = None, addrFamily = None):
        self.sessionId = sessionId
        self.name = name
        self.aclHandle = aclHandle
        self.lifetime = lifetime
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
                    self.sessionId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.name = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.aclHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.lifetime = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
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
        oprot.writeStructBegin('deleteNamedAcl_IDL_args')
        if self.sessionId != None:
            oprot.writeFieldBegin('sessionId', TType.I32, 1)
            oprot.writeI32(self.sessionId)
            oprot.writeFieldEnd()
        if self.name != None:
            oprot.writeFieldBegin('name', TType.STRING, 2)
            oprot.writeString(self.name)
            oprot.writeFieldEnd()
        if self.aclHandle != None:
            oprot.writeFieldBegin('aclHandle', TType.I32, 3)
            oprot.writeI32(self.aclHandle)
            oprot.writeFieldEnd()
        if self.lifetime != None:
            oprot.writeFieldBegin('lifetime', TType.I32, 4)
            oprot.writeI32(self.lifetime)
            oprot.writeFieldEnd()
        if self.addrFamily != None:
            oprot.writeFieldBegin('addrFamily', TType.I32, 5)
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




class deleteNamedAcl_IDL_result(object):
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
        oprot.writeStructBegin('deleteNamedAcl_IDL_result')
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




class addNamedL3Ace_IDL_args(object):
    """
    Attributes:
     - name
     - aclHandle
     - lifetime
     - addrFamily
     - aceParam
    """

    thrift_spec = (None,
     (1,
      TType.STRING,
      'name',
      None,
      None),
     (2,
      TType.I32,
      'aclHandle',
      None,
      None),
     (3,
      TType.I32,
      'lifetime',
      None,
      None),
     (4,
      TType.I32,
      'addrFamily',
      None,
      None),
     (5,
      TType.STRUCT,
      'aceParam',
      (L3AceParam_IDL, L3AceParam_IDL.thrift_spec),
      None))

    def __init__(self, name = None, aclHandle = None, lifetime = None, addrFamily = None, aceParam = None):
        self.name = name
        self.aclHandle = aclHandle
        self.lifetime = lifetime
        self.addrFamily = addrFamily
        self.aceParam = aceParam



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
                    self.name = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.aclHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.lifetime = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.addrFamily = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRUCT:
                    self.aceParam = L3AceParam_IDL()
                    self.aceParam.read(iprot)
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
        oprot.writeStructBegin('addNamedL3Ace_IDL_args')
        if self.name != None:
            oprot.writeFieldBegin('name', TType.STRING, 1)
            oprot.writeString(self.name)
            oprot.writeFieldEnd()
        if self.aclHandle != None:
            oprot.writeFieldBegin('aclHandle', TType.I32, 2)
            oprot.writeI32(self.aclHandle)
            oprot.writeFieldEnd()
        if self.lifetime != None:
            oprot.writeFieldBegin('lifetime', TType.I32, 3)
            oprot.writeI32(self.lifetime)
            oprot.writeFieldEnd()
        if self.addrFamily != None:
            oprot.writeFieldBegin('addrFamily', TType.I32, 4)
            oprot.writeI32(self.addrFamily)
            oprot.writeFieldEnd()
        if self.aceParam != None:
            oprot.writeFieldBegin('aceParam', TType.STRUCT, 5)
            self.aceParam.write(oprot)
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




class addNamedL3Ace_IDL_result(object):
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
        oprot.writeStructBegin('addNamedL3Ace_IDL_result')
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




class deleteNamedAce_IDL_args(object):
    """
    Attributes:
     - name
     - aclHandle
     - elemHandle
     - lifetime
     - addrFamily
    """

    thrift_spec = (None,
     (1,
      TType.STRING,
      'name',
      None,
      None),
     (2,
      TType.I32,
      'aclHandle',
      None,
      None),
     (3,
      TType.I32,
      'elemHandle',
      None,
      None),
     (4,
      TType.I32,
      'lifetime',
      None,
      None),
     (5,
      TType.I32,
      'addrFamily',
      None,
      None))

    def __init__(self, name = None, aclHandle = None, elemHandle = None, lifetime = None, addrFamily = None):
        self.name = name
        self.aclHandle = aclHandle
        self.elemHandle = elemHandle
        self.lifetime = lifetime
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
                if ftype == TType.STRING:
                    self.name = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.aclHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.elemHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.lifetime = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
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
        oprot.writeStructBegin('deleteNamedAce_IDL_args')
        if self.name != None:
            oprot.writeFieldBegin('name', TType.STRING, 1)
            oprot.writeString(self.name)
            oprot.writeFieldEnd()
        if self.aclHandle != None:
            oprot.writeFieldBegin('aclHandle', TType.I32, 2)
            oprot.writeI32(self.aclHandle)
            oprot.writeFieldEnd()
        if self.elemHandle != None:
            oprot.writeFieldBegin('elemHandle', TType.I32, 3)
            oprot.writeI32(self.elemHandle)
            oprot.writeFieldEnd()
        if self.lifetime != None:
            oprot.writeFieldBegin('lifetime', TType.I32, 4)
            oprot.writeI32(self.lifetime)
            oprot.writeFieldEnd()
        if self.addrFamily != None:
            oprot.writeFieldBegin('addrFamily', TType.I32, 5)
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




class deleteNamedAce_IDL_result(object):
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
        oprot.writeStructBegin('deleteNamedAce_IDL_result')
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




class applyNamedAclToInterface_IDL_args(object):
    """
    Attributes:
     - name
     - aclType
     - ifHandle
     - direction
     - addrFamily
    """

    thrift_spec = (None,
     (1,
      TType.STRING,
      'name',
      None,
      None),
     (2,
      TType.I32,
      'aclType',
      None,
      None),
     (3,
      TType.I64,
      'ifHandle',
      None,
      None),
     (4,
      TType.I16,
      'direction',
      None,
      None),
     (5,
      TType.I32,
      'addrFamily',
      None,
      None))

    def __init__(self, name = None, aclType = None, ifHandle = None, direction = None, addrFamily = None):
        self.name = name
        self.aclType = aclType
        self.ifHandle = ifHandle
        self.direction = direction
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
                if ftype == TType.STRING:
                    self.name = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.aclType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I64:
                    self.ifHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I16:
                    self.direction = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
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
        oprot.writeStructBegin('applyNamedAclToInterface_IDL_args')
        if self.name != None:
            oprot.writeFieldBegin('name', TType.STRING, 1)
            oprot.writeString(self.name)
            oprot.writeFieldEnd()
        if self.aclType != None:
            oprot.writeFieldBegin('aclType', TType.I32, 2)
            oprot.writeI32(self.aclType)
            oprot.writeFieldEnd()
        if self.ifHandle != None:
            oprot.writeFieldBegin('ifHandle', TType.I64, 3)
            oprot.writeI64(self.ifHandle)
            oprot.writeFieldEnd()
        if self.direction != None:
            oprot.writeFieldBegin('direction', TType.I16, 4)
            oprot.writeI16(self.direction)
            oprot.writeFieldEnd()
        if self.addrFamily != None:
            oprot.writeFieldBegin('addrFamily', TType.I32, 5)
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




class applyNamedAclToInterface_IDL_result(object):
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
        oprot.writeStructBegin('applyNamedAclToInterface_IDL_result')
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




class removeNamedAclFromInterface_IDL_args(object):
    """
    Attributes:
     - name
     - aclType
     - ifHandle
     - direction
     - addrFamily
    """

    thrift_spec = (None,
     (1,
      TType.STRING,
      'name',
      None,
      None),
     (2,
      TType.I32,
      'aclType',
      None,
      None),
     (3,
      TType.I64,
      'ifHandle',
      None,
      None),
     (4,
      TType.I16,
      'direction',
      None,
      None),
     (5,
      TType.I32,
      'addrFamily',
      None,
      None))

    def __init__(self, name = None, aclType = None, ifHandle = None, direction = None, addrFamily = None):
        self.name = name
        self.aclType = aclType
        self.ifHandle = ifHandle
        self.direction = direction
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
                if ftype == TType.STRING:
                    self.name = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.aclType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I64:
                    self.ifHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I16:
                    self.direction = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
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
        oprot.writeStructBegin('removeNamedAclFromInterface_IDL_args')
        if self.name != None:
            oprot.writeFieldBegin('name', TType.STRING, 1)
            oprot.writeString(self.name)
            oprot.writeFieldEnd()
        if self.aclType != None:
            oprot.writeFieldBegin('aclType', TType.I32, 2)
            oprot.writeI32(self.aclType)
            oprot.writeFieldEnd()
        if self.ifHandle != None:
            oprot.writeFieldBegin('ifHandle', TType.I64, 3)
            oprot.writeI64(self.ifHandle)
            oprot.writeFieldEnd()
        if self.direction != None:
            oprot.writeFieldBegin('direction', TType.I16, 4)
            oprot.writeI16(self.direction)
            oprot.writeFieldEnd()
        if self.addrFamily != None:
            oprot.writeFieldBegin('addrFamily', TType.I32, 5)
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




class removeNamedAclFromInterface_IDL_result(object):
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
        oprot.writeStructBegin('removeNamedAclFromInterface_IDL_result')
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




class getNamedAceMatch_IDL_args(object):
    """
    Attributes:
     - name
     - aclHandle
     - elemHandle
     - lifetime
     - addrFamily
    """

    thrift_spec = (None,
     (1,
      TType.STRING,
      'name',
      None,
      None),
     (2,
      TType.I32,
      'aclHandle',
      None,
      None),
     (3,
      TType.I32,
      'elemHandle',
      None,
      None),
     (4,
      TType.I32,
      'lifetime',
      None,
      None),
     (5,
      TType.I32,
      'addrFamily',
      None,
      None))

    def __init__(self, name = None, aclHandle = None, elemHandle = None, lifetime = None, addrFamily = None):
        self.name = name
        self.aclHandle = aclHandle
        self.elemHandle = elemHandle
        self.lifetime = lifetime
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
                if ftype == TType.STRING:
                    self.name = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.aclHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.elemHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.lifetime = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
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
        oprot.writeStructBegin('getNamedAceMatch_IDL_args')
        if self.name != None:
            oprot.writeFieldBegin('name', TType.STRING, 1)
            oprot.writeString(self.name)
            oprot.writeFieldEnd()
        if self.aclHandle != None:
            oprot.writeFieldBegin('aclHandle', TType.I32, 2)
            oprot.writeI32(self.aclHandle)
            oprot.writeFieldEnd()
        if self.elemHandle != None:
            oprot.writeFieldBegin('elemHandle', TType.I32, 3)
            oprot.writeI32(self.elemHandle)
            oprot.writeFieldEnd()
        if self.lifetime != None:
            oprot.writeFieldBegin('lifetime', TType.I32, 4)
            oprot.writeI32(self.lifetime)
            oprot.writeFieldEnd()
        if self.addrFamily != None:
            oprot.writeFieldBegin('addrFamily', TType.I32, 5)
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




class getNamedAceMatch_IDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.I64,
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
                if ftype == TType.I64:
                    self.success = iprot.readI64()
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
        oprot.writeStructBegin('getNamedAceMatch_IDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.I64, 0)
            oprot.writeI64(self.success)
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
# 2015.02.05 17:22:46 IST
