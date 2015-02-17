# 2015.02.05 17:20:59 IST
from onep.core.exception.OnepException import OnepException
from Shared.ttypes import ExceptionIDL

class OnepIllegalArgumentException(OnepException):
    """ Class for handling exceptions generated by Illegal arguments.
    
    The exception is thrown to indicate that a method has been passed.
    """

    __defaultMessage = 'Illegal or inappropriate argument. '

    def __init__(self, arg_string = None, arg_cause = None):
        """Constructor of OnepIllegalArgumentException.
        
        Default constructor. Constructs a new exception with default message
        as its detail message. If additional parameters are passed then those
        parameters will be displayed as part of error message depending on its type
        
        Parameters:
                arg_string: This is the error message.
                arg_cause : This is the class object which has more information
                    regarding the issue.
        """
        if arg_string and arg_string.__class__ == str:
            if arg_cause and isinstance(arg_cause, ExceptionIDL):
                message = self.__defaultMessage + ' ' + str(arg_string)
                super(OnepIllegalArgumentException, self).__init__(message, arg_cause)
            elif arg_cause and arg_cause.__class__ == str:
                message = self.__defaultMessage + ' ' + str(arg_string) + ' is set to ' + str(arg_cause)
                super(OnepIllegalArgumentException, self).__init__(message)
            else:
                message = self.__defaultMessage + ' ' + str(arg_string)
                super(OnepIllegalArgumentException, self).__init__(message)
        else:
            super(OnepIllegalArgumentException, self).__init__(self.__defaultMessage)




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:20:59 IST