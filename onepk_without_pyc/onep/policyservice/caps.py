# 2015.02.05 17:22:51 IST
from onep.policyservice import action
from onep.policyservice import match
from onep.PolicyBulkIDL.PolicyBulkIDL import Client
from onep.core.util.OnepArgumentTypeValidate import *
from onep.core.util.Enum import enum
from onep.core.exception import OnepIllegalArgumentException
from onep.core.exception import OnepRemoteProcedureException
from onep.core.exception import OnepNotSupportedException
from Shared.ttypes import ExceptionIDL
import logging
PolicyCapabilitiesType = enum('NONE', 'ACL_INGRESS', 'ACL_EGRESS', 'QOS_INGRESS', 'QOS_EGRESS', 'L2_ANY', 'L2_DEST', 'L2_IPV4_L4_ANY', 'L2_IPV6_L4_ANY', 'L2_ACL', 'L2_L3', 'L3_IPV4', 'L3_IPV6', 'L3_DS', 'IPV4_L4_ANY', 'IPV6_L4_ANY', 'IPV4_DEST', 'IPV6_DEST', 'PBR', 'TRAFFIC_INGRESS', 'TRAFFIC_EGRESS', 'ZBFW', 'DATAPATH', 'MAC', 'ANY', 'MPLS', 'ARP', 'SELECTOR', 'LAST')
_service_set_excluded = {PolicyCapabilitiesType.DATAPATH: {'actions': [action.ActionType.COPY, action.ActionType.DIVERT],
                                   'matches': []}}

def _in_excluded(table, item, index):
    if table.type in _service_set_excluded:
        return item in _service_set_excluded[table.type][index]



def _translate_action_enums(table):
    act = []
    for a in table.actions:
        if a.supported and a.type in action._map_external_action.keys():
            if _in_excluded(table, a.type, 'actions'):
                continue
            act.append(a.type)

    return act



def _translate_match_enums(table):
    mtchs = []
    for mtch in table.matches:
        if mtch.supported and mtch.type in match._map_external_match.keys():
            if _in_excluded(table, mtch.type, 'matches'):
                continue
            mtchs.append(mtch.type)

    return mtchs



def get_table_capabilities(element):
    """
        Returns a list of PolicyTable classes with capabilities per policy type
    
        @param NetworkElement class
        @type element: {NetworkElement<onep.element.NetworkElement>}
    
        @return PolicyTable classes
        @rtype: list of L{PolicyClass<onep.policyservice.caps.PolicyTable>}
    
        """
    try:
        tables = Client(element.api_protocol).Policy_getGlobalCapIDL(element.session_handle._id).tables
    except ExceptionIDL as e:
        raise OnepRemoteProcedureException(e)
    table_classes = []
    for table in tables:
        pt = PolicyTable(table)
        pt.actions = _translate_action_enums(table)
        pt.matches = _translate_match_enums(table)
        table_classes.append(pt)

    return table_classes



def get_global_capabilities(element):
    """ 
        Return a PolicyGlobal class specific to network element
    
        @param NetworkElement class
        @type element: {NetworkElement<onep.element.NetworkElement>}
    
        @return PolicyGlobal class
        @rtype: {PolicyGlobal<onep.policyservice.caps.PolicyGlobal>}
    
        """
    try:
        global_caps = Client(element.api_protocol).Policy_getGlobalCapIDL(element.session_handle._id)
    except ExceptionIDL as e:
        raise OnepRemoteProcedureException(e)
    return PolicyGlobal(global_caps)



class PolicyPipeline(object):
    """
        Policy pipeline capabilities
    
        name - PolicyTable name pipeline refers to
        handle - pipeline handle
        table_chain - list of table identifiers in chain
        id - optional identifier
        table_graph - graph of pipelines associated to this pipeline
        
        """


    def __init__(self, pipe):
        self.name = pipe.name
        self.description = pipe.desc
        self.handle = pipe.handle
        self.table_chain = pipe.tableChain
        self.id = None
        self.table_graph = None
        if pipe.id:
            self.id = pipe.id
        if pipe.tableGraph:
            self.table_graph = pipe.tableGraph



    def __str__(self):
        chain_str = []
        for chain in self.table_chain:
            chain_str.append(hex(chain))

        graph_str = ''
        if self.table_graph:
            for graph in self.table_graph:
                graph_str = graph_str + 'handles - [go to handles]\n'
                graph_str = graph_str + str(graph.handle) + ' - ' + str(graph.gotoHandles)

        if not graph_str:
            graph_str = str(None)
        return '\n        *-------------------------------\n        |  Policy Pipeline\n        *-------------------------------\n        %s - %s\n        handle - %d\n        id - %s\n        table chains:\n            %s\n        table graphs:\n            %s\n        ' % (self.name,
         self.description,
         self.handle,
         str(self.id),
         str(chain_str),
         graph_str)




