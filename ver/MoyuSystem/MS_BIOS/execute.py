# -- UTF-8 --
# date: 2022年4月24日
# made by: ourcwj

import logging
import os
import sys
import time
from shlex import split

import configobj
from MyQR import myqr

from MS_BIOS import error

logger = logging.getLogger('MS_logging')

def qrcode(di, object) -> bool:
    tmp = {}
    tmp['name'] = time.strftime('%Y-%M %H-%M-%S') + '.png'
    tmp['str'] = di['str']
    tmp['rou'] = di['rou']
    if di['len_if']:
        tmp['len'] = di['len']
    else:
        tmp['len'] = 5
    if di['isPhoto']:
        if os.path.isfile(di['rou_photo']):
            tmp['rou_photo'] = di['rou_photo']
        else:
            return False

        tmp['isCS'] = di['isCS']
    else:
        tmp['rou_photo'] = 'hknifucnhnhnhnhgivtestrg741758714bbbrgts51'
    
    try:
        if not os.path.isdir(tmp['rou']):
            os.makedirs(tmp['rou'])

    except BaseException as t:
        print(t)
        return False

    try:
        if tmp['rou_photo'] == 'hknifucnhnhnhnhgivtestrg741758714bbbrgts51':
            myqr.run(
                words = tmp['str'], 
                version=tmp['len'], 
                level='L', 
                save_dir=tmp['rou'], 
                save_name=tmp['name']
            )
            return True
        else:
            myqr.run(
                words = tmp['str'], 
                version=tmp['len'], 
                level='L', 
                save_dir=tmp['rou'], 
                picture=tmp['rou_photo'], 
                colorized=tmp['isCS'], 
                save_name=tmp['name']
            )
            return True
    except BaseException as t:
        logger.error(str(t))
        error.newError(object.appdataRoute, text=t)
        return False

class host:
    def __init__(self) -> None:
        self.hos_list = []
        self.hos = {}
        self.path = 'C:\\Windows\\System32\\drivers\\etc\\hosts'
        self.read()

    def read(self):
        self.tmp = 'hlnsieeeeeeeermrjmed148543486s1b4rt3s4b798169783419783466^&*^(*@&^#*&@^($*$@#'
        self.hos_list = []
        self.hos = {}
        with open(self.path, mode='r', encoding='UTF-8')as t:
            for lian in t:
                if not (lian[0] == '#' or lian[0] == '' or lian[0] == '\n' or lian[0] == '﻿'):
                    # print(lian)
                    tmp = split(lian)
                    # print(tmp)
                    self.hos_list.append(tmp[1])
                    self.hos[tmp[1]] = tmp[0]
                    # print('hos_list', self.hos_list)
                    # print('hos', self.hos)

    def wi(self):
        tmp = ''
        with open(self.path, mode='w', encoding='UTF-8')as t:
            for i in self.hos_list:
                if not i == self.tmp:
                    tmp = tmp + '\n' + self.hos[i] + '    ' + i
            t.write(tmp)

    def del_r(self, ob):
        self.tmp = ob
        self.wi()
        self.tmp = 'hlnsieeeeeeeermrjmed148543486s1b4rt3s4b798169783419783466^&*^(*@&^#*&@^($*$@#'
















# ------------------------------------------------------------
# 应付学校的关于错题读取与写入的函数，随便删
def readFile(filename):
    tmp = {}
    test = configobj.ConfigObj(filename, encoding='UTF-8')
    tmp['name'] = test['name']['name']
    tmp['answer'] = test['data']['dataA']
    tmp['photo'] = test['data']['photo']
    return tmp
def weitefile(route, name, dataP, answer):
    # (tmp_123, fileName) = os.path.split(dataP)
    # (name_file, suffix) = os.path.splitext(fileName)
    file = route + name + '.msdata'
    # if not os.path.isfile(file):
    #     with open(file, mode='w', encoding='UTF-8') as t:
    #         t.close()
    # else:
    #     return False
    # datapdata = b''
    test = configobj.ConfigObj(file, encoding='UTF-8')
    test['name'] = {}
    test['data'] = {}
    # photo = route + name + suffix
    # with open(dataP, mode='rb')as t:
    #     with open(photo, mode='wb')as w:
    #         while 1:
    #             data_tmp = t.read(1024)
    #             if not len(data_tmp):
    #                 break
    #             print(data_tmp)
    #             w.write(data_tmp)
    tmp = {
        'name' : name, 
        'dataphoto' : dataP, 
        'dataAn' : answer
    }
    test['name']['name'] = tmp['name']
    test['data']['dataA'] = tmp['dataAn']
    test['data']['photo'] = tmp['dataphoto']
    test.write()
# ------------------------------------------------------------
