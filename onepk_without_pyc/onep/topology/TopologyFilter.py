# 2015.02.05 17:23:16 IST
from onep.core.util.OnepArgumentTypeValidate import *
from onep.topology.TopologyEvent import *

class TopologyFilter:
    """
    This class implements of the EventFilter abstract class for filtering topology
    
    Sample code::
        listener = MyTopologyListener()
        event_type = {}
        event_type.append(TopologyEvent.TopologyEventType.EDGES_ADD)
        event_type.append(TopologyEvent.TopologyEventType.EDGES_DELETE)
        filter = TopolofyFilter(event_type)
        event_handle = topology.add_topology_listener(listener, filter, None)
    
    @undocumented: _set_event_type
    """

    _event_type = None

    def __init__(self, type):
        """
        Constructs a TopologyFilter object without specifying criteria.
        
        @param type: A set of TopologyEventType enum. 
        @type type: L{Enum<onep.core.util.Enum>}
        @raise OnepIllegalArgumentException: The exception is thrown when
        the topology event type received is invalid
        """
        validate_none(type, 'Event type list')
        validate(type, list)
        for type_ in type:
            validate(type_, int)
            if type_ != TopologyEvent.TopologyEventType.EDGES_ADD and type_ != TopologyEvent.TopologyEventType.EDGES_DELETE and type_ != TopologyEvent.TopologyEventType.NODES_ADD and type_ != TopologyEvent.TopologyEventType.NODES_DELETE:
                raise OnepIllegalArgumentException('topology event type', 'invalid')

        self._event_type = type



    def _get_event_type(self):
        return self._event_type



    def _set_event_type(self, event_type):
        validate_none(event_type, 'Event Type')
        validate(event_type, int)
        if type != TopologyEvent.TopologyEventType.EDGES_ADD and type != TopologyEvent.TopologyEventType.EDGES_DELETE and type != TopologyEvent.TopologyEventType.NODES_ADD and type != TopologyEvent.TopologyEventType.NODES_DELETE:
            raise OnepIllegalArgumentException('topology event type', 'invalid')
        self._event_type = type


    _doc = '\n    Gets the list of event types that the filter object is  instantiated with\n    \n    @type: C{list} of L{Enum<onep.util.Enum>}\n    '
    event_type = property(_get_event_type, _set_event_type, _doc)


# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:23:16 IST