class PolicyGlobal(object):
    """
        Policy capabilities of network element
    
        stat_polling_rate - max polling rate for getting statistics
        atomic_bulk - atomicity per bulk instance operation supported
        atomic_inline_class - atomicity per inline class operation supported
        atomic_pmap - atomicity per policy map operation supported
    
        """


    def __init__(self, global_caps):
        if global_caps.stats:
            self.stat_polling_rate = global_caps.stats.pollingRate
        if global_caps.atomicity:
            self.atomic_bulk = bool(global_caps.atomicity.bulkInstance)
            self.atomic_inline_class = bool(global_caps.atomicity.inlineClass)
            self.atomic_pmap = bool(global_caps.atomicity.policyMap)
        self.pipe_classes = []
        if global_caps.pipelines:
            for pipe in global_caps.pipelines:
                self.pipe_classes.append(PolicyPipeline(pipe))




    def __str__(self):
        pipe_str = ''
        for pipe in self.pipe_classes:
            pipe_str = pipe_str + pipe.__str__()

        return '\n        *-------------------------------\n        |  Policy Global Capabilities\n        *-------------------------------\n\n        statistic polling rate --------- %d\n        atomic bulk operations --------- %s\n        atomic inline class operations - %s\n        atomic policy maps operations -- %s\n        %s\n        ' % (self.stat_polling_rate,
         str(self.atomic_bulk),
         str(self.atomic_inline_class),
         str(self.atomic_pmap),
         pipe_str)




class PolicyTable(object):
    """
        Policy capabilities of a table type
    
        name - string - table type name
        type - PolicyCapabilitiesType
        max_entries - int - maximum number of entries allowed by the table
        persistant - boolean - persistant storage between reboots
        transient - boolean - transient storage
        actions - list of ActionType table type is capable of
        matches - list of MatchType table type is capable of
        packet_rate - long - expected packets per second rate
        sequence - order in which table type is processed
    
        class_map_support - boolean - supports class_maps
        class_inline_support - boolean - support inline class
        class_max_inline - int - maximum inline classes
        class_provision_rate - int - rate of updating the table in updates/second
        class_flow_timeout - boolean - support flow timeouts
        class_relative_insert - boolean - support entry insertion by relative ordering
        class_sequence_insert - boolean - support entry insertion by sequence number
    
        stats_per_target - boolean - supports entry action statistics per target
        stats_all_target - boolean - supports sum of all entry statistics
        stats_entry_per_target - boolean - supports all entries statistics per target
        stats_entry_all_target - boolean - supports entry statistics aggregated across all targets
    
        """


    def __init__(self, table):
        self.name = table.name
        self.type = table.type
        self.max_entries = table.maxEntries
        self.persistent = bool(table.persist)
        self.transient = bool(table.trans)
        self.actions = table.actions
        self.matches = table.matches
        self.packet_rate = table.pktPerSec
        self.sequence = table.seqNum
        self.class_map_support = bool(table.classcap.cmapClassSupp)
        self.class_inline_support = bool(table.classcap.inlineClsSupp)
        self.class_max_inline = table.classcap.clsPerTbl
        self.class_provision_rate = table.classcap.clsProvRate
        self.class_flow_timeout = bool(table.classcap.clsTimeoutSupp)
        self.class_relative_insert = bool(table.classcap.clsOrderSupp)
        self.class_sequence_insert = bool(table.classcap.clsSeqNumSupp)
        self.stats_per_target = bool(table.stats.actTgtStats)
        self.stats_all_target = bool(table.stats.clsAggTgtAggStats)
        self.stats_entry_per_target = bool(table.stats.tblTgtStats)
        self.stats_entry_all_target = bool(table.stats.clsTgtAggStats)



    def __str__(self):
        actions_str = ''
        for act in self.actions:
            actions_str = actions_str + action.ActionType.enumval(act) + '\n'
            actions_str = actions_str + '        '

        matches_str = ''
        for mtch in self.matches:
            matches_str = matches_str + match.MatchType.enumval(mtch) + '\n'
            matches_str = matches_str + '        '

        return '\n        *--------------------------------------\n        |  Name: %s\n        |  Type: %s\n        *--------------------------------------\n\n        GENERAL\n        -------\n        maximum entries allowed ------------ %d\n        transient support ------------------ %s\n        persistant support ----------------- %s\n        packet rate ------------------------ %d\n        table sequence --------------------- %d\n\n        CLASS\n        -----\n        class support ---------------------- %s\n        inline class support --------------- %s\n        max inline class ------------------- %d\n        class provision rate --------------- %d\n        flow timeout support --------------- %s\n        relative class insert support ------ %s\n        sequential class insert support ---- %s\n\n        STATISTICS\n        ----------\n        entry action stats per target ------ %s\n        entry aggregated action stats ------ %s\n        stats per target for all entries --- %s\n        entries aggregated for all targets - %s\n\n\n        Actions:\n\n        %s\n\n        Matches:\n\n        %s\n        ' % (self.name,
         PolicyCapabilitiesType.enumval(self.type),
         self.max_entries,
         str(self.transient),
         str(self.persistent),
         self.packet_rate,
         self.sequence,
         str(self.class_map_support),
         str(self.class_inline_support),
         self.class_max_inline,
         self.class_provision_rate,
         str(self.class_flow_timeout),
         str(self.class_relative_insert),
         str(self.class_sequence_insert),
         str(self.stats_per_target),
         str(self.stats_all_target),
         str(self.stats_entry_per_target),
         str(self.stats_entry_all_target),
         actions_str,
         matches_str)




