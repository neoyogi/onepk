# 2015.02.05 17:20:59 IST

class OnepIllegalEnumException(ValueError):
    pass

def getEnumVal(self, value):
    for x in self.keys():
        v = eval('self.' + x)
        if value == v:
            return x

    message = 'Enum value requested is ' + str(value) + ' is invalid'
    raise OnepIllegalEnumException(message)



def getIntVal(self, value):
    value_is_valid = value in self.keys()
    if value_is_valid:
        try:
            v = eval('self.' + value)
        except:
            value_is_valid = False
    if not value_is_valid:
        message = 'Enum value provided is ' + str(value) + ' is invalid'
        raise OnepIllegalEnumException(message)
    return v



def _isValid(self, value):
    try:
        if self.toInteger(self.enumval(value)) == value:
            return True
    except OnepIllegalEnumException as e:
        return False
    return False



def _keys(self):
    result = []
    for attr in dir(self):
        if attr.startswith('__'):
            break
        else:
            result.append(attr)

    return result



def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), enumval=getEnumVal, toInteger=getIntVal, _is_valid=_isValid, keys=_keys, **named)
    newType = type('Enum', (), enums)
    return newType()



def isValidEnum(self, value):
    if self is None or value is None:
        return False
    return _isValid(self, value)



# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:21:00 IST
