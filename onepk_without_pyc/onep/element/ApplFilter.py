# 2015.02.05 17:21:10 IST
from onep.core.event.EventFilter import EventFilter

class ApplFilter(EventFilter):
    """
        Implements the EventFilter abstract class for filtering a app event
        
        Implements the EventFilter abstract class for filtering a app event
        according to the specified criteria.
     
        A Filter can be used to provide fine-tuned control over which events to
        listen to.
    
        """


    def __init__(self, applID, applType):
        """
                Constructor for the ApplEvent class.
                
                The input parameters applID and applType are used in conjunction 
                to identify an application event. The application event 
                can come from other onePK applications, 
                Embedded Event Manager(EEM) policies, or Cisco IOS subsystems. 
                This method is also used in conjunction with the 
                event publish API, where application ID and type are given 
                as arbitrary values.
                
                @param applID: Value of the application ID.
                @param applType: Value of the application type.
        
                """
        super(ApplFilter, self).__init__()
        self.applID = applID
        self.applType = applType




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:21:10 IST
