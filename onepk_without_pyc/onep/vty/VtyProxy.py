# 2015.02.05 17:23:20 IST
from onep.core.exception.OnepException import OnepNotSupportedException
from onep.vty.VtyService import VtyService
import logging
import time

class VtyProxy(object):
    """
    INTERNAL USE
    VTY proxy for development presentation services
    (Not supported in onePK releases)
    """


    def __init__(self, elm):
        self.ne = elm
        self.vty = None
        self.trans = {}
        self.log = logging.getLogger(__name__)



    def prepare(self):
        raise OnepNotSupportedException('Internal development API')



    def config(self, cmd):
        self.prepare()



    def no_config(self, cmd):
        self.prepare()



    def show(self, cmd):
        return None



    def vty_exec(self, cli):
        self.prepare()



    def debug(self, cmd):
        self.prepare()



    def no_debug(self, cmd):
        self.prepare()



    def commit(self):
        self.prepare()




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:23:20 IST
