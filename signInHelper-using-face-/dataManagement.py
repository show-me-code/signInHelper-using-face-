# -*- coding: utf-8 -*-
import pandas as pd
from collections import defaultdict
import os
import numpy
import matplotlib.pyplot as plt
from math import isnan

class data_management():
    arrive_data = defaultdict(list)
    arrive_name = defaultdict(str)
    face_token_set = []
    arrive_emotion = defaultdict(list)

    def init_data(self, face_token):
        # 每次初始化的时候都会全部加一行
        for i in range(len(face_token)):
            self.arrive_data[face_token[i]].append(' ')

    def init_emotion(self, face_token):
        for i in range(len(face_token)):
            self.arrive_emotion[face_token[i]].append('')

    def add_name_data(self, face_token, name):
        #为face_token{key},添加姓名{value}
        self.arrive_name[face_token] = name

    def add_arrive_data(self, face_token, time):
        #将列表的最后一行改为time
        self.arrive_data[face_token][-1] = time

    def add_emotion_data(self, face_token, emotion):
        self.arrive_emotion[face_token][-1] = emotion

    def write_data_to_csv(self):
        #打开arrive_data.csv，将字典变为data_frame，存储在其中
        with open('arrive_data.csv', 'w', encoding='utf-8') as file_data:
            data_frame = pd.DataFrame(data=self.arrive_data)
            data_frame.to_csv(file_data, index=False)

    def load_data_to_dict(self):
        #打开存储到位信息的csv，若文件大小小于2字节，则返回，不装载
        with open('arrive_data.csv', 'r', encoding='utf-8') as file_data:
            # 因为基础文件就有2字节大
            if (os.path.getsize('arrive_data.csv') <= 2):
                print('空文件')
                return
            else:
                #按照list形式装载字典
                data_frame = pd.read_csv(file_data)
                self.arrive_data = data_frame.to_dict('list')
    
    def write_name_to_csv(self):
        #打开arrive_name.csv，将姓名信息变为data_frame，存储
        with open('arrive_name.csv', 'w', encoding='utf-8') as file_name:
            data_frame = pd.DataFrame(data=self.arrive_name, index=[0])
            data_frame.to_csv(file_name)
    
    def load_name_to_dict(self):
        #打开存储姓名信息的csv，若文件大小小于2字节，则返回，不装载
        #否则，读取data_frame变为，使用to_dict转换为字典
        with open('arrive_name.csv', 'r', encoding='utf-8') as file_name:
            if (os.path.getsize('arrive_name.csv') <= 2):
                print('空文件')
                return
            else:
                data_frame = pd.read_csv(file_name)
                self.arrive_name = data_frame.to_dict('dict')
    
    def write_emotion_to_csv(self):
        with open("arrive_emotion.csv", 'w', encoding='utf-8') as file_emotion:
            data_frame = pd.DataFrame(data=self.arrive_emotion)
            data_frame.to_csv(file_emotion, index=False)
    
    def load_emotion_to_dict(self):
        with open('arrive_emotion.csv', 'r', encoding='utf-8') as file_emotion:
            if(os.path.getsize('arrive_emotion.csv') <= 2):
                print('空文件')
                return
            else:
                data_frame = pd.read_csv(file_emotion)
                self.arrive_emotion = data_frame.to_dict('list')

    def write_face_token_to_csv(self, face_token):
        with open('face_token_set.csv', 'w', encoding='utf-8') as file_face_token:
            data_frame = pd.DataFrame(data=self.face_token_set)
            data_frame.to_csv(file_face_token)

    #将face_token装入列表
    def load_face_token_to_list(self):
        with open('face_token_set.csv', 'r', encoding='utf-8') as file_face_token:
            if (os.path.getsize('face_token_set.csv') <= 2):
                print('空文件')
                return
            else:
                data_frame = pd.read_csv(file_face_token)
                faces = numpy.array(data_frame)
                faces = faces.tolist()
                for i in range(len(faces)):
                    self.face_token_set.append(faces[i][1])
    
    #装载数据显示每个学生到位次数并以图标显示
    def load_csv_pic(self):
        x = []
        y = []
        self.load_data_to_dict()
        arrive_data_local = self.arrive_data
        x = list(arrive_data_local.keys())
        for i in range(len(x)):
            count = 0
            for j in range(len(arrive_data_local[x[i]])):
                if(arrive_data_local[x[i]][j] == ' '):
                    continue
                else:
                    count += 1
            y.append(count)
        plt.style.use("ggplot")
        x_index= range(len(x))
        fig = plt.figure()
        ax1 = fig.add_subplot(1,1,1)
        ax1.bar(x_index, y, align = 'center', color = 'darkgreen')
        ax1.xaxis.set_ticks_position('bottom')
        ax1.yaxis.set_ticks_position("left")
        plt.xticks(x_index, x, rotation = 0, fontsize = 'small')
        plt.xlabel('face_token')
        plt.ylabel("in place number")
        plt.title('analyze of arrive')
        plt.show()
    
    #得到每位学生的到位率在百分之几
    def given_arrive_percent(self):
        x = []
        y = []
        percent = [] # 超过了除自己之外的多少人
        better_than = 0
        self.load_data_to_dict()
        arrive_data_local = self.arrive_data
        x = list(arrive_data_local.keys())
        for i in range(len(x)):
            count = 0
            for j in range(len(arrive_data_local[x[i]])):
                if arrive_data_local[x[i]][j] == ' ':
                    continue
                else:
                    count += 1
            y.append(count)
        
        for i in range(len(y)):
            for j in range(len(y)):
                if(y[i] >= y[j]):
                    better_than += 1
            percent.append((better_than-1)/(len(x)-1)*100)
            better_than = 0
        return percent
    
    #得到到位率高的学生并得到到位率
    def get_percent_high(self):
        dict_percent_high = {}
        x = []
        self.load_data_to_dict()
        arrive_data_local = self.arrive_data
        x = list(arrive_data_local.keys())
        percent = self.given_arrive_percent()
        for i in range(len(percent)):
            if(percent[i] >= 75):
                dict_percent_high[x[i]] = percent[i]
        return dict_percent_high
    

    #得到到位率低的学生和到位率
    def get_percent_low(self):
        dict_percent_low = {}
        x = []
        self.load_data_to_dict()
        arrive_data_local = self.arrive_data
        x = list(arrive_data_local.keys())
        percent = self.given_arrive_percent()
        for i in range(len(percent)):
            if(percent[i] <= 25):
                dict_percent_low[x[i]] = percent[i]
        return dict_percent_low
    
    #正式给出建议，计算总的签到次数并且统计签到个人签到次数
    def give_advice_times(self):
        self.load_data_to_dict()
        arrive_data_local = self.arrive_data
        sign_len = 0
        sign_low_len = 0
        sign_low_dict = {}
        x = []
        y = []
        x = list(self.get_percent_low().keys())

        for k in arrive_data_local:
            sign_len = len(arrive_data_local[k])
            break
        for i in range(len(x)):
            for j in range(len(arrive_data_local[x[i]])):
                if arrive_data_local[x[i]][j] == ' ':
                    continue
                else:
                    sign_low_len += 1
            sign_low_dict[x[i]] = sign_low_len
            sign_low_len = 0
        return sign_len,sign_low_dict

    def given_advice_mood(self):
        avg_emotion = 0
        count = 0
        emotion_dict = {}
        sign_len,sign_low_dict = self.give_advice_times()
        self.load_emotion_to_dict()
        emotion_local = self.arrive_emotion
        for k in sign_low_dict:
            avg_temp = 0
            for j in range(len(emotion_local[k])):
                if(emotion_local[k][j] == " "):
                    continue
                else:
                    if(isnan(emotion_local[k][j])):
                        continue
                    else:
                        avg_temp += emotion_local[k][j]
            emotion_dict[k] = avg_temp/sign_low_dict[k]
        for k in emotion_local:
            for j in range(len(emotion_local[k])):
                if(emotion_local[k][j] == ' '):
                    continue
                else:
                    if(isnan(emotion_local[k][j])):
                        continue
                    else:
                        avg_emotion += emotion_local[k][j]
                    count += 1
        avg_emotion = avg_emotion/count
        return avg_emotion, emotion_dict
    
    def give_serach_pic(self):
        file_dir = os.path.abspath('.')
        jpg_file = []
        for root, dirs, files in os.walk(file_dir):
            for f in files:
                if os.path.splitext(f)[1] == '.jpg':
                    jpg_file.append(os.path.join(root, f))
        return jpg_file[-1]

if(__name__ == '__main__'):
    d = data_management()
    print(d.load_csv_pic())
