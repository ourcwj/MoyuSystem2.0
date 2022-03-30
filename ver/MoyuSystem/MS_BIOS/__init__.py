import configparser
from distutils.log import info
import os
import time


class BIOS():
    def __init__(self):
        self.appdataRoute = os.getenv('appdata')
        file = self.appdataRoute + '\\ms'
        if not os.path.isdir(file):
            os.makedirs(file)
            self.appdataRoute_if = False
        else:
            self.appdataRoute_if = True
            self.appdataRoute = file
    def init(self):
        pass
    
    def selfInspection(self):
        initFile = self.appdataRoute + "\\init.ini"
        if not os.path.os.path.isfile(initFile):
            with open(initFile, 'w') as file_init:
                inof = 'test'
                file_init.write(inof)

            return False
        else:
            init_ini = configparser.ConfigParser()
            init_ini.read(initFile)
            self.initState = init_ini.get('inof', 'edition')