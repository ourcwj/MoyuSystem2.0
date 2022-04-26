# -- UTF-8 --
# date: 2022年4月18日
# made by: ourcwj

import os
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
from MS_BIOS import execute as ex
from tkinter import END, messagebox
 
windows_root = tk.Tk()
windows_root.title('MoyuSystem')
windows_root.resizable(False, False)
windows_root.attributes("-alpha",1)
windows_root.geometry('600x300')


def startgui(route):
    global ww_23
    ww_23 = route
    gui = GUI()
    gui.windows()

def open_1():
    path = ww_23
    files= os.listdir(path)
    s = []
    a = ()
    tmp = -1
    for i in files:
        tmp = tmp + 1
        if not os.path.isdir(i):
            (tmp_123, fileName) = os.path.split(i)
            (name_file, suffix) = os.path.splitext(fileName)
            if suffix == '.msdata':
                s.append(i)
                tmp_qwe = ('',name_file)
                a = a + tmp_qwe
    open_windows = tk.Toplevel()
    open_windows.title('选择')
    open_windows.resizable(False, False)
    w1 = tk.Message(open_windows, text='选择一个题目')
    w1.pack()
    cbox = ttk.Combobox(open_windows)
    cbox.pack()
    cbox['value'] = a
    def func(event):
        tmp_tx = cbox.get()
        tmp_11 = ww_23 + tmp_tx + '.msdata'
        qwe = ex.readFile(tmp_11)
        open_windows.destroy()
        s_windows = tk.Toplevel()
        s_windows.title('查看')
        s_windows.resizable(False, False)
        an = qwe['answer']
        ph = qwe['photo']
        # img_open = Image.open(ph)
        # img_png = ImageTk.PhotoImage(img_open)
        # label_img = tk.Label(s_windows, image = img_png)
        # label_img.pack()
        t9 = tk.Text(s_windows,width=50,height=20)
        t9.pack()
        t9.insert(1.0, ph)
        t = tk.Text(s_windows,width=50,height=20)
        t.pack()
        t.insert(1.0, an)



    cbox.bind("<<ComboboxSelected>>",func)

def add():
    def en():
        na = e.get()
        an = t.get(1.0,END)
        ph = t8.get(1.0,END)
        ex.weitefile(ww_23, na, ph, an)
        add_windows.destroy()

    def check():
        tmp = su1.get()
        if os.path.isfile(tmp):
            (tmp_123, fileName) = os.path.split(tmp)
            (name_file, suffix) = os.path.splitext(fileName)
            listtmp = ['.gif']
            if not suffix in listtmp:
                # messagebox.showwarning("输入不正确")
                add_if = False
            else:
                add_if = True
        else:
            # messagebox.showwarning("输入不正确")
            add_if = False


    add_windows = tk.Toplevel()
    add_windows.title('添加作业')
    add_windows.resizable(False, False)
    w2 = tk.Message(add_windows, text='名称')
    w2.pack()
    e = tk.Entry(add_windows)
    e.pack()
    w1 = tk.Message(add_windows, text='输入题目')
    w1.pack()
    Dy_String = tk.StringVar()
    t8 = tk.Text(add_windows,width=50,height=20)
    t8.pack()
    w1 = tk.Message(add_windows, text='输入答案')
    w1.pack()
    t = tk.Text(add_windows,width=50,height=20)
    t.pack()
    b = tk.Button(add_windows, text="确定", command=en)
    b.pack()

    # ex.weitefile(route=route_root, )


class GUI:
    def __init__(self) -> None:
        main = tk.Menu(windows_root)
        main.add_command(label='添加', command=add)
        main.add_command(label='打开', command=open_1)
        windows_root.config(menu=main)
    def windows(self):
        
        windows_root.mainloop()
        
        
