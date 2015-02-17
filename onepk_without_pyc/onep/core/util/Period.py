# 2015.02.05 17:21:00 IST
from onep.core.exception.OnepIllegalArgumentException import OnepIllegalArgumentException

class Period(object):
    sec = int()
    msec = int()

    def __init__(self, sec, msec):
        self.set_sec(sec)
        self.set_msec(msec)



    def get_msec(self):
        return self.msec



    def get_sec(self):
        return self.sec



    def set_sec(self, sec):
        if sec > 999 or sec < 0:
            raise OnepIllegalArgumentException('Invalid value for Seconds')
        self.sec = sec



    def set_msec(self, msec):
        if msec > 999 or msec < 0:
            raise OnepIllegalArgumentException('Invalid value for Milliseconds')
        self.msec = msec




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:21:00 IST
