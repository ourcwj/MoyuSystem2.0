import configparser
import os
import time

import MS_BIOS


def main():
    bios = MS_BIOS.BIOS()
    if bios.appdataRoute_if:
        bios.selfInspection()

if __name__ == "__main__":
    main()