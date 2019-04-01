# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adviceUi.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class advice_ui(QtWidgets.QWidget, object):

    def __init__(self):
        super(advice_ui, self).__init__()
        self.setupUi(self)
    def setupUi(self, Form):
        Form.setObjectName("建议")
        Form.resize(842, 674)
        
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setAutoFillBackground(True)
        self.label_3.setGeometry(QtCore.QRect(0,0,842,674))
        self.gif = QtGui.QMovie('./uiResource/background_6.gif')
        self.label_3.setMovie(self.gif)
        self.gif.start()
        
        self.label = QtWidgets.QLabel(Form)
        self.label.setStyleSheet("QLabel{color:white}")
        self.label.setGeometry(QtCore.QRect(70, 50, 221, 31))
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setStyleSheet("QTextBrowser{background-color:rgb(131,175,155)}")
        self.textBrowser.setGeometry(QtCore.QRect(70, 110, 691, 511))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "建议"))
        self.label.setText(_translate("Form", "这里是我们的建议："))
    
    def closeEvent(self, a0: QtGui.QCloseEvent):
        self.textBrowser.setText("")
