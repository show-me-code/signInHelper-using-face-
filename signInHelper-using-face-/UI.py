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
        self.label_3 = QtWidgets.QLabel(MainWindow)
        self.label_3.setAutoFillBackground(True)
        self.label_3.setGeometry(QtCore.QRect(0,0,1261,926))
        self.gif = QtGui.QMovie('./uiResource/background_4.gif')
        self.label_3.setMovie(self.gif)
        self.gif.start()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setStyleSheet("QPushButton{background-color:rgb(254,67,101)}"
                                      "QPushButton{border:0px}"
                                      "QPushButton{color:white}")
        self.pushButton.setGeometry(QtCore.QRect(100, 120, 151, 141))
        self.pushButton.setObjectName("pushButton")
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setStyleSheet("QPushButton{background-color:rgb(252,157,154)}"
                                      "QPushButton{border:0px}"
                                      "QPushButton{color:white}")
        self.pushButton_2.setGeometry(QtCore.QRect(290, 120, 141, 141))
        self.pushButton_2.setObjectName("pushButton_2")
        self.btn_startSignIn = QtWidgets.QPushButton(self.centralwidget)
        self.btn_startSignIn.setStyleSheet("QPushButton{background-color:rgb(200,200,169)}"
                                      "QPushButton{border:0px}"
                                      "QPushButton{color:white}")
        self.btn_startSignIn.setGeometry(QtCore.QRect(480, 120, 141, 141))
        self.btn_startSignIn.setObjectName("btn_startSignIn")
        self.btn_signIn = QtWidgets.QPushButton(self.centralwidget)
        self.btn_signIn.setStyleSheet("QPushButton{background-color:rgb(255,245,247)}"
                                      "QPushButton{border:0px}"
                                      "QPushButton{color:black}")
        self.btn_signIn.setGeometry(QtCore.QRect(670, 120, 151, 141))
        self.btn_signIn.setObjectName("btn_signIn")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setStyleSheet("QPushButton{background-color:rgb(249,205,173)}"
                                      "QPushButton{border:0px}"
                                      "QPushButton{color:white}")
        self.pushButton_4.setGeometry(QtCore.QRect(100, 300, 150, 141))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setStyleSheet("QPushButton{background-color:rgb(131,175,155)}"
                                      "QPushButton{border:0px}"
                                      "QPushButton{color:white}")
        self.pushButton_5.setGeometry(QtCore.QRect(260, 300, 271, 141))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setStyleSheet("QPushButton{background-color:rgb(182,194,154)}"
                                      "QPushButton{border:0px}"
                                      "QPushButton{color:white}")
        self.pushButton_6.setGeometry(QtCore.QRect(550, 300, 271, 141))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setStyleSheet("QPushButton{background-color:rgb(138,151,123)}"
                                      "QPushButton{border:0px}"
                                      "QPushButton{color:white}")
        self.pushButton_7.setGeometry(QtCore.QRect(100, 480, 150, 141))
        self.pushButton_7.setObjectName("pushButton_7")
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
        self.btn_startSignIn.clicked.connect(MainWindow.startSignIn)
        self.btn_signIn.clicked.connect(MainWindow.signIn)
        self.pushButton_4.clicked.connect(MainWindow.showArriveDiagram)
        self.pushButton_5.clicked.connect(MainWindow.analyzeLowRateStu)
        self.pushButton_6.clicked.connect(MainWindow.analyzeHighRateStu)
        self.pushButton_7.clicked.connect(MainWindow.giveAdvice)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "添加面孔"))
        self.pushButton_2.setText(_translate("MainWindow", "删除面孔"))
        self.btn_startSignIn.setText(_translate("MainWindow", "发起签到"))
        self.btn_signIn.setText(_translate("MainWindow", "签到"))
        self.pushButton_4.setText(_translate("MainWindow", "显示到位图"))
        self.pushButton_5.setText(_translate("MainWindow", "分析低到位率学生"))
        self.pushButton_6.setText(_translate("MainWindow", "分析高到位率学生"))
        self.pushButton_7.setText(_translate("MainWindow", "给出到位建议"))

import app_rc
