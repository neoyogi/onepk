# 2015.02.05 17:21:11 IST
import logging
from onep.core.event.EventObject import EventObject
from core.util.OnepConstants import OnepConstants
from core.exception.OnepIllegalArgumentException import OnepIllegalArgumentException

class ApplEvent(EventObject):
    """
        An event that indicates that an App event occurred in a network element.
        
        An App event is triggered by other onep Apps using the publish_appl_event()
        method.
    
        @ivar event_handle: (OPTIONAL) The unique ID identifying the event listener which
        should receive the event. Not needed when an event is created to be published
        @ivar applID: The application ID.
        @ivar applType: The application type.
        @ivar applData: The list of application data buffers.
        """


    def __init__(self, element, applID, applType, applData1, applData2, applData3, applData4, eventHandle = None):
        """
        Constructor - used internally
        
        @param element:
            The Network Element object
        @param applId:
            The Application ID.
        @param applType:
            The Application type.
        @param applData1:
            Data buffer 1.
        @param applData2:
            Data buffer 2.
        @param applData3:
            Data buffer 3.
        @param applData4:
            Data buffer 4.
        @param eventHandle:
            Event handle is a unique ID to identify which event listener should
            receive the event. Not needed when an event is created to be published
        """
        super(ApplEvent, self).__init__(element, eventHandle, OnepConstants.EVENT_TYPE_APPLICATION)
        self.event_handle = eventHandle
        self.applID = applID
        self.applType = applType
        self.applData = ['',
         applData1,
         applData2,
         applData3,
         applData4]



    def do_event(self, ne):
        """
                This method specifies what action to do when an event is processed.
                
                For AppEvent, the action is invoking the client's event
                listener.
                
                @param ne:
                    The source of the event. For AppEvent, the source in an
                    instance of NetworkElement.
        
                """
        logging.debug('App do_event: applID = ' + str(self.applID) + ' applType = ' + str(self.applType) + ' applData = ' + str(self.applData))
        targetListener = ne.event_manager.get_event_listener(self.event_handle)
        clienData = ne.event_manager.get_event_listener_client_data(self.event_handle)
        try:
            if targetListener != None:
                targetListener.handle_event(self, clienData)
        except Exception as e:
            logging.warning(e.__str__())




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:21:11 IST
