# 2015.02.05 17:20:59 IST
from onep.core.exception.OnepException import OnepException
from Shared.ttypes import ExceptionIDL

class OnepDuplicateElementException(OnepException):
    """ Class which handles errors regarding duplicate sessions to the NetworkElement.
    
    An application can have only one session with a given NetworkElement. 
    A NetworkElement can have multiple interfaces and IP addresses.
    If the application is connected to the NetworkElement using one
    IP address, and then attempts to connect to the NetworkElement using
    another IP address, connect will fail with this exception. If this
    happens, the application can use get_original_network_element() method
    to retrieve the already connected NetworkElement instance.  
    """

    __defaultMessage = 'Duplicate IP address. '
    __element = None

    def __init__(self, arg_networkElement, arg_string = None, arg_cause = None):
        """ Default constructor. Constructs a new exception with default message as
            its detail message.
            
            Parameters:
                arg_networkElement: This is the instance of NetworkElement to which the
                                    duplicate session was being initiated.
                arg_string:         This is the error message.
                arg_cause :         This is the class object which has more information
                                    regarding the issue.
        """
        self.__element = arg_networkElement
        if arg_string and arg_string.__class__ == str:
            if arg_cause and isinstance(arg_cause, ExceptionIDL):
                message = self.__defaultMessage + ' ' + arg_string
                super(OnepDuplicateElementException, self).__init__(message, arg_cause)
            else:
                message = self.__defaultMessage + ' ' + arg_string
                super(OnepDuplicateElementException, self).__init__(message)
        else:
            super(OnepDuplicateElementException, self).__init__(self.__defaultMessage)



    def get_original_network_element(self):
        """ Get the existing NetworkElement instance that's already connected
        to the network element
            
        Returns:
            The existing NetworkElement instance
        """
        return self.__element




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:20:59 IST
