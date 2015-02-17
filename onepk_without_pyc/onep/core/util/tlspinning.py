# 2015.02.05 17:21:00 IST
"""The module for the TLS certificate pinning mechanism.

Pinning is the process by which certain hosts can be whitelisted for TLS
verification.  If the presented certificate matches the known certificate
for that host in the pinning file, that connection proceeds even if
the certificate fails the customary TLS verification.

"""
from abc import ABCMeta, abstractmethod
import errno
try:
    import fcntl
except ImportError:
    _fcntl_exists = False
else:
    _fcntl_exists = True
import logging
import os
import string
import thread
from onep.core.exception import OnepIllegalArgumentException
from onep.core.util.Enum import enum
_LOGGER = logging.getLogger(__name__)
_LOCK = thread.allocate_lock()
_VERSION = '# OneP Certificate Pinning Version 1.0'
_CLOSING_SENTINEL = '<EOF Marker>'
_DELIMITERS = string.whitespace + ','
_TRANSTABLE = string.maketrans(_DELIMITERS, ' ' * len(_DELIMITERS))

def _get_entry(file_path, host):
    if not file_path:
        raise OnepIllegalArgumentException('file_path', file_path)
    if not host:
        raise OnepIllegalArgumentException('host', host)
    f = None
    line = None
    ret = None
    error = False
    _LOCK.acquire()
    try:
        f = open(file_path, 'rb')
        if _fcntl_exists:
            fcntl.lockf(f, fcntl.LOCK_SH)
        for line in f:
            if ret is not None:
                continue
            if line.startswith('#'):
                continue
            if line.startswith('<'):
                continue
            content = line.partition('#')[0]
            tokens = content.translate(_TRANSTABLE).split()
            if len(tokens) != 3:
                error = True
                continue
            if host.lower() == tokens[0].lower():
                ret = tuple(tokens)

    finally:
        if f:
            f.close()
        _LOCK.release()
    if not error and (not line or _CLOSING_SENTINEL != line.rstrip()):
        error = True
    if error:
        _LOGGER.error("One or more errors occurred while processing file '%s'.  The file is possibly corrupted.", file_path)
    return ret



def _update_entry(file_path, entry):
    if not file_path:
        raise OnepIllegalArgumentException('file_path', file_path)
    if not isinstance(entry, (tuple, list)) or len(entry) != 3:
        raise OnepIllegalArgumentException('entry', entry)
    fd = -1
    f = None
    fcopy = None
    line = None
    error = False
    _LOCK.acquire()
    try:
        try:
            fd = os.open(file_path, os.O_RDWR | os.O_CREAT | os.O_EXCL, 420)
        except OSError as e:
            if e.errno == errno.EEXIST:
                f = open(file_path, 'r+b')
            else:
                raise e
        else:
            f = os.fdopen(fd, 'r+b')
        if _fcntl_exists:
            fcntl.lockf(f, fcntl.LOCK_EX)
        try:
            fdcopy = os.open(file_path + '.tmp', os.O_RDWR | os.O_CREAT | os.O_EXCL, 384)
        except OSError as e:
            if e.errno == errno.EEXIST:
                fcopy = open(file_path + '.tmp', 'r+b')
                for line in fcopy:
                    pass

                if line and _CLOSING_SENTINEL == line.rstrip():
                    f.truncate(0)
                    fcopy.seek(0)
                    f.writelines(fcopy.readlines())
                    _LOGGER.warn("The file '%s' was recovered from a working copy.", file_path)
                else:
                    _LOGGER.error("A working copy of the file '%s' was found but could not be recovered.", file_path)
                fcopy.truncate(0)
                fcopy.seek(0)
            else:
                raise e
        else:
            fcopy = os.fdopen(fdcopy, 'r+b')
        fcopy.write(_VERSION + os.linesep)
        past_first_line = False
        line = None
        for line in f:
            if line.startswith('#'):
                if not past_first_line:
                    continue
            elif line.startswith('<'):
                continue
            else:
                content = line.partition('#')[0]
                tokens = content.translate(_TRANSTABLE).split()
                if len(tokens) == 3:
                    if tokens[0].lower() == entry[0].lower():
                        continue
                else:
                    error = True
            fcopy.write(line.rstrip())
            fcopy.write(os.linesep)
            past_first_line = True

        fcopy.write('%s,%s,%s' % entry)
        fcopy.write(os.linesep)
        fcopy.write(_CLOSING_SENTINEL)
        fcopy.write(os.linesep)
        fcopy.flush()
        os.fsync(fcopy.fileno())
        f.truncate(0)
        f.seek(0)
        fcopy.seek(0)
        f.writelines(fcopy.readlines())
    finally:
        if f:
            f.close()
        if fcopy:
            fcopy.close()
            os.remove(file_path + '.tmp')
        _LOCK.release()
    if not error and fd == -1 and not line or _CLOSING_SENTINEL != line.rstrip():
        error = True
    if error:
        _LOGGER.error("One or more errors occurred while processing file '%s'.  The file is possibly corrupted.", file_path)


DecisionType = enum('REJECT', 'ACCEPT_AND_PIN', 'ACCEPT_ONCE')

class TLSUnverifiedElementHandler(object):
    """
        This class represents a handler for TLS connections in which the network
        element has not been verified.
        
        The class that wants to process unverified TLS connections and decide
        whether to accept or reject them should subclass this class.
    
        """

    __metaclass__ = ABCMeta

    @abstractmethod
    def handle_verify(self, host, hash_type, fingerprint, changed):
        """Invoked when a the network element could not be verified.
        
                @param host:        The hostname of the network element.
                @type  host:        C{str}
                @param hash_type:   The hashing algorithm used for the fingerprint.
                @type  hash_type:   C{str}
                @param fingerprint: The fingerprint of the presented ceritificate.
                @type  fingerprint: C{str}
                @param changed:     True if and only if there is an entry for the host
                                    in the pinning file but the presented certificate
                                    did not match the pinned certificate.
                @type  changed:     C{bool}
                @return: The action to take on the connection.
                @rtype:  L{DecisionType}
        
                """
        return DecisionType.REJECT




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:21:01 IST
