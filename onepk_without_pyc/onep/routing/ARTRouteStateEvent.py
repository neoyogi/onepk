# 2015.02.05 17:22:59 IST
from onep.core.util.OnepConstants import OnepConstants
from onep.core.event.EventObject import EventObject
import logging

class ARTRouteStateEvent(EventObject):
    """An event which indicates that a route state event occurred in
    a network element.
    
    @undocumented: __init__
    @undocumented: do_event
    """

    _scope = None
    _route = None
    _state = None
    log = logging.getLogger('onep.' + __name__)

    def __init__(self, element, eventHandle, scope, route, state):
        """
        Constructor for the RouteStateEvent class. For internal use only.
        """
        super(ARTRouteStateEvent, self).__init__(element, eventHandle, OnepConstants.EVENT_TYPE_ART_STATE)
        self._state = state
        self._scope = scope
        self._route = route
        self._state = state



    def _get_scope(self):
        return self._scope


    _doc = 'Gets the scope for a route state event.\n    @type: L{L3UnicastScope<onep.routing.L3UnicastScope>}\n    '
    scope = property(_get_scope, None, None, _doc)

    def _get_route(self):
        return self._route


    _doc = 'Gets the route for a route state event.\n    @type: L{L3UnicastRoute<onep.routing.L3UnicastRoute>}\n    '
    route = property(_get_route, None, None, _doc)

    def _get_state(self):
        return self._state


    _doc = 'Gets the route state for a route state event.\n    @type: L{Enum<onep.core.util.Enum>}\n    '
    state = property(_get_state, None, None, _doc)

    def do_event(self, source):
        """
                This method specifies which action to do when an event is processed in 
                the event queue. For internal use only.
        
                """
        dbg = 'RouteState.doEvent: eventHandle = ' + str(self.event_handle)
        self.log.debug(dbg)
        ne = source
        targetListener = ne.event_manager.get_event_listener(self.event_handle)
        clienData = ne.event_manager.get_event_listener_client_data(self.event_handle)
        if targetListener != None:
            targetListener.handle_event(self, clienData)




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:23:00 IST
