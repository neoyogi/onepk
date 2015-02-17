# 2015.02.05 17:20:59 IST
from onep.core.util.Enum import enum
from onep.core.util.OnepStatus import OnepStatus

class OnepConstants(object):
    OK = 0
    FAIL = 1
    ONEP_PORT = 15001
    ONEP_TLS_PORT = 15002
    DEFAULT_QUEUE_SIZE = 100
    DEFAULT_N_THREADS = 1
    SESSION_RECONNECT_LIMIT = 300
    MAX_USERNAME_LEN = 64
    MAX_PASSWORD_LEN = 25
    UNKNOWN_STATE = 0
    DISCONNECTED_STATE = 1
    CONNECTING_STATE = 2
    CONNECTED_STATE = 3
    EVENT_TYPE_CONNECTION = 0
    EVENT_TYPE_APPLICATION = 1
    EVENT_TYPE_CLI = 2
    EVENT_TYPE_CDP = 3
    EVENT_TYPE_SYSLOG = 4
    EVENT_TYPE_CONFIG_NOTIFICATION = 5
    EVENT_TYPE_DEBUG_FLAG = 6
    EVENT_TYPE_SHOW_DATA = 7
    EVENT_TYPE_DISCOVERY = 8
    EVENT_TYPE_INTERFACE_STATE = 9
    EVENT_TYPE_INTERFACE_STATISTICS = 10
    EVENT_TYPE_OIR = 11
    EVENT_TYPE_IF_ADDRCHANGE = 12
    EVENT_TYPE_LOCATION_CHANGE = 13
    EVENT_TYPE_VTY = 14
    EVENT_TYPE_TOPOLOGY = 15
    EVENT_TYPE_RIB_STATE = 16
    EVENT_TYPE_ART_STATE = 17
    EVENT_TYPE_VRF = 18
    EVENT_TYPE_VLAN = 19
    EVENT_TYPE_INTERFACE_STATISTICS_POLL = 20
    EVENT_TYPE_UPDATE_ROUTE = 21
    EVENT_TYPE_ROUTING_SERVICE_SATUS = 22
    EVENT_TYPE_REPLAY_ROUTE = 23
    INTERFACE_DESCRIPTION_SIZE = 200
    MAC_ADDRESS_SIZE = 6
    ERR_BAD_ARGUMENT = OnepStatus.ONEP_ERR_BAD_ARGUMENT
    ERR_CONNECT_FAIL = OnepStatus.ONEP_ERR_CONNECT_FAIL
    ERR_EVENT_CHANNEL = OnepStatus.ONEP_ERR_EVENT_CHANNEL
    ERR_NO_DATA = OnepStatus.ONEP_ERR_NO_DATA
    ERR_DUPLICATE = OnepStatus.ONEP_ERR_DUPLICATE
    ERR_EVENTQ_FULL = OnepStatus.ONEP_EOK_EVENTQ_FULL
    SERIAL_VERSION_UID = 1L
    EVENT_MAX_OCCURS = 32
    EVENT_MIN_PRIORITY = 0
    EVENT_MAX_PRIORITY = 8
    OnepOperatorType = enum('ONEP_OP_NONE', 'ONEP_OP_GT', 'ONEP_OP_GE', 'ONEP_OP_EQ', 'ONEP_OP_NE', 'ONEP_OP_LT', 'ONEP_OP_LE')
    OnepCombinationType = enum('ONEP_COMBINATION_NONE', 'ONEP_COMBINATION_OR', 'ONEP_COMBINATION_AND')
    OnepAddressFamilyType = enum('ONEP_AF_ANY', 'ONEP_AF_INET', 'ONEP_AF_INET6', 'ONEP_AF_MAX')
    OnepAddressScopeType = enum('ONEP_ADDRESS_IPv4_PRIMARY', 'ONEP_ADDRESS_IPv4_SECONDARY', 'ONEP_ADDRESS_IPv4_ALL', 'ONEP_ADDRESS_IPv6_LINK_LOCAL', 'ONEP_ADDRESS_IPv6_EUI64', 'ONEP_ADDRESS_IPv6_GLOBAL_ANYCAST', 'ONEP_ADDRESS_IPv6_GLOBAL', 'ONEP_ADDRESS_IPv6_ALL')
    OnepBandwidthUnits = enum('ONEP_BW_UNITS_KBPS', 'ONEP_BW_UNITS_PERCENT')
    OnepQueueSizeUnits = enum('ONEP_QUEUE_UNITS_PKTS', 'ONEP_QUEUE_UNITS_BYTES', 'ONEP_QUEUE_UNITS_MSEC')
    OnepDscp = enum(ONEP_DSCP_DEFAULT=0, ONEP_DSCP_AF11=10, ONEP_DSCP_AF12=12, ONEP_DSCP_AF13=14, ONEP_DSCP_AF21=18, ONEP_DSCP_AF22=20, ONEP_DSCP_AF23=22, ONEP_DSCP_AF31=26, ONEP_DSCP_AF32=28, ONEP_DSCP_AF33=30, ONEP_DSCP_AF41=34, ONEP_DSCP_AF42=36, ONEP_DSCP_AF43=38, ONEP_DSCP_CS1=8, ONEP_DSCP_CS2=16, ONEP_DSCP_CS3=24, ONEP_DSCP_CS4=32, ONEP_DSCP_CS5=40, ONEP_DSCP_CS6=48, ONEP_DSCP_CS7=56, ONEP_DSCP_EF=46)
    OnepSyslogLevel = enum(EMERGENCY=0, ALERT=1, CRITICAL=2, ERROR=3, WARNING=4, NOTICE=5, INFO=6, DEBUG=7)
    OnepSyslogFacility = enum('LOCAL0', 'LOCAL1', 'LOCAL2', 'LOCAL3', 'LOCAL4', 'LOCAL5', 'LOCAL6', 'LOCAL7')
    OnepProtocol = enum(UDP=1, TCP=2, ICMP=3)
    OnepSnmpSecurityModel = enum(V1=1, V2C=2, USM=3)
    OnepSnmpSecurityLevel = enum(NOAUTH_NOPRIV=1, AUTH_NOPRIV=2, AUTH_PRIV=3, UNKNOWN=4)
    OnepUserKeyEncrtption = enum('UNKNOWN', 'UNENCRYPTED', 'SHA256', 'MD5')
    OnepSnmpTrap = enum(SNMP=1, SYSLOG=18, ENTITY=21, IPSEC=55)
    OnepEulaState = enum(ONEP_EULA_ACCEPTED=0, ONEP_EULA_NOT_ACCEPTED=1, ONEP_EULA_NOT_APPLICABLE=2)
    PasswordEncrypt = enum(UNENCRYPTED=0, SHA256=4, MD5=5, HIDDEN=7)
    VlanState = enum('NONE', 'ACTIVE', 'SUSPEND', 'NOT_CONFIG')
    AclProtocol = enum(ICMP=1, IGMP=2, TCP=6, EGP=8, IGRP=9, UDP=17, RSVP=46, GRE=47, ESP=50, AH=51, ALL=256)


# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:20:59 IST
