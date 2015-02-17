# 2015.02.05 17:19:55 IST
from onep.core.util.Enum import *
from onep.interfaces.NetworkInterface import NetworkInterface
from onep.core.util.OnepArgumentTypeValidate import *
from onep.core.exception.OnepIllegalArgumentException import OnepIllegalArgumentException
import logging

class Target(object):
    """ Target Class.
        
        This class represents a network element resource to which a policy is applied.
        
        A target is an interface on a network element or a Firewall Zone Pair
    
        """

    TargetLocation = enum(HARDWARE_DEFINED_INPUT=0, HARDWARE_DEFINED_OUTPUT=1, HARDWARE_DEFINED_BOTH=2)

    def __init__(self, target, location = None):
        """
                Constructor of class Target.
        
                Throws on error
                    OnepIllegalArgumentException - target not proper class
        
                Keyword arguments
                target   -- NetworkInterface class or FirewallZonePair class
                location -- Target.TargetLocation
                                HARDWARE_DEFINED_INPUT
                                HARDWARE_DEFINED_OUTPUT
                                HARDWARE_DEFINED_BOTH
        
                """
        self.network_interface = None
        self.zone_pair = None
        self.log = logging.getLogger(__name__)
        if not target:
            raise OnepIllegalArgumentException('No target')
        if isinstance(target, NetworkInterface):
            try:
                validate(target, NetworkInterface)
            except OnepIllegalArgumentException as e:
                raise e
            self.network_interface = target
            self.xoshandle = target.xos_handle
        if location and not self.TargetLocation._is_valid(location):
            raise OnepIllegalArgumentException('Passed location parameter value ' + str(location) + ' is invalid.')
        self.location = location



    def _get_target_by_xoshandle(self, xoshandle):
        if self.network_interface and self.network_interface.xos_handle == xoshandle:
            return self.network_interface
        if self.zone_pair and self.zone_pair.xos_handle == xoshandle:
            return self.zone_pair



    def _get_target_by_name(self, name):
        if self.network_interface and self.network_interface.name == name:
            return self.network_interface
        if self.zone_pair and self.zone_pair.name == name:
            return self.zone_pair



    def _get_network_element(self):
        """
        """
        if self.zone_pair:
            return zone_pair.network_element
        if self.network_interface:
            return self.network_interface._network_element




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:19:55 IST
