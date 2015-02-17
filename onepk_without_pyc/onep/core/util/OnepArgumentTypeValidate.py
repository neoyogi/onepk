# 2015.02.05 17:21:00 IST
from onep.core.exception.OnepIllegalArgumentException import OnepIllegalArgumentException

def validate(obj, obj_type):
    if not isinstance(obj, obj_type):
        var_type = type(obj)
        msg = str(var_type) + ' has been passed to API.'
        raise OnepIllegalArgumentException(msg + ' Expected ', str(obj_type))
    else:
        return True



def validate_none(obj, obj_name):
    if obj == None:
        raise OnepIllegalArgumentException(obj_name, 'None.')
    return True



def validatelist_none(obj_list):
    for item in obj_list:
        if item == None:
            raise OnepIllegalArgumentException('None argument passed to API.')

    return True



def validate_dictionary(obj):
    for key in obj:
        if not isinstance(key, obj[key]):
            var_type = type(key)
            msg = str(var_type) + ' has been passed to API.'
            raise OnepIllegalArgumentException(msg + ' Expected ', str(obj[key]))

    return True



def _validate_mac_address(item_list):
    if item_list == None:
        raise OnepIllegalArgumentException('mac address is none')
    if not isinstance(item_list, list):
        raise OnepIllegalArgumentException('Argument mac_addr is not a list.')
    if len(item_list) != 6:
        raise OnepIllegalArgumentException('Argument mac_addr list is not of length 6.')
    item_pos = 0
    for item in item_list:
        item_pos += 1
        if item > 255 or item < 0:
            raise OnepIllegalArgumentException('MAC address byte:' + str(item_pos) + ' is not in valid(0x00 <= Byte <= 0xFF) byte range')




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:21:00 IST
