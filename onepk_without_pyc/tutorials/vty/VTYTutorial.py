#!/usr/bin/env python

# Copyright (c) 2010-2013 by Cisco Systems, Inc.
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
# package: tutorials.vty
import logging
from BaseTutorial import BaseTutorial
from onep.vty import VtyService
from onep.core.exception import OnepRemoteProcedureException, OnepException

logger = logging.getLogger('onep:VTYTutorial')
logger.setLevel(logging.INFO)

class VTYTutorial(BaseTutorial):
    """
    This tutorial shows how to create VTY Service on a ONEP Application 
    and demonstrates the capability to communicate with a Network Element via virtual terminal. .

    @author The onePK Team (onepk-feedback@cisco.com)
    """

    def show_parser_state_attributes(self, parser_state):
        """
        This method prints the attributes of the ParserState and iterates over the command results
        
        @param parser_state
        """
        #  START SNIPPET: vty_parser_state_attribs
        logger.info("ParserState prompt - %s", parser_state.prompt)
        logger.info("ParserState overallrc - %s", parser_state.overallRC)
        cmd_results = parser_state.results
        for cmd_result in cmd_results:
            logger.info("ParserState::cmdresult:inputline - %s", cmd_result.input_line)
            logger.info("ParserState::cmdresult:parsereturncode - %s", cmd_result.parse_return_code)
            logger.info("ParserState::cmdresult:errorlocation - %s", cmd_result.error_location)
        #  END SNIPPET: vty_parser_state_attribs


if __name__ == '__main__':
    """
    Invokes the tutorial via the command line. This main method attempts to use arguments from the command line.
    """
    import sys
    tutorial = VTYTutorial(sys.argv)
    logger.info("Reading arguments...")
    if not tutorial.parse_command_line():
        logger.error("Error in parsing arguments")
        sys.exit(1)
    try:
        logger.info("Connecting to Network Element...")
        if not tutorial.connect("VTYTutorial"):
            logger.error("Error in connecting to network element")
            sys.exit(1)
        logger.info("Done")
        
        """Get a VTYService from the NE"""
        #  START SNIPPET: create_vty
        vtyService = VtyService(tutorial.get_network_element()) 
        #  END SNIPPET: create_vty
        
        """Open the VTY on the NE with the default command interpreter"""
        #  START SNIPPET: open_vty
        vtyService.open()
        #  END SNIPPET: open_vty

        """Get a timeout of the VTY on NE"""
        #  START SNIPPET: get_vty_timeout
        logger.info("VTY Time Out - %s", vtyService.timeout)
        #  END SNIPPET: get_vty_timeout

        """Write a string to the VTY on NE"""        
        #  START SNIPPET: write_vty_command            
        TEST_CMD1 = "show onep status";
        cli_result = vtyService.write(TEST_CMD1)
        logger.info("Test Command : %s", TEST_CMD1)
        logger.info("CLI Result for Test Command : %s", cli_result)
        #  END SNIPPET: write_vty_command
        
        """Get the parser state and its attributes"""
        try:
            #  START SNIPPET: get_vty_parser_state
            parser_state = vtyService.get_parser_state()
            #  END SNIPPET: get_vty_parser_state
            
            """Show the parser state attributes"""
            tutorial.show_parser_state_attributes(parser_state)
        except OnepRemoteProcedureException as re:
            logger.error("Error in getting parser state : ", re)
        
        """Get the VTY State"""
        #  START SNIPPET: get_vty_state            
        logger.info("State - %s", vtyService.state)
        #  END SNIPPET: get_vty_state
        
        """Set the max response length"""
        #  START SNIPPET: set_vty_max_response            
        MAX_RESPONSE_LENGTH = 110
        vtyService.max_response = MAX_RESPONSE_LENGTH
        logger.info("MaxResponse - %s", vtyService.max_response)
        #  END SNIPPET: set_vty_max_response
        
        """Write a string to the VTY on NE"""
        TEST_CMD2 = "show version"
        cli_result = vtyService.write(TEST_CMD2)
        logger.info("Test Command : %s", TEST_CMD2)
        logger.info("CLI Result for Test Command : %s", cli_result)

        """Get the Max Response"""
        #  START SNIPPET: get_vty_max_response            
        logger.info("MaxResponse - %s", vtyService.max_response)
        #  END SNIPPET: get_vty_max_response
        
        """Resetting the max response length"""
        MAX_RESPONSE_LENGTH = 0
        vtyService.max_response = MAX_RESPONSE_LENGTH
        cli_result = vtyService.write(TEST_CMD2)
        logger.info("Test Command : %s", TEST_CMD2)
        logger.info("Test Command Max Response: %s", MAX_RESPONSE_LENGTH)
        logger.info("CLI Result for Test Command : %s", cli_result)
        try:
            """Show the parser state attributes"""
            tutorial.show_parser_state_attributes(parser_state)
        except OnepRemoteProcedureException as re:
            logger.error("Error in getting parser state", str(re))
        
        """Cancel the command execution"""
        #  START SNIPPET: vty_cancel_cmd
        vtyService.cancel()
        #  END SNIPPET: vty_cancel_cmd    
                
        """Close the VTY connection on NE"""
        #  START SNIPPET: vty_close            
        vtyService.close()
        #  END SNIPPET: vty_close            

        """Check if the VTY is still open"""
        logger.info("Is Open - %s", vtyService.is_open())

        """Destroy the VTY"""        
        #  START SNIPPET: vty_destroy      
        vtyService.destroy()
        #  END SNIPPET: vty_destroy 
    except Exception, e:
        #  START SNIPPET: disconnect_ne
        tutorial.disconnect()
        #  END SNIPPET: disconnect_ne
        logger.error(str(e))
    tutorial.disconnect()
    sys.exit(0)

