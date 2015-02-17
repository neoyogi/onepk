# 2015.02.05 17:19:39 IST
from thrift.Thrift import *
import PolicyCommonTypes.ttypes
import PolicyBulkIDL.ttypes
import AsyncMessageIDL.ttypes
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
    from thrift.protocol import fastbinary
except:
    fastbinary = None

class CmapResultAsyncIDL(object):
    """
    Attributes:
     - dsid
     - handle
     - opid
     - opcode
     - result
     - matchResultList
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'dsid',
      None,
      None),
     (2,
      TType.I64,
      'handle',
      None,
      None),
     (3,
      TType.I32,
      'opid',
      None,
      None),
     (4,
      TType.I16,
      'opcode',
      None,
      None),
     (5,
      TType.I16,
      'result',
      None,
      None),
     (6,
      TType.LIST,
      'matchResultList',
      (TType.STRUCT, (PolicyCommonTypes.ttypes.ResultIDL, PolicyCommonTypes.ttypes.ResultIDL.thrift_spec)),
      None))

    def __init__(self, dsid = None, handle = None, opid = None, opcode = None, result = None, matchResultList = None):
        self.dsid = dsid
        self.handle = handle
        self.opid = opid
        self.opcode = opcode
        self.result = result
        self.matchResultList = matchResultList



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
                    self.dsid = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.handle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.opid = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I16:
                    self.opcode = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I16:
                    self.result = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.LIST:
                    self.matchResultList = []
                    (_etype3, _size0,) = iprot.readListBegin()
                    for _i4 in xrange(_size0):
                        _elem5 = PolicyCommonTypes.ttypes.ResultIDL()
                        _elem5.read(iprot)
                        self.matchResultList.append(_elem5)

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
        oprot.writeStructBegin('CmapResultAsyncIDL')
        if self.dsid != None:
            oprot.writeFieldBegin('dsid', TType.I32, 1)
            oprot.writeI32(self.dsid)
            oprot.writeFieldEnd()
        if self.handle != None:
            oprot.writeFieldBegin('handle', TType.I64, 2)
            oprot.writeI64(self.handle)
            oprot.writeFieldEnd()
        if self.opid != None:
            oprot.writeFieldBegin('opid', TType.I32, 3)
            oprot.writeI32(self.opid)
            oprot.writeFieldEnd()
        if self.opcode != None:
            oprot.writeFieldBegin('opcode', TType.I16, 4)
            oprot.writeI16(self.opcode)
            oprot.writeFieldEnd()
        if self.result != None:
            oprot.writeFieldBegin('result', TType.I16, 5)
            oprot.writeI16(self.result)
            oprot.writeFieldEnd()
        if self.matchResultList != None:
            oprot.writeFieldBegin('matchResultList', TType.LIST, 6)
            oprot.writeListBegin(TType.STRUCT, len(self.matchResultList))
            for iter6 in self.matchResultList:
                iter6.write(oprot)

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




class EntryResultAsyncIDL(object):
    """
    Attributes:
     - dsid
     - handle
     - opid
     - opcode
     - policy_op_index
     - result
     - cmapResult
     - matchResultList
     - actionResultList
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'dsid',
      None,
      None),
     (2,
      TType.I64,
      'handle',
      None,
      None),
     (3,
      TType.I32,
      'opid',
      None,
      None),
     (4,
      TType.I16,
      'opcode',
      None,
      None),
     (5,
      TType.I32,
      'policy_op_index',
      None,
      None),
     (6,
      TType.I16,
      'result',
      None,
      None),
     (7,
      TType.STRUCT,
      'cmapResult',
      (CmapResultAsyncIDL, CmapResultAsyncIDL.thrift_spec),
      None),
     (8,
      TType.LIST,
      'matchResultList',
      (TType.STRUCT, (PolicyCommonTypes.ttypes.ResultIDL, PolicyCommonTypes.ttypes.ResultIDL.thrift_spec)),
      None),
     (9,
      TType.LIST,
      'actionResultList',
      (TType.STRUCT, (PolicyCommonTypes.ttypes.ResultIDL, PolicyCommonTypes.ttypes.ResultIDL.thrift_spec)),
      None))

    def __init__(self, dsid = None, handle = None, opid = None, opcode = None, policy_op_index = None, result = None, cmapResult = None, matchResultList = None, actionResultList = None):
        self.dsid = dsid
        self.handle = handle
        self.opid = opid
        self.opcode = opcode
        self.policy_op_index = policy_op_index
        self.result = result
        self.cmapResult = cmapResult
        self.matchResultList = matchResultList
        self.actionResultList = actionResultList



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
                    self.dsid = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.handle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.opid = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I16:
                    self.opcode = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.policy_op_index = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I16:
                    self.result = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.STRUCT:
                    self.cmapResult = CmapResultAsyncIDL()
                    self.cmapResult.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.LIST:
                    self.matchResultList = []
                    (_etype10, _size7,) = iprot.readListBegin()
                    for _i11 in xrange(_size7):
                        _elem12 = PolicyCommonTypes.ttypes.ResultIDL()
                        _elem12.read(iprot)
                        self.matchResultList.append(_elem12)

                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.LIST:
                    self.actionResultList = []
                    (_etype16, _size13,) = iprot.readListBegin()
                    for _i17 in xrange(_size13):
                        _elem18 = PolicyCommonTypes.ttypes.ResultIDL()
                        _elem18.read(iprot)
                        self.actionResultList.append(_elem18)

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
        oprot.writeStructBegin('EntryResultAsyncIDL')
        if self.dsid != None:
            oprot.writeFieldBegin('dsid', TType.I32, 1)
            oprot.writeI32(self.dsid)
            oprot.writeFieldEnd()
        if self.handle != None:
            oprot.writeFieldBegin('handle', TType.I64, 2)
            oprot.writeI64(self.handle)
            oprot.writeFieldEnd()
        if self.opid != None:
            oprot.writeFieldBegin('opid', TType.I32, 3)
            oprot.writeI32(self.opid)
            oprot.writeFieldEnd()
        if self.opcode != None:
            oprot.writeFieldBegin('opcode', TType.I16, 4)
            oprot.writeI16(self.opcode)
            oprot.writeFieldEnd()
        if self.policy_op_index != None:
            oprot.writeFieldBegin('policy_op_index', TType.I32, 5)
            oprot.writeI32(self.policy_op_index)
            oprot.writeFieldEnd()
        if self.result != None:
            oprot.writeFieldBegin('result', TType.I16, 6)
            oprot.writeI16(self.result)
            oprot.writeFieldEnd()
        if self.cmapResult != None:
            oprot.writeFieldBegin('cmapResult', TType.STRUCT, 7)
            self.cmapResult.write(oprot)
            oprot.writeFieldEnd()
        if self.matchResultList != None:
            oprot.writeFieldBegin('matchResultList', TType.LIST, 8)
            oprot.writeListBegin(TType.STRUCT, len(self.matchResultList))
            for iter19 in self.matchResultList:
                iter19.write(oprot)

            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.actionResultList != None:
            oprot.writeFieldBegin('actionResultList', TType.LIST, 9)
            oprot.writeListBegin(TType.STRUCT, len(self.actionResultList))
            for iter20 in self.actionResultList:
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




