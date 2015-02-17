# 2015.02.05 17:22:49 IST
from onep.PolicyCommonTypes.ttypes import actionStatsResultIDL
from onep.PolicyCommonTypes.ttypes import classStatsResultIDL
from onep.PolicyCommonTypes.ttypes import matchStatsResultIDL
from onep.policyservice import StorageType
from onep.core.util import enum
import logging

class PolicyStatistics(object):
    """
        Policy statistics class
    
        """


    def __init__(self, storage_type = 0, async_handle = 0, pmap_handle = 0, interfaces = [], total_count = 0, entry_count = 0, more = 0, entry_stats = []):
        self.log = logging.getLogger(__name__)
        self.storage_type = storage_type
        self.async_handle = async_handle
        self.pmap_handle = pmap_handle
        self.interfaces = interfaces
        self.total_count = total_count
        self.entry_count = entry_count
        self.more = more
        self.entry_stats = entry_stats



    @property
    def interfaces(self):
        return self._interfaces



    @interfaces.setter
    def interfaces(self, intfs):
        self._interfaces = intfs



    @property
    def entry_stats(self):
        return self._entry_stats



    @entry_stats.setter
    def entry_stats(self, estats):
        self._entry_stats = []
        for stat in estats:
            self._entry_stats.append(EntryStatistics(stat.time_stamp, stat.last_data_time, stat.classStatsResult, stat.matchStatsResultList, stat.actionStatsResultList))




    def __str__(self):
        estat_str = ''
        for stat in self.entry_stats:
            estat_str = estat_str + str(stat)

        return '\n        Policy Statistics\n        -----------------\n        storage_type - %s\n        async_handle - %d\n        pmap_handle  - %d\n        interfaces   - %s\n        total_count  - %d\n        entry_count  - %d\n        more         - %d\n        %s' % (StorageType.enumval(self.storage_type),
         self.async_handle,
         self.pmap_handle,
         str(self.interfaces),
         self.total_count,
         self.entry_count,
         self.more,
         estat_str)




class EntryStatistics(object):
    """
        Service policy delta statistics
    
        time_stamp     - Time statistics were retrieved
        last_data_time - Last time statistics were retrieved
        class_stats    - class ClassStatistics
        match_stats    - list of dict {type, class MatchStatistics}
        action_stats   - *depends on ActionStatisticType
    
        ActionStatisticType - GENERIC - list of dict {Action.ActionType, packets, bytes}
                              POLICE  - list of dict {Action.ActionType, class PoliceStatistics}
                              QUEUE   - list of dict {Action.ActionType, class QueueStatistics}
        
        @undocumented: action_stats
    
        """


    def __init__(self, time = 0, last_data_time = 0, class_stats = [], match_stats = [], action_stats = []):
        self.log = logging.getLogger(__name__)
        self.time_stamp = time
        self.last_data_time = last_data_time
        self.class_stats = class_stats
        self.match_stats = match_stats
        self.action_stats = action_stats


    ActionStatisticType = enum(GENERIC=0, POLICE=1, QUEUE=2)

    @property
    def class_stats(self):
        return self._class_stats



    @class_stats.setter
    def class_stats(self, cstats):
        self._class_stats = ClassStatistics._from_idl(cstats)



    @property
    def match_stats(self):
        return self._match_stats



    @match_stats.setter
    def match_stats(self, mstats):
        if mstats:
            for stat in mstats:
                self._match_stats.append(MatchStatistics._from_idl(mstats))

        else:
            self._match_stats = []



    @property
    def action_stats(self):
        return self._action_stats



    @action_stats.setter
    def action_stats(self, astats):
        if astats:
            for stat in astats:
                stats = {}
                stats['type'] = Action.ActionType.enumval(actionStatsResultIDL.action_type)
                if actionStatsResultIDL.action_stat_type == self.ActionStatisticType.POLICE:
                    stats['police'] = PoliceStatistics._from_idl(stat)
                elif actionStatsResultIDL.action_stat_type == self.ActionStatisticType.QUEUE:
                    stats['queue'] = QueueStatistics._from_idl(stat)
                elif actionStatsResultIDL.action_stat_type == self.ActionStatisticType.GENERIC:
                    stats['packets'] = actionStatsResultIDL.action_pkts
                    stats['bytes'] = actionStatsResultIDL.action_bytes
                else:
                    self.log.error('bad action stats ' + str(stat))
                self.action_stats.append(stats)

        else:
            self._action_stats = []



    def __str__(self):
        action_stats_str = ''
        for action_stats in self.action_stats:
            action_stats_str = action_stats_str + str(action_stats)

        match_stats_str = '\n'
        for match_stats in self.match_stats:
            match_stats_str = match_stats_str + str(match_stats)

        return '\n            Entry Statistics\n            ----------------\n            time_stamp     = %d\n            last_data_time = %d\n                %s\n                %s\n                %s\n            ' % (self.time_stamp,
         self.last_data_time,
         str(self.class_stats),
         action_stats_str,
         match_stats_str)




