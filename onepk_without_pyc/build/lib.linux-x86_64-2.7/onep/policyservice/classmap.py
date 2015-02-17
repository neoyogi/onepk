# 2015.02.05 17:19:55 IST
from onep.policyservice.caps import PolicyCapabilities
from onep.policyservice.caps import PolicyCapabilitiesType
from onep.PolicyBulkIDL.ttypes import CmapIDL
from onep.PolicyBulkIDL.ttypes import PolicyFilterIDL
from onep.policyservice import match
from onep.core.util.OnepArgumentTypeValidate import *
from onep.core.exception.OnepIllegalArgumentException import OnepIllegalArgumentException
from onep.core.exception.OnepException import OnepNotSupportedException
import logging
import types
from onep.core.util.OnepStatus import OnepStatus
from onep.core.util.Enum import enum
from onep.policyservice import StorageType
from abc import ABCMeta, abstractmethod
from onep.core.event.EventListener import EventListener
from onep.core.event.AsyncMsg import AsyncMsg

class ClassMap(object):
    """ ClassMap class.
    
    This class contains a hierarchy of matches that define class map.
    
    The ClassMap object is created with specified PolicyCapability and may be associated with one or more targets.
    
    Adding and removing Match(es) from this class will result in the local copy's Match(es) being removed.
     
    If the corresponding ClassMap requires that the Network Element's require changes, 
    then the class BulkServices must be use to submit those changes 
    or else those changes will not be noted on the Network Element.
    
    @undocumented: get_match_list
    @undocumented: name
    
    """


    def _get_capabilities(self):
        return self._capabilities


    _doc_capabilities = ' Capabilities.\n    \n    @type: L{PolicyCapabilities<onep.policyservice.PolicyCapabilities.PolicyCapabilities>}     \n    '
    capabilities = property(_get_capabilities, None, None, _doc_capabilities)

    def _set_match_all(self, match_all):
        try:
            validate(match_all, bool)
        except OnepIllegalArgumentException as e:
            raise e
        self._match_all = match_all



    def _get_match_all(self):
        return self._match_all


    _doc_match_all = ' Match criteria.\n    \n    Property determines how packets are evaluated when multiple match criteria exist.\n    \n    If set to true, matches in this class map will be based on the logical AND function, \n    otherwise matches will be based on the logical OR function.\n    \n    Default Value of property: True\n    \n    Raises: OnepIllegalArgumentException - If match_all value is invalid.\n        \n    @type: C{bool}\n    '
    match_all = property(_get_match_all, _set_match_all, None, _doc_match_all)

    def _get_handle(self):
        return self._handle



    def _set_handle(self, handle):
        self._handle = handle


    _doc_handle = ' Class Map handle.\n    \n    @type: C{long}\n    '
    handle = property(_get_handle, _set_handle, None, _doc_handle)

    def __init__(self, capabilities = None, name = None, storage_type = StorageType.TRANSIENT):
        """ Constructs an instance of ClassMap with specified capability.
        
        @param capabilities: Policy Capability.
        @type capabilities: L{PolicyCapabilities<onep.policyservice.PolicyCapabilities.PolicyCapabilities>}
        
        @raise OnepIllegalArgumentException: If constructor parameter is invalid.        
        """
        self.log = logging.getLogger(__name__)
        if capabilities != None:
            validate(capabilities, PolicyCapabilities)
            self._capabilities = capabilities
            self._element = capabilities.network_element
        self._handle = 0
        self._match_all = True
        self.storage_type = storage_type
        self.name = name
        self._match_list = []
        self._op_code = None
        self._result = None
        self.opid = 0


    ClassOperation = enum(ONEP_CLASS_OP_CREATE=0, ONEP_CLASS_OP_MODIFY=1, ONEP_CLASS_OP_DELETE=2, ONEP_CLASS_OP_REP=3, ONEP_CLASS_OP_GET=5)

    @property
    def capabilities(self):
        return self._capabilities



    def _get_result_code(self):
        if self._result:
            resultcode = self._result.resultCode
            for m in self._result.matchResultList:
                if m.result:
                    resultcode = m.result
                    break

            return resultcode
        return self._result


    _doc_result_code = '\n        Gets the value of result code. Code 0 indicates success \n        any other values indicates failure.\n        \n        @type: C{int}\n        '
    result_code = property(_get_result_code, None, None, _doc_result_code)

    def _get_result_text(self):
        if self._result:
            resulttext = OnepStatus.enumval(self._result.resultCode)
            for m in self._result.matchResultList:
                if m.result:
                    resulttext = OnepStatus.enumval(m.result)
                    break

            return resulttext
        return self._result


    _doc_result_text = '\n        Gets the top-level status of a bulk service invocation.\n        This status indicates the overall status of the top-level result \n        in the returned result structure. Application can call \n        result_code for detailed result code.\n        <p>\n        \n        @return String Value of OnepStauts<onep.core.util.OnepStatus> result. \n        Success if status is ONEP_OK, Fail otherwise\n        \n        @type: C{str}\n        '
    result_text = property(_get_result_text, None, None, _doc_result_text)

    def add_match(self, *matches):
        """ Adds match(es) to the class map.
        
        @param matches: The matches.
        @type matches: Variable length argument list of Match
        """
        for mtch in matches:
            if isinstance(mtch, match.Match):
                if not mtch.check_match_support(self.capabilities.matches):
                    raise OnepNotSupportedException('Match ' + match.MatchType.enumval(mtch.get_match_type()))
                if mtch not in self._match_list:
                    mtch.set_negate(False)
                    self._match_list.append(mtch)




    def add_match_not(self, *matches):
        """ Adds match(es) which specify the match criterion as an unsuccessful match criterion. 
        
        This is equivalent to CLI "match not <match-criterion>"
        
        @param matches: The matches.
        @type matches: Variable length argument list of Match      
        """
        for mtch in matches:
            if isinstance(mtch, match.Match):
                if not mtch.check_match_support(self.capabilities.matches):
                    raise OnepNotSupportedException('Match ' + match.MatchType.enumval(mtch.get_match_type()))
                if mtch not in self._match_list:
                    mtch.set_negate(True)
                    self._match_list.append(mtch)




    def remove_match(self, *matches):
        """ Removes match(es) from the class map.
        
        Removes only the matches that are added to class map.
        
        @param matches: The matches.
        @type matches: Variable length argument list of Match       
        """
        if self._handle:
            for mtch in matches:
                validate(mtch, match.Match)
                if mtch in self._match_list:
                    for i_match in self._match_list:
                        if mtch == i_match:
                            i_match._op_code = match.Match.MatchOpCode.DEL
                            break

                    continue

        else:
            for mtch in matches:
                validate(mtch, match.Match)
                if mtch != None and mtch in self._match_list:
                    self._match_list.remove(mtch)




    def remove_all_match(self):
        """ Removes all matches from the class map.
        """
        if self._handle:
            if len(self._match_list) != 0:
                for mtch in self._match_list:
                    mtch._op_code = match.Match.MatchOpCode.DEL

        else:
            while len(self._match_list) != 0:
                self._match_list.pop()




    def get_match_list(self):
        """ Gets all the matches in the class map.
        
        @return: List of Match objects, returns None if no match is added.
             
        @rtype: C{list} of Match objects.        
        """
        if len(self._match_list) > 0:
            return self._match_list



    def _set_result_idl(self, result):
        """
        """
        if result == None:
            result = None
        else:
            self._result = result
            self._handle = result.cmapHandle



    def _get_result_idl(self):
        """
        """
        return self._result



    def _to_idl(self):
        """
        """
        return CmapIDL(self.storage_type, self._handle, self._op_code, self.opid, int(self._match_all), match.Match._to_idl_list(self._match_list), [])



    @classmethod
    def _from_idl(cls, idl, type, element):
        """
        """
        if idl == None:
            return 
        match_idl_list = idl.matchList
        matches = match.Match._from_idl_list(match_idl_list, element)
        cap = PolicyCapabilities(type, element)
        new_class_map = ClassMap(cap, idl.name, idl.dsid)
        for mtch in matches:
            new_class_map.add_match(mtch)

        return new_class_map



    def _to_idl_list(cls, inst_list):
        """
        """
        if inst_list == None:
            return list()
        cmaps = list()
        for map in inst_list:
            cmaps.append(map.to_idl())

        return cmaps



    def _from_idl_list(cls, idl_list, element):
        """
        """
        if idl_list == None:
            return list()
        class_maps = list()
        for idl in idl_list:
            class_maps.append(ClassMap._from_idl(idl, element))

        return class_maps



    def get_result_detail(self):
        """
        Gets the results from submit/update/delete operations
        """
        if self._get_result_idl() and hasattr(self._get_result_idl(), '__dict__'):
            return self._genetate_dict_from_result_idl(self._get_result_idl())



    def _genetate_dict_from_result_idl(self, obj):
        if obj is None:
            return 
        else:
            if hasattr(obj, '__dict__'):
                return self._expand_dict_from_result_idl(obj.__dict__)
            if isinstance(obj, types.ListType):
                return self._expand_list_from_result_idl(obj)
            return obj



    def _expand_dict_from_result_idl(self, idl_map):
        if idl_map is None:
            return 
        new_map = {}
        for (k, v,) in idl_map.iteritems():
            if hasattr(v, '__dict__'):
                new_map[k] = self._expand_dict_from_result_idl(v.__dict__)
            elif isinstance(v, types.ListType):
                new_map[k] = self._expand_list_from_result_idl(v)
            else:
                new_map[k] = v

        return new_map



    def _expand_list_from_result_idl(self, idl_list):
        if idl_list is None:
            return 
        new_list = []
        for v in idl_list:
            if hasattr(v, '__dict__'):
                new_list.append(self._expand_dict_from_result_idl(v.__dict__))
            elif isinstance(v, types.ListType):
                new_list.append(self._expand_list_from_result_idl(v))
            else:
                new_list.append(v)

        return new_list



    def __str__(self):
        match_str = ''
        matches = self.get_match_list()
        if matches:
            for m in self.get_match_list():
                match_str = match_str + match.MatchType.enumval(m.get_match_type())

        return '\n        Class Map %s\n        ------------\n        handle    - %d\n        match_all - %s\n        matches   - %s\n        ' % (self.name,
         self.handle,
         str(self.match_all),
         str(self.get_match_list()))




