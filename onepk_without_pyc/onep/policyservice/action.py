# 2015.02.05 17:22:52 IST
from abc import *
import logging
import abc
from ctypes import c_byte
from array import array
from onep.core.util.Enum import enum
from onep.core.exception.OnepIllegalArgumentException import OnepIllegalArgumentException
from onep.core.exception import OnepNotSupportedException
from onep.core.util.OnepConstants import OnepConstants
from onep.core.util.HostIpCheck import HostIpCheck
from onep.core.util.OnepArgumentTypeValidate import _validate_mac_address
from onep.PolicyBulkIDL.ttypes import *
from onep.interfaces.NetworkInterface import NetworkInterface
ActionType = enum(NONE=0, DROP=1, COPY=2, DIVERT=3, XMIT=4, SET_QOS_GROUP=5, SET_MPLS_EXP=6, SET_DSCP=7, MARK=8, SET_MPLS_EXP_TOPMOST=9, SET_TUNNEL_DSCP=10, HDR_COMPRESS=11, OUTPUT_INTERFACE=12, POLICE=13, SHAPE=14, WRED=15, PRIORITY_QUEUE=16, CLASS_BASED_QUEUE=17, FAIR_QUEUE=18, QUEUE_LIMIT=19, NEXT_HOP=20, SET_TOS=21, SET_DST_MAC=22, SET_SRC_MAC=23, SET_DST_IP=24, SET_SRC_IP=25, SET_DST_UDP_PORT=26, SET_DST_TCP_PORT=27, SET_DST_SCTP_PORT=28, SET_SRC_UDP_PORT=29, SET_SRC_TCP_PORT=30, SET_SRC_SCTP_PORT=31, SET_IP_PROTOCOL=32, SET_VLAN_ID=33, POP_VLAN_ID=34, PUSH_VLAN_ID=35, SET_L2_COS=36, FORWARD_CLASS=37, FORWARD_NORMAL=38, BANDWIDTH=39, INSPECT=40, SET_MPLS_LABEL=41, GOTO_TABLE=42, WRITE_METADATA=43, WRITE=44, CLEAR=45, APPLY=46, COPY_TTL_OUT=47, COPY_TTL_IN=48, SET_MPLS_TTL=49, DEC_MPLS_TTL=50, PUSH_MPLS_LABEL=51, POP_MPLS_LABEL=52, SET_IP_TTL=53, DEC_IP_TTL=54, SET_MPLS_TC=55, COPY_TTL_IN_IF_LESS=56, OUTPUT_FLOOD=57, OUTPUT_ALL=58, OUTPUT_LOCAL=59, WRED_PROFILE=60, LAST=61)
_map_external_action = {ActionType.NONE: 0,
 ActionType.DROP: 1,
 ActionType.COPY: 3,
 ActionType.DIVERT: 4,
 ActionType.FORWARD_NORMAL: 5,
 ActionType.OUTPUT_INTERFACE: 6,
 ActionType.SET_DST_MAC: 7,
 ActionType.SET_SRC_MAC: 7,
 ActionType.SET_QOS_GROUP: 8,
 ActionType.SET_DSCP: 8,
 ActionType.MARK: 8,
 ActionType.SET_L2_COS: 8,
 ActionType.POLICE: 9,
 ActionType.SHAPE: 10,
 ActionType.WRED_PROFILE: 11,
 ActionType.PRIORITY_QUEUE: 12,
 ActionType.CLASS_BASED_QUEUE: 13,
 ActionType.BANDWIDTH: 13,
 ActionType.FAIR_QUEUE: 14,
 ActionType.QUEUE_LIMIT: 15,
 ActionType.NEXT_HOP: 16,
 ActionType.SET_VLAN_ID: 17,
 ActionType.POP_VLAN_ID: 17,
 ActionType.PUSH_VLAN_ID: 17,
 ActionType.FORWARD_CLASS: 18,
 ActionType.SET_DST_IP: 19,
 ActionType.SET_SRC_IP: 19,
 ActionType.SET_DST_TCP_PORT: 20,
 ActionType.SET_SRC_TCP_PORT: 20,
 ActionType.WRED: 21,
 ActionType.SET_MPLS_EXP: 22,
 ActionType.INSPECT: 25,
 ActionType.SET_IP_PROTOCOL: 30}
RateUnits = enum(RATE_UNITS_BPS=1, RATE_UNITS_PERCENT=2)
BurstUnits = enum(BURST_UNITS_BITS=1, BURST_UNITS_MSEC=2)
ThresholdUnits = enum(UNITS_PKTS=1, UNITS_BYTES=2, UNITS_CELLS=3, UNITS_PERCENT=4, UNITS_MSEC=5)
Direction = enum(SOURCE=0, DESTINATION=1)

