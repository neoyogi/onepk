# 2015.02.05 17:22:51 IST
from onep.interfaces.NetworkInterface import NetworkInterface
from onep.PolicyBulkIDL.PolicyBulkIDL import Client
from onep.policyservice.match import Match
from onep.policyservice.classmap import ClassMap, ClassFilter
from onep.policyservice.classmap import ClassEventListener
from onep.policyservice.policymap import PolicyMap, PolicyFilter, PolicySubmitListener
from onep.policyservice.policymap import PolicyStatsListener, PolicyActivateListener
from onep.policyservice.statistics import PolicyStatistics
from onep.policyservice.policymap import Entry, PolicyStatFilter
from onep.policyservice.action import Action
from onep.policyservice.target import Target
from onep.PolicyBulkIDL.ttypes import PmapActivateIDL
from onep.PolicyBulkIDL.ttypes import PolicyFilterIDL
from onep.PolicyBulkIDL.ttypes import PmapIDL
from onep.PolicyBulkIDL.ttypes import CmapIDL
from onep.core.util.OnepArgumentTypeValidate import *
from onep.core.exception.OnepIllegalArgumentException import OnepIllegalArgumentException
from onep.core.exception.OnepConnectionException import OnepConnectionException
from onep.core.exception.OnepRemoteProcedureException import OnepRemoteProcedureException
from Shared.ttypes import ExceptionIDL
from onep.thrift.Thrift import TException
import logging
from onep.core.exception.OnepException import OnepNotSupportedException
from onep.core.util.Enum import enum
from onep.policyservice import StorageType
from onep.policyservice.caps import PolicyCapabilities
from onep.policyservice.caps import PolicyCapabilitiesType
REQUEST_ASYNC_ID = 0

