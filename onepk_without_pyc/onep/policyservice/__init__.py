# 2015.02.05 17:22:49 IST
import logging
from onep.core.util.Enum import enum
StorageType = enum(TRANSIENT=0, PERSISTENT=1)
StatisticCategory = enum(NONE=0, ENTRY=1, MATCH=3, ACTION=5, ALL=7)
from onep.policyservice.bulk import BulkService
from onep.policyservice import match as Match
from onep.policyservice.target import Target
from onep.policyservice.caps import PolicyCapabilities
from onep.policyservice import action as Action

class PolicyQuery(object):
    """
        ***DEPRICATED***
        PolicyQuery class is deprecated.
        Please use caps.PolicyCapabilitiesType enum directly
        ****************
    
        """

    PolicyCapabilitiesType = caps.PolicyCapabilitiesType

    def __init__(self):
        self.log = logging.getLogger(__name__)
        self.log.warning('This class is deprecated. Please use caps.PolicyCapabilitiesType')




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:22:49 IST
