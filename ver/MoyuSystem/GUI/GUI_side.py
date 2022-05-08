# -- UTF-8 --
# date: 2022年4月30日
# made by: ourcwj

import logging
import sys

import win32api
import win32con
from MS_BIOS import execute as ex
from MS_BIOS.side_ui_file import AnalysisManagement, main_window, new, pic
from MS_BIOS.side_ui_file.help_an import help, help_main, url
from PySide6 import QtCore, QtGui, QtWidgets

from GUI import adout

# from asyncio import windows_events

logger = logging.getLogger('MS_logging')

class mainwindow(QtWidgets.QMainWindow):
    # 主窗口
    def __init__(self, object, parent=None) -> None:
        self.object = object
        super(mainwindow, self).__init__(parent)
        ui = main_window.Ui_MainWindow()
        ui.setupUi(self)

    @QtCore.Slot()
    def AnalysisManagement(self, temp00000001):
        # 本地解析管理器
        self.wwwwwwww = qwe()
        self.wwwwwwww.show()

    @QtCore.Slot()
    def qrcode(self, temp011111111111111 = None):
        # 生成二维码
        self.pic = qrwindow(self.object)
        self.pic.show()

    @QtCore.Slot()
    def about(self, temp011111111111111):
        self.adout = adout.about_mainwindow()
        self.adout.show()


class qrwindow(QtWidgets.QMainWindow):
    # 生成二维码的窗口
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

class qwe(QtWidgets.QMainWindow):
    # 生成本地资源管理器的窗口
    def __init__(self, parent = None) -> None:
        super(qwe, self).__init__(parent)
        self.ui = AnalysisManagement.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('本地解析管理')
        self.ho = ex.host()
        self.sx()

    def cx(self):
        tmp = self.ui.list.currentItem().text()
        tmp_2 = self.ho.hos[tmp]
        self.ui.q11.setText(tmp_2)

    def sc(self):
        self.ho.del_r(self.ui.list.currentItem().text())
        self.sx()

    def sx(self):
        self.ho.read()
        self.ui.list.clear()
        self.ui.list.addItems(self.ho.hos_list)

    def xg_123(self):
        tmp = self.ui.text_1.text()
        tmp_2 = self.ui.list.currentItem().text()
        self.ho.hos[tmp_2] = tmp
        self.ho.wi()
        self.sx()

    def tj(self):
        tmp = self.ui.text_2.text()
        tmp_2 = self.ui.text_3.text()
        self.ho.hos_list.append(tmp)
        self.ho.hos[tmp] = tmp_2
        self.ho.wi()
        self.sx()
    # --------------------
    @QtCore.Slot()
    def query(self, temp011111111111111):
        self.cx()

    @QtCore.Slot()
    def refresh(self, temp011111111111111):
        self.sx()

    @QtCore.Slot()
    def add(self, temp011111111111111):
        self.tj()

    @QtCore.Slot()
    def xg(self, temp011111111111111):
        self.xg_123()

    @QtCore.Slot()
    def help(self, temp011111111111111):
        self.window = help_an_qwe()
        self.window.show()
    
    @QtCore.Slot()
    def del_w(self, temp011111111111111):
        self.sc()
    # --------------------


# --------------------

class help_qwe(QtWidgets.QMainWindow):
    def __init__(self, parent = None) -> None:
        super(help_qwe, self).__init__(parent)
        self.ui = help.Ui_MainWindow()
        self.ui.setupUi(self)

class help_url_qwe(QtWidgets.QMainWindow):
    def __init__(self, parent = None) -> None:
        super(help_url_qwe, self).__init__(parent)
        self.ui = url.Ui_MainWindow()
        self.ui.setupUi(self)

class help_an_qwe(QtWidgets.QMainWindow):
    def __init__(self, parent = None) -> None:
        super(help_an_qwe, self).__init__(parent)
        self.ui = help_main.Ui_MainWindow()
        self.ui.setupUi(self)
        self.qsl = QtWidgets.QStackedLayout(self.ui.frame)
        help_text = help_qwe()
        help_url = help_url_qwe()
        self.qsl.addWidget(help_text)
        self.qsl.addWidget(help_url)



    # --------------------
    @QtCore.Slot()
    def help_123(self, temp011111111111111):
        # print('help')
        self.qsl.setCurrentIndex(0)

    @QtCore.Slot()
    def ip(self, temp011111111111111):
        # print('url')
        self.qsl.setCurrentIndex(1)
    # --------------------


# --------------------

