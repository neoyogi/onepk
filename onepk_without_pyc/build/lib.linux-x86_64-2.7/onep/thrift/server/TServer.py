# 2015.02.05 17:20:17 IST
import logging
import sys
import os
import traceback
import threading
import Queue
from thrift.Thrift import TProcessor
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

class TServer:
    """Base interface for a server, which must have a serve method."""


    def __init__(self, *args):
        if len(args) == 2:
            self.__initArgs__(args[0], args[1], TTransport.TTransportFactoryBase(), TTransport.TTransportFactoryBase(), TBinaryProtocol.TBinaryProtocolFactory(), TBinaryProtocol.TBinaryProtocolFactory())
        elif len(args) == 4:
            self.__initArgs__(args[0], args[1], args[2], args[2], args[3], args[3])
        elif len(args) == 6:
            self.__initArgs__(args[0], args[1], args[2], args[3], args[4], args[5])



    def __initArgs__(self, processor, serverTransport, inputTransportFactory, outputTransportFactory, inputProtocolFactory, outputProtocolFactory):
        self.processor = processor
        self.serverTransport = serverTransport
        self.inputTransportFactory = inputTransportFactory
        self.outputTransportFactory = outputTransportFactory
        self.inputProtocolFactory = inputProtocolFactory
        self.outputProtocolFactory = outputProtocolFactory



    def serve(self):
        pass




class TSimpleServer(TServer):
    """Simple single-threaded server that just pumps around one transport."""


    def __init__(self, *args):
        TServer.__init__(self, *args)



    def serve(self):
        self.serverTransport.listen()
        while True:
            client = self.serverTransport.accept()
            itrans = self.inputTransportFactory.getTransport(client)
            otrans = self.outputTransportFactory.getTransport(client)
            iprot = self.inputProtocolFactory.getProtocol(itrans)
            oprot = self.outputProtocolFactory.getProtocol(otrans)
            try:
                while True:
                    self.processor.process(iprot, oprot)

            except TTransport.TTransportException as tx:
                pass
            except Exception as x:
                logging.exception(x)
            itrans.close()
            otrans.close()





class TThreadedServer(TServer):
    """Threaded server that spawns a new thread per each connection."""


    def __init__(self, *args, **kwargs):
        TServer.__init__(self, *args)
        self.daemon = kwargs.get('daemon', False)



    def serve(self):
        self.serverTransport.listen()
        while True:
            try:
                client = self.serverTransport.accept()
                t = threading.Thread(target=self.handle, args=(client,))
                t.setDaemon(self.daemon)
                t.start()
            except KeyboardInterrupt:
                raise 
            except Exception as x:
                logging.exception(x)




    def handle(self, client):
        itrans = self.inputTransportFactory.getTransport(client)
        otrans = self.outputTransportFactory.getTransport(client)
        iprot = self.inputProtocolFactory.getProtocol(itrans)
        oprot = self.outputProtocolFactory.getProtocol(otrans)
        try:
            while True:
                self.processor.process(iprot, oprot)

        except TTransport.TTransportException as tx:
            pass
        except Exception as x:
            logging.exception(x)
        itrans.close()
        otrans.close()




class TThreadPoolServer(TServer):
    """Server with a fixed size pool of threads which service requests."""


    def __init__(self, *args, **kwargs):
        TServer.__init__(self, *args)
        self.clients = Queue.Queue()
        self.threads = 10
        self.daemon = kwargs.get('daemon', False)



    def setNumThreads(self, num):
        """Set the number of worker threads that should be created"""
        self.threads = num



    def serveThread(self):
        """Loop around getting clients from the shared queue and process them."""
        while True:
            try:
                client = self.clients.get()
                self.serveClient(client)
            except Exception as x:
                logging.exception(x)




    def serveClient(self, client):
        """Process input/output from a client for as long as possible"""
        itrans = self.inputTransportFactory.getTransport(client)
        otrans = self.outputTransportFactory.getTransport(client)
        iprot = self.inputProtocolFactory.getProtocol(itrans)
        oprot = self.outputProtocolFactory.getProtocol(otrans)
        try:
            while True:
                self.processor.process(iprot, oprot)

        except TTransport.TTransportException as tx:
            pass
        except Exception as x:
            logging.exception(x)
        itrans.close()
        otrans.close()



    def serve(self):
        """Start a fixed number of worker threads and put client into a queue"""
        for i in range(self.threads):
            try:
                t = threading.Thread(target=self.serveThread)
                t.setDaemon(self.daemon)
                t.start()
            except Exception as x:
                logging.exception(x)

        self.serverTransport.listen()
        while True:
            try:
                client = self.serverTransport.accept()
                self.clients.put(client)
            except Exception as x:
                logging.exception(x)





class TForkingServer(TServer):
    """A Thrift server that forks a new process for each request"""


    def __init__(self, *args):
        TServer.__init__(self, *args)
        self.children = []



    def serve(self):

        def try_close(file):
            try:
                file.close()
            except IOError as e:
                logging.warning(e, exc_info=True)


        self.serverTransport.listen()
        while True:
            client = self.serverTransport.accept()
            try:
                pid = os.fork()
                if pid:
                    self.children.append(pid)
                    self.collect_children()
                    itrans = self.inputTransportFactory.getTransport(client)
                    otrans = self.outputTransportFactory.getTransport(client)
                    try_close(itrans)
                    try_close(otrans)
                else:
                    itrans = self.inputTransportFactory.getTransport(client)
                    otrans = self.outputTransportFactory.getTransport(client)
                    iprot = self.inputProtocolFactory.getProtocol(itrans)
                    oprot = self.outputProtocolFactory.getProtocol(otrans)
                    ecode = 0
                    try:
                        while True:
                            self.processor.process(iprot, oprot)

                    except TTransport.TTransportException as tx:
                        pass
                    except Exception as e:
                        logging.exception(e)
                        ecode = 1
                    finally:
                        try_close(itrans)
                        try_close(otrans)
                    os._exit(ecode)
            except TTransport.TTransportException as tx:
                pass
            except Exception as x:
                logging.exception(x)




    def collect_children(self):
        while self.children:
            try:
                (pid, status,) = os.waitpid(0, os.WNOHANG)
            except os.error:
                pid = None
            if pid:
                self.children.remove(pid)
            else:
                break





# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:20:18 IST
