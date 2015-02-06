__author__ = 'yogesh'
from base import onepbase

class onepbase2(onepbase):
    def __init__(self):
        super(onepbase2,self).__init__()

if __name__ == "__main__":
    onep2 = onepbase2()
    onep2.disconnect()