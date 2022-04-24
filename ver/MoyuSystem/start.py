# -- UTF-8 --
# date: 2022年4月9日
# made by: ourcwj

# import configparser
import os
import sys
import time
import logging
import MS_BIOS
from MS_BIOS import execute
from MS_BIOS import GUI

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
    console  =  logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    logger.addHandler(console)
    logger.info('123')
    logger.debug('123')
    if bios.pid_inspect():
        print('14:', bios.pid.pid)
        print('PID互斥拒绝访问')
        time.sleep(5)
        sys.exit(403)
        
    else:
        bios.pid.new_pid()

    print('PID检查通过')
    gui = GUI.GUI()
    gui.windows()
    exit()
    
if __name__ == "__main__":
    main()