class ClassResultAsync(object):
    """
        docstring
        match_result_list - list of dict
            Keys           Values
            ----           ------
            storage_type - enum onep.policyservice.StorageType
            handle       - long match handle
            opcode       - enum onep.policyservice.ClassMap.ClassOperation
            opid         - Client context ID
            result       - enum onep.core.util.OnepStatus
            result_text  - result text
    
        """


    def __init__(self, result):
        self.storage_type = result.dsid
        self.handle = result.handle
        self.opid = result.opid
        self.opcode = result.opcode
        self.result = result.result
        self.match_result_list = []
        for rslt in result.matchResultList:
            mtch = {'storage_type': StorageType.enumval(rslt.dsid),
             'handle': rslt.handle,
             'opcode': ClassMap.ClassOperation.enumval(rslt.opcode),
             'opid': rslt.opId,
             'result': OnepStatus.enumval(rslt.result),
             'result_text': rslt.resultString}
            self.match_result_list.append(mtch)




    def __str__(self):
        match_str = ''
        for m in self.match_result_list:
            match_str = match_str + str(m) + '\n'

        return '\n        Class Result\n        ------------\n        storage_type - %s\n        handle       - %d\n        opid         - %d\n        opcode       - %s\n        result       - %s\n\n        Match results\n        -------------\n        %s' % (StorageType.enumval(self.storage_type),
         self.handle,
         self.opid,
         ClassMap.ClassOperation.enumval(self.opcode),
         OnepStatus.enumval(self.result),
         match_str)




