# 2015.02.05 17:20:23 IST
from onep.core.util.Enum import enum
from onep.core.util.Enum import isValidEnum
from onep.interfaces.NetworkInterface import NetworkInterface
from onep.topology.Node import Node
from onep.core.util.OnepArgumentTypeValidate import *
from onep.core.util.HostIpCheck import HostIpCheck
from collections import Counter

class NodeConnector:
    """
    NodeConnector class represents the logical/physical interfaces forming
    an edge in a topology graph. NodeConnectorc contains identity of a
    network interface including interface name, IP address, etc.
    depending on how the interface was discovered. If the interface
    is discovered through CDP(physical) then it is represented by
    a CDP instantiated node connector object. If the interface is
    discovered through OSPF or any other L3 routing protocol, then
    it is a OSPF instantiated node connector object and contains
    only IP address.
    
    @undocumented: __init__
    """

    NodeConnectorType = enum('ONEP_CDP_CONNECTOR', 'ONEP_INVALID_CONNECTOR_TYPE')
    _node = None
    _name = None
    _type = None
    _address_list = None

    def __init__(self, name, type, node, address_list):
        """
        Constructor For internal use only
        @raise OnepIllegalArgumentException: The exception is thrown if
        any of the input argument is invalid.
        """
        validate(name, str)
        if isValidEnum(self.NodeConnectorType, type) is False:
            raise OnepIllegalArgumentException('type is invalid.')
        if not isinstance(node, Node):
            raise OnepIllegalArgumentException('node is invalid.')
        validate(address_list, list)
        for addr in address_list:
            validate(addr, str)

        self._node = node
        self._name = name
        self._type = type
        self._address_list = address_list



    def _get_name(self):
        return self._name


    _doc = '\n    Get the name of the NodeConnector. This is applicable only if\n    the connector is discovered through protocols such as CDP.\n\n    @type: C{str}\n    '
    name = property(_get_name, None, _doc)

    def _get_node(self):
        return self._node


    _doc = 'Get the node that the NodeConnector object is associated with.\n\n    @type: L{Node<src.topology.Node>}\n    '
    node = property(_get_node, None, _doc)

    def _get_address_list(self):
        return self._address_list


    _doc = 'Get IP addresses associated with the NodeConnector object.\n\n    @type: C{list} of C{str}\n    '
    address_list = property(_get_address_list, None, _doc)

    def _get_type(self):
        return self._type


    _doc = '\n    Get the node type that NodeConnector object is created with.\n    '
    type = property(_get_type, None, _doc)

    @staticmethod
    def _from_idl(connector_idl, connector_type, node):
        """
                Convert a TopologyConnectorIDL object to NodeConnector.
                This method is for internal use only.
        
                @param connector_idl: TopologyConnectorIDL object.
                @param connector_type: ConnectorType object
                @param node: associated node
                @return: A NodeConnector object
                """
        if connector_idl == None or connector_type == None:
            return 
        node_name = connector_idl.connname
        addr_list = []
        na_list = connector_idl.addrlist
        if na_list != None:
            for na in na_list:
                inet_addr = NetworkInterface._convert_to_inetaddress(na)
                if inet_addr != None:
                    addr_list.append(inet_addr)

        return NodeConnector(node_name, connector_type, node, addr_list)



    @staticmethod
    def _from_out_idl(connector_idl, connector_type, node):
        """
                Convert a TopologyConnectorOutIDL object to NodeConnector.
                This method is for internal use only.
        
                @param connector_idl: TopologyConnectorOutIDL object.
                @param connector_type: NodeConnector type
                @param node: The associated node.
                @return: A NodeConnector object
                """
        if connector_idl == None or connector_type == None:
            return 
        node_name = connector_idl.connname
        addr_list = []
        na_list = connector_idl.addrlist
        if na_list != None:
            for na in na_list:
                inet_addr = None
                inet_addr = na.addr
                if inet_addr != None:
                    addr_list.append(inet_addr)

        return NodeConnector(node_name, connector_type, node, addr_list)



    def equals(self, obj):
        """
                Compare two NodeConnector for equality. This method returns true if
                the two NodeConnector are equal and the same. The connectors are equal
                only when the nodes they are housed in are also equal.
        
                @param obj:The other NodeConnector object to compare with.
                @type obj: C{Object}
                @return: returns true if the two NodeConnector are the same
                """
        if obj == None:
            return False
        if not isinstance(obj, NodeConnector):
            return False
        if self._name != obj.name:
            return False
        if self._type != obj.type:
            return False
        if self._node.equals(obj.node) is False:
            return False
        if Counter(self._address_list) != Counter(obj.address_list):
            return False
        return True



    def __str__(self):
        """
                Returns a string representation of the NodeConnector object.
        
                @return: string representation of the object
                @rtype: C{str}
                """
        mgmt = ''
        if self._address_list != None and len(self._address_list) > 0 and self._address_list[0] != None:
            mgmt = self._address_list[0]
        return 'NodeConnector[' + self._name + ',' + mgmt + ',' + NodeConnector.NodeConnectorType.enumval(self._type) + ']'




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:20:24 IST
