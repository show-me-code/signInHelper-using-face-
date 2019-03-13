# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from logIn import logIn_MainWindow
import os
from mainWindow import My_UI
import base64
import after_regist

user_name = ""
password = ""
file_name = "user_info.txt"


class logIn_manager(QtWidgets.QMainWindow, logIn_MainWindow):
    def __init__(self):
        super(logIn_manager,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("请输入用户名和密码")


    def confirm_password(self):
        global user_name
        global password
        #若注册文件大小为0则提示注册，使用base64加密密码
        if(os.path.getsize(file_name) == 0):
            self.setWindowTitle("请注册")
            user_name = self.lineEdit.text()
            password = self.lineEdit_2.text()
            password_ = base64.b64encode(password.encode("utf-8"))
            with open(file_name, "w") as file:
                file.write(user_name+'\n')
                file.write(str(password_))
            print(user_name)
            print(password_)
            #提示密码已经成功保存
            after_regist_log.show()
        else:
            #读取文件，第一行为用户名，第二行为密码
            with open(file_name, "r") as file:
                line = file.readlines()
                user_name = line[0]
                password = line[1]
            #因为有换行，所以需要加上\n
            if((self.lineEdit.text() + '\n') == user_name):
                if(str(base64.b64encode(self.lineEdit_2.text().encode("utf-8"))) == password):
                    print("登录成功")
                    #在此处进行主要窗口的显示
                    main_window.show()
                    #登录成功后关闭此窗口
                    logIn_window.close()
                else:
                    print("登录失败,密码")
            else:
                print("登陆失败，用户名")



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    logIn_window = logIn_manager()
    #实例化主要窗口
    main_window = My_UI()
    after_regist_log = after_regist.after_regist_Ui_Dialog()
    logIn_window.show()
    sys.exit(app.exec_())