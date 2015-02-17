# 2015.02.05 17:22:57 IST
from onep.core.util.Enum import enum

class RouteOperation(object):
    """
    This abstract class is the parent class of L3UnicastRouteOperation and 
    in the future for L3MulticastRouteOperation, L2UnicastRouteOperation,
    L2MulticastRouteOperation, etc.
    
    This class represents the operation to be performed on a route.
    """

    _op_type = int()
    RouteOperationType = enum('ADD', 'REMOVE', 'REPLACE')

    def __init__(self, opType):
        """
        Constructor
        
        @param opType: The operation type.
        @type opType: L{Enum<onep.core.util.Enum>}
        """
        super(RouteOperation, self).__init__()
        self._op_type = opType



    def _get_op_type(self):
        return self._op_type


    _doc = 'The operation type.\n    @type: L{Enum<onep.core.util.Enum>}\n    '
    op_type = property(_get_op_type, None, None, _doc)


# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:22:57 IST