class PolicyCapabilities(object):
    """
    Internal PolicyCapabilities class stores the capabilities of the Network Element.
    
    ***DEPRECATED***
    classmethods get_capabilities and get_table_capabilities
    Please use caps.get_table_capabilities()
    ****************
    
    """

    log = logging.getLogger(__name__)

    def __init__(self, type, element):
        """ 
                Class PolicyCapabilities.
                
                @param type: PolicyCapabilitiesType for type of policy
                @type type: {PolicyCapabilitiesType<onep.policyservice.caps.PolicyCapabilitiesType>}
                @param element: NetworkElement instance. 
                @type element: {NetworkElement<onep.element.NetworkElement>}
                
                @raise OnepIllegalArgumentException: If any of the constructor argument is invalid.
        
                """
        if not PolicyCapabilitiesType._is_valid(type):
            raise OnepIllegalArgumentException('invalid policy type')
        self.policy_type = type
        self.network_element = element
        self.session_id = element.session_handle._id
        self.client = Client(element.api_protocol)
        self.table = {'type': None,
         'actions': [],
         'matches': []}
        self.table['matches'] = self.matches = []
        self.table['actions'] = self.actions = []
        self.table_classes = []
        try:
            self.all = self.client.Policy_getGlobalCapIDL(self.session_id)
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        type_supported = False
        for tbl in self.all.tables:
            if tbl.type == type:
                self.table['type'] = type
                self.table['actions'] = self.actions = _translate_action_enums(tbl)
                self.table['matches'] = self.matches = _translate_match_enums(tbl)
                pt = PolicyTable(tbl)
                pt.actions = self.actions
                pt.matches = self.matches
                self.table_classes.append(pt)
                break

        if not self.table['type']:
            raise OnepNotSupportedException('Policy type ' + PolicyCapabilitiesType.enumval(type))



    @classmethod
    def get_capabilities(self, element):
        """
                ***DEPRECATED***
                Please use caps.get_table_capabilities()
                ****************
                -----------------------------------------------------------------------------------
                Returns a list of PolicyTable classes containing all capabilities on network element
        
                @param NetworkElement class
                @type element: {NetworkElement<onep.element.NetworkElement>}
        
                @return PolicyTable classes
                @rtype: list of L{PolicyTable<onep.policyservice.caps.PolicyTable>}
        
                """
        self.log.warning('PolicyCapabilities.get_capabilities classmethod is deprecated, Please use caps.get_table_capabilities')
        try:
            tables = Client(element.api_protocol).Policy_getGlobalCapIDL(element.session_handle._id).tables
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        table_classes = []
        for table in tables:
            pt = PolicyTable(table)
            pt.actions = _translate_action_enums(table)
            pt.matches = _translate_match_enums(table)
            table_classes.append(pt)

        return table_classes



    @classmethod
    def get_table_capabilities(self, element):
        """
                ***DEPRECATED***
                Please use caps.get_table_capabilities()
                ****************
                -----------------------------------------------------------------------------------
                Returns a list of PolicyQuery.PolicyCapabilitiesType supported on network element
        
                @param NetworkElement class
                @type element: {NetworkElement<onep.policy.element.NetworkElement>}
        
                @return PolicyCapabilitiesType enums
                @rtype: list of L{PolicyCapabilitiesType<onep.policyservice.caps.PolicyCapabilitiesType>}
        
                """
        self.log.warning('PolicyCapabilities.get_table_capabilities classmethod is deprecated. Please use caps.get_table_capabilities')
        try:
            tables = Client(element.api_protocol).Policy_getGlobalCapIDL(element.session_handle._id).tables
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        return [ table.type for table in tables ]




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:22:52 IST
