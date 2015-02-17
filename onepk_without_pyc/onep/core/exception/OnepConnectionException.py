# 2015.02.05 17:20:59 IST
from onep.core.exception.OnepException import OnepException
from Shared.ttypes import ExceptionIDL
from onep.thrift.Thrift import TException

class OnepConnectionException(OnepException):
    """
    The exception is thrown to indicate that error has occurred when
    trying to connect to a network element.
    """

    __defaultMessage = 'Failed to connect to the network element or the session is closed. '

    def __init__(self, arg_string = None, arg_cause = None):
        """ Constructor for the OnepConnectionException class.
         
                Default constructor. Constructs a new exception with default message
                as its detail message. If additional parameters are passed then those
                parameters will be displayed as part of error message depending on its type
        
                Parameters:
                arg_string: This is the error message.
                arg_cause : This is the class object which has more information regarding the issue.
        
                """
        if arg_string and arg_string.__class__ == str:
            if arg_cause and isinstance(arg_cause, TException):
                message = self.__defaultMessage + ' ' + arg_string
                super(OnepConnectionException, self).__init__(message, arg_cause)
            else:
                message = self.__defaultMessage + ' ' + arg_string
                super(OnepConnectionException, self).__init__(self.__defaultMessage)



    def get_default_message(self):
        """
                Get the default message of the exception. This method is for 
                internal use only. 
        
                @return the defaultMessage
        
                """
        return self.__defaultMessage




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:20:59 IST
