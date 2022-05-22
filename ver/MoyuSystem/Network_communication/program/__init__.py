import socket
import os
import sys
import threading

class sever(threading.Thread):
    def __init__(self, threadID: int, threadName: str, severIP: tuple, object: object):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = threadName
        self.ip = severIP
        self.object = object

    def run(self):
        pass