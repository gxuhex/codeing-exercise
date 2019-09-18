coding:'utf-8'
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import json 
import pygal
import csv
from datetime import datetime
from matplotlib import pyplot as plt
from pylab import *
from matplotlib.ticker import FuncFormatter
import matplotlib.ticker as ticker

mpl.rcParams['font.sans-serif'] = ['SimHei']


#定义读取文件内容
f = open('12.txt', 'r')              #文件为12.txt
sourceInLines = f.readlines()  #按行读出文件内容
f.close()
#存储数据
ia, ib, ic, ua, ub, uc, time = [], [], [], [], [], [], []
new = []                                   #定义一个空列表，用来存储结果
for line in sourceInLines:

    #temp1 = line.strip('\n')       #去掉每行最后的换行符'\n'

    #temp2 = temp1.split(',')     #以','为标志，将每行分割成列表

    #temp3 = eval(temp2)
    #new.append(temp2)          #将上一步得到的列表添加到new中
    
    temp2 = json.loads(line)
    ia.append(temp2['data']['ia'])
    ib.append(temp2['data']['ib'])
    ic.append(temp2['data']['ic'])
    ua.append(temp2['data']['ua'])
    ub.append(temp2['data']['ub'])
    uc.append(temp2['data']['uc'])
    time.append(temp2['time'])
#print (new)

#print(new.get('ib'))


with open ('12.csv', 'w') as f:
    f.write('time, A, B ,C, A, B, C\n')
    for i in range(len(ia)):
        data = '%s, %s, %s, %s, %s, %s, %s\n' % (time[i],ia[i],ib[i],ic[i],ua[i],ub[i],uc[i])
        f.write(data)

#配置缩放比例
def changex(temp, position):
    return int(temp*6)
#配置图形
fig = plt.figure(dpi=128, figsize= (120, 9))
#绘制ia的的折线
plt.plot(sort(time), ua, c = 'red', label = 'a相电压',
    alpha = 0.5, linewidth = 2.0, linestyle = '-.', marker = 'v')
#绘制一条折线
plt.plot(sort(time), ub, c = 'blue', label = 'b相电压',
    alpha = 0.5, linewidth = 3.0, linestyle = '-.', marker = 'o')
    #绘制ia的的折线
plt.plot(sort(time), uc, c = 'black', label = 'c相电压',
    alpha = 0.5, linewidth = 2.0, linestyle = '-.', marker = '^')
#为两个数据的绘图区域填充颜色
#plt.fill_between(time, ua, ub, uc, facecolor = 'blue', alpha = 0.1)
#ax.xaxis.set_major_locator(MultipleLocator(10))

#设置标题
plt.title('相电压')
#为两条坐标设置名称
plt.xlabel('日期')
#plt.xticks()
#plt.MultipleLocator(20)
#该方法绘制斜着的的日期标签
fig.autofmt_xdate()
plt.ylabel("电压（V）")
#显示图例
plt.legend()
ax = plt.gca()
#设置右边坐标轴的颜色(none不显示)
ax.spines['right'].set_color('none')
#设置顶部坐标轴的颜色，（设置为none）不显示
ax.spines['top'].set_color('none')
#设置横轴密度  以下注释效果都一样
tick_spacing = 20
ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))

#plt.gca().xaxis.set_major_formatter(FuncFormatter(changex))
#ax.xaxis.set_major_locator(MultipleLocator(20))
#ax.time.set_major_Formatter(changex)
#FuncFormatter(changex)
#set_major_Formatter(FuncFormatter(changex))
#.ax.set_major_Formatter(FuncFormatter(changex))
plt.show()
plt.savefig('figure.eps')



'''
filename = '12.json'
with open(filename) as f:
    bct_data = json.load(f)
#存储数据
ia, ib, ic, ua, ub, uc, time = [], [], [], [], [], [], []
#将。。。
for btc_dict in bct_data:
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


'''

