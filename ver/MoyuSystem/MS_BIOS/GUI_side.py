from asyncio import windows_events
import sys
from MS_BIOS import execute
from PySide6 import QtCore, QtWidgets, QtGui

from MS_BIOS.side_ui_file import main_window
from MS_BIOS.side_ui_file import new
from MS_BIOS.side_ui_file import pic

class mainwindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None) -> None:
        super(mainwindow, self).__init__(parent)
        ui = main_window.Ui_MainWindow()
        ui.setupUi(self)

    @QtCore.Slot()
    def test001(self, temp00000001):
        self.new = test()
        self.new.show()

    @QtCore.Slot()
    def qrcode(self, temp011111111111111 = None):
        self.pic = qrwindow()
        self.pic.show()


class qrwindow(QtWidgets.QMainWindow):
    def __init__(self, parent = None) -> None:
        super(qrwindow, self).__init__(parent)
        ui = pic.Ui_MainWindow()
        ui.setupUi(self)

    @QtCore.Slot()
    def start_photo(temp):
        print('111')
        print(temp)

class test(QtWidgets.QMainWindow):
    def __init__(self, parent = None) -> None:
        super(test, self).__init__(parent)
        ui = new.Ui_MainWindow()
        ui.setupUi(self)

class gui:
    def __init__(self) -> None:
        app = QtWidgets.QApplication([])
        window = mainwindow()
        window.show()
    
        self.exec = app.exec()
