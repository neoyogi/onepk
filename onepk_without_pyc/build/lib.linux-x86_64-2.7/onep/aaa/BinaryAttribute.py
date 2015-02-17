# 2015.02.05 17:17:50 IST
import onep.core.exception.OnepIllegalArgumentException
from onep.aaa.Attribute import Attribute
from onep.aaa.OnepAAAAttributeType import OnepAAAAttributeType

class BinaryAttribute(Attribute):
    """
    The Attribute class for storing AAA binary attributes.
    """


    def __init__(self, type_, name, binary_data):
        """    
                Create an Attribute that has binary format.
                This constructor creates an Attribute with the given Attribute type and value.
        
                The AAA attribute must be an array of bytes.
        
                @param type_: Type of the attribute.
                @param name: Name of the attribute.
                @param binary_data: Array of bytes.
                @raise OnepIllegalArgumentException: If the type of the attribute does not support the binary format or
                            if the name is null for Application-specific attributes.
                """
        super(BinaryAttribute, self).__init__(type_, name)
        self.binary_data = binary_data



    def __str__(self):
        str_attriute = 'Name:   ' + str(self.name)
        str_attriute += '\nType:   ' + OnepAAAAttributeType.enumval(self.type_)
        str_attriute += '\nFormat: BINARY'
        str_attriute += '\nValue:  ' + str(self.binary_data)
        return str_attriute




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:17:50 IST
