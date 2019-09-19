#定义读取文件内容
#文件为33.txt
import re
import operator

filename = 'F:\\工作\\2019 9 19\\1234\\33.txt'
f = open(filename, 'r')              
sourceInLines = f.readlines()  #按行读出文件内容

f.close()
#存储数据
#sid, fun, tot, leav, flow, temp, prw, sta= [], [], [], [], [], [], [], []
#站3的数据
tol3, lea3, std3, fow3, tep3, pres3 = [], [], [], [], [], []
#站2的数据
tol2, lea2, std2, fow2, tep2, pres2 = [], [], [], [], [], []

#存储转换后的数
#站3的数据
etol3, elea3, estd3, efow3, etep3, epres3 = [], [], [], [], [], []
#站2的数据
etol2, elea2, estd2, efow2, etep2, epres2 = [], [], [], [], [], []


for line in sourceInLines:
    temp1 = line.strip().rstrip(',')
    temp2 = temp1.split(',') 

mate = ['cc', '03', '31', '00', 'ee']
mate0 = ['cc', '02', '31', 'ff', 'ee']
data = []       #36
num_data = []
thr = []
tw = []


def func(list) :
    #data = []
    for i in range(len(list)) :
        j = i + 5
        list1 = list[i:j]        
        if (operator.ne(mate, list1) and operator.ne(mate0, list1)) : data.append(list[i])
        else:
            return data   
#        if(operator.eq(mate, list1) or operator.eq(mate0,list1)) : return data 
                

for i in range(len(temp2)) :

        #i = 5 + len(data)
        #i = i*5 + len(data)
 #       h = 0
 #       if(i != 0):h = i * (5 + len(data)//i)

                        
        if (operator.eq(mate,temp2[i:i+5]) or operator.eq(mate0,temp2[i:i+5])) : 
#        if (operator.eq(mate,temp2[h:h+5]) or operator.eq(mate0,temp2[h:h+5])) :

        #i = 0
                #h = i * 5 + len(data) 
                data1 = func(temp2[i+5:])
                #data = func(temp2[h+5:])
                num_data.append(data)
                x = len(data)
                i = 5 + len(data)
                data = []
#                print(l)
        #i += 1

#if (operator.eq(mate,temp2[0:5]) or operator.eq(mate0,temp2[0:5])) :
        #i = 0
        #data = func(temp2[i+5:])
        #num_data.append(data)
        #i = 5 + len(data)


print(num_data)

#按站分包
for frame in num_data :
    if (frame[1] == '03') : thr.append(frame)
    else:
        tw.append(frame)
        #frame[]

    print(tw)
    print(thr)
#    pass

#分包
for frame in thr :
#    tol3, lea3, std3, flow3, temp3, pres3 = frame[5:10], frame[11:16], frame[17:20], frame[21:24], frame[25:28], frame[29:32]
#    pass
    tol3.append(frame[5:11])
    lea3.append(frame[11:17])
    std3.append(frame[17:21])
    fow3.append(frame[21:25])
    tep3.append(frame[25:29])
    pres3.append(frame[29:33])


#print()
print(tol3)

for frame in tw :
    tol2.append(frame[5:11])
    lea2.append(frame[11:17])
    std2.append(frame[17:21])
    fow2.append(frame[21:25])
    tep2.append(frame[25:29])
    pres2.append(frame[29:33])


print(tol3)

#进行转换
for frame1 in tol2 :
    #etol2.append(int(str(frame1[1:4]))*2**int(frame1[0]))
    a = frame1[3] + frame1[4] + frame1[5]
    b = int(a,16)
   
    d = frame1[0] + frame1[1]
    e = int(d,16)
    f = b + e*(10**6)
    g = f / int('800000',16)
    #指数
    h = int(frame1[2], 16)
    i = g*(2**h)
    etol2.append(i)

    #print((frame1[3] + frame1[4] + frame1[5]))


print(g)

#进行转换
for frame1 in tol3 :
    #etol2.append(int(str(frame1[1:4]))*2**int(frame1[0]))
    a = frame1[3] + frame1[4] + frame1[5]
    b = int(a,16)
   
    d = frame1[0] + frame1[1]
    e = int(d,16)
    f = b + e*(10**6)
    g = f / int('800000',16)
    #指数
    h = int(frame1[2], 16)
    i = g*(2**h)
    etol3.append(i)

    #print((frame1[3] + frame1[4] + frame1[5]))

print(etol3)

