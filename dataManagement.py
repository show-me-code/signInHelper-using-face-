# -*- coding: utf-8 -*-
import pandas as pd
import csv
import time
from collections import defaultdict
import os
import numpy


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


if(__name__ == '__main__'):
    d = data_management()
    face_token = ['123', '456']
    d.load_data_to_dict()
    d.init_data(face_token)
    d.add_arrive_data(face_token[0], time.time())
    d.add_arrive_data(face_token[1], time.time())
    d.write_data_to_csv()