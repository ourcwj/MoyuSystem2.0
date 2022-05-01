# -- UTF-8 --
# date: 2022年4月11日
# made by: ourcwj

import logging
import os

from psutil import pid_exists


class pid_tools():
    def __init__(self, route, fileName = 'ms_pid.ms.pid') -> None:
        # 初始化PID工具
        self.logger = logging.getLogger('MS_logging')
        # self.logger.info('test')
        self.logger.info('PID tool to load')
        # print('PID工具已载入')
        self.route = route+fileName # 获得文件路径
        self.logger.debug('The PID file path obtained is %s'%(self.route))
        # print('12345689')
        self.pid = os.getpid()  # 获得本进程的PID
        self.logger.debug('The obtained PID of this process is %d'%(self.pid))
        # print(self.pid)

    def new_pid(self):
        self.logger.info('About to create a new PID file')
        # 创建PID文件的函数
        self.logger.debug('About to determine whether the PID file exists')
        if not os.path.isfile(self.route): # 判断文件是否存在
            self.logger.debug('The PID file does not exist. The PID data will be created and written soon')
            # 不存在，创建文件并写入
            with open(self.route, mode='x')as i:
                self.logger.debug('Opened file %s'%(self.route))
                i.write('%d'%(self.pid))
                self.logger.debug('Written %d to file %s'%(self.pid, self.route))
                self.logger.info('Create and write complete')
            self.logger.debug('Closed file %s'%(self.route))
        else:
            self.logger.debug('The file exists and will be deleted')
            # 存在，删除文件。然后再创建并写入数据
            os.remove(self.route) # 删除文件
            self.logger.debug('PID file deleted')
            with open(self.route, mode='x')as i:
                # 写入PID
                self.logger.debug('Opened file %s'%(self.route))
                i.write('%d'%(self.pid))
                self.logger.debug('Written %d to file %s'%(self.pid, self.route))
            self.logger.debug('Closed file %s'%(self.route))
            self.logger.info('文件已创建并写入')


        # 这些代码不知道为什么不能用，有BUG

        # with open(self.route, mode='w+') as i:
        #     print('new_pid:', self.pid)
        #     i.write('why%d'%(self.pid))
        #     i.close()
        # with open(self.route, mode='w+') as i:
        #     print('777', i.read())



    def pid_if(self, pid = 0):
        # 判断PID文件是否存在的函数
        self.logger.debug('Judging PID mutex')
        if pid == 0:
            if not os.path.isfile(self.route):
                self.logger.debug('No file exists, pass')
                self.logger.info('PID check passed')
                return False
            else:
                self.logger.debug('PID file exists')
                with open(self.route) as i:
                    tmp = i.read()
                    self.logger.debug('The PID file has been read, and the PID value is:%s' % (tmp))
                    
                    if pid_exists(int(tmp)):
                        self.logger.debug('PID process exists, check failed')
                        # self.logger.info('PID检查不通过')
                        return True
                    else:
                        self.logger.debug('PID process does not exist, check passed')
                        # self.logger.info('PID检查通过')
                        return False
        else:
            ttt = pid_exists(pid)
            self.logger.debug('PID has been specified, the result of direct check will be returned.The result is %s'%(str(ttt)))
            return ttt

    def delete_pidFile(self):
        # 删除PID文件的函数
        self.logger.debug('The PID file is about to be deleted')
        if os.path.isfile(self.route):
            # 判断文件是都存在，如果存在则删除
            os.remove(self.route)
            self.logger.info('PID file deleted')
        # os.remove(self.route)
