import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import json 
import pygal




#定义读取文件内容
f = open('12.txt', 'r')              #文件为12.txt
sourceInLines = f.readlines()  #按行读出文件内容
f.close()
new = []                                   #定义一个空列表，用来存储结果
for line in sourceInLines:

    #temp1 = line.strip('\n')       #去掉每行最后的换行符'\n'

    #temp2 = temp1.split(',')     #以','为标志，将每行分割成列表

    #temp3 = eval(temp2)
    #new.append(temp2)          #将上一步得到的列表添加到new中
print (new)

 #print(new.get('ib'))
    


filename = '12.json'
with open(filename) as f:
    btc_data = json.load(f)
#存储数据
ia, ib, ic, ua, ub, uc, time = [], [], [], [], [], [], []
#将。。。
for btc_dict in btc_data:
    ia.append(int(btc_dict['ia']))
    ib.append(int(btc_dict['ib']))
    ic.append(int(btc_dict['ic']))
    ua.append(int(btc_dict['ua']))
    ub.append(int(btc_dict['ub']))
    uc.append(int(btc_dict['uc']))
    time.append(int(btc_dict['time']))

line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
#标题
line_chart.title = '12'
line_chart.x_labels = ia
#X轴数据
#line_chart.x_labels = dates
#X轴坐标隔20天显示一次
N = 20
line_chart.x_labels_major = ia[::N]
#添加Y轴信息
line_chart.add('时间', time)
line_chart.render_to_file('12.svg')    




