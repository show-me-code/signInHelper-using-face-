# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'arrivePercentShow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class arrive_show(QtWidgets.QWidget, object):
    def __init__(self):
        super(arrive_show,self).__init__()
        self.setupUi(self)
    
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1026, 824)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setAutoFillBackground(True)
        self.label_3.setGeometry(QtCore.QRect(0,0,1026,824))
        self.gif = QtGui.QMovie('./uiResource/background_8.gif')
        self.label_3.setMovie(self.gif)
        self.gif.start()
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(80, 80, 300, 24))
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(80, 130, 701, 251))
        self.textBrowser.setObjectName("textBrowser")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(80, 410, 300, 24))
        self.label_2.setObjectName("label_2")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_2.setGeometry(QtCore.QRect(80, 460, 701, 221))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "超过阈值的学生"))
        self.label.setText(_translate("Form", "TextLabel"))
        self.label_2.setText(_translate("Form", "TextLabel"))

    def closeEvent(self, a0: QtGui.QCloseEvent):
        self.textBrowser.setText("")
        self.textBrowser_2.setText("")

    def change_ui_low(self, dict_percent_low):
        self.label.setText("到位率低的学生为：")
        self.label_2.setText("对应排名百分比分别为：")
        for k in dict_percent_low:
            self.textBrowser.append(k + '\n')
        for k in dict_percent_low:
            self.textBrowser_2.append(str(dict_percent_low[k]) + '\n')
        
    def change_ui_high(self, dict_percent_high):
        self.label.setText("到位率高的学生为：")
        self.label_2.setText('对应排名百分比分别为：')
        for k in dict_percent_high:
            self.textBrowser.append(k + '\n')
        for k in dict_percent_high:
            self.textBrowser_2.append(str(dict_percent_high[k]) + '\n')
    
if(__name__ == "__main__"):
    app = QtWidgets.QApplication(sys.argv)
    show_dialog = arrive_show()
    show_dialog.show()
    sys.exit(app.exec_())
