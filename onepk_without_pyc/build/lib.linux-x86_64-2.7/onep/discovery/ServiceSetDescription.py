# 2015.02.05 17:18:15 IST
from onep.core.util.Enum import enum

class ServiceSetDescription(object):
    """
    ServiceSetDescription defines a collection of service sets that are grouped
    as an integral unit to provide  a collection of services on a network 
    element. A service set collection is a logical grouping of ONE-P network 
    services providing modular access to a set of network functionality.
    
    The ServiceSetDescription class provides information about the service set 
    name and the version and the network element on which this service set is 
    available.
    
    See L{discover_service_set_list<onep.element.NetworkElement.discover_service_set_list>}
    """

    ServiceSetName = enum('ONEP_SERVICE_SET_ALL', 'ONEP_BASE_SERVICE_SET', 'ONEP_LISP_SERVICE_SET', 'ONEP_VTY_SERVICE_SET', 'ONEP_ONEFW_SERVICE_SET', 'ONEP_MEDIATRACE_SERVICE_SET', 'ONEP_DATAPATH_SERVICE_SET', 'ONEP_ADVRTG_SERVICE_SET')
    _network_element = None
    _service_set_list = dict()

    def __init__(self, networkElement = None, serviceSetList = None):
        """
        Constructor
        
        @param networkElement: 
        @type networkElement: L{NetworkElement<onep.element.NetworkElement>}
        @paramserviceSetlist:
        """
        if networkElement == None and serviceSetList == None:
            self.__init___0()
        else:
            self._network_element = networkElement
            self._service_set_list = serviceSetList



    def __init___0(self):
        pass



    def _get_network_element(self):
        return self._network_element


    _doc = '\n        Gets the network element.\n        \n        @type: L{NetworkElement<onep.element.NetworkElement>}\n        '
    network_element = property(_get_network_element, None, None, _doc)

    def _get_service_set_list(self):
        return self._service_set_list


    _doc = '\n    Gets the HashMap containing the service name and the versions. The HashMap \n    key is the service name as defined in ServiceSetName and the HashMap value \n    is the array of available service set versions. Because a particular \n    service set can have multiple versions, the value associated with each \n    key is an array of strings.\n    \n    @return: The C{dict} containing the service name and the array of available \n    versions.\n    @rtype: C{dict} \n    '
    service_set_list = property(_get_service_set_list, None, None, _doc)


# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:18:15 IST
