# 2015.02.05 17:22:11 IST
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

    def createPropVector_IDL(self, domain_id, policy_version, summary):
        """
            Create a Proposition Vector object
        
            Parameters:
             - domain_id
             - policy_version
             - summary
            """
        pass



    def destroyPropVector_IDL(self, domain_id, policy_version):
        """
            Destroy a Proposition Vector object
        
            Parameters:
             - domain_id
             - policy_version
            """
        pass



    def addPropToVector_IDL(self, domain_id, prop):
        """
            Add a Proposition to the Prop Vector object
        
            Parameters:
             - domain_id
             - prop
            """
        pass



    def removePropFromVector_IDL(self, domain_id, id):
        """
            Remove a Proposition from the Prop Vector object
        
            Parameters:
             - domain_id
             - id
            """
        pass



    def createTable_IDL(self, domain_id, type, table_id, policy_version, persist_id, combining_alg, table_hierarchy, tbl):
        """
            Create a Table object
        
            Parameters:
             - domain_id
             - type
             - table_id
             - policy_version
             - persist_id
             - combining_alg
             - table_hierarchy
             - tbl
            """
        pass



    def destroyTable_IDL(self, domain_id, table_id):
        """
            Destroy a Table object
        
            Parameters:
             - domain_id
             - table_id
            """
        pass



    def addRowToTable_IDL(self, domain_id, table_id, row):
        """
            Add a Row To Table object
        
            Parameters:
             - domain_id
             - table_id
             - row
            """
        pass



    def removeRowFromTable_IDL(self, domain_id, table_id, row_id):
        """
            Remove a Row From Table object
        
            Parameters:
             - domain_id
             - table_id
             - row_id
            """
        pass



    def policyInstall_IDL(self, domain_id, policy_version, config_version):
        """
            Install Policy
        
            Parameters:
             - domain_id
             - policy_version
             - config_version
            """
        pass



    def Capabilities_getCapList_IDL(self):
        """
        Get proposition Capabilities
        """
        pass



    def addFlowRule_IDL(self, flowRule):
        """
            addFlowRule_IDL
        
            Parameters:
             - flowRule
            """
        pass



    def load_nbar_pp_IDL(self, proto_pack):
        """
            Load Protocol Pack
        
            Parameters:
             - proto_pack
            """
        pass



    def add_AVC_group_IDL(self, type_id, apps):
        """
            Add an AVC group
        
            Parameters:
             - type_id
             - apps
            """
        pass



    def AVC_groups_complete_IDL(self, version):
        """
            AVC groups complete
        
            Parameters:
             - version
            """
        pass



    def add_AVC_IDL(self, name, unified_id, display_name, nbar_id):
        """
            Add an application
        
            Parameters:
             - name
             - unified_id
             - display_name
             - nbar_id
            """
        pass



    def AVC_complete_IDL(self, version):
        """
            AVC  complete
        
            Parameters:
             - version
            """
        pass



    def init_IDL(self):
        """
        Init
        """
        pass



    def deinit_IDL(self):
        """
        DeInit
        """
        pass



    def syslog_cfg_IDL(self, domain_id, enable, level, interval_len, msg_count):
        """
            Syslog cfg
        
            Parameters:
             - domain_id
             - enable
             - level
             - interval_len
             - msg_count
            """
        pass



    def domain_cfg_IDL(self, domain_id, events, syslog_chnl, dp_stats, dp_user_stats, pcap, appnav, wse_enabled, ips_enabled):
        """
            Domain configuration
        
            Parameters:
             - domain_id
             - events
             - syslog_chnl
             - dp_stats
             - dp_user_stats
             - pcap
             - appnav
             - wse_enabled
             - ips_enabled
            """
        pass



    def createIntfMapTable_IDL(self):
        """
        Create Interface Map Table
        """
        pass



    def destroyIntfMapTable_IDL(self):
        """
        Destroy Interface Map Table
        """
        pass



    def addIntfMapTable_IDL(self, intfMapTbl):
        """
            Add
        
            Parameters:
             - intfMapTbl
            """
        pass



    def add_AVC_list_IDL(self, avcObj):
        """
            Add AVC Object List
        
            Parameters:
             - avcObj
            """
        pass



    def add_AVC_group_list_IDL(self, avcGroupObj):
        """
            Add AVC Group Object List
        
            Parameters:
             - avcGroupObj
            """
        pass



    def get_IOSXE_Version_IDL(self):
        """
        Get IOSXE Version
        """
        pass



    def get_nbar_eng_Version_IDL(self):
        """
        Get NBAR Eng Version
        """
        pass



    def pcap_cfg_IDL(self, domain_id, capture_size, rl_interval_length, rl_packet_count, buffer_size, circular_buffer):
        """
            Packet capture cfg
        
            Parameters:
             - domain_id
             - capture_size
             - rl_interval_length
             - rl_packet_count
             - buffer_size
             - circular_buffer
            """
        pass



    def pcap_drop_capture_cfg_IDL(self, domain_id, enable):
        """
            Capture dropped packets cfg
        
            Parameters:
             - domain_id
             - enable
            """
        pass




