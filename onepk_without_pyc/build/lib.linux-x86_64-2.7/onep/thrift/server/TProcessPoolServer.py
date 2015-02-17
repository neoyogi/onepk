# 2015.02.05 17:20:18 IST
import logging
from multiprocessing import Process, Value, Condition, reduction
from TServer import TServer
from thrift.transport.TTransport import TTransportException

class TProcessPoolServer(TServer):
    """
    Server with a fixed size pool of worker subprocesses which service requests.
    Note that if you need shared state between the handlers - it's up to you!
    Written by Dvir Volk, doat.com
    """


    def __init__(self, *args):
        TServer.__init__(self, *args)
        self.numWorkers = 10
        self.workers = []
        self.isRunning = Value('b', False)
        self.stopCondition = Condition()
        self.postForkCallback = None



    def setPostForkCallback(self, callback):
        if not callable(callback):
            raise TypeError('This is not a callback!')
        self.postForkCallback = callback



    def setNumWorkers(self, num):
        """Set the number of worker threads that should be created"""
        self.numWorkers = num



    def workerProcess(self):
        """Loop around getting clients from the shared queue and process them."""
        if self.postForkCallback:
            self.postForkCallback()
        while self.isRunning.value == True:
            try:
                client = self.serverTransport.accept()
                self.serveClient(client)
            except (KeyboardInterrupt, SystemExit):
                return 0
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

        except TTransportException as tx:
            pass
        except Exception as x:
            logging.exception(x)
        itrans.close()
        otrans.close()



    def serve(self):
        """Start a fixed number of worker threads and put client into a queue"""
        self.isRunning.value = True
        self.serverTransport.listen()
        for i in range(self.numWorkers):
            try:
                w = Process(target=self.workerProcess)
                w.daemon = True
                w.start()
                self.workers.append(w)
            except Exception as x:
                logging.exception(x)

        while True:
            self.stopCondition.acquire()
            try:
                self.stopCondition.wait()
                break
            except (SystemExit, KeyboardInterrupt):
                break
            except Exception as x:
                logging.exception(x)

        self.isRunning.value = False



    def stop(self):
        self.isRunning.value = False
        self.stopCondition.acquire()
        self.stopCondition.notify()
        self.stopCondition.release()




# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2015.02.05 17:20:18 IST
