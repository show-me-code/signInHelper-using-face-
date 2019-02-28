# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loading.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class loading_Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("请稍等")
        Form.resize(1151, 647)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.label = QtWidgets.QLabel('', self)
        self.label.setText("")
        self.setFixedSize(800, 650)
        self.pix = QtGui.QPixmap(':/pic/uiResource/loading.gif')
        self.label.setPixmap(self.pix)
        self.label.setScaledContents(True)

        movie = QtGui.QMovie(":/pic/uiResource/loading.gif")
        self.label.setMovie(movie)
        movie.start()
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle("请稍等")


class loading_Ui_Dialog(QtWidgets.QWidget, loading_Ui_Form):
    def __init__(self):
        super(loading_Ui_Dialog, self).__init__()
        self.setupUi(self)
import app_rc

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    loading = loading_Ui_Dialog()
    loading.show()
    sys.exit(app.exec_())