class PoliceStatistics(object):
    """
    This class contains all the information received from the
    Network Element about PoliceStatistics.
    
    @cvar conform_bytes: The conform bytes
    @type conform_bytes:  C{int}
    
    @cvar conform_packets: The conform packets
    @type conform_packets:  C{int}
    
    @cvar conform_rate: The conform rate
    @type conform_rate:  C{int}
    
    @cvar exceed_bytes: The exceed bytes
    @type exceed_bytes:  C{int}
    
    @cvar exceed_packets: The exceed packets
    @type exceed_packets:  C{int}
    
    @cvar exceed_rate: The exceed rate
    @type exceed_rate:  C{int}
    
    @cvar violate_bytes: The violate bytes
    @type violate_bytes:  C{int}
    
    @cvar violate_packets: The violate packets
    @type violate_packets:  C{int}
    
    @cvar violate_rate: The violate rate
    @type violate_rate:  C{int}  
    
    @undocumented: conform_packets
    @undocumented: conform_rate
    @undocumented: exceed_packets
    @undocumented: exceed_rate
    @undocumented: violate_packets
    @undocumented: violate_rate
    """


    @property
    def conform_bytes(self):
        return self._conform_bytes



    @property
    def conform_packets(self):
        return self._conform_packets



    @property
    def conform_rate(self):
        return self._conform_rate



    @property
    def exceed_bytes(self):
        return self.exceedBytes



    @property
    def exceed_packets(self):
        return self.exceed_packets



    @property
    def exceed_rate(self):
        return self.exceed_rate



    @property
    def violate_bytes(self):
        return self._violate_bytes



    @property
    def violate_packets(self):
        return self._violate_packets



    @property
    def violate_rate(self):
        return self._violate_rate



    def __init__(self, conform_bytes, conform_packets, conform_rate, exceed_bytes, exceed_packets, exceed_rate, violate_bytes, violate_packets, violate_rate):
        """Constructor of PoliceStatistics."""
        self._conform_bytes = conform_bytes
        self._conform_packets = conform_packets
        self._conform_rate = conform_rate
        self._exceed_bytes = exceed_bytes
        self._exeed_packets = exceed_packets
        self._exceed_rate = exceed_rate
        self._violate_bytes = violate_bytes
        self._violate_packets = violate_packets
        self._violate_rate = violate_rate



    @classmethod
    def _from_idl(cls, astats):
        return PoliceStatistics(astats.conform_bytes, astats.conform_pkts, astats.conform_rate, astats.exceed_bytes, astats.exceed_pkts, astats.exceed_rate, astats.violate_bytes, astats.violate_pkts, astats.violate_rate)



    def __str__(self):
        return '\n                Police Statistics\n                -----------------\n                conform_bytes   = %d\n                conform_packets = %d\n                conform_rate    = %d\n                exceed_bytes    = %d\n                exceed_packets  = %d\n                exceed_rate     = %d\n                violate_bytes   = %d\n                violate_packets = %d\n                violate_rate    = %d\n            ' % (self._conform_bytes,
         self._conform_packets,
         self._conform_rate,
         self._exceed_bytes,
         self._exeed_packets,
         self._exceed_rate,
         self._violate_bytes,
         self._violate_packets,
         self._violate_rate)




