# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pic.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QCommandLinkButton, QGridLayout,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QRadioButton, QSizePolicy, QSpinBox, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(607, 363)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setEnabled(False)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_4, 4, 0, 1, 1)

        self.spinBox = QSpinBox(self.centralwidget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setEnabled(False)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(40)

        self.gridLayout_2.addWidget(self.spinBox, 4, 1, 1, 2)

        self.checkBox_2 = QCheckBox(self.centralwidget)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.gridLayout_2.addWidget(self.checkBox_2, 4, 3, 1, 1)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setEnabled(True)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_5, 3, 0, 1, 1)

        self.radioButton = QRadioButton(self.centralwidget)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setEnabled(False)

        self.gridLayout_2.addWidget(self.radioButton, 6, 3, 1, 1)

        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout_2.addWidget(self.checkBox, 5, 0, 1, 1)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_2.addWidget(self.lineEdit, 1, 2, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setEnabled(False)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_3, 6, 0, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Microsoft JhengHei UI"])
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 4)

        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setEnabled(True)

        self.gridLayout_2.addWidget(self.lineEdit_3, 3, 2, 1, 1)

        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setEnabled(False)

        self.gridLayout_2.addWidget(self.lineEdit_2, 6, 1, 1, 2)

        self.commandLinkButton = QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setMaximumSize(QSize(16777, 50))

        self.gridLayout_2.addWidget(self.commandLinkButton, 7, 0, 1, 4)


        self.gridLayout.addLayout(self.gridLayout_2, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 607, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.checkBox_2.clicked["bool"].connect(self.spinBox.setEnabled)
        self.checkBox_2.clicked["bool"].connect(self.label_4.setEnabled)
        self.checkBox.clicked["bool"].connect(self.label_3.setEnabled)
        self.checkBox.clicked["bool"].connect(self.lineEdit_2.setEnabled)
        self.checkBox.clicked["bool"].connect(self.radioButton.setEnabled)
        self.checkBox.clicked["bool"].connect(self.radioButton.setChecked)
        self.commandLinkButton.clicked.connect(MainWindow.start_photo)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u751f\u6210\u4e8c\u7ef4\u7801", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u4e8c\u7ef4\u7801\u5185\u5bb9", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u4e8c\u7ef4\u7801\u957f\u5ea6", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"\u662f\u5426\u542f\u7528", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u51fa\u8def\u5f84", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"\u542f\u7528\u5f69\u8272", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\u5e26\u6709\u56fe\u7247\u7684\u4e8c\u7ef4\u7801", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"http://www.baidu.com/", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u7247\u8def\u5f84", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u751f\u6210\u4e8c\u7ef4\u7801", None))
        self.lineEdit_3.setText(QCoreApplication.translate("MainWindow", u"C:\\", None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"C:\\", None))
        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"\u751f\u6210\u4e8c\u7ef4\u7801", None))
    # retranslateUi

