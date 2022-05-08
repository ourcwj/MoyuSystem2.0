from PySide6 import QtCore, QtGui, QtWidgets
import webbrowser
import sys
from GUI.GUIFILE.about import ZZworlds, about_main, about_RJ, about_ZZ, web


class about_mainwindow(QtWidgets.QMainWindow):
    # 主窗口
    def __init__(self, parent=None) -> None:
        super(about_mainwindow, self).__init__(parent)
        self.ui = about_main.Ui_MainWindow()
        self.ui.setupUi(self)

        ab = RJ()
        dh = wr()
        wy = WE()
        Zz = ZZ()

        self.qsl = QtWidgets.QStackedLayout(self.ui.frame)

        self.qsl.addWidget(ab)
        self.qsl.addWidget(dh)
        self.qsl.addWidget(wy)
        self.qsl.addWidget(Zz)


    @QtCore.Slot()
    def adout(self, temp011111111111111):
        self.qsl.setCurrentIndex(0)

    @QtCore.Slot()
    def zzdh(self, temp011111111111111):
        self.qsl.setCurrentIndex(1)

    @QtCore.Slot()
    def web(self, temp011111111111111):
        self.qsl.setCurrentIndex(2)

    @QtCore.Slot()
    def bdweb(self, temp011111111111111):
        webbrowser.open('https://github.com/ourcwj/MoyuSystem2.0')

    @QtCore.Slot()
    def adoutzz(self, temp011111111111111):
        self.qsl.setCurrentIndex(3)

class RJ(QtWidgets.QMainWindow):
    def __init__(self, parent=None) -> None:
        super(RJ, self).__init__(parent)
        self.ui = about_RJ.Ui_MainWindow()
        self.ui.setupUi(self)


class ZZ(QtWidgets.QMainWindow):
    def __init__(self, parent=None) -> None:
        super(ZZ, self).__init__(parent)
        self.ui = about_ZZ.Ui_MainWindow()
        self.ui.setupUi(self)

class WE(QtWidgets.QMainWindow):
    def __init__(self, parent=None) -> None:
        super(WE, self).__init__(parent)
        self.ui = web.Ui_MainWindow()
        self.ui.setupUi(self)

class wr(QtWidgets.QMainWindow):
    def __init__(self, parent=None) -> None:
        super(wr, self).__init__(parent)
        self.ui = ZZworlds.Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == '__main__':
    class gui:
        def __init__(self, object) -> None:
            self.app = QtWidgets.QApplication([])
            self.window = about_mainwindow()


        def runGui(self):
            self.window.show()
            # self.exec = self.app.exec()
            sys.exit(self.app.exec())

    Gui = gui()
    Gui.runGui()