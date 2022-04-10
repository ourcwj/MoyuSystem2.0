# -- UTF-8 --
# date: 2022年4月9日
# made by: ourcwj

from psutil import pid_exists
import os

class pid_tools():
    def __init__(self, route, fileName = 'ms_pid.ms') -> None:
        self.route = route+fileName
        self.pid = os.getpid()

    def new_pid(self):
        try:
            with open(self.route, 'w') as i:
                i.write(self.pid)
            return 0

        except:
            return 1

    def pid_if(self, pid = 0):

        if pid == 0:
            if not os.path.isfile(self.route):
                return False
            else:
                with open(self.route) as i:
                    tmp = i.read()
                    if pid_exists(tmp):
                        return True
                    else:
                        return False
        else:
            return pid_exists(pid)

    def delete_pidFile(self):
        os.remove(self.route)
