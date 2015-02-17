# 2015.02.05 17:22:59 IST
from onep.core.event.EventObject import EventObject
from onep.core.util.OnepConstants import OnepConstants
import logging

class UpdateRouteResponse(EventObject):
    """
    This class indicates response from asynchronous call to update application
    route table.
    
    @undocumented: __init__
    @undocumented: do_event
    """

    scope = None
    rop_list = None
    status = None
    log = logging.getLogger('onep.' + __name__)

    def __init__(self, element, event_handle, scope, rop_list, status):
        """
        Constructor for the UpdateRouteResponse class. For internal use only.
        """
        super(UpdateRouteResponse, self).__init__(element, event_handle, OnepConstants.EVENT_TYPE_UPDATE_ROUTE)
        self.scope = scope
        self.rop_list = rop_list
        self.status = status



    def do_event(self, source):
        """
        This method specifies which action to do when an event is processed in
        the event queue. For internal use only.
        
        @param source: Source of the event
        @type source: L{NetworkElement<onep.element.NetworkElement>}
        """
        dbg = 'ReplayRoute.doEvent: eventHandle = ' + str(self.event_handle)
        ne = source
        self.log.info('UpdateRouteResponse: If a listener is listening to this event, invoke it')
        targetListener = ne.event_manager.get_event_listener(self.event_handle)
        clienData = ne.event_manager.get_event_listener_client_data(self.event_handle)
        if targetListener != None:
            self.log.info('calling listener handle event')
            targetListener.handle_event(self, clienData)




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:22:59 IST
