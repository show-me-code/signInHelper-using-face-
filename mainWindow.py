import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from UI import Ui_MainWindow
from collections import defaultdict
from loading import loading_Ui_Dialog
from UI import Ui_MainWindow
from PyQt5.QtCore import QTimer
import time
# 导入系统库并定义辅助函数
from pprint import pformat
import app_rc
import cv2

from PythonSDK.facepp import API,File
# 导入图片处理类
import PythonSDK.ImagePro


# 以下四项是dmeo中用到的图片资源，可根据需要替换
faceSet_img = ''                        #"./imgResource/img.jpg"       # 用于创建faceSet
face_search_img = './imgResource/singleface.jpg'  # 用于人脸搜索
face_search_img2 = './imgResource/singleface2.png'

arrive_data = defaultdict(list)

# 此方法专用来打印api返回的信息
def print_result(hit, result):
    print(hit)
    print('\n'.join("  " + i for i in pformat(result, width=75).split('\n')))

def printFuctionTitle(title):
    return "\n"+"-"*60+title+"-"*60;

# 初始化对象，进行api的调用工作
api = API()

class My_UI(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(My_UI, self).__init__()
        self.setupUi(self)
        self.child = loading_Ui_Dialog()
        self.btn_signIn.setEnabled(False)
        self.timer = QTimer()
        self.timer.timeout.connect(self.enable_btn)


    def addNewFace(self):
        global faceSet_img
        faceSet_img = QtWidgets.QFileDialog.getOpenFileName(self, 'open the dialog',
                                                                   "C:\\Users\Administrator\Desktop",
                                                                   'JEPG files(*.jpg);;PNG files(*.PNG)')

        print(faceSet_img[0])
        faceStr = []; #存储faceatoken
        face_string = ''
        #创建一个faceset
        api.faceset.create(outer_id = 'test2');
        #探测图片中的face
        res = api.detect(image_file=File(faceSet_img[0]));
        print_result("detect resule", res);
        #将返回值中的数据复制给faceList
        faceList = res["faces"];
        #创建一个str数组存储所有face的facetoken
        for i in range(len(faceList)):
            faceStr.append(faceList[i]["face_token"])
        for i in range(0, len(faceList)):
            #在剩下多于5个的情况下，按照最大一次添加5个
            if ((len(faceList) - i) >= 5):
                face_string = ''
                for j in range(i, 5):
                    if (face_string == ''):
                        face_string = face_string + faceList[j]["face_token"]
                    else:
                        face_string = face_string + ',' + faceList[j]['face_token'];
                i = i + 4;
            #剩下数量不足的时候添加剩下的所有
            if ((len(faceList) - i) < 5):
                for j in range(i + 1, len(faceList)):
                    face_string = ''
                    if (face_string == ''):
                        face_string = face_string + faceList[j]["face_token"]
                    else:
                        face_string = face_string + ',' + faceList[j]['face_token'];
                e = True;
                # api.faceset.addface(outer_id='test2', face_tokens=face_string_2)
            api.faceset.addface(outer_id='test2', face_tokens=face_string)
            if (e):
                break;

    def deleteFace(self):
        res = api.faceset.delete(outer_id='test2', check_empty=0)
        print_result('删除',res)

    def searchFace(self):
        #不显示图片是因为多线程的问题，单一线程会导致图片和搜索同时，搜索完了图片还没加载

        global face_search_img
        #此处之后应当改为调用摄像头后采取图片
        face_search_img = QtWidgets.QFileDialog.getOpenFileName(self, '选择要搜索的图片',
                                                                   "C:\\Users\Administrator\Desktop",
                                                                   'JEPG files(*.jpg);;PNG files(*.PNG)')

        #首先显示要搜索的图片
        serach_res = api.search(image_file=File(face_search_img[0]), outer_id='test2');
        #serach_res返回搜索结果，置信度大于90%则设施为已经到位
        print_result("搜索结果", serach_res)
        #serach_list用于将serach_res中的faces部分信息转换为列表
        #输出特定的face_token
        serach_result = serach_res['results']
        #输出对应的置信值
        serach_confidence = serach_result[0]['confidence']
        face_token = serach_result[0]['face_token']
        print(face_token, serach_confidence)
        '''arrive_or_not = 0
        #置信度大于70%则设施为已经到位
        if(serach_confidence >= 80) :
            arrive_or_not = 1
        else:
            arrive_or_not = 0
        global arrive_data
        data_manage.addArriveData(arrive_data, face_token, arrive_or_not)
        data_manage.saveAsCsv(arrive_data)
        print(arrive_data)'''

    def choosePic(self):
        #引用全局变量
        global faceSet_img
        faceSet_img = QtWidgets.QFileDialog.getOpenFileName(self,'open the dialog',"C:\\Users\Administrator\Desktop", 'JEPG files(*.jpg);;PNG files(*.PNG)')

    def startSignIn(self):
        #点击这一按钮后选择要开放多长时间签到，随后将签到按钮开放这么长时间
        num,ok = QtWidgets.QInputDialog.getInt(self, '请选择开放签到多长时间', '输入时间（分钟）')
        if ok:
            self.btn_signIn.setEnabled(True)
            self.btn_startSignIn.setEnabled(False)
            print(num)
        self.timer.start(num*60*1000)
        #QTimer.singleShot(num * 60 * 1000, self.btn_signIn.setEnabled(False))

    def signIn(self):
        pass

    def enable_btn(self):
        self.btn_startSignIn.setEnabled(True)
        self.btn_signIn.setEnabled(False)
        self.timer.stop()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = My_UI()
    main_window.show()
    sys.exit(app.exec_())
