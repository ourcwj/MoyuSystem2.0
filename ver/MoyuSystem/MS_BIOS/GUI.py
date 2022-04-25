# -- UTF-8 --
# date: 2022年4月18日
# made by: ourcwj

import tkinter as tk
from MS_BIOS import execute as ex
 
windows_root = tk.Tk()
windows_root.title('MoyuSystem')
windows_root.resizable(False, False)
windows_root.attributes("-alpha",1)
windows_root.geometry('600x300')


route_root = None

def add():
    ex.weitefile(route=route_root, )


class GUI:
    def __init__(self) -> None:
        main = tk.Menu(windows_root)
        main.add_command(label='添加', command=add)
        windows_root.config(menu=main)
    def windows(self):
        
        windows_root.mainloop()
        
        
def startgui(route):
    route_root = route