#!/usr/bin/env python

# 
#  * Copyright (c) 2010-2013, Cisco Systems, Inc.
#  *
#  * THIS SAMPLE CODE IS PROVIDED "AS IS" WITHOUT ANY EXPRESS OR IMPLIED WARRANTY
#  * BY CISCO SOLELY FOR THE PURPOSE of PROVIDING PROGRAMMING EXAMPLES.
#  * CISCO SHALL NOT BE HELD LIABLE FOR ANY USE OF THE SAMPLE CODE IN ANY
#  * APPLICATION.
#  *
#  * Redistribution and use of the sample code, with or without
#  * modification, are permitted provided that the following conditions
#  * are met:
#  * Redistributions of source code must retain the above disclaimer.
#  *
"""
This tutorial demonstrates how to use custom application managed data.

@author The onePK Team (onepk-feedback@cisco.com)
"""
import logging
import getopt
import getpass
from BaseTutorial import BaseTutorial
from onep.element import NetworkElement
from onep.applmgmt import ApplicationCli
from onep.applmgmt import ApplicationConfigCliListener
from onep.applmgmt import ApplicationExecCliListener
import time
from onep.core.exception import OnepRemoteProcedureException

logger = logging.getLogger('onep:ApplicationManagementTutorial')
logger.setLevel(logging.INFO)

class ApplicationManagementTutorial(BaseTutorial):
    
    
    SLEEP = 300000
    app_name = None
    domain = None
    instance_ = None
    version = None
    args = None


    
    def parse_command_line_applmgmt(self):
        
        #super(ApplicationManagementTutorial, self).parse_command_line(args)
        base_usage_msg = tutorial.get_usage()
        usage_message_applmgmt = base_usage_msg + '\n -n <app_name> \n -d <domain> \n -i <instance> \n -v <version>'
        try:
            opts, args = getopt.getopt(self.args[1:],"ha:n:d:i:v:t:R:C:K:P:",["hostname=","app_name=","domain=","instance=","version=","transport=", "rootcert=", "clientcert=", "key=", "passphrase="])
        except getopt.GetoptError as err:
            print str(err)
            logger.info(usage_message_applmgmt)
            sys.exit()
        for option, arg in opts:
            if option == '-h':
                logger.info(usage_message_applmgmt)
                sys.exit()
            elif option in ("-a", "--hostname"):
                tutorial.element_hostname = arg
            elif option in ("-t", "--transport"):
                tutorial.transport = arg
            elif option in ("-n", "--app_name"):
                self.app_name = arg
            elif option in ("-d","--domain"):
                self.domain = arg
            elif option in ("-i", "--instance"):
                self.instance = arg
            elif option in ("-v", "--version"):
                self.version = arg
            elif option in ("-R", "--rootcert"):
                tutorial.root_cert_path = arg
            elif option in ("-C", "--clientcert"):
                tutorial.client_cert_path = arg
            elif option in ("-K", "--key"):
                tutorial.client_key_path = arg
            elif option in ("P", "--passphrase"):
                tutorial.key_passphrase = arg
        tutorial.username = raw_input('Enter Username : ')
        tutorial.password = getpass.getpass('Enter Password : ')
        
        if(tutorial.element_hostname==None or tutorial.username==None or tutorial.password==None or self.app_name==None or self.domain==None or self.instance==None or self.version==None):
            logger.error(usage_message_applmgmt)
            return False
        return True
            



    def getUsageRequiredOptions(self):
        
        return super(ApplicationManagementTutorial, self).getUsageRequiredOptions() + " -n <app name>" + " -c <config domain>" + " -i <instance>" + " -v <version>"

#  START SNIPPET: ExampleConfigListener
class ExampleConfigListener(ApplicationConfigCliListener):
        
    def handle_event(self, cli_data, client_data):
            
        cli_data_name = cli_data.data_name
        cli_data_value = cli_data.data_value
        print "\ndataName = " + cli_data_name + ", dataValue = " + cli_data_value + ", clientData = " + client_data

#  END SNIPPET: ExampleConfigListener
     
#  START SNIPPET: ExampleExecListener
class ExampleExecListener(ApplicationExecCliListener):
        
    def handle_event(self, cli_data, client_data):
            
        cli_data_name = cli_data.data_name
        print "\ndataName = " + cli_data_name + ", clientData = " + client_data
        return "PythonClient data"

#  END SNIPPET: ExampleExecListener


if __name__ == '__main__':
    import sys
    tutorial = ApplicationManagementTutorial(sys.argv)
    if not tutorial.parse_command_line_applmgmt():
        logger.error("Error in parsing arguments")
        sys.exit(1)
    try:
        logger.info("Connecting to Network Element...")
        #  START SNIPPET: appName
        '''
         Note that the application name has to match the name in xml file.
         In this case, in cli_ext_tutorial_app.xml, its name 'cli_tutorial_app'.
        '''    
        if not tutorial.connect(tutorial.app_name):
            sys.exit(2)
            
        #  END SNIPPET: appName
        #  Create ApplicationCLI instance 
        #  START SNIPPET: getConfig
        # Retrieve config value for App config data 'app-category' 
        
        application_cli = ApplicationCli(tutorial.get_network_element(),
                                         tutorial.version,
                                         tutorial.instance,
                                         tutorial.domain )
        config_data = application_cli.get_config('app_category_cmd')
        #  END SNIPPET: getConfig
        if config_data != None:
            logger.info("Config data = %s" , config_data)
        #  START SNIPPET: registerListener
        #  Add execListener and configListener 
        application_cli.set_exec_listener(ExampleExecListener(), "Show data changed")
        application_cli.set_config_listener(ExampleConfigListener(), "Config data changed")
        #  END SNIPPET: registerListener
        # 
        #  * Issue config command on Network Element to receive notification 
        #  * about application defined config data.
        #              
        logger.info("\n on NE, issue the command in : " + "conf t \n" + "  onep applications domain1 \n" + "  cli_tutorial_app v0.2 instance1 \n" + "  app-category name routing \n" + "  end\n")
        #  Issue show command for application defined show data 
        logger.info("\n on NE, issue command: \n" + "  show onep application cli_tutorial_app v0.2 domain1 instance1 app-category")
        try:
            # Wait for response
            logger.info("\n\n Waiting for event....\n\n")
            time.sleep(30)
        except Exception as e:
            logger.error(e)
                
    except OnepRemoteProcedureException as e:
        logger.error("Make sure the cli_ext_tutorial_app.xsd" + " is installed properly on the router\n" + "Run this command on the router: \n" + "\"show onep cli-extensions applications\" " + " and check if \"cli_tutorial_app\" is installed\n")
        logger.error(e)
    except Exception as e:
        logger.error(e)
    finally:
        print "Disconnecting from the Network Element"    
        tutorial.disconnect()
    sys.exit(0)

