import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from UI import Ui_MainWindow
from collections import defaultdict
from loading import loading_Ui_Dialog, Thread_loading
from UI import Ui_MainWindow
from PyQt5.QtCore import QTimer
import time
from dataManagement import data_management
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
        #self.child = loading_Ui_Dialog()
        self.btn_signIn.setEnabled(False)
        self.timer = QTimer()
        self.timer.timeout.connect(self.enable_btn)
        self.data_manager = data_management()
        self.data_manager.load_face_token_to_list()
        self.data_manager.init_data(self.data_manager.face_token_set)
        self.data_manager.init_emotion(self.data_manager.face_token_set)
        self.loading = loading_Ui_Dialog()
        self.pbar = QtWidgets.QProgressBar()
        self.process_bar = QTimer()
        self.step = 0

        self.add_thread = Thread()
        self.add_thread.sinOut.connect(self.add_finished_connect)

    def add_finished_connect(self):
        self.loading.close()
        reply = QtWidgets.QMessageBox.information(self,'请重启', '数据已经载入成功，请重新启动', 
                                            QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.Yes)
        print(reply)
        if(reply == 16384):
            sys.exit(app.exec_)

    def addNewFace(self):
        global faceSet_img
        faceSet_img = QtWidgets.QFileDialog.getOpenFileName(self, 'open the dialog',
                                                                   "C:\\Users\Administrator\Desktop",
                                                                   'JEPG files(*.jpg);;PNG files(*.PNG)')
        self.loading.show()
        faceStr = []; #存储face_token
        face_string = ''
        #创建一个faceset
        api.faceset.create(outer_id = 'test2');
        #探测图片中的face
        res = api.detect(image_file=File(faceSet_img[0]), return_attributes='emotion');
        print_result("detect resule", res);
        #将返回值中的数据复制给faceList
        faceList = res["faces"];
        #创建一个str数组存储所有face的facetoken
        for i in range(len(faceList)):
            faceStr.append(faceList[i]["face_token"])

        self.data_manager.face_token_set = faceStr
        self.data_manager.write_face_token_to_csv(self.data_manager.face_token_set)
        
        self.add_thread.faceList = faceList
        self.add_thread.start()

       
        '''for i in range(0, len(faceList)):
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
            print(face_string)
            api.faceset.addface(outer_id='test2', face_tokens=face_string)
            if (e):
                break;'''
        

    def deleteFace(self):
        reply = QtWidgets.QMessageBox.warning(self, '删除','将删除您的人脸数据集并且删除签到记录，确定吗？',QtWidgets.QMessageBox.Yes|
                                                QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        if(reply == 65536):
            return
        with open('arrive_data.csv', 'w', encoding='utf-8') as filename:
            filename.truncate()
        with open('arrive_emotion.csv','w', encoding='utf-8') as filename:
            filename.truncate()
        with open('face_token_set.csv', 'w', encoding='utf-8') as filename:
            filename.truncate()
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
        detec_res = api.detect(image_file = File(face_search_img[0]), return_attributes = 'emotion')

        print_result("搜索结果", serach_res)
        print_result("探测结果", detec_res)
        #serach_list用于将serach_res中的faces部分信息转换为列表
        #输出特定的face_token
        serach_result = serach_res['results']
        #输出对应的置信值
        serach_confidence = serach_result[0]['confidence']
        face_token = serach_result[0]['face_token']
        threshold_up = serach_res['thresholds']['1e-5']
        #threshold_down = serach_res['thresholds']['1e-3']
        
        #print_result('探测结果', detec_res)
        detec_res = detec_res['faces']
        down_emotion_detect = (detec_res[0]['attributes']['emotion']['disgust'] + detec_res[0]['attributes']['emotion']['anger']
                                + detec_res[0]['attributes']['emotion']['fear'] + detec_res[0]['attributes']['emotion']['sadness']) / 4
        up_emotion_detect = (detec_res[0]['attributes']['emotion']['happiness'] + detec_res[0]['attributes']['emotion']['neutral']) / 2
        
        if(serach_confidence >= threshold_up):
            print(face_token+'到位了')
            self.data_manager.load_data_to_dict()
            self.data_manager.load_emotion_to_dict()
            self.data_manager.add_arrive_data(face_token, QtCore.QDateTime.currentDateTime().toString('yyyy-MM-dd hh:mm:ss'))
            self.data_manager.add_emotion_data(face_token, (up_emotion_detect/down_emotion_detect))
            self.data_manager.write_data_to_csv()
            self.data_manager.write_emotion_to_csv()


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


    def signIn(self):
        r = api.faceset.getdetail(outer_id='test2')
        print_result('faceset内部结果', r)
        pass

    def enable_btn(self):
        self.btn_startSignIn.setEnabled(True)
        self.btn_signIn.setEnabled(False)
        self.timer.stop()


class Thread(QtCore.QThread):
    sinOut = QtCore.pyqtSignal()
    def __init__(self):
        super(Thread, self).__init__()
        self.faceList = []
        
    def run(self):

        for i in range(len(self.faceList)):
            api.faceset.addface(outer_id='test2', face_tokens=self.faceList[i]["face_token"]);
            print(self.faceList[i]["face_token"])
        self.sinOut.emit()
        
        


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    main_window = My_UI()
    add_thread = Thread()
    main_window.show()
    sys.exit(app.exec_())
