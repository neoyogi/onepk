# 2015.02.05 17:23:20 IST
import logging
import sys
import os
import time
from onep.element import NetworkElement, SessionConfig
from onep.core.exception import OnepCommandException
from onep.core.exception import OnepResourceBusyException
from onep.core.exception import OnepNotSupportedException
from onep.vty import VtyService

class VtyHelper(object):
    """
        VTY helper for any presentation service to VtyService handling
    
        Contains helper functions that mimic IOS parser.  Is useful for
        cases where applications running in different threads share the same
        connection.  Flask REST frontend is a good example.
    
        - Automatically opens VtyService and leaves it open
    
        - If platform supports it, sets idle timeout of VtyService to infinite
    
        - Manages NetworkElement to ensure only one VtyService is instantiated
          per connection/application.
    
        - Evaluates parser errors
    
        - commit method automatically does retries if resource busy
          is returned
    
        """


    def __init__(self, elm):
        """
                Constructor takes a connected network element
                Throws on error:
                         OnepConnectionException - Connection to element failed.
        
                Keyword argument:
                class NetworkElement()
        
                """
        self.ne = elm
        self.vty = None
        self.trans = {}
        self.timeout = 0
        self.log = logging.getLogger(__name__)



    def _check_result(self, cli, ret):
        try:
            state = self.vty.get_parser_state()
        except OnepNotSupportedException:
            return 
        if state.overallRC:
            self.log.error('Command failed with overall return code %d', state.overallRC)
            for result in state.results:
                if result.parse_return_code:
                    self.log.error('Command: "%s" with return code %d', result.input_line, result.parse_return_code)
                    raise OnepCommandException('Command: "%s" with return code %d' % (result.input_line, result.parse_return_code))

        if ret and 'busy' in ret:
            raise OnepResourceBusyException('Command: "%s" with return error %s' % (cli, ret))



    def prepare(self):
        if not self.vty:
            if not self.ne._vty_service:
                self.ne._vty_service = VtyService(self.ne)
            self.vty = self.ne._vty_service
            if not self.vty.is_open():
                try:
                    self.vty._set_idle_timeout(self.timeout)
                except Exception as e:
                    self.log.info('Set idle timeout error ' + str(e))
                self.vty.open()



    def config(self, cmd):
        """
                Send a configuration command to Network Element
                  "config t " will be prepended if not in config_submode
                  " end" appended
                Throws on error:
                         OnepConnectionException - Connection to element failed.
                         OnepRemoteProcedureException - call to RPC failed
        
                Keyword argument:
                string -- CLI command
        
                """
        self.prepare()
        cli = 'config t\n' + cmd + '\nend'
        result = self.vty.write(cli)
        self._check_result(cli, result)
        self.destroy()
        return result



    def no_config(self, cmd):
        """
                Removes a configuration command from a Network Element
                  "config t " and "no" will be prepended and " end" appended
                Throws on error:
                         OnepConnectionException - Connection to element failed.
                         OnepRemoteProcedureException - call to RPC failed
         
                Keyword argument:
                string -- CLI command
        
                """
        self.prepare()
        cli = 'config t\nno ' + cmd + '\nend\n'
        result = self.vty.write(cli)
        self._check_result(cli, result)
        self.destroy()
        return result



    def rollback(self, start, end):
        """
                NOT IMPLEMENTED!!
        
                Rollback configuration commands stored in trasaction dict
                from start time to end time associated to command
        
                Keyword arguments:
                real -- start time
                real -- end time
        
                """
        rem = []
        [ rem.append(a) for a in self.trans if a >= start if a <= end ]



    def show(self, cmd):
        """
                Send a show command to Network Element
                  "show " will be prepended
                Throws on error:
                         OnepConnectionException - Connection to element failed.
                         OnepRemoteProcedureException - call to RPC failed
        
                Keyword argument:
                string -- CLI command
        
                """
        self.prepare()
        cli = 'show ' + cmd
        result = self.vty.write(cli)
        self._check_result(cli, result)
        self.destroy()
        return result



    def vty_exec(self, cli):
        """
                Send an executable command to Network Element
                Throws on error:
                         OnepConnectionException - Connection to element failed.
                         OnepRemoteProcedureException - call to RPC failed
        
                Keyword argument:
                string -- CLI command
        
                """
        self.prepare()
        result = self.vty.write(cli)
        self._check_result(cli, result)
        self.destroy()
        return result



    def debug(self, cmd):
        """
                Activate debug on Network Element
                  "debug " will be prepended
                Throws on error:
                         OnepConnectionException - Connection to element failed.
                         OnepRemoteProcedureException - call to RPC failed
        
                Keyword argument:
                string -- CLI command
        
                """
        self.prepare()
        cli = 'debug ' + cmd
        result = self.vty.write(cli)
        self._check_result(cli, result)
        self.destroy()
        return result



    def no_debug(self, cmd):
        """
                Deactivate debug on Network Element
                  "no debug " will be prepended
                Throws on error:
                         OnepConnectionException - Connection to element failed.
                         OnepRemoteProcedureException - call to RPC failed
        
                Keyword argument:
                string -- CLI command
        
                """
        self.prepare()
        cli = 'no debug ' + cmd
        result = self.vty.write(cli)
        self._check_result(cli, result)
        self.destroy()
        return result



    def commit(self):
        """
                Preform a write command to save running-config to startup-config
        
                WARNING: Not supported on all platforms
        
                """
        self.prepare()
        self.trans = {}
        result = ''
        try:
            result = self.vty.write('write')
            self._check_result('write', result)
            self.destroy()
            return result
        except OnepResourceBusyException:
            delay = 0.2
            for i in range(10):
                time.sleep(delay)
                delay *= 2
                try:
                    result = self.vty.write('write')
                    self._check_result('write', result)
                    self.destroy()
                    return result
                except OnepResourceBusyException as e:
                    pass

            raise e



    def destroy(self):
        pass