#对余量进行转换
for frame2 in lea2 :
    #etol2.append(int(str(frame1[1:4]))*2**int(frame1[0]))
    #a = frame1[3] + frame1[4] + frame1[5]
    #b = int(a,16)
   #
    #d = frame1[0] + frame1[1]
    #e = int(d,16)
    #f = b + e*(10**6)
    #g = f / int('800000',16)
    ##指数
    #h = int(frame1[2], 16)
    #i = g*(2**h)
    #elea2.append(i)

    #print((frame1[3] + frame1[4] + frame1[5]))
    #(frame1[0] == '01') ? a: b
    a = frame2[1] + frame2[2] + frame2[3] + frame2[4] + frame2[5] 
    b = int(a, 16)
    if frame2[0] == '01': c = 0 - b
    else : c = b
    elea2.append(c)



print(elea2)

#对余量进行转换
for frame2 in lea3 :
    #etol2.append(int(str(frame1[1:4]))*2**int(frame1[0]))
   # a = frame1[3] + frame1[4] + frame1[5]
   # b = int(a,16)
   #
   # d = frame1[0] + frame1[1]
   # e = int(d,16)
   # f = b + e*(10**6)
   # g = f / int('800000',16)
   # #指数
   # h = int(frame1[2], 16)
   # i = g*(2**h)
   # elea3.append(i)

    #print((frame1[3] + frame1[4] + frame1[5]))
    a = frame2[1] + frame2[2] + frame2[3] + frame2[4] + frame2[5] 
    b = int(a, 16)
    if frame2[0] == '01': c = 0 - b
    else : c = b
    elea3.append(c)


print(elea3)


#剩下的4个元素
for frame3 in std2 :
    a = frame3[1] + frame3[2] + frame3[3]
    b = int(a,16)
   
    #d = frame1[0]
    #e = int(d,16)
    #f = b + e*(10**6)
    g = b / int('800000',16)
    #指数
    h = int(frame1[0], 16)
    i = g*(2**h)
    estd2.append(i)

print(estd2)

#剩下的4个元素
for frame3 in std3 :
    a = frame3[1] + frame3[2] + frame3[3]
    b = int(a,16)
   
    #d = frame1[0]
    #e = int(d,16)
    #f = b + e*(10**6)
    g = b / int('800000',16)
    #指数
    h = int(frame1[0], 16)
    i = g*(2**h)
    estd3.append(i)

print(estd3)

for frame3 in fow2 :
    a = frame3[1] + frame3[2] + frame3[3]
    b = int(a,16)
   
    #d = frame1[0]
    #e = int(d,16)
    #f = b + e*(10**6)
    g = b / int('800000',16)
    #指数
    h = int(frame1[0], 16)
    i = g*(2**h)
    efow2.append(i)

print(efow2)

for frame3 in fow3 :
    a = frame3[1] + frame3[2] + frame3[3]
    b = int(a,16)
   
    #d = frame1[0]
    #e = int(d,16)
    #f = b + e*(10**6)
    g = b / int('800000',16)
    #指数
    h = int(frame1[0], 16)
    i = g*(2**h)
    efow3.append(i)

print(efow3)

for frame3 in tep2 :
    a = frame3[1] + frame3[2] + frame3[3]
    b = int(a,16)
   
    #d = frame1[0]
    #e = int(d,16)
    #f = b + e*(10**6)
    g = b / int('800000',16)
    #指数
    h = int(frame1[0], 16)
    i = g*(2**h)
    etep2.append(i)

print(etep2)

for frame3 in tep3 :
    a = frame3[1] + frame3[2] + frame3[3]
    b = int(a,16)
   
    #d = frame1[0]
    #e = int(d,16)
    #f = b + e*(10**6)
    g = b / int('800000',16)
    #指数
    h = int(frame1[0], 16)
    i = g*(2**h)
    etep3.append(i)

print(etep3)

for frame3 in pres2 :
    a = frame3[1] + frame3[2] + frame3[3]
    b = int(a,16)
   
    #d = frame1[0]
    #e = int(d,16)
    #f = b + e*(10**6)
    g = b / int('800000',16)
    #指数
    h = int(frame1[0], 16)
    i = g*(2**h)
    epres2.append(i)

print(epres2)

for frame3 in pres3 :
    a = frame3[1] + frame3[2] + frame3[3]
    b = int(a,16)
   
    #d = frame1[0]
    #e = int(d,16)
    #f = b + e*(10**6)
    g = b / int('800000',16)
    #指数
    h = int(frame1[0], 16)
    i = g*(2**h)
    epres3.append(i)

print(epres3)



