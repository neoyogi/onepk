# 2015.02.05 17:21:10 IST

class FRU(object):
    """
    This class represent the static properties of the Field Replaceable 
    Unit (FRU) on the network element.
    
    @undocumented: __init__
    """


    def __init__(self, ne, slot, alarm_type, product_id, serial_no, part_no, sw_version, fw_version, hw_version):
        """
        Constructor, for internal use only.
        """
        self.element = ne
        self.slot = slot
        self.alarm_type = alarm_type
        self.product_id = product_id
        self.serial_no = serial_no
        self.part_no = part_no
        self.sw_version = sw_version
        self.fw_version = fw_version
        self.hw_version = hw_version



    def __str__(self):
        return 'FRU [' + self.product_id + ']\n' + '\tSlot         : ' + str(self.slot) + '\n' + '\tAlarm Type   : ' + self.alarm_type + '\n' + '\tProduct ID   : ' + self.product_id + '\n' + '\tSerial No    : ' + self.serial_no + '\n' + '\tPart No      : ' + self.part_no + '\n' + '\tSW Version   : ' + self.sw_version + '\n' + '\tFW Version   : ' + self.fw_version + '\n' + '\tHW Version   : ' + self.hw_version + '\n'




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:21:10 IST
