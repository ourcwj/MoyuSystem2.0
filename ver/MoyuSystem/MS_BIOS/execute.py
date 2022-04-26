# -- UTF-8 --
# date: 2022年4月24日
# made by: ourcwj

import os
import sys
import time
import MS_BIOS as BIOS
import configobj

def add():
    pass

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
