# 2015.02.05 17:20:58 IST
import threading
import logging
from time import sleep
from onep.core.event.AsyncMsg import AsyncMsg
from onep.core.exception.OnepException import OnepException
OnepAsyncMsgType = AsyncMsg.OnepAsyncMsgType

class EventDispatcher(threading.Thread):
    element = None
    event_queue = None
    terminated = False
    delay = 1.0 / 4

    def __init__(self):
        super(EventDispatcher, self).__init__()
        self.log = logging.getLogger(__name__)



    def run(self):
        event = None
        listener = None
        try:
            while self.terminated == False:
                try:
                    event = self.event_queue.popleft()
                except IndexError:
                    sleep(self.delay)
                    continue
                if event.msg_type == OnepAsyncMsgType.ONEP_ASYNC_MESSAGE_TYPE_EVENT:
                    listener = self.element.event_manager.get_event_listener(event.event_handle)
                    if listener == None:
                        self.log.warn('No listener for event ' + str(event.event_handle))
                        continue
                try:
                    event.do_event(self.element)
                except Exception as e:
                    self.log.exception('Exception in event listener: ' + str(e))

        except Exception as e:
            if not self.terminated:
                self.log.warn('Dispatcher thread interrupted: ' + str(e))
        finally:
            if self.terminated:
                self.log.info('Terminating dispatcher thread..')
            else:
                self.log.error('Dispatcher thread exit triggered disconnect')
                self.element.disconnect('OneP Internal error triggered disconnect')



    def interrupt(self):
        self.terminated = True




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:20:59 IST
