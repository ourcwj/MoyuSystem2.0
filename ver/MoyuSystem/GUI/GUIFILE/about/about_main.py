# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '关于的主窗口.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QMainWindow,
    QMenu, QMenuBar, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(741, 461)
        self.action_aboutRJ = QAction(MainWindow)
        self.action_aboutRJ.setObjectName(u"action_aboutRJ")
        self.action_Author_s_words = QAction(MainWindow)
        self.action_Author_s_words.setObjectName(u"action_Author_s_words")
        self.action_Open_with_default_browser = QAction(MainWindow)
        self.action_Open_with_default_browser.setObjectName(u"action_Open_with_default_browser")
        self.action_Open_using_the_software_s_built_in_browser = QAction(MainWindow)
        self.action_Open_using_the_software_s_built_in_browser.setObjectName(u"action_Open_using_the_software_s_built_in_browser")
        self.action_aboutZZ = QAction(MainWindow)
        self.action_aboutZZ.setObjectName(u"action_aboutZZ")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 741, 22))
        self.menu_about = QMenu(self.menubar)
        self.menu_about.setObjectName(u"menu_about")
        self.menu = QMenu(self.menu_about)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_about.menuAction())
        self.menu_about.addAction(self.action_aboutRJ)
        self.menu_about.addAction(self.action_Author_s_words)
        self.menu_about.addAction(self.action_aboutZZ)
        self.menu_about.addSeparator()
        self.menu_about.addAction(self.menu.menuAction())
        self.menu.addAction(self.action_Open_with_default_browser)
        self.menu.addAction(self.action_Open_using_the_software_s_built_in_browser)

        self.retranslateUi(MainWindow)
        self.action_aboutRJ.triggered.connect(MainWindow.adout)
        self.action_Author_s_words.triggered.connect(MainWindow.zzdh)
        self.action_aboutZZ.triggered.connect(MainWindow.adoutzz)
        self.action_Open_with_default_browser.triggered.connect(MainWindow.bdweb)
        self.action_Open_using_the_software_s_built_in_browser.triggered.connect(MainWindow.web)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.action_aboutRJ.setText(QCoreApplication.translate("MainWindow", u"&\u5173\u4e8e\u672c\u8f6f\u4ef6", None))
        self.action_Author_s_words.setText(QCoreApplication.translate("MainWindow", u"&\u4f5c\u8005\u7684\u8bdd", None))
        self.action_Open_with_default_browser.setText(QCoreApplication.translate("MainWindow", u"&\u4f7f\u7528\u9ed8\u8ba4\u6d4f\u89c8\u5668\u6253\u5f00", None))
        self.action_Open_using_the_software_s_built_in_browser.setText(QCoreApplication.translate("MainWindow", u"&\u4f7f\u7528\u8f6f\u4ef6\u5185\u7f6e\u6d4f\u89c8\u5668\u6253\u5f00", None))
        self.action_aboutZZ.setText(QCoreApplication.translate("MainWindow", u"&\u5173\u4e8e\u4f5c\u8005", None))
        self.menu_about.setTitle(QCoreApplication.translate("MainWindow", u"&\u66f4\u591a\u5173\u4e8e", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"&\u8f6f\u4ef6\u5f00\u6e90\u5730\u5740", None))
    # retranslateUi

