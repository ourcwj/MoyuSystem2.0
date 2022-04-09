# -- UTF-8 --
# date: 2022年4月9日
# made by: ourcwj

import configparser
import os
import time

import MS_BIOS


def main():
    bios = MS_BIOS.BIOS()
    if not bios.selfInspection():
        print('未通过自检')
        bios.init()
    else:
        print('已通过自检')

if __name__ == "__main__":
    main()
