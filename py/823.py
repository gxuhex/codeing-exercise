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
#通过全局变量的"变量数组"来访问x全局变量
print(globals()['x'])  #5
#通过全局变量的'变量数组'对x全局变量赋值
globals()['x'] = 39
print(x)
#在全局范围内使用local()函数对x全局变量赋值
locals()['x'] = 99
print(x)    #输出x


#定义一个函数
def grith(width, height) :
    print("width =", width)
    print("height =", height)
    return 2 * (width + height)
#传统调用函数的方式,根据位置传递参数
print(grith(3.5, 4.8))
#根据关键字参数来传入参数
print(grith(width = 3.5, height = 4.8))
#使用关键字参数时可以交换位置
print(grith(height = 4.8, width = 3.5))
#使用部分关键字参数, 部分使用位置参数
print(grith(3.5, height = 4.8))

#使用参数必须放置在关键字参数之前,下面的代码错误
#print(grith(width = 3.5, 4.8))

#下面定义了三个test()函数, 但函数的形参列表不同
#系统可以区分他们,这被称为函数重载
def test() :
    print("无参数的test()函数")
#该函数类型为(String):Unit
def test(msg) :
    print("重载的test()函数", msg)
#该函数的类型为(Int) : String
def test(msg) :
    print("重载的test()函数%s,带返回值" % msg)
    return "test"
##调用test()时没有传入参数,因此系统调用上面参数的test函数
#test()
#调用带String参数的test()函数
test('fkjava')
#调用带Int类型的test()函数,该函数返回字符串
rt = test(30)
print(rt)

#定义了支持参数收集的函数
def test(a, *books) :
    print(books)
    #books被当成元组处理
    for b in books :
        print(b)
    #输出正数变量a的值
    print(a)
#调用test()函数
test(5, "疯狂ios讲义", "疯狂Android讲义")


#定义了支持参数收集的函数
def test(*books, num) :
    print(books)
    #books被当成元组处理
    for b in books :
        print(b)
    print(num)
#调用test()函数
test("疯狂ios讲义", "疯狂Android讲义", num = 20)

my_list = ["疯狂Swift讲义", "疯狂Python讲义"]
#将列表的多个元素传给支持参数收集的参数
test(my_list, num = 20)
my_tuple = ("疯狂Switf讲义", "疯狂Python讲义")
#将元组的多个元素传给支持参数收集的函数
test(*my_tuple, num = 20)

#定义了支持参数收集的函数
def test(x, y, z = 3, *books, **scores) :
    print(x, y, z)
    print(books)
    print(scores)
test(1, 2, 3, "疯狂ios讲义","疯狂Android讲义",语文 = 89, 数学 = 94)
test(1, 2, "疯狂ios讲义", "疯狂Android讲义",语文 = 89, 数学 = 94)
test(1, 2, 语文 = 89, 数学 = 94)

def test (name, message) :
    print("用户是: ", name)
    print("欢迎消息: ", message)
my_list = ["孙悟空", "欢迎来到疯狂软件"]
test(*my_list)

def foo(name, *nums) :
    print("name参数: ", name)
    print("num参数: ", nums)
my_tuple = (1, 2, 3)
#使用逆向收集,将my_tuple元组的元素传给nums参数
foo('fkit', *my_tuple)

#使用逆向收集,将my_tuple元组的第一个元素传给nums参数
foo('fkit', *my_tuple)

#不使用逆向收集, my-tiple元组整体传给name参数,剩下的催产素传给named手册上
foo(*my_tuple)

#不使用逆向收集, my_tiple元组整体赋值给name参数
foo(my_tuple)

def bar(book, price, dest) :
    print(book, "这本书的价格是: ",price)
    print('描述信息', test)
my_dict = {'price' : 89, 'book' : '疯狂Python讲义', 'desc' : '这就是一本破书' }


#定义函数, 该函数会包含局部函数
def get_math_func(type, nn) :
    #定义一个计算平方的局部函数
    def square(n) :
        return n * n
    #定义一个计算立方的局部函数
    def cube(n) :
        return n * n * n
    #定义一个计算阶乘的局部函数
    def factorial(n) :
        result = 1
        for index in range(2, n + 1) :
            result *= index
        return result
    #调用局部函数
    if type == "square" :
        return square(nn)
    elif type == "cube" :
        return cube(nn)
    else :
        return factorial(nn)
print(get_math_func("square", 3))
print(get_math_func("cube", 3))
print(get_math_func("", 3))

def foo() :
    # 局部变量name
    name = 'Charile'
    def bar() :
        nonlocal name
        #访问bar函数所在的name局部变量
        print(name)
        name = '孙悟空'
    bar()
foo()

#nonlocal 的具体含义

def foo() :
    #局部变量name
    name = 'Charile'
    def bar() :
        #访问bar函数所在的foo函数的name局部变量
      # 
        nonlocal name
        print(name)
        name = '孙悟空'
    bar()
foo()









