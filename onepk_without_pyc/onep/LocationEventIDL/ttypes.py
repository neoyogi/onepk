# 2015.02.05 17:21:35 IST
from thrift.Thrift import *
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
    from thrift.protocol import fastbinary
except:
    fastbinary = None

# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:21:35 IST
