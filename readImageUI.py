# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'readImageUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class read_image_Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1000, 716)
        self.opencamera = QtWidgets.QPushButton(Form)
        self.opencamera.setGeometry(QtCore.QRect(40, 200, 150, 46))
        self.opencamera.setObjectName("opencamera")
        self.cancel = QtWidgets.QPushButton(Form)
        self.cancel.setGeometry(QtCore.QRect(40, 370, 150, 46))
        self.cancel.setObjectName("cancel")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(250, 60, 800, 600))
        self.label.setObjectName("label")

        self.opencamera.clicked.connect(self.on_click_open)
        self.cancel.clicked.connect(self.close_window)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.opencamera.setText(_translate("Form", "打开相机"))
        self.cancel.setText(_translate("Form", "关闭"))
        self.label.setText(_translate("Form", ""))