class Client(Iface):

    def __init__(self, iprot, oprot = None):
        self._iprot = self._oprot = iprot
        if oprot != None:
            self._oprot = oprot
        self._seqid = 0



    def createPropVector_IDL(self, domain_id, policy_version, summary):
        """
            Create a Proposition Vector object
        
            Parameters:
             - domain_id
             - policy_version
             - summary
            """
        self._oprot.rlock.acquire()
        try:
            self.send_createPropVector_IDL(domain_id, policy_version, summary)
            result = self.recv_createPropVector_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_createPropVector_IDL(self, domain_id, policy_version, summary):
        self._oprot.writeMessageBegin('createPropVector_IDL', TMessageType.CALL, self._seqid)
        args = createPropVector_IDL_args()
        args.domain_id = domain_id
        args.policy_version = policy_version
        args.summary = summary
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_createPropVector_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = createPropVector_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'createPropVector_IDL failed: unknown result')



    def destroyPropVector_IDL(self, domain_id, policy_version):
        """
            Destroy a Proposition Vector object
        
            Parameters:
             - domain_id
             - policy_version
            """
        self._oprot.rlock.acquire()
        try:
            self.send_destroyPropVector_IDL(domain_id, policy_version)
            result = self.recv_destroyPropVector_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_destroyPropVector_IDL(self, domain_id, policy_version):
        self._oprot.writeMessageBegin('destroyPropVector_IDL', TMessageType.CALL, self._seqid)
        args = destroyPropVector_IDL_args()
        args.domain_id = domain_id
        args.policy_version = policy_version
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_destroyPropVector_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = destroyPropVector_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'destroyPropVector_IDL failed: unknown result')



    def addPropToVector_IDL(self, domain_id, prop):
        """
            Add a Proposition to the Prop Vector object
        
            Parameters:
             - domain_id
             - prop
            """
        self._oprot.rlock.acquire()
        try:
            self.send_addPropToVector_IDL(domain_id, prop)
            result = self.recv_addPropToVector_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_addPropToVector_IDL(self, domain_id, prop):
        self._oprot.writeMessageBegin('addPropToVector_IDL', TMessageType.CALL, self._seqid)
        args = addPropToVector_IDL_args()
        args.domain_id = domain_id
        args.prop = prop
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_addPropToVector_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = addPropToVector_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'addPropToVector_IDL failed: unknown result')



    def removePropFromVector_IDL(self, domain_id, id):
        """
            Remove a Proposition from the Prop Vector object
        
            Parameters:
             - domain_id
             - id
            """
        self._oprot.rlock.acquire()
        try:
            self.send_removePropFromVector_IDL(domain_id, id)
            result = self.recv_removePropFromVector_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_removePropFromVector_IDL(self, domain_id, id):
        self._oprot.writeMessageBegin('removePropFromVector_IDL', TMessageType.CALL, self._seqid)
        args = removePropFromVector_IDL_args()
        args.domain_id = domain_id
        args.id = id
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_removePropFromVector_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = removePropFromVector_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'removePropFromVector_IDL failed: unknown result')



    def createTable_IDL(self, domain_id, type, table_id, policy_version, persist_id, combining_alg, table_hierarchy, tbl):
        """
            Create a Table object
        
            Parameters:
             - domain_id
             - type
             - table_id
             - policy_version
             - persist_id
             - combining_alg
             - table_hierarchy
             - tbl
            """
        self._oprot.rlock.acquire()
        try:
            self.send_createTable_IDL(domain_id, type, table_id, policy_version, persist_id, combining_alg, table_hierarchy, tbl)
            result = self.recv_createTable_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_createTable_IDL(self, domain_id, type, table_id, policy_version, persist_id, combining_alg, table_hierarchy, tbl):
        self._oprot.writeMessageBegin('createTable_IDL', TMessageType.CALL, self._seqid)
        args = createTable_IDL_args()
        args.domain_id = domain_id
        args.type = type
        args.table_id = table_id
        args.policy_version = policy_version
        args.persist_id = persist_id
        args.combining_alg = combining_alg
        args.table_hierarchy = table_hierarchy
        args.tbl = tbl
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_createTable_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = createTable_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'createTable_IDL failed: unknown result')



    def destroyTable_IDL(self, domain_id, table_id):
        """
            Destroy a Table object
        
            Parameters:
             - domain_id
             - table_id
            """
        self._oprot.rlock.acquire()
        try:
            self.send_destroyTable_IDL(domain_id, table_id)
            result = self.recv_destroyTable_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_destroyTable_IDL(self, domain_id, table_id):
        self._oprot.writeMessageBegin('destroyTable_IDL', TMessageType.CALL, self._seqid)
        args = destroyTable_IDL_args()
        args.domain_id = domain_id
        args.table_id = table_id
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_destroyTable_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = destroyTable_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'destroyTable_IDL failed: unknown result')



    def addRowToTable_IDL(self, domain_id, table_id, row):
        """
            Add a Row To Table object
        
            Parameters:
             - domain_id
             - table_id
             - row
            """
        self._oprot.rlock.acquire()
        try:
            self.send_addRowToTable_IDL(domain_id, table_id, row)
            result = self.recv_addRowToTable_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_addRowToTable_IDL(self, domain_id, table_id, row):
        self._oprot.writeMessageBegin('addRowToTable_IDL', TMessageType.CALL, self._seqid)
        args = addRowToTable_IDL_args()
        args.domain_id = domain_id
        args.table_id = table_id
        args.row = row
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_addRowToTable_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = addRowToTable_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'addRowToTable_IDL failed: unknown result')



    def removeRowFromTable_IDL(self, domain_id, table_id, row_id):
        """
            Remove a Row From Table object
        
            Parameters:
             - domain_id
             - table_id
             - row_id
            """
        self._oprot.rlock.acquire()
        try:
            self.send_removeRowFromTable_IDL(domain_id, table_id, row_id)
            result = self.recv_removeRowFromTable_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_removeRowFromTable_IDL(self, domain_id, table_id, row_id):
        self._oprot.writeMessageBegin('removeRowFromTable_IDL', TMessageType.CALL, self._seqid)
        args = removeRowFromTable_IDL_args()
        args.domain_id = domain_id
        args.table_id = table_id
        args.row_id = row_id
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_removeRowFromTable_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = removeRowFromTable_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'removeRowFromTable_IDL failed: unknown result')



    def policyInstall_IDL(self, domain_id, policy_version, config_version):
        """
            Install Policy
        
            Parameters:
             - domain_id
             - policy_version
             - config_version
            """
        self._oprot.rlock.acquire()
        try:
            self.send_policyInstall_IDL(domain_id, policy_version, config_version)
            result = self.recv_policyInstall_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_policyInstall_IDL(self, domain_id, policy_version, config_version):
        self._oprot.writeMessageBegin('policyInstall_IDL', TMessageType.CALL, self._seqid)
        args = policyInstall_IDL_args()
        args.domain_id = domain_id
        args.policy_version = policy_version
        args.config_version = config_version
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_policyInstall_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = policyInstall_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'policyInstall_IDL failed: unknown result')



    def Capabilities_getCapList_IDL(self):
        """
        Get proposition Capabilities
        """
        self._oprot.rlock.acquire()
        try:
            self.send_Capabilities_getCapList_IDL()
            result = self.recv_Capabilities_getCapList_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_Capabilities_getCapList_IDL(self):
        self._oprot.writeMessageBegin('Capabilities_getCapList_IDL', TMessageType.CALL, self._seqid)
        args = Capabilities_getCapList_IDL_args()
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_Capabilities_getCapList_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = Capabilities_getCapList_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'Capabilities_getCapList_IDL failed: unknown result')



    def addFlowRule_IDL(self, flowRule):
        """
            addFlowRule_IDL
        
            Parameters:
             - flowRule
            """
        self._oprot.rlock.acquire()
        try:
            self.send_addFlowRule_IDL(flowRule)
            result = self.recv_addFlowRule_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_addFlowRule_IDL(self, flowRule):
        self._oprot.writeMessageBegin('addFlowRule_IDL', TMessageType.CALL, self._seqid)
        args = addFlowRule_IDL_args()
        args.flowRule = flowRule
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_addFlowRule_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = addFlowRule_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'addFlowRule_IDL failed: unknown result')



    def load_nbar_pp_IDL(self, proto_pack):
        """
            Load Protocol Pack
        
            Parameters:
             - proto_pack
            """
        self._oprot.rlock.acquire()
        try:
            self.send_load_nbar_pp_IDL(proto_pack)
            result = self.recv_load_nbar_pp_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_load_nbar_pp_IDL(self, proto_pack):
        self._oprot.writeMessageBegin('load_nbar_pp_IDL', TMessageType.CALL, self._seqid)
        args = load_nbar_pp_IDL_args()
        args.proto_pack = proto_pack
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_load_nbar_pp_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = load_nbar_pp_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'load_nbar_pp_IDL failed: unknown result')



    def add_AVC_group_IDL(self, type_id, apps):
        """
            Add an AVC group
        
            Parameters:
             - type_id
             - apps
            """
        self._oprot.rlock.acquire()
        try:
            self.send_add_AVC_group_IDL(type_id, apps)
            result = self.recv_add_AVC_group_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_add_AVC_group_IDL(self, type_id, apps):
        self._oprot.writeMessageBegin('add_AVC_group_IDL', TMessageType.CALL, self._seqid)
        args = add_AVC_group_IDL_args()
        args.type_id = type_id
        args.apps = apps
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_add_AVC_group_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = add_AVC_group_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'add_AVC_group_IDL failed: unknown result')



    def AVC_groups_complete_IDL(self, version):
        """
            AVC groups complete
        
            Parameters:
             - version
            """
        self._oprot.rlock.acquire()
        try:
            self.send_AVC_groups_complete_IDL(version)
            result = self.recv_AVC_groups_complete_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_AVC_groups_complete_IDL(self, version):
        self._oprot.writeMessageBegin('AVC_groups_complete_IDL', TMessageType.CALL, self._seqid)
        args = AVC_groups_complete_IDL_args()
        args.version = version
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_AVC_groups_complete_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = AVC_groups_complete_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'AVC_groups_complete_IDL failed: unknown result')



    def add_AVC_IDL(self, name, unified_id, display_name, nbar_id):
        """
            Add an application
        
            Parameters:
             - name
             - unified_id
             - display_name
             - nbar_id
            """
        self._oprot.rlock.acquire()
        try:
            self.send_add_AVC_IDL(name, unified_id, display_name, nbar_id)
            result = self.recv_add_AVC_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_add_AVC_IDL(self, name, unified_id, display_name, nbar_id):
        self._oprot.writeMessageBegin('add_AVC_IDL', TMessageType.CALL, self._seqid)
        args = add_AVC_IDL_args()
        args.name = name
        args.unified_id = unified_id
        args.display_name = display_name
        args.nbar_id = nbar_id
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_add_AVC_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = add_AVC_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'add_AVC_IDL failed: unknown result')



    def AVC_complete_IDL(self, version):
        """
            AVC  complete
        
            Parameters:
             - version
            """
        self._oprot.rlock.acquire()
        try:
            self.send_AVC_complete_IDL(version)
            result = self.recv_AVC_complete_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_AVC_complete_IDL(self, version):
        self._oprot.writeMessageBegin('AVC_complete_IDL', TMessageType.CALL, self._seqid)
        args = AVC_complete_IDL_args()
        args.version = version
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_AVC_complete_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = AVC_complete_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'AVC_complete_IDL failed: unknown result')



    def init_IDL(self):
        """
        Init
        """
        self._oprot.rlock.acquire()
        try:
            self.send_init_IDL()
            result = self.recv_init_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_init_IDL(self):
        self._oprot.writeMessageBegin('init_IDL', TMessageType.CALL, self._seqid)
        args = init_IDL_args()
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_init_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = init_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'init_IDL failed: unknown result')



    def deinit_IDL(self):
        """
        DeInit
        """
        self._oprot.rlock.acquire()
        try:
            self.send_deinit_IDL()
            result = self.recv_deinit_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_deinit_IDL(self):
        self._oprot.writeMessageBegin('deinit_IDL', TMessageType.CALL, self._seqid)
        args = deinit_IDL_args()
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_deinit_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = deinit_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'deinit_IDL failed: unknown result')



    def syslog_cfg_IDL(self, domain_id, enable, level, interval_len, msg_count):
        """
            Syslog cfg
        
            Parameters:
             - domain_id
             - enable
             - level
             - interval_len
             - msg_count
            """
        self._oprot.rlock.acquire()
        try:
            self.send_syslog_cfg_IDL(domain_id, enable, level, interval_len, msg_count)
            result = self.recv_syslog_cfg_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_syslog_cfg_IDL(self, domain_id, enable, level, interval_len, msg_count):
        self._oprot.writeMessageBegin('syslog_cfg_IDL', TMessageType.CALL, self._seqid)
        args = syslog_cfg_IDL_args()
        args.domain_id = domain_id
        args.enable = enable
        args.level = level
        args.interval_len = interval_len
        args.msg_count = msg_count
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_syslog_cfg_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = syslog_cfg_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'syslog_cfg_IDL failed: unknown result')



    def domain_cfg_IDL(self, domain_id, events, syslog_chnl, dp_stats, dp_user_stats, pcap, appnav, wse_enabled, ips_enabled):
        """
            Domain configuration
        
            Parameters:
             - domain_id
             - events
             - syslog_chnl
             - dp_stats
             - dp_user_stats
             - pcap
             - appnav
             - wse_enabled
             - ips_enabled
            """
        self._oprot.rlock.acquire()
        try:
            self.send_domain_cfg_IDL(domain_id, events, syslog_chnl, dp_stats, dp_user_stats, pcap, appnav, wse_enabled, ips_enabled)
            result = self.recv_domain_cfg_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_domain_cfg_IDL(self, domain_id, events, syslog_chnl, dp_stats, dp_user_stats, pcap, appnav, wse_enabled, ips_enabled):
        self._oprot.writeMessageBegin('domain_cfg_IDL', TMessageType.CALL, self._seqid)
        args = domain_cfg_IDL_args()
        args.domain_id = domain_id
        args.events = events
        args.syslog_chnl = syslog_chnl
        args.dp_stats = dp_stats
        args.dp_user_stats = dp_user_stats
        args.pcap = pcap
        args.appnav = appnav
        args.wse_enabled = wse_enabled
        args.ips_enabled = ips_enabled
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_domain_cfg_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = domain_cfg_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'domain_cfg_IDL failed: unknown result')



    def createIntfMapTable_IDL(self):
        """
        Create Interface Map Table
        """
        self._oprot.rlock.acquire()
        try:
            self.send_createIntfMapTable_IDL()
            result = self.recv_createIntfMapTable_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_createIntfMapTable_IDL(self):
        self._oprot.writeMessageBegin('createIntfMapTable_IDL', TMessageType.CALL, self._seqid)
        args = createIntfMapTable_IDL_args()
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_createIntfMapTable_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = createIntfMapTable_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'createIntfMapTable_IDL failed: unknown result')



    def destroyIntfMapTable_IDL(self):
        """
        Destroy Interface Map Table
        """
        self._oprot.rlock.acquire()
        try:
            self.send_destroyIntfMapTable_IDL()
            result = self.recv_destroyIntfMapTable_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_destroyIntfMapTable_IDL(self):
        self._oprot.writeMessageBegin('destroyIntfMapTable_IDL', TMessageType.CALL, self._seqid)
        args = destroyIntfMapTable_IDL_args()
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_destroyIntfMapTable_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = destroyIntfMapTable_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'destroyIntfMapTable_IDL failed: unknown result')



    def addIntfMapTable_IDL(self, intfMapTbl):
        """
            Add
        
            Parameters:
             - intfMapTbl
            """
        self._oprot.rlock.acquire()
        try:
            self.send_addIntfMapTable_IDL(intfMapTbl)
            result = self.recv_addIntfMapTable_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_addIntfMapTable_IDL(self, intfMapTbl):
        self._oprot.writeMessageBegin('addIntfMapTable_IDL', TMessageType.CALL, self._seqid)
        args = addIntfMapTable_IDL_args()
        args.intfMapTbl = intfMapTbl
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_addIntfMapTable_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = addIntfMapTable_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'addIntfMapTable_IDL failed: unknown result')



    def add_AVC_list_IDL(self, avcObj):
        """
            Add AVC Object List
        
            Parameters:
             - avcObj
            """
        self._oprot.rlock.acquire()
        try:
            self.send_add_AVC_list_IDL(avcObj)
            result = self.recv_add_AVC_list_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_add_AVC_list_IDL(self, avcObj):
        self._oprot.writeMessageBegin('add_AVC_list_IDL', TMessageType.CALL, self._seqid)
        args = add_AVC_list_IDL_args()
        args.avcObj = avcObj
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_add_AVC_list_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = add_AVC_list_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'add_AVC_list_IDL failed: unknown result')



    def add_AVC_group_list_IDL(self, avcGroupObj):
        """
            Add AVC Group Object List
        
            Parameters:
             - avcGroupObj
            """
        self._oprot.rlock.acquire()
        try:
            self.send_add_AVC_group_list_IDL(avcGroupObj)
            result = self.recv_add_AVC_group_list_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_add_AVC_group_list_IDL(self, avcGroupObj):
        self._oprot.writeMessageBegin('add_AVC_group_list_IDL', TMessageType.CALL, self._seqid)
        args = add_AVC_group_list_IDL_args()
        args.avcGroupObj = avcGroupObj
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_add_AVC_group_list_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = add_AVC_group_list_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'add_AVC_group_list_IDL failed: unknown result')



    def get_IOSXE_Version_IDL(self):
        """
        Get IOSXE Version
        """
        self._oprot.rlock.acquire()
        try:
            self.send_get_IOSXE_Version_IDL()
            result = self.recv_get_IOSXE_Version_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_get_IOSXE_Version_IDL(self):
        self._oprot.writeMessageBegin('get_IOSXE_Version_IDL', TMessageType.CALL, self._seqid)
        args = get_IOSXE_Version_IDL_args()
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_get_IOSXE_Version_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = get_IOSXE_Version_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'get_IOSXE_Version_IDL failed: unknown result')



    def get_nbar_eng_Version_IDL(self):
        """
        Get NBAR Eng Version
        """
        self._oprot.rlock.acquire()
        try:
            self.send_get_nbar_eng_Version_IDL()
            result = self.recv_get_nbar_eng_Version_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_get_nbar_eng_Version_IDL(self):
        self._oprot.writeMessageBegin('get_nbar_eng_Version_IDL', TMessageType.CALL, self._seqid)
        args = get_nbar_eng_Version_IDL_args()
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_get_nbar_eng_Version_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = get_nbar_eng_Version_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'get_nbar_eng_Version_IDL failed: unknown result')



    def pcap_cfg_IDL(self, domain_id, capture_size, rl_interval_length, rl_packet_count, buffer_size, circular_buffer):
        """
            Packet capture cfg
        
            Parameters:
             - domain_id
             - capture_size
             - rl_interval_length
             - rl_packet_count
             - buffer_size
             - circular_buffer
            """
        self._oprot.rlock.acquire()
        try:
            self.send_pcap_cfg_IDL(domain_id, capture_size, rl_interval_length, rl_packet_count, buffer_size, circular_buffer)
            result = self.recv_pcap_cfg_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_pcap_cfg_IDL(self, domain_id, capture_size, rl_interval_length, rl_packet_count, buffer_size, circular_buffer):
        self._oprot.writeMessageBegin('pcap_cfg_IDL', TMessageType.CALL, self._seqid)
        args = pcap_cfg_IDL_args()
        args.domain_id = domain_id
        args.capture_size = capture_size
        args.rl_interval_length = rl_interval_length
        args.rl_packet_count = rl_packet_count
        args.buffer_size = buffer_size
        args.circular_buffer = circular_buffer
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_pcap_cfg_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = pcap_cfg_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'pcap_cfg_IDL failed: unknown result')



    def pcap_drop_capture_cfg_IDL(self, domain_id, enable):
        """
            Capture dropped packets cfg
        
            Parameters:
             - domain_id
             - enable
            """
        self._oprot.rlock.acquire()
        try:
            self.send_pcap_drop_capture_cfg_IDL(domain_id, enable)
            result = self.recv_pcap_drop_capture_cfg_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_pcap_drop_capture_cfg_IDL(self, domain_id, enable):
        self._oprot.writeMessageBegin('pcap_drop_capture_cfg_IDL', TMessageType.CALL, self._seqid)
        args = pcap_drop_capture_cfg_IDL_args()
        args.domain_id = domain_id
        args.enable = enable
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_pcap_drop_capture_cfg_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = pcap_drop_capture_cfg_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'pcap_drop_capture_cfg_IDL failed: unknown result')




