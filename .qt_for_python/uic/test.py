# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(509, 224)
        MainWindow.setMinimumSize(QSize(509, 224))
        MainWindow.setMaximumSize(QSize(9999, 99999))
        self.photo = QAction(MainWindow)
        self.photo.setObjectName(u"photo")
        self.ooo = QAction(MainWindow)
        self.ooo.setObjectName(u"ooo")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label)


        self.verticalLayout_2.addLayout(self.formLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 509, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.photo)
        self.menu.addAction(self.ooo)

        self.retranslateUi(MainWindow)
        self.photo.triggered.connect(MainWindow.qrcode)
        self.ooo.triggered.connect(MainWindow.AnalysisManagement)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MoyuSystem", None))
        self.photo.setText(QCoreApplication.translate("MainWindow", u"&\u751f\u6210\u4e8c\u7ef4\u7801", None))
        self.ooo.setText(QCoreApplication.translate("MainWindow", u"&\u672c\u5730\u89e3\u6790\u7ba1\u7406\u5668", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u6b22\u8fce\u4f7f\u7528MoyuSystem", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"&\u529f\u80fd", None))
    # retranslateUi

