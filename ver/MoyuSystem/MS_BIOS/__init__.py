# -- UTF-8 --
# date: 2022年4月9日
# made by: ourcwj

# 注意这里所有的 print 函数均是为了开发调试需要，可以删除（特殊备注除外）

import logging
# import configparser
import os
import sys

# import time
from MS_BIOS import PID

logger = logging.getLogger('MS_logging')
class BIOS():
    def __init__(self):
        #初始化ms_bios的数据
        self.wirte_fils = [
            'readme.txt', 
            'test.txt', 
            'test01.txt', 
            'test02.txt'
        ]

        self.content_fils = {
            'readme' : '写入测试', 
            'test' : 'test\n这是另一行字符', 
            'test01' : 'test01', 
            'test02' : 'test02'
        }


        self.appdataRoute = os.getenv('appdata')     # 获得appdata绝对的路径
        logger.debug('Obtained absolute path of appdata folder  path=%s'%(self.appdataRoute))
        file = self.appdataRoute + '\\ms'  # 设置ms的路径
        logger.debug('Get the absolute path of the configuration folder  path=%s'%(file))
        if not os.path.isdir(file):   # 判断路径是否存在
            # 不存在，创建路径 并把appdataRoute_if设置为“否”
            os.makedirs(file)
            logger.debug('Folder path %s does not exist, created'%(file))
            self.appdataRoute = file+'\\'
            self.appdataRoute_if = False
            logger.debug('The value of variable appdataRoute_if has been set to False')
            # print('if', self.appdataRoute_if)
        else:
            # 存在把appdataRoute_if设置为“是” 并把路径设置为ms路径
            self.appdataRoute_if = True
            logger.debug('The value of variable appdataRoute_if has been set to True')
            self.appdataRoute = file+'\\'
            # print(self.appdataRoute)

    def init(self):
        # MS初始化函数
        fileName_key = []
        fils = {}
        logger.debug('Created list [filename_key] and DICTIONARY [fils]')

        def addFils():
            for i in self.wirte_fils:
                # 分离路径，文件名称及后缀。并把绝对路径添加至fils字典, 将文件名（key）加入fileName_key列表
                tmp = self.appdataRoute+i
                logger.debug('Path connected:%s' % (tmp))
                # print('tmp:', tmp)
                (route, fileName) = os.path.split(tmp)
                logger.debug('Separated path and file name. path=%s  file name=%s' % (route, fileName))
                # print('file name:', fileName)
                (name, suffix) = os.path.splitext(fileName)
                logger.debug('Separated file name and suffix.  name=%s  suffix=%s' % (name, suffix))
                # print('name:', name)
                fileName_key.append(name)
                logger.debug('%s has been added to the end of list %s' % (name, 'fileName_key'))
                fils['%s' % (name)] = tmp
                logger.debug('Added %s to key %s of list fils' % (tmp, '%s' % (name)))
            # print(fils)

        def write():
            # 数据写入函数
            for i in fileName_key:
                # 利用递归fileName_key顺次读取fils的数据用于创建文件，并使用fileName_key的数据读取content_fils字典的内容用于写入
                with open(fils[i], 'w') as tmp:
                    logger.debug('Opened file %s' % (fils[i]))
                    tmp.write(self.content_fils[i])
                    logger.debug('Written %s to file %s', (self.content_fils[i], fils[i]))
                logger.debug('Closed file %s' % (fils[i]))


            # with open(fils['readme'], 'w') as tmp:
            #     tmp.write('写入测试')


        addFils()
        write()

    def selfInspection(self):
        # 自检函数

        if not self.appdataRoute_if:
            # 直接检擦路径是否存在
            logger.debug('Because the value of variable appdataRoute_if is False, False will be returned')
            return False
            

        fils = []

        for i in self.wirte_fils:
            # 建立将要检擦的文件的绝对路径
            fils.append(self.appdataRoute+ "%s" % (i))
            logger.debug('%s has been added to the end of the list fils'%(self.appdataRoute+ "%s" % (i)))
        # print(fils)
        tmp = True
        for i in fils:
            # 检擦文件
            logger.debug('Checking file %s'%(i))
            if not os.path.isfile(i):
                # 如果未发现文件将tmp设置为“否”并退出循环
                logger.debug('File %s does not exist, so false will be returned'%(i))
                tmp = False
                break
        
        return tmp



    def pid_inspect(self, file_route = None, file_custom = None, inspect_if = True, pid_custom = 0):
        logger.info('PID check in progress')
        # 判断各种使用可选参数的情况，以加以使用不同的运行方案
        if file_custom is None:
            # 判断是否使用了file_custom可选参数
            self.pid = PID.pid_tools(self.appdataRoute)
        elif file_route == None:
            self.pid = PID.pid_tools(self.appdataRoute, fileName=file_custom)
        else:
            self.pid = PID.pid_tools(file_route, fileName=file_custom)

        if inspect_if:
            if pid_custom == 0: # 判断是否使用了pid_custom可选参数
                return self.pid.pid_if()
            else:
                return self.pid.pid_if(pid=pid_custom)

