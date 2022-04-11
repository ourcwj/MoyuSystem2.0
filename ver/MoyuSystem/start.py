# -- UTF-8 --
# date: 2022年4月9日
# made by: ourcwj

# import configparser
# import os
import sys
import time

import MS_BIOS


def main():
    bios = MS_BIOS.BIOS()
    if not bios.selfInspection():
        print('未通过自检,准备初始化...')
        bios.init()
        print('已初始化。\n准备进行PID检查')
    else:
        print('已通过自检,准备进行PID检查')

    if bios.pid_inspect():
        print('14:', bios.pid.pid)
        print('PID互斥拒绝访问')
        time.sleep(5)
        sys.exit(403)
        
    else:
        bios.pid.new_pid()
    while True:
        print('PID检查通过')
        time.sleep(10000)
if __name__ == "__main__":
    main()
