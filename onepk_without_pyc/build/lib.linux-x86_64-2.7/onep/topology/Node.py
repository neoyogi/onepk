# 2015.02.05 17:20:23 IST
from onep.core.util.Enum import enum
from onep.core.util.Enum import isValidEnum
from onep.core.util.HostIpCheck import HostIpCheck
from onep.interfaces.NetworkInterface import NetworkInterface
from onep.core.util.OnepArgumentTypeValidate import *
from collections import Counter

class Node(object):
    """
    Node class represents topology node discovered via a protocol
    by connecting to a NetworkElement. A Node object can contain
    the identity of a network node like hostname, IP address etc,
    depending how the node was discovered. For example, if the node is
    discovered via CDP, then the Node object contains hostname,
    IP address; if the node is discovered through OSPF or
    any other L3 routing protocol, then the Node object  contains
    only the IP address.
    """

    NodeType = enum('CDP_NODE', 'MEDIA_TRACE_NODE', 'INVALID_NODE_TYPE')
    _name = None
    _type = None
    _address_list = None

    def __init__(self, name, type, address_list):
        """
        @raise OnepIllegalArgumentException: The exception is thrown when
        address received in the address list is None or invalid.
        """
        validate(name, str)
        if isValidEnum(self.NodeType, type) is False:
            raise OnepIllegalArgumentException('type is invalid.')
        validate(address_list, list)
        for addr in address_list:
            validate(addr, str)

        self._name = name
        self._type = type
        self._address_list = address_list
        self.mt_node = None



    def _get_name(self):
        return self._name


    _doc = '\n    Get the hostname of the Node object\n\n    The administratively-assigned name of a node when the node was\n    discovered. The host name of the nodes are available only if\n    the nodes are discovered by CDP. If they are logical nodes\n    discovered through routing protocols then the method returns null.\n\n    @type: C{str}\n    '
    name = property(_get_name, None, _doc)

    def _get_type(self):
        return self._type


    _doc = '\n    Get the node type that Node object is created with.\n    '
    type = property(_get_type, None, _doc)

    def _get_address_list(self):
        return self._address_list


    _doc = '\n    Get IP addresses associated with the Node object. A topology node can\n    contain multiple IP address when nodes are correlated\n    but for CDP this would be only one which denotes the management IP address.\n    '
    address_list = property(_get_address_list, None, _doc)

    @staticmethod
    def _from_idl(node_idl, node_type):
        if node_idl is None or node_type is None:
            return 
        node_name = node_idl.hostname
        addr_list = list()
        na_list = node_idl.addrlist
        if na_list != None:
            for na in na_list:
                inet_addr = NetworkInterface._convert_to_inetaddress(na)
                if inet_addr != None:
                    addr_list.append(inet_addr)

        return Node(node_name, node_type, addr_list)



    @staticmethod
    def _from_out_idl(node_out_idl, node_type):
        """
                Convert TopologyNodeOutIDL to Node object
                This method for internal use only
        
                @param node_out_idl: TopologyNodeOutIDL object
                @param node_type: NodeType node type
                @return: Node object
                """
        if node_out_idl == None or node_type == None:
            return 
        node_name = node_out_idl.hostname
        addr_list = list()
        na_list = node_out_idl.addrlist
        if na_list != None:
            for na in na_list:
                inet_addr = NetworkInterface._convert_to_inetaddress(na)
                if inet_addr != None:
                    addr_list.append(inet_addr)

        return Node(node_name, node_type, addr_list)



    def equals(self, obj):
        """
                Compare two nodes for equality. This method returns true if the two topology nodes
                are equal and the same. For CDP nodes the hostname and the management IP address of
                the node are compared.
        
                @param obj: The other Node object to compare with.
                @return: Returns true if the two topology nodes are equal and the same.
                """
        if obj == None:
            return False
        if not isinstance(obj, Node):
            return False
        if self._type != obj.type:
            return False
        if self._name != obj.name:
            return False
        if Counter(self._address_list) != Counter(obj.address_list):
            return False
        return True



    def __str__(self):
        mgmt = ''
        if self._address_list != None and len(self._address_list) != 0 and self._address_list[0] != None:
            mgmt = self._address_list[0]
        return 'Node[' + self._name + ',' + mgmt + ',' + Node.NodeType.enumval(self._type) + ']'




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:20:23 IST