class BulkService(object):
    """ BulkService class.
    
    The BulkService class provides the enhanced Policy API for submitting and activating policy in bulk fashion.
    
    ActivationHolder in BulkService is provided as a container to group a policy with its intended targets.
    
    The ActivationHolder object is then used to activate the policy in the network element. 
    
    @undocumented: _create_cmap_list_helper_
    @undocumented: _create_pmap_list_helper_
    @undocumented: _update_cmap_entries_
    @undocumented: _update_pmap_entries_
    """


    def __init__(self, element):
        """ Constructs a BulkService object.
                
        @param element: Network Element object.
        @type element: L{NetworkElement<onep.element.NetworkElement.NetworkElement>}
        
        @raise OnepIllegalArgumentException: If constructor parameter is invalid.        
        """
        self.log = logging.getLogger(__name__)
        if not hasattr(element, 'session_handle'):
            raise OnepIllegalArgumentException('Invalid NetworkElement')
        self._element = element
        self._session_id = element.session_handle._id
        self._class_client = Client(element.api_protocol)
        self._caps = []



    def _check_element(self, element):
        if self._element != element:
            raise OnepIllegalArgumentException('Wrong network element for bulk service')



    def _get_policy_filter_idl(self):
        return PolicyFilterIDL(dsid=0, opCode=0, opId=0, pollIntervalSec=0, pollIntervalMsec=0, tableType=0, ifHandle=[], maxEntryCount=0, persistent=0, lastEntryHandle=0, statsCategory=0, target_direction=0)



    def _validate_capability(self, type, element):
        if not PolicyCapabilitiesType._is_valid(type):
            raise OnepIllegalArgumentException(type, 'PolicyCapabilitiesType')
        if not hasattr(element, 'session_handle'):
            raise OnepIllegalArgumentException('Invalid NetworkElement')
        for cap in self._caps:
            if cap.policy_type == type:
                return cap

        new_cap = PolicyCapabilities(type, element)
        self._caps.append(new_cap)
        return new_cap



    def create_class(self, type, element, class_name = None):
        """ 
                Create an instance of ClassMap class
        
                @param type
                @type {PolicyCapabilitiesType<onep.policyservice.PolicyiCapabilities.PolicyCapabilitiesType>}
        
                @param element
                @type {NetworkElement<onep.element.NetworkElement.NetworkElement>}
        
                @param class_name
                @type class_name (optional): {str}
        
                """
        cap = self._validate_capability(type, element)
        return ClassMap(cap, name=class_name)



    def create_policy(self, type, element, policy_name = None):
        """ 
                Create an instance of PolicyMap class
        
                @param type
                @type {PolicyCapabilitiesType<onep.policyservice.PolicyCapabilities.PolicyCapabilitiesType>}
        
                @param element
                @type {NetworkElement<onep.element.NetworkElement.NetworkElement>}
        
                @param policy_name
                @type policy_name (optional): {str}
        
                """
        cap = self._validate_capability(type, element)
        return PolicyMap(cap, name=policy_name)



    def submit_class_map(self, *class_maps):
        """ Submits a list of class maps. 
        
        This will create the class maps in the network element.
        
        @param class_maps: The class maps.
        @type class_maps: Variable length argument list of L{ClassMap<onep.policyservice.ClassMap.ClassMap>}
        
        @raise OnepIllegalArgumentException: If any ClassMap in *class_maps is invalid.
        @raise OnepRemoteProcedureException: If error occurs when remote procedure call is made to network element.
        @raise OnepConnectionException: If connection to network element fails.    
        """
        try:
            class_map_idl_list = []
            policy_type = 0
            for class_map in class_maps:
                self._check_element(class_map._element)
                if not isinstance(class_map, ClassMap):
                    raise OnepIllegalArgumentException('Invalid class map in *class_maps.')
                if policy_type and policy_type != class_map.capabilities.policy_type:
                    raise OnepIllegalArgumentException('Cannot submit classes with differing capabilities')
                policy_type = class_map.capabilities.policy_type
                class_map._op_code = ClassMap.ClassOperation.ONEP_CLASS_OP_CREATE
                class_map_idl_list.append(class_map._to_idl())

            if len(class_map_idl_list) == 0:
                raise OnepIllegalArgumentException('*class_maps has no valid ClassMap.')
            self.log.info('submit_class_map: class_map_idl_list:%s', str(class_map_idl_list))
            results = self._class_client.Policy_submitCmapBulkIDL(self._session_id, policy_type, class_map_idl_list)
            self.log.info('submit_class_map: idl results:%s', str(results))
            if results:
                for (i, class_map,) in enumerate(class_maps):
                    class_map._set_result_idl(results[i])

                self.log.info('submit_class_map executed with success.')
            else:
                self.log.error('no results for submit class map')
        except OnepIllegalArgumentException as e:
            raise e
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e.message, e)



    def _add_cmap_listener(self, event_id, listener, app_context, *cmaps):
        """
                Private function for adding event listener.
                ClassMap objects are saved so event can assign returned handle.
        
                """
        if not isinstance(listener, ClassEventListener):
            raise OnepIllegalArgumentException(listener, ClassEventListener)
        if self._element.event_manager.bulk_listener_map.has_key(event_id):
            raise OnepIllegalArgumentException('Listener exists with this event_id')
        self._element.event_manager.bulk_listener_map[event_id] = (listener, app_context, cmaps)



    def get_all_bulk_listeners(self):
        """
                Returns dict of tuples containing all active bulk listeners in element
        
                dict of tuple - {(Policy listening class, application context, ClassMap objects), ...}
        
                """
        return self._element.event_manager.bulk_listener_map



    def async_submit_class_map(self, listener, app_context, *class_maps):
        """
                Submits a list of class maps asynchronously. 
                
                This will create the class maps in the network element.
                
                @param event_id: ID retrieved from BulkService.get_event_id(). Match to listener event_id.
                @type event_id: C{int}
        
                @param class_maps: The class maps.
                @type class_maps: Variable length argument list of L{ClassMap<onep.policyservice.ClassMap.ClassMap>}
                
                @raise OnepIllegalArgumentException: If any ClassMap in *class_maps is invalid.
                @raise OnepRemoteProcedureException: If error occurs when remote procedure call is made to network element.
                @raise OnepConnectionException: If connection to network element fails.
        
                """
        try:
            class_map_idl_list = list()
            policy_type = 0
            for class_map in class_maps:
                self._check_element(class_map._element)
                if not isinstance(class_map, ClassMap):
                    raise OnepIllegalArgumentException('Invalid class map in *class_maps.')
                if policy_type and policy_type != class_map.capabilities.policy_type:
                    raise OnepIllegalArgumentException('Cannot submit classes with differing capabilities')
                policy_type = class_map.capabilities.policy_type
                class_map._op_code = ClassMap.ClassOperation.ONEP_CLASS_OP_CREATE
                class_map_idl_list.append(class_map._to_idl())

            if len(class_map_idl_list) == 0:
                raise OnepIllegalArgumentException('*class_maps has no valid ClassMap.')
            event_hdl = self._class_client.Policy_submitCmapBulkAsyncIDL(self._session_id, policy_type, REQUEST_ASYNC_ID, class_map_idl_list)
            self.log.debug('Class Event handle ' + str(event_hdl))
            self._add_cmap_listener(event_hdl.eventHandle, listener, app_context, *class_maps)
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e.message, e)



    def _validate_class_filter(self, filter):
        if not isinstance(filter, ClassFilter):
            self.log.error('ClassFilter class required')
            raise OnepIllegalArgumentException('ClassFilter required')
        if not filter.class_type:
            self.log.error('Filter type not set')
            raise OnepIllegalArgumentException('ClassFilter type not set')
        if not filter.class_handle:
            self.log.error('ClassFilter handle not set')
            raise OnepIllegalArgumentException('ClassFilter handle not set')
        return True



    def update_class_map(self, *class_maps):
        """ Update a list of class maps in the network element.
        
        @param class_maps: The class maps to update.
        @type class_maps: Variable length argument list of L{ClassMap<onep.policyservice.ClassMap.ClassMap>}
        
        @raise OnepIllegalArgumentException: If class_maps has no valid ClassMap.
        @raise OnepRemoteProcedureException: If error occurs when remote procedure call is made to network element.
        @raise OnepConnectionException: If connection to network element fails.        
        """
        try:
            cmap_idl_list = list()
            policy_type = 0
            for map in class_maps:
                self._check_element(map._element)
                if policy_type and policy_type != map.capabilities.policy_type:
                    raise OnepIllegalArgumentException('Cannot update classes with differing capabilities')
                policy_type = map.capabilities.policy_type
                if isinstance(map, ClassMap):
                    map._op_code = ClassMap.ClassOperation.ONEP_CLASS_OP_MODIFY
                    cmap_idl_list.append(map._to_idl())

            if len(cmap_idl_list) == 0:
                raise OnepIllegalArgumentException('class_list has no valid ClassMap.')
            self.log.info('update_class_map: cmap_idl_list:%s', str(cmap_idl_list))
            results = self._class_client.Policy_submitCmapBulkIDL(self._session_id, policy_type, cmap_idl_list)
            self.log.info('update_class_map: idl results:%s', str(results))
            if results:
                for (i, class_map,) in enumerate(class_maps):
                    class_map._set_result_idl(results[i])

                self.log.info('update_class_map executed with success.')
            else:
                self.log.error('no results for update class map')
        except OnepIllegalArgumentException as e:
            raise e
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e.message, e)



    def delete_class_map(self, *class_maps):
        """ Deletes a list of class maps from the network element.
        
        @param class_maps: The class maps to delete.
        @type class_maps: Variable length argument list of L{ClassMap<onep.policyservice.ClassMap.ClassMap>}
        
        @raise OnepRemoteProcedureException: If error occurs when remote procedure call is made to network element.
        @raise OnepConnectionException: If connection to network element fails.        
        """
        try:
            cmap_idl_list = list()
            policy_type = 0
            for map in class_maps:
                self._check_element(map._element)
                if policy_type and policy_type != map.capabilities.policy_type:
                    raise OnepIllegalArgumentException('Cannot delete classes with differing capabilities')
                policy_type = map.capabilities.policy_type
                if isinstance(map, ClassMap):
                    map._op_code = ClassMap.ClassOperation.ONEP_CLASS_OP_DELETE
                    cmap_idl_list.append(map._to_idl())

            results = self._class_client.Policy_submitCmapBulkIDL(self._session_id, policy_type, cmap_idl_list)
            self.log.info('delete_class_map: idl results:%s', str(results))
            if results:
                for (i, class_map,) in enumerate(class_maps):
                    class_map._set_result_idl(results[i])

                self.log.info('delete_class_map executed with success.')
            else:
                self.log.error('no result for delete class map')
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e.message, e)



    def submit_policy_map(self, *policy_maps):
        """ Submits a list of policy maps.
        
        This will create the policy maps in the network element.
        
        @param policy_maps: The policy maps.
        @type policy_maps: Variable length argument list of L{PolicyMap<onep.policyservice.PolicyMap.PolicyMap>}
        
        @raise OnepIllegalArgumentException: If an PolicyMap in *policy_maps is invalid.
        @raise OnepRemoteProcedureException: If error occurs when remote procedure call is made to network element.
        @raise OnepConnectionException: If connection to network element fails.        
        """
        try:
            pmap_idl_list = []
            policy_type = 0
            for policy_map in policy_maps:
                self._check_element(policy_map._element)
                if not isinstance(policy_map, PolicyMap):
                    raise OnepIllegalArgumentException('Invalid policy map in *policy_maps.')
                if policy_type and policy_type != policy_map.capabilities.policy_type:
                    raise OnepIllegalArgumentException('Cannot submit policies with differing capabilities')
                policy_type = policy_map.capabilities.policy_type
                policy_map._op_code = PolicyMap.PolicyOperation.ONEP_POLICY_OP_CREATE
                pmap_idl_list.append(policy_map._to_idl())
                entries = policy_map.get_entry_list()

            if len(pmap_idl_list) == 0:
                raise OnepIllegalArgumentException('*policy_maps has no valid PolicyMap.')
            self.log.info('submit_policy_map: pmap_idl_list:%s', str(pmap_idl_list))
            results = self._class_client.Policy_submitPmapBulkIDL(self._session_id, policy_type, pmap_idl_list)
            self.log.info('submit_policy_map: idl results:%s', str(results))
            if results:
                for (i, policy_map,) in enumerate(policy_maps):
                    policy_map._set_result_idl(results[i])

                self.log.info('submit_policy_map executed with success.')
            else:
                self.log.error('no results for submit policy map')
        except OnepIllegalArgumentException as e:
            raise e
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e.message, e)



    def _add_policy_submit_listener(self, event_id, listener, app_context, *pmaps):
        """
                Add a PolicySubmitListener class to event manager for asynchronous
                submit operation.  Client creates handle_event callback in listener.
                Listener handle_event will be called when element is done with submit.
        
                @param event_id: ID retrieved from BulkService.get_event_id()
                @type event_id: C{int}
        
                @param listener: Custom PolicySubmitListener class with callback
                @type listener: {PolicySubmitListener<onep.policyservice.PolicyMap.PolicySubmitListener>}
        
                @param app_context: Optional client data returned with listener response
                @type app_context: Any object
        
                """
        if not isinstance(listener, PolicySubmitListener):
            raise OnepIllegalArgumentException(listener, PolicySubmitListener)
        if self._element.event_manager.bulk_listener_map.has_key(event_id):
            raise OnepIllegalArgumentException('Listener exists with this event_id')
        self._element.event_manager.bulk_listener_map[event_id] = (listener, app_context, pmaps)



    def _add_policy_activate_listener(self, event_id, listener, app_context, *activations):
        """ 
                Add a PolicyEventListener class to event manager for asynchronous
                activate operation.  Client creates handle_event callback in listener.
                Listener handle_event will be called when element is done with activation.
        
                @param event_id: ID retrieved from BulkService.get_event_id()
                @type event_id: C{int}
        
                @param listener: Custom PolicyActivateListener class with callback
                @type listener: {PolicyActivateListener<onep.policyservice.PolicyMap.PolicyActivateListener>}
        
                @param app_context: Optional client data returned with listener response
                @type app_context: Any object
        
                """
        if not isinstance(listener, PolicyActivateListener):
            raise OnepIllegalArgumentException(listener, PolicyActivateListener)
        if self._element.event_manager.bulk_listener_map.has_key(event_id):
            raise OnepIllegalArgumentException('Listener exists with this event_id')
        self._element.event_manager.bulk_listener_map[event_id] = (listener, app_context, activations)



    def _add_policy_statistic_listener(self, event_id, listener, app_context, filters):
        """ 
                Add a PolicyEventListener class to event manager for asynchronous
                statistic operation.  Client creates handle_event callback in listener.
                Listener handle_event will be called when statistic filter specifications are met.
        
                @param event_id: ID retrieved from BulkService.get_event_id()
                @type event_id: C{int}
        
                @param listener: Custom PolicyStatsListener class with callback
                @type listener: {PolicyStatsListener<onep.policyservice.PolicyMap.PolicyStatsListener>}
        
                @param app_context: Optional client data returned with listener response
                @type app_context: Any object
        
                """
        if not isinstance(listener, PolicyStatsListener):
            raise OnepIllegalArgumentException(listener, PolicyStatsListener)
        if self._element.event_manager.bulk_listener_map.has_key(event_id):
            raise OnepIllegalArgumentException('Listener exists with this event_id')
        self._element.event_manager.bulk_listener_map[event_id] = (listener, app_context, filters)



    def async_submit_policy_map(self, listener, app_context, *policy_maps):
        """
                Submits a list of policy maps asynchronously.
                
                This will create the policy maps in the network element.
                
                @param listener: PolicySubmitEvent class created by user
                @type listener: L{PolicySubmitEvent<policymap.PolicySubmitEvent>}
        
                @param app_context: Object sent from user for providing context specific to user
                @type app_context: Any Python object
        
                @param policy_maps: The policy maps.
                @type policy_maps: Variable length argument list of L{PolicyMap<onep.policyservice.PolicyMap.PolicyMap>}
                
                @raise OnepIllegalArgumentException: If an PolicyMap in *policy_maps is invalid.
                @raise OnepRemoteProcedureException: If error occurs when remote procedure call is made to network element.
                @raise OnepConnectionException: If connection to network element fails.
                """
        try:
            pmap_idl_list = list()
            policy_type = 0
            for map in policy_maps:
                self._check_element(map._element)
                if not isinstance(map, PolicyMap):
                    raise OnepIllegalArgumentException('Invalid policy map in *policy_maps.')
                if policy_type and policy_type != map.capabilities.policy_type:
                    raise OnepIllegalArgumentException('Cannot update classes with differing capabilities')
                policy_type = map.capabilities.policy_type
                map._op_code = PolicyMap.PolicyOperation.ONEP_POLICY_OP_CREATE
                pmap_idl_list.append(map._to_idl())

            if len(pmap_idl_list) == 0:
                raise OnepIllegalArgumentException('*policy_maps has no valid PolicyMap.')
            event_hdl = self._class_client.Policy_submitPmapBulkAsyncIDL(self._session_id, policy_type, REQUEST_ASYNC_ID, pmap_idl_list)
            self.log.info('Policy Submit Event handle ' + str(event_hdl))
            self._add_policy_submit_listener(event_hdl.eventHandle, listener, app_context, *policy_maps)
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e.message, e)



    def _validate_policy_filter(self, filter):
        if not isinstance(filter, PolicyFilter):
            self.log.error('PolicyFilter class required')
            raise OnepIllegalArgumentException('PolicyFilter class required')
        if not filter.policy_type:
            self.log.error('Filter type not set')
            raise OnepIllegalArgumentException('PolicyFilter type not set')
        return True



    def _update_pmap_entries_(self, policy_maps):
        for policy_map in policy_maps:
            validate(policy_map, PolicyMap)
            new_entry_list = []
            for entry in policy_map._entries:
                if not entry._entry_op_code == Entry._entry_op_type.ENTRY_REM:
                    new_action_list = []
                    for action in entry._action_list:
                        if not action.op_code == Action.ActionOpCode.DEL:
                            new_action_list.append(action)

                    entry._action_list = new_action_list
                    new_match_list = []
                    for match in entry._match_list:
                        if not match._op_code == Match.MatchOpCode.DEL:
                            new_match_list.append(match)

                    entry._match_list = new_match_list
                    new_entry_list.append(entry)

            policy_map._entries = new_entry_list




    def update_policy_map(self, *policy_maps):
        """ Update a list of policy maps in the network element.
        
        @param policy_maps: The policy maps to update.
        @type policy_maps: Variable length argument list of L{PolicyMap<onep.policyservice.PolicyMap.PolicyMap>}
        
        @raise OnepIllegalArgumentException: If policy_maps has no valid PolicyMap.
        @raise OnepRemoteProcedureException: If error occurs when remote procedure call is made to network element.
        @raise OnepConnectionException: If connection to network element fails.        
        """
        try:
            pmap_idl_list = list()
            policy_type = 0
            for map in policy_maps:
                self._check_element(map._element)
                if policy_type and policy_type != map.capabilities.policy_type:
                    raise OnepIllegalArgumentException('Cannot update classes with differing capabilities')
                policy_type = map.capabilities.policy_type
                if isinstance(map, PolicyMap):
                    map._change_entry_op_code(Entry._entry_op_type.ENTRY_MOD)
                    map._op_code = PolicyMap.PolicyOperation.ONEP_POLICY_OP_MODIFY
                    pmap_idl_list.append(map._to_idl())

            self.log.info('update_policy_map: pmap_idl_list:%s', str(pmap_idl_list))
            results = self._class_client.Policy_submitPmapBulkIDL(self._session_id, policy_type, pmap_idl_list)
            self.log.info('update_policy_map: idl results:%s', str(results))
            if results:
                for (i, policy_map,) in enumerate(policy_maps):
                    policy_map._set_result_idl(results[i])

                self._update_pmap_entries_(policy_maps)
                self.log.info('update_policy_map executed with success.')
            else:
                self.log.error('no result in update policy map')
        except OnepIllegalArgumentException as e:
            raise e
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e.message, e)



    def delete_policy_map(self, *policy_maps):
        """ Deletes a list of policy maps from the network element.
        
        @param policy_maps: The policy maps to delete.
        @type policy_maps: Variable length argument list of L{PolicyMap<onep.policyservice.PolicyMap.PolicyMap>}
        
        @raise OnepRemoteProcedureException: If error occurs when remote procedure call is made to network element.
        @raise OnepConnectionException: If connection to network element fails.                
        """
        try:
            pmap_idl_list = list()
            policy_type = 0
            for map in policy_maps:
                self._check_element(map._element)
                if policy_type and policy_type != map.capabilities.policy_type:
                    raise OnepIllegalArgumentException('Cannot update classes with differing capabilities')
                policy_type = map.capabilities.policy_type
                if not isinstance(map, PolicyMap):
                    raise OnepIllegalArgumentException('Invalid policy map ' + str(map))
                map._op_code = PolicyMap.PolicyOperation.ONEP_POLICY_OP_DELETE
                pmap_idl_list.append(map._to_idl())

            results = self._class_client.Policy_submitPmapBulkIDL(self._session_id, policy_type, pmap_idl_list)
            self.log.info('submit_policy_map: idl results:%s', str(results))
            if results:
                for (i, policy_map,) in enumerate(policy_maps):
                    policy_map._set_result_idl(results[i])

                self._update_pmap_entries_(policy_maps)
                self.log.info('delete_policy_map executed with success.')
            else:
                self.log.error('no result in delete policy map')
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e.message, e)



    def create_activation_holder(self, policy_map, *targets):
        """ Creates a ActivationHolder with the supplied policy and targets.
                
                @param policy_map: The policy to be activated.
                @type policy_map: L{PolicyMap<onep.policyservice.PolicyMap.PolicyMap>}
                @param targets: The targets to apply to.
                @type targets: Variable length argument list of L{Target<onep.policyservice.Target.Target>} 
                
                @return: Returns an ActivationHolder object.
                     
                @rtype: L{BulkService.ActivationHolder<onep.policyservice.BulkService.BulkService.ActivationHolder>}
        
                @raise OnepIllegalArgumentException: If policy or targets is invalid.
                """
        try:
            new_activation_holder = ActivationHolder(policy_map, *targets)
        except OnepIllegalArgumentException as e:
            raise e
        return new_activation_holder



    def activate_policy(self, *activations):
        """ Activates the policy to its targets that are specified in the ActivationHolder list.
        
        @param activations: The activation holder.
        @type activations: Variable length argument list of L{BulkService.ActivationHolder<onep.policyservice.BulkService.BulkService.ActivationHolder>}
        
        @raise OnepRemoteProcedureException: If error occurs when remote procedure call is made to network element.
        @raise OnepConnectionException: If connection to network element fails.
        """
        try:
            activate_idl_list = []
            policy_type = 0
            for activation in activations:
                self._check_element(activation._element)
                if isinstance(activation, ActivationHolder):
                    activation._op_code = PolicyMap.PolicyOperation.ONEP_POLICY_OP_ACTIVATE
                    if policy_type and policy_type != activation._policy.capabilities.policy_type:
                        raise OnepIllegalArgumentException('Cannot activate policies with differing capabilities')
                    policy_type = activation._policy.capabilities.policy_type
                    activate_idl_list.append(activation._to_idl())

            self.log.info('activate_policy: activate_idl_list:%s', str(activate_idl_list))
            results = self._class_client.Policy_submitPmapActivateIDL(self._session_id, policy_type, activate_idl_list)
            if results:
                for (i, activation,) in enumerate(activations):
                    activation._set_result(results[i])

            else:
                self.log.error('no result in update policy map')
            self.log.info('activate_policy executed with success.')
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e.message, e)



    def async_activate_policy(self, listener, app_context, *activations):
        """ 
        Asynchronously activates the policy to its targets that are specified in the ActivationHolder list.
        
        @param activations: The activation holder.
        @type activations: list of L{ActivationHolder<onep.policyservice.bulk.ActivationHolder>}
        
        @raise OnepRemoteProcedureException: If error occurs when remote procedure call is made to network element.
        @raise OnepConnectionException: If connection to network element fails.
        """
        try:
            activate_idl_list = []
            policy_type = 0
            for activation in activations:
                self._check_element(activation._element)
                if isinstance(activation, ActivationHolder):
                    activation._op_code = PolicyMap.PolicyOperation.ONEP_POLICY_OP_ACTIVATE
                    if policy_type and policy_type != activation._policy.capabilities.policy_type:
                        raise OnepIllegalArgumentException('Cannot activate policies with differing capabilities')
                    policy_type = activation._policy.capabilities.policy_type
                    activate_idl_list.append(activation._to_idl())

            if not activate_idl_list:
                raise OnepillegalArgumentException('No valid activation holders')
            self.log.info('async_activate_policy: activate_idl_list:%s', str(activate_idl_list))
            async_hdl = self._class_client.Policy_submitPmapActivateAsyncIDL(self._session_id, policy_type, REQUEST_ASYNC_ID, activate_idl_list)
            self._add_policy_activate_listener(async_hdl.eventHandle, listener, app_context, *activations)
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e.message, e)



    def deactivate_policy(self, *activations):
        """
        De-activates the policy from its targets that are specified in the ActivationHolder list.
        
        @param activations: The activation holder.
        @type activations: List of L{ActivationHolder<onep.policyservice.bulk.ActivationHolder>}
        
        @raise OnepRemoteProcedureException: error when remote procedure call is made to network element.
        @raise OnepConnectionException: If connection to network element fails.        
        """
        try:
            activate_idl_list = list()
            policy_type = 0
            for activation in activations:
                self._check_element(activation._element)
                if isinstance(activation, ActivationHolder):
                    activation._op_code = PolicyMap.PolicyOperation.ONEP_POLICY_OP_DEACTIVATE
                    if policy_type and policy_type != activation._policy.capabilities.policy_type:
                        raise OnepIllegalArgumentException('Cannot deactivate policies with differing capabilities')
                    policy_type = activation._policy.capabilities.policy_type
                    activate_idl_list.append(activation._to_idl())

            self.log.info('deactivate_policy: activate_idl_list:%s', str(activate_idl_list))
            self._class_client.Policy_submitPmapActivateIDL(self._session_id, policy_type, activate_idl_list)
            self.log.info('deactivate_policy executed with success.')
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e.message, e)



    def remove_statistic_listener(self, listener):
        """
                Removes client statistic listener
        
                @param listener: PolicyStatsListener class
                @type listener: {PolicyStatsListener<onep.policyservice.policymap.PolicyStatsListener>}
        
                """
        filters = None
        if isinstance(listener, PolicyStatsListener):
            self.log.debug('remove listener ' + str(listener))
            if self._element.event_manager.bulk_listener_map.has_key(listener.event_handle):
                (id, listen, filters,) = self._element.event_manager.bulk_listener_map.pop(listener.event_handle)
            self._element.event_manager.request_event_unregister(listener.event_handle)
        else:
            self.log.warning('Failed to remove listener ' + str(listener))
        if filters:
            print 'STOPPING STATS'
            self.get_policy_statistics(filters, opcode=PolicyMap.PolicyOperation.ONEP_POLICY_OP_REMOVE_STATS)



    def _validate_policy_stat_filter(self, filter):
        if not isinstance(filter, PolicyStatFilter):
            self.log.error('PolicyStatFilter class required')
            raise OnepIllegalArgumentException('PolicyStatFilter class required')
        if not filter.policy_type:
            self.log.error('PolicyStatFilter type not set')
            raise OnepIllegalArgumentException('PolicyStatFilter type not set')
        if not filter.policy_handle:
            self.log.error('PolicyStatFilter handle not set')
            raise OnepIllegalArgumentException('PolicyStatFilter handle not set')
        return True



    def get_policy_statistics(self, filters, listener = None, app_context = None, opcode = None):
        """
                Retrieves statistics according to filter specifications.
                A list of PolicyStatistics classes are populated in PolicyStatFilter.stats_result.
        
                @param filters: one or more PolicyStatFilter classes
                @type filters: {PolicyMap<onep.policyservice.PolicyMap.PolicyStatFilter>}
        
                @param listener: PolicyStatsListener class created by user
                @type listener: l{PolicyStatsListener<policymap.PolicyStatsListener>)
        
                @param app_context: Optional context for application
                @type: app_context: Any Python object
        
                @raise OnepIllegalArgumentException: If nif or policy_map is invalid.
                @raise OnepRemoteProcedureException: If error occurs when remote procedure call is made to network element.
                @raise OnepConnectionException: If connection to network element fails.
                """
        try:
            self.log.info('get_policy_statistics start')
            try:
                obj_iterator = iter(filters)
            except TypeError:
                filters = [filters]
            type = 0
            pmap_idl_list = []
            for filter in filters:
                self._validate_policy_stat_filter(filter)
                if not type:
                    type = filter.policy_type
                if filter.policy_type != type:
                    self.log.error('Filter types must all be the same')
                    raise OnepIllegalArgumentException('PolicyFilter types must all be the same')
                if not opcode:
                    opcode = PolicyMap.PolicyOperation.ONEP_POLICY_OP_GET_STATS
                in_pmap_idl = PmapIDL(filter.storage_type, filter.policy_handle, opcode, opId=0, entryList=[])
                in_pmap_idl.filter = filter._to_idl()
                pmap_idl_list.append(in_pmap_idl)

            results = self._class_client.Policy_submitPmapBulkIDL(self._session_id, type, pmap_idl_list)
            if results:
                self.log.info('policy get stats results ' + str(results))
                if results[0].statsResultEventHandle and listener:
                    listener.event_handle = results[0].statsResultEventHandle
                    self._add_policy_statistic_listener(results[0].statsResultEventHandle, listener, app_context, filters)
                for (i, result,) in enumerate(results):
                    if result.resultCode:
                        filters[i].result.append(result.resultCode)
                        self.log.error('statistic fail %d for filter %d' % (result.resultCode, filters[i].policy_type))
                        continue
                    if result.statsResult:
                        self.log.info('fetch_policy_map stats')
                        stat = result.statsResult
                        filters[i].stats_result.append(PolicyStatistics(stat.dsid, stat.asyncHandle, stat.pmapHandle, stat.ifHandle, stat.total_count, stat.entry_count, stat.more, stat.entryStatsResultList))
                        filters[i].entry_start = stat.entry_count
                        filters[i].more = stat.more

            else:
                self.log.error('no result in get_policy_statistics')
        except OnepIllegalArgumentException as e:
            raise e
        except ExceptionIDL as e:
            raise OnepRemoteProcedureException(e)
        except TException as e:
            raise OnepConnectionException(e.message, e)




