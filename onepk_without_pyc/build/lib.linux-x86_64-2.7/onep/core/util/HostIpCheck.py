# 2015.02.05 17:18:08 IST
import socket
import onep.core.util.socket_imp
import re
from onep.core.exception.OnepException import OnepInvalidMaskException
from binascii import hexlify

class HostIpCheck(object):
    """
    Use this to check for a valid ipv4, ipv6 or hostname string.
    Examples:  
    HostIpCheck('1.1.1.1').is_ipv4()       -- check for valid ipv4
                          .is_ipv6()       -- check for valid ipv6
                          .is_hostname()   -- check for valid hostname
                          .is_valid()      -- check for valid hostname or ip
                          .is_ipaddress()  -- check for valid ip address
    """

    _address_space_list = ['ipv4', 'ipv6']
    _address_space = None

    def __init__(self, argument, address_space = None):
        if not isinstance(argument, str):
            raise TypeError('argument must be an IP or hostname string ')
        self._argument = argument
        if address_space is not None:
            if address_space in self._address_space_list:
                self._address_space = address_space
            else:
                raise ValueError('address_space is either ' + ' or '.join(self._address_space_list))
        else:
            (ipv4, ipv6,) = self._address_space_list
            if self.is_ipv4():
                self._address_space = ipv4
            elif self.is_ipv6():
                self._address_space = ipv6
            elif self.is_hostname():
                if not self._address_space:
                    self._address_space = ipv4



    def _get_address_space(self):
        return self._address_space


    address_space = property(_get_address_space)

    def is_ipv4(self):
        """
        Check if argument is a valid ipv4.
        """
        try:
            addr = socket.inet_pton(socket.AF_INET, self._argument)
        except AttributeError:
            try:
                addr = socket.inet_aton(self._argument)
            except socket.error:
                return False
            return self._argument.count('.') == 3
        except socket.error:
            return False
        return True



    def is_ipv6(self):
        """
        Check if argument is a valid ipv6.
        """
        try:
            addr = socket.inet_pton(socket.AF_INET6, self._argument)
        except socket.error:
            return False
        return True



    def is_hostname(self):
        """
        Check if argument is a valid hostname.
        """
        if len(self._argument) > 255:
            return False
        if self._argument[-1:] == '.':
            self._argument = self._argument[:-1]
        allowed = re.compile('(?!-)[A-Z\\d-]{1,63}(?<!-)$', re.IGNORECASE)
        for x in self._argument.split('.'):
            if not allowed.match(x):
                return False

        return True



    def is_valid(self):
        """
        Check if argument is a valid hostname, ipv4 or ipv6.
        """
        if self.is_ipv4():
            return True
        if self.is_ipv6():
            return True
        if self.is_hostname():
            return True
        return False



    def is_ipaddress(self):
        """
        Check for valid ipv4 or ipv6 address
        """
        if self.is_ipv4() or self.is_ipv6():
            return True
        return False



    def __eq__(self, other):
        """
        Check if host ip address equals other
        """
        if not isinstance(other, HostIpCheck):
            return False
        if self.is_ipv4() and other.is_ipv4():
            return self._argument == other._argument
        if self.is_ipv6() and other.is_ipv6():
            self_addr = int(hexlify(socket.inet_pton(socket.AF_INET6, self._argument)), 16)
            other_addr = int(hexlify(socket.inet_pton(socket.AF_INET6, other._argument)), 16)
            return self_addr == other_addr
        return False



    @staticmethod
    def len2mask(len):
        """
        Convert a bit length to a dotted netmask (aka. CIDR to netmask)
        """
        mask = ''
        if not isinstance(len, int):
            raise TypeError('Prefix length must be integer')
        if len < 0 or len > 32:
            raise ValueError('Invalid prefix length %d' % len)
        for t in range(4):
            if len > 7:
                mask += '255.'
            else:
                dec = 255 - (2 ** (8 - len) - 1)
                mask += str(dec) + '.'
            len -= 8
            if len < 0:
                len = 0

        return mask[:-1]



    @staticmethod
    def mask2len(mask):
        """
                Convert network submask to prefix length
        
                """
        if not HostIpCheck.ipv4_validate_mask(mask):
            raise OnepInvalidMaskException('invalid mask')
        total = 0
        for i in mask.split('.'):
            total += len(bin(int(i)).lstrip('0b').rstrip('0'))

        return total



    @staticmethod
    def ipv4_validate_mask(mask):
        """
                Validate IPv4 subnetmask is valid
        
                """
        tuples = mask.split('.')
        if len(tuples) != 4:
            return False
        else:
            mask_value = 0
            for i in xrange(0, 4):
                mask_value += int(tuples[i]) << 24 - 8 * i

            allbits = bin(mask_value)
            ones = allbits.count('1')
            correct_value = 0
            for i in xrange(32 - ones, 32):
                correct_value |= 1 << i

            if bin(correct_value) == allbits:
                return True
            return False



    @staticmethod
    def calc_mask(address):
        mask = []
        lmask = [ seg for seg in address.split('.') if int(seg) > 0 ]
        zeros = 4 - len(lmask)
        [ mask.append('255') for i in lmask ]
        [ mask.append('0') for i in range(0, zeros) ]
        return '.'.join(mask)



    @staticmethod
    def len2mask6(prefix_length):
        """
                Convert an IPv6 prefix length to string representation.
        
                Example:
        
                >>> len2mask6(64)
                'ffff:ffff:ffff:ffff:0000:0000:0000:0000'
                >>>
        
                @param prefix_length: Integer between 0 - 128
                @type prefix_length: C{int}
        
                @return: prefix length in string format
                @rtype: C{string}
        
                """
        if prefix_length < 0 or prefix_length > 128:
            raise OnepIllegalArgumentException('Invalid prefix_length', str(prefix_length))
        s = ''
        temp = '1' * (prefix_length % 16)
        if temp:
            temp += '0' * (16 - len(temp))
            hextemp = hex(int(temp, base=2)).rstrip('L').lstrip('0x')
        else:
            hextemp = temp
        s = 'ffff' * (prefix_length / 16)
        s += hextemp
        s += '0' * (32 - len(s))
        newtemp = [ s[i:(i + 4)] for i in range(0, len(s), 4) ]
        return ':'.join(newtemp)




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:18:08 IST
