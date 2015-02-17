# 2015.02.05 17:20:33 IST
import onep.core.exception.OnepException
import onep.core.exception.OnepIllegalArgumentException
from onep.aaa.Attribute import Attribute
from onep.aaa.OnepAAAAttributeType import OnepAAAAttributeType

class IntAttribute(Attribute):
    """
    The Attribute class for storing an integer attribute.
    """


    def __init__(self, type_, name, long_value):
        """
                Create an Attribute that has integer format.
                This constructor creates an Attribute with the given Attribute type and value.
                The Application-specific attributes are keyed on attribute names, hence the name parameters are
                required parameters for application-specific attributes. 
                The AAA attribute should be of integer format.
        
                @param type_: Type of the attribute.
                @param name: Name of the attribute.
                @param long_value: Value of the attribute.
                @raise OnepIllegalArgumentException: if the Attribute type does not support the integer format or
                               if the name is null for Application-specific attributes.
                """
        super(IntAttribute, self).__init__(type_, name)
        self.long_value = long_value



    def __str__(self):
        str_attriute = 'Name:   ' + str(self.name)
        str_attriute += '\nType:   ' + OnepAAAAttributeType.enumval(self.type_)
        str_attriute += '\nFormat: ULONG'
        str_attriute += '\nValue:  ' + str(self.long_value)
        return str_attriute




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:20:33 IST
