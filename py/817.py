'''
多段注释 以下是一个简单的输出语句
使用UTF-8编码
'''

#coding: utf-8

print('hello world')

#这个也是一个简单的注释

#print('nihao 2019 !')

user_name = 'Charlie'
user_age = 8

#同时输出多个变量和字符串

print("读者名:", user_name,"年龄:",user_age)

#同时输出多个变量和字符串,指定分隔符

print("读者名:", user_name, "年龄:", user_age, sep = '|')

#指定end参数,指定输出后不换行

print(40, '\t', end = "")

print(50, '\t', end = "")

print(60, '\t', end = "")

f = open("poem1.txt","w")   #打开文件以便输入
print("洛阳亲友如相问", file = f)
print("一片冰心在玉壶", file = f)

#doc_read = f.read()
#print(doc_read)
f.close()
#help(__file__)

#导入keyword模块
import keyword

#显示所有关键字
keyword.kwlist