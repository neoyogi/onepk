# 2015.02.05 17:20:59 IST
from onep.core.util.Enum import enum
from onep.core.util.OnepConstants import OnepConstants
from onep.core.util.OnepStatus import OnepStatus
from onep.core.util.Period import Period
from onep.core.util.HostIpCheck import HostIpCheck
try:
    from onep.core.util.LicensingService import LicensingService
except ImportError:
    pass
from onep.core.util.Version import Version
from functools import wraps
import inspect

def deprecated(replacement = None):
    """
        This is a decorator to deprecate a function.
        Deprecating __init__ function of a class means the class itself is deprecated.
        The parameter replacement is the replacement of the deprecated function or class.
        This decorator prints a warning message before running the deprecated function.
    
        Ex1: deprecate class InterfaceBandwidthFilter using class InterfaceFilter
        @deprecated(InterfaceFilter)
        def __init__(self,interface=None,interface_type=None):
        
        >>> filter=InterfaceBandwidthFilter(interface_type=NetworkInterface.InterfaceTypes.ONEP_IF_TYPE_ETHERNET)
        WARNING:onep.core.util:onep.interfaces.InterfaceBandwidthFilter is deprecated; Use <class 'onep.interfaces.InterfaceFilter.InterfaceFilter'> instead
    
        Ex2: deprecate func using newFunc
        >>> from onep.core.util import deprecated
        >>> def newFunc():
        ...   print "hello"
        ...
        >>> @deprecated(newFunc)
        ... def func():
        ...   print "old hello"
        ...
        >>> func
        <function func at 0xf744cdf4>
        >>> func()
        WARNING:onep.core.util:func is deprecated; Use <function newFunc at 0xf7425f44> instead
        old hello
        >>>
        """

    def outer(func):
        if func.__name__ == '__init__':
            frm = inspect.stack()[1]
            mod = inspect.getmodulename(inspect.getfile(frm[0]))
            msg = '%s is deprecated' % mod
        else:
            msg = '%s is deprecated' % func.__name__
        if replacement:
            msg += '; Use %s instead' % replacement

        @wraps(func)
        def inner(*arg, **kwargs):
            import logging
            logging.basicConfig(level=logging.WARNING)
            logger = logging.getLogger(__name__)
            logger.warning(msg)
            return func(*arg, **kwargs)


        return inner


    return outer



# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:20:59 IST