class QueueStatistics(object):
    """ QueueStatistics class.
    
    This class gets the information from the Network Element about QueueStatistics.
    
    @undocumented: drop_packets
    @undocumented: out_packets
    """


    def _get_queue_size_bytes(self):
        return self._queue_size_bytes


    _doc_queue_size_bytes = ' Queue Size Bytes.\n     \n    @type: C{long}\n    '
    queue_size_bytes = property(_get_queue_size_bytes, None, None, _doc_queue_size_bytes)

    def _get_queue_size_packets(self):
        return self._queue_size_packets


    _doc_queue_size_packets = ' Queue Size Packets.\n     \n    @type: C{long}\n    '
    queue_size_packets = property(_get_queue_size_packets, None, None, _doc_queue_size_packets)

    def _get_drop_bytes(self):
        return self._drop_bytes


    _doc_drop_bytes = ' Drop Bytes.\n     \n    @type: C{long}\n    '
    drop_bytes = property(_get_drop_bytes, None, None, _doc_drop_bytes)

    def _get_drop_packets(self):
        return self._drop_packets


    _doc_drop_packets = ' Drop Packets.\n     \n    @type: C{long}\n    '
    drop_packets = property(_get_drop_packets, None, None, _doc_drop_packets)

    def _get_flow_drops(self):
        return self._flow_drops


    _doc_flow_drops = ' Flow Drops.\n     \n    @type: C{long}\n    '
    flow_drops = property(_get_flow_drops, None, None, _doc_flow_drops)

    def _get_no_buffer_drops(self):
        return self._no_buffer_drops


    _doc_no_buffer_drops = ' No Buffer Drops.\n     \n    @type: C{long}\n    '
    no_buffer_drops = property(_get_no_buffer_drops, None, None, _doc_no_buffer_drops)

    def _get_out_bytes(self):
        return self._out_bytes


    _doc_out_bytes = ' Out Bytes.\n     \n    @type: C{long}\n    '
    out_bytes = property(_get_out_bytes, None, None, _doc_out_bytes)

    def _get_out_packets(self):
        return self._out_packets


    _doc_out_packets = ' Out Packets.\n     \n    @type: C{long}\n    '
    out_packets = property(_get_out_packets, None, None, _doc_out_packets)

    def __init__(self, queue_size_bytes, queue_size_packets, drop_bytes, drop_packets, flow_drops, no_buffer_drops, out_bytes, out_packets):
        """ Constructor of Class QueueStatistics.
        """
        self._queue_size_bytes = queue_size_bytes
        self._queue_size_packets = queue_size_packets
        self._drop_bytes = drop_bytes
        self._drop_packets = drop_packets
        self._flow_drops = flow_drops
        self._no_buffer_drops = no_buffer_drops
        self._out_bytes = out_bytes
        self._out_packets = out_packets



    @classmethod
    def _from_idl(cls, queue):
        """
        """
        return QueueStatistics(queue.queue_size_bytes, queue.queue_size_pkts, queue.queue_drop_bytes, queue.queue_drop_pkts, queue.queue_drop_flows, queue.queue_no_buffers, queue.queue_out_bytes, queue.queue_out_pkts)



    def __str__(self):
        return '\n                Queue Statistics\n                ----------------\n                queue_size_bytes   = %d\n                queue_size_packets = %d\n                drop_bytes         = %d\n                drop_packets       = %d\n                flow_drops         = %d\n                no_buffer_drops    = %d\n                out_bytes          = %d\n                out_packets        = %d\n            ' % (self._queue_size_bytes,
         self._queue_size_packets,
         self._drop_bytes,
         self._drop_packets,
         self._flow_drops,
         self._no_buffer_drops,
         self._out_bytes,
         self._out_packets)




