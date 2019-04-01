import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from collections import defaultdict
from loading import loading_Ui_Dialog, Thread_loading
from UI import Ui_MainWindow
from PyQt5.QtCore import QTimer

from dataManagement import data_management
from adviceUi import advice_ui
from readImage import read_image
# 导入系统库并定义辅助函数
from pprint import pformat
from arrivePercentShow import arrive_show
from PythonSDK.facepp import API,File
# 导入图片处理类


# 以下四项是dmeo中用到的图片资源，可根据需要替换
faceSet_img = ''                      # 用于创建faceSet
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

        self.btn_signIn.setEnabled(False)
        self.timer = QTimer()
        self.timer.timeout.connect(self.enable_btn)
        self.shot_time = QTimer()
        self.shot_time.timeout.connect(self.afterTakeShot)
        self.data_manager = data_management()
        self.data_manager.load_face_token_to_list()
        self.data_manager.load_data_to_dict()
        self.data_manager.load_emotion_to_dict()
        self.data_manager.init_data(self.data_manager.face_token_set)
        self.data_manager.init_emotion(self.data_manager.face_token_set)
        self.loading = loading_Ui_Dialog()
        self.step = 0
        self.add_thread = Thread()
        self.add_thread.sinOut.connect(self.add_finished_connect)

    #在“添加”这一线程结束时触发，结束loading
    def add_finished_connect(self):
        self.loading.close()
        reply = QtWidgets.QMessageBox.information(self,'请重启', '数据已经载入成功，请重新启动', 
                                            QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.Yes)
        print(reply)
        #确认
        if(reply == 16384):
            sys.exit(app.exec_)

    
    def addNewFace(self):
        global faceSet_img
        faceSet_img = QtWidgets.QFileDialog.getOpenFileName(self, 'open the dialog',
                                                                   "C:\\Users\Administrator\Desktop",
                                                                   'JEPG files(*.jpg);;PNG files(*.PNG)')
        faceStr = []; #存储face_token
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
        #在创建时就获得face_token并将其写入文件
        self.data_manager.face_token_set = faceStr
        self.data_manager.write_face_token_to_csv(self.data_manager.face_token_set)
        self.loading.show()
        self.add_thread.faceList = faceList
        self.add_thread.start()

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

    def searchFace(self,face_search_img):

        #不显示图片是因为多线程的问题，单一线程会导致图片和搜索同时，搜索完了图片还没加载
        print(face_search_img)
        QtWidgets.QMessageBox.information(self, '请稍等', '将在几秒钟内完成签到', QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No,
                                         QtWidgets.QMessageBox.Yes)
        #首先显示要搜索的图片
        serach_res = api.search(image_file=File(face_search_img), outer_id='test2');
        detec_res = api.detect(image_file = File(face_search_img), return_attributes = 'emotion')

        print_result("搜索结果", serach_res)
        print_result("探测结果", detec_res)
        #serach_list用于将serach_res中的faces部分信息转换为列表
        #输出特定的face_token
        serach_result = serach_res['results']
        #输出对应的置信值
        serach_confidence = serach_result[0]['confidence']
        face_token = serach_result[0]['face_token']
        threshold_up = serach_res['thresholds']['1e-5']
        detec_res = detec_res['faces']
        down_emotion_detect = (detec_res[0]['attributes']['emotion']['disgust'] + detec_res[0]['attributes']['emotion']['anger']
                                + detec_res[0]['attributes']['emotion']['fear'] + detec_res[0]['attributes']['emotion']['sadness']) / 4
        up_emotion_detect = (detec_res[0]['attributes']['emotion']['happiness'] + detec_res[0]['attributes']['emotion']['neutral']) / 2
        if(serach_confidence >= threshold_up):
            print(face_token+'到位了')
            self.data_manager.add_arrive_data(face_token, QtCore.QDateTime.currentDateTime().toString('yyyy-MM-dd hh:mm:ss'))
            self.data_manager.add_emotion_data(face_token, (up_emotion_detect/down_emotion_detect))
            self.data_manager.write_data_to_csv()
            self.data_manager.write_emotion_to_csv()
        QtWidgets.QMessageBox.information(self, '成功',face_token+"您已经签到成功",QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No,
                                          QtWidgets.QMessageBox.Yes)


    def startSignIn(self):
        #点击这一按钮后选择要开放多长时间签到，随后将签到按钮开放这么长时间
        #在此时只开放这一按钮，其他所有按钮disable
        num,ok = QtWidgets.QInputDialog.getInt(self, '请选择开放签到多长时间', '输入时间（分钟）')
        if ok:
            self.btn_signIn.setEnabled(True)
            self.btn_startSignIn.setEnabled(False)
            self.pushButton.setEnabled(False)
            self.pushButton_2.setEnabled(False)
            self.pushButton_5.setEnabled(False)
            self.pushButton_6.setEnabled(False)
            self.pushButton_7.setEnabled(False)
        self.timer.start(num*60*1000)

    def afterTakeShot(self):
        take_shot.close()
        file_need_serach = self.data_manager.give_serach_pic()
        self.searchFace(file_need_serach)
        self.shot_time.stop()

    def signIn(self):
        take_shot.show()
        self.shot_time.start(10*1000)

    def enable_btn(self):
        self.btn_startSignIn.setEnabled(True)
        self.btn_signIn.setEnabled(False)
        self.pushButton.setEnabled(True)
        self.pushButton_2.setEnabled(True)
        self.pushButton_5.setEnabled(True)
        self.pushButton_6.setEnabled(True)
        self.pushButton_7.setEnabled(True)
        self.timer.stop()

    def showArriveDiagram(self):
        self.data_manager.load_csv_pic()

    def analyzeLowRateStu(self):
        dict_percent_low = self.data_manager.get_percent_low()
        show_percent_dialog.change_ui_low(dict_percent_low)
        show_percent_dialog.show()

    def analyzeHighRateStu(self):
        dict_percent_high = self.data_manager.get_percent_high()
        show_percent_dialog.change_ui_high(dict_percent_high)
        show_percent_dialog.show()

    def giveAdvice(self):
        sign_len, sign_low_dict = self.data_manager.give_advice_times()
        avg_emotion, emotion_dict = self.data_manager.given_advice_mood()
        show_advice.textBrowser.append('您总共发起了' + str(sign_len) + '次签到\n')
        show_advice.textBrowser.append("其中以下同学的到位率较低：\n")
        for k in sign_low_dict:
            show_advice.textBrowser.append(k + "同学的到位次数是：" + str(sign_low_dict[k])+'。\n')
            show_advice.textBrowser.append('这位同学每次上课时的心情是：' + str(emotion_dict[k]) + '，')
            if(emotion_dict[k] > 30):
                show_advice.textBrowser.append('看起来每次来上课的心情都不错。\n')
                show_advice.textBrowser.append('也许您需要结合成绩来决定是否要对这位同学进行学习方法上的指导。\n')
                show_advice.textBrowser.append('您可以观察到位时间表（arrive_data），这位同学在未到位的区段可能有知识的欠缺。\n')
            elif(emotion_dict[k] >= 1 and emotion_dict[k] <= 30):
                show_advice.textBrowser.append('这位同学来上课的心情比较平静。\n')
                show_advice.textBrowser.append('也许您需要结合成绩来决定是否要对这位同学进行学习方法上的指导。\n')
                show_advice.textBrowser.append('您可以观察到位时间表（arrive_data），这位同学在未到位的区段可能有知识的欠缺。\n')
            elif(emotion_dict[k] < 1):
                show_advice.textBrowser.append('这位同学来上课的心情似乎很不好\n')
                show_advice.textBrowser.append('也许这位同学需要心理上的疏导。\n')
                show_advice.textBrowser.append('您可以观察到位时间表（arrive_data），这位同学在未到位的区段可能有知识的欠缺。\n')
        if(avg_emotion < 1):
            show_advice.textBrowser.append('看起来大家来上课的心情都不是很好，心情指数为：'+str(avg_emotion) + '\n')
            show_advice.textBrowser.append('也许您需要活跃课堂气氛？\n')
        if(avg_emotion >= 30):
            show_advice.textBrowser.append('太好了！看起来大家都很乐于上您的课，心情指数达到了：'+str(avg_emotion)+'\n')
        show_advice.show()

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
    show_percent_dialog = arrive_show()
    show_advice = advice_ui()
    take_shot = read_image()
    main_window.show()
    sys.exit(app.exec_())
