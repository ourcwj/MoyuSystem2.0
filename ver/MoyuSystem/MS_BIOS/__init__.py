import configparser
import os
import time


class BIOS():
    def __init__(self):
        #初始化ms_bios的数据
        self.tmp_fils = ['readme.txt']
        self.appdataRoute = os.getenv('appdata')     # 获得appdata绝对的路径
        file = self.appdataRoute + '\\ms'  # 设置ms的路径
        if not os.path.isdir(file):   # 判断路径是否存在
            # 不存在，创建路径 并把appdataRoute_if设置为“否”
            os.makedirs(file)
            self.appdataRoute_if = False
            # print('if', self.appdataRoute_if)
        else:
            # 存在把appdataRoute_if设置为“是” 并把路径设置为ms路径
            self.appdataRoute_if = True
            self.appdataRoute = file+'\\'
            # print(self.appdataRoute)

    def init(self):
        # MS初始化函数
        fils = {}

        def addFils():
            for i in self.tmp_fils:
                # 分离路径，文件名称及后缀。并把绝对路径添加至fils字典
                tmp = self.appdataRoute+i
                (route, fileName) = os.path.split(tmp)
                # print('file name:', fileName)
                (name, suffix) = os.path.splitext(fileName)
                # print('name:', name)

                fils['%s' % (name)] = tmp
            # print(fils)

        def write():
            with open(fils['readme'], 'w') as tmp:
                tmp.write('写入测试')


        addFils()
        write()

    def selfInspection(self):
        # 自检函数

        if not self.appdataRoute_if:
            # 直接检擦路径是否存在
            return False
            

        fils = []

        for i in self.tmp_fils:
            # 建立将要检擦的文件的绝对路径
            fils.append(self.appdataRoute+ "%s" % (i))
        # print(fils)
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
