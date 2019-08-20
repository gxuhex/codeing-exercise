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

#定义一个数值类型的变量
a = 5
print(5)

#重新将字符串赋值给a变量
a = 'Hello Charlie'
print(a)
print(type(a))

ac1 = 3 + 0.2j
print(ac1)

print(type(ac1))   #输出complex类型

ac2 = 4 - 0.1j
print(ac2)
print(type(ac2))
#复数运行
print(ac1 + ac2)

#导入cmath模块
import cmath

#sqrt()是cmath下的函数,计算平方根
ac3 = cmath.sqrt(-1)
print(ac3)              #开-1的平方 得到的是复数的单位

af1 = 5.234556
#输出af1的值
print("af1的值为:", af1)

af2 = 25.2345

print("af2的值为:", af2)

f1 = 5.12e2

print("f1的值为:", f1)

f2 = 5e3

print("f2的值为:", f2)
print("f2的类型为:", type(f2))      #f2的类型为float

#以0X或0x为开头的是十六进制的整数
hex_value1 = 0x13
hex_value2 = 0XaF

print("hexvalue1的值为:", hex_value1)
print("hexvalue2的值为:", hex_value2)

#以0b或者0B开头的整数是二进制整数
bin_val = 0b111
print("bin_val的值为: ", bin_val)
bin_val = 0B101
print("bin_val的值为: ", bin_val)

#以0o或者0O开头的值是八进制的整数
oct_val = 0o54
print("oct_val的值为: ", oct_val)
oct_val = 0O17
print("oct_val的值为: ", oct_val)

#在数值中使用下划线
one_million = 1_000_000
print(one_million)
price = 234_234_234             #price的实际值为234234234
android = 1234_1234             #android的实际值为12341234
print(price,android)

#定义变量a, 赋值为36
a = 56
print(a)

#为a赋一个大整数
a = 9999999999999999999999
print(a)

print(type(a))
a = None

print(a)

#创建一个空的bytes
b1 = bytes()
#创建一个空的bytes值
b2 = b''
#通过bytes方法将字符串转换成bytes对象
b3 = b'hello'
print(b3)
print(b3[0])
print(b3[2:4])
#调用bytes方法将字符串转成bytes对象
b4 = bytes('我爱Python编程', encoding = 'utf-8')
print(b4)

#利用字符串的encode()方法编码成bytes,默然使用utf-8字符集
b5 = "学习Python很有趣".encode('utf-8')
print(b5)

#将bytes对象解码成字符串, 默认使用utf-8进行解码
st = b5.decode('utf-8')
print(st)

msg = input("请输入你的值")
print(type(msg))
print(msg)

s = '''"Let's go fishing",said mary."oK,let's go",said brother.they walked to lake'''
print(s)

s2 = 'The quick brown fox \
jump over the lazy dog'

print(s2)

num = 20 + 3/4 + \
    2 * 3
print(num)

#raw_str这个是什么意思
s1 = r'G:\publish\codes\02\2.4'
print(s1)

#原始字符串包含的的引号需要进行转义
s2 = r'"Let\'s go", said Charlie'
print(s2)

s3 = r'Good Morning''\\'
print(s3)

s1 = "hello," 'Charile'
print(s1)
s2 = "Python "
s3 = "is Funny"
#使用+拼接字符串
s4 = s2 + s3
print(s4)

str1 = 'Charile'
str2 = "疯狂Python"
print(str1)
print(str2)

str3 = "i'm a coder"
str4 = '"spring is here,let us jam!",said woodchunk'
str5 = '"we are scared,let\'s hide in the shadow",says the bird'
print(str5)

s1 = "这本的价格是: "
p = 99.8 
#字符串直接拼接数值,程序报错
#print(s1 + p)
#使用str()将数值转换成字符串
print(s1 + repr(p))
st = "i will paly my life"
print(st)
print(repr(st))

a = 'out domin is crazy.org'
#每个单词首字母大学
print(a.title())
#每个单词首字母小写
print(a.lower())
#每个单词首字母大写
print(a.upper())

s = 'crazy.org is very good'
#获取索引2处的字符
print(s[2])     #输出a
#获取s中从右边开始,索引4处的字符
print(s[-4])    #输出g
#获取s中从索引3到索引5处(不含)子串
print(s[3: 5])      #输出zy
#获取s中从索引3到倒数第五个字符的子串
print(s[3: -5])     #输出zy.org is very 
#获取s中从倒数第六个字符到倒数第三个字符的子串
print(s[-6: -3])    #y g  后一个合适不包含的
#获取s中索引5处到到结束的子串
print(s[5: ])       #输出org is very good
#获取s中从倒数第6个字符到结束的子串
print(s[-6: ])      #输出y good
#获取开始到索引5处的子串
print(s[: 5])       #输出crazy
#获取s中从开始到倒数第6个字符的子串
print(s[:-6])
#判断s中是否包含'very'子串
print('very' in s)      #true
print('fkit' in s)      #false
#输出s的长度
print(len(s))
#输出test的长度
print(len('test'))
#输出s字符串中最大的字符
print(max(s))
#输出s字符串中最小的字符
print(min(s))  