class PmapResultAsyncIDL(object):
    """
    Attributes:
     - dsid
     - handle
     - opid
     - opcode
     - result
     - entryResult
     - statsResult
     - statsResultEventHandle
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'dsid',
      None,
      None),
     (2,
      TType.I64,
      'handle',
      None,
      None),
     (3,
      TType.I32,
      'opid',
      None,
      None),
     (4,
      TType.I16,
      'opcode',
      None,
      None),
     (5,
      TType.I16,
      'result',
      None,
      None),
     (6,
      TType.LIST,
      'entryResult',
      (TType.STRUCT, (EntryResultAsyncIDL, EntryResultAsyncIDL.thrift_spec)),
      None),
     (7,
      TType.STRUCT,
      'statsResult',
      (PolicyCommonTypes.ttypes.PolicyStatsResultIDL, PolicyCommonTypes.ttypes.PolicyStatsResultIDL.thrift_spec),
      None),
     (8,
      TType.I32,
      'statsResultEventHandle',
      None,
      None))

    def __init__(self, dsid = None, handle = None, opid = None, opcode = None, result = None, entryResult = None, statsResult = None, statsResultEventHandle = None):
        self.dsid = dsid
        self.handle = handle
        self.opid = opid
        self.opcode = opcode
        self.result = result
        self.entryResult = entryResult
        self.statsResult = statsResult
        self.statsResultEventHandle = statsResultEventHandle



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
                    self.dsid = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.handle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.opid = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I16:
                    self.opcode = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I16:
                    self.result = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.LIST:
                    self.entryResult = []
                    (_etype24, _size21,) = iprot.readListBegin()
                    for _i25 in xrange(_size21):
                        _elem26 = EntryResultAsyncIDL()
                        _elem26.read(iprot)
                        self.entryResult.append(_elem26)

                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.STRUCT:
                    self.statsResult = PolicyCommonTypes.ttypes.PolicyStatsResultIDL()
                    self.statsResult.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.I32:
                    self.statsResultEventHandle = iprot.readI32()
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
        oprot.writeStructBegin('PmapResultAsyncIDL')
        if self.dsid != None:
            oprot.writeFieldBegin('dsid', TType.I32, 1)
            oprot.writeI32(self.dsid)
            oprot.writeFieldEnd()
        if self.handle != None:
            oprot.writeFieldBegin('handle', TType.I64, 2)
            oprot.writeI64(self.handle)
            oprot.writeFieldEnd()
        if self.opid != None:
            oprot.writeFieldBegin('opid', TType.I32, 3)
            oprot.writeI32(self.opid)
            oprot.writeFieldEnd()
        if self.opcode != None:
            oprot.writeFieldBegin('opcode', TType.I16, 4)
            oprot.writeI16(self.opcode)
            oprot.writeFieldEnd()
        if self.result != None:
            oprot.writeFieldBegin('result', TType.I16, 5)
            oprot.writeI16(self.result)
            oprot.writeFieldEnd()
        if self.entryResult != None:
            oprot.writeFieldBegin('entryResult', TType.LIST, 6)
            oprot.writeListBegin(TType.STRUCT, len(self.entryResult))
            for iter27 in self.entryResult:
                iter27.write(oprot)

            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.statsResult != None:
            oprot.writeFieldBegin('statsResult', TType.STRUCT, 7)
            self.statsResult.write(oprot)
            oprot.writeFieldEnd()
        if self.statsResultEventHandle != None:
            oprot.writeFieldBegin('statsResultEventHandle', TType.I32, 8)
            oprot.writeI32(self.statsResultEventHandle)
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
# 2015.02.05 17:19:39 IST
