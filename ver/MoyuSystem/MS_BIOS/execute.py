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
    test = configobj.ConfigObj(filename, encoding='UTF8')
    tmp['name'] = test['name']['name']
    
def weitefile(route, name, dataP, dataA):
    datapdata = ''
    for line in open(dataP, mode='rb'):
        datapdata = datapdata + line
    tmp = {
        'name' : name, 
        'dataphoto' : datapdata, 
        'dataAn' : dataA
    }

    file = route + name + '.msdata'
    if not os.path.isfile(file):
        with open(file, mode='w', encoding='UTF-8') as t:
            t.close()
    else:
        return False
    test = configobj.ConfigObj(file, encoding='UTF-8')
    test['name'] = {}
    test['data'] = {}
    test['name']['name'] = tmp['name']
    test['data']['dataP'] = tmp['dataphoto']
    test['data']['dataA'] = tmp['dataAn']
    test.write()
