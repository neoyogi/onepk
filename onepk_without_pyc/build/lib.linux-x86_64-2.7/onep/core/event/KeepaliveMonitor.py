# 2015.02.05 17:18:07 IST
import threading
import logging
from time import time, sleep

class KeepaliveMonitor(threading.Thread):
    """
        This is a class for monitoring keepalive events
        For internal use only.
    
        """


    def __init__(self, element):
        super(KeepaliveMonitor, self).__init__()
        if element == None:
            return 
        self.log = logging.getLogger(__name__)
        self.network_element = element
        session_prop = element.session_handle.sessionProp
        self.configured_idle = session_prop.keepAliveIdleTime
        self.configured_interval = session_prop.keepAliveInterval
        self.configured_retry_count = session_prop.keepAliveRetryCount
        self.configured_reconnect_timer = session_prop.reconnectTimer
        self.last_heatbeat_time = time()
        self.running = True
        self.daemon = True
        self.start()



    def run(self):
        while self.running == True:
            self.log.debug('checking socket keepalive ...')
            alive = False
            i = 0
            while i <= self.configured_retry_count:
                elapse = time() - self.last_heatbeat_time
                self.log.debug('seconds since last heartbeat: ' + str(elapse) + ', try #' + str(i + 1))
                if self.configured_idle > elapse:
                    alive = True
                    try:
                        sleep(1)
                    except Exception as e:
                        self.log.debug('sleep is interrupted: ' + e.__str__())
                    break
                else:
                    try:
                        sleep(self.configured_interval)
                    except Exception as e:
                        self.log.debug('sleep is interrupted: ' + e.__str__())
                i += 1

            if alive:
                self.log.debug('done checking socket keepalive, socket is alive.')
            else:
                self.log.error('no keepalive event from network element!')
                self.stop_monitor()
                if self.configured_reconnect_timer:
                    self.network_element._reconnect_waiting = True
                self.network_element.disconnect('no keepalive event from network element')




    def start_monitor(self):
        self.log.debug('start KeepaliveMonitor...')
        self.running = True



    def stop_monitor(self):
        self.log.debug('stop KeepaliveMonitor!')
        self.running = False



    def update_heatbeat_time(self):
        self.last_heatbeat_time = time()




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:18:07 IST
