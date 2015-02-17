# 2015.02.05 17:20:54 IST
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

    def cs_containernew_IDL(self, sessionHandle, macID):
        """
        Parameters:
         - sessionHandle
         - macID
        """
        pass



    def get_container_profile_IDL(self, containerId):
        """
        Parameters:
         - containerId
        """
        pass



    def cs_get_dns_list_IDL(self, containerId):
        """
        Parameters:
         - containerId
        """
        pass



    def cs_get_net_addr_info_list_IDL(self, containerID, interfaceid):
        """
        Parameters:
         - containerID
         - interfaceid
        """
        pass



    def cs_callback_registration_IDL(self, containerID, cbtype, adding):
        """
        Parameters:
         - containerID
         - cbtype
         - adding
        """
        pass



    def cs_reply_notification_result_IDL(self, containerID, cbtype, notif_success):
        """
        Parameters:
         - containerID
         - cbtype
         - notif_success
        """
        pass



    def cs_reply_addr_information_result_IDL(self, containerID, cbtype, returncode, transactionID, nettype, count, netlist):
        """
        Parameters:
         - containerID
         - cbtype
         - returncode
         - transactionID
         - nettype
         - count
         - netlist
        """
        pass



    def cs_reply_string_information_result_IDL(self, containerID, cbtype, returncode, transactionID, str1):
        """
        Parameters:
         - containerID
         - cbtype
         - returncode
         - transactionID
         - str1
        """
        pass



    def cs_ext_request_IDL(self, containerID, req_info):
        """
        Parameters:
         - containerID
         - req_info
        """
        pass



    def cs_ext_guest_reply_IDL(self, containerID, transactionID, reply_info):
        """
        Parameters:
         - containerID
         - transactionID
         - reply_info
        """
        pass




