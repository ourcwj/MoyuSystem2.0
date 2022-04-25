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
    rou = os.getenv('temp') + '\\ms\\'
    if not os.path.isdir(rou):
        os.makedirs(rou)
    tmp = {}
    test = configobj.ConfigObj(filename, encoding='UTF-8')
    tmp['name'] = test['name']['name']
    tmp_rou = rou + test['data']['photoname']
    if os.path.isfile(tmp_rou):
        os.remove(tmp_rou)
    with open(tmp_rou, mode='wb') as t:
        t.write(str.encode(test['data']['dataP']))
    # tmp['photo'] = test['data']['dataP']
    tmp['photo'] = tmp_rou
    tmp['answer'] = test['data']['dataA']
    return tmp
    
def weitefile(route, name, dataP, dataA):
    datapdata = ''
    datapdata = bytes(datapdata, encoding='UTF-8')
    for line in open(dataP, mode='rb'):
        datapdata = datapdata + line
    tmp = {
        'name' : name, 
        'dataphoto' : datapdata, 
        'dataAn' : dataA
    }

    file = route + '\\' + name + '.msdata'
    if not os.path.isfile(file):
        with open(file, mode='w', encoding='UTF-8') as t:
            t.close()
    else:
        return False
    test = configobj.ConfigObj(file, encoding='UTF-8')
    (tmp_123, fileName) = os.path.split(dataP)
    test['name'] = {}
    test['data'] = {}
    test['name']['name'] = tmp['name']
    test['data']['dataP'] = tmp['dataphoto']
    test['data']['dataA'] = tmp['dataAn']
    test['data']['photoname'] = fileName
    test.write()
