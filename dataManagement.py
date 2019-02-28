# -*- coding: utf-8 -*-
import pandas as pd
import csv
import time
from collections import defaultdict
import os


class data_management():
    arrive_data = defaultdict(list)
    arrive_name = defaultdict(str)

    def init_data(self, face_token):
        # 每次初始化的时候都会全部加一行
        for i in range(len(face_token)):
            self.arrive_data[face_token[i]].append(' ')

    def add_name_data(self, face_token, name):
        #为face_token{key},添加姓名{value}
        self.arrive_name[face_token] = name

    def add_arrive_data(self, face_token, time):
        #将列表的最后一行改为time
        self.arrive_data[face_token][-1] = time

    def write_data_to_csv(self):
        #打开arrive_data.csv，将字典变为data_frame，存储在其中
        with open('arrive_data.csv', 'w', encoding='utf-8') as file_data:
            data_frame = pd.DataFrame(data=self.arrive_data)
            data_frame.to_csv(file_data, index=False)

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
