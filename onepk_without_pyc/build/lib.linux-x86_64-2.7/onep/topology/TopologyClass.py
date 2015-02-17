# 2015.02.05 17:20:23 IST
from onep.core.exception.OnepRemoteProcedureException import OnepRemoteProcedureException
from onep.core.exception.OnepConnectionException import OnepConnectionException
from onep.core.util.OnepArgumentTypeValidate import *
from onep.TopologyIDL import TopologyIDL
from onep.TopologyIDL.ttypes import TopologyConfigIDL
from onep.topology.Node import *
from onep.topology.NodeConnector import *
from onep.topology.Graph import Graph
from onep.topology.Edge import Edge
from onep.element.NetworkElement import NetworkElement
from Shared.ttypes import ExceptionIDL
from onep.thrift.Thrift import TException
from onep.topology.TopologyListener import TopologyListener

class TopologyClass(object):
    """
        The Topology class represents the network topology as seen by a protocol in
        an element.It provides methods to obtain the topology graph and to register
        listener for receiving topology change events. A topology contains a list
        of edges. Each edge denotes the connectivity between two node connectors
        which in turn are hosted in network nodes.
    
        For protocols such as CDP and EIGRP, the topology will contain only one-hop
        neighbors. For OSPF or any other link state protocol it is possible to
        obtain a complete topology pertaining to an area.
    
        A Topology object will provide only the topology graph and report topology
        changes as seen by an element. In the case where the application chooses
        to obtain incremental topology by connecting to each discovered node, then
        a new Topology object should  be instantiated using the new node.
    
        Example:
        #Get NetworkElement and connect to it
    
        network_element = element.NetworkElement.NetworkElement("127.0.0.1","pythonapp")
        handle = network_element.connect("cisco", "cisco")
    
        # create a Topology object based on Topology Type
        # The Topology object will keep a Graph object and will also keep the graph
        # updated based on the events received
        # The latest graph can be obtained by using the graph property
        topology = TopologyClass(network_element, Topology.TopologyType.CDP)
    
        # Get the Graph object which reflect the current snapshot.
        graph = topology.get_graph()
    
        # A topology Graph contains a list of Edge objects. We can traverse the
        # Graph by visiting each Edge object in the list.
    
        for (edge in graph.get_edge_list(Edge.EdgeType.UNDIRECTED)):
            edge_count = 1
    
            print "Edge #" + str(edge_count)
            edge_count += 1
    
        # Every Edge object has a head NodeConnector and tail NodeConnector
        # on its two ends.
        edge_connector = edge.head_node_connector
        tail_connector = edge.tail_node_connector
    
        # Each NodeConnector in turn is housed in a topology Node.
        head_node = head_connector.node
        tail_node = tail_connector.node
    
        # print information of connectors and nodes
    
        print "Head Connector name " + head_connector.name + ",type = " + str(head_connector.type)
        print "Head Node :" + head_node.name + ",type = " + str(head_node.type)
    
        # Print information of connectors and nodes
    
        for addr in headnode.address_list:
            print " address: " + addr
    
        print "Tail Connector name :" + tail_connector.name + ",type = " + str(tail_connector.type)
        print "Tail Node: " + tail_node.name + "type = " + str(tail_node.type)
    
        for addr in tail_node.address_list:
            print "address : " + addr
    
        class MyTopologyListener(TopologyListener):
            def handle_event(self, event, clientData):
                print "-------------"
                print Topology Event
                print "-------------"
    
        listener = MyTopologyListener()
        event_type = []
        event_type.append(TopologyEvent.TopologyEventType.EDGES_ADD)
        event_type.append(TopologyEvent.TopologyEventType.EDGES_DELETE)
    
        filter = TopologyFilter(event_type)
        event_handle = topology.add_topology_listener(listener, filter, None)
    
        """

    _network_element = None
    _type = None
    _topology_client = None
    _key = None
    _counter = 0
    _topology_key_map = None
    _filter_map = None
    _cached_graph = None
    TopologyType = enum('CDP')

    def __init__(self, element, type):
        """
                Construct a Topology object as seen by a protocol in an element.
        
                @param element: The NetworkElement from which to initiate the
                discovery of topology.
                @type element: L{NetworkElement<src.element.NetworkElement>}
                @param type: Type of topology as seen by a protocol
                @type type: L{int}
                @raise OnepIllegalArgumentException: The exception is thrown when
                element or type is not valid
                """
        if element == None:
            raise OnepIllegalArgumentException('element', 'invalid')
        if type == None:
            raise OnepIllegalArgumentException('type', 'invalid')
        validate(element, NetworkElement)
        validate(type, int)
        if type not in range(0, 567):
            raise OnepIllegalArgumentException('Invalid', 'type')
        self._network_element = element
        self._type = type
        TopologyClass._counter += 1
        self._key = TopologyClass._counter
        TopologyClass._topology_key_map = {}
        TopologyClass._topology_key_map[self._key] = self
        try:
            self.get_graph()
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e)



    def _get_network_element(self):
        return self._network_element


    _doc = 'Get the NetworkElement from which the discovery of\n    topology is initiated.\n    @type: L{NetworkElement<src.element.NetworkElement>}\n    '
    network_element = property(_get_network_element, None, _doc)

    def _get_type(self):
        return self._type


    _doc = 'Type of topology as seen by a protocol.\n    @type: L{Enum<src.core.util.Enum>}\n    '
    type = property(_get_type, None)

    def get_graph(self):
        """
                Get the topology graph that represents the current snapshot of the
                topology. This method assumes that the network element is connected.
                If it is not,OnepConnectionException will be thrown.
        
                @raise OnepConnectionException: The exception is thrown when the
                network element is not connected.
                @raise OnepRemoteProcedureException: The exception is thrown when an
                error has occurred in the remote procedure call made to a network element
        
                @return: The Graph object representing the current snapshot of the topology.
                """
        if not self._network_element.is_connected():
            self._topology_client = None
            raise OnepConnectionException()
        if self._topology_client == None:
            self._topology_client = TopologyIDL.Client(self._network_element.api_protocol)
            if self._topology_client == None:
                raise OnepConnectionException('Unable to create Topology client instance')
        config_idl = TopologyConfigIDL(self._type, 0)
        session_handle = self._network_element.session_handle._id
        try:
            edge_list = []
            idl_list = self._topology_client.NetworkElement_getEdgeListIDL(session_handle, config_idl)
            node_type = Node.NodeType.INVALID_NODE_TYPE
            conn_type = NodeConnector.NodeConnectorType.ONEP_INVALID_CONNECTOR_TYPE
            if self._type == self.TopologyType.CDP:
                node_type = Node.NodeType.CDP_NODE
                conn_type = NodeConnector.NodeConnectorType.ONEP_CDP_CONNECTOR
            for edge_idl in idl_list:
                if edge_idl != None:
                    edge_list.append(Edge._from_idl(edge_idl, node_type, conn_type))

            self._cached_graph = Graph(self, edge_list)
            return Graph(self, edge_list)
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e)



    def add_topology_listener(self, listener, filter, client_data):
        """
                Adds a topology event listener to the Topology object.
        
                @param listener:  The TopologyListener object that handles the events.
                @type listener: L{TopologyListener<src.topology.TopologyListener>}
        
                @param filter: The TopologyFilter to specify criteria of interested
                topology events
                @type filter: L{TopologyFilter<src.topology.TopologyFilter>}
        
                @param client_data: The client data associated with the listener.
                This client data will be part of input parameters when the handleEvent
                method in the listener is invoked.
                @type client_data : C{object}
        
                @return event_handle:  a numeric ID associated with this event
                registration. The eventHandle is used to unregister the listener
                using the removeEventListener method. If registration fails, -1
                is returned.
                @rtype event_handle: C{int}
        
                @raise OnepIllegalArgumentException: The exception is thrown when
                listener or filter is not valid
        
                @raise OnepConnectionException: The exception is thrown when connection
                to a network element has failed
        
                @raise OnepRemoteProcedureException: The exception is thrown when an
                error has occurred in the remote procedure call made to a network element
        
                @raise OnepException: The exception is thrown when an internal error occurs
                """
        from onep.topology.TopologyFilter import TopologyFilter
        if listener == None:
            raise OnepIllegalArgumentException('listener', 'None')
        if not isinstance(listener, TopologyListener):
            raise OnepIllegalArgumentException('listener', 'invalid type')
        if filter == None:
            raise OnepIllegalArgumentException('filter', 'None')
        if not isinstance(filter, TopologyFilter):
            raise OnepIllegalArgumentException('filter', 'invalid type')
        session = self._network_element.session_handle
        event_manager = self._network_element.event_manager
        if self._topology_client == None:
            self._topology_client = TopologyIDL.Client(self._network_element.api_protocol)
            if self._topology_client == None:
                raise OnepConnectionException('Unable to create Topology client instance')
        if self._topology_client == None or session == None or event_manager == None:
            raise OnepConnectionException('')
        config_idl = TopologyConfigIDL(self._type, 0)
        try:
            event_prop = self._topology_client.TopologyChange_Event_registerIDL(session._id, self._key, config_idl)
            if event_prop != None:
                event_manager.add_listener(event_prop.eventHandle, listener, client_data)
                TopologyClass._filter_map = {}
                TopologyClass._filter_map[event_prop.eventHandle] = filter
                return event_prop.eventHandle
            raise OnepConnectionException('')
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e)



    def remove_topology_listener(self, event_handle):
        """
                Removes the topology event listener. This method will remove the listener
                associated with the specified eventHandle and also remove the
                corresponding registered event on the NetworkElement
        
                @param event_handle: Registered event identifier
                @type event_handle: C{int}
        
                @raise OnepIllegalArgumentException: The exception is thrown when
                event_handle is not valid or unregistered already
                @raise OnepRemoteProcedureException: The exception is thrown when
                an error has occured in remote procedure call made to a network
                element.
                @raise OnepException: The exception is thrown when connection
                to a network element has failed
                """
        self._network_element.event_manager.remove_listener(event_handle)



    @staticmethod
    def _get_topology(key):
        return TopologyClass._topology_key_map[key]



    @staticmethod
    def _get_filter_by_event_handle(handle):
        return TopologyClass._filter_map[handle]




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:20:23 IST
