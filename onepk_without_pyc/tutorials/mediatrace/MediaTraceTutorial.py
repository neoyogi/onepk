#! /usr/bin/env python

# Copyright (c) 2010-2014 by Cisco Systems, Inc.
# 
# THIS SAMPLE CODE IS PROVIDED "AS IS" WITHOUT ANY EXPRESS OR IMPLIED WARRANTY
# BY CISCO SOLELY FOR THE PURPOSE of PROVIDING PROGRAMMING EXAMPLES.
# CISCO SHALL NOT BE HELD LIABLE FOR ANY USE OF THE SAMPLE CODE IN ANY 
# APPLICATION.
# 
# Redistribution and use of the sample code, with or without
# modification, are permitted provided that the following conditions
# are met:
# Redistributions of source code must retain the above disclaimer.
# 
import logging, sys
from onep.vty import VtyService
from onep.mediatrace import mtrace
from BaseTutorial import BaseTutorial

logger = logging.getLogger('onep:MediaTraceTutorial')
logger.setLevel(logging.INFO)


class MediaTrace(BaseTutorial):
    '''
    This tutorial will configure and print out the results of a simple
    Mediatrace ECHO profile.

    @author The onePK Team (onepk-feedback@cisco.com)
    '''
    def check_target(self):
        logger.info("******* CHECKING MEDIATRACE CONFIG *******")
        try:
            vty = VtyService(self.get_network_element())
            vty.open()
            resp = vty.write('sho run')
            resping = vty.write('ping '+ self.dst_ip)
            vty.close()
            if resp:
                vty.open()
                if resp.find('mediatrace initiator source-ip') == -1:
                    logger.info('"mediatrace initiator ..." not set on target')
                    logger.info("******* ADDING INITIATOR SOURCE *******")
                    vty.write('conf t')
                    vty.write('mediatrace initiator source-ip '+ self.initiater_src)
                if resp.find('mediatrace responder') == -1:
                    logger.info('"mediatrace responder" not set on target ')
                    logger.info("******* ADDING RESPONDER *******")
                    vty.write('conf t)
                    vty.write('mediatrace responder')
                if resp.find('service set mediatrace') > -1:
                    if resping.find('Success rate is 0') > -1:
                        logger.info('Target cannot reach %s so ECHO '
                                    'traceroute_status will TIMEOUT',
                                    self.dst_ip)
                    return True
            raise Exception('forced fail')
        except Exception as e:
            logger.info("Target not setup correctly")
            res = raw_input('''
                Target test device must have the following configurations:
                -------------------------------------------------------------------
                |conf t                                                           |
                | mediatrace responder                                            |
                | mediatrace initiator source-ip <IP address of Target interface> |
                | onep                                                            |
                |  service set mediatrace                                         |
                -------------------------------------------------------------------
                Enter yes if config has been applied or quit to exit: 
                ''')
            if res.startswith('y'):
                return self.check_target()
            else:
                return False
        return True

    def __enter__(self):
        return self

    def __exit__(self, type, value, tb):
        logger.info("******* DISCONNECT *******")
        self.disconnect()

    initiater_src = '10.1.1.4'
    src_ip = '10.0.0.1'
    src_port = 1000
    dst_ip = '10.0.2.2'
    dst_port = 2000
    to = 5


if __name__ == '__main__':
    with MediaTrace(sys.argv) as tutorial:

        if not tutorial.parse_command_line(False):
            logger.error("Error in parsing arguments")
            exit(1)

        logger.info("******* CONNECT *******")
        tutorial.connect('MediaTraceTutorial')

        logger.info("******* CREATE PATH SPECIFIER *******")
        ps = mtrace.PathSpecifier(tutorial.src_ip,
                                  tutorial.src_port,
                                  tutorial.dst_ip,
                                  tutorial.dst_port,
                                  mtrace.Protocol.UDP)
        print str(ps)

        if not tutorial.check_target():
            logger.info("******* MEDIATRACE NOT CONFIGURED *******")
            exit(1)

        logger.info("******* INITIATE MEDIATRACE *******")
        graph = mtrace.trace_request(tutorial.get_network_element(),
                                     mtrace.ProfileType.ECHO, ps, tutorial.to)

        logger.info("******* PRINT GRAPH RESULTS *******")
        print str(graph)