class ActivationHolder(object):
    """ This class is provided as a container to group a policy with its intended targets.
    
    """


    def __init__(self, policy_map, *infs):
        """ Constructor of ActivationHolder.
        """
        try:
            validate(policy_map, PolicyMap)
            for target in infs:
                validate(target, Target)

        except OnepIllegalArgumentException as e:
            raise e
        self.storage_type = StorageType.PERSISTENT
        self._policy = policy_map
        self._targe_array = infs
        self._op_code = PolicyMap.PolicyOperation.ONEP_POLICY_OP_ACTIVATE
        self._element = policy_map._element



    def _to_idl(self):
        """
        """
        interface_handles = []
        location_handles = []
        zone_pairs = []
        for target in self._targe_array:
            if target.network_interface:
                interface_handles.append(target.network_interface.xos_handle)
                location_handles.append(target.location)
            if target.zone_pair:
                zone_pairs.append(target.zone_pair.name)

        if not interface_handles:
            interface_handles = None
        if not zone_pairs:
            zone_pairs = None
        activate_idl = PmapActivateIDL(self.storage_type, self._policy._handle, self._op_code, 0, interface_handles, location_handles, zone_pairs)
        return activate_idl



    def _set_result(self, results):
        self._result = results



    def _get_result(self):
        rdict = {}
        for (i, result,) in enumerate(self._result.ifHandle):
            rdict[result] = self._result.resultCode[i]

        if self._result.zpName:
            for (i, result,) in enumerate(self._result.zpName):
                rdict[result] = self._result.resultCode[i]

        return rdict


    _result_doc = '\n        Activation result dictionary\n\n        {target handle : result code}\n\n        '
    result = property(_get_result, _set_result, None, _result_doc)


# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:22:51 IST
