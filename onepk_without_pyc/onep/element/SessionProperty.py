# 2015.02.05 17:21:11 IST
import onep.core.util.OnepConstants
from onep.element.SessionConfig import SessionConfig

class SessionProperty(object):
    """
        SessionProperty contains properties of a connection to the network element.
        The properties are read-only and cannot be modified by the application.
    
        @ivar element: The network element
        @type element: L{NetworkElement<onep.element.NetworkElement.NetworkElement>}
        @ivar username: The user name for the network element.
        @type username: C{str}
        """


    def __init__(self, config, ne):
        """
                Constructor
        
                Keyword argument:
                config 
                    The SessionConfig object whose attributes will be used and contained 
                    by this SessionProperty instance.
                ne
                    The network element
        
                """
        self.sessionConfig = SessionConfig(config)
        self.username = ne.username
        self.element = ne



    def _get_transport_mode(self):
        return self.sessionConfig.transportMode


    transportMode = property(_get_transport_mode)

    def _get_reconnect_timer(self):
        return self.sessionConfig.reconnectTimer


    reconnectTimer = property(_get_reconnect_timer)

    def _get_port(self):
        return self.sessionConfig.port


    port = property(_get_port)

    def _get_event_queue_size(self):
        return self.sessionConfig.eventQueueSize


    eventQueueSize = property(_get_event_queue_size)

    def _get_event_thread_pool(self):
        return self.sessionConfig.eventThreadPool


    eventThreadPool = property(_get_event_thread_pool)

    def _get_event_drop_mode(self):
        return self.sessionConfig.eventDropMode


    eventDropMode = property(_get_event_drop_mode)

    def _get_keep_alive_idle_time(self):
        return self.sessionConfig.keepAliveIdleTime


    keepAliveIdleTime = property(_get_keep_alive_idle_time)

    def _get_keep_alive_interval(self):
        return self.sessionConfig.keepAliveInterval


    keepAliveInterval = property(_get_keep_alive_interval)

    def _get_keep_alive_retry_count(self):
        return self.sessionConfig.keepAliveRetryCount


    keepAliveRetryCount = property(_get_keep_alive_retry_count)


# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:21:11 IST
