from Network_communication.GUI.login import conn, login, main, re1, re2
from PySide6 import QtCore, QtGui, QtWidgets
import win32api, win32con

class window_con(QtWidgets.QMainWindow):
    def __init__(self, main, parent=None) -> None:
        super(window_con, self).__init__(parent)
        self.ui = conn.Ui_MainWindow()
        self.ui.setupUi(self)
        self.main = main

    @QtCore.Slot()
    def connect(self, tmp):
        ip = self.ui.lineEdit.text()
        dk = self.ui.spinBox.value()
        if self.ob.con((ip, dk)):
            self.main.change('log')
        else:
            win32api.MessageBox(0, "警告，无法连接到对应服务器", "警告",win32con.MB_ICONWARNING)

class window_log(QtWidgets.QMainWindow):
    def __init__(self, main, parent=None) -> None:
        super(window_log, self).__init__(parent)
        self.ui = login.Ui_MainWindow()
        self.ui.setupUi(self)
        self.main = main

    @QtCore.Slot()
    def login(self, tmp):
        pass

    @QtCore.Slot()
    def register(self, tmp):
        pass


class window_re1(QtWidgets.QMainWindow):
    def __init__(self, main, parent=None) -> None:
        super(window_re1, self).__init__(parent)
        self.ui = re1.Ui_MainWindow()
        self.ui.setupUi(self)
        self.main = main

    @QtCore.Slot()
    def register(self, tmp):
        pass

class window_re2(QtWidgets.QMainWindow):
    def __init__(self, main, parent=None) -> None:
        super(window_re2, self).__init__(parent)
        self.ui = re2.Ui_MainWindow()
        self.ui.setupUi(self)
        self.main = main

    @QtCore.Slot()
    def register(self, tmp):
        pass
# --------------------
class main_Window(QtWidgets.QMainWindow):
    ui_window_child = {}
    def __init__(self, parent=None) -> None:
        super(main_Window, self).__init__(parent)
        self.ui = main.Ui_login()
        self.ui.setupUi(self)

        self.qsl = QtWidgets.QStackedLayout(self.ui.test)
        self.object_con = window_con(main = self)
        self.object_log = window_log(main = self)
        self.object_re1 = window_re1(main = self)
        self.object_re2 = window_re2(main = self)

        self.ui_window_child['con'] = self.qsl.addWidget(self.object_con)
        self.ui_window_child['log'] = self.qsl.addWidget(self.object_log)
        self.ui_window_child['re1'] = self.qsl.addWidget(self.object_re1)
        self.ui_window_child['re2'] = self.qsl.addWidget(self.object_re2)
        self.qsl.setCurrentIndex(self.ui_window_child['con'])

    def get_thread(self, object):
        self.comThread = object
        self.object_con.ob = object
        self.object_log.ob = object
        self.object_re1.ob = object
        self.object_re2.ob = object

    def change(self, win: str):
        self.qsl.setCurrentIndex(self.ui_window_child[win])


def startGui() -> None:
    # app = QtWidgets.QApplication([])
    pass
    # return app.exec()

# if __name__ == '__main__':
#     # 测试使用
#     startGui()
