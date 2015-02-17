# 2015.02.05 17:18:27 IST
from onep.core.event.EventFilter import EventFilter
from onep.core.exception.OnepIllegalArgumentException import OnepIllegalArgumentException
from onep.core.util.OnepConstants import OnepConstants
from onep.core.util.Period import Period
from onep.core.util.Enum import enum
from onep.interfaces.InterfaceStatistics import InterfaceStatistics

class InterfaceStatisticsFilter(EventFilter):
    """
    The InterfaceStatistics Filter represents the specifications needed to
    monitor for an interface statistics event on a given Network Interface.
    
    Comparison value is specified in the filter which will be compared against
    the actual value of the parameter at poll intervals.
    
    When poll_interval expires, the monitor compares the interface
    parameter value against the specified entry value in this filter. If poll_interval 
    is not specified, default value for monitor interval is 300 seconds.
    
    Comparison operations can be specified using L{OnepOperatorType<onep.core.util.OnepConstants.OnepConstants.OnepOperatorType>}.
    
    Comparison value can be qualified by means of L{InterfaceStatisticsType<onep.interfaces.InterfaceStatisticsFilter.InterfaceStatisticsFilter.InterfaceStatisticsType>} 
    indicating how the value field should be interpreted. i.e. absolute value or rate of increase or
    incremental increase/decrease since last event.
    
    Events will start occurring when the criteria is met. Such criteria is
    considered as entry criteria. 
    After the entry criteria is met, at each poll interval the event will keep
    triggering unless the entry criteria no longer qualifies.
    Eg. Send event if tx_load utilization is more than 50 and keep sending events
    until it drops below this threshold every minute.
    
    However, in some cases like bursts, where the utilization may spike
    momentarily, admin may need notification when the threshold is crossed and no
    event until the normal level is reached. This would avoid event noise as well
    as identify each spike separately This can be achieved by means of exit
    criteria.
    
    Exit criteria can optionally be specified. If specified once entry criteria
    is met, event monitoring will stop until the exit criteria is satisfied. 
    Once exit criteria is met, it re-arms the event monitor i.e. after exit
    criteria is met, the monitor will now compare against entry criteria until
    entry criteria is met and when it does event is sent. And the cycle will
    continue.
    
    Exit criteria can be combined with exit_time, which specifies the time
    interval after which the monitor will be re-armed.
    
    @see: L{add_statistics_listener<interfaces.NetworkInterface.NetworkInterface.add_statistics_listener>}    
    """

    InterfaceStatisticsType = enum('ONEP_INTERFACE_STATISTICS_TYPE_VALUE', 'ONEP_INTERFACE_STATISTICS_TYPE_INCREMENT', 'ONEP_INTERFACE_STATISTICS_TYPE_RATE')
    _parameter = InterfaceStatistics.InterfaceStatisticsParameter.ONEP_IF_STAT_RX_PKTS_ERRORS
    _poll_interval = Period(300, 0)
    _entry_value = 0
    _entry_op = OnepConstants.OnepOperatorType.ONEP_OP_NONE
    _exit_value = 0
    _exit_op = OnepConstants.OnepOperatorType.ONEP_OP_NONE
    _exit_combination = OnepConstants.OnepCombinationType.ONEP_COMBINATION_NONE
    _exit_time = Period(1, 0)
    _exit_event = False
    _average_factor = 0
    MAX_AVERAGEFACTOR = 64
    MIN_AVERAGEFACTOR = 1
    _exit_type = InterfaceStatisticsType.ONEP_INTERFACE_STATISTICS_TYPE_VALUE
    _entry_type = InterfaceStatisticsType.ONEP_INTERFACE_STATISTICS_TYPE_VALUE

    def _check_parameter(self, param_name, parameter, enum = None):
        if parameter == None:
            raise OnepIllegalArgumentException(param_name, 'None')
        if enum:
            if not enum._is_valid(parameter):
                raise OnepIllegalArgumentException(param_name, 'Invalid Value')



    def _get_parameter(self):
        return self._parameter



    def _set_parameter(self, parameter):
        self._check_parameter('parameter', parameter, InterfaceStatistics.InterfaceStatisticsParameter)
        self._parameter = parameter


    _doc = '\n    The parameter id set in this filter.\n    This is a mandatory property and must have a value. This is used to set the counter which \n    will be compared as part of interface statistics event monitoring.\n    \n    Raises: OnepIllegalArgumentException - if parameter is assigned None or invalid value\n    \n    @type:L{InterfaceStatisticsParameter<interfaces.InterfaceStatistics.InterfaceStatistics.InterfaceStatisticsParameter>}\n    '
    parameter = property(_get_parameter, _set_parameter, None, _doc)

    def _get_poll_interval(self):
        return self._poll_interval



    def _set_poll_interval(self, poll_inter):
        if poll_inter != None and isinstance(poll_inter, Period):
            self._poll_interval = poll_inter
            if poll_inter.sec < 1:
                self._poll_interval = Period(1, 0)
        else:
            raise OnepIllegalArgumentException('poll_inter', 'Invalid Value')


    _doc = '\n    The poll interval set in this filter.\n    Values are compared at poll interval to determine if event criteria is met. \n    The default is 300 seconds.\n    \n    The frequency used to collect the samples. The seconds parameter must be\n    a number between 1 and 4294967295 inclusive. The poll interval value \n    must not be less than 1 second.\n    If it is, the poll interval is set to 1 sec.\n    \n    \n    Raises: OnepIllegalArgumentException - if poll_intercal is assigned None or invalid value\n    \n    @type: L{Period<core.util.Period.Period >}   \n    '
    poll_interval = property(_get_poll_interval, _set_poll_interval, None, _doc)

    def _get_entry_value(self):
        return self._entry_value



    def _set_entry_value(self, entry_val):
        if entry_val != None and isinstance(entry_val, int):
            self._entry_value = entry_val
        else:
            raise OnepIllegalArgumentException('entry_val', 'Invalid Value')


    _doc = '\n    The entry comparison value set in this filter.\n    The entry comparison value is the value at which the event will be triggered.\n    \n    Raises: OnepIllegalArgumentException - When entry_op is assigned None or invalid value.\n    \n    @type: C{int}\n    '
    entry_value = property(_get_entry_value, _set_entry_value, None, _doc)

    def _get_entry_op(self):
        return self._entry_op



    def _set_entry_op(self, entryop):
        self._check_parameter('entry_op', entryop, OnepConstants.OnepOperatorType)
        self._entry_op = entryop


    _doc = '\n    The entry comparison operator type\n    \n    Raises: OnepIllegalArgumentException - if entry_op is assigned None or invalid value\n    \n    @type: L{OnepOperatorType<core.util.OnepConstants.OnepConstants.OnepOperatorType>}\n    '
    entry_op = property(_get_entry_op, _set_entry_op, None, _doc)

    def _get_entry_type(self):
        return self._entry_type



    def _set_entry_type(self, entry_type_val):
        self._check_parameter('entry_type', entry_type_val, self.InterfaceStatisticsType)
        self._entry_type = entry_type_val


    _doc = '\n    Entry value monitoring type.\n    Type of operation (semantics) to be used in event monitor criteria.\n    Specifies a type of operation used in checking against the entry value.\n    \n    Raises: OnepIllegalArgumentException - if entry_type is assigned None or invalid value\n    \n    @type: L{InterfaceStatisticsType<interfaces.InterfaceStatisticsFilter.InterfaceStatisticsFilter.InterfaceStatisticsType>}\n    '
    entry_type = property(_get_entry_type, _set_entry_type, None, _doc)

    def _get_exit_value(self):
        return self._exit_value



    def _set_exit_value(self, exit_val):
        if exit_val < 0 or exit_val == None or not isinstance(exit_val, int):
            raise OnepIllegalArgumentException('exit_value', 'is None or less than 0')
        self._exit_value = exit_val


    _doc = '\n    Exit comparison value set in this filter\n    The default value is zero\n    \n    Raises : OnepIllegalArgumentException - if exit_value is assigned None or invalid value\n    \n    @type: C{int}\n    '
    exit_value = property(_get_exit_value, _set_exit_value, None, _doc)

    def _get_exit_op(self):
        return self._exit_op



    def _set_exit_op(self, exitop):
        self._check_parameter('exit_op', exitop, OnepConstants.OnepOperatorType)
        self._exit_op = exitop


    _doc = '\n    Exit operator type\n    \n    Raises: OnepIllegalArgumentException - if exit_op is assigned None or invalid value\n    \n    @type: L{OnepOperatorType<onep.core.util.OnepConstants.OnepConstants.OnepOperatorType>}\n    '
    exit_op = property(_get_exit_op, _set_exit_op, None, _doc)

    def _get_exit_type(self):
        return self._exit_type



    def _set_exit_type(self, exittype):
        self._check_parameter('exit_type', exittype, self.InterfaceStatisticsType)
        self._exit_type = exittype


    _doc = '\n    Exit value monitoring type.\n    Type of operation (semantics) to be used in event monitor criteria.\n    Specifies a type of operation used in checking against the exit value.\n    \n    Raises: OnepIllegalArgumentException - if exit_type is assigned None or invalid value\n    \n    @type: L{InterfaceStatisticsType<interfaces.InterfaceStatisticsFilter.InterfaceStatisticsFilter.InterfaceStatisticsType>} \n    '
    exit_type = property(_get_exit_type, _set_exit_type, None, _doc)

    def _get_exit_combination(self):
        return self._exit_combination



    def _set_exit_combination(self, exitcombination):
        self._check_parameter('exit_combination', exitcombination, OnepConstants.OnepCombinationType)
        self._exit_combination = exitcombination


    _doc = '\n    Exit combination type.\n    \n    This property is used to indicate the combination of exit condition tests required to\n    re-arm the event trigger; if the and operator is specified, both exit\n    value and exit time tests must be true to cause re-arm; if the or\n    operator is specified, either exit value or exit time tests can be true\n    to cause event monitoring to be rearmed.\n    \n    Raises: OnepIllegalArgumentException - if exit_combination is assigned None or invalid value\n    \n    @type: L{OnepCombinationType<onep.core.util.OnepConstants.OnepConstants.OnepCombinationType>}\n    '
    exit_combination = property(_get_exit_combination, _set_exit_combination, None, _doc)

    def _get_exit_time(self):
        return self._exit_time



    def _set_exit_time(self, exittime):
        if exittime != None and isinstance(exittime, Period):
            self._exit_time = exittime
        else:
            raise OnepIllegalArgumentException('exit_time', 'Invalid Value')


    _doc = '\n    Exit criteria time period set in this filter.\n    \n    Raises: OnepIllegalArgumentException - if exit_time is assigned None or invalid value.\n    \n    @type: L{Period<onep.core.util.Period.Period>}\n    '
    exit_time = property(_get_exit_time, _set_exit_time, None, _doc)

    def _get_exit_event(self):
        return self._exit_event



    def _set_exit_event(self, exitEvent):
        if exitEvent != None and isinstance(exitEvent, bool):
            self._exit_event = exitEvent
        else:
            raise OnepIllegalArgumentException('exit_event should be of type bool')


    _doc = '\n    Indicates if exit event is set.Indicates if an event should be triggered when exit criteria is met.\n    \n    TRUE: event starts occurring when exit criteria met.\n    \n    FALSE: event stops occurring when exit criteria is met\n    \n    Raises: OnepIllegalArgumentException - if exit_event is assigned None or invalid value.\n    \n    @type: C{bool}\n    '
    exit_event = property(_get_exit_event, _set_exit_event, None, _doc)

    def _get_average_factor(self):
        return self._average_factor



    def _set_average_factor(self, averagefactor):
        if averagefactor == None or averagefactor < self.MIN_AVERAGEFACTOR or averagefactor > self.MAX_AVERAGEFACTOR:
            raise OnepIllegalArgumentException('averageFactor', str(averagefactor) + ' ')
        self._average_factor = averagefactor


    _doc = '\n    The average factor for rate based calculations.\n    \n    Number in the range from 1 to 64 used to calculate the period used for\n    rate-based calculations (InterfaceStatisticsType.ONEP_INTERFACE_STATISTICS_RATE). \n    The average-factor value is multiplied by the poll_interval value to derive the \n    period in milliseconds. The minimum average factor value is 1.\n    \n    Raises: OnepIllegalArgumentException - when average_factor outside valid range of 1 to 64\n    \n    @type: C{int}\n    '
    average_factor = property(_get_average_factor, _set_average_factor, None, _doc)

    def _is_exit_value_set(self):
        if self._exit_time.msec == 0 and self._exit_time.sec == 0 and self._exit_op == OnepConstants.OnepOperatorType.ONEP_OP_NONE:
            return False
        return True


    _doc = '\n    Determines if exit criteria is set\n    @type: C{bool}\n    '
    is_exit_value_set = property(_is_exit_value_set, None, None, _doc)

    def __init__(self, parameter, entryop, entryvalue, entrytype):
        """ 
                Constructor for Interface Statistics All the other conditions than
                following input parameters are set to appropriate default values. Poll
                interval is set to 300 seconds.
        
                Default filter settings depict scenario where parameter value will be
                checked against entryValue and if qualifies the specified operator
                comparison event will be generated.
                 
                @param parameter: Value defined in InterfaceStatisticsParameter.
                @type parameter:  L{InterfaceStatisticsParameter<interfaces.InterfaceStatistics.InterfaceStatistics.InterfaceStatisticsParameter>} 
                @param entryop: Value defined in OnepOperatorType.
                @type entryop: L{OnepOperatorType<onep.core.util.OnepConstants.OnepConstants.OnepOperatorType>}
                @param entryvalue: The value of parameter at which the listener should be activated.
                @type entryvalue: C{int} 
                @param entrytype: It can be any type defined in InterfaceStatisticsType.
                @type entrytype: L{InterfaceStatisticsType<interfaces.InterfaceStatisticsFilter.InterfaceStatisticsFilter.InterfaceStatisticsType>}
                
                @raise OnepIllegalArgumentException : This exception is thrown if input parameter is not specified or if 
                        it is not of correct type.
                
                """
        super(InterfaceStatisticsFilter, self).__init__()
        self.parameter = parameter
        self.poll_interval.set_sec(300)
        self.poll_interval.set_msec(0)
        self.entry_value = entryvalue
        self.entry_op = entryop
        self.entry_type = entrytype
        self.exit_value = 0
        self.exit_op = OnepConstants.OnepOperatorType.ONEP_OP_NONE
        self.exit_type = self.InterfaceStatisticsType.ONEP_INTERFACE_STATISTICS_TYPE_VALUE
        self.exit_combination = OnepConstants.OnepCombinationType.ONEP_COMBINATION_NONE
        self.exit_time.set_sec(0)
        self.exit_time.set_msec(0)
        self.exit_event = False
        self._average_factor = 0




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:18:27 IST
