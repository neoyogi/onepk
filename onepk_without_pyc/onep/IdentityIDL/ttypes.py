# 2015.02.05 17:21:18 IST
from thrift.Thrift import *
import Shared.ttypes
import AaaIDL.ttypes
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
    from thrift.protocol import fastbinary
except:
    fastbinary = None

class Iden_event_e(object):
    IDEN_EVENT_SESION_UNDEF = 0
    IDEN_EVENT_SESSION_STARTED = 1
    IDEN_EVENT_SESSION_STOPPED = 2
    IDEN_EVENT_SESSION_AUTHC = 3
    IDEN_EVENT_SESSION_AUTHC_FAILED = 4
    IDEN_EVENT_SESSION_AUTHZ = 5
    IDEN_EVENT_SESSION_AUTHZ_FAILED = 6
    IDEN_EVENT_SESSION_POLICY_VIOLATION = 7
    IDEN_EVENT_SESSION_ATTR_CHANGE = 8
    IDEN_EVENT_SESSION_MAX = 9
    _VALUES_TO_NAMES = {0: 'IDEN_EVENT_SESION_UNDEF',
     1: 'IDEN_EVENT_SESSION_STARTED',
     2: 'IDEN_EVENT_SESSION_STOPPED',
     3: 'IDEN_EVENT_SESSION_AUTHC',
     4: 'IDEN_EVENT_SESSION_AUTHC_FAILED',
     5: 'IDEN_EVENT_SESSION_AUTHZ',
     6: 'IDEN_EVENT_SESSION_AUTHZ_FAILED',
     7: 'IDEN_EVENT_SESSION_POLICY_VIOLATION',
     8: 'IDEN_EVENT_SESSION_ATTR_CHANGE',
     9: 'IDEN_EVENT_SESSION_MAX'}
    _NAMES_TO_VALUES = {'IDEN_EVENT_SESION_UNDEF': 0,
     'IDEN_EVENT_SESSION_STARTED': 1,
     'IDEN_EVENT_SESSION_STOPPED': 2,
     'IDEN_EVENT_SESSION_AUTHC': 3,
     'IDEN_EVENT_SESSION_AUTHC_FAILED': 4,
     'IDEN_EVENT_SESSION_AUTHZ': 5,
     'IDEN_EVENT_SESSION_AUTHZ_FAILED': 6,
     'IDEN_EVENT_SESSION_POLICY_VIOLATION': 7,
     'IDEN_EVENT_SESSION_ATTR_CHANGE': 8,
     'IDEN_EVENT_SESSION_MAX': 9}


class Iden_filter_match_criteria_e(object):
    IDEN_FILTER_MATCH_CRITERIA_UNDEF = 0
    IDEN_FILTER_MATCH_CRITERIA_ALL = 1
    IDEN_FILTER_MATCH_CRITERIA_ANY = 2
    IDEN_FILTER_MATCH_CRITERIA_MAX = 3
    _VALUES_TO_NAMES = {0: 'IDEN_FILTER_MATCH_CRITERIA_UNDEF',
     1: 'IDEN_FILTER_MATCH_CRITERIA_ALL',
     2: 'IDEN_FILTER_MATCH_CRITERIA_ANY',
     3: 'IDEN_FILTER_MATCH_CRITERIA_MAX'}
    _NAMES_TO_VALUES = {'IDEN_FILTER_MATCH_CRITERIA_UNDEF': 0,
     'IDEN_FILTER_MATCH_CRITERIA_ALL': 1,
     'IDEN_FILTER_MATCH_CRITERIA_ANY': 2,
     'IDEN_FILTER_MATCH_CRITERIA_MAX': 3}


class Iden_action_e(object):
    IDEN_ACTION_UNDEF = 0
    IDEN_ACTION_NOTIFY = 1
    IDEN_ACTION_MAX = 2
    _VALUES_TO_NAMES = {0: 'IDEN_ACTION_UNDEF',
     1: 'IDEN_ACTION_NOTIFY',
     2: 'IDEN_ACTION_MAX'}
    _NAMES_TO_VALUES = {'IDEN_ACTION_UNDEF': 0,
     'IDEN_ACTION_NOTIFY': 1,
     'IDEN_ACTION_MAX': 2}


