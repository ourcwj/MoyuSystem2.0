# -- UTF-8 --
# date: 2022年4月24日
# made by: ourcwj

import os
import sys
import MS_BIOS as BIOS
from start import bios

def exit(code = 0):
    bios.pid.delete_pidFile()
    sys.exit(code)

def add():
    pass