class DoHost(object):
    """
        This is a helper class that accepts input from shell scripts
        or shell commands and pipes them to the onep Python SDK. See
        __main__ below.
    
        Environment variables with defaults:
    
        ONEP_CERTIFICATE=~/ca.pem
        ONEP_PWD=''
        ONEP_USER=''
        ONEP_TRANSPORT=SessionConfig.SessionTransportMode.TIPC
        ONEP_UT_ADDR=127.0.0.1
    
        ------------------------------------------------------------------
        Example bash shell script "dohost":
    
        #!/bin/bash
        exec python /usr/lib/python2.7/site-packages/onep/vty/util.py "$@"
    
        Example bash shell script usage:
    
        ~/> dohost 'show hostname' 'sho hostna'
        hostname        N3k-2
    
        hostname        N3k-2
    
        ------------------------------------------------------------------
    
    
        The class can also be included in other Python scripts. If an
        instantiated and connected NetworkElement class is not passed
        in, the class will look for environment variables and if not
        found, default to a TIPC connection.
    
        ----------------------------------------------------------------------
        Example usage for Python script:
    
        ~/> python
        Python 2.7.1 (r271:86832, Mar 14 2011, 14:03:08) 
        [GCC 3.4.6 20060404 (Red Hat 3.4.6-3)] on linux2
        Type "help", "copyright", "credits" or "license" for more information.
        >>> from onep.vty.util import DoHost
        >>> with DoHost() as console:
        ...     output = console.dohost('show hostname', 'sho hostnam')
        ...     for text in output:
        ...         print text
        ... 
        hostname        N3k-2
    
        hostname        N3k-2
    
        >>>
        -----------------------------------------------------------------------
        """


    def __init__(self, element = None):
        if element:
            self.vty = VtyHelper(element)
        else:
            self._default_connect()
        self.delimiter = True



    def _default_connect(self):
        self.ios_ip_addr = os.getenv('ONEP_UT_ADDR', '127.0.0.1')
        self.onep_user = os.getenv('ONEP_USER', '')
        self.onep_pwd = os.getenv('ONEP_PWD', '')
        self.onep_cert = os.getenv('ONEP_CERTIFICATE', '~/ca.pem')
        self.onep_transport = os.getenv('ONEP_TRANSPORT', SessionConfig.SessionTransportMode.TIPC)
        self.sess = SessionConfig(self.onep_transport)
        self.sess.ca_certs = self.onep_cert
        self.ne = NetworkElement(self.ios_ip_addr, 'dohost')
        self.con = self.ne.connect(self.onep_user, self.onep_pwd, self.sess)
        self.vty = VtyHelper(self.ne)



    def _collect_output(self, _cmd):
        _ret = ''
        try:
            _ret = self.vty.vty_exec(str(_cmd))
            if self.delimiter:
                _ret = '{0}{' + _ret.strip() + '}'
        except Exception as e:
            if self.delimiter:
                _ret = 'ERROR: Command "' + _cmd + '"'
                ecode = str(e)[(str(e).rfind('code ') + 5):]
                _ret = '{' + ecode + '}{' + _ret + '}'
            else:
                _ret = 'ERROR: ' + str(e)
        return _ret



    def dohost(self, *commands):
        ret = []
        for cmd in commands:
            if hasattr(cmd, '__iter__'):
                for c in cmd:
                    ret.append(self._collect_output(c))

            else:
                ret.append(self._collect_output(cmd))

        return ret



    def __enter__(self):
        return self



    def __exit__(self, type, value, tb):
        self.ne.disconnect()



if __name__ == '__main__':
    log = None
    args = sys.argv[1:]
    if not args:
        print ''
        exit()
    with DoHost() as console:
        if args[0].startswith('-'):
            if args[0].startswith('-raw'):
                console.delimiter = False
            elif args[0].startswith('-li'):
                log = logging.getLogger('onep')
                log.setLevel(logging.INFO)
            elif args[0].startswith('-ld'):
                log = logging.getLogger('onep')
                log.setLevel(logging.DEBUG)
            else:
                raise TypeError('Illegal command')
            args.pop(0)
        if not args:
            if log:
                log.info('No argument passed to util')
            print ''
            exit()
        output = console.dohost(args)
        for text in output:
            print text


# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:23:20 IST