class ClassEvent(AsyncMsg):
    """ 
        Class asynchronous event class
    
        result - enum onep.core.util.OnepStatus
        type   - Class type
        class_result_list - List of classmap.ClassResultAsync classes
    
        """


    def __init__(self, element, base, result, type, reslist):
        self.log = logging.getLogger(__name__)
        self.log.info('Class Event asyncHandle %d', base.asyncHandle)
        super(ClassEvent, self).__init__(element, AsyncMsg.OnepAsyncMsgType.ONEP_ASYNC_MESSAGE_TYPE_APICALL)
        self.event_handle = base.asyncHandle
        self.result = result
        self.type = type
        self.class_result_list = []
        self.reslist = reslist



    def do_event(self, element):
        """ 
                This method invokes the client's ClassEventListener class.
        
                @param element: The NetworkElement class associated to event.
                @type element: L{NetworkElement<onep.element.NetworkElement>}
        
                """
        self.log.info('Class Event do_event')
        if not element.event_manager.bulk_listener_map.has_key(self.event_handle):
            self.log.error('Class Event has no listener')
            return 
        (tgt_listener, app_context, cmaps,) = element.event_manager.bulk_listener_map.get(self.event_handle, None)
        if tgt_listener:
            self.log.info('Class Event listener found')
            for (i, rslt,) in enumerate(self.reslist):
                cmaps[i].handle = rslt.handle
                self.class_result_list.append(ClassResultAsync(rslt))

            tgt_listener.handle_event(self, app_context)



    def __str__(self):
        clsres_str = ''
        for clsres in self.class_result_list:
            clsres_str = clsres_str + str(clsres)

        return '\n        Class Event\n        -----------\n        result - %s\n\n        %s' % (OnepStatus.enumval(self.result), clsres)




class ClassEventListener(EventListener):
    """
        Listener to register for revieving Class events
    
        """

    __metaclass__ = ABCMeta

    @abstractmethod
    def handle_event(self, event, app_context):
        """
                Invoked when a Class event is received from the network element.
            
                @param event: An event object which indicates that an event occurred
                in a network element
                @type event: L{onep.policyservice.classmap.ClassEvent>}
            
                @param app_context: The app_context is an object that was passed in when
                application called an API to add/register the event listener.
                The application is responsible for casting the input clientData
                to the appropriate class before using it.
        
                """
        pass




class ClassFilter(object):
    """
        Filter specifications for ClassMap get functions
    
        class_type     - PolicyiCapabilities.PolicyCapabilitiesType
        class_handle   - ClassMap.handle (optional)
        #more to be added 
    
        results - list of ClassMap classes from fetch
        
        @undocumented: __init__
        @undocumented: class_type
        """


    def __init__(self, class_type, class_handle = 0):
        self.log = logging.getLogger(__name__)
        self.class_type = class_type
        self.class_handle = class_handle
        self.result = []



    @property
    def class_type(self):
        return self._class_type



    @class_type.setter
    def class_type(self, type):
        if not PolicyCapabilitiesType._is_valid(type):
            raise OnepIllegalArgumentException('Invalid class type')
        self._class_type = type



    def _to_idl(self):
        return PolicyFilterIDL(0, 0, 0, 0, 0, self.class_type, [], 0, 0, 0, 0, 0)




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:19:56 IST
