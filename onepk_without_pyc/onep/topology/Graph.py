# 2015.02.05 17:23:16 IST
from onep.core.exception.OnepIllegalArgumentException import OnepIllegalArgumentException
from onep.topology.Edge import Edge
from onep.topology.Node import Node
from onep.topology.NodeConnector import NodeConnector
from onep.core.util.Enum import enum
from onep.core.util.Enum import isValidEnum
from onep.core.util.OnepArgumentTypeValidate import *
import logging
import threading

class Graph(object):
    """
    The Graph class represents the topology graph as seen by a protocol from a
    node. A Graph object contains a collection of Edge objects.
    
    @undocumented: __init__
    """

    _parent_topology = None
    _edge_map = None
    _node_map = None
    _node_connector_map = None
    _log = logging.getLogger(__name__)
    _lock = threading.Lock()

    def __init__(self, topology, edge_list):
        """
        Constructor for internal use only
        """
        from onep.topology.TopologyClass import TopologyClass
        if not isinstance(topology, TopologyClass):
            raise OnepIllegalArgumentException('topology', 'invalid type')
        self._parent_topology = topology
        self._edge_map = {}
        self._node_map = {}
        self._node_connector_map = {}
        validate(edge_list, list)
        for edge in edge_list:
            if not isinstance(edge, Edge):
                raise OnepIllegalArgumentException('edge_list', 'invalid type')
            self._edge_map[str(edge)] = edge
            self._add_to_index(edge)




    def update(self, event_type, list):
        """
                Updates the topology graph object with a list of objects passed,
                based on the topology change events. If the event is:
        
                ONEP_TOPOLOGY_EDGES_ADD - The list should contain a set of EDGE object
                that needs to be added to the graph object.
        
                ONEP_TOPOLOGY_EDGES_DELETE - The list should contain a set of EDGE
                objects that needs to be removed from the graph object.
        
                ONEP_TOPOLOGY_NODES_ADD - The list should contain a set of nodes that
                needs to be added to the graph object.
        
                ONEP_TOPOLOGY_NODES_DELETE - The list should contain a set of
                nodes that needs to be remove to the graph object.
                Removing a node from a graph would also result in removing
                all IN bound and OUT bound edges associated with the node.
        
                Note:
                Adding a node to a graph would only reflect in the output of
                get_node_list() method, and the node remains orphaned.
        
                @param event_type: Type of topology change event.
                @type event_type: L{enum<onep.core.util.Enum>}
                @param list: List of edges or nodes that needs to be updated based on
                @type list: C{list}
        
                @raise OnepIllegalArgumentException: The exception is thrown when the
                input list contains wrong type of element.
                """
        from onep.topology.TopologyEvent import TopologyEvent
        if isValidEnum(TopologyEvent.TopologyEventType, event_type) is False:
            raise OnepIllegalArgumentException('event_type is invalid.')
            return 
        validate(list, type([]))
        if event_type == TopologyEvent.TopologyEventType.EDGES_ADD:
            for obj in list:
                if not isinstance(obj, Edge):
                    raise OnepIllegalArgumentException('Edge is invalid.')
                with self._lock:
                    self._edge_map[str(obj)] = obj
                    self._add_to_index(obj)

            return 
        if event_type == TopologyEvent.TopologyEventType.EDGES_DELETE:
            for obj in list:
                if not isinstance(obj, Edge):
                    raise OnepIllegalArgumentException('Edge is invalid.')
                with self._lock:
                    if self._edge_map.has_key(str(obj)):
                        self._log.debug('update1 removing edge ' + str(obj))
                        del self._edge_map[str(obj)]
                        self._remove_from_index(obj)
                    else:
                        edge_to_remove = self._get_matching_edge_from_map(obj)
                        if edge_to_remove:
                            self._log.debug('update2 removing edge ' + str(edge_to_remove))
                            del self._edge_map[str(edge_to_remove)]
                            self._remove_from_index(edge_to_remove)

            return 
        if event_type == TopologyEvent.TopologyEventType.NODES_ADD:
            for obj in list:
                if not isinstance(obj, Node):
                    raise OnepIllegalArgumentException('Node is invalid.')
                with self._lock:
                    self._node_map[str(obj)] = obj

            return 
        if event_type == TopologyEvent.TopologyEventType.NODES_DELETE:
            for obj in list:
                if not isinstance(obj, Node):
                    raise OnepIllegalArgumentException('Node is invalid.')
                edge_list = self.get_edge_list_by_node(Edge.EdgeType.DIRECTED, obj)
                for edge in edge_list:
                    with self._lock:
                        if self._edge_map.has_key(str(edge)):
                            self._log.debug('update ND removing edge ' + str(edge))
                            del self._edge_map[str(edge)]
                            self._remove_from_index(edge)
                            break
                        else:
                            edge_to_remove = self._get_matching_edge_from_map(edge)
                            if edge_to_remove:
                                self._log.debug('update ND2 removing edge ' + str(edge_in_map))
                                del self._edge_map[str(edge_in_map)]
                                self._remove_from_index(edge_in_map)
                                break

                with self._lock:
                    if self._node_map.has_key(str(obj)):
                        self._log.debug('update2 removing node ' + str(obj))
                        del self._node_map[str(obj)]

            return 



    def concatenate(self, other):
        """
                Concatenate this Graph object with another. The result graph is stored
                in this instance of Graph. Equal nodes(NodeA, NodeA') from the two
                graphs and their corresponding edges are merged to form a single node,
                the new node contains the edges from both the nodes(NodeA, NodeA'). If
                there are equal edges(with the same head and tail node connectors) in
                the two graphs, only one is retained in the original graph
        
                Two CDP nodes are equal if they have same management IP and the hostname.
        
                Two CDP connectors are equal if they have the same IP and the interface
                name.
        
                @param other: The other Graph object to be concatenated with.
                @type other: L{Graph<onep.topology.Graph>}
                @raise OnepIllegalArgumentException: The exception is thrown when
                the input parameter is not a Graph object.
                """
        validate(other, Graph)
        if self.type != other.type:
            raise OnepIllegalArgumentException('other', 'is of different type of Graph')
        for other_edge in other._edge_map.itervalues():
            if self._edge_map.get(str(other_edge)) == None:
                self._edge_map[str(other_edge)] = other_edge
                self._add_to_index(other_edge)
            if self._node_map.get(str(other_edge.head_node)) != None:
                self._node_map[str(other_edge.head_node)] = other_edge.head_node
            if self._node_map.get(str(other_edge.tail_node)) != None:
                self._node_map[str(other_edge.tail_node)] = other_edge.tail_node
            if self._node_connector_map.get(str(other_edge.head_node_connector)) != None:
                self._node_connector_map[str(other_edge.head_node_connector)] = other_edge.head_node_connector
            if self._node_connector_map.get(str(other_edge.tail_node_connector)) != None:
                self._node_connector_map[str(other_edge.tail_node_connector)] = other_edge.tail_node_connector
            for other_key in other._node_map.iterkeys():
                if self._node_map.get(other_key) == None:
                    other_node = other._node_map.get(other_key)
                    self._node_map[other_key] = other_node





    def get_edge_list(self, edge_type):
        """
                Get the list of edges based on the directionality in a grpah
                The method returns a set of edges based on the direction requested
                if DIRECTED edges are requested then the edges to/from Node A and Node B
                are treated as different edges and both edges are returned.
                If UNDIRECTED edges are requested then the graph is assumed symmetric
                and only one edge in this case is returned
        
                @param edge_type: Type of edge either DIRECTED or UNDIRECTED. If the input
                is None, default type DIRECTED will be used
                @type edge_type: C{list} of L{Edge<onep.topology.Edge>}
                """
        if not isValidEnum(Edge.EdgeType, edge_type):
            raise OnepIllegalArgumentException('edge_type is invalid')
        if edge_type == None or edge_type == Edge.EdgeType.DIRECTED:
            return self._edge_map.values()
        else:
            return self._convert_to_undirected_edge_list(self._edge_map.values())



    def _get_node_list(self):
        return self._node_map.values()


    _doc = '\n    Get the list of topology Node objects in the topology Graph.\n\n    @type: C{list} of L{Node<onep.topology.Node>}\n    '
    node_list = property(_get_node_list, None, _doc)

    def get_edge_list_by_node(self, edge_type, node):
        """
                Get the edges connected with specified node in a given direction
                If the input edge_type is DIRECTED then graph is asymmetric
                If the edge_type is UNDIRECTED then graph is symmetric
        
                @param edge_type: The direction  of the edge
                @type edge_type : L{Enum<onep.topology.Enum>}
        
                @param node: The node of interest. The Node object
                must contain the node name
                @type node: L{Node<onep.topology.Node>}
        
                @return: A list of Edges. If no match found empty list is returned
                @rtype: C{list} of L{Edge<onep.topology.Edge>}
                """
        validate(node, Node)
        if not isValidEnum(Edge.EdgeType, edge_type):
            raise OnepIllegalArgumentException('edge_type is invalid')
        edge_list = []
        for edge in self._edge_map.values():
            if node.name == edge._head_node.name and node.address_list is not None and edge._head_node.address_list is not None and set(node.address_list) == set(edge._head_node.address_list):
                edge_list.append(edge)
            if node.name == edge._tail_node.name and node.address_list is not None and edge._tail_node.address_list is not None and set(node.address_list) == set(edge._tail_node.address_list):
                edge_list.append(edge)

        if edge_type == Edge.EdgeType.DIRECTED:
            return edge_list
        else:
            return self._convert_to_undirected_edge_list(edge_list)



    def get_connector_list_by_node(self, node):
        """
                Get the node connectors associated with specified node in the graph
                This method returns the list of node connectors associated with a
                node in a graph. Every time a graph is concatenated with another and
                if new set of node connectors are added to the graph, the list returned
                would be different.
        
                @param node: The node of interest
                @type node: L{Node<onep.topology.Node>}
                @return : A list of NodeConnector. If no match is found, empty list is
                returned. Since the input node can match head node or tail node of a
                connector , it is possible the return list contains duplicate connectors
                """
        validate(node, Node)
        conn_list = []
        for edge in self._edge_map.values():
            if node.name == edge._head_node._name:
                conn_list.append(edge._head_node_connector)
            if node.name == edge._tail_node._name:
                conn_list.append(edge._tail_node_connector)

        return conn_list



    def _get_type(self):
        return self._parent_topology._type


    _doc = 'Type of graph as seen by protocol\n    @type: L{Enum<onep.util.Enum>}\n    '
    type = property(_get_type, None, _doc)

    def __str__(self):
        from onep.topology.TopologyClass import TopologyClass
        edge_buf = ''
        for edge in self._edge_map.values():
            edge_buf += str(edge)

        return 'Graph:\nType: ' + TopologyClass.TopologyType.enumval(self.type) + '\n' + 'Edge list: ' + edge_buf



    def _dispose(self):
        self._edge_map = None
        self._node_map = None
        self._node_connector_map = None



    def _add_to_index(self, edge):
        """
        Add the edge to index tables. For internal use only
        """
        self._node_map[str(edge._head_node)] = edge._head_node
        self._node_map[str(edge._tail_node)] = edge._tail_node
        self._node_connector_map[str(edge._head_node_connector)] = edge._head_node
        self._node_connector_map[str(edge._tail_node_connector)] = edge._tail_node



    def _remove_from_index(self, edge):
        """
        Remove the index from index tables. For internal use only
        """
        head_node = edge._head_node
        if len(self.get_edge_list_by_node(Edge.EdgeType.DIRECTED, head_node)) == 0:
            if self._node_map.has_key(str(head_node)):
                self._log.debug('removing head node ' + str(head_node))
                del self._node_map[str(head_node)]
            else:
                for key in self._node_map.keys():
                    if self._node_map[key]._name == head_node._name and self._node_map[key]._type == head_node._type:
                        self._log.debug('removing head node ' + str(head_node))
                        del self._node_map[key]

        tail_node = edge._tail_node
        if len(self.get_edge_list_by_node(Edge.EdgeType.DIRECTED, tail_node)) == 0:
            if self._node_map.has_key(str(tail_node)):
                self._log.debug('removing tail node ' + str(tail_node))
                del self._node_map[str(tail_node)]
            else:
                for key in self._node_map.keys():
                    if self._node_map[key]._name == tail_node._name and self._node_map[key]._type == tail_node._type:
                        self._log.debug('removing tail node ' + str(tail_node))
                        del self._node_map[key]

        head_conn = edge._head_node_connector
        if len(self._get_edge_list_by_connector(Edge.EdgeType.DIRECTED, head_conn)) == 0:
            if self._node_connector_map.has_key(str(head_conn)):
                self._log.debug('removing head_conn ' + str(head_conn))
                del self._node_connector_map[str(head_conn)]
        tail_conn = edge._tail_node_connector
        if len(self._get_edge_list_by_connector(Edge.EdgeType.DIRECTED, tail_conn)) == 0:
            if self._node_connector_map.has_key(str(tail_conn)):
                self._log.debug('removing tail_conn ' + str(tail_conn))
                del self._node_connector_map[str(tail_conn)]



    def _get_edge_list_by_connector(self, edge_type, conn):
        """
        Get  edge list by connector. For internal use only
        """
        edge_list = []
        for edge in self._edge_map.values():
            if conn.name == edge._head_node_connector._name:
                edge_list.append(edge)
            if conn.name == edge._tail_node_connector._name:
                edge_list.append(edge)

        if edge_type == Edge.EdgeType.DIRECTED:
            return edge_list
        else:
            return self._convert_to_undirected_edge_list(edge_list)



    def _convert_to_undirected_edge_list(self, edge_list):
        """
        Convert directed edge list to undirected. For internal
        use only
        """
        edge_map = {}
        for edge in edge_list:
            keyset = []
            keyset.append(str(edge._head_node))
            keyset.append(str(edge._tail_node))
            keyset.sort()
            key = ''
            for key_item in keyset:
                key += key_item

            edge_map[key] = edge

        return edge_map.values()



    def _get_matching_edge_from_map(self, event_edge):
        """
           This method iterates through the cached edge list to
           find the matching edge that the event has occurred on.
           Note: Unlike Edge equals method, this method does not
           compare the Node's IP address as the event manager does
           not return IP address for remote nodes/edges
           For internal use only.
           @param event_edge: Edge returned by event manager
           @type edge: L{Node<onep.topology.Edge>}
           @return edge_in_map: edge in map that matches the event edge
        """
        for edge_in_map in self._edge_map.values():
            if edge_in_map._head_node._name == event_edge._head_node._name and edge_in_map._tail_node._name == event_edge._tail_node._name and edge_in_map._head_node_connector._name == event_edge._head_node_connector._name and edge_in_map._tail_node_connector._name == event_edge._tail_node_connector._name:
                return edge_in_map





# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:23:16 IST
