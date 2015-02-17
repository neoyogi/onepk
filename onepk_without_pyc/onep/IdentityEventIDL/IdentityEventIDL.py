# 2015.02.05 17:21:17 IST
from thrift.Thrift import *
from ttypes import *
from thrift.Thrift import TProcessor
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
    from thrift.protocol import fastbinary
except:
    fastbinary = None

class Iface(object):

    def OnepEvent_IdenNotificationIDL(self, event_id, sess_label, notify_attr_list):
        """
        Parameters:
         - event_id
         - sess_label
         - notify_attr_list
        """
        pass




class Client(Iface):

    def __init__(self, iprot, oprot = None):
        self._iprot = self._oprot = iprot
        if oprot != None:
            self._oprot = oprot
        self._seqid = 0



    def OnepEvent_IdenNotificationIDL(self, event_id, sess_label, notify_attr_list):
        """
        Parameters:
         - event_id
         - sess_label
         - notify_attr_list
        """
        self._oprot.rlock.acquire()
        try:
            self.send_OnepEvent_IdenNotificationIDL(event_id, sess_label, notify_attr_list)
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()



    def send_OnepEvent_IdenNotificationIDL(self, event_id, sess_label, notify_attr_list):
        self._oprot.writeMessageBegin('OnepEvent_IdenNotificationIDL', TMessageType.CALL, self._seqid)
        args = OnepEvent_IdenNotificationIDL_args()
        args.event_id = event_id
        args.sess_label = sess_label
        args.notify_attr_list = notify_attr_list
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()




class Processor(Iface, TProcessor):

    def __init__(self, handler):
        self._handler = handler
        self._processMap = {}
        self._processMap['OnepEvent_IdenNotificationIDL'] = Processor.process_OnepEvent_IdenNotificationIDL



    def process(self, iprot, oprot):
        (name, type, seqid,) = iprot.readMessageBegin()
        if name not in self._processMap:
            iprot.skip(TType.STRUCT)
            iprot.readMessageEnd()
            x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % name)
            oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
            x.write(oprot)
            oprot.writeMessageEnd()
            oprot.trans.flush()
            return 
        self._processMap[name](self, seqid, iprot, oprot)
        return True



    def process_OnepEvent_IdenNotificationIDL(self, seqid, iprot, oprot):
        args = OnepEvent_IdenNotificationIDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        self._handler.OnepEvent_IdenNotificationIDL(args.event_id, args.sess_label, args.notify_attr_list)




class OnepEvent_IdenNotificationIDL_args(object):
    """
    Attributes:
     - event_id
     - sess_label
     - notify_attr_list
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'event_id',
      None,
      None),
     (2,
      TType.I32,
      'sess_label',
      None,
      None),
     (3,
      TType.LIST,
      'notify_attr_list',
      (TType.STRUCT, (AttributeOutIDL, AttributeOutIDL.thrift_spec)),
      None))

    def __init__(self, event_id = None, sess_label = None, notify_attr_list = None):
        self.event_id = event_id
        self.sess_label = sess_label
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
                if ftype == TType.I32:
                    self.event_id = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.sess_label = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.LIST:
                    self.notify_attr_list = []
                    (_etype10, _size7,) = iprot.readListBegin()
                    for _i11 in xrange(_size7):
                        _elem12 = AttributeOutIDL()
                        _elem12.read(iprot)
                        self.notify_attr_list.append(_elem12)

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
        oprot.writeStructBegin('OnepEvent_IdenNotificationIDL_args')
        if self.event_id != None:
            oprot.writeFieldBegin('event_id', TType.I32, 1)
            oprot.writeI32(self.event_id)
            oprot.writeFieldEnd()
        if self.sess_label != None:
            oprot.writeFieldBegin('sess_label', TType.I32, 2)
            oprot.writeI32(self.sess_label)
            oprot.writeFieldEnd()
        if self.notify_attr_list != None:
            oprot.writeFieldBegin('notify_attr_list', TType.LIST, 3)
            oprot.writeListBegin(TType.STRUCT, len(self.notify_attr_list))
            for iter13 in self.notify_attr_list:
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




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:21:17 IST
