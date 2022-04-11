# -- UTF-8 --
# date: 2022年4月9日
# made by: ourcwj

from psutil import pid_exists
import os

class pid_tools():
    def __init__(self, route, fileName = 'ms_pid.ms') -> None:
        print('PID工具已载入')
        self.route = route+fileName
        # print('12345689')
        self.pid = os.getpid()
        # print(self.pid)

    def new_pid(self):


        if not os.path.isfile(self.route):
            with open(self.route, mode='x')as i:
                i.write('%d'%(self.pid))
        else:
            os.remove(self.route)
            with open(self.route, mode='x')as i:
                i.write('%d'%(self.pid))
        # with open(self.route, mode='w+') as i:
        #     print('new_pid:', self.pid)
        #     i.write('why%d'%(self.pid))
        #     i.close()
        # with open(self.route, mode='w+') as i:
        #     print('777', i.read())



    def pid_if(self, pid = 0):

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
        os.remove(self.route)
