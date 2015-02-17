# 2015.02.05 17:18:18 IST
from onep.element.SessionStatistics import SessionStatistics
from onep.element.SessionProperty import SessionProperty

class SessionHandle(object):
    """
    SessionHandle represents a live session (connection) between a
    NetworkApplication and a single NetworkElement. It is the owner of session
    property settings and statistics.
    
    """


    def __init__(self, _id, ne, sessionConf):
        """
                Constructor
        
                Keyword argument:
                id -- ID of the session.
                ne
                sessionProf
                Session profile.
        
                """
        self._id = _id
        self.element = ne
        self.sessionProp = SessionProperty(sessionConf, ne)
        self.sessionStat = SessionStatistics(ne)



    @property
    def id(self):
        return self._id



    def equals(self, other):
        """
                Indicates whether another SessionHandle is "equal to" this one. Each
                authenticated session is assigned a SessionHandle, and each SessionHandle
                is assigned a unique ID (handle). The equals method for the SessionHandle
                compares the unique ID of the self SessionHandle with the ID of the other
                returned if the other is NULL, or if the unique ID of the other SessionHandle does
        
                Keyword argument:
                    other
                
                Return;
                    True if the IDs are the same; false otherwise.
        
                """
        if other == None:
            return False
        if self._id == other._id:
            return True
        return False



    def _get_connect_time(self):
        if self.element != None and self.element.get_connect_time() != None:
            return self.element.get_connect_time()
        else:
            return 


    connectTime = property(_get_connect_time)

    def __str__(self):
        sb = '\nSessionHandle [' + str(self._id) + ']\n'
        if self.element == None:
            return sb
        sb += '\tNetworkElement   : ' + self.element.host_address + '\n'
        sb += '\tSessionProperties\n'
        sb += '\t  thread pool    : ' + str(self.sessionProp.eventThreadPool) + '\n'
        sb += '\t  queue Size     : ' + str(self.sessionProp.eventQueueSize) + '\n'
        sb += '\t  drop mode      : ' + str(self.sessionProp.eventDropMode) + '\n'
        sb += '\t  reconnect timer: ' + str(self.sessionProp.reconnectTimer) + '\n'
        sb += '\t  username       : ' + self.sessionProp.username + '\n'
        sb += '\t  transport mode : ' + str(self.sessionProp.transportMode) + '\n'
        sb += '\t  transport port : ' + str(self.sessionProp.port) + '\n'
        sb += '\tSessionStatistics\n'
        sb += '\t  eventDropCount : ' + str(self.sessionStat.eventDropCount) + '\n'
        sb += '\t  eventRecvCount : ' + str(self.sessionStat.eventTotalCount) + '\n'
        return sb




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:18:18 IST
