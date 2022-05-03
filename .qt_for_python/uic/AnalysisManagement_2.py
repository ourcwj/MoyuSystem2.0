# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AnalysisManagement_2.ui'
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
from PySide6.QtWidgets import (QApplication, QCommandLinkButton, QGridLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTabWidget, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(761, 434)
        self.action_111 = QAction(MainWindow)
        self.action_111.setObjectName(u"action_111")
        self.action_111.setCheckable(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.add = QWidget()
        self.add.setObjectName(u"add")
        self.gridLayout_4 = QGridLayout(self.add)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tabWidget_2 = QTabWidget(self.add)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.add_1 = QWidget()
        self.add_1.setObjectName(u"add_1")
        self.gridLayout_5 = QGridLayout(self.add_1)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.text_1 = QLineEdit(self.add_1)
        self.text_1.setObjectName(u"text_1")

        self.gridLayout_5.addWidget(self.text_1, 2, 1, 1, 1)

        self.label_6 = QLabel(self.add_1)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777182, 167770))
        self.label_6.setSizeIncrement(QSize(34, 12))

        self.gridLayout_5.addWidget(self.label_6, 0, 1, 1, 1)

        self.label_7 = QLabel(self.add_1)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_5.addWidget(self.label_7, 2, 0, 1, 1)

        self.label_5 = QLabel(self.add_1)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 167770))

        self.gridLayout_5.addWidget(self.label_5, 0, 0, 1, 1)

        self.commandLinkButton = QCommandLinkButton(self.add_1)
        self.commandLinkButton.setObjectName(u"commandLinkButton")

        self.gridLayout_5.addWidget(self.commandLinkButton, 3, 0, 1, 2)

        self.tabWidget_2.addTab(self.add_1, "")
        self.add_3 = QWidget()
        self.add_3.setObjectName(u"add_3")
        self.gridLayout_6 = QGridLayout(self.add_3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.text_2 = QLineEdit(self.add_3)
        self.text_2.setObjectName(u"text_2")

        self.gridLayout_6.addWidget(self.text_2, 0, 2, 1, 1)

        self.label_9 = QLabel(self.add_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(16777215, 167770))

        self.gridLayout_6.addWidget(self.label_9, 0, 0, 1, 2)

        self.text_3 = QLineEdit(self.add_3)
        self.text_3.setObjectName(u"text_3")

        self.gridLayout_6.addWidget(self.text_3, 1, 2, 1, 1)

        self.label_10 = QLabel(self.add_3)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_6.addWidget(self.label_10, 1, 0, 1, 2)

        self.commandLinkButton_2 = QCommandLinkButton(self.add_3)
        self.commandLinkButton_2.setObjectName(u"commandLinkButton_2")

        self.gridLayout_6.addWidget(self.commandLinkButton_2, 2, 0, 1, 3)

        self.tabWidget_2.addTab(self.add_3, "")

        self.gridLayout_3.addWidget(self.tabWidget_2, 0, 0, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)

        self.tabWidget.addTab(self.add, "")
        self.see = QWidget()
        self.see.setObjectName(u"see")
        self.gridLayout = QGridLayout(self.see)
        self.gridLayout.setObjectName(u"gridLayout")
        self.q11 = QLabel(self.see)
        self.q11.setObjectName(u"q11")

        self.gridLayout.addWidget(self.q11, 2, 1, 1, 1)

        self.label_2 = QLabel(self.see)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.label_3 = QLabel(self.see)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.label = QLabel(self.see)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.see)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 3, 1, 2, 1)

        self.tabWidget.addTab(self.see, "")

        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 3, 1)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_4, 0, 1, 1, 1)

        self.list = QListWidget(self.centralwidget)
        self.list.setObjectName(u"list")

        self.gridLayout_2.addWidget(self.list, 1, 1, 1, 1)

        self.commandLinkButton_3 = QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_3.setObjectName(u"commandLinkButton_3")

        self.gridLayout_2.addWidget(self.commandLinkButton_3, 2, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 761, 22))
        self.q111 = QMenu(self.menubar)
        self.q111.setObjectName(u"q111")
        self.q111.setTearOffEnabled(True)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.q111.menuAction())
        self.q111.addAction(self.action_111)

        self.retranslateUi(MainWindow)
        self.list.currentTextChanged.connect(self.label_6.setText)
        self.commandLinkButton_3.clicked.connect(MainWindow.refresh)
        self.commandLinkButton.clicked.connect(MainWindow.xg)
        self.commandLinkButton_2.clicked.connect(MainWindow.add)
        self.list.currentTextChanged.connect(self.label_2.setText)
        self.pushButton.clicked.connect(MainWindow.query)
        self.action_111.triggered.connect(MainWindow.help)

        self.tabWidget.setCurrentIndex(1)
        self.tabWidget_2.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u672c\u5730\u89e3\u6790\u7ba1\u7406\u5668", None))
        self.action_111.setText(QCoreApplication.translate("MainWindow", u"&\u6253\u5f00\u7a97\u53e3", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"#[unknow]\u8bf7\u5728\u53f3\u4fa7\u9009\u62e9", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u5c06\u88ab\u89e3\u6790\u5230\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u7f51\u5740\uff1a", None))
        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539\u5230\u6570\u636e", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.add_1), QCoreApplication.translate("MainWindow", u"\u4fee\u6539", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u7f51\u5740\uff1a", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u5c06\u88ab\u89e3\u6790\u5230\uff1a", None))
        self.commandLinkButton_2.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u5230\u6570\u636e", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.add_3), QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.add), QCoreApplication.translate("MainWindow", u"\u4fee\u6539", None))
        self.q11.setText(QCoreApplication.translate("MainWindow", u"\u7b49\u5f85\u9009\u62e9", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"#[unknow]\u8bf7\u5728\u53f3\u4fa7\u9009\u62e9", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u5c06\u88ab\u89e3\u6790\u5230\uff1a", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u7f51\u5740\uff1a", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u8be2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.see), QCoreApplication.translate("MainWindow", u"\u67e5\u770b", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u5df2\u6dfb\u52a0\u7684\u89e3\u6790", None))
        self.commandLinkButton_3.setText(QCoreApplication.translate("MainWindow", u"\u5237\u65b0\u6570\u636e", None))
        self.q111.setTitle(QCoreApplication.translate("MainWindow", u"&\u5e2e\u52a9", None))
    # retranslateUi