s = 'Hello\nCharlie\nGood\nMoring'
print(s)
s2 = '商品名\t\t单价\t\t数量\t\t总价'
s3 = '疯狂java讲义\t108\t\t2\t\t316'
print(s2)
print(s3)

price = 108
print("the book's price is %x" %price)
user = "Charli"
age = 8
#格式化字符串有两个占位符,第三部分提供两个变量
print("%s is a %s years old boy" %(user, age))
num = -28
print("num is : %6i"%num)
print("num is : %6d"%num)
print("num is : %6o"%num)
print("num is : %6x"%num)
print("num is : %6X"%num)
print("num is : %6s"%num)
num2 = 20
#最小宽度为0,左边补0
print("num2 is: %06d"% num2)
#最小的宽度为6,左边补0,总带上符号
print("num2 is: %+06d"%num2)
#最小宽度为6,右对齐
print("num2 is: %-6d" %num2)
my_value = 3.001415926535
#最小宽度为8,小数点后保留3位,左边补0,始终待符号
print("my_value is %+08.3f" %my_value)
the_name = "Charile"
#只保留3个字符
print("the name is : %3s" %the_name)  #输出Cha
#只保留2个字符,最小宽度是10
print("the name is : %10.2s" %the_name)

s = 'crazyit.org is a good site'
#判断s是否以crazy开头
print(s.startswith('crazyit'))
#判断是否是以site结尾
print(s.endswith('site'))
#查找s中'org'出现的位置
print(s.find('org'))
#从索引为9处开始查找'org'的出现位置
print(s.find('org',9))
#从索引处为9处开始查找'org'的出现位置
#print(s.index('org',9))
#将字符串中所有的it替换成xxxx
print(s.replace('it','xxxx'))
#将字符串中1个it替换成xxxx
print(s.replace('it','xxxx',1))
#定义替换表:97(a) - 945(&),98(b)-945(*),116(t)-946(%)   特殊字符不知道如何输入
table = {97: 945, 98: 946, 116: 964}
print(s.translate(table))

s = 'crazyit.org is good site'
#使用空白字符对字符串进行分割
print(s.split())        #输出'crazyit.org','is','a','good','site'
#使用空白对字符串进行分割,最多只分割前两个单词
print(s.split(None,2))  #输出['crazyit.org','is','a good site']
#使用点进行分割
print(s.split('.')) #输出['crazyit','org is a good site']
mylist = s.split()
#使用'/'为分割符,将mylist连接成字符串
print('/'.join(mylist))     #输出crazyit.org/is/a/good/site
#使用','作为分割符,将mylist连接成字符串
print(','.join(mylist))     #输出 crazyit.otg,id,a,good,site

#2.5    strip_test.py
s = '      this is a puppy  '
#删除左边的空白
print(s.lstrip())
#删除右边的空白
print(s.rstrip())
#删除两边的空白
print(s.strip())
#再次输出,将会看到S右没有改变
print(s)

s2 = 'i think it is a scarecrow'
#删除左边的i,t,o,w字符
print(s2.lstrip('itow'))
#删除右边的i,t,o,w字符
print(s2.rstrip('itow'))
#删除两边的额i,t,o,w字符
print(s2.strip('itow'))

a = 5.2
b = 3.1 
the_sum = a + b
#sum的值为8.3
print("the_sum的值为; ", the_sum)

s1 = 'Hello, '
s2 = 'Charlie'
#使用+连接这两个字符串
print(s1 + s2)

c = 5.2
d = 3.1
sub = c - d
#sub的值为
print('sub的值为: ', sub)

e = 5.2
f = 3.1
multiply = e * f
#multiply 的值
print("multiply的值为: ", multiply)

s3 = 'crazyit'
#使用*将5个字符串连接起立
print(s3 * 5)

