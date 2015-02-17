# 2015.02.05 17:17:54 IST
from onep.core.event.EventListener import EventListener

class ApplicationExecCliListener(EventListener):
    """
    The listener interface for receiving Exec/showdata events. The class that is
    interested in processing a ConfigNotification event should implement this interface.
    """


    def handle_event(self, cli_data, client_data):
        """
        Invoked when the Exec/showdata event is received from the network element.
        
        This method must be over-ridden in the class implementing this interface.
        
        The over-riding method must return a string response.
        
        @param cli_data:
                   A cli_data object.
                   
        @param client_data:
                   The client_data is an object that was passed in when
                   the application called an API to add/register the event listener. 
                   The application is responsible for casting the input client_data
                   to the appropriate class before using it.
                   
        """
        pass




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:17:54 IST