class Client(Iface):

    def __init__(self, iprot, oprot = None):
        self._iprot = self._oprot = iprot
        if oprot != None:
            self._oprot = oprot
        self._seqid = 0



    def cs_containernew_IDL(self, sessionHandle, macID):
        """
        Parameters:
         - sessionHandle
         - macID
        """
        self._oprot.rlock.acquire()
        try:
            self.send_cs_containernew_IDL(sessionHandle, macID)
            result = self.recv_cs_containernew_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_cs_containernew_IDL(self, sessionHandle, macID):
        self._oprot.writeMessageBegin('cs_containernew_IDL', TMessageType.CALL, self._seqid)
        args = cs_containernew_IDL_args()
        args.sessionHandle = sessionHandle
        args.macID = macID
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_cs_containernew_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = cs_containernew_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'cs_containernew_IDL failed: unknown result')



    def get_container_profile_IDL(self, containerId):
        """
        Parameters:
         - containerId
        """
        self._oprot.rlock.acquire()
        try:
            self.send_get_container_profile_IDL(containerId)
            result = self.recv_get_container_profile_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_get_container_profile_IDL(self, containerId):
        self._oprot.writeMessageBegin('get_container_profile_IDL', TMessageType.CALL, self._seqid)
        args = get_container_profile_IDL_args()
        args.containerId = containerId
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_get_container_profile_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = get_container_profile_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'get_container_profile_IDL failed: unknown result')



    def cs_get_dns_list_IDL(self, containerId):
        """
        Parameters:
         - containerId
        """
        self._oprot.rlock.acquire()
        try:
            self.send_cs_get_dns_list_IDL(containerId)
            result = self.recv_cs_get_dns_list_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_cs_get_dns_list_IDL(self, containerId):
        self._oprot.writeMessageBegin('cs_get_dns_list_IDL', TMessageType.CALL, self._seqid)
        args = cs_get_dns_list_IDL_args()
        args.containerId = containerId
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_cs_get_dns_list_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = cs_get_dns_list_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'cs_get_dns_list_IDL failed: unknown result')



    def cs_get_net_addr_info_list_IDL(self, containerID, interfaceid):
        """
        Parameters:
         - containerID
         - interfaceid
        """
        self._oprot.rlock.acquire()
        try:
            self.send_cs_get_net_addr_info_list_IDL(containerID, interfaceid)
            result = self.recv_cs_get_net_addr_info_list_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_cs_get_net_addr_info_list_IDL(self, containerID, interfaceid):
        self._oprot.writeMessageBegin('cs_get_net_addr_info_list_IDL', TMessageType.CALL, self._seqid)
        args = cs_get_net_addr_info_list_IDL_args()
        args.containerID = containerID
        args.interfaceid = interfaceid
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_cs_get_net_addr_info_list_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = cs_get_net_addr_info_list_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'cs_get_net_addr_info_list_IDL failed: unknown result')



    def cs_callback_registration_IDL(self, containerID, cbtype, adding):
        """
        Parameters:
         - containerID
         - cbtype
         - adding
        """
        self._oprot.rlock.acquire()
        try:
            self.send_cs_callback_registration_IDL(containerID, cbtype, adding)
            result = self.recv_cs_callback_registration_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_cs_callback_registration_IDL(self, containerID, cbtype, adding):
        self._oprot.writeMessageBegin('cs_callback_registration_IDL', TMessageType.CALL, self._seqid)
        args = cs_callback_registration_IDL_args()
        args.containerID = containerID
        args.cbtype = cbtype
        args.adding = adding
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_cs_callback_registration_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = cs_callback_registration_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'cs_callback_registration_IDL failed: unknown result')



    def cs_reply_notification_result_IDL(self, containerID, cbtype, notif_success):
        """
        Parameters:
         - containerID
         - cbtype
         - notif_success
        """
        self._oprot.rlock.acquire()
        try:
            self.send_cs_reply_notification_result_IDL(containerID, cbtype, notif_success)
            result = self.recv_cs_reply_notification_result_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_cs_reply_notification_result_IDL(self, containerID, cbtype, notif_success):
        self._oprot.writeMessageBegin('cs_reply_notification_result_IDL', TMessageType.CALL, self._seqid)
        args = cs_reply_notification_result_IDL_args()
        args.containerID = containerID
        args.cbtype = cbtype
        args.notif_success = notif_success
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_cs_reply_notification_result_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = cs_reply_notification_result_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'cs_reply_notification_result_IDL failed: unknown result')



    def cs_reply_addr_information_result_IDL(self, containerID, cbtype, returncode, transactionID, nettype, count, netlist):
        """
        Parameters:
         - containerID
         - cbtype
         - returncode
         - transactionID
         - nettype
         - count
         - netlist
        """
        self._oprot.rlock.acquire()
        try:
            self.send_cs_reply_addr_information_result_IDL(containerID, cbtype, returncode, transactionID, nettype, count, netlist)
            result = self.recv_cs_reply_addr_information_result_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_cs_reply_addr_information_result_IDL(self, containerID, cbtype, returncode, transactionID, nettype, count, netlist):
        self._oprot.writeMessageBegin('cs_reply_addr_information_result_IDL', TMessageType.CALL, self._seqid)
        args = cs_reply_addr_information_result_IDL_args()
        args.containerID = containerID
        args.cbtype = cbtype
        args.returncode = returncode
        args.transactionID = transactionID
        args.nettype = nettype
        args.count = count
        args.netlist = netlist
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_cs_reply_addr_information_result_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = cs_reply_addr_information_result_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'cs_reply_addr_information_result_IDL failed: unknown result')



    def cs_reply_string_information_result_IDL(self, containerID, cbtype, returncode, transactionID, str1):
        """
        Parameters:
         - containerID
         - cbtype
         - returncode
         - transactionID
         - str1
        """
        self._oprot.rlock.acquire()
        try:
            self.send_cs_reply_string_information_result_IDL(containerID, cbtype, returncode, transactionID, str1)
            result = self.recv_cs_reply_string_information_result_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_cs_reply_string_information_result_IDL(self, containerID, cbtype, returncode, transactionID, str1):
        self._oprot.writeMessageBegin('cs_reply_string_information_result_IDL', TMessageType.CALL, self._seqid)
        args = cs_reply_string_information_result_IDL_args()
        args.containerID = containerID
        args.cbtype = cbtype
        args.returncode = returncode
        args.transactionID = transactionID
        args.str1 = str1
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_cs_reply_string_information_result_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = cs_reply_string_information_result_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'cs_reply_string_information_result_IDL failed: unknown result')



    def cs_ext_request_IDL(self, containerID, req_info):
        """
        Parameters:
         - containerID
         - req_info
        """
        self._oprot.rlock.acquire()
        try:
            self.send_cs_ext_request_IDL(containerID, req_info)
            result = self.recv_cs_ext_request_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_cs_ext_request_IDL(self, containerID, req_info):
        self._oprot.writeMessageBegin('cs_ext_request_IDL', TMessageType.CALL, self._seqid)
        args = cs_ext_request_IDL_args()
        args.containerID = containerID
        args.req_info = req_info
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_cs_ext_request_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = cs_ext_request_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'cs_ext_request_IDL failed: unknown result')



    def cs_ext_guest_reply_IDL(self, containerID, transactionID, reply_info):
        """
        Parameters:
         - containerID
         - transactionID
         - reply_info
        """
        self._oprot.rlock.acquire()
        try:
            self.send_cs_ext_guest_reply_IDL(containerID, transactionID, reply_info)
            result = self.recv_cs_ext_guest_reply_IDL()
        except Exception as e:
            self._oprot.rlock.release()
            raise e
        self._oprot.rlock.release()
        return result



    def send_cs_ext_guest_reply_IDL(self, containerID, transactionID, reply_info):
        self._oprot.writeMessageBegin('cs_ext_guest_reply_IDL', TMessageType.CALL, self._seqid)
        args = cs_ext_guest_reply_IDL_args()
        args.containerID = containerID
        args.transactionID = transactionID
        args.reply_info = reply_info
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()



    def recv_cs_ext_guest_reply_IDL(self):
        (fname, mtype, rseqid,) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = cs_ext_guest_reply_IDL_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success != None:
            return result.success
        if result.e != None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, 'cs_ext_guest_reply_IDL failed: unknown result')




