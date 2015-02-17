# 2015.02.05 17:20:16 IST
from protocol import TBinaryProtocol
from transport import TTransport

def serialize(thrift_object, protocol_factory = TBinaryProtocol.TBinaryProtocolFactory()):
    transport = TTransport.TMemoryBuffer()
    protocol = protocol_factory.getProtocol(transport)
    thrift_object.write(protocol)
    return transport.getvalue()



def deserialize(base, buf, protocol_factory = TBinaryProtocol.TBinaryProtocolFactory()):
    transport = TTransport.TMemoryBuffer(buf)
    protocol = protocol_factory.getProtocol(transport)
    base.read(protocol)
    return base



# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:20:16 IST
