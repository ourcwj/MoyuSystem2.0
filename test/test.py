import sys

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect, QSize, Qt,
                            QTime, QUrl)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QGradient, QIcon, QImage,
                           QKeySequence, QLinearGradient, QPainter, QPalette,
                           QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
                               QMenuBar, QPushButton, QScrollArea, QSizePolicy,
                               QStatusBar, QVBoxLayout, QWidget)

import test01 as test


class window002(QtWidgets.QMainWindow):
    tmp = {}
    nbm = 0

    def __init__(self, parent=None) -> None:
            super(window002, self).__init__(parent)
            self.ui = test.Ui_MainWindow()
            self.ui.setupUi(self)

    @QtCore.Slot()
    def test(self, tmp):
        print('111')
        self.ui.test()


def main():
    app = QtWidgets.QApplication([])
    window = window002()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