class Action(object):
    """
        The Action class is an abstract class that represents an action to be applied 
        to a policy entry (PolicyMap.Entry). The Action object specifies the actions 
        to be performed when a packet matches the match criteria. There may be 
        one or more actions within an entry. There are different 
        types of action objects that specify details of each action to be performed.
        It is also possible that an action object can contain a dependent action object.
        You will see this object assigned to the dependent_action instance variable.
    
        ***DEPRECATED***
        The following enums were copied to root of action.py module because they
        are used by multiple classes in the module.  Eventually they will be removed
        from this class.
    
        RateUnits
        BurstUnits
        BandwidthUnits
        ThresholdUnits
        ActionType
        Direction
        ***********
    
        @undocumented: __init__
        """

    __metaclass__ = abc.ABCMeta
    _action_type = 0
    _op_code = 0
    _handle = 0
    _log = logging.getLogger(__name__)
    RateUnits = RateUnits
    BandwidthUnits = RateUnits
    BurstUnits = BurstUnits
    ThresholdUnits = ThresholdUnits
    ActionType = ActionType
    Direction = Direction

    def __init__(self, action_type):
        """
        Action abstract class constructor for internal use only
        """
        self.action_type = action_type
        self.op_code = self.ActionOpCode.CREATE
        self.dependent_action = None



    def check_action_support(self, capable_actions):
        """
                Check to see if policy action is supported on network element
        
                @param capable_actions: list of ActionType from network element
                @type capable_actions: L{ActionType<action.ActionType>}
        
                @return: Returns True if supported False if not
                @rtype: C{bool}
        
                """
        self._log.debug('ACTION CAPS ' + str(capable_actions))
        if hasattr(self, '_external_type'):
            act_type = self._external_type
            self._log.debug('external type ' + ActionType.enumval(act_type))
        else:
            act_type = self._map_internal_action[self.action_type]
            self._log.debug('external type mapped ' + ActionType.enumval(act_type))
        return act_type in capable_actions



    def get_action_type(self):
        """
                Return ActionType of action class (action_type variable is internal only)
        
                @return: Return ActionType of action
                @rtype: L{ActionType<action.ActionType>}
        
                """
        if hasattr(self, '_external_type'):
            return self._external_type
        else:
            return self._map_internal_action[self.action_type]



    @abstractmethod
    def _to_idl(self):
        pass


    _internal_action_types = enum(NONE=0, DROP=1, PKT_DROP=2, COPY=3, DIVERT=4, NORMAL=5, OUTPUT_INTERFACE=6, MAC_ADDRESS=7, MARK=8, POLICE=9, SHAPE=10, WRED_PROFILE=11, PRIORITY_QUEUE=12, CLASS_BASED_QUEUE=13, FAIR_QUEUE=14, QUEUE_LIMIT=15, NEXT_HOP=16, VLAN=17, FWD_CLASS_ID=18, IP_ADDRESS=19, TCP_PORT=20, WRED=21, MPLS_EXP=22, INSPECT=25, PROTOCOL=30)
    _map_internal_action = {0: ActionType.NONE,
     1: ActionType.DROP,
     3: ActionType.COPY,
     4: ActionType.DIVERT,
     5: ActionType.FORWARD_NORMAL,
     6: ActionType.OUTPUT_INTERFACE,
     9: ActionType.POLICE,
     10: ActionType.SHAPE,
     11: ActionType.WRED_PROFILE,
     12: ActionType.PRIORITY_QUEUE,
     13: ActionType.CLASS_BASED_QUEUE,
     14: ActionType.FAIR_QUEUE,
     15: ActionType.QUEUE_LIMIT,
     16: ActionType.NEXT_HOP,
     18: ActionType.FORWARD_CLASS,
     21: ActionType.WRED,
     22: ActionType.SET_MPLS_EXP,
     25: ActionType.INSPECT,
     30: ActionType.SET_IP_PROTOCOL}
    ActionOpCode = enum('CREATE', 'MOD', 'DEL', 'REP')

    def _get_actiontype(self):
        return self._action_type



    def _set_actiontype(self, actiontype):
        self._action_type = actiontype


    action_type = property(_get_actiontype, _set_actiontype, None, None)

    def _get_opcode(self):
        return self._op_code



    def _set_opcode(self, opcode):
        self._op_code = opcode


    op_code = property(_get_opcode, _set_opcode, None, None)

    def _get_handle(self):
        return self._handle



    def _set_handle(self, handle):
        self._handle = handle


    handle = property(_get_handle, _set_handle, None, None)

    @classmethod
    def _to_idl_list(cls, inst_list):
        idl_list = []
        for i in inst_list:
            idl_list.append(i._to_idl())

        return idl_list



    @classmethod
    def _from_idl_list(cls, idl_list, element):
        inst_list = []
        for idl in idl_list:
            act_type = cls._internal_action_types.enumval(idl.type)
            if act_type == 'NONE':
                pass
            elif act_type == 'DROP':
                pass
            elif act_type == 'COPY':
                inst_list.append(PacketCopy._from_idl(idl))
            elif act_type == 'DIVERT':
                inst_list.append(PacketDivert._from_idl(idl))
            elif act_type == 'NORMAL':
                pass
            elif act_type == 'OUTPUT_INTERFACE':
                inst_list.append(OutInterface._from_idl(idl, element))
            elif act_type == 'MAC_ADDRESS':
                inst_list.append(MACAddress._from_idl(idl))
            elif act_type == 'MARK':
                inst_list.append(Mark._from_idl(idl))
            elif act_type == 'POLICE':
                inst_list.append(Police._from_idl(idl))
            elif act_type == 'SHAPE':
                inst_list.append(Shape._from_idl(idl))
            elif act_type == 'WRED_PROFILE':
                inst_list.append(WREDProfile._from_idl(idl))
            elif act_type == 'PRIORITY_QUEUE':
                inst_list.append.add(PriorityQueue._from_idl(idl))
            elif act_type == 'CLASS_BASED_QUEUE':
                inst_list.append(ClassQueue._from_idl(idl))
            elif act_type == 'FAIR_QUEUE':
                inst_list.append(FairQueue._from_idl(idl))
            elif act_type == 'QUEUE_LIMIT':
                inst_list.append(QueueLimit._from_idl(idl))
            elif act_type == 'NEXT_HOP':
                inst_list.append(NextHop._from_idl(idl))
            elif act_type == 'VLAN':
                inst_list.append(VLAN._from_idl(idl))
            elif act_type == 'FWD_CLASS_ID':
                pass
            elif act_type == 'IP_ADDRESS':
                pass
            elif act_type == 'TCP_PORT':
                pass
            elif act_type == 'WRED':
                inst_list.append(WRED._from_idl(idl))
            elif act_type == 'MPLS_EXP':
                pass
            elif act_type == 'INSPECT':
                pass
            elif act_type == 'PROTOCOL':
                pass

        return inst_list




class OutInterface(Action):
    """
    Action to direct packet to an output interface.
    
    @undocumented: interface_list
    """


    def __init__(self, intf_list):
        """
        @param intf_list: NetworkInterface List of all of the OutInterfaces.
        @type intf_list: L{NetworkInterface<onep.interfaces.NetworkInterface>}  
        """
        super(OutInterface, self).__init__(self._internal_action_types.OUTPUT_INTERFACE)
        self.interface_list = intf_list



    def __eq__(self, obj):
        if obj == None:
            return False
        else:
            if not isinstance(obj, type(self)):
                return False
            if self is obj:
                return True
            if self.interface_list == obj.interface_list:
                return True
            return False



    def _to_idl(self):
        idl = ActionIDL(0, 0, 0, 0, 0)
        idl.actionType = self.action_type
        ilist = []
        for ni in self.interface_list:
            ilist.append(ni.xos_handle)

        idl.outIfAction = ActionOutInterfaceIDL(ilist)
        idl.opCode = self.op_code
        return idl



    @classmethod
    def _from_idl(cls, idl, element):
        if idl == None:
            return 
        try:
            hlist = idl.outIfAction.ifHandle
            intf_list = []
            for ni_handle in hlist:
                intf = NetworkInterface(element, None, NetworkInterface.InterfaceTypes.ONEP_IF_TYPE_ANY, ni_handle)
                intf_list.append(intf)

            aobj = OutInterface(intf_list)
            aobj.handle = idl.actionHandle
            return aobj
        except OnepIllegalArgumentException as e:
            cls._log.debug(e.message)



    def get_interface_list(self):
        """
        Gets the list of interface.
        
        @return: List of interfaces
        @rtype: C{list}
        """
        return self.interface_list




class MPLS(Action):
    """
        Action class for MPLS
    
        ActionType.SET_MPLS_EXP - MPLS Experimental field
    
        @ivar type: MPLS ActionType
        @type type: L{type<onep.policyservice.action.ActionType>}
    
        @ivar value: MPLS action value
        @type value: C{int} 
    
        """


    def __init__(self, type, value):
        """
                @param type: MPLS ActionType
                @type type: L{type<onep.policyservice.action.ActionType>}
                
                @param value: MPLS action value
                @type value: C{int}  
        
                """
        super(MPLS, self).__init__(self._internal_action_types.MPLS_EXP)
        self.value = value



    @property
    def value(self):
        """MPLS action value"""
        return self._value



    @value.setter
    def value(self, val):
        if self.action_type == self._internal_action_types.MPLS_EXP:
            if val < 0 or val > 7 or not isinstance(val, int):
                raise OnepIllegalArgumentException('MPLS experimental must be 0 to 7')
        self._value = val



    def _to_idl(self):
        idl = ActionIDL(0, 0, 0, 0, 0)
        idl.actionType = self.action_type
        idl.mplsExpAction = ActionMplsExpIDL(0, self.value)
        idl.opCode = self.op_code
        return idl



    @classmethod
    def _from_idl(cls, idl, element):
        if idl == None:
            return 
        return MPLS(idl.actionType, idl.mplsExpAction.mplsExp)



    def __eq__(self, obj):
        if not isinstance(obj, MPLS):
            return False
        return self.action_type == obj.action_type and self.value == obj.value




