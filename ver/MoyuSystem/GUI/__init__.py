from PySide6 import QtCore, QtGui, QtWidgets

from GUI import GUI_side as ui


class gui:
    def __init__(self, object) -> None:
        self.app = QtWidgets.QApplication([])
        self.window = ui.mainwindow(object=object)
        

    def runGui(self):
        self.window.show()
        self.exec = self.app.exec()
