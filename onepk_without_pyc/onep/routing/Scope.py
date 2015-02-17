# 2015.02.05 17:22:58 IST
from onep.core.exception.OnepIllegalArgumentException import OnepIllegalArgumentException

class Scope(object):
    """
    This abstract class is the parent class of L3UnicastScope and
    in the future for L3MulticastScope, L2UnicastScope,
    L2MulticastScope, etc.
    
    All common fields among these derived class will be defined in this
    class.
    """

    _vrf = str()

    def _get_vrf(self):
        return self._vrf



    def _set_vrf(self, vrf):
        if vrf is not None and not isinstance(vrf, str):
            raise OnepIllegalArgumentException(vrf + 'Invalid argument for vrf')
        if vrf is None:
            self._vrf = ''
        else:
            self._vrf = vrf


    _doc = ' Name of the VRF. An empty string means default VRF.\n    If the input is None, it will be interpreted as\n    empty string.\n    \n    @type: C{str}\n    @raise OnepIllegalArgumentException: If vrf is invalid \n    '
    vrf = property(_get_vrf, _set_vrf, None, _doc)


# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:22:58 IST
