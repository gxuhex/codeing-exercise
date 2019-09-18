#定义读取文件内容
#文件为12.txt
import re
import operator

filename = 'F:\\工作\\2019 9 18\\1234\\33.txt'
f = open(filename, 'r')              
sourceInLines = f.readlines()  #按行读出文件内容
#new = sourceInLines.  #替换掉空格replace(' ', '_')
f.close()
#存储数据
sid, fun, tot, leav, flow, temp, prw, sta= [], [], [], [], [], [], [], []
#定义一个空列表，用来存储结果
#re.findall(r'.{41}',new)
#sourceInLines
for line in sourceInLines:
    temp1 = line.strip().rstrip(',')
    temp2 = temp1.split(',') 
#print(temp2)
'''
pattern = r'[ff]'                      # 定义分隔符
url = str(temp2) # 需要拆分的字符串
result = re.finditer(pattern, url) # 以pattern的值 分割字符串
print(result)
'''
#print(temp1)
#print(temp2)
mate = ['cc', '03', '31', '00', 'ee']
mate0 = ['cc', '02', '31', 'ff', 'ee']
num_data = []



def func(list) :
    data = []
    for i in range(len(list)) :
        j = i + 5
        list1 = list[i : j]        
        if ( operator.ne(mate, list1) and operator.ne(mate0, list1)) :
            data.append(list[i])
            if(operator.eq(mate, list1) or operator.eq(mate0, list1)) :
                return data 
            

        

if (operator.eq(mate,temp2[0:5]) or operator.eq(mate0,temp2[0:5])) :
    i = 0
    data = func(temp2[i+5:])
    num_data.append(data)
    i = 5 + len(data)

for frame in num_data:
    pass
