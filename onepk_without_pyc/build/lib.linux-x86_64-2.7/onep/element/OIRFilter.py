# 2015.02.05 17:18:17 IST
from onep.core.event.EventFilter import EventFilter
from onep.core.util.Enum import enum

class OIRFilter(EventFilter):
    """
       Implements of the EventFilter abstract class for filtering an OIR event
       
       Implements of the EventFilter abstract class for filtering an OIR event
       according to the specified criteria.
    
       A filter can be used to provide fine-tuned control over what events to
       listen to.
       
       """


    def __init__(self):
        """
        Constructs an OIRFilter object without specifying criteria
         
        """
        super(OIRFilter, self).__init__()
        self._oir_type = OIRFilter.OIRType.ONEP_OIR_ALL



    def _get_oir_type(self):
        return self._oir_type



    def _set_oir_type(self, oir_type):
        if oir_type:
            self._oir_type = oir_type
        else:
            self._oir_type = OIRFilter.OIRType.ONEP_OIR_ALL


    _doc_oir_type = '\n    The parameter used by the filter to identify type of OIR event to be \n    listened to. It is of the type OIRFilter.OIRTYPE. If the oir_type is\n    set to none, the default type "ONEP_OIR_ALL" will be used,\n    which will receive notifications for all OIR events.\n    '
    oir_type = property(_get_oir_type, _set_oir_type, _doc_oir_type)

OIRFilter.OIRType = enum('ONEP_OIR_ALL', 'ONEP_OIR_INSERT', 'ONEP_OIR_REMOVE', 'ONEP_OIR_UNKNOWN')

# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:18:18 IST
