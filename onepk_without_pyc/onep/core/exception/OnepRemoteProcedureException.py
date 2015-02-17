# 2015.02.05 17:20:59 IST
from onep.core.exception.OnepException import OnepException
from onep.core.exception.OnepException import OnepNotSupportedException
from onep.core.exception.OnepException import OnepServiceNotEnabledException
from onep.core.exception.OnepException import OnepNoDataException
from onep.core.exception.OnepException import OnepDataExistsException
from onep.core.exception.OnepException import OnepInvalidVrfException
from onep.core.exception.OnepException import OnepExceedMaxAllowanceException
try:
    from onep.core.util.OnepStatus import OnepStatus
except ImportError:
    pass
from Shared.ttypes import ExceptionIDL

class OnepRemoteProcedureException(OnepException):
    """
    The exception is thrown to indicate error has occurred in the  
    remote procedure call made to a network element.
          
    """

    __defaultMessage = 'Error occurs in the remote procedure call. '
    __errorCode = int()

    def __init__(self, remote_cause = None):
        if remote_cause and isinstance(remote_cause, ExceptionIDL):
            from onep.core.util.OnepStatus import OnepStatus
            if remote_cause.code == OnepStatus.ONEP_ERR_NOT_SUPPORTED:
                raise OnepNotSupportedException(remote_cause.text)
            elif remote_cause.code == OnepStatus.ONEP_ERR_SERVICE_DISABLED:
                raise OnepServiceNotEnabledException(remote_cause.text)
            elif remote_cause.code == OnepStatus.ONEP_ERR_NO_DATA:
                raise OnepNoDataException(remote_cause.text)
            elif remote_cause.code == OnepStatus.ONEP_ERR_DUPLICATE:
                raise OnepDataExistsException(remote_cause.text)
            elif remote_cause.code == OnepStatus.ONEP_ERR_INVALID_VRF:
                raise OnepInvalidVrfException(remote_cause.text)
            elif remote_cause.code == OnepStatus.ONEP_ERR_EXCEEDS_MAX_ALLOWANCE:
                raise OnepExceedMaxAllowanceException(remote_cause.text)
            self.__errorCode = remote_cause.code
            super(OnepRemoteProcedureException, self).__init__(remote_cause.text, remote_cause)
        else:
            super(OnepRemoteProcedureException, self).__init__(self.__defaultMessage)



    def get_error_code(self):
        """
        Get the error code that returns from the remote procedure call.
        
        Returns:
            The error Code from the remote procedure call.
        """
        return self.__errorCode




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:20:59 IST
