# 2015.02.05 17:20:34 IST
import core.exception.OnepIllegalArgumentException
from onep.aaa.Attribute import Attribute
from onep.aaa.OnepAAAAttributeType import OnepAAAAttributeType

class StringAttribute(Attribute):
    """
    The Attribute class for storing AAA string attribute.
    """


    def __init__(self, type_, name, str_value):
        """
                Create an Attribute that has String format.
                This constructor creates an Attribute with the given Attribute type and value.
                The Application-specific attributes are keyed on attribute names, hence the name parameters are
                required parameters for application-specific attributes. 
                The AAA attribute must be of string format.
        
                @param type_: Type of the attribute.
                @param name: Name of the attribute.
                @param str_value: Value of the attribute.
                @raise OnepIllegalArgumentException: if the application name or str_value is invalid.
                """
        super(StringAttribute, self).__init__(type_, name)
        self.str_value = str_value
        if str_value == None:
            self.str_value = ''



    def __str__(self):
        str_attriute = 'Name:   ' + str(self.name)
        str_attriute += '\nType:   ' + OnepAAAAttributeType.enumval(self.type_)
        str_attriute += '\nFormat: STRING'
        str_attriute += '\nValue:  ' + self.str_value
        return str_attriute




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:20:34 IST