class ClassStatistics(object):
    """ 
        Class statistic totals
    
        pkts  - Number of classified packets
        bytes - Number of bytes total in classified packet streams
        drop_bytes - Number of dropped bytes total in classified packet streams
    
        """


    def __init__(self, pkts = 0, bytes = 0, rate = 0, drop_pkts = 0, drop_bytes = 0, drop_rate = 0):
        self.pkts = pkts
        self.bytes = bytes
        self.rate = rate
        self.drop_pkts = drop_pkts
        self.drop_bytes = drop_bytes
        self.drop_rate = drop_rate



    @classmethod
    def _from_idl(self, cls):
        return ClassStatistics(cls.classified_pkts, cls.classified_bytes, cls.classified_rate, cls.drop_pkts, cls.drop_bytes, cls.drop_rate)



    def __str__(self):
        return '\n                Class Statistics\n                ----------------\n                packets = %d\n                bytes   = %d\n                rate    = %d\n                dropped packets = %d\n                dropped bytes   = %d\n                dropped rate    = %d\n            ' % (self.pkts,
         self.bytes,
         self.rate,
         self.drop_pkts,
         self.drop_bytes,
         self.drop_rate)




class MatchStatistics(object):
    """  
        Match statistics
    
        type - enum Match.MatchType
        bytes - number of bytes matched in packet streams
    
        """


    def __init__(self, type = 0, pkts = 0, bytes = 0, rate = 0):
        self.type = type
        self.pkts = pkts
        self.bytes = bytes
        self.rate = rate



    @classmethod
    def _from_idl(self, idl):
        return MatchStatistics(idl.match_type, idl.match_pkts, idl.match_bytes, idl.match_rate)



    def __str__(self):
        return '\n                Match Statistics\n                ----------------\n                type    = %d \n                packets = %d \n                bytes   = %d \n                rate    = %d \n            ' % (Match.MatchType.enumval(self.type),
         self.pkts,
         self.bytes,
         self.rate)



from onep.PolicyCommonTypes.ttypes import actionStatsResultIDL
from onep.PolicyCommonTypes.ttypes import classStatsResultIDL
from onep.PolicyCommonTypes.ttypes import matchStatsResultIDL
from onep.policyservice import StorageType
from onep.core.util import enum
import logging

class PolicyStatistics(object):
    """
        Policy statistics class
    
        """


    def __init__(self, storage_type = 0, async_handle = 0, pmap_handle = 0, interfaces = [], total_count = 0, entry_count = 0, more = 0, entry_stats = []):
        self.log = logging.getLogger(__name__)
        self.storage_type = storage_type
        self.async_handle = async_handle
        self.pmap_handle = pmap_handle
        self.interfaces = interfaces
        self.total_count = total_count
        self.entry_count = entry_count
        self.more = more
        self.entry_stats = entry_stats



    @property
    def interfaces(self):
        return self._interfaces



    @interfaces.setter
    def interfaces(self, intfs):
        self._interfaces = intfs



    @property
    def entry_stats(self):
        return self._entry_stats



    @entry_stats.setter
    def entry_stats(self, estats):
        self._entry_stats = []
        for stat in estats:
            self._entry_stats.append(EntryStatistics(stat.time_stamp, stat.last_data_time, stat.classStatsResult, stat.matchStatsResultList, stat.actionStatsResultList))




    def __str__(self):
        estat_str = ''
        for stat in self.entry_stats:
            estat_str = estat_str + str(stat)

        return '\n        Policy Statistics\n        -----------------\n        storage_type - %s\n        async_handle - %d\n        pmap_handle  - %d\n        interfaces   - %s\n        total_count  - %d\n        entry_count  - %d\n        more         - %d\n        %s' % (StorageType.enumval(self.storage_type),
         self.async_handle,
         self.pmap_handle,
         str(self.interfaces),
         self.total_count,
         self.entry_count,
         self.more,
         estat_str)




