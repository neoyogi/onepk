# 2015.02.05 17:18:25 IST
from onep.core.exception import OnepException, OnepIllegalArgumentException, OnepNotSupportedException
from onep.core.util import enum, OnepStatus
from Shared.ttypes import ExceptionIDL

class InterfaceStatistics(object):
    """ 
    This class represents the Interface Statistics properties of the network interface.
    
    The interface statistics are dynamic software properties, such as number of
    packets in, number of errors, and number of out packets. These properties
    must always be received on demand from the Network Element, because they are
    constantly changing.
    
    The interface statistics can be obtained via two methods: 
        
        1. Using the NetworkInterface.get_statistics() method to
           get an InterfaceStatistics instance.
        
        2. Using the NetworkInterface.add_interface_statistics_listener() method 
           to register a statistics event listener.
        
    The get_statistics() API only gets a snapshot of the interface statistics on
    each invocation. Thus, an application that requires periodic updates of the
    statistics must use this API in a loop.
    
    The preferred way of retrieving the interface statistics is to use the
    add_interface_statistics_listener() method, and register for periodically
    receiving the interface statistics when the filter criteria (specified through
    InterfaceStatisticsFilter) are met.
    
    This class contains various property attributes corresponding to the
    statistics contained in the snapshot. The application must call
    get_statistics() on the NetworkInterface whenever it requires
    the latest updated values.
    
    @undocumented: __init__
    @undocumented: __str__
    @undocumented: tail_drops
    @undocumented: voq_drops
    @undocumented: replication_engine_drops
    @undocumented: get_param
    """

    InterfaceStatisticsParameter = enum('ONEP_IF_STAT_RELIABILITY', 'ONEP_IF_STAT_RESETS', 'ONEP_IF_STAT_RX_LOAD', 'ONEP_IF_STAT_RX_BYTES_PER_SEC', 'ONEP_IF_STAT_RX_PKTS_PER_SEC', 'ONEP_IF_STAT_RX_BYTES', 'ONEP_IF_STAT_RX_PKTS_UCAST', 'ONEP_IF_STAT_RX_PKTS_MCAST', 'ONEP_IF_STAT_RX_PKTS_BCAST', 'ONEP_IF_STAT_IN_PKTS_DROP', 'ONEP_IF_STAT_RX_PKTS_ERRORS', 'ONEP_IF_STAT_IN_PKTS_UNKNOWN', 'ONEP_IF_STAT_RX_PKTS_RUNTS', 'ONEP_IF_STAT_RX_PKTS_GIANTS', 'ONEP_IF_STAT_RX_PKTS_THROTTLE', 'ONEP_IF_STAT_RX_PKTS_CRC', 'ONEP_IF_STAT_RX_PKTS_FRAME', 'ONEP_IF_STAT_RX_PKTS_OVERRUN', 'ONEP_IF_STAT_TX_LOAD', 'ONEP_IF_STAT_TX_BYTES_PER_SEC', 'ONEP_IF_STAT_TX_PKTS_PER_SEC', 'ONEP_IF_STAT_TX_BYTES', 'ONEP_IF_STAT_TX_PKTS_UCAST', 'ONEP_IF_STAT_TX_PKTS_MCAST', 'ONEP_IF_STAT_TX_PKTS_BCAST', 'ONEP_IF_STAT_OUT_PKTS_DROP', 'ONEP_IF_STAT_TX_PKTS_ERRORS', 'ONEP_IF_STAT_TX_PKTS_UNDERRUN', 'ONEP_IF_STAT_TX_PKTS_BUFFER_FAILURES', 'ONEP_IF_STAT_TX_PKTS_BUFFER_SWAPPEDOUT', 'ONEP_IF_STAT_TX_PKTS_TAIL_DROPS', 'ONEP_IF_STAT_TX_PKTS_VOQ_DROPS', 'ONEP_IF_STAT_TX_PKTS_REP_ENG_DROP', 'ONEP_IF_STAT_RX_PKTS', 'ONEP_IF_STAT_TX_PKTS')

    def __init__(self, stats_list):
        self.stats_list = stats_list



    @property
    def reliability(self):
        """The reliability of the associated interface.
        
                The value returned is from 1 to 255, and is calculated as an
                exponential average over 5 minutes.  A value of 255/255 means
                the interface is 100 percent reliable.
        
                @return: The reliability.
                @rtype: C{int}
                """
        return self.get_param(self.InterfaceStatisticsParameter.ONEP_IF_STAT_RELIABILITY)



    @property
    def transmit_load(self):
        """The transmit load on the associated interface.
        
                The transmit load returned is a fraction of 255 (255/255 is
                completely saturated), calculated as an exponential average over
                5 minutes.
        
                @return: The transmit load.
                @rtype: C{int}
                """
        return self.get_param(self.InterfaceStatisticsParameter.ONEP_IF_STAT_TX_LOAD)



    @property
    def transmit_rate_pps(self):
        """The number of packets transmitted in packets per second (PPS)
                on the associated interface.
        
                The returned value is the average number of packets transmitted
                per second over the load interval time, which is 300 seconds
                (5 minutes).  The number is an approximation of the rate per
                second.
        
                @return: The transmit rate PPS.
                @rtype: C{int}
                """
        return self.get_param(self.InterfaceStatisticsParameter.ONEP_IF_STAT_TX_PKTS_PER_SEC)



    @property
    def transmit_rate_bps(self):
        """The number of packets transmitted in bits per second (BPS)
                on the associated interface.
        
                The returned value is the average number of bits transmitted per
                second over the load interval time, which is 300 seconds
                (5 minutes). The number is an approximation of the rate per
                second.
        
                @return: The transmit rate BPS.
                @rtype: C{int}
                """
        return self.get_param(self.InterfaceStatisticsParameter.ONEP_IF_STAT_TX_BYTES_PER_SEC)



    @property
    def receive_rate_pps(self):
        """The number of packets received in packets per second (PPS)
                on the associated interface.
        
                The returned value is the average number of packets received per
                second over the load interval time, which is 300 seconds
                (5 minutes). The number is an approximation of the rate per
                second.
        
                @return: The receive rate PPS.
                @rtype: C{int}
                """
        return self.get_param(self.InterfaceStatisticsParameter.ONEP_IF_STAT_RX_PKTS_PER_SEC)



    @property
    def receive_rate_bps(self):
        """The number of packets received in bits per second (BPS)
                on the associated interface.
        
                The returned value is the average number of bits received per
                second over the load interval time, which is 300 seconds
                (5 minutes).  The number is an approximation of the rate per
                second.
        
                @return: The receive rate BPS.
                @rtype: C{int}
                """
        return self.get_param(self.InterfaceStatisticsParameter.ONEP_IF_STAT_RX_BYTES_PER_SEC)



    @property
    def transmit_rate_cum_byte(self):
        """The cumulative number of bytes transmitted from the
                associated interface since the last bootup.
        
                @return: The cumulative number of bytes transmitted.
                @rtype: C{int}
                """
        return self.get_param(self.InterfaceStatisticsParameter.ONEP_IF_STAT_TX_BYTES)



    @property
    def receive_rate_cum_byte(self):
        """The cumulative number of bytes received on the associated
                interface since the last bootup.
        
                @return: The cumulative number of bytes received.
                @rtype: C{int}
                """
        return self.get_param(self.InterfaceStatisticsParameter.ONEP_IF_STAT_RX_BYTES)



    @property
    def receive_load(self):
        """The receive load on the associated interface.
        
                The receive load returned is a fraction of 255 (255/255 is
                completely saturated) calculated as an exponential average over
                5 minutes.
        
                @return: The receive load.
                @rtype: C{int}
                """
        return self.get_param(self.InterfaceStatisticsParameter.ONEP_IF_STAT_RX_LOAD)



    @property
    def receive_broadcast(self):
        """The number of broadcast packets received on the associated
                interface.
        
                @return: The number of broadcast packets received.
                @rtype: C{int}
                """
        return self.get_param(self.InterfaceStatisticsParameter.ONEP_IF_STAT_RX_PKTS_BCAST)



    @property
    def receive_multicast(self):
        """The number of multicast packets received on the associated
                interface.
        
                @return: The number of multicast packets received.
                @rtype: C{int}
                """
        return self.get_param(self.InterfaceStatisticsParameter.ONEP_IF_STAT_RX_PKTS_MCAST)



    @property
    def receive_unicast(self):
        """The number of unicast packets received on the associated
                interface.
        
                @return: The number of unicast packets received.
                @rtype: C{int}
                """
        return self.get_param(self.InterfaceStatisticsParameter.ONEP_IF_STAT_RX_PKTS_UCAST)



    @property
    def transmit_broadcast(self):
        """The number of broadcast packets transmitted on the associated
                interface.
        
                @return: The number broadcast packets transmitted.
                @rtype: C{int}
                """
        return self.get_param(self.InterfaceStatisticsParameter.ONEP_IF_STAT_TX_PKTS_BCAST)



    @property
    def transmit_multicast(self):
        """The number of multicast packets transmitted on the associated
                interface.
        
                @return: The number multicast packets transmitted.
                @rtype: C{int}
                """
        return self.get_param(self.InterfaceStatisticsParameter.ONEP_IF_STAT_TX_PKTS_MCAST)



    @property
    def transmit_unicast(self):
        """The number of unicast packets transmitted on the associated
                interface.
        
                @return: The number unicast packets transmitted.
                @rtype: C{int}
                """
        return self.get_param(self.InterfaceStatisticsParameter.ONEP_IF_STAT_TX_PKTS_UCAST)



    @property
    def receive_runt(self):
        """The number of runt packets received on the associated
                interface.
        
                The runt packets correspond to packets discarded because they
                are smaller in length than the physical medium minimum packet
                size.  For example, any Ethernet packet that is less than 64
                bytes in length is considered a runt.
        
                @return: The number of runt packets received.
                @rtype: C{int}
                """
        return self.get_param(self.InterfaceStatisticsParameter.ONEP_IF_STAT_RX_PKTS_RUNTS)



    @property
    def receive_giant(self):
        """The number of giant packets received on the asssociated
                interface.
        
                The giant packets correspond to packets discarded because they
                exceed the physical medium's maximum packet size.  For example,
                any Ethernet packet that is greater than 1518 bytes in length is
                considered a giant.
        
                @return: The number of giant packets received.
                @rtype: C{int}
                """
        return self.get_param(self.InterfaceStatisticsParameter.ONEP_IF_STAT_RX_PKTS_GIANTS)



    @property
    def receive_throttle(self):
        """The number of throttle packets received on the associated
                interface.
        
                The returned value indicates the number of times the input
                buffers of an interface were cleaned because they were not
                serviced fast enough or because they were overwhelmed.  Typically, an
                explorer storm can cause the throttles counter to increment.
                Note that all packets in the input queue are dropped every
                time there is a throttle, which causes very slow performance and
                may also disrupt existing sessions.
        
                @return: The number of throttle packets received.
                @rtype: C{int}
                """
        return self.get_param(self.InterfaceStatisticsParameter.ONEP_IF_STAT_RX_PKTS_THROTTLE)



    @property
    def in_unknown_protocol_drop(self):
        """The number of unknown protocol messages received on the
                associated interface.
        
                @return: The number of unknown protocol messages received.
                @rtype: C{int}
                """
        return self.get_param(self.InterfaceStatisticsParameter.ONEP_IF_STAT_IN_PKTS_UNKNOWN)



    @property
    def in_packet_drop(self):
        """The number of input packets dropped on the associated
                interface because the maximum queue size was exceeded.
        
                @return: The number of input packets dropped.
                @rtype: C{int}
                """
        return self.get_param(self.InterfaceStatisticsParameter.ONEP_IF_STAT_IN_PKTS_DROP)



    @property
    def in_error(self):
        """Get the number of errors received on the associated
                interface.
        
                The returned value includes runts, giants, no buffer, cyclic
                redundancy check (CRC), frame, overrun, and ignored counts.
                Other input related errors can also cause the input errors count
                to be increased.  Some datagrams may have more than one error;
                the error count may not balance with the sum of the
                enumerated errors, because some datagrams may have more than one
                error and others may have errors that do not fall into any of
                the specific categories.
        
                @return: The number of errors received.
                @rtype: C{int}
                """
        return self.get_param(self.InterfaceStatisticsParameter.ONEP_IF_STAT_RX_PKTS_ERRORS)



    @property
    def in_error_crc(self):
        """The the number of cyclic redundancy check (CRC) errors on the
                associated interface.
        
                The returned value corresponds to CRC-generated mismatches.
                CRC errors are also reported when a far-end abort occurs and
                when the idle flag pattern is corrupted.  The CRC errors can
                occur even when there is no data traffic.
        
                @return: The number of CRC errors received.
                @rtype: C{int}
                """
        return self.get_param(self.InterfaceStatisticsParameter.ONEP_IF_STAT_RX_PKTS_CRC)



    @property
    def in_error_frame(self):
        """The number of input frame errors received on the associated
                interface.
        
                The returned value corresponds to the number of times the
                receiver hardware was unable to hand received data to a
                hardware buffer, because the input rate exceeded the receiver's
                ability to handle the data.
        
                @return: The number of input frame errors received.
                @rtype: C{int}
                """
        return self.get_param(self.InterfaceStatisticsParameter.ONEP_IF_STAT_RX_PKTS_FRAME)



    @property
    def in_error_overrun(self):
        """The number of input buffer overrun errors on the associated
                interface.
        
                The returned value corresponds to the number of received
                packets ignored by the interface because the interface hardware
                ran low on internal buffers.
        
                @return: The number of input buffer overrun errors.
                @rtype: C{int}
                """
        return self.get_param(self.InterfaceStatisticsParameter.ONEP_IF_STAT_RX_PKTS_OVERRUN)



    @property
    def in_error_ignore(self):
        """The number of input errors that are ignored on the associated
                interface.
        
                @return: The number of input errors that are ignored.
                @rtype: C{int}
                """
        return self.get_param(self.InterfaceStatisticsParameter.ONEP_IF_STAT_RX_PKTS_ERRORS)



    @property
    def out_packet_drop(self):
        """The number of output packets dropped on the associated
                interface.
        
                The returned value corresponds to the sum of all errors that
                prevented the final transmission of datagrams out of the
                interface.  A common cause is a low Output Queue size.
        
                @return: The number of output packets dropped.
                @rtype: C{int}
                """
        return self.get_param(self.InterfaceStatisticsParameter.ONEP_IF_STAT_OUT_PKTS_DROP)



    @property
    def out_error(self):
        """The number of outgoing errors received on the associated
                interface.
        
                The returned value corresponds to the number of times that the
                far-end router's transmitter ran faster than the near-end
                router's receiver was able to handle.  This situation may never occur or
                be reported on some interfaces.
        
                @return: The number of outgoing errors received.
                @rtype: C{int}
                """
        return self.get_param(self.InterfaceStatisticsParameter.ONEP_IF_STAT_TX_PKTS_ERRORS)



    @property
    def out_error_underrun(self):
        """The number of output buffer underrun errors on the associated
                interface.
        
                @return: The number of output buffer underrun errors.
                @rtype: C{int}
                """
        return self.get_param(self.InterfaceStatisticsParameter.ONEP_IF_STAT_TX_PKTS_UNDERRUN)



    @property
    def out_error_reset(self):
        """The number of output error resets on the associated
                interface.
        
                @return: The number of output error resets.
                @rtype: C{int}
                """
        return self.get_param(self.InterfaceStatisticsParameter.ONEP_IF_STAT_RESETS)



    @property
    def out_buffer_fail(self):
        """The number of output buffer failures on the associated
                interface.
        
                @return: The number of output buffer failures.
                @rtype: C{int}
                """
        return self.get_param(self.InterfaceStatisticsParameter.ONEP_IF_STAT_TX_PKTS_BUFFER_FAILURES)



    @property
    def out_buffer_swap(self):
        """The number of output buffers that were swapped out to DRAM on
                the associated interface.
        
                @return: The number of output buffers that were swapped out.
                @rtype: C{int}
                """
        return self.get_param(self.InterfaceStatisticsParameter.ONEP_IF_STAT_TX_PKTS_BUFFER_SWAPPEDOUT)



    @property
    def transmit_cum_packet(self):
        """The cumulative number of packets transmitted from the
                associated interface since the last bootup.
        
                @return: The cumulative number of packets transmitted.
                @rtype: C{int}
                """
        return self.get_param(self.InterfaceStatisticsParameter.ONEP_IF_STAT_TX_PKTS)



    @property
    def receive_cum_packet(self):
        """The cumulative number of packets received by the associated
                interface since the last bootup.
        
                @return: The cumulative number of packets received.
                @rtype: C{int}
                """
        return self.get_param(self.InterfaceStatisticsParameter.ONEP_IF_STAT_RX_PKTS)



    def __str__(self):
        """Returns a string summary the InterfaceStatistics instance.
        
                @return: A string summary the InterfaceStatistics instance.
                @rtype: C{str}
                """
        sb = 'InterfaceStatistics:'
        for param in sorted([ self.InterfaceStatisticsParameter.toInteger(k) for k in self.InterfaceStatisticsParameter.keys() ]):
            try:
                if self.stats_list[param].retcode == OnepStatus.ONEP_OK:
                    sb += '\n\t' + self.InterfaceStatisticsParameter.enumval(param) + ':\t' + str(self.stats_list[param].stats)
            except:
                break

        return sb



    @property
    def tail_drops(self):
        """The number of tail drops on the associated interface.
        
                @return: The number of tail drops.
                @rtype: C{int}
                """
        return self.get_param(self.InterfaceStatisticsParameter.ONEP_IF_STAT_TX_PKTS_TAIL_DROPS)



    @property
    def voq_drops(self):
        """The number of VOQ drops on the associated interface.
        
                @return: The number of VOQ drops.
                @rtype: C{int}
                """
        return self.get_param(self.InterfaceStatisticsParameter.ONEP_IF_STAT_TX_PKTS_VOQ_DROPS)



    @property
    def replication_engine_drops(self):
        """The number of Replication Engine drops on the associated
                interface.
        
                @return: The number of Replication Engine drops.
                @rtype: C{int}
                """
        return self.get_param(self.InterfaceStatisticsParameter.ONEP_IF_STAT_TX_PKTS_REP_ENG_DROP)



    def get_param(self, parameter):
        """
        This function is used to retrieve the particular Interface Statistic.
        The Interface Statistic is specified by using L{InterfaceStatisticsParameter<interfaces.InterfaceStatistics.InterfaceStatistics.InterfaceStatisticsParameter>}
        
        @param parameter: The specific InterfaceStatistics parameter which is required.
        @type parameter: L{InterfaceStatisticsParameter<interfaces.InterfaceStatistics.InterfaceStatistics.InterfaceStatisticsParameter>}
        
        @return: The value of Interface Statistic
        @rtype: C{int}  
        """
        if not self.InterfaceStatisticsParameter._is_valid(parameter):
            raise OnepIllegalArgumentException(parameter, 'Invalid Value')
        try:
            param = self.stats_list[parameter]
        except IndexError:
            raise OnepNotSupportedException('%s is not supported.' % self.InterfaceStatisticsParameter.enumval(parameter))
        if param.retcode == OnepStatus.ONEP_OK:
            return param.stats
        raise OnepException('Error', ExceptionIDL(param.retcode))




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:18:25 IST
