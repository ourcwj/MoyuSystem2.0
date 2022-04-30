# -- UTF-8 --
# date: 2022年4月9日
# made by: ourcwj

from __future__ import print_function

import ctypes
import logging
# import configparser
import os
import sys
import time

import MS_BIOS
from MS_BIOS import GUI_side as GUI

# from MS_BIOS import execute
# from MS_BIOS import GUI

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

bios = MS_BIOS.BIOS()

def exit(code = 0):
    bios.pid.delete_pidFile()
    sys.exit(code)

def main():
    
    if not bios.selfInspection():
        print('未通过自检,准备初始化...')
        bios.init()
        print('已初始化。\n准备进行PID检查')
    else:
        print('已通过自检,准备进行PID检查')




    # ------------------------------------------
    # 这些是用来添加日志的，暂时没有大用，可注释
    logger = logging.getLogger('MS_logging')
    logger.setLevel(level=logging.DEBUG)
    file = bios.appdataRoute + time.strftime('%Y-%M %H-%M-%S') + '.log'
    if not os.path.isfile(file):
        with open(file, 'w') as t:
            t.close()
    handler  =  logging.FileHandler(file)
    handler.setLevel(logging.DEBUG)
    formatter  =  logging.Formatter( '[%(asctime)s]%(name)s - %(module)s - %(levelname)s : %(message)s' )
    handler.setFormatter(formatter)
    # console  =  logging.StreamHandler()
    # console.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    # logger.addHandler(console)
    logger.info('123')
    logger.debug('123')
    # ------------------------------------------




    if bios.pid_inspect():
        print('14:', bios.pid.pid)
        print('PID互斥拒绝访问')
        time.sleep(5)
        sys.exit(403)
        
    else:
        bios.pid.new_pid()

    print('PID检查通过')
    # GUI.startgui(bios.appdataRoute)  # 已被抛弃的代码，毫无用处！！！ 此代码调用了MS_BIOS的GUI模块。模块可删除（模块内代码已全部注释，取消注释仍然可用）
    gui = GUI.gui()

    # print('123')
    exit(code=gui.exec)
    
if __name__ == "__main__":
    if is_admin():
        main()
    else:
        if sys.version_info[0] == 3:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        else: #in python2.x
            ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)