class Mark(Action):
    """
        Action to mark packet.
    
        Actions include:
        ActionType.SET_DSCP
        ActionType.SET_L2_COS
        ActionType.SET_QOS_GROUP
        ActionType.SET_MPLS_EXP
        **************************
        *** MPLS actions moved ***
        *** to MPLS class      ***
        **************************
    
        ***DEPRECATED***
        MarkType enum is deprecated.  Please use action.ActionTypes
        ***********
        
        @undocumented: value
        """

    MarkType = enum(MARK_IP_DSCP=ActionType.SET_DSCP, MARK_L2_COS=ActionType.SET_L2_COS, MARK_QOS_GROUP=ActionType.SET_QOS_GROUP, MARK_MPLS_EXP=ActionType.SET_MPLS_EXP, MARK_MPLS_EXP_TOPMOST=ActionType.SET_MPLS_EXP_TOPMOST)

    def _get_value(self):
        return self._value



    def _set_value(self, value):
        self._value = value


    _doc = '\n    The value of this Mark Action\n    @type: C{int}\n    '
    value = property(_get_value, _set_value, None, _doc)
    _external_mark_map = {ActionType.SET_DSCP: 0,
     ActionType.SET_L2_COS: 1,
     ActionType.SET_QOS_GROUP: 2,
     ActionType.SET_MPLS_EXP: 3,
     ActionType.SET_MPLS_EXP_TOPMOST: 4}

    def __init__(self, mark_type, value):
        """
                @param mark_type: Marking ActionType
                @type mark_type: L{mark_type<onep.policyservice.action.ActionType>}
                
                @param value: Marking value
                @type value: C{int}  
        
                """
        if mark_type == ActionType.SET_MPLS_EXP:
            if value < 0 or value > 7 or not isinstance(value, int):
                raise OnepIllegalArgumentException('MPLS experimental must be 0 to 7')
            super(Mark, self).__init__(self._internal_action_types.MPLS_EXP)
        elif mark_type == ActionType.SET_DSCP:
            if value < 0 or value > 63 or not isinstance(value, int):
                raise OnepIllegalArgumentException('DSCP must be 0 to 63')
        super(Mark, self).__init__(self._internal_action_types.MARK)
        self._external_type = mark_type
        self._mark_type = self._external_mark_map.get(mark_type)
        self.value = value



    def _to_idl(self):
        idl = ActionIDL(0, 0, 0, 0, 0)
        idl.actionType = self.action_type
        if self.action_type == self._internal_action_types.MPLS_EXP:
            idl.mplsExpAction = ActionMplsExpIDL(0, self.value)
        else:
            idl.markAction = ActionMarkIDL(self._mark_type, self.value)
        idl.opCode = self.op_code
        return idl



    @classmethod
    def _from_idl(cls, idl):
        if idl == None:
            return 
        aobj = Mark(cls._external_map[idl.markAction.type], idl.markAction.value)
        aobj.handle = idl.actionHandle
        return aobj



    def __eq__(self, obj):
        if not isinstance(obj, Mark):
            return False
        return self._mark_type == obj._mark_type and self.value == obj.value




class Police(Action):
    """
    Action to police traffic.
    
    """

    PoliceActionType = enum('POLICE_ACTION_UNKNOWN', 'POLICE_ACTION_DROP', 'POLICE_ACTION_XMIT', 'POLICE_ACTION_SET_QOS_GROUP', 'POLICE_ACTION_SET_MPLS_EXP', 'POLICE_ACTION_SET_DSCP', 'POLICE_ACTION_SET_L2_COS', 'POLICE_ACTION_SET_MPLS_EXP_TOPMOST', 'POLICE_ACTION_SET_TUNNEL_DSCP')

    def _validate_police_action(self, action, value):
        if not self.PoliceActionType._is_valid(action):
            return False
        if self.PoliceActionType.enumval(action) == 'POLICE_ACTION_SET_DSCP' or self.PoliceActionType.enumval(action) == 'POLICE_ACTION_SET_TUNNEL_DSCP':
            return isinstance(value, int) and value > -1 and value < 64
        return True



    def __init__(self, rate_units, burst_units, cir, pir = 0, cbs = 0, ebs = 0, conform_action = 0, conform_value = 0, exceed_action = 0, exceed_value = 0, violate_action = 0, violate_value = 0, conform_color = 0, exceed_color = 0):
        """
                @param rate_units: The units for measuring the rate 
                @type rate_units: L{RateUnits<onep.policyservice.action.RateUnits>}
            
                @param burst_units: The units for measuring the burst
                @type burst_units: L{BurstUnits<onep.policyservice.action.BurstUnits>}
            
                @param cir: Committed information rate (CIR)
                @type cir: C{int}  
            
                @param pir: Peak information rate (PIR)
                @type pir: C{int}  
            
                @param cbs: Committed burst size (CBS)
                @type cbs: C{int}  
            
                @param ebs: Excess burst size (EBS)
                @type ebs: C{int}  
            
                @param conform_color: Conform-color class - for color-aware policing, 
                                      this is the handle of the class that specifies the  
                                      conform-color for incoming packets marked by a previous node.
                @type conform_color: C{int}  
            
                @param exceed_color: Exceed-color class - for color-aware policing, 
                                     this is the handle of the class that specifies 
                                     the exceed-color for incoming packets marked by a previous node.
                @type exceed_color: C{int}  
            
                @param conform_action: Action applied to conforming traffic
                @type conform_action: L{PoliceActionType<onep.policyservice.action.Police.PoliceActionType>}  
            
                @param exceed_action: Action applied to excess traffic
                @type exceed_action: L{PoliceActionType<onep.policyservice.action.Police.PoliceActionType>}  
            
                @param violate_action: Action applied to excess traffic
                @type violate_action: L{PoliceActionType<onep.policyservice.action.Police.PoliceActionType>}  
            
                @param conform_value: Action value applied to conforming traffic
                @type conform_value: C{int}  
            
                @param exceed_value: Action value applied to excess traffic
                @type exceed_value: C{int}  
            
                @param violate_value: Action value applied to traffic in violation
                @type violate_value: C{int}
        
                """
        super(Police, self).__init__(self._internal_action_types.POLICE)
        self.log = logging.getLogger(__name__)
        if rate_units == RateUnits.RATE_UNITS_PERCENT:
            if cir < 1 or cir > 100:
                raise OnepIllegalArgumentException('cir must be between 1 and 100 percent')
            if pir and pir > 100:
                raise OnepIllegalArgumentException('pir must be between 1 and 100 percent')
        if pir and cir > pir:
            raise OnepIllegalArgumentException('cir must be less than pir')
        if self._validate_police_action(conform_action, conform_value) == False:
            raise OnepIllegalArgumentException('conform action setting invlaid')
        if self._validate_police_action(exceed_action, exceed_value) == False:
            raise OnepIllegalArgumentException('exceed action setting invalid')
        if self._validate_police_action(violate_action, violate_value) == False:
            raise OnepIllegalArgumentException('violate action setting invalid')
        self.cir = cir
        self.pir = pir
        self.cbs = cbs
        self.ebs = ebs
        self.rate_units = rate_units
        self.burst_units = burst_units
        self.conform_action = conform_action
        self.exceed_action = exceed_action
        self.violate_action = violate_action
        self.conform_value = conform_value
        self.exceed_value = exceed_value
        self.violate_value = violate_value
        self.conform_color = conform_color
        self.exceed_color = exceed_color



    def __eq__(self, obj):
        if obj == None:
            return False
        if not isinstance(obj, type(self)):
            return False
        if self is obj:
            return True
        return self.rateUnits.equals(obj.rateUnits) and self.burstUnits.equals(obj.burstUnits) and self.cir == obj.cir and self.pir == obj.pir and self.cbs == obj.cbs and self.ebs == obj.ebs and self.conform_color == obj.conform_color and self.exceed_color == obj.exceed_color and self.conform_action == obj.conform_action and self.exceed_action == obj.exceed_action and self.violate_action == obj.violate_action and self.conform_value == obj.conform_value and self.exceed_value == obj.exceed_value and self.violate_value == obj.violate_value



    def _to_idl(self):
        idl = ActionIDL(0, 0, 0, 0, 0)
        idl.actionType = self.action_type
        idl.policeAction = ActionPoliceIDL(self.rate_units, self.burst_units, self.cir, self.pir, self.cbs, self.ebs, self.conform_action, self.conform_value, self.exceed_action, self.exceed_value, self.violate_action, self.violate_value, self.conform_color, self.exceed_color)
        idl.opCode = self.op_code
        return idl



    @classmethod
    def _from_idl(cls, idl):
        if idl == None:
            return 
        try:
            aobj = Police(idl.policeAction.rateUnits, idl.policeActionburstUnits, idl.policeAction.cir, idl.policeAction.cir, idl.policeAction.cbs, idl.getPoliceAction.ebs, idl.policeAction.conformAction, idl.policeAction.conformValue, idl.policeAction.exceedAction, idl.policeAction.exceedValue, idl.policeAction.violateAction, idl.policeAction.violateValue, idl.policeAction.conformColor, idl.policeAction.exceedColor)
            aobj.handle = idl.actionHandle
            return aobj
        except OnepIllegalArgumentException as e:
            cls._log.error(e.message)



