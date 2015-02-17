# 2015.02.05 17:22:58 IST
from onep.core.event.EventObject import EventObject
from onep.core.util.OnepConstants import OnepConstants
import logging

class ReplayRouteEvent(EventObject):
    """
    An event which indicates that a routing service replay route event occurred
    in a network element.
    
    @undocumented: __init__
    @undocumented: do_event
    """

    afi = None
    safi = None
    vrf = None
    topology = None
    log = logging.getLogger('onep.' + __name__)

    def __init__(self, element, event_handle, afi, safi, vrf, topology):
        """
        Constructor for the ReplayRouteEvent class. For internal use only.
        """
        super(ReplayRouteEvent, self).__init__(element, event_handle, OnepConstants.EVENT_TYPE_REPLAY_ROUTE)
        self.afi = afi
        self.safi = safi
        self.vrf = vrf
        self.topology = topology



    def do_event(self, source):
        """
        This method specifies which action to do when an event is processed in
        the event queue. For internal use only.
        
        @param source: Source of the event
        @type source: L{NetworkElement<src.element.NetworkElement>}
        """
        dbg = 'ReplayRoute.doEvent: eventHandle = ' + str(self.event_handle)
        self.log.debug(dbg)
        ne = source
        self.log.info('ReplayRouteListener: If a listener is listening to this event, invoke it')
        targetListener = ne.event_manager.get_event_listener(self.event_handle)
        clienData = ne.event_manager.get_event_listener_client_data(self.event_handle)
        if targetListener != None:
            self.log.info('calling listener handle event')
            targetListener.handle_event(self, clienData)




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:22:58 IST
