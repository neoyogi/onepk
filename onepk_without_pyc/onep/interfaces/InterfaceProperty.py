# 2015.02.05 17:21:23 IST

class InterfaceProperty(object):
    """
        This class represents hardware property of the network interface.
    
        The property is associated with physical hardware; for example, a hardware slot
        or port location of the interface. It is retrieved only once from the NetworkElement,
        because it is not changed during the life of the session.
        
        @ivar port:
            The physical Port location of the logical interface if applicable.
            This API is currently deprecated as the underlying platform is not correctly
            returning the port info that matches with the port in the interface name
        @type port : C{int}
        
        @ivar speed:
            The interface speed
        @type speed: C{int}
        
        @ivar short_name:
            The interface's short name
        @type short_name: C{str}
        
        @ivar subif_id:
            If the interface is a logical sub-interface it will have this ID
        @type subif_id: C{int}
    
        @undocumented: slot
        """

    slot = -1
    port = -1

    def __init__(self, slot, port, speed = None, short_name = None, subif_id = None):
        """
                Constructor of InterfaceProperty class.
                
                @param slot:
                    The physical slot location of the logical interface if applicable.
                    For virtual interfaces the slot will be set to -1
                @type slot: C{int}
                
                @param port:
                    The physical Port location of the logical interface if applicable.
                @type port : C{int}
                
                @param speed:
                    The interface speed
                @type speed: C{int}
            
                @param short_name:
                    The interface's short name
                @type short_name: C{str}
        
                @param subif_id:
                    If the interface is a logical sub-interface it will have this ID
                @type subif_id: C{int}
        
                """
        self.slot = slot
        self.port = port
        self.speed = speed
        self.short_name = short_name
        self.subif_id = subif_id




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:21:23 IST