ShapeType = enum(SHAPE_AVG=1, SHAPE_PEAK=2)

class Shape(Action):
    """
    Action to shape traffic.
    
    """


    def __init__(self, type = ShapeType.SHAPE_AVG, rate_units = RateUnits.RATE_UNITS_BPS, cir = None, cbs = None, burst_units = BurstUnits.BURST_UNITS_BITS, ebs = None):
        """
                @param shape_type: Shape type: average or peak
                @type shape_type: L{ShapeType<onep.policyservice.action.Shape.ShapeType>}
        
                @param rate_units: The units for measuring the rate
                @type rate_units: L{RateUnits<onep.policyservice.action.RateUnits>}
        
                @param burst_units: The units for measuring the burst
                @type burst_units: L{BurstUnits<onep.policyservice.action.BurstUnits>}
        
                @param cir: Committed information rate (CIR)
                @type cir: C{int}
        
                @param cbs: Committed burst size (CBS)
                @type cbs: C{int}
        
                @param ebs: Excess burst size (EBS)
                @type ebs: C{int}
        
                """
        super(Shape, self).__init__(self._internal_action_types.SHAPE)
        self.shape_type = type
        self.rate_units = rate_units
        self.cir = cir
        self.burst_units = burst_units
        self.cbs = cbs
        self.ebs = ebs
        if not cbs:
            self.burst_units = None
            self.ebs = None



    def __eq__(self, obj):
        if obj == None:
            return False
        if not isinstance(obj, type(self)):
            return False
        if self is obj:
            return True
        return self.shape_type == obj.shape_type and self.rate_units == obj.rate_units and self.cir == obj.cir and self.burst_units == obj.burst_units and self.cbs == obj.cbs and self.ebs == obj.ebs



    def _to_idl(self):
        idl = ActionIDL(0, 0, 0, 0, 0)
        idl.actionType = self.action_type
        idl.shapeAction = ActionShapeIDL(self.shape_type, self.rate_units, self.burst_units, self.cir, self.cbs, self.ebs)
        idl.opCode = self.op_code
        return idl



    @classmethod
    def _from_idl(cls, idl):
        if idl == None:
            return 
        aobj = Shape(idl.shapeActiontype, idl.shapeAction.rateUnits, idl.shapeAction.burstUnits, idl.shapeAction.cir, idl.shapeAction.cbs, idl.shapeAction.ebs)
        aobj.handle = idl.actionHandle
        return aobj



QueueSizeUnits = enum(QUEUE_UNITS_PKTS=1, QUEUE_UNITS_BYTES=2, QUEUE_UNITS_MSEC=3)

class PriorityQueue(Action):
    """
    Action to control traffic priority queue.
    
    @undocumented: burst
    @undocumented: level
    @undocumented: bandwidth
    """


    def __init__(self, bandwidth, bandwidth_units, level, burst, queue_size, queuesize_units):
        """
                @param bandwidth: The maximum rate at which priority service is guaranteed.
                @type bandwidth:  C{int}
        
                @param bandwidth_units: Bandwidth units: kbit/s or percentage
                @type bandwidth_units: L{BandwidthUnits<onep.policyservice.action.BandwidthUnits>}
        
                @param level: Priority level
                @type level: C{int}
        
                @param burst: Burst size
                @type burst: C{int}
        
                @param queue_size: Queue size
                @type queue_size: C{int}
        
                @param queuesize_units: Queue size units
                @type queuesize_units: L{QueueSizeUnits<onep.policyservice.action.QueueSizeUnits>}
        
                """
        super(PriorityQueue, self).__init__(self._internal_action_types.PRIORITY_QUEUE)
        self.bandwidth = bandwidth
        self.bandwidth_units = bandwidth_units
        self.level = level
        self.burst = burst
        self.queue_size = queue_size
        self.queuesize_units = queuesize_units



    def __eq__(self, obj):
        if obj == None:
            return False
        if not isinstance(obj, type(self)):
            return False
        if self is obj:
            return True
        return self.bandwidth == obj.bandwidth and self.bandwidth_units == obj.bandwidth_units and self.level == obj.level and self.burst == obj.burst and self.queue_size == obj.queue_size and self.queuesize_units == obj.queuesize_units



    def _to_idl(self):
        idl = ActionIDL(0, 0, 0, 0, 0)
        idl.actionType = self.action_type
        idl.pqAction = ActionPriorityQueueIDL(self.bandwidth, self.bandwidth_units, self.level, self.burst, self.queue_size, self.queuesize_units)
        idl.opCode = self.op_code
        return idl



    @classmethod
    def _from_idl(cls, idl):
        if idl == None:
            return 
        aobj = PriorityQueue(idl.pqAction.bandwidth, idl.pqAction.bandwidthUnits, idl.pqAction.level, idl.pqAction.burst, idl.pqAction.queueSize, idl.pqAction.queueSizeUnits)
        aobj.handle = idl.actionHandle
        return aobj




