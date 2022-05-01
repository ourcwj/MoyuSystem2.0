# -- UTF-8 --
# date: 2022年4月30日
# made by: ourcwj

import logging
import sys

import win32api
import win32con
from PySide6 import QtCore, QtGui, QtWidgets

from MS_BIOS import execute as ex
from MS_BIOS.side_ui_file import main_window, new, pic

# from asyncio import windows_events


logger = logging.getLogger('MS_logging')

class mainwindow(QtWidgets.QMainWindow):
    def __init__(self, object, parent=None) -> None:
        self.object = object
        super(mainwindow, self).__init__(parent)
        ui = main_window.Ui_MainWindow()
        ui.setupUi(self)

    @QtCore.Slot()
    def test001(self, temp00000001):
        self.new = test()
        self.new.show()

    @QtCore.Slot()
    def qrcode(self, temp011111111111111 = None):
        self.pic = qrwindow(self.object)
        self.pic.show()


class qrwindow(QtWidgets.QMainWindow):
    def __init__(self, object, parent = None) -> None:
        self.object = object
        super(qrwindow, self).__init__(parent)
        self.ui = pic.Ui_MainWindow()
        self.ui.setupUi(self)

    @QtCore.Slot()
    def start_photo(self, temp):
        # print('111')
        # print(temp)
        tmp = self.ui.get()
        print(tmp)
        if not ex.qrcode(di=tmp, object=self.object):
            # win32api.MessageBox(0, "生成错误。请检查您的参数。\n或您的设备不支持", "警告",win32con.MB_ICONWARNING)
            win32api.MessageBox(0, "生成错误。请检查您的参数。\n或您的设备不支持", "重试",win32con.MB_RETRYCANCEL)
        else:
            win32api.MessageBox(0, "生成完成\n请前往您指定的目录查看", "完成",win32con.MB_OK)
class test(QtWidgets.QMainWindow):
    def __init__(self, parent = None) -> None:
        super(test, self).__init__(parent)
        ui = new.Ui_MainWindow()
        ui.setupUi(self)

class gui:
    def __init__(self, object) -> None:
        self.app = QtWidgets.QApplication([])
        self.window = mainwindow(object=object)
        

    def startGui(self):
        self.window.show()
        self.exec = self.app.exec()