# -- UTF-8 --
# date: 2022年4月11日
# made by: ourcwj

import os
import logging
from psutil import pid_exists


class pid_tools():
    def __init__(self, route, fileName = 'ms_pid.ms.pid') -> None:
        # 初始化PID工具
        self.logger = logging.getLogger('MS_logging')
        # self.logger.info('test')
        self.logger.info('PID工具以载入')
        # print('PID工具已载入')
        self.route = route+fileName # 获得文件路径
        # print('12345689')
        self.pid = os.getpid()  # 获得本进程的PID
        # print(self.pid)

    def new_pid(self):
        # 创建PID文件的函数
        self.logger.debug('即将判断pid文件是否存在')
        if not os.path.isfile(self.route): # 判断文件是否存在
            self.logger.debug('PID文件不存在，即将创建并写入PID数据')
            # 不存在，创建文件并写入
            with open(self.route, mode='x')as i:
                i.write('%d'%(self.pid))
                self.logger.debug('创建并写入完成')
        else:
            self.logger.debug('文件存在，即将删除文件')
            # 存在，删除文件。然后再创建并写入数据
            os.remove(self.route) # 删除文件
            self.logger.debug('已删除文件')
            with open(self.route, mode='x')as i:
                # 写入PID
                i.write('%d'%(self.pid))
                self.logger.debug('文件已创建并写入')


        # 这些代码不知道为什么不能用，有BUG

        # with open(self.route, mode='w+') as i:
        #     print('new_pid:', self.pid)
        #     i.write('why%d'%(self.pid))
        #     i.close()
        # with open(self.route, mode='w+') as i:
        #     print('777', i.read())



    def pid_if(self, pid = 0):
        # 判断PID文件是否存在的函数
        self.logger.debug('正在判断PID互斥')
        if pid == 0:
            if not os.path.isfile(self.route):
                self.logger.debug('不存在文件，通过')
                self.logger.info('PID检查通过')
                return False
            else:
                self.logger.debug('存在PID文件')
                with open(self.route) as i:
                    tmp = i.read()
                    self.logger.debug('已读取PID文件， pid数值为：%s' % (tmp))
                    
                    if pid_exists(int(tmp)):
                        self.logger.debug('PID进程存在，检查不通过')
                        self.logger.info('PID检查不通过')
                        return True
                    else:
                        self.logger.debug('PID进程不存在，检查通过')
                        self.logger.info('PID检查通过')
                        return False
        else:
            self.logger.debug('已指定PID，将返回直接检查的结果')
            return pid_exists(pid)

    def delete_pidFile(self):
        # 删除PID文件的函数
        self.logger.debug('即将删除PID文件')
        if os.path.isfile(self.route):
            # 判断文件是都存在，如果存在则删除
            os.remove(self.route)
            self.logger.info('已删除PID文件')
        # os.remove(self.route)
