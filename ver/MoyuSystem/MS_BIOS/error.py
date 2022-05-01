import logging
import os
import time

import win32api
import win32con

logger = logging.getLogger('MS_logging')

def newError(route, text):
    route = route+'error\\'
    if not os.path.isdir(route):
        os.makedirs(route)
    file_name = route + time.strftime('%Y-%M %H-%M-%S') + '.error.txt'

    if os.path.isfile(file_name):
        os.remove(file_name)
        with open(file_name, mode='w', encoding='UTF-8') as t:
            t.write(str(text))
    else:
        with open(file_name, mode='w', encoding='UTF-8') as t:
            t.write(str(text))
    # logging.error(str(text))
    win32api.MessageBox(0, "MoyuSystem在运行时发生了一个错误！\n错误已被捕捉，希望您将本次运行的日志及错误文件发送给开发者。\n谢谢！", "MoyuSystem错误捕捉",win32con.MB_ICONWARNING)
