# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1261, 926)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 120, 151, 141))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 120, 141, 141))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(410, 120, 151, 141))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(250, 290, 801, 531))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_startSignIn = QtWidgets.QPushButton(self.centralwidget)
        self.btn_startSignIn.setGeometry(QtCore.QRect(570, 120, 141, 141))
        self.btn_startSignIn.setObjectName("btn_startSignIn")
        self.btn_signIn = QtWidgets.QPushButton(self.centralwidget)
        self.btn_signIn.setGeometry(QtCore.QRect(720, 120, 151, 141))
        self.btn_signIn.setObjectName("btn_signIn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1261, 37))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.addNewFace)
        self.pushButton_2.clicked.connect(MainWindow.deleteFace)
        self.pushButton_3.clicked.connect(MainWindow.searchFace)
        self.btn_startSignIn.clicked.connect(MainWindow.startSignIn)
        self.btn_signIn.clicked.connect(MainWindow.signIn)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "添加面孔"))
        self.pushButton_2.setText(_translate("MainWindow", "删除面孔"))
        self.pushButton_3.setText(_translate("MainWindow", "执行搜索"))
        self.btn_startSignIn.setText(_translate("MainWindow", "发起签到"))
        self.btn_signIn.setText(_translate("MainWindow", "签到"))

import app_rc
