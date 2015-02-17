# 2015.02.05 17:18:18 IST
import logging
from onep.core.event.EventObject import EventObject
from onep.core.event.EventFilter import EventFilter
from onep.core.util.Enum import enum
from onep.core.util.OnepConstants import OnepConstants

class SyslogEvent(EventObject):
    """
    An event which indicates that a syslog event occurred in a Network Element.
    """


    def __init__(self, element, eventHandle, count, priority, msg):
        """
        Constructor - used internally
        
        """
        super(SyslogEvent, self).__init__(element, eventHandle, OnepConstants.EVENT_TYPE_SYSLOG)
        self.event_handle = eventHandle
        self.message = msg
        self.msg_count = count
        self.priority = priority



    def do_event(self, ne):
        """
                This method specifies what action to do when an event is processed.
                
                For Syslog Event, the action is invoking the client's event
                listener.
                
                @param ne:
                    The source of the event. For Syslog Event, the source in an
                    instance of NetworkElement.
        
                """
        logging.debug('Syslog.do_event: event_handle = ' + str(self.event_handle) + ' msgCount = ' + str(self.msg_count) + ' priority = ' + str(self.priority) + ' message = ' + self.message)
        targetListener = ne.event_manager.get_event_listener(self.event_handle)
        clienData = ne.event_manager.get_event_listener_client_data(self.event_handle)
        if targetListener != None:
            targetListener.handle_event(self, clienData)




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:18:18 IST
