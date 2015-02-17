# 2015.02.05 17:18:18 IST
from onep.NetworkElementIDL import *
from onep.core.util.Enum import enum

class ElementProperty(object):
    """
    Provides the static properties of the NetworkElement.
    
    @undocumented: __init__
    @undocumented: _get_product_id
    @undocumented: _get_processor
    @undocumented: _get_serial_no
    @undocumented: _get_sys_name
    @undocumented: _get_sys_uptime
    @undocumented: _get_content_string
    @undocumented: _get_udi
    @undocumented: _get_version_id
    """


    def __init__(self, elem, idl):
        """
        For internal use only
        """
        self.element = elem
        self.idl = idl
        self.api_client = NetworkElementIDL.Client(self.element.api_protocol)



    def _get_product_id(self):
        """
        For internal use only
        """
        return self.idl.platform


    product_id = property(_get_product_id)

    def _get_processor(self):
        """
        For internal use only
        """
        return self.idl.processor


    processor = property(_get_processor)

    def _get_serial_no(self):
        """
        For internal use only
        """
        return self.idl.serialNo


    SerialNo = property(_get_serial_no)

    def _get_udi(self):
        """
        For internal use only
        """
        return self.idl.udi


    udi = property(_get_udi)

    def _get_version_id(self):
        """
        For internal use only
        """
        return self.idl.versionId


    version_id = property(_get_version_id)

    def _get_sys_descr(self):
        """
        For internal use only
        """
        return self.idl.sysDescr


    sys_descr = property(_get_sys_descr)

    def _get_sys_name(self):
        """
        For internal use only
        """
        sysName = None
        try:
            if self.element != None and self.element.session_handle != None:
                sysName = self.api_client.NetworkElement_getSysNameIDL(self.element.session_handle._id)
            return sysName
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e.message, e)


    sys_name = property(_get_sys_name)

    def _get_sys_uptime(self):
        """
        For internal use only
        """
        uptime = 0
        try:
            if self.element != None and self.element.session_handle != None:
                uptime = self.api_client.NetworkElement_getSysUpTimeIDL(self.element.session_handle._id)
            return uptime
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e.message, e)


    sys_uptime = property(_get_sys_uptime)

    def _get_content_string(self):
        """
        For internal use only
        """
        sb = '\tProduct ID   : ' + str(self.idl.platform) + '\n'
        sb += '\tProcessor    : ' + str(self.idl.processor) + '\n'
        sb += '\tSerial No    : ' + str(self.idl.serialNo) + '\n'
        try:
            sb += '\tsysName      : ' + self.sys_name + '\n'
            sb += '\tsysUpTime    : ' + str(self._get_sys_uptime()) + '\n'
        except Exception as e:
            sb += '\tsysName      :\n'
            sb += '\tsysUpTime    :\n'
        sb += '\tsysDescr     : ' + str(self.idl.sysDescr) + '\n'
        return sb


    content_string = property(_get_content_string)

    def __str__(self):
        sb = ''
        addr = ''
        if self.element != None:
            addr = self.element.host_address
            if addr == None:
                addr = ''
        sb += 'ElementProperty  [ ' + addr + ' ]\n'
        sb += self.content_string
        return sb



ElementProperty.OnepElementHwType = enum('ONEP_ELEMENT_HW_BASE_ETHER', 'ONEP_ELEMENT_HW_FAST_ETHER', 'ONEP_ELEMENT_HW_GIGA_ETHER')

# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:18:18 IST