class ClassQueue(Action):
    """
    Action to control traffic class-based queue.
    
    """


    def __init__(self, bandwidth, bandwidth_units, queue_size = 0, queuesize_units = 0):
        """
                @param bandwidth: The maximum rate at which priority service is guaranteed.
                @type bandwidth:  C{int}
        
                @param bandwidth_units: Bandwidth units: kbit/s or percentage
                @type bandwidth_units: L{RateUnits<onep.policyservice.action.RateUnits>}
        
                @param queue_size: Queue size
                @type queue_size: C{int}
        
                @param queuesize_units: Queue size units
                @type queuesize_units: L{QueueSizeUnits<onep.policyservice.action.QueueSizeUnits>}
        
                """
        if bandwidth < 0:
            raise OnepIllegalArgumentException('Invalid bandwidth', str(bandwidth))
        if not RateUnits._is_valid(bandwidth_units):
            raise OnepIllegalArgumentException('Invalid bandwidth_units', str(bandwidth_units))
        if bandwidth_units == RateUnits.RATE_UNITS_PERCENT and bandwidth > 100:
            raise OnepIllegalArgumentException('Invalid percent bandwidth', str(bandwidth))
        if queue_size < 0:
            raise OnepIllegalArgumentException('Invalid queue_size', str(queue_size))
        if queuesize_units and not QueueSizeUnits._is_valid(queuesize_units):
            raise OnepIllegalArgumentException('Invalid queuesize_units', str(queuesize_units))
        super(ClassQueue, self).__init__(self._internal_action_types.CLASS_BASED_QUEUE)
        self.bandwidth = bandwidth
        self.bandwidth_units = bandwidth_units
        self.queue_size = queue_size
        self.queuesize_units = queuesize_units



    def __eq__(self, obj):
        if obj == None:
            return False
        if not isinstance(obj, type(self)):
            return False
        if self is obj:
            return True
        return self.bandwidth == obj.bandwidth and self.bandwidth_units == obj.bandwidth_units and self.queue_size == obj.queueSize and self.queuesize_units == obj.queuesize_units



    def _to_idl(self):
        idl = ActionIDL(0, 0, 0, 0, 0)
        idl.actionType = self.action_type
        idl.cqAction = ActionClassQueueIDL(self.bandwidth, self.bandwidth_units, self.queue_size, self.queuesize_units)
        idl.opCode = self.op_code
        return idl



    @classmethod
    def _from_idl(cls, idl):
        if idl == None:
            return 
        aobj = ClassQueue(idl.cqAction.bandwidth, idl.cqAction.bandwidth_units, idl.cqAction.queueSize, idl.cqAction.queueSizeUnits)
        aobj.handle = idl.actionHandle
        return aobj




class Bandwidth(ClassQueue):
    """
        Bandwidth action
    
        """


    def __init__(self, bandwidth, bandwidth_units):
        """  
                @param bandwidth: The maximum rate at which priority service is guaranteed.
                @type bandwidth:  C{int}
        
                @param bandwidth_units: Bandwidth units: kbit/s or percentage
                @type bandwidth_units: L{RateUnits<action.RateUnits>}
        
                """
        super(Bandwidth, self).__init__(bandwidth, bandwidth_units, 0, 0)
        self._external_type = ActionType.BANDWIDTH




class FairQueue(Action):
    """
    Action to set configure fair queue.
    
    """


    def __init__(self, num_flow_queues, queue_size, queuesize_units):
        """
                @param num_flow_queues: The number of flow queues
                @type num_flow_queues:  C{int}
                
                @param queue_size: Queue size
                @type queue_size: C{int}    
                
                @param queuesize_units: Queue size units
                @type queuesize_units: L{QueueSizeUnits<onep.policyservice.action.QueueSizeUnits>}
        
                """
        super(FairQueue, self).__init__(self._internal_action_types.FAIR_QUEUE)
        self.num_flow_queues = num_flow_queues
        self.queue_size = queue_size
        self.queuesize_units = queuesize_units



    def __eq__(self, obj):
        if obj == None:
            return False
        if not isinstance(obj, type(self)):
            return False
        if self is obj:
            return True
        return self.num_flow_queues == obj.num_flow_queues and self.queue_size == obj.queue_size and self.queuesize_units == obj.queuesize_units



    def _to_idl(self):
        idl = ActionIDL(0, 0, 0, 0, 0)
        idl.actionType = self.action_type
        idl.fqAction = ActionFairQueueIDL(self.num_flow_queues, self.queue_size, self.queuesize_units)
        idl.opCode = self.op_code
        return idl



    @classmethod
    def _from_idl(cls, idl):
        if idl == None:
            return 
        aobj = FairQueue(idl.fqAction.numFlowQueues, idl.fqAction.queueSize, idl.fqAction.queueSizeUnits)
        aobj.handle = idl.actionHandle
        return aobj




class QueueLimit(Action):
    """
    Action to set queue limit.
    
    """


    def __init__(self, queue_size, queuesize_units):
        """
                @param queue_size: Queue size.
                @type queue_size: C{int}    
        
                @param queuesize_units: Queue size units.
                @type queuesize_units: L{QueueSizeUnits<onep.policyservice.action.QueueSizeUnits>}
        
                """
        super(QueueLimit, self).__init__(self._internal_action_types.QUEUE_LIMIT)
        self.queue_size = queue_size
        self.queuesize_units = queuesize_units



    def __eq__(self, obj):
        if obj == None:
            return False
        if not isinstance(obj, type(self)):
            return False
        if self is obj:
            return True
        return self.queue_size == obj.queue_size and self.queuesize_units == obj.queuesize_units



    def _to_idl(self):
        idl = ActionIDL(0, 0, 0, 0, 0)
        idl.actionType = self.action_type
        idl.queueLimitAction = ActionQueueLimitIDL(self.queue_size, self.queuesize_units)
        idl.opCode = self.op_code
        return idl



    @classmethod
    def _from_idl(cls, idl):
        if idl == None:
            return 
        aobj = None
        aobj.handle = idl.actionHandle
        return aobj



WREDType = enum(WRED_DSCP=1, WRED_L2_COS=2)

