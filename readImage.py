import sys
import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from readImageUI import read_image_Ui_Form
import time
import os

class read_image(QtWidgets.QWidget, read_image_Ui_Form):
    def __init__(self):
        super(read_image, self).__init__()
        self.timer_camera = QtCore.QTimer()
        self.cap = cv2.VideoCapture()
        #设置为前置摄像头
        self.CAM_NUM = 1
        self.slot_init()
        self.setupUi(self)

        self.faces = []
       

    def slot_init(self):
        #开始定制捕获图片
        self.timer_camera.timeout.connect(self.show_camera)


    def on_click_open(self):
        if(self.timer_camera.isActive() == False):
            flag = self.cap.open(self.CAM_NUM)
            if(flag == False):
                msg = QtWidgets.QMessageBox.warning(self, 'Warning', '请检查摄像头是否连接正确',buttons=QtWidgets.QMessageBox.Ok,
                                                    defaultButton=QtWidgets.QMessageBox.Ok)
            else:
                self.timer_camera.start(3)
                self.opencamera.setText("关闭相机")
        else:
            self.timer_camera.stop()
            self.cap.release()
            self.label.clear()
            self.opencamera.setText('打开相机')

    def show_camera(self):
        #载入cv2的人脸识别标签
        detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        flag, self.image = self.cap.read()
        show = cv2.resize(self.image, (800,600))
        show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
        show_image = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888)
        self.label.setPixmap(QtGui.QPixmap.fromImage(show_image))
        #变为灰度图，将侦测到的人脸信息记录
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, 1.3, 5)
        print(faces + len(faces))

        for (x, y, w, h) in faces:
            cv2.rectangle(self.image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        self.label.setPixmap(QtGui.QPixmap.fromImage(show_image))
        if(len(faces) == 1):
            #如果检测到了一张人脸，则记录当前帧并弹出窗口，停止计时器，关闭签到窗口
            cv2.imwrite(str(time.time())+'.jpg', self.image)
            notice = QtWidgets.QMessageBox.information(self, '成功',"您的签到照片已经成功保存")
            if self.cap.isOpened():
                self.cap.release()
            if self.timer_camera.isActive():
                self.timer_camera.stop()
            ex.close()

    def close_window(self, event):
        ok = QtWidgets.QPushButton()
        cacel = QtWidgets.QPushButton()
        msg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, u"关闭", u"是否关闭！")
        msg.addButton(ok, QtWidgets.QMessageBox.ActionRole)
        msg.addButton(cacel, QtWidgets.QMessageBox.RejectRole)
        ok.setText(u'确定')
        cacel.setText(u'取消')
        if msg.exec_() == QtWidgets.QMessageBox.RejectRole:
            event.ignore()
        else:
            if self.cap.isOpened():
                self.cap.release()
            if self.timer_camera.isActive():
                self.timer_camera.stop()
            event.accept()

if(__name__ == '__main__'):
    App = QtWidgets.QApplication(sys.argv)
    ex = read_image()
    ex.show()
    sys.exit(App.exec_())