class Processor(Iface, TProcessor):

    def __init__(self, handler):
        self._handler = handler
        self._processMap = {}
        self._processMap['cs_containernew_IDL'] = Processor.process_cs_containernew_IDL
        self._processMap['get_container_profile_IDL'] = Processor.process_get_container_profile_IDL
        self._processMap['cs_get_dns_list_IDL'] = Processor.process_cs_get_dns_list_IDL
        self._processMap['cs_get_net_addr_info_list_IDL'] = Processor.process_cs_get_net_addr_info_list_IDL
        self._processMap['cs_callback_registration_IDL'] = Processor.process_cs_callback_registration_IDL
        self._processMap['cs_reply_notification_result_IDL'] = Processor.process_cs_reply_notification_result_IDL
        self._processMap['cs_reply_addr_information_result_IDL'] = Processor.process_cs_reply_addr_information_result_IDL
        self._processMap['cs_reply_string_information_result_IDL'] = Processor.process_cs_reply_string_information_result_IDL
        self._processMap['cs_ext_request_IDL'] = Processor.process_cs_ext_request_IDL
        self._processMap['cs_ext_guest_reply_IDL'] = Processor.process_cs_ext_guest_reply_IDL



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



    def process_cs_containernew_IDL(self, seqid, iprot, oprot):
        args = cs_containernew_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = cs_containernew_IDL_result()
        try:
            result.success = self._handler.cs_containernew_IDL(args.sessionHandle, args.macID)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('cs_containernew_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_get_container_profile_IDL(self, seqid, iprot, oprot):
        args = get_container_profile_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = get_container_profile_IDL_result()
        try:
            result.success = self._handler.get_container_profile_IDL(args.containerId)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('get_container_profile_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_cs_get_dns_list_IDL(self, seqid, iprot, oprot):
        args = cs_get_dns_list_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = cs_get_dns_list_IDL_result()
        try:
            result.success = self._handler.cs_get_dns_list_IDL(args.containerId)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('cs_get_dns_list_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_cs_get_net_addr_info_list_IDL(self, seqid, iprot, oprot):
        args = cs_get_net_addr_info_list_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = cs_get_net_addr_info_list_IDL_result()
        try:
            result.success = self._handler.cs_get_net_addr_info_list_IDL(args.containerID, args.interfaceid)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('cs_get_net_addr_info_list_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_cs_callback_registration_IDL(self, seqid, iprot, oprot):
        args = cs_callback_registration_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = cs_callback_registration_IDL_result()
        try:
            result.success = self._handler.cs_callback_registration_IDL(args.containerID, args.cbtype, args.adding)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('cs_callback_registration_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_cs_reply_notification_result_IDL(self, seqid, iprot, oprot):
        args = cs_reply_notification_result_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = cs_reply_notification_result_IDL_result()
        try:
            result.success = self._handler.cs_reply_notification_result_IDL(args.containerID, args.cbtype, args.notif_success)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('cs_reply_notification_result_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_cs_reply_addr_information_result_IDL(self, seqid, iprot, oprot):
        args = cs_reply_addr_information_result_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = cs_reply_addr_information_result_IDL_result()
        try:
            result.success = self._handler.cs_reply_addr_information_result_IDL(args.containerID, args.cbtype, args.returncode, args.transactionID, args.nettype, args.count, args.netlist)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('cs_reply_addr_information_result_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_cs_reply_string_information_result_IDL(self, seqid, iprot, oprot):
        args = cs_reply_string_information_result_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = cs_reply_string_information_result_IDL_result()
        try:
            result.success = self._handler.cs_reply_string_information_result_IDL(args.containerID, args.cbtype, args.returncode, args.transactionID, args.str1)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('cs_reply_string_information_result_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_cs_ext_request_IDL(self, seqid, iprot, oprot):
        args = cs_ext_request_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = cs_ext_request_IDL_result()
        try:
            result.success = self._handler.cs_ext_request_IDL(args.containerID, args.req_info)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('cs_ext_request_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()



    def process_cs_ext_guest_reply_IDL(self, seqid, iprot, oprot):
        args = cs_ext_guest_reply_IDL_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = cs_ext_guest_reply_IDL_result()
        try:
            result.success = self._handler.cs_ext_guest_reply_IDL(args.containerID, args.transactionID, args.reply_info)
        except Shared.ttypes.ExceptionIDL as e:
            result.e = e
        oprot.writeMessageBegin('cs_ext_guest_reply_IDL', TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()




class cs_containernew_IDL_args(object):
    """
    Attributes:
     - sessionHandle
     - macID
    """

    thrift_spec = (None, (1,
      TType.I32,
      'sessionHandle',
      None,
      None), (2,
      TType.STRUCT,
      'macID',
      (CS_mac_id_IDL, CS_mac_id_IDL.thrift_spec),
      None))

    def __init__(self, sessionHandle = None, macID = None):
        self.sessionHandle = sessionHandle
        self.macID = macID



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
                    self.sessionHandle = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.macID = CS_mac_id_IDL()
                    self.macID.read(iprot)
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
        oprot.writeStructBegin('cs_containernew_IDL_args')
        if self.sessionHandle != None:
            oprot.writeFieldBegin('sessionHandle', TType.I32, 1)
            oprot.writeI32(self.sessionHandle)
            oprot.writeFieldEnd()
        if self.macID != None:
            oprot.writeFieldBegin('macID', TType.STRUCT, 2)
            self.macID.write(oprot)
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




class cs_containernew_IDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.I32,
      'success',
      None,
      None), (1,
      TType.STRUCT,
      'e',
      (Shared.ttypes.ExceptionIDL, Shared.ttypes.ExceptionIDL.thrift_spec),
      None))

    def __init__(self, success = None, e = None):
        self.success = success
        self.e = e



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.I32:
                    self.success = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = Shared.ttypes.ExceptionIDL()
                    self.e.read(iprot)
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
        oprot.writeStructBegin('cs_containernew_IDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.I32, 0)
            oprot.writeI32(self.success)
            oprot.writeFieldEnd()
        if self.e != None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
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




class get_container_profile_IDL_args(object):
    """
    Attributes:
     - containerId
    """

    thrift_spec = (None, (1,
      TType.I32,
      'containerId',
      None,
      None))

    def __init__(self, containerId = None):
        self.containerId = containerId



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
                    self.containerId = iprot.readI32()
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
        oprot.writeStructBegin('get_container_profile_IDL_args')
        if self.containerId != None:
            oprot.writeFieldBegin('containerId', TType.I32, 1)
            oprot.writeI32(self.containerId)
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




class get_container_profile_IDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.STRUCT,
      'success',
      (CS_profile_info_IDL, CS_profile_info_IDL.thrift_spec),
      None), (1,
      TType.STRUCT,
      'e',
      (Shared.ttypes.ExceptionIDL, Shared.ttypes.ExceptionIDL.thrift_spec),
      None))

    def __init__(self, success = None, e = None):
        self.success = success
        self.e = e



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = CS_profile_info_IDL()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = Shared.ttypes.ExceptionIDL()
                    self.e.read(iprot)
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
        oprot.writeStructBegin('get_container_profile_IDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e != None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
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




class cs_get_dns_list_IDL_args(object):
    """
    Attributes:
     - containerId
    """

    thrift_spec = (None, (1,
      TType.I32,
      'containerId',
      None,
      None))

    def __init__(self, containerId = None):
        self.containerId = containerId



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
                    self.containerId = iprot.readI32()
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
        oprot.writeStructBegin('cs_get_dns_list_IDL_args')
        if self.containerId != None:
            oprot.writeFieldBegin('containerId', TType.I32, 1)
            oprot.writeI32(self.containerId)
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




class cs_get_dns_list_IDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.LIST,
      'success',
      (TType.STRUCT, (Shared.ttypes.NetworkAddressIDL, Shared.ttypes.NetworkAddressIDL.thrift_spec)),
      None), (1,
      TType.STRUCT,
      'e',
      (Shared.ttypes.ExceptionIDL, Shared.ttypes.ExceptionIDL.thrift_spec),
      None))

    def __init__(self, success = None, e = None):
        self.success = success
        self.e = e



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.LIST:
                    self.success = []
                    (_etype24, _size21,) = iprot.readListBegin()
                    for _i25 in xrange(_size21):
                        _elem26 = Shared.ttypes.NetworkAddressIDL()
                        _elem26.read(iprot)
                        self.success.append(_elem26)

                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = Shared.ttypes.ExceptionIDL()
                    self.e.read(iprot)
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
        oprot.writeStructBegin('cs_get_dns_list_IDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.STRUCT, len(self.success))
            for iter27 in self.success:
                iter27.write(oprot)

            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.e != None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
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




class cs_get_net_addr_info_list_IDL_args(object):
    """
    Attributes:
     - containerID
     - interfaceid
    """

    thrift_spec = (None, (1,
      TType.I32,
      'containerID',
      None,
      None), (2,
      TType.STRUCT,
      'interfaceid',
      (CS_mac_id_IDL, CS_mac_id_IDL.thrift_spec),
      None))

    def __init__(self, containerID = None, interfaceid = None):
        self.containerID = containerID
        self.interfaceid = interfaceid



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
                    self.containerID = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.interfaceid = CS_mac_id_IDL()
                    self.interfaceid.read(iprot)
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
        oprot.writeStructBegin('cs_get_net_addr_info_list_IDL_args')
        if self.containerID != None:
            oprot.writeFieldBegin('containerID', TType.I32, 1)
            oprot.writeI32(self.containerID)
            oprot.writeFieldEnd()
        if self.interfaceid != None:
            oprot.writeFieldBegin('interfaceid', TType.STRUCT, 2)
            self.interfaceid.write(oprot)
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




class cs_get_net_addr_info_list_IDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.LIST,
      'success',
      (TType.STRUCT, (CS_network_config_IDL, CS_network_config_IDL.thrift_spec)),
      None), (1,
      TType.STRUCT,
      'e',
      (Shared.ttypes.ExceptionIDL, Shared.ttypes.ExceptionIDL.thrift_spec),
      None))

    def __init__(self, success = None, e = None):
        self.success = success
        self.e = e



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.LIST:
                    self.success = []
                    (_etype31, _size28,) = iprot.readListBegin()
                    for _i32 in xrange(_size28):
                        _elem33 = CS_network_config_IDL()
                        _elem33.read(iprot)
                        self.success.append(_elem33)

                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = Shared.ttypes.ExceptionIDL()
                    self.e.read(iprot)
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
        oprot.writeStructBegin('cs_get_net_addr_info_list_IDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.STRUCT, len(self.success))
            for iter34 in self.success:
                iter34.write(oprot)

            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.e != None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
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




class cs_callback_registration_IDL_args(object):
    """
    Attributes:
     - containerID
     - cbtype
     - adding
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'containerID',
      None,
      None),
     (2,
      TType.I32,
      'cbtype',
      None,
      None),
     (3,
      TType.I32,
      'adding',
      None,
      None))

    def __init__(self, containerID = None, cbtype = None, adding = None):
        self.containerID = containerID
        self.cbtype = cbtype
        self.adding = adding



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
                    self.containerID = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.cbtype = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.adding = iprot.readI32()
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
        oprot.writeStructBegin('cs_callback_registration_IDL_args')
        if self.containerID != None:
            oprot.writeFieldBegin('containerID', TType.I32, 1)
            oprot.writeI32(self.containerID)
            oprot.writeFieldEnd()
        if self.cbtype != None:
            oprot.writeFieldBegin('cbtype', TType.I32, 2)
            oprot.writeI32(self.cbtype)
            oprot.writeFieldEnd()
        if self.adding != None:
            oprot.writeFieldBegin('adding', TType.I32, 3)
            oprot.writeI32(self.adding)
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




class cs_callback_registration_IDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.I32,
      'success',
      None,
      None), (1,
      TType.STRUCT,
      'e',
      (Shared.ttypes.ExceptionIDL, Shared.ttypes.ExceptionIDL.thrift_spec),
      None))

    def __init__(self, success = None, e = None):
        self.success = success
        self.e = e



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.I32:
                    self.success = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = Shared.ttypes.ExceptionIDL()
                    self.e.read(iprot)
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
        oprot.writeStructBegin('cs_callback_registration_IDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.I32, 0)
            oprot.writeI32(self.success)
            oprot.writeFieldEnd()
        if self.e != None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
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




class cs_reply_notification_result_IDL_args(object):
    """
    Attributes:
     - containerID
     - cbtype
     - notif_success
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'containerID',
      None,
      None),
     (2,
      TType.I32,
      'cbtype',
      None,
      None),
     (3,
      TType.I32,
      'notif_success',
      None,
      None))

    def __init__(self, containerID = None, cbtype = None, notif_success = None):
        self.containerID = containerID
        self.cbtype = cbtype
        self.notif_success = notif_success



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
                    self.containerID = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.cbtype = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.notif_success = iprot.readI32()
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
        oprot.writeStructBegin('cs_reply_notification_result_IDL_args')
        if self.containerID != None:
            oprot.writeFieldBegin('containerID', TType.I32, 1)
            oprot.writeI32(self.containerID)
            oprot.writeFieldEnd()
        if self.cbtype != None:
            oprot.writeFieldBegin('cbtype', TType.I32, 2)
            oprot.writeI32(self.cbtype)
            oprot.writeFieldEnd()
        if self.notif_success != None:
            oprot.writeFieldBegin('notif_success', TType.I32, 3)
            oprot.writeI32(self.notif_success)
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




class cs_reply_notification_result_IDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.I32,
      'success',
      None,
      None), (1,
      TType.STRUCT,
      'e',
      (Shared.ttypes.ExceptionIDL, Shared.ttypes.ExceptionIDL.thrift_spec),
      None))

    def __init__(self, success = None, e = None):
        self.success = success
        self.e = e



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.I32:
                    self.success = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = Shared.ttypes.ExceptionIDL()
                    self.e.read(iprot)
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
        oprot.writeStructBegin('cs_reply_notification_result_IDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.I32, 0)
            oprot.writeI32(self.success)
            oprot.writeFieldEnd()
        if self.e != None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
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




class cs_reply_addr_information_result_IDL_args(object):
    """
    Attributes:
     - containerID
     - cbtype
     - returncode
     - transactionID
     - nettype
     - count
     - netlist
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'containerID',
      None,
      None),
     (2,
      TType.I32,
      'cbtype',
      None,
      None),
     (3,
      TType.I32,
      'returncode',
      None,
      None),
     (4,
      TType.I32,
      'transactionID',
      None,
      None),
     (5,
      TType.I32,
      'nettype',
      None,
      None),
     (6,
      TType.I32,
      'count',
      None,
      None),
     (7,
      TType.STRUCT,
      'netlist',
      (CS_netlist_IDL, CS_netlist_IDL.thrift_spec),
      None))

    def __init__(self, containerID = None, cbtype = None, returncode = None, transactionID = None, nettype = None, count = None, netlist = None):
        self.containerID = containerID
        self.cbtype = cbtype
        self.returncode = returncode
        self.transactionID = transactionID
        self.nettype = nettype
        self.count = count
        self.netlist = netlist



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
                    self.containerID = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.cbtype = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.returncode = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.transactionID = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.nettype = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I32:
                    self.count = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.STRUCT:
                    self.netlist = CS_netlist_IDL()
                    self.netlist.read(iprot)
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
        oprot.writeStructBegin('cs_reply_addr_information_result_IDL_args')
        if self.containerID != None:
            oprot.writeFieldBegin('containerID', TType.I32, 1)
            oprot.writeI32(self.containerID)
            oprot.writeFieldEnd()
        if self.cbtype != None:
            oprot.writeFieldBegin('cbtype', TType.I32, 2)
            oprot.writeI32(self.cbtype)
            oprot.writeFieldEnd()
        if self.returncode != None:
            oprot.writeFieldBegin('returncode', TType.I32, 3)
            oprot.writeI32(self.returncode)
            oprot.writeFieldEnd()
        if self.transactionID != None:
            oprot.writeFieldBegin('transactionID', TType.I32, 4)
            oprot.writeI32(self.transactionID)
            oprot.writeFieldEnd()
        if self.nettype != None:
            oprot.writeFieldBegin('nettype', TType.I32, 5)
            oprot.writeI32(self.nettype)
            oprot.writeFieldEnd()
        if self.count != None:
            oprot.writeFieldBegin('count', TType.I32, 6)
            oprot.writeI32(self.count)
            oprot.writeFieldEnd()
        if self.netlist != None:
            oprot.writeFieldBegin('netlist', TType.STRUCT, 7)
            self.netlist.write(oprot)
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




class cs_reply_addr_information_result_IDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.I32,
      'success',
      None,
      None), (1,
      TType.STRUCT,
      'e',
      (Shared.ttypes.ExceptionIDL, Shared.ttypes.ExceptionIDL.thrift_spec),
      None))

    def __init__(self, success = None, e = None):
        self.success = success
        self.e = e



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.I32:
                    self.success = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = Shared.ttypes.ExceptionIDL()
                    self.e.read(iprot)
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
        oprot.writeStructBegin('cs_reply_addr_information_result_IDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.I32, 0)
            oprot.writeI32(self.success)
            oprot.writeFieldEnd()
        if self.e != None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
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




class cs_reply_string_information_result_IDL_args(object):
    """
    Attributes:
     - containerID
     - cbtype
     - returncode
     - transactionID
     - str1
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'containerID',
      None,
      None),
     (2,
      TType.I32,
      'cbtype',
      None,
      None),
     (3,
      TType.I32,
      'returncode',
      None,
      None),
     (4,
      TType.I32,
      'transactionID',
      None,
      None),
     (5,
      TType.STRING,
      'str1',
      None,
      None))

    def __init__(self, containerID = None, cbtype = None, returncode = None, transactionID = None, str1 = None):
        self.containerID = containerID
        self.cbtype = cbtype
        self.returncode = returncode
        self.transactionID = transactionID
        self.str1 = str1



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
                    self.containerID = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.cbtype = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.returncode = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.transactionID = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.str1 = iprot.readString()
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
        oprot.writeStructBegin('cs_reply_string_information_result_IDL_args')
        if self.containerID != None:
            oprot.writeFieldBegin('containerID', TType.I32, 1)
            oprot.writeI32(self.containerID)
            oprot.writeFieldEnd()
        if self.cbtype != None:
            oprot.writeFieldBegin('cbtype', TType.I32, 2)
            oprot.writeI32(self.cbtype)
            oprot.writeFieldEnd()
        if self.returncode != None:
            oprot.writeFieldBegin('returncode', TType.I32, 3)
            oprot.writeI32(self.returncode)
            oprot.writeFieldEnd()
        if self.transactionID != None:
            oprot.writeFieldBegin('transactionID', TType.I32, 4)
            oprot.writeI32(self.transactionID)
            oprot.writeFieldEnd()
        if self.str1 != None:
            oprot.writeFieldBegin('str1', TType.STRING, 5)
            oprot.writeString(self.str1)
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




class cs_reply_string_information_result_IDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.I32,
      'success',
      None,
      None), (1,
      TType.STRUCT,
      'e',
      (Shared.ttypes.ExceptionIDL, Shared.ttypes.ExceptionIDL.thrift_spec),
      None))

    def __init__(self, success = None, e = None):
        self.success = success
        self.e = e



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.I32:
                    self.success = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = Shared.ttypes.ExceptionIDL()
                    self.e.read(iprot)
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
        oprot.writeStructBegin('cs_reply_string_information_result_IDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.I32, 0)
            oprot.writeI32(self.success)
            oprot.writeFieldEnd()
        if self.e != None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
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




class cs_ext_request_IDL_args(object):
    """
    Attributes:
     - containerID
     - req_info
    """

    thrift_spec = (None, (1,
      TType.I32,
      'containerID',
      None,
      None), (2,
      TType.STRUCT,
      'req_info',
      (CS_ext_guest_request_param_IDL, CS_ext_guest_request_param_IDL.thrift_spec),
      None))

    def __init__(self, containerID = None, req_info = None):
        self.containerID = containerID
        self.req_info = req_info



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
                    self.containerID = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.req_info = CS_ext_guest_request_param_IDL()
                    self.req_info.read(iprot)
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
        oprot.writeStructBegin('cs_ext_request_IDL_args')
        if self.containerID != None:
            oprot.writeFieldBegin('containerID', TType.I32, 1)
            oprot.writeI32(self.containerID)
            oprot.writeFieldEnd()
        if self.req_info != None:
            oprot.writeFieldBegin('req_info', TType.STRUCT, 2)
            self.req_info.write(oprot)
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




class cs_ext_request_IDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.STRUCT,
      'success',
      (CS_ext_host_info_IDL, CS_ext_host_info_IDL.thrift_spec),
      None), (1,
      TType.STRUCT,
      'e',
      (Shared.ttypes.ExceptionIDL, Shared.ttypes.ExceptionIDL.thrift_spec),
      None))

    def __init__(self, success = None, e = None):
        self.success = success
        self.e = e



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = CS_ext_host_info_IDL()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = Shared.ttypes.ExceptionIDL()
                    self.e.read(iprot)
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
        oprot.writeStructBegin('cs_ext_request_IDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e != None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
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




class cs_ext_guest_reply_IDL_args(object):
    """
    Attributes:
     - containerID
     - transactionID
     - reply_info
    """

    thrift_spec = (None,
     (1,
      TType.I32,
      'containerID',
      None,
      None),
     (2,
      TType.I32,
      'transactionID',
      None,
      None),
     (3,
      TType.LIST,
      'reply_info',
      (TType.STRUCT, (CS_ext_guest_reply_IDL, CS_ext_guest_reply_IDL.thrift_spec)),
      None))

    def __init__(self, containerID = None, transactionID = None, reply_info = None):
        self.containerID = containerID
        self.transactionID = transactionID
        self.reply_info = reply_info



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
                    self.containerID = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.transactionID = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.LIST:
                    self.reply_info = []
                    (_etype38, _size35,) = iprot.readListBegin()
                    for _i39 in xrange(_size35):
                        _elem40 = CS_ext_guest_reply_IDL()
                        _elem40.read(iprot)
                        self.reply_info.append(_elem40)

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
        oprot.writeStructBegin('cs_ext_guest_reply_IDL_args')
        if self.containerID != None:
            oprot.writeFieldBegin('containerID', TType.I32, 1)
            oprot.writeI32(self.containerID)
            oprot.writeFieldEnd()
        if self.transactionID != None:
            oprot.writeFieldBegin('transactionID', TType.I32, 2)
            oprot.writeI32(self.transactionID)
            oprot.writeFieldEnd()
        if self.reply_info != None:
            oprot.writeFieldBegin('reply_info', TType.LIST, 3)
            oprot.writeListBegin(TType.STRUCT, len(self.reply_info))
            for iter41 in self.reply_info:
                iter41.write(oprot)

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




class cs_ext_guest_reply_IDL_result(object):
    """
    Attributes:
     - success
     - e
    """

    thrift_spec = ((0,
      TType.I32,
      'success',
      None,
      None), (1,
      TType.STRUCT,
      'e',
      (Shared.ttypes.ExceptionIDL, Shared.ttypes.ExceptionIDL.thrift_spec),
      None))

    def __init__(self, success = None, e = None):
        self.success = success
        self.e = e



    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return 
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid,) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.I32:
                    self.success = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = Shared.ttypes.ExceptionIDL()
                    self.e.read(iprot)
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
        oprot.writeStructBegin('cs_ext_guest_reply_IDL_result')
        if self.success != None:
            oprot.writeFieldBegin('success', TType.I32, 0)
            oprot.writeI32(self.success)
            oprot.writeFieldEnd()
        if self.e != None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
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
# 2015.02.05 17:20:56 IST
