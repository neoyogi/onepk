# 2015.02.05 17:20:04 IST
from onep.routing.Scope import Scope
from onep.core.exception.OnepIllegalArgumentException import OnepIllegalArgumentException
from onep.RoutingIDL import ttypes
from onep.core.util.Enum import enum
import logging

class L3UnicastScope(Scope):
    AFIType = enum('UNKNOWN', 'IPV4', 'IPV6')
    SAFIType = enum('UNKNOWN', 'UNICAST', 'MULTICAST')
    _afi = None
    _safi = None
    _topology = None

    def __init__0(self):
        super(L3UnicastScope, self).__init__()
        self._vrf = ''
        self._afi = self.AFIType.IPV4
        self._safi = self.SAFIType.UNICAST
        self._topology = ''



    def __init__(self, vrf = None, afi = None, safi = None, topology = None):
        """
        Constructor
        
        @param vrf: Name of the VRF. An empty string means default VRF.
                    If the input is None, it will be interpreted as
                    empty string.
        @type vrf: C{str}
        @param afi: The address family. See AFIType for allowed value.
                    If this parameter is None, default is IPV4.
        @type afi : C{int}
        @param safi: The subsequence address family. See SAFIType for
                     allowed value.
                     If this parameter is None, default is UNICAST.
        @type safi : C{int}
        @param topology : Name of the topology. An empty string means the
                          default topology. If the input is None, it will be
                          interpreted as empty string.
        @type topology: C{str}
        @raise OnepIllegalArgumentException : The exception is thrown if vrf is invalid.
        """
        if vrf == None and afi == None and safi == None and topology == None:
            self.__init__0()
        else:
            self.__init__1(vrf, afi, safi, topology)
        self.log = logging.getLogger('onep.' + __name__)



    def __init__1(self, vrf, afi, safi, topology):
        super(L3UnicastScope, self).__init__()
        if vrf is not None and not isinstance(vrf, str):
            raise OnepIllegalArgumentException('vrf', 'invalid')
        if vrf is None:
            self._vrf = ''
        else:
            self._vrf = vrf
        if afi == None:
            self._afi = self.AFIType.IPV4
        elif not isinstance(afi, int):
            raise OnepIllegalArgumentException('afi', 'invalid')
        if afi < self.AFIType.UNKNOWN or afi > self.AFIType.IPV6:
            raise OnepIllegalArgumentException('afi', 'invalid')
        self._afi = afi
        if safi == None:
            self._safi = self.SAFIType.UNICAST
        elif not isinstance(safi, int):
            raise OnepIllegalArgumentException('safi', 'invalid')
        if safi < self.SAFIType.UNKNOWN or safi > self.SAFIType.MULTICAST:
            raise OnepIllegalArgumentException('safi', 'invalid')
        self._safi = safi
        if topology is None:
            self._topology = ''
        else:
            self._topology = topology



    def _get_afi(self):
        return self._afi



    def _set_afi(self, afi):
        if afi == None:
            self._afi = self.AFIType.IPV4
        elif not isinstance(afi, int):
            raise OnepIllegalArgumentException
        if afi < self.AFIType.UNKNOWN or afi > self.AFIType.IPV6:
            raise OnepIllegalArgumentException
        self._afi = afi


    _doc = '\n    The address family to set.\n    If this parameter is null, default is IPV4\n    @type: C{int}\n    @raise OnepIllegalArgumentException: If afi is invalid\n    '
    afi = property(_get_afi, _set_afi, None, _doc)

    def _get_safi(self):
        return self._safi



    def _set_safi(self, safi):
        if safi == None:
            self._safi = self.SAFIType.UNICAST
        elif not isinstance(safi, int):
            raise OnepIllegalArgumentException
        if safi < self.SAFIType.UNKNOWN or safi > self.SAFIType.MULTICAST:
            raise OnepIllegalArgumentException
        self._safi = safi


    _doc = '\n    Sets the subsequence address family.\n    If this parameter is null, default is UNICAST.\n    \n    @type: C{int}\n    @raise OnepIllegalArgumentException: If SAFI is invalid\n    '
    safi = property(_get_safi, _set_safi, None, _doc)

    def _get_topology_name(self):
        return self._topology



    def _set_topology_name(self, topology):
        self._topology = '' if topology == None else topology


    _doc = '\n    Sets name of the topology. None means the default topology.\n    An empty string means the default topology.\n    \n    @type: C{str}\n    '
    topology = property(_get_topology_name, _set_topology_name, None, _doc)

    def __str__(self):
        """
        Returns a string representation of the L3UnicastScope object.
        
        @return: a string representation of the object
        """
        return 'Scope[vrf:' + self.vrf + ',' + 'afi:' + str(self.AFIType.enumval(self.afi)) + ',' + 'safi:' + str(self.SAFIType.enumval(self.safi)) + ',' + 'topology:' + self.topology + ']'



    def _to_idl(self):
        self.log.info('Calling L3UcastScopeIDL')
        return ttypes.L3UcastScopeIDL(self._afi, self._safi, self._topology, self._vrf)



    @staticmethod
    def _from_idl(scopeIdl):
        try:
            return L3UnicastScope(scopeIdl.vrfName, scopeIdl.afi, scopeIdl.safi, scopeIdl.topoName)
        except OnepIllegalArgumentException:
            return None




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:20:04 IST
