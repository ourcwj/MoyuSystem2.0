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
        MainWindow.resize(556, 246)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(9999, 99999))
        self.action_test = QAction(MainWindow)
        self.action_test.setObjectName(u"action_test")
        self.newWindow = QAction(MainWindow)
        self.newWindow.setObjectName(u"newWindow")
        self.photo = QAction(MainWindow)
        self.photo.setObjectName(u"photo")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(95)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.label_2)


        self.verticalLayout_2.addLayout(self.formLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 556, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.action_test)
        self.menu.addAction(self.newWindow)
        self.menu.addAction(self.photo)

        self.retranslateUi(MainWindow)
        self.newWindow.triggered.connect(MainWindow.test001)
        self.photo.triggered.connect(MainWindow.qrcode)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MoyuSystem", None))
        self.action_test.setText(QCoreApplication.translate("MainWindow", u"&\u6d4b\u8bd5", None))
        self.newWindow.setText(QCoreApplication.translate("MainWindow", u"&\u65b0\u5efa\u5b50\u7a97\u53e3", None))
        self.photo.setText(QCoreApplication.translate("MainWindow", u"&\u751f\u6210\u4e8c\u7ef4\u7801", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u6b22\u8fce\u4f7f\u7528", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u662f\u4e0d\u662f\u5199\u7684\u5f88\u5783\u573e\uff08\u7a97\u53e3\u5927\u5c0f\u968f\u4fbf\u8c03\u6574\uff0c\u4f1a\u81ea\u52a8\u9002\u5e94.\u57fa\u4e8ePySide\u3002MD\u83dc\u5355\u7ed1\u5b9a\u69fd\u51fd\u6570\u5199\u4e86\u6211\u534a\u5929\uff09", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"&\u6d4b\u8bd5", None))
    # retranslateUi

