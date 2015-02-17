# 2015.02.05 17:20:33 IST
import core.exception.OnepIllegalArgumentException
from onep.core.util.Enum import enum
OnepAAAAttributeType = enum('ONEP_AAA_AT_INVALID', 'ONEP_AAA_AT_USER_NAME', 'ONEP_AAA_AT_USER_PASSWORD', 'ONEP_AAA_AT_CHAP_ID', 'ONEP_AAA_AT_NAS_IP_ADDRESS', 'ONEP_AAA_AT_INTERFACE', 'ONEP_AAA_AT_SERVICE_TYPE', 'ONEP_AAA_AT_FRAMED_PROTOCOL', 'ONEP_AAA_AT_IPV4_ADDRESS', 'ONEP_AAA_AT_IPV4_NETMASK', 'ONEP_AAA_AT_ROUTING', 'ONEP_AAA_AT_ACL', 'ONEP_AAA_AT_FRAMED_MTU', 'ONEP_AAA_AT_LINK_COMPRESSION', 'ONEP_AAA_AT_LOGIN_IP_ADDR_HOST', 'ONEP_AAA_AT_LOGIN_SERVICE', 'ONEP_AAA_AT_LOGIN_TCP_PORT', 'ONEP_AAA_AT_MESSAGE', 'ONEP_AAA_AT_CALLBACK', 'ONEP_AAA_AT_ROUTE', 'ONEP_AAA_AT_STATE', 'ONEP_AAA_AT_CLASS', 'ONEP_AAA_AT_TIMEOUT', 'ONEP_AAA_AT_IDLE_TIMEOUT', 'ONEP_AAA_AT_TERMINATION_ACTION', 'ONEP_AAA_AT_DNIS', 'ONEP_AAA_AT_FORMATTED_CLID', 'ONEP_AAA_AT_NAS_IDENTIFIER', 'ONEP_AAA_AT_ACCT_STATUS_TYPE', 'ONEP_AAA_AT_DELAY_TIME', 'ONEP_AAA_AT_INPUT_OCTETS', 'ONEP_AAA_AT_OUTPUT_OCTETS', 'ONEP_AAA_AT_SESSION_ID', 'ONEP_AAA_AT_AUTHENTIC', 'ONEP_AAA_AT_SESSION_TIME', 'ONEP_AAA_AT_INPUT_PACKETS', 'ONEP_AAA_AT_OUTPUT_PACKETS', 'ONEP_AAA_AT_TERMINATE_CAUSE', 'ONEP_AAA_AT_MLP_SESSION_ID', 'ONEP_AAA_AT_MLP_LINKS_MAX', 'ONEP_AAA_AT_INPUT_GIGA_WORDS', 'ONEP_AAA_AT_OUTPUT_GIGA_WORDS', 'ONEP_AAA_AT_EVENT_TIMESTAMP', 'ONEP_AAA_AT_CHAP_CHALLENGE', 'ONEP_AAA_AT_INTERFACE_TYPE', 'ONEP_AAA_AT_PORT_LIMIT', 'ONEP_AAA_AT_TUNNEL_TYPE', 'ONEP_AAA_AT_TUNNEL_MEDIUM_TYPE', 'ONEP_AAA_AT_TUNNEL_CLIENT_ENDPOINT', 'ONEP_AAA_AT_TUNNEL_SERVER_ENDPOINT', 'ONEP_AAA_AT_TUNNEL_CONNECTION_ID', 'ONEP_AAA_AT_TUNNEL_PASSWORD', 'ONEP_AAA_AT_CONNECT_INFO', 'ONEP_AAA_AT_EAP_MESSAGE', 'ONEP_AAA_AT_MESSAGE_AUTHENTICATOR', 'ONEP_AAA_AT_TUNNEL_PRIVATE_GROUP_ID', 'ONEP_AAA_AT_VPDN_GROUP', 'ONEP_AAA_AT_TUNNEL_PREFERENCE', 'ONEP_AAA_AT_INTERIM_INTERVAL', 'ONEP_AAA_AT_ACCT_TUNNEL_PACKETS_LOST', 'ONEP_AAA_AT_ADDRESS_POOL', 'ONEP_AAA_AT_TUNNEL_CLIENT_AUTH_ID', 'ONEP_AAA_AT_TUNNEL_SERVER_AUTH_ID', 'ONEP_AAA_AT_NAS_IPV6_ADDRESS', 'ONEP_AAA_AT_IPV6_INTERFACEID', 'ONEP_AAA_AT_IPV6_PREFIX', 'ONEP_AAA_AT_LOGIN_IPV6_ADDR_HOST', 'ONEP_AAA_AT_ERROR_CAUSE', 'ONEP_AAA_AT_EAP_SESSION_ID', 'ONEP_AAA_AT_DELEGATED_IPV6_PREFIX', 'ONEP_AAA_AT_APP_ATTR', 'ONEP_AAA_AT_ALLOWED_APP', 'ONEP_AAA_AT_ALLOWED_ACTION', 'ONEP_AAA_AT_AUTO_ACCT')

# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:20:33 IST
