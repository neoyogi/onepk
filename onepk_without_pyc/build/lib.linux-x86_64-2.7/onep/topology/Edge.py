# 2015.02.05 17:20:23 IST
from onep.topology.NodeConnector import NodeConnector
from onep.topology.Node import Node
from onep.core.util.OnepArgumentTypeValidate import *
from onep.core.util.Enum import enum

class Edge(object):
    """
    Edge class represents a path as seen by a protocol from one interface (head)
    on a node to an interface (tail) on another node.
    """

    EdgeType = enum('DIRECTED', 'UNDIRECTED')
    _head_node = None
    _tail_node = None
    _head_node_connector = None
    _tail_node_connector = None

    def __init__(self, head_node, head_node_connector, tail_node, tail_node_connector):
        """
        @raise OnepIllegalArgumentException: The exception is thrown when
        one or more of the input arguments is invalid.
        """
        validate_none(head_node, 'head_node')
        validate_none(head_node_connector, 'head_node_connector')
        validate_none(tail_node, 'tail_node')
        validate_none(tail_node_connector, 'tail_node_connector')
        validate(head_node, Node)
        validate(head_node_connector, NodeConnector)
        validate(tail_node, Node)
        validate(tail_node_connector, NodeConnector)
        self._head_node = head_node
        self._tail_node = tail_node
        self._head_node_connector = head_node_connector
        self._tail_node_connector = tail_node_connector



    def _get_head_node(self):
        return self._head_node


    _doc = ' Get the head node of this instance of head\n    @return: Head node object\n    @rtype: L{Node<src.topology.Node>}\n    '
    head_node = property(_get_head_node, None, _doc)

    def _get_head_node_connector(self):
        return self._head_node_connector


    _doc = 'Get the head node connector\n    @return: The head NodeConnector object.\n    '
    head_node_connector = property(_get_head_node_connector, None, _doc)

    def _get_tail_node(self):
        return self._tail_node


    _doc = ' Get the tail Node of this instance of Edge.\n\n    @return: The tail Node object.\n    '
    tail_node = property(_get_tail_node, None, _doc)

    def _get_tail_node_connector(self):
        return self._tail_node_connector


    _doc = ' Get the tail NodeCnnector of this instance of Edge.\n\n    @return: The tail NodeConnector object.\n    '
    tail_node_connector = property(_get_tail_node_connector, None, _doc)

    @staticmethod
    def _from_idl(edge_idl, node_type, conn_type):
        """
                Convert TopologyEdgeIDL to Edge object.
                This method is for internal use only.
        
                @param edge_idl: EdgeIdl object
                @param node_type: NodeType object
                @param conn_type: NodeConnector type
                @return: Edge object
                """
        head_node = Node._from_idl(edge_idl.headnode, node_type)
        tail_node = Node._from_idl(edge_idl.tailnode, node_type)
        head_conn = NodeConnector._from_idl(edge_idl.headconn, conn_type, head_node)
        tail_conn = NodeConnector._from_idl(edge_idl.tailconn, conn_type, tail_node)
        return Edge(head_node, head_conn, tail_node, tail_conn)



    @staticmethod
    def _from_out_idl(edge_idl, node_type, conn_type):
        """
                Convert TopologyEdgeOutIDL to Edge object.
                This method is for internal use only.
        
                @param edge_idl: EdgeIdl object
                @param node_type: NodeType object
                @param conn_type: NodeConnector type
                @return: Edge object
                """
        head_node = Node._from_out_idl(edge_idl.headnode, node_type)
        tail_node = Node._from_out_idl(edge_idl.tailnode, node_type)
        head_conn = NodeConnector._from_out_idl(edge_idl.headconn, conn_type, head_node)
        tail_conn = NodeConnector._from_out_idl(edge_idl.tailconn, conn_type, tail_node)
        return Edge(head_node, head_conn, tail_node, tail_conn)



    def equals(self, obj):
        """
                Compare two Edge object for equality. This method returns true if the two Edge
                are equal and the same.
        
                @param obj: The other Edge object to compare with.
                @type obj: C{Object}
                @return: True if the edge are equal or the same
                @rtype: C{boolean}
                """
        if obj == None:
            return False
        if not isinstance(obj, Edge):
            return False
        if self._head_node.equals(obj.head_node) is False:
            return False
        if self._tail_node.equals(obj.tail_node) is False:
            return False
        if self._head_node_connector.equals(obj.head_node_connector) is False:
            return False
        if self._tail_node_connector.equals(obj.tail_node_connector) is False:
            return False
        return True



    def __str__(self):
        return 'Edge[' + str(self._head_node) + ',' + str(self._head_node_connector) + ',' + str(self._tail_node) + ',' + str(self._tail_node_connector) + ']'




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:20:23 IST
