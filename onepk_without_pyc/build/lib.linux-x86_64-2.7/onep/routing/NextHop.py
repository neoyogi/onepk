# 2015.02.05 17:20:02 IST
from onep.routing.Scope import Scope
from onep.core.exception.OnepIllegalArgumentException import OnepIllegalArgumentException

class NextHop(object):
    _scope = Scope()
    _error_code = int()

    def _get_scope(self):
        return self._scope



    def _set_scope(self, scope):
        if not scope or not isinstance(scope, Scope):
            raise OnepIllegalArgumentException('Invalid', 'scope')
        self._scope = scope


    _doc = 'The the next hop scope to set.\n    @type: L{Scope<onep.routing.Scope>}\n    '
    scope = property(_get_scope, _set_scope, None, _doc)

    def _get_error_code(self):
        return self._error_code


    _doc = 'Gets the the next hop error code.\n    It is available for checking after route update operation and\n    possible values are SUCCESS or FAILURE. It no add/remove\n    operation has been performed, the error code should be NONE.\n    \n    @type: C{int} \n    '
    error_code = property(_get_error_code, None, None, _doc)


# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:20:02 IST
