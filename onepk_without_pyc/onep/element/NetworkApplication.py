# 2015.02.05 17:21:10 IST
import logging
import socket
from time import time
import onep

class NetworkApplication(object):
    """
    NetworkApplication represents the network services consumer delegate and 
    is the owner of onePK application-level property settings and statistics. 
    Only one such instance exists (singleton instance). 
    It is used to instantiate NetworkElements and keeps the collection of 
    NetworkElements instantiated from it.
    
    @undocumented: __init__
    @undocumented: find_element_by_session_handle
    @undocumented: find_element_by_address
    @undocumented: get_default_app_name
    @undocumented: increment_connected_count
    @undocumented: decrement_connected_count
    
    """

    DEFAULT_RDWR_TIMEOUT = 180
    instance_ = None
    DEFAULT_ROOT_CA_CERTS = './nerootca.pem'

    @classmethod
    def get_instance(cls):
        """
                Gets the instance of the NetworkApplication singleton class.
        
                @return: The instance of the NetworkApplication singleton class.
                """
        if cls.instance_ == None:
            cls.instance_ = NetworkApplication()
        return cls.instance_



    def __init__(self):
        """
        Constructor for internal use only.
        """
        self.elementList = []
        self.initDone = False
        self.connectedCount = 0
        self._name = 'onePK_App'
        try:
            self.hostName = socket.gethostname()
        except Exception as e:
            self.hostName = '127.0.0.1'
            logging.debug(e.__str__())



    def find_element_by_session_handle(self, session):
        """
        For internal use only.
        """
        for ne in self.elementList:
            if ne.session_handle._id == session:
                return ne




    def find_element_by_address(self, ipaddr):
        """
        For internal use only.
        """
        for ne in self.elementList:
            if ne.host_address == ipaddr:
                return ne




    def create_network_element(self, address):
        """
                Instantiates a new NetworkElement. 
        
                @param address: Address of the NetworkElement
                @return: The NetworkElement object.
                """
        if self._name == None:
            raise OnepInvalidSettingsException('The application name is not set and default name cannot be determined')
        for ne in self.elementList:
            if ne.host_address == address:
                return ne

        elem = onep.element.NetworkElement(address, self._name)
        elem.parent = self
        self.elementList.append(elem)
        return elem



    def get_network_element(self, elementAddress):
        """
           Gets an instance of the NetworkElement addressed by the elementAddress
           
           Gets an instance of the NetworkElement addressed by the elementAddress,
           which is represented in the InetAddress format.
        
           Instantiates a network element addressed by the 
           elementAddress in the InetAddress format, if it does not
           exist yet.  NetworkApplication can have only one session
           (connection) to a network element. If it exists already,
           the existing instance is returned.
           The newly instantiated network_element is in the initial
           DISCONNECTED state.  Use NetworkElement connect() API to connect 
           to the network element.
         
           @param elementAddress: The element IP address
           @return: An instance of the NetworkElement.
           @raise OnepIllegalArgumentException:P
                       Thrown when the IP address is invalid.
           @raise OnepInvalidSettingsException:
                       Thrown to indicate that the name of application
                       is not properly set and the default name is not available.
           """
        if elementAddress == None or 0 == len(elementAddress):
            raise OnepIllegalArgumentException('elementAddress', 'null/empty')
        return self.create_network_element(elementAddress)



    def _set_name(self, name):
        if self.initDone and self.connectedCount > 0:
            raise OnepInvalidSettingsException('the name cannot be changed after connected to network element.')
        if 125 < len(name):
            self._name = name[0:125]
        else:
            self._name = name



    def _get_name(self):
        return self._name


    name = property(_get_name, _set_name)

    def get_default_app_name(self):
        """
        For internal use only.
        """
        if Thread.currentThread() == None:
            return 
        else:
            stacks = Thread.currentThread().getStackTrace()
            if stacks == None or len(stacks):
                return 
            bottomElement = stacks[len(stacks)]
            if bottomElement == None:
                return 
            className = bottomElement.getClassName()
            if className == None:
                return 
            subStrs = className.split('\\.')
            if subStrs == None or len(subStrs):
                return className
            return subStrs[len(subStrs)]



    def increment_connected_count(self):
        """
        For internal use only.
        """
        self.connectedCount += 1
        if not self.initDone:
            self.initDone = True



    def decrement_connected_count(self):
        """
        For internal use only.
        """
        if self.connectedCount > 0:
            self.connectedCount -= 1




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:21:10 IST