class Iden_action_criteria_e(object):
    IDEN_ACTION_CRITERIA_UNDEF = 0
    IDEN_ACTION_CRITERIA_DO_ALL = 1
    IDEN_ACTION_CRITERIA_MAX = 2
    _VALUES_TO_NAMES = {0: 'IDEN_ACTION_CRITERIA_UNDEF',
     1: 'IDEN_ACTION_CRITERIA_DO_ALL',
     2: 'IDEN_ACTION_CRITERIA_MAX'}
    _NAMES_TO_VALUES = {'IDEN_ACTION_CRITERIA_UNDEF': 0,
     'IDEN_ACTION_CRITERIA_DO_ALL': 1,
     'IDEN_ACTION_CRITERIA_MAX': 2}


class Iden_filter_e(object):
    IDEN_FILTER_SESSION_TYPE = 0
    IDEN_FILTER_INTERFACE = 1
    IDEN_FILTER_MAC_ADDRESS = 2
    IDEN_FILTER_IP_ADDRESS = 3
    IDEN_FILTER_DEVICE_NAME = 4
    IDEN_FILTER_SSID = 5
    IDEN_FILTER_SGT = 6
    IDEN_FILTER_ALWAYS = 7
    _VALUES_TO_NAMES = {0: 'IDEN_FILTER_SESSION_TYPE',
     1: 'IDEN_FILTER_INTERFACE',
     2: 'IDEN_FILTER_MAC_ADDRESS',
     3: 'IDEN_FILTER_IP_ADDRESS',
     4: 'IDEN_FILTER_DEVICE_NAME',
     5: 'IDEN_FILTER_SSID',
     6: 'IDEN_FILTER_SGT',
     7: 'IDEN_FILTER_ALWAYS'}
    _NAMES_TO_VALUES = {'IDEN_FILTER_SESSION_TYPE': 0,
     'IDEN_FILTER_INTERFACE': 1,
     'IDEN_FILTER_MAC_ADDRESS': 2,
     'IDEN_FILTER_IP_ADDRESS': 3,
     'IDEN_FILTER_DEVICE_NAME': 4,
     'IDEN_FILTER_SSID': 5,
     'IDEN_FILTER_SGT': 6,
     'IDEN_FILTER_ALWAYS': 7}


class Iden_filter_op_criteria_e(object):
    IDEN_FILTER_OP_UNDEF = 0
    IDEN_FILTER_OP_EQUAL = 1
    IDEN_FILTER_OP_NOT_EQUAL = 2
    IDEN_FILTER_OP_TOKEN_MATCH = 3
    IDEN_FILTER_OP_MATCH_FROM_END = 4
    IDEN_FILTER_OP_REG_EXP = 5
    IDEN_FILTER_OP_MAX = 6
    _VALUES_TO_NAMES = {0: 'IDEN_FILTER_OP_UNDEF',
     1: 'IDEN_FILTER_OP_EQUAL',
     2: 'IDEN_FILTER_OP_NOT_EQUAL',
     3: 'IDEN_FILTER_OP_TOKEN_MATCH',
     4: 'IDEN_FILTER_OP_MATCH_FROM_END',
     5: 'IDEN_FILTER_OP_REG_EXP',
     6: 'IDEN_FILTER_OP_MAX'}
    _NAMES_TO_VALUES = {'IDEN_FILTER_OP_UNDEF': 0,
     'IDEN_FILTER_OP_EQUAL': 1,
     'IDEN_FILTER_OP_NOT_EQUAL': 2,
     'IDEN_FILTER_OP_TOKEN_MATCH': 3,
     'IDEN_FILTER_OP_MATCH_FROM_END': 4,
     'IDEN_FILTER_OP_REG_EXP': 5,
     'IDEN_FILTER_OP_MAX': 6}