class WRED(Action):
    """
        Action to set to set Weighted Random Early Detect
    
        """


    def __init__(self, type, ecn_enabled, expon_weight, units):
        """
                @param type: WRED type
                @type type: L{WREDType<onep.policyservice.action.WREDType>}
        
                @param ecn_enabled: True means explicit congestion enabled
                @type ecn_enabled: C{bool}
        
                @param expon_weight: Weight for mean queue depth calculation
                @type expon_weight: C{int}
        
                @param units: Threshold units
                @type units: L{ThresholdUnits<onep.policyservice.action.ThresholdUnits>}
        
                """
        super(WRED, self).__init__(self._internal_action_types.WRED)
        if not WREDType._is_valid(type):
            raise OnepIllegalArgumentException('action.WREDType', type)
        if not ThresholdUnits._is_valid(units):
            raise OnepIllegalArgumentException('ThresholdUnits', units)
        if expon_weight < 0:
            raise OnepIllegalArgumentException('Exponential weight less that zero')
        if not isinstance(ecn_enabled, bool):
            raise OnepIllegalArgumentException('ecn_enabled not True/False')
        self.type = type
        self.ecn_enabled = ecn_enabled
        self.expon_weight = expon_weight
        self.units = units



    def _to_idl(self):
        idl = ActionIDL(0, 0, 0, 0, 0)
        idl.actionType = self.action_type
        idl.wredParam = ActionWredParamIDL(self.type, int(self.ecn_enabled), self.expon_weight, self.units)
        idl.opCode = self.op_code
        return idl



    @classmethod
    def _from_idl(self, idl):
        return WRED(idl.type, bool(idl.ecnEnabled), idl.exponWeight, idl.thresholdUnits)




class WREDProfile(Action):
    """
    Action to set to set Weighted Random Early Detect Profile
    
    """


    def __init__(self, type, value, min_threshold, max_threshold, drop_prob, threshold_units):
        """
                @param wred_type: WRED Type
                @type wred_type: L{WREDType<onep.policyservice.action.WREDType>}
        
                @param value: WRED Value
                @type value: C{int}
        
                @param min_threshold: Minimum threshold
                @type min_threshold: C{int}
        
                @param max_threshold: Maximum threshold
                @type max_threshold: C{int}
        
                @param threshold_units: Threshold Units
                @type threshold_units: L{ThresholdUnits<onep.policyservice.action.ThresholdUnits>}
        
                @param drop_prop: Drop probability
                @type drop_prop: C{int}
        
                """
        super(WREDProfile, self).__init__(self._internal_action_types.WRED_PROFILE)
        if min_threshold < 1 or min_threshold > 4096:
            raise OnepIllegalArgumentException('minThreshold out of range')
        if max_threshold < min_threshold or max_threshold > 4096:
            raise OnepIllegalArgumentException('maxThreshold out of range')
        self.wred_type = type
        self.value = value
        self.min_threshold = min_threshold
        self.max_threshold = max_threshold
        self.threshold_units = threshold_units
        self.drop_prob = drop_prob



    def __eq__(self, obj):
        if obj == None:
            return False
        if not isinstance(obj, type(self)):
            return False
        if self is obj:
            return True
        return self.wred_type == obj.wred_type and self.value == obj.value and self.min_threshold == obj.min_threshold and self.max_threshold == obj.max_threshold and self.threshold_units == obj.threshold_units and self.drop_prob == obj.drop_prob



    def _to_idl(self):
        idl = ActionIDL(0, 0, 0, 0, 0)
        idl.actionType = self.action_type
        idl.wredAction = ActionWredProfileIDL(self.wred_type, self.value, self.min_threshold, self.max_threshold, self.drop_prob, self.threshold_units)
        idl.opCode = self.op_code
        return idl



    @classmethod
    def _from_idl(cls, idl):
        if idl == None:
            return 
        try:
            aobj = WREDProfile(idl.wredAction.type, idl.wredAction.value, idl.wredAction.minThreshold, idl.wredAction.maxThreshold, dl.wredAction.drop_prob, idl.wredAction.threshold_units)
            aobj.handle = idl.actionHandle
            return aobj
        except OnepIllegalArgumentException as e:
            cls._log.error(e.message)




class PacketCopy(Action):
    """
    Action to copy packet to an application. This will duplicate packets 
    and send them to the onePK application. A local ID may be specified 
    that is attached to the packets delivered to the onePK application.
    
    """


    def __init__(self, remote_service_node, app_id, local_id, size, sample_type, sample_rate):
        """
                @param remote_service_node: The value of remote_service_node
                @type remote_service_node: C{int}
                
                @param app_id: The onePK application ID.
                @type app_id: C{int}
                
                @param local_id: The local_id
                @type local_id: C{int}
                
                @param size: The size of sample.
                @type size: C{int}
                
                @param sample_type: The value of sample_type
                @type sample_type: C{int}
                
                @param sample_rate: The value of sample_rate
                @type sample_rate: C{int}
        
                """
        super(PacketCopy, self).__init__(self._internal_action_types.COPY)
        self.remote_service_node = remote_service_node
        self.app_id = app_id
        self.local_id = local_id
        self.size = size
        self.sample_type = sample_type
        self.sample_rate = sample_rate
        self.log = logging.getLogger(__name__)



    def __eq__(self, obj):
        if obj == None:
            return False
        if not isinstance(obj, type(self)):
            return False
        if self is obj:
            return True
        return self.remote_service_node == obj.remoteServiceNode and self.app_id == obj.app_id and self.local_id == obj.local_id and self.size == obj.size and self.sample_type == obj.sample_type and self.sample_rate == obj.sample_rate



    def _to_idl(self):
        idl = ActionIDL(0, 0, 0, 0, 0)
        idl.actionType = self.action_type
        idl.pktCopyAction = ActionPktCopyIDL(self.remote_service_node, self.app_id, self.local_id, self.size, self.sample_type, self.sample_rate)
        idl.opCode = self.op_code
        return idl



    @classmethod
    def _from_idl(cls, idl):
        if idl == None:
            return 
        aobj = PacketCopy(idl.pktCopyAction.remoteSn, idl.pktCopyAction.app_id, idl.pktCopyAction.local_id, idl.pktCopyAction.size, idl.pktCopyAction.sampleType, idl.pktCopyAction.sampleRate)
        aobj.handle = idl.actionHandle
        return aobj




class PacketDivert(Action):
    """
    Action to copy packet to an application. This will divert packets 
    to the onePK application. A local ID may be specified 
    that is attached to the packets delivered to the onePK application.
    
    """


    def __init__(self, remote_service_node, app_id, local_id):
        """
                @param remote_service_node: The value of remote_service_node
                @type remote_service_node: C{int}
                
                @param app_id: The onePK application ID.
                @type app_id: C{int}
                
                @param local_id: The local_id
                @type local_id: C{int}
        
                """
        super(PacketDivert, self).__init__(self._internal_action_types.DIVERT)
        self.remote_service_node = remote_service_node
        self.app_id = app_id
        self.local_id = local_id



    def __eq__(self, obj):
        if obj == None:
            return False
        if not isinstance(obj, type(self)):
            return False
        if self is obj:
            return True
        return self.remote_service_node == obj.remoteServiceNode and self.app_id == obj.app_id and self.local_id == obj.local_id



    def _to_idl(self):
        idl = ActionIDL(0, 0, 0, 0, 0)
        idl.actionType = self.action_type
        idl.pktCopyAction = ActionPktDivertIDL(self.remote_service_node, self.app_id, self.local_id)
        idl.opCode = self.op_code
        return idl



    @classmethod
    def _from_idl(cls, idl):
        if idl == None:
            return 
        aobj = PacketDivert(idl.pktDivertAction.remoteSn, idl.pktDivertAction.app_id, idl.pktDivertAction.local_id)
        aobj.handle = idl.actionHandle
        return aobj




