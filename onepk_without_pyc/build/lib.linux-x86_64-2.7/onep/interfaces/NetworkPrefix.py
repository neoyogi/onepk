# 2015.02.05 17:18:27 IST
from onep.core.util.HostIpCheck import HostIpCheck
from onep.core.exception.OnepIllegalArgumentException import OnepIllegalArgumentException

class NetworkPrefix(object):
    """ 
    Class representing the interface prefix that includes the IP address and Prefix length.
    """

    _address = None
    _prefix_length = 0

    def _get_address(self):
        return self._address



    def _set_address(self, addr):
        val = HostIpCheck(addr).is_ipaddress()
        if val:
            self._address = addr
        else:
            raise OnepIllegalArgumentException('The address provided to NetworkPrefix class is invalid')


    _doc = '\n    Contains the IP address from the Network Prefix object.\n    \n    Raises: OnepIllegalArgumentException if user tries to set invalid value as IP Address.\n    \n    @type:  C{str}\n    '
    address = property(_get_address, _set_address, None, _doc)

    def _get_prefix_length(self):
        return self._prefix_length



    def _set_prefix_length(self, len):
        self._prefix_length = len


    _doc = '\n    Contains the Prefix Length of the IP address provided to the Network Prefix class.\n    @type:  C{int}\n    '
    prefix_length = property(_get_prefix_length, _set_prefix_length, None, _doc)

    def __init__(self, address, prefix_length):
        """ 
        Constructor of Network Prefix
        
        @param address: The IP address from the Network Prefix object.
        @type address:  C{str}
        
        @param prefix_length: The prefix length of the NetworkPrefix object.
        @type prefix_length: C{int} 
        
        """
        self.address = address
        self.prefix_length = prefix_length



    def __str__(self):
        return 'Address: %s Prefix: %d' % (self.address, self.prefix_length)




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:18:27 IST
