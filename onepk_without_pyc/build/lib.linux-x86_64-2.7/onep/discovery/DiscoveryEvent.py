# 2015.02.05 17:18:15 IST
from onep.core.event.EventObject import EventObject
from onep.core.util import OnepConstants
from onep.core.util import Version
import logging

class DiscoveryEvent(EventObject):
    """
    The DiscoveryEvent returns the event information associated with the 
    service set discovery event trigger. 
    
    The service set discovery event is triggered by the network element 
    when a given service set is enabled or disabled on a network element. The 
    DiscoveryEvent contains information about the name and version of the 
    service set and information about the service set state change that 
    triggered the event notification.
    The DiscoveryEvent also returns the information about the network element
    on which the service set change occurred, including the directly connected 
    neighbors of the root network element. When a service set discovery occurs, 
    the DiscoveryEvent is passed to the event callback handler.
    
    @ivar description: Gets the service set description for which the event 
    was triggered.
    @type description: L{Enum<onep.core.util.Enum>}
    
    @ivar state: Gets the new service set state that caused the event trigger.
    @type state: L{Enum<onep.core.util.Enum>}
    
    @ivar version: Gets the service sets version for which the event was 
    triggered.
    @type version: L{Version<onep.core.util.Version.Version>}
    
    @ivar ip_address : Gets the IP address for the network element for which 
    the service change notification was received. 
    @type ip_address: C{str}
    
    @ivar type_: Gets the new service set discovery type.
    @type type_: L{Enum<onep.routing.Enum>} defined in L{DiscoveryFilter<src.discovery.DiscoveryFilter>}
    
    @undocumented: __init__
    @undocumented: do_event
    """

    description = None
    state = None
    version = None
    ip_address = None
    type_ = None
    log = logging.getLogger('onep.' + __name__)

    def __init__(self, srcElement, eventID, type_, desc, state, version, discoveredIP):
        """
        Constructs a ServiceDiscoveryEvent object with the service sets attributes.
        
        Internal use only
        """
        super(DiscoveryEvent, self).__init__(srcElement, eventID, OnepConstants.EVENT_TYPE_DISCOVERY)
        self.type_ = type_
        self.description = desc
        self.state = state
        self.version = Version(version.major, version.minor, version.maint)
        self.ip_address = discoveredIP



    def do_event(self, source):
        """
        This method specifies which action to take when an event is processed 
        in the event queue. For ServiceDiscoveryEvent, the action is invoking 
        the client's event listener
               
        For internal use only
        """
        dbg_msg = 'SS discovery EventIDL: session Handle = ' + str(self.src_ne.session_handle._id)
        if self.event_handle:
            dbg_msg += ' eventHandle = ' + str(self.event_handle)
        if self.description:
            dbg_msg += ' Service Set name = ' + str(self.description)
        if self.type_:
            dbg_msg += ' discoveryType = ' + str(self.type_)
        if self.ip_address:
            dbg_msg += ' ip address  = ' + str(self.ip_address)
        if self.state:
            dbg_msg += ' new service state = ' + str(self.state)
        self.log.debug(dbg_msg)
        ne = source
        targetListener = ne.event_manager.get_event_listener(self.event_handle)
        clienData = ne.event_manager.get_event_listener_client_data(self.event_handle)
        if targetListener != None:
            targetListener.handle_event(self, clienData)




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:18:15 IST
