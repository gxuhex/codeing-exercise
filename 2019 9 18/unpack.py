#定义读取文件内容
#文件为12.txt
f = open('12.txt', 'r')              
sourceInLines = f.readlines()  #按行读出文件内容
f.close()