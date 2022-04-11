# -- UTF-8 --
# date: 2022年4月11日
# made by: ourcwj

import os

from psutil import pid_exists


class pid_tools():
    def __init__(self, route, fileName = 'ms_pid.ms') -> None:
        # 初始化PID工具
        print('PID工具已载入')
        self.route = route+fileName # 获得文件路径
        # print('12345689')
        self.pid = os.getpid()  # 获得本进程的PID
        # print(self.pid)

    def new_pid(self):
        # 创建PID文件的函数
        if not os.path.isfile(self.route): # 判断文件是否存在
            # 不存在，创建文件并写入
            with open(self.route, mode='x')as i:
                i.write('%d'%(self.pid))
        else:
            # 存在，删除文件。然后再创建并写入数据
            os.remove(self.route) # 删除文件
            with open(self.route, mode='x')as i:
                # 写入PID
                i.write('%d'%(self.pid))


        # 这些代码不知道为什么不能用，有BUG

        # with open(self.route, mode='w+') as i:
        #     print('new_pid:', self.pid)
        #     i.write('why%d'%(self.pid))
        #     i.close()
        # with open(self.route, mode='w+') as i:
        #     print('777', i.read())



    def pid_if(self, pid = 0):
        # 判断PID文件是否存在的函数
        if pid == 0:
            if not os.path.isfile(self.route):
                return False
            else:
                with open(self.route) as i:
                    tmp = i.read()
                    
                    if pid_exists(int(tmp)):
                        return True
                    else:
                        return False
        else:
            return pid_exists(pid)

    def delete_pidFile(self):
        # 删除PID文件的函数
        if os.path.isfile(self.route):
            # 判断文件是都存在，如果存在则删除
            os.remove(self.route)
        # os.remove(self.route)