class VLAN(Action):
    """
        Action to set the top most VLAN ID. If no VLAN exists, push it and set it.
        
        ActionType.SET_VLAN_ID
        ActionType.POP_VLAN_ID
    
        ***DEPRICATED***
        VLANActionType is depricated.
        Please use action.ActionType
        ****************
    
        """

    VLANActionType = enum(SET=ActionType.SET_VLAN_ID, POP=ActionType.POP_VLAN_ID)
    _external_map = {2: ActionType.SET_VLAN_ID,
     3: ActionType.POP_VLAN_ID,
     4: ActionType.PUSH_VLAN_ID,
     ActionType.SET_VLAN_ID: 2,
     ActionType.POP_VLAN_ID: 3,
     ActionType.PUSH_VLAN_ID: 4}

    def __init__(self, type, vlan):
        """
                @param type: ActionType of VLAN
                @type type: L{ActionType<onep.policyservice.action.ActionType>}
                 
                @param vlan: VLAN ID.
                @type type: C{int}
        
                """
        if not ActionType._is_valid(type) or type not in self._external_map.keys():
            raise OnepIllegalArgumentException('invalid vlan action type')
        super(VLAN, self).__init__(self._internal_action_types.VLAN)
        self._external_type = type
        self._vlan = vlan
        self._vlan_action_type = self._external_map[type]



    def __eq__(self, obj):
        if obj == None:
            return False
        if not isinstance(obj, type(self)):
            return False
        if self is obj:
            return True
        return self._vlan_action_type == obj._vlan_action_type and self._vlan == obj.vlan



    def _to_idl(self):
        idl = ActionIDL(0, 0, 0, 0, 0)
        idl.actionType = self.action_type
        idl.vlanAction = ActionVlanIDL(self._vlan_action_type, self._vlan)
        idl.opCode = self.op_code
        return idl



    @classmethod
    def _from_idl(cls, idl):
        if idl == None:
            return 
        aobj = VLAN(self._external_map[idl.vlanAction.type], idl.vlanAction.vlan)
        aobj.handle = idl.actionHandle
        return aobj




class IpProtocol(Action):
    """
        Set IP protocol field in L3 header
        http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml
    
        """


    def __init__(self, protocol):
        """
                @param protocol: IP protocol field in L3 header
                @type protocol: C{int}
        
                """
        if not isinstance(protocol, int) or protocol < 0 or protocol > 255:
            raise OnepIllegalArgumentException('protocol ' + str(protocol))
        super(IpProtocol, self).__init__(self._internal_action_types.PROTOCOL)
        self._external_type = ActionType.SET_IP_PROTOCOL
        self.protocol = protocol



    def _to_idl(self):
        idl = ActionIDL(0, 0, 0, 0, 0)
        idl.actionType = self.action_type
        idl.protocolAction = ActionProtocolIDL(0, self.protocol)
        return idl



    def _from_idl(self, idl):
        return IpProtocol(idl.protocol)



    def __eq__(self, obj):
        if not isinstance(obj, IpProtocol):
            return False
        return self.protocol == obj.protocol



    def __str__(self):
        return '\n            Action %s\n            --------------------\n            Protocol  %d\n            ' % (ActionType.enumval(self._external_type), self.protocol)




class IpAddress(Action):
    """
        Set source or destination IP Address field in L3 header
    
        """


    def __init__(self, address, prefix_length, type):
        """
                @param address: IP Address 'AAA.BBB.CCC.DDD'
                @type address: C{string}
        
                @param prefix_length: Prefix length (subnet mask)
                @param prefix_length: C{int}
        
                @param type:  ActionType  SET_SRC_IP or SET_DST_IP
                @type type: L{action.ActionType}
        
                """
        if HostIpCheck(address).is_ipv4():
            self.family = OnepConstants.OnepAddressFamilyType.ONEP_AF_INET
            if not isinstance(prefix_length, int) or prefix_length < 0 or prefix_length > 32:
                raise OnepIllegalArgumentException('Invalid prefix length ' + str(prefix_length))
        elif HostIpCheck(address).is_ipv6():
            raise OnepNotSupportedException('Set IPv6 action not supported')
            self.family = OnepConstants.OnepAddressFamilyType.ONEP_AF_INET6
            if not isinstance(prefix_length, int) or prefix_length < 0 or prefix_length > 128:
                raise OnepIllegalArgumentException('Invalid prefix length ' + str(prefix_length))
        else:
            raise OnepIllegalArgumentException('Invalid IP address ' + str(address))
        self.direction = None
        if type == ActionType.SET_SRC_IP:
            self.direction = Direction.SOURCE
        elif type == ActionType.SET_DST_IP:
            self.direction = Direction.DESTINATION
        else:
            raise OnepIllegalArgumentException('Invalid action type ' + ActionType.enumval(type))
        super(IpAddress, self).__init__(self._internal_action_types.IP_ADDRESS)
        self._external_type = type
        self.address = address
        self.prefix_length = prefix_length



    def _convert_ipv4_address_to_byte_array(self, address):
        addr = array('b', address)
        addr.append(0)
        return addr



    def _convert_byte_array_to_ip_address(self, address):
        addr_str = ''
        for n in address:
            addr_str += str(n) + '.'

        return addr_str.rstrip('.')



    def _to_idl(self):
        idl = ActionIDL(0, 0, 0, 0, 0)
        idl.actionType = self.action_type
        idl.ipAddressAction = ActionIpAddressIDL(0, self.direction, 0, self.family, self._convert_ipv4_address_to_byte_array(self.address), self.prefix_length)
        idl.opCode = self.op_code
        return idl



    def _from_idl(self, idl):
        return IpAddress(self._convert_byte_array_to_ip_address(idl.addr), idl.prefixLen, idl.family)



    def __eq__(self, obj):
        if not isinstance(obj, IpAddress):
            return False
        return self.address == obj.address and self.family == obj.family and self.prefix_length == obj.prefix_length and self.direction == obj.direction



    def __str__(self):
        return '\n            Action %s\n            --------------------\n            %s/%d\n            ' % (ActionType.enumval(self._external_type), self.address, self.prefix_length)