class EntryStatistics(object):
    """
        Service policy delta statistics
    
        time_stamp     - Time statistics were retrieved
        last_data_time - Last time statistics were retrieved
        class_stats    - class ClassStatistics
        match_stats    - list of dict {type, class MatchStatistics}
        action_stats   - *depends on ActionStatisticType
    
        ActionStatisticType - GENERIC - list of dict {Action.ActionType, packets, bytes}
                              POLICE  - list of dict {Action.ActionType, class PoliceStatistics}
                              QUEUE   - list of dict {Action.ActionType, class QueueStatistics}
    
        """


    def __init__(self, time = 0, last_data_time = 0, class_stats = [], match_stats = [], action_stats = []):
        self.log = logging.getLogger(__name__)
        self.time_stamp = time
        self.last_data_time = last_data_time
        self.class_stats = class_stats
        self.match_stats = match_stats
        self.action_stats = action_stats


    ActionStatisticType = enum(GENERIC=0, POLICE=1, QUEUE=2)

    @property
    def class_stats(self):
        return self._class_stats



    @class_stats.setter
    def class_stats(self, cstats):
        self._class_stats = ClassStatistics._from_idl(cstats)



    @property
    def match_stats(self):
        return self._match_stats



    @match_stats.setter
    def match_stats(self, mstats):
        if mstats:
            for stat in mstats:
                self._match_stats.append(MatchStatistics._from_idl(mstats))

        else:
            self._match_stats = []



    @property
    def action_stats(self):
        return self._action_stats



    @action_stats.setter
    def action_stats(self, astats):
        if astats:
            for stat in astats:
                stats = {}
                stats['type'] = Action.ActionType.enumval(actionStatsResultIDL.action_type)
                if actionStatsResultIDL.action_stat_type == self.ActionStatisticType.POLICE:
                    stats['police'] = PoliceStatistics._from_idl(stat)
                elif actionStatsResultIDL.action_stat_type == self.ActionStatisticType.QUEUE:
                    stats['queue'] = QueueStatistics._from_idl(stat)
                elif actionStatsResultIDL.action_stat_type == self.ActionStatisticType.GENERIC:
                    stats['packets'] = actionStatsResultIDL.action_pkts
                    stats['bytes'] = actionStatsResultIDL.action_bytes
                else:
                    self.log.error('bad action stats ' + str(stat))
                self.action_stats.append(stats)

        else:
            self._action_stats = []



    def __str__(self):
        action_stats_str = ''
        for action_stats in self.action_stats:
            action_stats_str = action_stats_str + str(action_stats)

        match_stats_str = '\n'
        for match_stats in self.match_stats:
            match_stats_str = match_stats_str + str(match_stats)

        return '\n            Entry Statistics\n            ----------------\n            time_stamp     = %d\n            last_data_time = %d\n                %s\n                %s\n                %s\n            ' % (self.time_stamp,
         self.last_data_time,
         str(self.class_stats),
         action_stats_str,
         match_stats_str)




