# 2015.02.05 17:21:10 IST
import os
import sys
from onep.core.exception.OnepIllegalArgumentException import OnepIllegalArgumentException
from onep.core.util.OnepConstants import OnepConstants
from onep.core.util.Enum import enum
from onep.core.util.tlspinning import TLSUnverifiedElementHandler
from onep.element.NetworkApplication import NetworkApplication

class SessionConfig(object):
    """
        SessionConfig contains the configuration that will be used
        for connecting to the network element.
        
        SessionConfig provides a means to configure session attributes
        prior to connecting to a NetworkElement.
        The SessionConfig data is used at the NetworkElement.connect() time.
        On successful connection, the session attributes for that particular
        session can no longer be modified.
        However, the SessionConfig object can be modified as needed, and reused
        to NetworkElement.connect() to other network elements.
        To modify the session attributes for an active session, call
        NetworkElement.disconnect()
        and NetworkElement.connect() again passing in the modified attributes
        set in the SessionConfig object.
        If needed, the session attributes for an active session can be retrieved
        using the SessionHandle  returned by
        NetworkElement.connect().
        The SessionHandle holds the session attributes for an active session.
        The session attributes from the provided SessionConfig are copied
        to a SessionProperty as static property of the session.
        
        The SessionConfig object is required only if the defaults need to
        be overridden. Passing a null for the SessionConfig in the
        connect() call will result in a TLS connection between the application
        and the network element using default values. See specific setter APIs
        for the defaults for each attribute.
    
        @ivar ca_certs: The Certification Authority certificates file location. 
        @type ca_certs: C{str}
        @ivar keyfile: The client key file location.
        @type keyfile: C{str}
        @ivar certfile: The client certificate file location. 
        @type certfile: C{str}
        @ivar vm_credential_file: Virtual Machine credentials allowing for internal
        container connection.  Credentials created from local file in container or
        constructed by container service set. Default "/cisco/onep/info.data"
        @type vm_credential_file: C{string}
        @ivar read_write_timeout: Timeout of response to read or write request.  
        Default is 180 seconds
        @type read_write_timeout: C{int}
    
        """


    def __init__(self, transport):
        """
                Constructor
        
                Keyword argument:
                transport
                    Transport type to be used for the session. If the value is
                    null, the default transport type will be used. The default
                    transport is SessionTransportMode.TLS.
                
                """
        if isinstance(transport, SessionConfig):
            self.__init___0(transport)
            return 
        if transport == None:
            self.transportMode = self.DEFAULT_TRANSPORT_MODE
        else:
            self.transportMode = transport
        self._port = self.DEFAULT_PORT
        self._reconnectTimer = self.DEFAULT_RECONNECT_TIMER
        self._eventQueueSize = self.DEFAULT_EVENT_QUEUE_SIZE
        self._eventThreadPool = self.DEFAULT_THREADPOOL_SIZE
        self._eventDropMode = self.DEFAULT_EVENT_DROP_MODE
        self._keepAliveIdleTime = self.DEFAULT_KEEPALIVE_IDLE_TIME
        self._keepAliveInterval = self.DEFAULT_KEEPALIVE_INTERVAL
        self._keepAliveRetryCount = self.DEFAULT_KEEPALIVE_RETRY_COUNT
        self._thread_stack_size = 0
        self.ca_certs = None
        self.keyfile = None
        self.certfile = None
        self.vm_credential = None
        self.vm_credential_file = '/cisco/onep/info.data'
        self._tls_pinning_file = None
        self._tls_pinning_handler = None
        self.read_write_timeout = NetworkApplication.DEFAULT_RDWR_TIMEOUT



    def __init___0(self, other):
        """
        Keyword argument:
        other -- The SessionConfig object to copy from
        
        """
        self.transportMode = other.transportMode
        self._port = other._port
        self._reconnectTimer = other._reconnectTimer
        self._eventQueueSize = other._eventQueueSize
        self._eventThreadPool = other._eventThreadPool
        self._eventDropMode = other._eventDropMode
        self._keepAliveIdleTime = other._keepAliveIdleTime
        self._keepAliveInterval = other._keepAliveInterval
        self._keepAliveRetryCount = other._keepAliveRetryCount
        self._thread_stack_size = other._thread_stack_size
        self.ca_certs = other.ca_certs
        self.vm_credential = other.vm_credential
        self._tls_pinning_file = other._tls_pinning_file
        self._tls_pinning_handler = other._tls_pinning_handler
        self.read_write_timeout = other.read_write_timeout



    def _set_transport_mode(self, transportMode):
        if transportMode == None:
            transportMode = self.DEFAULT_TRANSPORT_MODE
        self._transportMode = transportMode



    def _get_transport_mode(self):
        return self._transportMode


    _doc_transport_mode = '\n    Transport type to be used for the session. If the value is None,\n    the default transport type will be used. The default transport is\n    SessionConfig.SessionTransportMode.TLS\n    '
    transportMode = property(_get_transport_mode, _set_transport_mode, None, _doc_transport_mode)

    def _set_reconnect_timer(self, reconnectTimer):
        if reconnectTimer < 0:
            reconnectTimer = 0
        self._reconnectTimer = reconnectTimer



    def _get_reconnect_timer(self):
        return self._reconnectTimer


    _doc_reconnect_timer = '\n    Reconnect timeout for the session. If the value is less than or equal to 0,\n    there will be no timeout for reconnect.\n    '
    reconnectTimer = property(_get_reconnect_timer, _set_reconnect_timer, None, _doc_reconnect_timer)

    def _set_port(self, port):
        if port <= 0:
            port = self.DEFAULT_PORT
        self._port = port



    def _get_port(self):
        return self._port


    _doc_port = '\n    Port number for the session. If the value is equal to or less than 0,\n    the default port will be used which is OnepConstants.ONEP_TLS_PORT\n    '
    port = property(_get_port, _set_port, None, _doc_port)

    def _set_event_queue_size(self, eventQueueSize):
        if eventQueueSize < 1 or eventQueueSize > 1000:
            eventQueueSize = 200
        self._eventQueueSize = eventQueueSize



    def _get_event_queue_size(self):
        return self._eventQueueSize


    _doc_event_queue_size = '\n    The size of the local event queue in the range of 1 - 1000. \n    If the value is out of range, the default value 200 is\n    used.\n    '
    eventQueueSize = property(_get_event_queue_size, _set_event_queue_size, None, _doc_event_queue_size)

    def _set_event_thread_pool(self, eventThreadPool):
        if eventThreadPool <= 0:
            eventThreadPool = 10
        self._eventThreadPool = eventThreadPool



    def _get_event_thread_pool(self):
        return self._eventThreadPool


    _doc_event_thread_pool = '\n    Specifies the number of dispatcher threads. Any positive integer is allowed for the thread count. \n    If the value equals or less than 0, the default value 10 is used.\n    The upper bound for the thread pool depends on the following factors:\n    1. Available memory on the system where the application runs\n    2. The expected number of network elements that the application connects to.\n       A separate thread pool is created for every connected NetworkElement object.\n    3. The expected rate of incoming events and the event queue size that the threads will service.\n    '
    eventThreadPool = property(_get_event_thread_pool, _set_event_thread_pool, None, _doc_event_thread_pool)

    def _set_event_drop_mode(self, eventDropMode):
        if eventDropMode == None:
            eventDropMode = self.OnepEventDropMode.ONEP_EVENT_DROP_NEW
        self._eventDropMode = eventDropMode



    def _get_event_drop_mode(self):
        return self._eventDropMode


    _doc_event_drop_mode = '\n    Event drop mode type to be used for the session. If the value is null,\n    the default will be SessionConfig.OnepEventDropMode.ONEP_EVENT_DROP_NEW.\n    When the event queue is full, new event will be dropped by default. \n    But if this value is set to ONEP_EVENT_DROP_OLD, oldest event in the queue \n    is dropped to allow new event to be queued.\n    '
    eventDropMode = property(_get_event_drop_mode, _set_event_drop_mode, None, _doc_event_drop_mode)

    def _set_keep_alive_idle_time(self, keepAliveIdleTime):
        if keepAliveIdleTime < self.MIN_KEEPALIVE_IDLE_TIME or keepAliveIdleTime > sys.maxint:
            keepAliveIdleTime = self.DEFAULT_KEEPALIVE_IDLE_TIME
        self._keepAliveIdleTime = keepAliveIdleTime



    def _get_keep_alive_idle_time(self):
        return self._keepAliveIdleTime


    _doc_keep_alive_idle_time = '\n    The idle time in seconds. Any value between SessionConfig.MIN_KEEPALIVE_IDLE_TIME\n    and Integer.MAX_VALUE is allowed. If the value is out of this range, default value will be assigned.\n    Default value is SessionConfig.DEFAULT_KEEPALIVE_IDLE_TIME seconds.\n    '
    keepAliveIdleTime = property(_get_keep_alive_idle_time, _set_keep_alive_idle_time, None, _doc_keep_alive_idle_time)

    def _set_keep_alive_interval(self, keepAliveInterval):
        if keepAliveInterval < 0 or keepAliveInterval > sys.maxint:
            keepAliveInterval = self.DEFAULT_KEEPALIVE_INTERVAL
        self._keepAliveInterval = keepAliveInterval



    def _get_keep_alive_interval(self):
        return self._keepAliveInterval


    _doc_keep_alive_interval = '\n    The interval between each retry in the unit of seconds. Any value between 0 and \n    Integer.MAX_VALUE is allowed. If the value is out of this range, default value will be assigned.\n    Default is SessionConfig.DEFAULT_KEEPALIVE_INTERVAL seconds.\n    '
    keepAliveInterval = property(_get_keep_alive_interval, _set_keep_alive_interval, None, _doc_keep_alive_interval)

    def _set_keep_alive_retry_count(self, keepAliveRetryCount):
        if keepAliveRetryCount < 0 or keepAliveRetryCount > sys.maxint:
            keepAliveRetryCount = self.DEFAULT_KEEPALIVE_RETRY_COUNT
        self._keepAliveRetryCount = keepAliveRetryCount



    def _get_keep_alive_retry_count(self):
        return self._keepAliveRetryCount


    _doc_keep_alive_retry_count = '\n    The retry count number of keepalive. Any value between 0 and Integer.MAX_VALUE is allowed.\n    If the value is out of this range, default value SessionConfig.DEFAULT_KEEPALIVE_RETRY_COUNT will be assigned.\n    '
    keepAliveRetryCount = property(_get_keep_alive_retry_count, _set_keep_alive_retry_count, None, _doc_keep_alive_retry_count)

    def _set_thread_stack_size(self, size):
        if size < 0:
            size = 0
        elif size > 0 and size < self.MIN_STACK_SIZE:
            size = self.MIN_STACK_SIZE
        self._thread_stack_size = size



    def _get_thread_stack_size(self):
        return self._thread_stack_size


    _doc_thread_stack_size = '\n    The thread stack size. Must be set before conneting. If set to 0, the value\n    will be the OS default stack size.\n    The minimum value is SessionConfig.MIN_STACK_SIZE\n    '
    thread_stack_size = property(_get_thread_stack_size, _set_thread_stack_size, None, _doc_thread_stack_size)

    def set_tls_pinning(self, pinning_file, handler):
        """
                Sets the parameters for TLS pinning.
        
                Pinning is the process by which certain hosts can be whitelisted for
                TLS verification.  If the presented certificate matches the known
                certificate for that host in the pinning file, that connection proceeds
                even if the certificate fails the customary TLS verification.  Using a
                handler for unverified TLS hosts, an application may present a
                fingerprint of the unknown host to a user for manual verification.
        
                @param pinning_file: The path to the pinning file to use.  If None, no
                                     pinning file will be used.  By default, no pinning
                                     file is used.
                @type  pinning_file: C{str}
                @param handler: The handler to use.  If None, the default action is
                                taken which is to terminate the connection that is not
                                verified.
                @type  handler:
                            L{TLSUnverifiedElementHandler<onep.core.util.tlspinning>}
                """
        self.tls_pinning_file = pinning_file
        self.tls_unverified_element_handler = handler



    def _set_tls_pinning_file(self, pinning_file):
        if pinning_file is not None and not isinstance(pinning_file, str):
            raise OnepIllegalArgumentException('pinning_file', pinning_file)
        self._tls_pinning_file = pinning_file



    def _get_tls_pinning_file(self):
        return self._tls_pinning_file


    _doc_tls_pinning_file = '\n    The path of the pinning file to use.  If null, no pinning\n    file will be used.  By default, no pinning file is used.\n    '
    tls_pinning_file = property(_get_tls_pinning_file, _set_tls_pinning_file, None, _doc_tls_pinning_file)

    def _set_tls_unverified_element_handler(self, handler):
        if handler is not None and not isinstance(handler, TLSUnverifiedElementHandler):
            raise OnepIllegalArgumentException('handler', handler)
        self._tls_pinning_handler = handler



    def _get_tls_unverified_element_handler(self):
        return self._tls_pinning_handler


    _doc_tls_unverified_element_handler = '\n    The handler to use.  If null, the default action is taken\n    which is to terminate the connection that is not verified.\n    '
    tls_unverified_element_handler = property(_get_tls_unverified_element_handler, _set_tls_unverified_element_handler, None, _doc_tls_unverified_element_handler)

SessionConfig.SessionTransportMode = enum('SOCKET', 'TLS', 'TIPC')
SessionConfig.OnepEventDropMode = enum('ONEP_EVENT_DROP_NEW', 'ONEP_EVENT_DROP_OLD')
SessionConfig.DEFAULT_TRANSPORT_MODE = SessionConfig.SessionTransportMode.TLS
SessionConfig.DEFAULT_PORT = OnepConstants.ONEP_TLS_PORT
SessionConfig.DEFAULT_RECONNECT_TIMER = 0
SessionConfig.DEFAULT_EVENT_QUEUE_SIZE = 200
SessionConfig.DEFAULT_THREADPOOL_SIZE = 10
SessionConfig.DEFAULT_EVENT_DROP_MODE = SessionConfig.OnepEventDropMode.ONEP_EVENT_DROP_NEW
SessionConfig.DEFAULT_KEEPALIVE_IDLE_TIME = 60
SessionConfig.MIN_KEEPALIVE_IDLE_TIME = 60
SessionConfig.DEFAULT_KEEPALIVE_INTERVAL = 30
SessionConfig.DEFAULT_KEEPALIVE_RETRY_COUNT = 2
SessionConfig.MIN_STACK_SIZE = 32 * 1024

# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:21:10 IST
