# 2015.02.05 17:19:37 IST
from thrift.Thrift import *
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
    from thrift.protocol import fastbinary
except:
    fastbinary = None

class ResultIDL(object):
    """
      Result
    
      Attributes:
       - dsid
       - handle
       - opcode
       - opId
       - result
       - resultString
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
      TType.I16,
      'opcode',
      None,
      None),
     (4,
      TType.I32,
      'opId',
      None,
      None),
     (5,
      TType.I16,
      'result',
      None,
      None),
     (6,
      TType.STRING,
      'resultString',
      None,
      None))

    def __init__(self, dsid = None, handle = None, opcode = None, opId = None, result = None, resultString = None):
        self.dsid = dsid
        self.handle = handle
        self.opcode = opcode
        self.opId = opId
        self.result = result
        self.resultString = resultString



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
                if ftype == TType.I16:
                    self.opcode = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.opId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I16:
                    self.result = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRING:
                    self.resultString = iprot.readString()
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
        oprot.writeStructBegin('ResultIDL')
        if self.dsid != None:
            oprot.writeFieldBegin('dsid', TType.I32, 1)
            oprot.writeI32(self.dsid)
            oprot.writeFieldEnd()
        if self.handle != None:
            oprot.writeFieldBegin('handle', TType.I64, 2)
            oprot.writeI64(self.handle)
            oprot.writeFieldEnd()
        if self.opcode != None:
            oprot.writeFieldBegin('opcode', TType.I16, 3)
            oprot.writeI16(self.opcode)
            oprot.writeFieldEnd()
        if self.opId != None:
            oprot.writeFieldBegin('opId', TType.I32, 4)
            oprot.writeI32(self.opId)
            oprot.writeFieldEnd()
        if self.result != None:
            oprot.writeFieldBegin('result', TType.I16, 5)
            oprot.writeI16(self.result)
            oprot.writeFieldEnd()
        if self.resultString != None:
            oprot.writeFieldBegin('resultString', TType.STRING, 6)
            oprot.writeString(self.resultString)
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




class classStatsResultIDL(object):
    """
      Class Stats Result
    
      Attributes:
       - classified_pkts
       - classified_bytes
       - classified_rate
       - drop_pkts
       - drop_bytes
       - drop_rate
      """

    thrift_spec = (None,
     (1,
      TType.I64,
      'classified_pkts',
      None,
      None),
     (2,
      TType.I64,
      'classified_bytes',
      None,
      None),
     (3,
      TType.I64,
      'classified_rate',
      None,
      None),
     (4,
      TType.I64,
      'drop_pkts',
      None,
      None),
     (5,
      TType.I64,
      'drop_bytes',
      None,
      None),
     (6,
      TType.I64,
      'drop_rate',
      None,
      None))

    def __init__(self, classified_pkts = None, classified_bytes = None, classified_rate = None, drop_pkts = None, drop_bytes = None, drop_rate = None):
        self.classified_pkts = classified_pkts
        self.classified_bytes = classified_bytes
        self.classified_rate = classified_rate
        self.drop_pkts = drop_pkts
        self.drop_bytes = drop_bytes
        self.drop_rate = drop_rate



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
                if ftype == TType.I64:
                    self.classified_pkts = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.classified_bytes = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I64:
                    self.classified_rate = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I64:
                    self.drop_pkts = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I64:
                    self.drop_bytes = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I64:
                    self.drop_rate = iprot.readI64()
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
        oprot.writeStructBegin('classStatsResultIDL')
        if self.classified_pkts != None:
            oprot.writeFieldBegin('classified_pkts', TType.I64, 1)
            oprot.writeI64(self.classified_pkts)
            oprot.writeFieldEnd()
        if self.classified_bytes != None:
            oprot.writeFieldBegin('classified_bytes', TType.I64, 2)
            oprot.writeI64(self.classified_bytes)
            oprot.writeFieldEnd()
        if self.classified_rate != None:
            oprot.writeFieldBegin('classified_rate', TType.I64, 3)
            oprot.writeI64(self.classified_rate)
            oprot.writeFieldEnd()
        if self.drop_pkts != None:
            oprot.writeFieldBegin('drop_pkts', TType.I64, 4)
            oprot.writeI64(self.drop_pkts)
            oprot.writeFieldEnd()
        if self.drop_bytes != None:
            oprot.writeFieldBegin('drop_bytes', TType.I64, 5)
            oprot.writeI64(self.drop_bytes)
            oprot.writeFieldEnd()
        if self.drop_rate != None:
            oprot.writeFieldBegin('drop_rate', TType.I64, 6)
            oprot.writeI64(self.drop_rate)
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




class matchStatsResultIDL(object):
    """
      Match Stats Result
    
      Attributes:
       - match_stat_type
       - match_type
       - match_pkts
       - match_bytes
       - match_rate
      """

    thrift_spec = (None,
     (1,
      TType.I32,
      'match_stat_type',
      None,
      None),
     (2,
      TType.I32,
      'match_type',
      None,
      None),
     (3,
      TType.I64,
      'match_pkts',
      None,
      None),
     (4,
      TType.I64,
      'match_bytes',
      None,
      None),
     (5,
      TType.I64,
      'match_rate',
      None,
      None))

    def __init__(self, match_stat_type = None, match_type = None, match_pkts = None, match_bytes = None, match_rate = None):
        self.match_stat_type = match_stat_type
        self.match_type = match_type
        self.match_pkts = match_pkts
        self.match_bytes = match_bytes
        self.match_rate = match_rate



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
                    self.match_stat_type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.match_type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I64:
                    self.match_pkts = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I64:
                    self.match_bytes = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I64:
                    self.match_rate = iprot.readI64()
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
        oprot.writeStructBegin('matchStatsResultIDL')
        if self.match_stat_type != None:
            oprot.writeFieldBegin('match_stat_type', TType.I32, 1)
            oprot.writeI32(self.match_stat_type)
            oprot.writeFieldEnd()
        if self.match_type != None:
            oprot.writeFieldBegin('match_type', TType.I32, 2)
            oprot.writeI32(self.match_type)
            oprot.writeFieldEnd()
        if self.match_pkts != None:
            oprot.writeFieldBegin('match_pkts', TType.I64, 3)
            oprot.writeI64(self.match_pkts)
            oprot.writeFieldEnd()
        if self.match_bytes != None:
            oprot.writeFieldBegin('match_bytes', TType.I64, 4)
            oprot.writeI64(self.match_bytes)
            oprot.writeFieldEnd()
        if self.match_rate != None:
            oprot.writeFieldBegin('match_rate', TType.I64, 5)
            oprot.writeI64(self.match_rate)
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




class actionStatsResultIDL(object):
    """
      Action Stats Result
    
      Attributes:
       - action_stat_type
       - action_type
       - action_pkts
       - action_bytes
       - conform_pkts
       - conform_bytes
       - conform_rate
       - exceed_pkts
       - exceed_bytes
       - exceed_rate
       - violate_pkts
       - violate_bytes
       - violate_rate
       - queue_drop_pkts
       - queue_drop_bytes
       - queue_drop_flows
       - queue_no_buffers
       - queue_out_pkts
       - queue_out_bytes
       - queue_size_pkts
       - queue_size_bytes
      """

    thrift_spec = (None,
     (1,
      TType.I32,
      'action_stat_type',
      None,
      None),
     (2,
      TType.I32,
      'action_type',
      None,
      None),
     (3,
      TType.I64,
      'action_pkts',
      None,
      None),
     (4,
      TType.I64,
      'action_bytes',
      None,
      None),
     (5,
      TType.I64,
      'conform_pkts',
      None,
      None),
     (6,
      TType.I64,
      'conform_bytes',
      None,
      None),
     (7,
      TType.I64,
      'conform_rate',
      None,
      None),
     (8,
      TType.I64,
      'exceed_pkts',
      None,
      None),
     (9,
      TType.I64,
      'exceed_bytes',
      None,
      None),
     (10,
      TType.I64,
      'exceed_rate',
      None,
      None),
     (11,
      TType.I64,
      'violate_pkts',
      None,
      None),
     (12,
      TType.I64,
      'violate_bytes',
      None,
      None),
     (13,
      TType.I64,
      'violate_rate',
      None,
      None),
     (14,
      TType.I64,
      'queue_drop_pkts',
      None,
      None),
     (15,
      TType.I64,
      'queue_drop_bytes',
      None,
      None),
     (16,
      TType.I64,
      'queue_drop_flows',
      None,
      None),
     (17,
      TType.I64,
      'queue_no_buffers',
      None,
      None),
     (18,
      TType.I64,
      'queue_out_pkts',
      None,
      None),
     (19,
      TType.I64,
      'queue_out_bytes',
      None,
      None),
     (20,
      TType.I64,
      'queue_size_pkts',
      None,
      None),
     (21,
      TType.I64,
      'queue_size_bytes',
      None,
      None))

    def __init__(self, action_stat_type = None, action_type = None, action_pkts = None, action_bytes = None, conform_pkts = None, conform_bytes = None, conform_rate = None, exceed_pkts = None, exceed_bytes = None, exceed_rate = None, violate_pkts = None, violate_bytes = None, violate_rate = None, queue_drop_pkts = None, queue_drop_bytes = None, queue_drop_flows = None, queue_no_buffers = None, queue_out_pkts = None, queue_out_bytes = None, queue_size_pkts = None, queue_size_bytes = None):
        self.action_stat_type = action_stat_type
        self.action_type = action_type
        self.action_pkts = action_pkts
        self.action_bytes = action_bytes
        self.conform_pkts = conform_pkts
        self.conform_bytes = conform_bytes
        self.conform_rate = conform_rate
        self.exceed_pkts = exceed_pkts
        self.exceed_bytes = exceed_bytes
        self.exceed_rate = exceed_rate
        self.violate_pkts = violate_pkts
        self.violate_bytes = violate_bytes
        self.violate_rate = violate_rate
        self.queue_drop_pkts = queue_drop_pkts
        self.queue_drop_bytes = queue_drop_bytes
        self.queue_drop_flows = queue_drop_flows
        self.queue_no_buffers = queue_no_buffers
        self.queue_out_pkts = queue_out_pkts
        self.queue_out_bytes = queue_out_bytes
        self.queue_size_pkts = queue_size_pkts
        self.queue_size_bytes = queue_size_bytes



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
                    self.action_stat_type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.action_type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I64:
                    self.action_pkts = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I64:
                    self.action_bytes = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I64:
                    self.conform_pkts = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I64:
                    self.conform_bytes = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I64:
                    self.conform_rate = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.I64:
                    self.exceed_pkts = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.I64:
                    self.exceed_bytes = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.I64:
                    self.exceed_rate = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.I64:
                    self.violate_pkts = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 12:
                if ftype == TType.I64:
                    self.violate_bytes = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 13:
                if ftype == TType.I64:
                    self.violate_rate = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 14:
                if ftype == TType.I64:
                    self.queue_drop_pkts = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 15:
                if ftype == TType.I64:
                    self.queue_drop_bytes = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 16:
                if ftype == TType.I64:
                    self.queue_drop_flows = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 17:
                if ftype == TType.I64:
                    self.queue_no_buffers = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 18:
                if ftype == TType.I64:
                    self.queue_out_pkts = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 19:
                if ftype == TType.I64:
                    self.queue_out_bytes = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 20:
                if ftype == TType.I64:
                    self.queue_size_pkts = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 21:
                if ftype == TType.I64:
                    self.queue_size_bytes = iprot.readI64()
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
        oprot.writeStructBegin('actionStatsResultIDL')
        if self.action_stat_type != None:
            oprot.writeFieldBegin('action_stat_type', TType.I32, 1)
            oprot.writeI32(self.action_stat_type)
            oprot.writeFieldEnd()
        if self.action_type != None:
            oprot.writeFieldBegin('action_type', TType.I32, 2)
            oprot.writeI32(self.action_type)
            oprot.writeFieldEnd()
        if self.action_pkts != None:
            oprot.writeFieldBegin('action_pkts', TType.I64, 3)
            oprot.writeI64(self.action_pkts)
            oprot.writeFieldEnd()
        if self.action_bytes != None:
            oprot.writeFieldBegin('action_bytes', TType.I64, 4)
            oprot.writeI64(self.action_bytes)
            oprot.writeFieldEnd()
        if self.conform_pkts != None:
            oprot.writeFieldBegin('conform_pkts', TType.I64, 5)
            oprot.writeI64(self.conform_pkts)
            oprot.writeFieldEnd()
        if self.conform_bytes != None:
            oprot.writeFieldBegin('conform_bytes', TType.I64, 6)
            oprot.writeI64(self.conform_bytes)
            oprot.writeFieldEnd()
        if self.conform_rate != None:
            oprot.writeFieldBegin('conform_rate', TType.I64, 7)
            oprot.writeI64(self.conform_rate)
            oprot.writeFieldEnd()
        if self.exceed_pkts != None:
            oprot.writeFieldBegin('exceed_pkts', TType.I64, 8)
            oprot.writeI64(self.exceed_pkts)
            oprot.writeFieldEnd()
        if self.exceed_bytes != None:
            oprot.writeFieldBegin('exceed_bytes', TType.I64, 9)
            oprot.writeI64(self.exceed_bytes)
            oprot.writeFieldEnd()
        if self.exceed_rate != None:
            oprot.writeFieldBegin('exceed_rate', TType.I64, 10)
            oprot.writeI64(self.exceed_rate)
            oprot.writeFieldEnd()
        if self.violate_pkts != None:
            oprot.writeFieldBegin('violate_pkts', TType.I64, 11)
            oprot.writeI64(self.violate_pkts)
            oprot.writeFieldEnd()
        if self.violate_bytes != None:
            oprot.writeFieldBegin('violate_bytes', TType.I64, 12)
            oprot.writeI64(self.violate_bytes)
            oprot.writeFieldEnd()
        if self.violate_rate != None:
            oprot.writeFieldBegin('violate_rate', TType.I64, 13)
            oprot.writeI64(self.violate_rate)
            oprot.writeFieldEnd()
        if self.queue_drop_pkts != None:
            oprot.writeFieldBegin('queue_drop_pkts', TType.I64, 14)
            oprot.writeI64(self.queue_drop_pkts)
            oprot.writeFieldEnd()
        if self.queue_drop_bytes != None:
            oprot.writeFieldBegin('queue_drop_bytes', TType.I64, 15)
            oprot.writeI64(self.queue_drop_bytes)
            oprot.writeFieldEnd()
        if self.queue_drop_flows != None:
            oprot.writeFieldBegin('queue_drop_flows', TType.I64, 16)
            oprot.writeI64(self.queue_drop_flows)
            oprot.writeFieldEnd()
        if self.queue_no_buffers != None:
            oprot.writeFieldBegin('queue_no_buffers', TType.I64, 17)
            oprot.writeI64(self.queue_no_buffers)
            oprot.writeFieldEnd()
        if self.queue_out_pkts != None:
            oprot.writeFieldBegin('queue_out_pkts', TType.I64, 18)
            oprot.writeI64(self.queue_out_pkts)
            oprot.writeFieldEnd()
        if self.queue_out_bytes != None:
            oprot.writeFieldBegin('queue_out_bytes', TType.I64, 19)
            oprot.writeI64(self.queue_out_bytes)
            oprot.writeFieldEnd()
        if self.queue_size_pkts != None:
            oprot.writeFieldBegin('queue_size_pkts', TType.I64, 20)
            oprot.writeI64(self.queue_size_pkts)
            oprot.writeFieldEnd()
        if self.queue_size_bytes != None:
            oprot.writeFieldBegin('queue_size_bytes', TType.I64, 21)
            oprot.writeI64(self.queue_size_bytes)
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




class entryStatsResultIDL(object):
    """
      Entry Stats Result
    
      Attributes:
       - dsid
       - entryHandle
       - opId
       - resultCode
       - time_stamp
       - last_data_time
       - classStatsResult
       - matchStatsResultList
       - actionStatsResultList
      """

    thrift_spec = (None,
     (1,
      TType.I32,
      'dsid',
      None,
      None),
     (2,
      TType.I64,
      'entryHandle',
      None,
      None),
     (3,
      TType.I32,
      'opId',
      None,
      None),
     (4,
      TType.I16,
      'resultCode',
      None,
      None),
     (5,
      TType.I64,
      'time_stamp',
      None,
      None),
     (6,
      TType.I32,
      'last_data_time',
      None,
      None),
     (7,
      TType.STRUCT,
      'classStatsResult',
      (classStatsResultIDL, classStatsResultIDL.thrift_spec),
      None),
     (8,
      TType.LIST,
      'matchStatsResultList',
      (TType.STRUCT, (matchStatsResultIDL, matchStatsResultIDL.thrift_spec)),
      None),
     (9,
      TType.LIST,
      'actionStatsResultList',
      (TType.STRUCT, (actionStatsResultIDL, actionStatsResultIDL.thrift_spec)),
      None))

    def __init__(self, dsid = None, entryHandle = None, opId = None, resultCode = None, time_stamp = None, last_data_time = None, classStatsResult = None, matchStatsResultList = None, actionStatsResultList = None):
        self.dsid = dsid
        self.entryHandle = entryHandle
        self.opId = opId
        self.resultCode = resultCode
        self.time_stamp = time_stamp
        self.last_data_time = last_data_time
        self.classStatsResult = classStatsResult
        self.matchStatsResultList = matchStatsResultList
        self.actionStatsResultList = actionStatsResultList



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
                    self.entryHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.opId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I16:
                    self.resultCode = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I64:
                    self.time_stamp = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I32:
                    self.last_data_time = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.STRUCT:
                    self.classStatsResult = classStatsResultIDL()
                    self.classStatsResult.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.LIST:
                    self.matchStatsResultList = []
                    (_etype3, _size0,) = iprot.readListBegin()
                    for _i4 in xrange(_size0):
                        _elem5 = matchStatsResultIDL()
                        _elem5.read(iprot)
                        self.matchStatsResultList.append(_elem5)

                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.LIST:
                    self.actionStatsResultList = []
                    (_etype9, _size6,) = iprot.readListBegin()
                    for _i10 in xrange(_size6):
                        _elem11 = actionStatsResultIDL()
                        _elem11.read(iprot)
                        self.actionStatsResultList.append(_elem11)

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
        oprot.writeStructBegin('entryStatsResultIDL')
        if self.dsid != None:
            oprot.writeFieldBegin('dsid', TType.I32, 1)
            oprot.writeI32(self.dsid)
            oprot.writeFieldEnd()
        if self.entryHandle != None:
            oprot.writeFieldBegin('entryHandle', TType.I64, 2)
            oprot.writeI64(self.entryHandle)
            oprot.writeFieldEnd()
        if self.opId != None:
            oprot.writeFieldBegin('opId', TType.I32, 3)
            oprot.writeI32(self.opId)
            oprot.writeFieldEnd()
        if self.resultCode != None:
            oprot.writeFieldBegin('resultCode', TType.I16, 4)
            oprot.writeI16(self.resultCode)
            oprot.writeFieldEnd()
        if self.time_stamp != None:
            oprot.writeFieldBegin('time_stamp', TType.I64, 5)
            oprot.writeI64(self.time_stamp)
            oprot.writeFieldEnd()
        if self.last_data_time != None:
            oprot.writeFieldBegin('last_data_time', TType.I32, 6)
            oprot.writeI32(self.last_data_time)
            oprot.writeFieldEnd()
        if self.classStatsResult != None:
            oprot.writeFieldBegin('classStatsResult', TType.STRUCT, 7)
            self.classStatsResult.write(oprot)
            oprot.writeFieldEnd()
        if self.matchStatsResultList != None:
            oprot.writeFieldBegin('matchStatsResultList', TType.LIST, 8)
            oprot.writeListBegin(TType.STRUCT, len(self.matchStatsResultList))
            for iter12 in self.matchStatsResultList:
                iter12.write(oprot)

            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.actionStatsResultList != None:
            oprot.writeFieldBegin('actionStatsResultList', TType.LIST, 9)
            oprot.writeListBegin(TType.STRUCT, len(self.actionStatsResultList))
            for iter13 in self.actionStatsResultList:
                iter13.write(oprot)

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




class PolicyStatsResultIDL(object):
    """
      Policy Stats Result (sync and async)
    
      Attributes:
       - dsid
       - asyncHandle
       - pmapHandle
       - ifHandle
       - total_count
       - entry_count
       - more
       - entryStatsResultList
      """

    thrift_spec = (None,
     (1,
      TType.I32,
      'dsid',
      None,
      None),
     (2,
      TType.I32,
      'asyncHandle',
      None,
      None),
     (3,
      TType.I64,
      'pmapHandle',
      None,
      None),
     (4,
      TType.LIST,
      'ifHandle',
      (TType.I64, None),
      None),
     (5,
      TType.I32,
      'total_count',
      None,
      None),
     (6,
      TType.I32,
      'entry_count',
      None,
      None),
     (7,
      TType.I32,
      'more',
      None,
      None),
     (8,
      TType.LIST,
      'entryStatsResultList',
      (TType.STRUCT, (entryStatsResultIDL, entryStatsResultIDL.thrift_spec)),
      None))

    def __init__(self, dsid = None, asyncHandle = None, pmapHandle = None, ifHandle = None, total_count = None, entry_count = None, more = None, entryStatsResultList = None):
        self.dsid = dsid
        self.asyncHandle = asyncHandle
        self.pmapHandle = pmapHandle
        self.ifHandle = ifHandle
        self.total_count = total_count
        self.entry_count = entry_count
        self.more = more
        self.entryStatsResultList = entryStatsResultList



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
                if ftype == TType.I32:
                    self.asyncHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I64:
                    self.pmapHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.LIST:
                    self.ifHandle = []
                    (_etype17, _size14,) = iprot.readListBegin()
                    for _i18 in xrange(_size14):
                        _elem19 = iprot.readI64()
                        self.ifHandle.append(_elem19)

                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.total_count = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I32:
                    self.entry_count = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I32:
                    self.more = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.LIST:
                    self.entryStatsResultList = []
                    (_etype23, _size20,) = iprot.readListBegin()
                    for _i24 in xrange(_size20):
                        _elem25 = entryStatsResultIDL()
                        _elem25.read(iprot)
                        self.entryStatsResultList.append(_elem25)

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
        oprot.writeStructBegin('PolicyStatsResultIDL')
        if self.dsid != None:
            oprot.writeFieldBegin('dsid', TType.I32, 1)
            oprot.writeI32(self.dsid)
            oprot.writeFieldEnd()
        if self.asyncHandle != None:
            oprot.writeFieldBegin('asyncHandle', TType.I32, 2)
            oprot.writeI32(self.asyncHandle)
            oprot.writeFieldEnd()
        if self.pmapHandle != None:
            oprot.writeFieldBegin('pmapHandle', TType.I64, 3)
            oprot.writeI64(self.pmapHandle)
            oprot.writeFieldEnd()
        if self.ifHandle != None:
            oprot.writeFieldBegin('ifHandle', TType.LIST, 4)
            oprot.writeListBegin(TType.I64, len(self.ifHandle))
            for iter26 in self.ifHandle:
                oprot.writeI64(iter26)

            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.total_count != None:
            oprot.writeFieldBegin('total_count', TType.I32, 5)
            oprot.writeI32(self.total_count)
            oprot.writeFieldEnd()
        if self.entry_count != None:
            oprot.writeFieldBegin('entry_count', TType.I32, 6)
            oprot.writeI32(self.entry_count)
            oprot.writeFieldEnd()
        if self.more != None:
            oprot.writeFieldBegin('more', TType.I32, 7)
            oprot.writeI32(self.more)
            oprot.writeFieldEnd()
        if self.entryStatsResultList != None:
            oprot.writeFieldBegin('entryStatsResultList', TType.LIST, 8)
            oprot.writeListBegin(TType.STRUCT, len(self.entryStatsResultList))
            for iter27 in self.entryStatsResultList:
                iter27.write(oprot)

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




class PmapActivateResultIDL(object):
    """
      PMAP Activate Result
    
      Attributes:
       - dsid
       - pmapHandle
       - opId
       - ifHandle
       - zpName
       - resultCode
      """

    thrift_spec = (None,
     (1,
      TType.I32,
      'dsid',
      None,
      None),
     (2,
      TType.I64,
      'pmapHandle',
      None,
      None),
     (3,
      TType.I32,
      'opId',
      None,
      None),
     (4,
      TType.LIST,
      'ifHandle',
      (TType.I64, None),
      None),
     (5,
      TType.LIST,
      'zpName',
      (TType.STRING, None),
      None),
     (6,
      TType.LIST,
      'resultCode',
      (TType.I16, None),
      None))

    def __init__(self, dsid = None, pmapHandle = None, opId = None, ifHandle = None, zpName = None, resultCode = None):
        self.dsid = dsid
        self.pmapHandle = pmapHandle
        self.opId = opId
        self.ifHandle = ifHandle
        self.zpName = zpName
        self.resultCode = resultCode



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
                    self.pmapHandle = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.opId = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.LIST:
                    self.ifHandle = []
                    (_etype31, _size28,) = iprot.readListBegin()
                    for _i32 in xrange(_size28):
                        _elem33 = iprot.readI64()
                        self.ifHandle.append(_elem33)

                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.LIST:
                    self.zpName = []
                    (_etype37, _size34,) = iprot.readListBegin()
                    for _i38 in xrange(_size34):
                        _elem39 = iprot.readString()
                        self.zpName.append(_elem39)

                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.LIST:
                    self.resultCode = []
                    (_etype43, _size40,) = iprot.readListBegin()
                    for _i44 in xrange(_size40):
                        _elem45 = iprot.readI16()
                        self.resultCode.append(_elem45)

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
        oprot.writeStructBegin('PmapActivateResultIDL')
        if self.dsid != None:
            oprot.writeFieldBegin('dsid', TType.I32, 1)
            oprot.writeI32(self.dsid)
            oprot.writeFieldEnd()
        if self.pmapHandle != None:
            oprot.writeFieldBegin('pmapHandle', TType.I64, 2)
            oprot.writeI64(self.pmapHandle)
            oprot.writeFieldEnd()
        if self.opId != None:
            oprot.writeFieldBegin('opId', TType.I32, 3)
            oprot.writeI32(self.opId)
            oprot.writeFieldEnd()
        if self.ifHandle != None:
            oprot.writeFieldBegin('ifHandle', TType.LIST, 4)
            oprot.writeListBegin(TType.I64, len(self.ifHandle))
            for iter46 in self.ifHandle:
                oprot.writeI64(iter46)

            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.zpName != None:
            oprot.writeFieldBegin('zpName', TType.LIST, 5)
            oprot.writeListBegin(TType.STRING, len(self.zpName))
            for iter47 in self.zpName:
                oprot.writeString(iter47)

            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.resultCode != None:
            oprot.writeFieldBegin('resultCode', TType.LIST, 6)
            oprot.writeListBegin(TType.I16, len(self.resultCode))
            for iter48 in self.resultCode:
                oprot.writeI16(iter48)

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




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:19:38 IST