class PoliceStatistics(object):
    """
    This class contains all the information received from the
    Network Element about PoliceStatistics.
    
    @cvar conform_bytes: The conform bytes
    @type conform_bytes:  C{int}
    
    @cvar conform_packets: The conform packets
    @type conform_packets:  C{int}
    
    @cvar conform_rate: The conform rate
    @type conform_rate:  C{int}
    
    @cvar exceed_bytes: The exceed bytes
    @type exceed_bytes:  C{int}
    
    @cvar exceed_packets: The exceed packets
    @type exceed_packets:  C{int}
    
    @cvar exceed_rate: The exceed rate
    @type exceed_rate:  C{int}
    
    @cvar violate_bytes: The violate bytes
    @type violate_bytes:  C{int}
    
    @cvar violate_packets: The violate packets
    @type violate_packets:  C{int}
    
    @cvar violate_rate: The violate rate
    @type violate_rate:  C{int}  
    """


    @property
    def conform_bytes(self):
        return self._conform_bytes



    @property
    def conform_packets(self):
        return self._conform_packets



    @property
    def conform_rate(self):
        return self._conform_rate



    @property
    def exceed_bytes(self):
        return self.exceedBytes



    @property
    def exceed_packets(self):
        return self.exceed_packets



    @property
    def exceed_rate(self):
        return self.exceed_rate



    @property
    def violate_bytes(self):
        return self._violate_bytes



    @property
    def violate_packets(self):
        return self._violate_packets



    @property
    def violate_rate(self):
        return self._violate_rate



    def __init__(self, conform_bytes, conform_packets, conform_rate, exceed_bytes, exceed_packets, exceed_rate, violate_bytes, violate_packets, violate_rate):
        """Constructor of PoliceStatistics."""
        self._conform_bytes = conform_bytes
        self._conform_packets = conform_packets
        self._conform_rate = conform_rate
        self._exceed_bytes = exceed_bytes
        self._exeed_packets = exceed_packets
        self._exceed_rate = exceed_rate
        self._violate_bytes = violate_bytes
        self._violate_packets = violate_packets
        self._violate_rate = violate_rate



    @classmethod
    def _from_idl(cls, astats):
        return PoliceStatistics(astats.conform_bytes, astats.conform_pkts, astats.conform_rate, astats.exceed_bytes, astats.exceed_pkts, astats.exceed_rate, astats.violate_bytes, astats.violate_pkts, astats.violate_rate)



    def __str__(self):
        return '\n                Police Statistics\n                -----------------\n                conform_bytes   = %d\n                conform_packets = %d\n                conform_rate    = %d\n                exceed_bytes    = %d\n                exceed_packets  = %d\n                exceed_rate     = %d\n                violate_bytes   = %d\n                violate_packets = %d\n                violate_rate    = %d\n            ' % (self._conform_bytes,
         self._conform_packets,
         self._conform_rate,
         self._exceed_bytes,
         self._exeed_packets,
         self._exceed_rate,
         self._violate_bytes,
         self._violate_packets,
         self._violate_rate)




class QueueStatistics(object):
    """ QueueStatistics class.
    
    This class gets the information from the Network Element about QueueStatistics.
    """


    def _get_queue_size_bytes(self):
        return self._queue_size_bytes


    _doc_queue_size_bytes = ' Queue Size Bytes.\n     \n    @type: C{long}\n    '
    queue_size_bytes = property(_get_queue_size_bytes, None, None, _doc_queue_size_bytes)

    def _get_queue_size_packets(self):
        return self._queue_size_packets


    _doc_queue_size_packets = ' Queue Size Packets.\n     \n    @type: C{long}\n    '
    queue_size_packets = property(_get_queue_size_packets, None, None, _doc_queue_size_packets)

    def _get_drop_bytes(self):
        return self._drop_bytes


    _doc_drop_bytes = ' Drop Bytes.\n     \n    @type: C{long}\n    '
    drop_bytes = property(_get_drop_bytes, None, None, _doc_drop_bytes)

    def _get_drop_packets(self):
        return self._drop_packets


    _doc_drop_packets = ' Drop Packets.\n     \n    @type: C{long}\n    '
    drop_packets = property(_get_drop_packets, None, None, _doc_drop_packets)

    def _get_flow_drops(self):
        return self._flow_drops


    _doc_flow_drops = ' Flow Drops.\n     \n    @type: C{long}\n    '
    flow_drops = property(_get_flow_drops, None, None, _doc_flow_drops)

    def _get_no_buffer_drops(self):
        return self._no_buffer_drops


    _doc_no_buffer_drops = ' No Buffer Drops.\n     \n    @type: C{long}\n    '
    no_buffer_drops = property(_get_no_buffer_drops, None, None, _doc_no_buffer_drops)

    def _get_out_bytes(self):
        return self._out_bytes


    _doc_out_bytes = ' Out Bytes.\n     \n    @type: C{long}\n    '
    out_bytes = property(_get_out_bytes, None, None, _doc_out_bytes)

    def _get_out_packets(self):
        return self._out_packets


    _doc_out_packets = ' Out Packets.\n     \n    @type: C{long}\n    '
    out_packets = property(_get_out_packets, None, None, _doc_out_packets)

    def __init__(self, queue_size_bytes, queue_size_packets, drop_bytes, drop_packets, flow_drops, no_buffer_drops, out_bytes, out_packets):
        """ Constructor of Class QueueStatistics.
        """
        self._queue_size_bytes = queue_size_bytes
        self._queue_size_packets = queue_size_packets
        self._drop_bytes = drop_bytes
        self._drop_packets = drop_packets
        self._flow_drops = flow_drops
        self._no_buffer_drops = no_buffer_drops
        self._out_bytes = out_bytes
        self._out_packets = out_packets



    @classmethod
    def _from_idl(cls, queue):
        """
        """
        return QueueStatistics(queue.queue_size_bytes, queue.queue_size_pkts, queue.queue_drop_bytes, queue.queue_drop_pkts, queue.queue_drop_flows, queue.queue_no_buffers, queue.queue_out_bytes, queue.queue_out_pkts)



    def __str__(self):
        return '\n                Queue Statistics\n                ----------------\n                queue_size_bytes   = %d\n                queue_size_packets = %d\n                drop_bytes         = %d\n                drop_packets       = %d\n                flow_drops         = %d\n                no_buffer_drops    = %d\n                out_bytes          = %d\n                out_packets        = %d\n            ' % (self._queue_size_bytes,
         self._queue_size_packets,
         self._drop_bytes,
         self._drop_packets,
         self._flow_drops,
         self._no_buffer_drops,
         self._out_bytes,
         self._out_packets)




