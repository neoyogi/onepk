# 2015.02.05 17:17:57 IST
import logging
from onep.core.event.EventObject import EventObject
from onep.core.event.EventFilter import EventFilter
from onep.core.util.Enum import enum
from onep.core.util.OnepConstants import OnepConstants

class CDPEvent(EventObject):
    """
    An event which indicates that a CDP event occurred in a Network Element.
    
    A CDP event occurs when the neighbor is connected or disconnected, 
    or its capabilities are updated on the neighbor.
    """

    CDPEventNotifyType = enum(ONEP_CDP_ADD=1, ONEP_CDP_UPDATE=2, ONEP_CDP_DELETE=3, ONEP_CDP_ALL=4)

    def __init__(self, sourceNE, eventHandle, ni, notifyType, deviceId, holdTime, mgmtDomain, platform, version, capabilities, inetAddr, neighborIntfName):
        """
         Constructor - used internally
         
        @param  event_handle : Registered event identifier.
        @type event_handle : C{int}
        
        @param  intf : Interface on which the CDP event was received
        @type intf :  L{NetworkInterface<onep.interfaces.NetworkInterface>}
        
        @param  notify_type : CDP notification type add/update/delete
        @type notify_type : C{int}
        
        @param  device_id : Device ID from which the CDP event was received
        @type device_id : C{int}
        
        @param  hold_time : CDP event hold time associated with this event
        @type hold_time : C{int}
        
        @param  mgmt_domain : VTP management domain of the neighbor interface that caused this CDP
        @type mgmt_domain : C{str}
        
        @param  platform : Platform type of the neighbor that caused this CDP event
        @type platform : C{str}
        
        @param  version : OS version running on the neighbor that caused this CDP event
        @type version : C{str}
        
        @param  capabilities : Capabilities
        @type capabilities : L{PolicyCapabilities<onep.policyservice.PolicyCapabilities.PolicyCapabilities>}
        
        @param  inet_addr : Network address
        @type inet_addr : C{str}
        
        @param  neighbor_intf_name : Neighbor interface name
        @type neighbor_intf_name : C{str}
         
         """
        super(CDPEvent, self).__init__(sourceNE, eventHandle, OnepConstants.EVENT_TYPE_CDP)
        CDPEvent.log = logging.getLogger(__name__)
        self.log.debug('CDPEvent is constructed')
        self.event_handle = eventHandle
        self.intf = ni
        self.notify_type = notifyType
        self.device_id = deviceId
        self.hold_time = holdTime
        self.mgmt_domain = mgmtDomain
        self.platform = platform
        self.version = version
        self.capabilities = capabilities
        self.inet_addr = inetAddr
        self.neighbor_intf_name = neighborIntfName



    def do_event(self, ne):
        """
                This method specifies what action to do when an event is processed.
                
                For CDPEvent, the action is invoking the client's event
                listener.
                
                @param ne:
                    The source of the event. For CDPEvent, the source in an
                    instance of NetworkElement.
        
                """
        self.log.debug('cdp EventIDL: event_handle = ' + str(self.event_handle) + ' NetworkInterface = ' + str(self.intf) + ' notify_type = ' + str(self.notify_type) + ' neighbor  = ' + str(self.device_id) + ' hold time = ' + str(self.hold_time) + ' vtp domain = ' + self.mgmt_domain + ' platform = ' + self.platform + ' version = ' + self.version + ' capabilitites = ' + self.capabilities)
        targetListener = ne.event_manager.get_event_listener(self.event_handle)
        clienData = ne.event_manager.get_event_listener_client_data(self.event_handle)
        if targetListener != None:
            targetListener.handle_event(self, clienData)



CDPEvent.log = None

# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:17:57 IST
