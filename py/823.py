def my_max(x, y) :
    '''
    获取两个数值之间较大的函数.

    my_max(x, y) 
        返回两个参数之间较大的那个
    '''

    #定义一个变量z,该变量等于x,y中较大的值
    z = x if x > y else y
    #返回变量z的值
    return z
#使用help()函数查看my_max的帮助文档
help(my_max)
print(my_max.__doc__)


def my_max(x, y) :
    #返回一个表达式
    return x if x > y else y

#定义一个函数,声明一个形参
def say_hi(name) :
    print("===正在执行say_hi函数===")
    return name + "您好!"
a = 6
b = 9
#调用my_max()函数,将函数返回值赋值给result变量
result = my_max(a, b) #1
print("result :", result)
#调用say_hi函数,直接输出函数的返回值
print(say_hi('孙悟空')) #2


def sum_and_avg(list) :
    sum = 0
    count = 0
    for e in list :
        #如果元素e是数值
        if isinstance(e, int) or isinstance(e, float) :
            count += 1
            sum += e
    return sum, sum / count
my_list = [20, 15, 2.8, 'a', 35, 5.9, -1.8]
#获取sum_and_zvg函数返回的多个值,多个返回值封装成元组
tp = sum_and_avg(my_list) #1
print(tp)
#使用序列解包来获取多个返回值
s, avg = sum_and_avg(my_list) #2
print(s)
print(avg)

def fn(n) :
    if n == 0 :
        return 1
    elif n == 1:
        return 4
    else :
        #函数中调用自己就是递归
        return 2 * fn(n - 1) + fn(n - 2)
#输出fn(10)的结果
print("fn(10)的结果是:", fn(10))

#为两个参数设置默认值
def say_hi(name = "孙悟空", message = "欢迎来到疯狂软件") :
    print(name, ", 您好")
    print("消息是: ", message)
#全部使用默认参数
say_hi()
#只有message使用默认参数
say_hi("白骨精")
#两个参数都不使用默认参数
say_hi("白骨精","欢迎学习python")
#只有name参数使用默认值
say_hi ("欢迎学习python")



say_hi("白骨精", message = "欢迎学习python")
say_hi(name = "白骨精", message = "欢迎学习python")


#定义一个打印三角形的函数, 有默认值的参数须放在后面
def printTriangle(char, height = 5) :
    for i in range(1, height + 1) :
        #先打印一排空
        for j in range(height - i) :
            print(char, end = '')
        print()
printTriangle("@", 6)
printTriangle('#', height = 7)
printTriangle(char = '*')

def swap(dw) :
    #下面的代码实现dw的a, b两个元素的互换
    dw['a'], dw['b'] = dw['b'], dw['a']
    print("swap函数里, a元素的值是",\
        dw['a'], "; b元素的值是", dw['b'])
    #把dw直接赋值为none,让她不再指向任何对象
    dw = None
dw = {'a': 6, 'b': 9}
swap(dw)
print("交换结束后,a元素的值是",\
    dw['a'], ";b元素的值是", dw['b'])

name = 'Charile'
def test() :
    #直接访问name全局变量
    print(globals()['name']) #Charile
    name = "孙悟空"
test()
print(name)  #Charile

name = 'Charile'
def test() :
    #申明name是全局变量,后面的赋值语句不会重新定义局部变量
    global name
    #直接访问 name全局变量
    print(name)   #Charile
    name = '孙悟空'
test()
print(name)

#问题代码
'''
name = 'Charile'
def test() :
    #直接访问name全局变量
    print(name) #Charile
    name = '孙悟空'
test()
print(name)

'''

def swap(a, b) :
    #下面代码实现a, b变量的值交换
    a, b = b, a
    print("swap的函数里,a的值是:"\
        ,a,";交换变量b的值是", b)
a = 6
b = 9
swap(a, b)
print("交换结束后,变量a的值是",\
    a,"变量b的值是:",b)


def test() :
    age = 20
    #直接访问age局部变量
    print(age) #输出20
    #访问函数局部范围的"变量数组"
    print(locals()) #{'age':20}
    #通过函数局部范围的"变量数组"访问age变量的值
    locals()['age'] = 12
    #再次访问age变量的值
    print('xxx', age) #依然输出20
    #通过globals函数修改x全局变量
    globals()['x'] = 19
x = 5
y = 20
print(globals()) #
#通过全局访问locals函数,访问的是全局变量的'变量数组"
print(locals())
#直接访问x全局变量
print(x) #5
#通过去哪聚变量的"变量数组"来访问x全局变量
print(globals()['x'])  #5
#通过