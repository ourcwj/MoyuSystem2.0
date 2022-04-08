import configparser
import os
import time


class BIOS():
    def __init__(self):
        #初始化ms_bios的数据
        self.appdataRoute = os.getenv('appdata')     # 获得appdata绝对的路径
        file = self.appdataRoute + '\\ms'  # 设置ms的路径
        if not os.path.isdir(file):   # 判断路径是否存在
            # 不存在，创建路径 并把appdataRoute_if设置为“否”
            os.makedirs(file)
            self.appdataRoute_if = False
        else:
            # 存在把appdataRoute_if设置为“是” 并把路径设置为ms路径
            self.appdataRoute_if = True
            self.appdataRoute = file

    def init(self):
        # MS初始化函数
        pass
    
    def selfInspection(self):
        # 自检函数
        fils_tmp = ['init.ini']  # 要检查的文件
        fils = []
        for i in fils_tmp:
            # 建立将要检擦的文件的绝对路径
            fils.append(self.appdataRoute+"\\%s" % (i))
        tmp = True
        for i in fils:
            # 检擦文件
            if not os.path.isfile(i):
                # 如果未发现文件将tmp设置为“否”并退出循环
                tmp = False
                break
        
        return tmp


        '''
        # 以下代码已废弃


        # initFile = self.appdataRoute + "\\init.ini"
        # if not os.path.os.path.isfile(initFile):
        #     with open(initFile, 'w') as file_init:
        #         inof = '#test'
        #         file_init.write(inof)
        #     self.init()

        # else:
        #     init_ini = configparser.ConfigParser()
        #     init_ini.read(initFile)
        #     self.initState = init_ini.get('inof', 'edition')
        '''