class Iden_Match_IDL(object):
    """
    Attributes:
     - match_id
     - match_attr_list
     - filter_op
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'match_id',
      None,
      None),
     (2,
      TType.LIST,
      'match_attr_list',
      (TType.STRUCT, (AaaIDL.ttypes.Attribute_IDL, AaaIDL.ttypes.Attribute_IDL.thrift_spec)),
      None),
     (3,
      TType.I32,
      'filter_op',
      None,
      None))

    def __init__(self, match_id = None, match_attr_list = None, filter_op = None):
        self.match_id = match_id
        self.match_attr_list = match_attr_list
        self.filter_op = filter_op



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.match_id = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.match_attr_list = []
                    (_etype3, _size0,) = iprot.readListBegin()
                    for _i4 in xrange(_size0):
                        _elem5 = AaaIDL.ttypes.Attribute_IDL()
                        _elem5.read(iprot)
                        self.match_attr_list.append(_elem5)

                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.filter_op = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()

        iprot.readStructEnd()



    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return 
        oprot.writeStructBegin('Iden_Match_IDL')
        if self.match_id != None:
            oprot.writeFieldBegin('match_id', TType.I32, 1)
            oprot.writeI32(self.match_id)
            oprot.writeFieldEnd()
        if self.match_attr_list != None:
            oprot.writeFieldBegin('match_attr_list', TType.LIST, 2)
            oprot.writeListBegin(TType.STRUCT, len(self.match_attr_list))
            for iter6 in self.match_attr_list:
                iter6.write(oprot)

            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.filter_op != None:
            oprot.writeFieldBegin('filter_op', TType.I32, 3)
            oprot.writeI32(self.filter_op)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

        def validate(self):
            pass





    def __repr__(self):
        L = [ '%s=%r' % (key, value) for (key, value,) in self.__dict__.iteritems() ]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))



    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__



    def __ne__(self, other):
        return not self == other




class Iden_Filter_IDL(object):
    """
    Attributes:
     - match_list
     - match_criteria
     - notify_attr_list
    """

    thrift_spec = (None,
     (1,
      TType.LIST,
      'match_list',
      (TType.STRUCT, (Iden_Match_IDL, Iden_Match_IDL.thrift_spec)),
      None),
     (2,
      TType.I32,
      'match_criteria',
      None,
      None),
     (3,
      TType.LIST,
      'notify_attr_list',
      (TType.STRUCT, (AaaIDL.ttypes.Attribute_IDL, AaaIDL.ttypes.Attribute_IDL.thrift_spec)),
      None))

    def __init__(self, match_list = None, match_criteria = None, notify_attr_list = None):
        self.match_list = match_list
        self.match_criteria = match_criteria
        self.notify_attr_list = notify_attr_list



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.LIST:
                    self.match_list = []
                    (_etype10, _size7,) = iprot.readListBegin()
                    for _i11 in xrange(_size7):
                        _elem12 = Iden_Match_IDL()
                        _elem12.read(iprot)
                        self.match_list.append(_elem12)

                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.match_criteria = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.LIST:
                    self.notify_attr_list = []
                    (_etype16, _size13,) = iprot.readListBegin()
                    for _i17 in xrange(_size13):
                        _elem18 = AaaIDL.ttypes.Attribute_IDL()
                        _elem18.read(iprot)
                        self.notify_attr_list.append(_elem18)

                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()

        iprot.readStructEnd()



    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return 
        oprot.writeStructBegin('Iden_Filter_IDL')
        if self.match_list != None:
            oprot.writeFieldBegin('match_list', TType.LIST, 1)
            oprot.writeListBegin(TType.STRUCT, len(self.match_list))
            for iter19 in self.match_list:
                iter19.write(oprot)

            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.match_criteria != None:
            oprot.writeFieldBegin('match_criteria', TType.I32, 2)
            oprot.writeI32(self.match_criteria)
            oprot.writeFieldEnd()
        if self.notify_attr_list != None:
            oprot.writeFieldBegin('notify_attr_list', TType.LIST, 3)
            oprot.writeListBegin(TType.STRUCT, len(self.notify_attr_list))
            for iter20 in self.notify_attr_list:
                iter20.write(oprot)

            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

        def validate(self):
            pass





    def __repr__(self):
        L = [ '%s=%r' % (key, value) for (key, value,) in self.__dict__.iteritems() ]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))



    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__



    def __ne__(self, other):
        return not self == other




class Iden_Event_IDL(object):
    """
    Attributes:
     - event
     - filter
    """

    thrift_spec = (None, (1,
      TType.I32,
      'event',
      None,
      None), (2,
      TType.STRUCT,
      'filter',
      (Iden_Filter_IDL, Iden_Filter_IDL.thrift_spec),
      None))

    def __init__(self, event = None, filter = None):
        self.event = event
        self.filter = filter



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.event = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.filter = Iden_Filter_IDL()
                    self.filter.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()

        iprot.readStructEnd()



    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return 
        oprot.writeStructBegin('Iden_Event_IDL')
        if self.event != None:
            oprot.writeFieldBegin('event', TType.I32, 1)
            oprot.writeI32(self.event)
            oprot.writeFieldEnd()
        if self.filter != None:
            oprot.writeFieldBegin('filter', TType.STRUCT, 2)
            self.filter.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

        def validate(self):
            pass





    def __repr__(self):
        L = [ '%s=%r' % (key, value) for (key, value,) in self.__dict__.iteritems() ]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))



    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__



    def __ne__(self, other):
        return not self == other




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:21:19 IST
