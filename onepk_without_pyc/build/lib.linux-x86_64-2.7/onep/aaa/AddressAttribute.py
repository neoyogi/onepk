# 2015.02.05 17:17:49 IST
import onep.core.exception.OnepException
import onep.core.exception.OnepIllegalArgumentException
from onep.aaa.Attribute import Attribute
from onep.aaa.OnepAAAAttributeType import OnepAAAAttributeType

class AddressAttribute(Attribute):
    """ 
    The AAA Attribute which has an IP address format.
    """


    def __init__(self, type_, name, address):
        """
        Create a AAA Attribute that has the InetAddress format.
        This constructor creates an Attribute with the specified Attribute type and value.
        The AAA attribute must be of the InetAddress format.
        
        @param type_: The type of the attribute. 
        @param name: The name of the attribute.
        @param address: The value of the attribute.
        @raise OnepIllegalArgumentException: If the attribute type does not support the InetAddress format.
        """
        super(AddressAttribute, self).__init__(type_, name)
        self.address = address



    def __str__(self):
        str_attriute = 'Name:   ' + str(self.name)
        str_attriute += '\nType:   ' + OnepAAAAttributeType.enumval(self.type_)
        str_attriute += '\nFormat: ADRESS'
        str_attriute += '\nValue:  ' + self.address
        return str_attriute




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:17:49 IST
