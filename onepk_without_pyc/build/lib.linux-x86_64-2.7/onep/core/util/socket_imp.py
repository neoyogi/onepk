# 2015.02.05 17:18:08 IST
import socket
if not hasattr(socket, 'inet_pton'):
    import os
    if os.name == 'nt':
        from onep.core.util.win_inet_pton import inet_pton, inet_ntop
        socket.inet_pton = inet_pton
        socket.inet_ntop = inet_ntop

# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:18:08 IST
