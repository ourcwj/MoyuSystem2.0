# -- UTF-8 --
# date: 2022年4月9日
# made by: ourcwj

# It cannot be used alone for the time being (please modify the source code if it is used alone.), Highly bound to moyusystem.
# 暂时不可单独使用（单独使用请修改源代码。），与MoyuSystem高度绑定。

# --------------------
# 一个网络通讯软件，功能简单直接
# 当然，没什么用（用QQ不好吗？？？）
# --------------------

import logging
import socket as s
import threading as th
# import GUI
from typing import Callable

import Network_communication.GUI
import Network_communication.program as ex

# server.daemon_threads = True


logger = logging.getLogger('MS_logging')

class window(th.Thread):
    def __init__(self, threadID: int, threadName: str) -> None:
        th.Thread.__init__(self)
        logger.debug('Thread ID is %d' % (threadID))
        self.threadID = threadID
        self.name = threadName
    def run(self):
        self.win = Network_communication.GUI.main_Window()
        self.win.show()


class ProGram(th.Thread):
    def __init__(self, threadID: int, threadName: str) -> None:
        th.Thread.__init__(self)
        logger.debug('Thread ID is %d' % (threadID))
        self.threadID = threadID
        self.name = threadName

    def run(self) -> None:
        self.window_main = window(2, 'window_comm')
        
        self.window_main.start()
        logger.info('Thread window started')
        self.window_main.join()
        # self.exitId = self.window_main.win
        
class client(th.Thread):
    def __init__(self, threadID: int = 0, threadName: str = 'new_thread', window_object = None)->None:
        th.Thread.__init__(self)
        self.threadID = threadID
        self.name = threadName
        self.object = window_object
        self.object.get_thread(self)
        self.sever = s.socket(s.AF_INET, s.SOCK_STREAM)

    def run(self):
        pass

    def con(self, ip) -> bool:
        try:
            self.sever.connect(ip)
            return True
        except s.error:
            return False