class ClassStatistics(object):
    """ 
        Class statistic totals
    
        pkts  - Number of classified packets
        bytes - Number of bytes total in classified packet streams
        rate  - Byte rate of classified packets
        drop_pkts  - Number of packets dropped
        drop_bytes - Number of dropped bytes total in classified packet streams
        drop_rate  - Byte rate of dropped packets
    
        """


    def __init__(self, pkts = 0, bytes = 0, rate = 0, drop_pkts = 0, drop_bytes = 0, drop_rate = 0):
        self.pkts = pkts
        self.bytes = bytes
        self.rate = rate
        self.drop_pkts = drop_pkts
        self.drop_bytes = drop_bytes
        self.drop_rate = drop_rate



    @classmethod
    def _from_idl(self, cls):
        return ClassStatistics(cls.classified_pkts, cls.classified_bytes, cls.classified_rate, cls.drop_pkts, cls.drop_bytes, cls.drop_rate)



    def __str__(self):
        return '\n                Class Statistics\n                ----------------\n                packets = %d\n                bytes   = %d\n                rate    = %d\n                dropped packets = %d\n                dropped bytes   = %d\n                dropped rate    = %d\n            ' % (self.pkts,
         self.bytes,
         self.rate,
         self.drop_pkts,
         self.drop_bytes,
         self.drop_rate)




class MatchStatistics(object):
    """  
        Match statistics
    
        type - enum Match.MatchType
        pkts - number of packets matched
        bytes - number of bytes matched in packet streams
        rate  - rate of bytes matched in packet streams
    
        """


    def __init__(self, type = 0, pkts = 0, bytes = 0, rate = 0):
        self.type = type
        self.pkts = pkts
        self.bytes = bytes
        self.rate = rate



    @classmethod
    def _from_idl(self, idl):
        return MatchStatistics(idl.match_type, idl.match_pkts, idl.match_bytes, idl.match_rate)



    def __str__(self):
        return '\n                Match Statistics\n                ----------------\n                type    = %d \n                packets = %d \n                bytes   = %d \n                rate    = %d \n            ' % (Match.MatchType.enumval(self.type),
         self.pkts,
         self.bytes,
         self.rate)




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:22:50 IST
