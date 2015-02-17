# 2015.02.05 17:20:24 IST
from onep.topology.TopologyClass import TopologyClass
from onep.core.event.EventObject import EventObject
from onep.core.util.OnepConstants import OnepConstants
from onep.core.util.Enum import enum
from onep.topology.Edge import Edge
from onep.topology.Node import Node
from onep.topology.NodeConnector import NodeConnector
import threading
import logging

class TopologyEvent(EventObject):
    """
        An event which indicates that a Topology event occurred in a network element.
        
        Sample code::
        
            class MyTopologyListener(TopologyListener):
                def handle_event(self, event, clientData):
                    print "Received Topology Event"
                    if event.type == TopologyEvent.EventType.EDGES_ADD:
                        print "Some edges are added"
                    if event.type = TopologyEvent.EventType.EDGES_DELETE:
                        print "Some edges are removed"
                    print "Number of edges in new topology" 
                    print len(event.edge_list)
        
            # Create a Topology based on Topology type
            # The Toplogy object will contain Graph object and will keep the graph updated based
            # on the events received The latest graph can be obtained 
            # using get_graph method
            
            topology = TopologyClass(ne, Topology.TopologyType.CDP)
            graph = topology.get_graph()
            
            listener = MyTopologyListener()
            event_type = list()
            event_type.append(TopologyEvent.TopologyEventType.EDGES_ADD)
            event_type.append(TopologyEvent.TopologyEventType.EDGES_DELETE)
            
            filter = TopologyFilter(event_type)
            event_handle = topology.add_listener(listener, filter, None)
        
    
        @undocumented: do_event
        @undocumented: __init__
        """

    TopologyEventType = enum(EDGES_ADD=1, EDGES_DELETE=2, NODES_ADD=4, NODES_DELETE=8)
    _log = logging.getLogger(__name__)
    _lock = threading.Lock()
    _topology = None
    _tp_event_types = None
    _edge_list = None

    def __init__(self, element, event_handle, topology_handle, types, edge_list):
        """
        Constructor for TopologyEvent class
        
        @param element: The Network Element in which the topology event occured.
        @type element: L{NetworkElement<onep.element.NetworkElement>}
        @param event_handle: Event handle is a unique ID to identify which 
        event listener should receive the event .
        @type event_handle: C{int}
        @param topology_handle: A handle/key of topology the sends the events
        @type topology_handle: C{int}
        @param types: A set of TopologyTypeEvent enum representing types of 
        changes
        @type types: C{list} of L{Enum<onep.core.util.Enum>}
        @param edge_list: List of edges representing the changes
        @type edge_list: C{list} of L{onep.topology.Edge>}
        """
        super(TopologyEvent, self).__init__(element, event_handle, OnepConstants.EVENT_TYPE_TOPOLOGY)
        self._topology = TopologyClass._get_topology(topology_handle)
        self._tp_event_types = types
        self._edge_list = edge_list



    def _get_topology(self):
        return self._topology


    _doc = ' \n    return the Topology object\n    @type: L{onep.topology.TopologyClass>}\n    '
    topology = property(_get_topology, None, _doc)

    def _get_types(self):
        return self._tp_event_types


    _doc = '\n    Gets the list of TopologyEventType enum representing the types of changes.\n    \n    @type: C{list} of L{Enum<onep.util.Enum>}\n    '
    types = property(_get_types, None, _doc)

    def _get_edge_list(self):
        return self._edge_list


    _doc = '\n    Gets the list of edges representing the changes\n    \n    @type : C{list} of L{Edge<onep.topology.Edge>}\n    '
    edge_list = property(_get_edge_list, None, _doc)

    def get_node_list(self):
        """
        Get the node list associated with the event.
        
        @return: A list of nodes
        @rtype: C{list} of L{Node<onep.topology.Node>}
        """
        node_list = []
        if self._edge_list:
            for edge in self._edge_list:
                node_list.append(edge._head_node)
                node_list.append(edge._tail_node)

        return node_list



    def do_event(self, source):
        """
        This method specifies what action to do when a event is processed 
        in the event queue. For Topology Event, the action is invoking client's 
        event listener
        
        @param source: The source of the event. For Topology Event, the source 
        in an instance of NetworkElement
        @type source: L{NetworkElement<onep.element.NetworkElement>}
        """
        dbg = 'TopologyEvent.doEvent: eventHandle = ' + str(self.event_handle)
        self._log.debug(dbg)
        ne = source
        targetListener = ne.event_manager.get_event_listener(self.event_handle)
        filter = TopologyClass._get_filter_by_event_handle(self.event_handle)
        final_event_types = self._get_matched_event_type_list(self._tp_event_types, filter, self)
        if final_event_types:
            self._tp_event_types = final_event_types
        else:
            self._log.debug('Skip topology event, no listener is interested.')
            return 
        if targetListener:
            clientData = ne.event_manager.get_event_listener_client_data(self.event_handle)
            targetListener.handle_event(self, clientData)
        self._log.debug('Topology doEvent complete')



    def _get_matched_event_type_list(self, tp_event_types, filter, event):
        """
        This method processes the events returned by the network element and  
        compares them with the local/cached graph. It identifies if Edges delete or
        edges add have resulted into Nodes delete or Nodes add events too and updates
        the local/cached graph accordingly. For internal use only.
        @param tp_event_types: the events
        @type tp_event_types: C{list} of L{Enum<onep.util.Enum>}
        @param filter: The TopologyFilter to specify criteria of interested
        topology events
        @type filter: L{TopologyFilter<src.topology.TopologyFilter>}        
        @param event: An event object which indicates that an event occurred
                in a network element
        @type event: L{TopologyEvent<src.topology.TopologyEvent>}
        @return: A list of matched event types
        @rtype: C{list} of L{Enum<onep.util.Enum>}
        """
        filter_criteria = filter._event_type
        events_list = []
        if filter_criteria:
            for et in filter_criteria:
                if et == TopologyEvent.TopologyEventType.EDGES_ADD:
                    if TopologyEvent.TopologyEventType.EDGES_ADD in tp_event_types:
                        events_list.append(et)
                elif et == TopologyEvent.TopologyEventType.EDGES_DELETE:
                    if TopologyEvent.TopologyEventType.EDGES_DELETE in tp_event_types:
                        events_list.append(et)
                elif et == TopologyEvent.TopologyEventType.NODES_ADD:
                    if TopologyEvent.TopologyEventType.NODES_ADD in tp_event_types:
                        events_list.append(et)
                    elif TopologyEvent.TopologyEventType.EDGES_ADD in tp_event_types:
                        if self._contains_new_node(event._edge_list, event._topology):
                            self._log.debug('NODES_ADD: found new node')
                            events_list.append(et)
                elif et == TopologyEvent.TopologyEventType.NODES_DELETE:
                    if TopologyEvent.TopologyEventType.NODES_DELETE in tp_event_types:
                        self._log.debug('NODES_DELETE: found node delete')
                        events_list.append(et)
                    elif TopologyEvent.TopologyEventType.EDGES_DELETE in tp_event_types:
                        if self._contains_dangling_node(event._edge_list, event._topology):
                            self._log.debug('NODES_DELETE: found dangling node')
                            events_list.append(et)

        for etype in tp_event_types:
            if etype in (TopologyEvent.TopologyEventType.EDGES_ADD, TopologyEvent.TopologyEventType.EDGES_DELETE):
                event._topology._cached_graph.update(etype, event._get_edge_list())
            if etype in (TopologyEvent.TopologyEventType.NODES_ADD, TopologyEvent.TopologyEventType.NODES_DELETE):
                event._topology._cached_graph.update(etype, event._get_node_list())

        return events_list



    def _contains_new_node(self, edge_list, topology):
        """
            This method returns true if a new node is found.
            For internal use only.
            @param edge_list: List of Edges
            @type edge_list: C{list} of L{onep.topology.Edge>}
            @param topology: TopologyClass
            @type topology: L{TopologyClassr<src.topology.TopologyClass>}        
            @return: True if a new node is found else False
        """
        if edge_list:
            for edge in edge_list:
                if self._is_node_exists(edge._head_node, topology):
                    if self._is_node_exists(edge._tail_node, topology):
                        return False

        else:
            raise OnepIllegalArgumentException('EdgeList is invalid.')
        return True



    def _is_node_exists(self, node, topology):
        """
         This method iterates through the cached graph to find
         if the node already exists or not
         For internal use only.
         @param node: Node to be found
         @type node: L{Node<onep.topology.Node>}
         @param topology: TopologyClass
         @type topology: L{TopologyClassr<src.topology.TopologyClass>}        
         @return: True if the node exists else False
        """
        if topology and topology._cached_graph:
            with self._lock:
                for cnode in topology._cached_graph._get_node_list():
                    if node._name == cnode._name:
                        return True

        else:
            raise OnepIllegalArgumentException('Invalid Topology params.')
        return False



    def _contains_dangling_node(self, edge_list, topology):
        """
         This method returns true if it finds a Node that has no
         connection to another node.
         For internal use only.
         @param edge_list: List of Edges
         @type edge_list: C{list} of L{onep.topology.Edge>}
         @param topology: TopologyClass
         @type topology: L{TopologyClassr<src.topology.TopologyClass>}        
         @return: True if a dangling node is found else False
        """
        if edge_list:
            for edge in edge_list:
                if self._get_edge_count_by_node(edge._head_node, topology) <= 1:
                    return True
                if self._get_edge_count_by_node(edge._tail_node, topology) <= 1:
                    return True

        else:
            raise OnepIllegalArgumentException('EdgeList is invalid.')
        return False



    def _get_edge_count_by_node(self, node, topology):
        """
         This method iterates through the cached graph to find
         the number of connections a node has.
         For internal use only.
         @param node: Node to be found
         @type node: L{Node<onep.topology.Node>}
         @param topology: TopologyClass
         @type topology: L{TopologyClassr<src.topology.TopologyClass>}        
         @return count: number of connections a node has
        """
        if not node or not topology or not topology._cached_graph:
            raise OnepIllegalArgumentException('Invalid Topology params.')
        with self._lock:
            edge_list = topology._cached_graph.get_edge_list(Edge.EdgeType.DIRECTED)
            if edge_list:
                count = 0
                for edge in edge_list:
                    if edge:
                        if node._name == edge._head_node._name:
                            count = count + 1
                        if node._name == edge._tail_node._name:
                            count = count + 1

                return count
            raise OnepIllegalArgumentException('EdgeList is invalid.')



    @staticmethod
    def _convert_type_list_to_bitmip(type_list):
        bitmask = 0
        for st in type_list:
            bitmask |= st

        return bitmask



    @staticmethod
    def convert_type_bitmip_to_list(type_mask):
        type_list = []
        if type_mask & TopologyEvent.TopologyEventType.EDGES_ADD > 0:
            type_list.append(TopologyEvent.TopologyEventType.EDGES_ADD)
        if type_mask & TopologyEvent.TopologyEventType.EDGES_DELETE > 0:
            type_list.append(TopologyEvent.TopologyEventType.EDGES_DELETE)
        if type_mask & TopologyEvent.TopologyEventType.NODES_ADD > 0:
            type_list.append(TopologyEvent.TopologyEventType.NODES_ADD)
        if type_mask & TopologyEvent.TopologyEventType.NODES_DELETE > 0:
            type_list.append(TopologyEvent.TopologyEventType.NODES_DELETE)
        return type_list




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:20:24 IST