class Port(Action):
    """
        Set port field in L4 header
    
        Pass in an IP protocol to signify which protocol
        the port belongs to.
    
        Supported protocols:
        --------------------
        TCP
        UDP
        SCTP
    
        """


    def __init__(self, port, direction, protocol):
        """
                @param port: L4 port to set
                @type port: C{short}
        
                @param direction: Direction enum
                @type direction: L{action.Direction}
        
                @param protocol: IP protocol number
                @type protocol: C{int}
        
                """
        if port < 0 or port > 65535:
            raise OnepIllegalArgumentException('0 - 0xFFFF', str(port))
        if not Direction._is_valid(direction):
            raise OnepIllegalArgumentException('Invalid direction')
        if not self._protocol_type_map.has_key((direction, protocol)):
            raise OnepIllegalArgumentException('Protocol ' + str(protocol) + ' ' + str(direction) + ' not supported')
        super(Port, self).__init__(self._internal_action_types.TCP_PORT)
        self.direction = direction
        self._external_type = self._protocol_type_map[direction, protocol]
        self.dependent_action = IpProtocol(protocol)
        self.port = port


    TCP = 6
    UDP = 17
    SCTP = 132
    _protocol_type_map = {(Direction.SOURCE, UDP): ActionType.SET_SRC_UDP_PORT,
     (Direction.SOURCE, TCP): ActionType.SET_SRC_TCP_PORT,
     (Direction.SOURCE, SCTP): ActionType.SET_SRC_SCTP_PORT,
     (Direction.DESTINATION, UDP): ActionType.SET_SRC_UDP_PORT,
     (Direction.DESTINATION, TCP): ActionType.SET_SRC_TCP_PORT,
     (Direction.DESTINATION, SCTP): ActionType.SET_SRC_SCTP_PORT}

    def _to_idl(self):
        idl = ActionIDL(0, 0, 0, 0, 0)
        idl.actionType = self.action_type
        idl.tcpPortAction = ActionTcpPortIDL(0, self.direction, 1, self.port, 0)
        idl.opCode = self.op_code
        return idl



    def _from_idl(self, idl):
        pass



    def __eq__(self, obj):
        if not isinstance(obj, Port):
            return False
        if self.dependent_action != obj.dependent_action:
            return False
        return self.port == obj.port and self.direction == obj.direction



    def __str__(self):
        return '\n            Action %s\n            --------------------\n            Port      %d\n            Direction %s\n\n            Dependency Action\n            -----------------\n            %s\n            ' % (ActionType.enumval(self._external_type),
         self.port,
         Direction.enumval(self.direction),
         str(self.dependent_action))




class MACAddress(Action):
    """
    Action to set to source or destination MAC address.
    
    @undocumented: src_dst
    """

    _external_map = {Direction.SOURCE: ActionType.SET_SRC_MAC,
     Direction.DESTINATION: ActionType.SET_DST_MAC,
     ActionType.SET_SRC_MAC: Direction.SOURCE,
     ActionType.SET_DST_MAC: Direction.DESTINATION}

    def __init__(self, src_dst, mac_addr):
        """
                @param mac_addr: MAC address.
                @type mac_addr: C{list}
                 
                @param src_dst: Either the source or destination address.
                @type src_dst: C{str} 
        
                """
        if not Direction._is_valid(src_dst):
            raise OnepIllegalArgumentException('direction is invalid')
        _validate_mac_address(mac_addr)
        super(MACAddress, self).__init__(self._internal_action_types.MAC_ADDRESS)
        self._external_type = self._external_map[src_dst]
        self.src_dst = src_dst
        self.mac_addr = [ c_byte(mac).value for mac in mac_addr ]
        self.log = logging.getLogger(__name__)



    def __eq__(self, obj):
        if obj == None:
            return False
        if not isinstance(obj, type(self)):
            return False
        if self is obj:
            return True
        return self.mac_addr == obj.mac_addr and self.src_dst == obj.src_dst



    def _to_idl(self):
        idl = ActionIDL(0, 0, 0, 0, 0)
        idl.actionType = self.action_type
        idl.macAction = ActionMacAddressIDL(self.src_dst, self.mac_addr)
        idl.opCode = self.op_code
        return idl



    @classmethod
    def _from_idl(cls, idl):
        if idl == None:
            return 
        aobj = MACAddress(idl.macAction.type, idl.macAction.addr)
        aobj.handle = idl.actionHandle
        return aobj




class Drop(Action):
    """
        Action to drop packets
    
        """


    def __init__(self):
        super(Drop, self).__init__(self._internal_action_types.DROP)



    def _to_idl(self):
        idl = ActionIDL(0, 0, 0, 0, 0)
        idl.actionType = self.action_type
        idl.nhAction = ActionNextHopIDL(0, [0])
        idl.opCode = self.op_code
        return idl




class NextHop(Action):
    """
    Action to set next hop.
    
    @undocumented: inet_addr
    """


    def __init__(self, inet_addr):
        """
                @param inet_addr: Network Address for the next hop.
                @type inet_addr: C{str}
        
                """
        self.log = logging.getLogger(__name__)
        h = HostIpCheck(inet_addr)
        if h.is_ipaddress():
            super(NextHop, self).__init__(self._internal_action_types.NEXT_HOP)
            self.inet_addr = inet_addr
            if h.is_ipv4():
                self.family = OnepConstants.OnepAddressFamilyType.ONEP_AF_INET
            elif h.is_ipv6():
                self.family = OnepConstants.OnepAddressFamilyType.ONEP_AF_INET6
        else:
            raise OnepIllegalArgumentException('Invalid address passed to constructor of NextHop')



    def __eq__(self, obj):
        if obj == None:
            return False
        if not isinstance(obj, type(self)):
            return False
        if self is obj:
            return True
        return self.family == obj.family and self.inet_addr == obj.inet_addr



    def _to_idl(self):
        idl = ActionIDL(0, 0, 0, 0, 0)
        idl.actionType = self.action_type
        byte_array = array('B', self.inet_addr)
        byte_array.append(0)
        idl.nhAction = ActionNextHopIDL(self.family, byte_array)
        idl.opCode = self.op_code
        return idl



    @classmethod
    def _from_idl(cls, idl):
        if idl == None:
            return 
        arr = idl.nhAction.addr
        inet_addr = ''
        for l in arr:
            if l == 0:
                break
            inet_addr += str(unichr(l))

        aobj = NextHop(inet_addr)
        aobj.handle = idl.actionHandle
        return aobj




class ForwardClass(Action):
    """
        Forward packets to Class
    
        """


    def __init__(self, class_id):
        """
                @param class_id: Class ID
                @type class_id: C{int}
        
                """
        self.class_id = class_id
        super(ForwardClass, self).__init__(self._internal_action_types.FWD_CLASS_ID)



    def _to_idl(self):
        idl = ActionIDL(0, 0, 0, 0, 0)
        idl.actionType = self.action_type
        idl.fwdClassIdAction = ActionFwdClassIdIDL(self.class_id)
        idl.opCode = self.op_code
        return idl



    @classmethod
    def _from_idl(cls, idl):
        if not idl:
            return None
        aobj = ForwardClass(idl.fwdClassIdAction)
        aobj.handle = idl.actionHandle
        return aobj




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:22:53 IST
