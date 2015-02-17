#!/usr/bin/env python

# 
# * Copyright (c) 2010-2013 by Cisco Systems, Inc.
# *
# * THIS SAMPLE CODE IS PROVIDED "AS IS" WITHOUT ANY EXPRESS OR IMPLIED WARRANTY
# * BY CISCO SOLELY FOR THE PURPOSE of PROVIDING PROGRAMMING EXAMPLES.
# * CISCO SHALL NOT BE HELD LIABLE FOR ANY USE OF THE SAMPLE CODE IN ANY
# * APPLICATION.
# *
# * Redistribution and use of the sample code, with or without
# * modification, are permitted provided that the following conditions
# * are met:
# * Redistributions of source code must retain the above disclaimer.
# 
# package: tutorials.topology

"""
  The goal of this tutorial is to show how to get the Network element's 
  topology graph and neighbor network element's information. 
  This tutorial will also show how to register a CDP listener and 
  handle the event when there's a topology change in the neighbors 
  of the Network Element.
"""
import sys
import logging

from BaseTutorial import BaseTutorial
from onep.element import NetworkElement
from onep.core.exception import OnepIllegalArgumentException
from onep.core.exception import OnepException
from onep.core.exception import OnepRemoteProcedureException
from onep.topology import TopologyListener
from onep.topology import TopologyEvent
from onep.topology import TopologyClass
from onep.topology import TopologyFilter
from onep.topology import Edge
from time import sleep

from onep.core.util import enum
logger = logging.getLogger('onep:TopologyTutorial')
logger.setLevel(logging.INFO)

"""
  An example Topology Listener event handler  
""" 
#  START SNIPPET: ExampleTopologyListener
class ExampleTopologyListener(TopologyListener):
    
    name = str()
    
    """
      Creates an Example Topology Event Listener.
      @param name
            Identifies the instance.
    """
    def __init__(self, name):        
        super(TopologyListener, self).__init__()
        self.name = name

    """
      Invoked when an event is received from a network element.
      @param event
                 An event object that indicates that an event has occurred in a network element.
      @param clientData
                 The clientData is an object that is passed in when the application calls an API to add/register
                 the event listener. The application is responsible for casting the input clientData to the
                 appropriate class before using it.
    """    
    def handle_event(self, event, clientData):
        
        print "\nReceived Topology Event from " + self.name
        for type in event.types:
            if (type == TopologyEvent.TopologyEventType.EDGES_ADD):
                print "Some edges were added"
            if (type == TopologyEvent.TopologyEventType.EDGES_DELETE):
                print "Some edges were deleted"
            if (type == TopologyEvent.TopologyEventType.NODES_ADD):
                print "Some nodes were added"
            if (type == TopologyEvent.TopologyEventType.NODES_DELETE):
                print "Some nodes were deleted"
        print "No of edges changed" , len(event.edge_list)
#  END SNIPPET: ExampleTopologyListener
    
"""
Invokes the tutorial
"""
class TopologyTutorial(BaseTutorial):
    
    TWENTY_SEC = 10    
    
    """
      Obtain a Topology instance from the NetworkElement for TopologyType.CDP
      and print the Topology graph information.
      
      @return A Topology instance.
      @throws OnepException
                  If there is an error.     
    """
    def discoverCDPTopology(self, network_element):        
        #  START SNIPPET: discoverCDPTopology
        #  Create a topology object
        topology = TopologyClass(network_element, TopologyClass.TopologyType.CDP)
        #  Get the graph object 
        graph = topology.get_graph()
        #  Get the list of edges from the Graph object. 
        edgeList = graph.get_edge_list(Edge.EdgeType.UNDIRECTED)
        #  Get the Node and Node connectors          
        edge_count  = 0
        if len(edgeList) > 0:
            for edge in edgeList:
                edge_count += 1
                print "*** Edge no" , edge_count
            
                print "Local Host (Head node) is: ", edge.head_node
                print "Remote Host (Tail node) is :", edge.tail_node
                print "Local interface (Head node connector) is:", edge.head_node_connector
                print "Remote interface (Tail node connector) is:", edge.tail_node_connector
        else:
            print "There are no edges."
        #  END SNIPPET: discoverCDPTopology

if __name__ == '__main__':
    """
    Invokes the tutorial via the command line. This main method attempts to use arguments from the command line.
    """
    tutorial = TopologyTutorial(sys.argv)
    logger.info("Reading arguments ...")
    if not tutorial.parse_command_line():
        logger.error("Error in parsing arguments")
        sys.exit(1)
    try:
        logger.info("Connecting to Network Element...")
        if not tutorial.connect("TopologyTutorial"):
            logger.error("Error in connecting to network element")
            sys.exit(1)

        print "Connected to Network Element " + str(tutorial.get_element_hostname())      
 
        network_element = tutorial.get_network_element()
        
        print "Priting the topology graph..."
        tutorial.discoverCDPTopology(network_element)
        
        print "\nAdding Topology event listener on the network element..."
        #  START SNIPPET: addTopologyListener
        listener = ExampleTopologyListener("TopologyListener1")
        topology = TopologyClass(network_element, TopologyClass.TopologyType.CDP)
        event_type = []
        event_type.append(TopologyEvent.TopologyEventType.EDGES_ADD)
        event_type.append(TopologyEvent.TopologyEventType.EDGES_DELETE)
        filter = TopologyFilter(event_type)
        event_handle = topology.add_topology_listener(listener, filter, "TopologyClient1")
        #  END SNIPPET: addTopologyListener
        
        print "\nTo trigger a topology event, telnet to the connected device and shutdown one of the connector interface"
        print "Waiting for event ....."
        sleep(tutorial.TWENTY_SEC)
        
        print "\nRemoving Topology listener..."
        topology.remove_topology_listener(event_handle)
    except Exception as e:
        print e
    finally:
        print "Disconnecting from the Network Element"
        tutorial.disconnect()
        sys.exit(0)

 