print("19/4的结果为: ", 19/4)
print("19//4的结果是: ", 19//4)
aa = 5.2 
bb = 3.1
#aa/bb的值将是1.677419..
print("aa/bb的值将是: ", aa/bb)
#aa//bb的值将是1.0
print("aa//bb的值是: ", aa//bb)

print('5的2次方: ', 5 ** 2)  #25
print('4的3次方: ', 4 ** 3)     #64
print('4的开平方: ', 4 ** 0.5)      #2.0
print('27开三次方: ', 27 ** (1/3))  #3.0

#为变量st赋值Python
st = "Python"
#为变量pi赋值3.14
pi = 3.14
#为变量visited赋值为Ture
visited = True
print(st)
print(pi)
print(visited)

#将变量st的值赋给st2
st2 = st 
print(st2)

a = b = c = 20
print(a)
print(b)
print(c)

d1 = 12.34
#将表达式的值赋给d2
d2 = d1 + 5 
#输出d2的值
print("d2的值为:%g" %d2)

#将输出1
print(5 & 9)
#将输出13
print(5 | 9)

a = -5
#将输出4
print(~a)
#将输出12
print(5 ^ 9)

#输出20
print(5 << 2)
#输出-20
print(-5 << 2)

b = -5
#输出-2
print(b >> 2)

bookName = "疯狂Python"
price = 79
version = "正式版"
if bookName.endswith("Python")and(price<50 or version == "正式版"):
    print("打算购买这本Python图书")
else:
    print("不购买! ")

#输出Ture
print("5是否大于4: ", 5 > 4)
#输出False
print("3的4次方大于等于90.0: ", 3 ** 4 >= 90)
#输出Ture
print("20是否大于等于20.0: ", 20 >= 20.0)
#输出Ture
print("5和5.0是否相等: ", 5 == 5.0)
#输出False
print("Ture和False是否相等: ", True == False)


#输出Ture
print("1和Ture是否相等: ", 1 == True)
#输出Ture 
print("0和Ture是否相等: ", 0 == False)
print(True + False)
print(False - True)

import time
#获取当前时间
a = time.gmtime()
b = time.gmtime()
print(a == b)
print(a is b)
print(id(a))
print(id(b))

s = 'crazyit.org'
print('it' in s)    #True
print('it' not in s)    #False
print('fkit' in s)  #False
print('fkit' not in s)  #True

a = 'abcdefghijklmn'
#获取索引2到索引8的子串,步长为3
print(a[2:8:3])
#获取索引2到索引8的子串,步长为2
print(a[2:8:2])

#直接对False求非运算,将返回True
print(not False)
#5>3返回True,20.0大于10,因此结果返回True
print(5 > 3 and 20.0 > 10)
#4 >= 5返回False,"c">"a"返回True.求或后返回True
print(4 >= 5 or "c" > "a")

print("5%3的值为: ", 5 % 3) #输出2
print("5.2%3.1的值为: ", 5.2 % 3.1)  #输出2.1
print("-5.2%-3.1的值为: ", -5.2 % -3.1) #输出-2.1
print("5.2%-2.9的值为: ", 5.2 % -2.9)   #输出-0.6
print("5.2%-1.5的值为: ", 5.2 %-1.5)    #输出-0.8
print("-5.2%1.5的值为: ", -5.2 %1.5)    #输出0.8

#定义变量s,其值为-5.0
x = -5.0
#将x求负,其值变成5.0
x = -x
print(x)
#定义变量y,其值为-5.0
y = -5.0
#y的值依然是-5.0
y = +y
print(y)

a = 5
b = 3
st = "a大于b" if a>b else "a不大于b"
#输出a大于b
print(st)

#输出'a大于b"
print("a大于b") if a > b else print("a不大于b")

#第一个返回值部分使用两条语句,逗号隔开
st = print("crazyit"), 'a大于b' if a > b else "a不大于b"
print(st)

#第一个返回值部使用两条语句,分号隔开
st = print("crazyit"); x = 20 if a > b else "a不大于b"
print(st)
print(x)

c = 5
d = 5
#下面将输出c等于d
print("c大于d") if c > d else (print("c小于d") if c < d \
    else print("c等于d"))


#使用方括号定义列表
my_list = ['crazyit', 20, 'Python']
print(my_list)
#使用圆括号定义元组
my_tuple = ('crazyit', 20, 'Python')
print(my_tuple)

#元素都是数值的元组
a_tuple = (20, 10, -2, 15.2, 102, 50)
#计算最大值
print(max(a_tuple))
#计算最小值
print(min(a_tuple))
#计算长度
print(len(a_tuple))
#元素都是字符的列表
b_list = ['crazy', 'fkit', 'Python', 'Kotlin']
#计算最大值(依次比较ASCII码26个字母97~122)
print(max(b_list))
#计算最小值
print(min(b_list))
#计算长度
print(len(b_list))


a_tuple = ('crazy', 20, -1.2)
print(20 in a_tuple)
print(1.2 in a_tuple)
print('fkit' not in a_tuple)

a_tuple = ('crazyit', 20, 5.6, 'fkit', -17)
print(a_tuple)
#访问第一个元素
print(a_tuple[0])
#访问第2个元素
print(a_tuple[1])
#访问第2个元素
print(a_tuple[-1])
#访问倒数第2个元素
print(a_tuple[-2])


a_tuple = ('fkit', 20)
#执行乘法
mul_tuple = a_tuple * 3
print(mul_tuple)
a_list = [30, 'Python', 2]
mul_list = a_list * 3
print(mul_list)

a_tuple = ('crazyit', 20, -1.2)
b_tuple = (127, 'crazyit', 'fkit', 3.33)
#计算元组相加
sum_tuple = a_tuple + b_tuple
print(sum_tuple)
print(a_tuple)
print(b_tuple)
#两个元组相加
print(a_tuple + (-20, -30))
#列表和元组不能相加
a_list = [20, 30, 50, 100]
b_list = ['a', 'b', 'c' ]
#计算列表相加
sum_list = a_list + b_list
print(sum_list)
print(a_list + ['fkit'])

#序列封包:将10,20,30封装成元组后赋值给vals
vals = 10, 20, 30
print(vals)
print(type(vals))
print(vals[1])
a_tuple = tuple(range(1, 10, 2))
#序列解包,将a_tuple的各元素一次赋值给a,b,c,d,e变量
a, b, c, d, e = a_tuple
print(a, b, c, d, e)
a_list = ['fkit', 'crazyit']
#序列解包,将a_list序列的各元素赋值给a_str,b_str变量
a_str, b_str = a_list
print(a_str, b_str)

#将10,20,30依次赋给x,y,z
x,y,z = 10, 20, 30
print(x, y, z)
#将y,z,x依次赋给x,y,z
x, y, z = y, z, x
print(x, y, z)

#将first\scend保存在前两个元素,rest列表包含剩下的元素
first, second, *rest = range(10)
print(first)
print(second)
print(rest)

#last保存最后一个元素,bengin保存前面剩下的元素
*begin, last = range(10)
print(begin)
print(last)

#first保存第一个元素,last保存最后一个元素,middle保存中间剩下的元素
first, *middle, last = range(10)
print(first)
print(middle)
print(last)


a_tuple = ('crazyit', 20, 5.6, 'fkit', -17)
#访问从第二个到倒数第4个(不包含)所有元素
print(a_tuple[1:3])
#访问从倒数第3个到倒数第一个(不包含)所有元素
print(a_tuple[-3: -1])
#访问从第二个到倒数第二个(不包含)所有元素
print(a_tuple[1: -2])
#访问从倒数第3个到第五个(不包含)所有元素
print(a_tuple[-3: 4])

b_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
#访问从第3个到第9个(不包含)\间隔为2的所有元素
print(b_tuple[2: 8: 2])
#访问从第3个到第9个(不包含)\间隔为3的所有元素
print(b_tuple[2: 8: 3])
#访问从第3个到倒数第2个(不包含)\间隔为3的所有元素
print(b_tuple[2: -2: 2])


#同时对元组使用加法\乘法
order_endings = ('st', 'nd', 'rd')\
    + ('th',) * 17 + ('st', 'nd', 'rd')\
    + ('th',) * 7 +('st',)

#将会看到st\nd\rd\17个th\st\nd\rd\7个th\st
print(order_endings)
day = input("输入日期(1-31): ")
#将支付串转成整数
day_int = int(day)
print(day + order_endings[day_int - 1])

a_list = ['crazyit', 20, -2]
#追加元素
a_list.append('fkit')
print(a_list)
a_tuple = (3.4, 5.6)
#追加元组,元组被当成一个元素
a_list.append(a_tuple)
print(a_list)
#追加列表,列表被当成一个元素
a_list.append(['a', 'b'])
print(a_list)

b_list = ['a', 30]
#追加元组中的所有元素
b_list.extend((-2, 3.1))
print(b_list)
#追加列表中的所有元素
b_list.extend(['C', 'R', 'A'])
print(b_list)
#追加区间的元素
b_list.extend(range(97, 100))
print(b_list)

c_list = list(range(1, 6))
print(c_list)

#在索引3处插入字符串
c_list.insert(3, 'CRAZY')
print(c_list)
#在索引3处插入元组,元组被当成一个元素
c_list.insert(3, tuple('crazy'))
print(c_list)

a_list = [2, 30, 'a', [5, 30], 30]
#计算列表中30出现的次数
print(a_list.count(30)) 
#计算列表中[5, 30]出现的次数
print(a_list.count([5, 30]))