class Processor(Iface, TProcessor):

    def __init__(self, handler):
        self._handler = handler
        self._processMap = {}
        self._processMap['createPropVector_IDL'] = Processor.process_createPropVector_IDL
        self._processMap['destroyPropVector_IDL'] = Processor.process_destroyPropVector_IDL
        self._processMap['addPropToVector_IDL'] = Processor.process_addPropToVector_IDL
        self._processMap['removePropFromVector_IDL'] = Processor.process_removePropFromVector_IDL
        self._processMap['createTable_IDL'] = Processor.process_createTable_IDL
        self._processMap['destroyTable_IDL'] = Processor.process_destroyTable_IDL
        self._processMap['addRowToTable_IDL'] = Processor.process_addRowToTable_IDL
        self._processMap['removeRowFromTable_IDL'] = Processor.process_removeRowFromTable_IDL
        self._processMap['policyInstall_IDL'] = Processor.process_policyInstall_IDL
        self._processMap['Capabilities_getCapList_IDL'] = Processor.process_Capabilities_getCapList_IDL
        self._processMap['addFlowRule_IDL'] = Processor.process_addFlowRule_IDL
        self._processMap['load_nbar_pp_IDL'] = Processor.process_load_nbar_pp_IDL
        self._processMap['add_AVC_group_IDL'] = Processor.process_add_AVC_group_IDL
        self._processMap['AVC_groups_complete_IDL'] = Processor.process_AVC_groups_complete_IDL
        self._processMap['add_AVC_IDL'] = Processor.process_add_AVC_IDL
        self._processMap['AVC_complete_IDL'] = Processor.process_AVC_complete_IDL
        self._processMap['init_IDL'] = Processor.process_init_IDL
        self._processMap['deinit_IDL'] = Processor.process_deinit_IDL
        self._processMap['syslog_cfg_IDL'] = Processor.process_syslog_cfg_IDL
        self._processMap['domain_cfg_IDL'] = Processor.process_domain_cfg_IDL
        self._processMap['createIntfMapTable_IDL'] = Processor.process_createIntfMapTable_IDL
        self._processMap['destroyIntfMapTable_IDL'] = Processor.process_destroyIntfMapTable_IDL
        self._processMap['addIntfMapTable_IDL'] = Processor.process_addIntfMapTable_IDL
        self._processMap['add_AVC_list_IDL'] = Processor.process_add_AVC_list_IDL
        self._processMap['add_AVC_group_list_IDL'] = Processor.process_add_AVC_group_list_IDL
        self._processMap['get_IOSXE_Version_IDL'] = Processor.process_get_IOSXE_Version_IDL
        self._processMap['get_nbar_eng_Version_IDL'] = Processor.process_get_nbar_eng_Version_IDL
        self._processMap['pcap_cfg_IDL'] = Processor.process_pcap_cfg_IDL
        self._processMap['pcap_drop_capture_cfg_IDL'] = Processor.process_pcap_drop_capture_cfg_IDL



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



    def process_createPropVector_IDL(self, seqid, iprot, oprot):
        args = createPropVector_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = createPropVector_IDL_result()
        try:
            result.success = self._handler.createPropVector_IDL(args.domain_id, args.policy_version, args.summary)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('createPropVector_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_destroyPropVector_IDL(self, seqid, iprot, oprot):
        args = destroyPropVector_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = destroyPropVector_IDL_result()
        try:
            result.success = self._handler.destroyPropVector_IDL(args.domain_id, args.policy_version)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('destroyPropVector_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_addPropToVector_IDL(self, seqid, iprot, oprot):
        args = addPropToVector_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = addPropToVector_IDL_result()
        try:
            result.success = self._handler.addPropToVector_IDL(args.domain_id, args.prop)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('addPropToVector_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_removePropFromVector_IDL(self, seqid, iprot, oprot):
        args = removePropFromVector_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = removePropFromVector_IDL_result()
        try:
            result.success = self._handler.removePropFromVector_IDL(args.domain_id, args.id)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('removePropFromVector_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_createTable_IDL(self, seqid, iprot, oprot):
        args = createTable_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = createTable_IDL_result()
        try:
            result.success = self._handler.createTable_IDL(args.domain_id, args.type, args.table_id, args.policy_version, args.persist_id, args.combining_alg, args.table_hierarchy, args.tbl)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('createTable_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_destroyTable_IDL(self, seqid, iprot, oprot):
        args = destroyTable_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = destroyTable_IDL_result()
        try:
            result.success = self._handler.destroyTable_IDL(args.domain_id, args.table_id)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('destroyTable_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_addRowToTable_IDL(self, seqid, iprot, oprot):
        args = addRowToTable_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = addRowToTable_IDL_result()
        try:
            result.success = self._handler.addRowToTable_IDL(args.domain_id, args.table_id, args.row)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('addRowToTable_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_removeRowFromTable_IDL(self, seqid, iprot, oprot):
        args = removeRowFromTable_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = removeRowFromTable_IDL_result()
        try:
            result.success = self._handler.removeRowFromTable_IDL(args.domain_id, args.table_id, args.row_id)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('removeRowFromTable_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_policyInstall_IDL(self, seqid, iprot, oprot):
        args = policyInstall_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = policyInstall_IDL_result()
        try:
            result.success = self._handler.policyInstall_IDL(args.domain_id, args.policy_version, args.config_version)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('policyInstall_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_Capabilities_getCapList_IDL(self, seqid, iprot, oprot):
        args = Capabilities_getCapList_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = Capabilities_getCapList_IDL_result()
        try:
            result.success = self._handler.Capabilities_getCapList_IDL()
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('Capabilities_getCapList_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_addFlowRule_IDL(self, seqid, iprot, oprot):
        args = addFlowRule_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = addFlowRule_IDL_result()
        try:
            result.success = self._handler.addFlowRule_IDL(args.flowRule)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('addFlowRule_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_load_nbar_pp_IDL(self, seqid, iprot, oprot):
        args = load_nbar_pp_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = load_nbar_pp_IDL_result()
        try:
            result.success = self._handler.load_nbar_pp_IDL(args.proto_pack)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('load_nbar_pp_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_add_AVC_group_IDL(self, seqid, iprot, oprot):
        args = add_AVC_group_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = add_AVC_group_IDL_result()
        try:
            result.success = self._handler.add_AVC_group_IDL(args.type_id, args.apps)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('add_AVC_group_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_AVC_groups_complete_IDL(self, seqid, iprot, oprot):
        args = AVC_groups_complete_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = AVC_groups_complete_IDL_result()
        try:
            result.success = self._handler.AVC_groups_complete_IDL(args.version)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('AVC_groups_complete_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_add_AVC_IDL(self, seqid, iprot, oprot):
        args = add_AVC_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = add_AVC_IDL_result()
        try:
            result.success = self._handler.add_AVC_IDL(args.name, args.unified_id, args.display_name, args.nbar_id)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('add_AVC_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_AVC_complete_IDL(self, seqid, iprot, oprot):
        args = AVC_complete_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = AVC_complete_IDL_result()
        try:
            result.success = self._handler.AVC_complete_IDL(args.version)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('AVC_complete_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_init_IDL(self, seqid, iprot, oprot):
        args = init_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = init_IDL_result()
        try:
            result.success = self._handler.init_IDL()
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('init_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_deinit_IDL(self, seqid, iprot, oprot):
        args = deinit_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = deinit_IDL_result()
        try:
            result.success = self._handler.deinit_IDL()
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('deinit_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_syslog_cfg_IDL(self, seqid, iprot, oprot):
        args = syslog_cfg_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = syslog_cfg_IDL_result()
        try:
            result.success = self._handler.syslog_cfg_IDL(args.domain_id, args.enable, args.level, args.interval_len, args.msg_count)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('syslog_cfg_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_domain_cfg_IDL(self, seqid, iprot, oprot):
        args = domain_cfg_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = domain_cfg_IDL_result()
        try:
            result.success = self._handler.domain_cfg_IDL(args.domain_id, args.events, args.syslog_chnl, args.dp_stats, args.dp_user_stats, args.pcap, args.appnav, args.wse_enabled, args.ips_enabled)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('domain_cfg_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_createIntfMapTable_IDL(self, seqid, iprot, oprot):
        args = createIntfMapTable_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = createIntfMapTable_IDL_result()
        try:
            result.success = self._handler.createIntfMapTable_IDL()
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('createIntfMapTable_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_destroyIntfMapTable_IDL(self, seqid, iprot, oprot):
        args = destroyIntfMapTable_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = destroyIntfMapTable_IDL_result()
        try:
            result.success = self._handler.destroyIntfMapTable_IDL()
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('destroyIntfMapTable_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_addIntfMapTable_IDL(self, seqid, iprot, oprot):
        args = addIntfMapTable_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = addIntfMapTable_IDL_result()
        try:
            result.success = self._handler.addIntfMapTable_IDL(args.intfMapTbl)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('addIntfMapTable_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_add_AVC_list_IDL(self, seqid, iprot, oprot):
        args = add_AVC_list_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = add_AVC_list_IDL_result()
        try:
            result.success = self._handler.add_AVC_list_IDL(args.avcObj)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('add_AVC_list_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_add_AVC_group_list_IDL(self, seqid, iprot, oprot):
        args = add_AVC_group_list_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = add_AVC_group_list_IDL_result()
        try:
            result.success = self._handler.add_AVC_group_list_IDL(args.avcGroupObj)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('add_AVC_group_list_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_get_IOSXE_Version_IDL(self, seqid, iprot, oprot):
        args = get_IOSXE_Version_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = get_IOSXE_Version_IDL_result()
        try:
            result.success = self._handler.get_IOSXE_Version_IDL()
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('get_IOSXE_Version_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_get_nbar_eng_Version_IDL(self, seqid, iprot, oprot):
        args = get_nbar_eng_Version_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = get_nbar_eng_Version_IDL_result()
        try:
            result.success = self._handler.get_nbar_eng_Version_IDL()
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('get_nbar_eng_Version_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_pcap_cfg_IDL(self, seqid, iprot, oprot):
        args = pcap_cfg_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = pcap_cfg_IDL_result()
        try:
            result.success = self._handler.pcap_cfg_IDL(args.domain_id, args.capture_size, args.rl_interval_length, args.rl_packet_count, args.buffer_size, args.circular_buffer)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('pcap_cfg_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_pcap_drop_capture_cfg_IDL(self, seqid, iprot, oprot):
        args = pcap_drop_capture_cfg_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = pcap_drop_capture_cfg_IDL_result()
        try:
            result.success = self._handler.pcap_drop_capture_cfg_IDL(args.domain_id, args.enable)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('pcap_drop_capture_cfg_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()




class createPropVector_IDL_args(object):
    """
    Attributes:
     - domain_id
     - policy_version
     - summary
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'domain_id',
      None,
      None),
     (2,
      TType.I64,
      'policy_version',
      None,
      None),
     (3,
      TType.STRUCT,
      'summary',
      (PropositionSummary_IDL, PropositionSummary_IDL.thrift_spec),
      None))

    def __init__(self, domain_id = None, policy_version = None, summary = None):
        self.domain_id = domain_id
        self.policy_version = policy_version
        self.summary = summary



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
                    self.domain_id = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.policy_version = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRUCT:
                    self.summary = PropositionSummary_IDL()
                    self.summary.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()

        iprot.readStructEnd()



    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return 
        oprot.writeStructBegin('createPropVector_IDL_args')
        if self.domain_id != None:
            oprot.writeFieldBegin('domain_id', TType.I32, 1)
            oprot.writeI32(self.domain_id)
            oprot.writeFieldEnd()
        if self.policy_version != None:
            oprot.writeFieldBegin('policy_version', TType.I64, 2)
            oprot.writeI64(self.policy_version)
            oprot.writeFieldEnd()
        if self.summary != None:
            oprot.writeFieldBegin('summary', TType.STRUCT, 3)
            self.summary.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

        def validate(self):
            pass





    def __repr__(self):
        L = [ '%s=%r' % (key, value) for (key, value,) in self.__dict__.iteritems() ]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))



    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__



    def __ne__(self, other):
        return not self == other




class createPropVector_IDL_result(object):
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
        oprot.writeStructBegin('createPropVector_IDL_result')
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




class destroyPropVector_IDL_args(object):
    """
    Attributes:
     - domain_id
     - policy_version
    """

    thrift_spec = (None, (1,
      TType.I32,
      'domain_id',
      None,
      None), (2,
      TType.I64,
      'policy_version',
      None,
      None))

    def __init__(self, domain_id = None, policy_version = None):
        self.domain_id = domain_id
        self.policy_version = policy_version



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
                    self.domain_id = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.policy_version = iprot.readI64()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()

        iprot.readStructEnd()



    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return 
        oprot.writeStructBegin('destroyPropVector_IDL_args')
        if self.domain_id != None:
            oprot.writeFieldBegin('domain_id', TType.I32, 1)
            oprot.writeI32(self.domain_id)
            oprot.writeFieldEnd()
        if self.policy_version != None:
            oprot.writeFieldBegin('policy_version', TType.I64, 2)
            oprot.writeI64(self.policy_version)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

        def validate(self):
            pass





    def __repr__(self):
        L = [ '%s=%r' % (key, value) for (key, value,) in self.__dict__.iteritems() ]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))



    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__



    def __ne__(self, other):
        return not self == other




class destroyPropVector_IDL_result(object):
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
        oprot.writeStructBegin('destroyPropVector_IDL_result')
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




class addPropToVector_IDL_args(object):
    """
    Attributes:
     - domain_id
     - prop
    """

    thrift_spec = (None, (1,
      TType.I32,
      'domain_id',
      None,
      None), (2,
      TType.STRUCT,
      'prop',
      (Proposition_IDL, Proposition_IDL.thrift_spec),
      None))

    def __init__(self, domain_id = None, prop = None):
        self.domain_id = domain_id
        self.prop = prop



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
                    self.domain_id = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.prop = Proposition_IDL()
                    self.prop.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()

        iprot.readStructEnd()



    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return 
        oprot.writeStructBegin('addPropToVector_IDL_args')
        if self.domain_id != None:
            oprot.writeFieldBegin('domain_id', TType.I32, 1)
            oprot.writeI32(self.domain_id)
            oprot.writeFieldEnd()
        if self.prop != None:
            oprot.writeFieldBegin('prop', TType.STRUCT, 2)
            self.prop.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

        def validate(self):
            pass





    def __repr__(self):
        L = [ '%s=%r' % (key, value) for (key, value,) in self.__dict__.iteritems() ]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))



    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__



    def __ne__(self, other):
        return not self == other




class addPropToVector_IDL_result(object):
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
        oprot.writeStructBegin('addPropToVector_IDL_result')
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




class removePropFromVector_IDL_args(object):
    """
    Attributes:
     - domain_id
     - id
    """

    thrift_spec = (None, (1,
      TType.I32,
      'domain_id',
      None,
      None), (2,
      TType.I32,
      'id',
      None,
      None))

    def __init__(self, domain_id = None, id = None):
        self.domain_id = domain_id
        self.id = id



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
                    self.domain_id = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.id = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()

        iprot.readStructEnd()



    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return 
        oprot.writeStructBegin('removePropFromVector_IDL_args')
        if self.domain_id != None:
            oprot.writeFieldBegin('domain_id', TType.I32, 1)
            oprot.writeI32(self.domain_id)
            oprot.writeFieldEnd()
        if self.id != None:
            oprot.writeFieldBegin('id', TType.I32, 2)
            oprot.writeI32(self.id)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

        def validate(self):
            pass





    def __repr__(self):
        L = [ '%s=%r' % (key, value) for (key, value,) in self.__dict__.iteritems() ]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))



    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__



    def __ne__(self, other):
        return not self == other




class removePropFromVector_IDL_result(object):
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
        oprot.writeStructBegin('removePropFromVector_IDL_result')
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




class createTable_IDL_args(object):
    """
    Attributes:
     - domain_id
     - type
     - table_id
     - policy_version
     - persist_id
     - combining_alg
     - table_hierarchy
     - tbl
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'domain_id',
      None,
      None),
     (2,
      TType.I32,
      'type',
      None,
      None),
     (3,
      TType.I32,
      'table_id',
      None,
      None),
     (4,
      TType.I64,
      'policy_version',
      None,
      None),
     (5,
      TType.I64,
      'persist_id',
      None,
      None),
     (6,
      TType.I32,
      'combining_alg',
      None,
      None),
     (7,
      TType.I32,
      'table_hierarchy',
      None,
      None),
     (8,
      TType.STRUCT,
      'tbl',
      (Table_IDL, Table_IDL.thrift_spec),
      None))

    def __init__(self, domain_id = None, type = None, table_id = None, policy_version = None, persist_id = None, combining_alg = None, table_hierarchy = None, tbl = None):
        self.domain_id = domain_id
        self.type = type
        self.table_id = table_id
        self.policy_version = policy_version
        self.persist_id = persist_id
        self.combining_alg = combining_alg
        self.table_hierarchy = table_hierarchy
        self.tbl = tbl



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
                    self.domain_id = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.table_id = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I64:
                    self.policy_version = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I64:
                    self.persist_id = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I32:
                    self.combining_alg = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I32:
                    self.table_hierarchy = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.STRUCT:
                    self.tbl = Table_IDL()
                    self.tbl.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()

        iprot.readStructEnd()



    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return 
        oprot.writeStructBegin('createTable_IDL_args')
        if self.domain_id != None:
            oprot.writeFieldBegin('domain_id', TType.I32, 1)
            oprot.writeI32(self.domain_id)
            oprot.writeFieldEnd()
        if self.type != None:
            oprot.writeFieldBegin('type', TType.I32, 2)
            oprot.writeI32(self.type)
            oprot.writeFieldEnd()
        if self.table_id != None:
            oprot.writeFieldBegin('table_id', TType.I32, 3)
            oprot.writeI32(self.table_id)
            oprot.writeFieldEnd()
        if self.policy_version != None:
            oprot.writeFieldBegin('policy_version', TType.I64, 4)
            oprot.writeI64(self.policy_version)
            oprot.writeFieldEnd()
        if self.persist_id != None:
            oprot.writeFieldBegin('persist_id', TType.I64, 5)
            oprot.writeI64(self.persist_id)
            oprot.writeFieldEnd()
        if self.combining_alg != None:
            oprot.writeFieldBegin('combining_alg', TType.I32, 6)
            oprot.writeI32(self.combining_alg)
            oprot.writeFieldEnd()
        if self.table_hierarchy != None:
            oprot.writeFieldBegin('table_hierarchy', TType.I32, 7)
            oprot.writeI32(self.table_hierarchy)
            oprot.writeFieldEnd()
        if self.tbl != None:
            oprot.writeFieldBegin('tbl', TType.STRUCT, 8)
            self.tbl.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

        def validate(self):
            pass





    def __repr__(self):
        L = [ '%s=%r' % (key, value) for (key, value,) in self.__dict__.iteritems() ]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))



    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__



    def __ne__(self, other):
        return not self == other




class createTable_IDL_result(object):
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
        oprot.writeStructBegin('createTable_IDL_result')
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




class destroyTable_IDL_args(object):
    """
    Attributes:
     - domain_id
     - table_id
    """

    thrift_spec = (None, (1,
      TType.I32,
      'domain_id',
      None,
      None), (2,
      TType.I32,
      'table_id',
      None,
      None))

    def __init__(self, domain_id = None, table_id = None):
        self.domain_id = domain_id
        self.table_id = table_id



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
                    self.domain_id = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.table_id = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()

        iprot.readStructEnd()



    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return 
        oprot.writeStructBegin('destroyTable_IDL_args')
        if self.domain_id != None:
            oprot.writeFieldBegin('domain_id', TType.I32, 1)
            oprot.writeI32(self.domain_id)
            oprot.writeFieldEnd()
        if self.table_id != None:
            oprot.writeFieldBegin('table_id', TType.I32, 2)
            oprot.writeI32(self.table_id)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

        def validate(self):
            pass





    def __repr__(self):
        L = [ '%s=%r' % (key, value) for (key, value,) in self.__dict__.iteritems() ]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))



    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__



    def __ne__(self, other):
        return not self == other




class destroyTable_IDL_result(object):
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
        oprot.writeStructBegin('destroyTable_IDL_result')
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




class addRowToTable_IDL_args(object):
    """
    Attributes:
     - domain_id
     - table_id
     - row
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'domain_id',
      None,
      None),
     (2,
      TType.I32,
      'table_id',
      None,
      None),
     (3,
      TType.STRUCT,
      'row',
      (Row_IDL, Row_IDL.thrift_spec),
      None))

    def __init__(self, domain_id = None, table_id = None, row = None):
        self.domain_id = domain_id
        self.table_id = table_id
        self.row = row



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
                    self.domain_id = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.table_id = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRUCT:
                    self.row = Row_IDL()
                    self.row.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()

        iprot.readStructEnd()



    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return 
        oprot.writeStructBegin('addRowToTable_IDL_args')
        if self.domain_id != None:
            oprot.writeFieldBegin('domain_id', TType.I32, 1)
            oprot.writeI32(self.domain_id)
            oprot.writeFieldEnd()
        if self.table_id != None:
            oprot.writeFieldBegin('table_id', TType.I32, 2)
            oprot.writeI32(self.table_id)
            oprot.writeFieldEnd()
        if self.row != None:
            oprot.writeFieldBegin('row', TType.STRUCT, 3)
            self.row.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

        def validate(self):
            pass





    def __repr__(self):
        L = [ '%s=%r' % (key, value) for (key, value,) in self.__dict__.iteritems() ]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))



    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__



    def __ne__(self, other):
        return not self == other




class addRowToTable_IDL_result(object):
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
        oprot.writeStructBegin('addRowToTable_IDL_result')
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




class removeRowFromTable_IDL_args(object):
    """
    Attributes:
     - domain_id
     - table_id
     - row_id
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'domain_id',
      None,
      None),
     (2,
      TType.I32,
      'table_id',
      None,
      None),
     (3,
      TType.I32,
      'row_id',
      None,
      None))

    def __init__(self, domain_id = None, table_id = None, row_id = None):
        self.domain_id = domain_id
        self.table_id = table_id
        self.row_id = row_id



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
                    self.domain_id = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.table_id = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.row_id = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()

        iprot.readStructEnd()



    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return 
        oprot.writeStructBegin('removeRowFromTable_IDL_args')
        if self.domain_id != None:
            oprot.writeFieldBegin('domain_id', TType.I32, 1)
            oprot.writeI32(self.domain_id)
            oprot.writeFieldEnd()
        if self.table_id != None:
            oprot.writeFieldBegin('table_id', TType.I32, 2)
            oprot.writeI32(self.table_id)
            oprot.writeFieldEnd()
        if self.row_id != None:
            oprot.writeFieldBegin('row_id', TType.I32, 3)
            oprot.writeI32(self.row_id)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

        def validate(self):
            pass





    def __repr__(self):
        L = [ '%s=%r' % (key, value) for (key, value,) in self.__dict__.iteritems() ]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))



    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__



    def __ne__(self, other):
        return not self == other




class removeRowFromTable_IDL_result(object):
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
        oprot.writeStructBegin('removeRowFromTable_IDL_result')
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




class policyInstall_IDL_args(object):
    """
    Attributes:
     - domain_id
     - policy_version
     - config_version
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'domain_id',
      None,
      None),
     (2,
      TType.I64,
      'policy_version',
      None,
      None),
     (3,
      TType.I64,
      'config_version',
      None,
      None))

    def __init__(self, domain_id = None, policy_version = None, config_version = None):
        self.domain_id = domain_id
        self.policy_version = policy_version
        self.config_version = config_version



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
                    self.domain_id = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.policy_version = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I64:
                    self.config_version = iprot.readI64()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()

        iprot.readStructEnd()



    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return 
        oprot.writeStructBegin('policyInstall_IDL_args')
        if self.domain_id != None:
            oprot.writeFieldBegin('domain_id', TType.I32, 1)
            oprot.writeI32(self.domain_id)
            oprot.writeFieldEnd()
        if self.policy_version != None:
            oprot.writeFieldBegin('policy_version', TType.I64, 2)
            oprot.writeI64(self.policy_version)
            oprot.writeFieldEnd()
        if self.config_version != None:
            oprot.writeFieldBegin('config_version', TType.I64, 3)
            oprot.writeI64(self.config_version)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

        def validate(self):
            pass





    def __repr__(self):
        L = [ '%s=%r' % (key, value) for (key, value,) in self.__dict__.iteritems() ]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))



    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__



    def __ne__(self, other):
        return not self == other




class policyInstall_IDL_result(object):
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
        oprot.writeStructBegin('policyInstall_IDL_result')
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




class Capabilities_getCapList_IDL_args(object):
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
        oprot.writeStructBegin('Capabilities_getCapList_IDL_args')
        oprot.writeFieldStop()
        oprot.writeStructEnd()

        def validate(self):
            pass





    def __repr__(self):
        L = [ '%s=%r' % (key, value) for (key, value,) in self.__dict__.iteritems() ]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))



    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__



    def __ne__(self, other):
        return not self == other




class Capabilities_getCapList_IDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.STRUCT,
      'success',
      (CapabilityList_IDL, CapabilityList_IDL.thrift_spec),
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
                    self.success = CapabilityList_IDL()
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
        oprot.writeStructBegin('Capabilities_getCapList_IDL_result')
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




class addFlowRule_IDL_args(object):
    """
    Attributes:
     - flowRule
    """

    thrift_spec = (None, (1,
      TType.STRUCT,
      'flowRule',
      (FlowRule_IDL, FlowRule_IDL.thrift_spec),
      None))

    def __init__(self, flowRule = None):
        self.flowRule = flowRule



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
                    self.flowRule = FlowRule_IDL()
                    self.flowRule.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()

        iprot.readStructEnd()



    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return 
        oprot.writeStructBegin('addFlowRule_IDL_args')
        if self.flowRule != None:
            oprot.writeFieldBegin('flowRule', TType.STRUCT, 1)
            self.flowRule.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

        def validate(self):
            pass





    def __repr__(self):
        L = [ '%s=%r' % (key, value) for (key, value,) in self.__dict__.iteritems() ]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))



    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__



    def __ne__(self, other):
        return not self == other




class addFlowRule_IDL_result(object):
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
        oprot.writeStructBegin('addFlowRule_IDL_result')
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




class load_nbar_pp_IDL_args(object):
    """
    Attributes:
     - proto_pack
    """

    thrift_spec = (None, (1,
      TType.STRUCT,
      'proto_pack',
      (NbarProtocolPack_IDL, NbarProtocolPack_IDL.thrift_spec),
      None))

    def __init__(self, proto_pack = None):
        self.proto_pack = proto_pack



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
                    self.proto_pack = NbarProtocolPack_IDL()
                    self.proto_pack.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()

        iprot.readStructEnd()



    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return 
        oprot.writeStructBegin('load_nbar_pp_IDL_args')
        if self.proto_pack != None:
            oprot.writeFieldBegin('proto_pack', TType.STRUCT, 1)
            self.proto_pack.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

        def validate(self):
            pass





    def __repr__(self):
        L = [ '%s=%r' % (key, value) for (key, value,) in self.__dict__.iteritems() ]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))



    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__



    def __ne__(self, other):
        return not self == other




class load_nbar_pp_IDL_result(object):
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
        oprot.writeStructBegin('load_nbar_pp_IDL_result')
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




class add_AVC_group_IDL_args(object):
    """
    Attributes:
     - type_id
     - apps
    """

    thrift_spec = (None, (1,
      TType.I32,
      'type_id',
      None,
      None), (2,
      TType.LIST,
      'apps',
      (TType.I32, None),
      None))

    def __init__(self, type_id = None, apps = None):
        self.type_id = type_id
        self.apps = apps



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
                    self.type_id = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.apps = []
                    (_etype59, _size56,) = iprot.readListBegin()
                    for _i60 in xrange(_size56):
                        _elem61 = iprot.readI32()
                        self.apps.append(_elem61)

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
        oprot.writeStructBegin('add_AVC_group_IDL_args')
        if self.type_id != None:
            oprot.writeFieldBegin('type_id', TType.I32, 1)
            oprot.writeI32(self.type_id)
            oprot.writeFieldEnd()
        if self.apps != None:
            oprot.writeFieldBegin('apps', TType.LIST, 2)
            oprot.writeListBegin(TType.I32, len(self.apps))
            for iter62 in self.apps:
                oprot.writeI32(iter62)

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




class add_AVC_group_IDL_result(object):
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
        oprot.writeStructBegin('add_AVC_group_IDL_result')
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




class AVC_groups_complete_IDL_args(object):
    """
    Attributes:
     - version
    """

    thrift_spec = (None, (1,
      TType.I64,
      'version',
      None,
      None))

    def __init__(self, version = None):
        self.version = version



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
                    self.version = iprot.readI64()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()

        iprot.readStructEnd()



    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return 
        oprot.writeStructBegin('AVC_groups_complete_IDL_args')
        if self.version != None:
            oprot.writeFieldBegin('version', TType.I64, 1)
            oprot.writeI64(self.version)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

        def validate(self):
            pass





    def __repr__(self):
        L = [ '%s=%r' % (key, value) for (key, value,) in self.__dict__.iteritems() ]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))



    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__



    def __ne__(self, other):
        return not self == other




class AVC_groups_complete_IDL_result(object):
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
        oprot.writeStructBegin('AVC_groups_complete_IDL_result')
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




class add_AVC_IDL_args(object):
    """
    Attributes:
     - name
     - unified_id
     - display_name
     - nbar_id
    """

    thrift_spec = (None,
     (1,
      TType.STRING,
      'name',
      None,
      None),
     (2,
      TType.I32,
      'unified_id',
      None,
      None),
     (3,
      TType.STRING,
      'display_name',
      None,
      None),
     (4,
      TType.I32,
      'nbar_id',
      None,
      None))

    def __init__(self, name = None, unified_id = None, display_name = None, nbar_id = None):
        self.name = name
        self.unified_id = unified_id
        self.display_name = display_name
        self.nbar_id = nbar_id



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
                    self.unified_id = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.display_name = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.nbar_id = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()

        iprot.readStructEnd()



    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return 
        oprot.writeStructBegin('add_AVC_IDL_args')
        if self.name != None:
            oprot.writeFieldBegin('name', TType.STRING, 1)
            oprot.writeString(self.name)
            oprot.writeFieldEnd()
        if self.unified_id != None:
            oprot.writeFieldBegin('unified_id', TType.I32, 2)
            oprot.writeI32(self.unified_id)
            oprot.writeFieldEnd()
        if self.display_name != None:
            oprot.writeFieldBegin('display_name', TType.STRING, 3)
            oprot.writeString(self.display_name)
            oprot.writeFieldEnd()
        if self.nbar_id != None:
            oprot.writeFieldBegin('nbar_id', TType.I32, 4)
            oprot.writeI32(self.nbar_id)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

        def validate(self):
            pass





    def __repr__(self):
        L = [ '%s=%r' % (key, value) for (key, value,) in self.__dict__.iteritems() ]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))



    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__



    def __ne__(self, other):
        return not self == other




class add_AVC_IDL_result(object):
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
        oprot.writeStructBegin('add_AVC_IDL_result')
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




class AVC_complete_IDL_args(object):
    """
    Attributes:
     - version
    """

    thrift_spec = (None, (1,
      TType.I64,
      'version',
      None,
      None))

    def __init__(self, version = None):
        self.version = version



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
                    self.version = iprot.readI64()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()

        iprot.readStructEnd()



    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return 
        oprot.writeStructBegin('AVC_complete_IDL_args')
        if self.version != None:
            oprot.writeFieldBegin('version', TType.I64, 1)
            oprot.writeI64(self.version)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

        def validate(self):
            pass





    def __repr__(self):
        L = [ '%s=%r' % (key, value) for (key, value,) in self.__dict__.iteritems() ]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))



    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__



    def __ne__(self, other):
        return not self == other




class AVC_complete_IDL_result(object):
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
        oprot.writeStructBegin('AVC_complete_IDL_result')
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




class init_IDL_args(object):
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
        oprot.writeStructBegin('init_IDL_args')
        oprot.writeFieldStop()
        oprot.writeStructEnd()

        def validate(self):
            pass





    def __repr__(self):
        L = [ '%s=%r' % (key, value) for (key, value,) in self.__dict__.iteritems() ]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))



    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__



    def __ne__(self, other):
        return not self == other




class init_IDL_result(object):
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
        oprot.writeStructBegin('init_IDL_result')
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




class deinit_IDL_args(object):
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
        oprot.writeStructBegin('deinit_IDL_args')
        oprot.writeFieldStop()
        oprot.writeStructEnd()

        def validate(self):
            pass





    def __repr__(self):
        L = [ '%s=%r' % (key, value) for (key, value,) in self.__dict__.iteritems() ]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))



    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__



    def __ne__(self, other):
        return not self == other




class deinit_IDL_result(object):
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
        oprot.writeStructBegin('deinit_IDL_result')
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




class syslog_cfg_IDL_args(object):
    """
    Attributes:
     - domain_id
     - enable
     - level
     - interval_len
     - msg_count
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'domain_id',
      None,
      None),
     (2,
      TType.BYTE,
      'enable',
      None,
      None),
     (3,
      TType.I32,
      'level',
      None,
      None),
     (4,
      TType.I32,
      'interval_len',
      None,
      None),
     (5,
      TType.I32,
      'msg_count',
      None,
      None))

    def __init__(self, domain_id = None, enable = None, level = None, interval_len = None, msg_count = None):
        self.domain_id = domain_id
        self.enable = enable
        self.level = level
        self.interval_len = interval_len
        self.msg_count = msg_count



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
                    self.domain_id = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.BYTE:
                    self.enable = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.level = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.interval_len = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.msg_count = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()

        iprot.readStructEnd()



    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return 
        oprot.writeStructBegin('syslog_cfg_IDL_args')
        if self.domain_id != None:
            oprot.writeFieldBegin('domain_id', TType.I32, 1)
            oprot.writeI32(self.domain_id)
            oprot.writeFieldEnd()
        if self.enable != None:
            oprot.writeFieldBegin('enable', TType.BYTE, 2)
            oprot.writeByte(self.enable)
            oprot.writeFieldEnd()
        if self.level != None:
            oprot.writeFieldBegin('level', TType.I32, 3)
            oprot.writeI32(self.level)
            oprot.writeFieldEnd()
        if self.interval_len != None:
            oprot.writeFieldBegin('interval_len', TType.I32, 4)
            oprot.writeI32(self.interval_len)
            oprot.writeFieldEnd()
        if self.msg_count != None:
            oprot.writeFieldBegin('msg_count', TType.I32, 5)
            oprot.writeI32(self.msg_count)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

        def validate(self):
            pass





    def __repr__(self):
        L = [ '%s=%r' % (key, value) for (key, value,) in self.__dict__.iteritems() ]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))



    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__



    def __ne__(self, other):
        return not self == other




class syslog_cfg_IDL_result(object):
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
        oprot.writeStructBegin('syslog_cfg_IDL_result')
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




class domain_cfg_IDL_args(object):
    """
    Attributes:
     - domain_id
     - events
     - syslog_chnl
     - dp_stats
     - dp_user_stats
     - pcap
     - appnav
     - wse_enabled
     - ips_enabled
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'domain_id',
      None,
      None),
     (2,
      TType.STRUCT,
      'events',
      (Channel_IDL, Channel_IDL.thrift_spec),
      None),
     (3,
      TType.STRUCT,
      'syslog_chnl',
      (Channel_IDL, Channel_IDL.thrift_spec),
      None),
     (4,
      TType.STRUCT,
      'dp_stats',
      (Channel_IDL, Channel_IDL.thrift_spec),
      None),
     (5,
      TType.STRUCT,
      'dp_user_stats',
      (Channel_IDL, Channel_IDL.thrift_spec),
      None),
     (6,
      TType.STRUCT,
      'pcap',
      (Channel_IDL, Channel_IDL.thrift_spec),
      None),
     (7,
      TType.STRUCT,
      'appnav',
      (Channel_IDL, Channel_IDL.thrift_spec),
      None),
     (8,
      TType.I32,
      'wse_enabled',
      None,
      None),
     (9,
      TType.I32,
      'ips_enabled',
      None,
      None))

    def __init__(self, domain_id = None, events = None, syslog_chnl = None, dp_stats = None, dp_user_stats = None, pcap = None, appnav = None, wse_enabled = None, ips_enabled = None):
        self.domain_id = domain_id
        self.events = events
        self.syslog_chnl = syslog_chnl
        self.dp_stats = dp_stats
        self.dp_user_stats = dp_user_stats
        self.pcap = pcap
        self.appnav = appnav
        self.wse_enabled = wse_enabled
        self.ips_enabled = ips_enabled



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
                    self.domain_id = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.events = Channel_IDL()
                    self.events.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRUCT:
                    self.syslog_chnl = Channel_IDL()
                    self.syslog_chnl.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRUCT:
                    self.dp_stats = Channel_IDL()
                    self.dp_stats.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRUCT:
                    self.dp_user_stats = Channel_IDL()
                    self.dp_user_stats.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRUCT:
                    self.pcap = Channel_IDL()
                    self.pcap.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.STRUCT:
                    self.appnav = Channel_IDL()
                    self.appnav.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.I32:
                    self.wse_enabled = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.I32:
                    self.ips_enabled = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()

        iprot.readStructEnd()



    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return 
        oprot.writeStructBegin('domain_cfg_IDL_args')
        if self.domain_id != None:
            oprot.writeFieldBegin('domain_id', TType.I32, 1)
            oprot.writeI32(self.domain_id)
            oprot.writeFieldEnd()
        if self.events != None:
            oprot.writeFieldBegin('events', TType.STRUCT, 2)
            self.events.write(oprot)
            oprot.writeFieldEnd()
        if self.syslog_chnl != None:
            oprot.writeFieldBegin('syslog_chnl', TType.STRUCT, 3)
            self.syslog_chnl.write(oprot)
            oprot.writeFieldEnd()
        if self.dp_stats != None:
            oprot.writeFieldBegin('dp_stats', TType.STRUCT, 4)
            self.dp_stats.write(oprot)
            oprot.writeFieldEnd()
        if self.dp_user_stats != None:
            oprot.writeFieldBegin('dp_user_stats', TType.STRUCT, 5)
            self.dp_user_stats.write(oprot)
            oprot.writeFieldEnd()
        if self.pcap != None:
            oprot.writeFieldBegin('pcap', TType.STRUCT, 6)
            self.pcap.write(oprot)
            oprot.writeFieldEnd()
        if self.appnav != None:
            oprot.writeFieldBegin('appnav', TType.STRUCT, 7)
            self.appnav.write(oprot)
            oprot.writeFieldEnd()
        if self.wse_enabled != None:
            oprot.writeFieldBegin('wse_enabled', TType.I32, 8)
            oprot.writeI32(self.wse_enabled)
            oprot.writeFieldEnd()
        if self.ips_enabled != None:
            oprot.writeFieldBegin('ips_enabled', TType.I32, 9)
            oprot.writeI32(self.ips_enabled)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

        def validate(self):
            pass





    def __repr__(self):
        L = [ '%s=%r' % (key, value) for (key, value,) in self.__dict__.iteritems() ]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))



    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__



    def __ne__(self, other):
        return not self == other




class domain_cfg_IDL_result(object):
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
        oprot.writeStructBegin('domain_cfg_IDL_result')
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




class createIntfMapTable_IDL_args(object):
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
        oprot.writeStructBegin('createIntfMapTable_IDL_args')
        oprot.writeFieldStop()
        oprot.writeStructEnd()

        def validate(self):
            pass





    def __repr__(self):
        L = [ '%s=%r' % (key, value) for (key, value,) in self.__dict__.iteritems() ]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))



    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__



    def __ne__(self, other):
        return not self == other




class createIntfMapTable_IDL_result(object):
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
        oprot.writeStructBegin('createIntfMapTable_IDL_result')
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




class destroyIntfMapTable_IDL_args(object):
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
        oprot.writeStructBegin('destroyIntfMapTable_IDL_args')
        oprot.writeFieldStop()
        oprot.writeStructEnd()

        def validate(self):
            pass





    def __repr__(self):
        L = [ '%s=%r' % (key, value) for (key, value,) in self.__dict__.iteritems() ]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))



    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__



    def __ne__(self, other):
        return not self == other




class destroyIntfMapTable_IDL_result(object):
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
        oprot.writeStructBegin('destroyIntfMapTable_IDL_result')
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




class addIntfMapTable_IDL_args(object):
    """
    Attributes:
     - intfMapTbl
    """

    thrift_spec = (None, (1,
      TType.LIST,
      'intfMapTbl',
      (TType.STRUCT, (interfaceRoleMap_IDL, interfaceRoleMap_IDL.thrift_spec)),
      None))

    def __init__(self, intfMapTbl = None):
        self.intfMapTbl = intfMapTbl



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
                if ftype == TType.LIST:
                    self.intfMapTbl = []
                    (_etype66, _size63,) = iprot.readListBegin()
                    for _i67 in xrange(_size63):
                        _elem68 = interfaceRoleMap_IDL()
                        _elem68.read(iprot)
                        self.intfMapTbl.append(_elem68)

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
        oprot.writeStructBegin('addIntfMapTable_IDL_args')
        if self.intfMapTbl != None:
            oprot.writeFieldBegin('intfMapTbl', TType.LIST, 1)
            oprot.writeListBegin(TType.STRUCT, len(self.intfMapTbl))
            for iter69 in self.intfMapTbl:
                iter69.write(oprot)

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




class addIntfMapTable_IDL_result(object):
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
        oprot.writeStructBegin('addIntfMapTable_IDL_result')
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




class add_AVC_list_IDL_args(object):
    """
    Attributes:
     - avcObj
    """

    thrift_spec = (None, (1,
      TType.LIST,
      'avcObj',
      (TType.STRUCT, (avcObj_IDL, avcObj_IDL.thrift_spec)),
      None))

    def __init__(self, avcObj = None):
        self.avcObj = avcObj



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
                if ftype == TType.LIST:
                    self.avcObj = []
                    (_etype73, _size70,) = iprot.readListBegin()
                    for _i74 in xrange(_size70):
                        _elem75 = avcObj_IDL()
                        _elem75.read(iprot)
                        self.avcObj.append(_elem75)

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
        oprot.writeStructBegin('add_AVC_list_IDL_args')
        if self.avcObj != None:
            oprot.writeFieldBegin('avcObj', TType.LIST, 1)
            oprot.writeListBegin(TType.STRUCT, len(self.avcObj))
            for iter76 in self.avcObj:
                iter76.write(oprot)

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




class add_AVC_list_IDL_result(object):
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
        oprot.writeStructBegin('add_AVC_list_IDL_result')
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




class add_AVC_group_list_IDL_args(object):
    """
    Attributes:
     - avcGroupObj
    """

    thrift_spec = (None, (1,
      TType.LIST,
      'avcGroupObj',
      (TType.STRUCT, (avcGroupObj_IDL, avcGroupObj_IDL.thrift_spec)),
      None))

    def __init__(self, avcGroupObj = None):
        self.avcGroupObj = avcGroupObj



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
                if ftype == TType.LIST:
                    self.avcGroupObj = []
                    (_etype80, _size77,) = iprot.readListBegin()
                    for _i81 in xrange(_size77):
                        _elem82 = avcGroupObj_IDL()
                        _elem82.read(iprot)
                        self.avcGroupObj.append(_elem82)

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
        oprot.writeStructBegin('add_AVC_group_list_IDL_args')
        if self.avcGroupObj != None:
            oprot.writeFieldBegin('avcGroupObj', TType.LIST, 1)
            oprot.writeListBegin(TType.STRUCT, len(self.avcGroupObj))
            for iter83 in self.avcGroupObj:
                iter83.write(oprot)

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




class add_AVC_group_list_IDL_result(object):
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
        oprot.writeStructBegin('add_AVC_group_list_IDL_result')
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




class get_IOSXE_Version_IDL_args(object):
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
        oprot.writeStructBegin('get_IOSXE_Version_IDL_args')
        oprot.writeFieldStop()
        oprot.writeStructEnd()

        def validate(self):
            pass





    def __repr__(self):
        L = [ '%s=%r' % (key, value) for (key, value,) in self.__dict__.iteritems() ]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))



    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__



    def __ne__(self, other):
        return not self == other




class get_IOSXE_Version_IDL_result(object):
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
        oprot.writeStructBegin('get_IOSXE_Version_IDL_result')
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




class get_nbar_eng_Version_IDL_args(object):
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
        oprot.writeStructBegin('get_nbar_eng_Version_IDL_args')
        oprot.writeFieldStop()
        oprot.writeStructEnd()

        def validate(self):
            pass





    def __repr__(self):
        L = [ '%s=%r' % (key, value) for (key, value,) in self.__dict__.iteritems() ]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))



    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__



    def __ne__(self, other):
        return not self == other




class get_nbar_eng_Version_IDL_result(object):
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
        oprot.writeStructBegin('get_nbar_eng_Version_IDL_result')
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




class pcap_cfg_IDL_args(object):
    """
    Attributes:
     - domain_id
     - capture_size
     - rl_interval_length
     - rl_packet_count
     - buffer_size
     - circular_buffer
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'domain_id',
      None,
      None),
     (2,
      TType.I32,
      'capture_size',
      None,
      None),
     (3,
      TType.I32,
      'rl_interval_length',
      None,
      None),
     (4,
      TType.I32,
      'rl_packet_count',
      None,
      None),
     (5,
      TType.I32,
      'buffer_size',
      None,
      None),
     (6,
      TType.I32,
      'circular_buffer',
      None,
      None))

    def __init__(self, domain_id = None, capture_size = None, rl_interval_length = None, rl_packet_count = None, buffer_size = None, circular_buffer = None):
        self.domain_id = domain_id
        self.capture_size = capture_size
        self.rl_interval_length = rl_interval_length
        self.rl_packet_count = rl_packet_count
        self.buffer_size = buffer_size
        self.circular_buffer = circular_buffer



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
                    self.domain_id = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.capture_size = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.rl_interval_length = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.rl_packet_count = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.buffer_size = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I32:
                    self.circular_buffer = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()

        iprot.readStructEnd()



    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return 
        oprot.writeStructBegin('pcap_cfg_IDL_args')
        if self.domain_id != None:
            oprot.writeFieldBegin('domain_id', TType.I32, 1)
            oprot.writeI32(self.domain_id)
            oprot.writeFieldEnd()
        if self.capture_size != None:
            oprot.writeFieldBegin('capture_size', TType.I32, 2)
            oprot.writeI32(self.capture_size)
            oprot.writeFieldEnd()
        if self.rl_interval_length != None:
            oprot.writeFieldBegin('rl_interval_length', TType.I32, 3)
            oprot.writeI32(self.rl_interval_length)
            oprot.writeFieldEnd()
        if self.rl_packet_count != None:
            oprot.writeFieldBegin('rl_packet_count', TType.I32, 4)
            oprot.writeI32(self.rl_packet_count)
            oprot.writeFieldEnd()
        if self.buffer_size != None:
            oprot.writeFieldBegin('buffer_size', TType.I32, 5)
            oprot.writeI32(self.buffer_size)
            oprot.writeFieldEnd()
        if self.circular_buffer != None:
            oprot.writeFieldBegin('circular_buffer', TType.I32, 6)
            oprot.writeI32(self.circular_buffer)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

        def validate(self):
            pass





    def __repr__(self):
        L = [ '%s=%r' % (key, value) for (key, value,) in self.__dict__.iteritems() ]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))



    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__



    def __ne__(self, other):
        return not self == other




class pcap_cfg_IDL_result(object):
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
        oprot.writeStructBegin('pcap_cfg_IDL_result')
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




class pcap_drop_capture_cfg_IDL_args(object):
    """
    Attributes:
     - domain_id
     - enable
    """

    thrift_spec = (None, (1,
      TType.I32,
      'domain_id',
      None,
      None), (2,
      TType.BYTE,
      'enable',
      None,
      None))

    def __init__(self, domain_id = None, enable = None):
        self.domain_id = domain_id
        self.enable = enable



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
                    self.domain_id = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.BYTE:
                    self.enable = iprot.readByte()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()

        iprot.readStructEnd()



    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return 
        oprot.writeStructBegin('pcap_drop_capture_cfg_IDL_args')
        if self.domain_id != None:
            oprot.writeFieldBegin('domain_id', TType.I32, 1)
            oprot.writeI32(self.domain_id)
            oprot.writeFieldEnd()
        if self.enable != None:
            oprot.writeFieldBegin('enable', TType.BYTE, 2)
            oprot.writeByte(self.enable)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

        def validate(self):
            pass





    def __repr__(self):
        L = [ '%s=%r' % (key, value) for (key, value,) in self.__dict__.iteritems() ]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))



    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__



    def __ne__(self, other):
        return not self == other




class pcap_drop_capture_cfg_IDL_result(object):
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
        oprot.writeStructBegin('pcap_drop_capture_cfg_IDL_result')
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
# 2015.02.05 17:22:16 IST
