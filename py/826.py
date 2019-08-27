'''
def foo() :
    #局部变量name
    name = 'Charile'
    def bar() :
        #访问bar函数所在的foo函数的name局部变量
        print(name)
        name = '孙悟空'
    bar()
foo()


#定义函数类型的形参,其中fn是一个函数
def map(date, fn) :
    result = []
    #遍历data列表中的每个元素,并用fn函数对每个元素进行计算
    #然后将计算结果作为新数组的元素
    for e in date :
        result.append(fn(e))
    return result
#定义一个计算平方的函数
def square(n) :
    return n * n
#定义一个计算立方的函数
def cube(n) :
    return n * n * n
#定义一个计算阶乘的函数
def factorial(n) :
    result = 1
    for e in range(2, n + 1) :
        result *= e
    return result
date = [3, 4, 9, 5, 8]
print("原数据", date)
#下面程序3次调用map()函数, 每次调用时候传入不同的函数
print("计算数组元素的平方")
print(map(date, square))
print("计算数组元素的立方")
print(map(date, cube))
print("计算数组元素的阶乘:")
print(map(date, factorial))
#获取map的类型
print(type(map))

def get_math_func(type) :
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
    #返回局部函数
    if type == "square" :
        return square
    if type == "cube" :
        return cube
    else :
        return factorial
#调用get_math_func(), 程序返回一个嵌套函数
math_func = get_math_func("cube") #得到cube函数
print(math_func(5))
math_func = get_math_func("square")
print(math_func(5))
math_func = get_math_func("")
print(math_func(5))

#定义一个计算乘方的函数
def pow(base, exponent) :
    result = 1
    for i in range(1, exponent + 1) :
        result *= base
    return result
#将pow函数赋值给my_fun, 则my_fun可当成pow使用
my_fun = pow
print(my_fun(3, 4))
#定义一个计算面积的函数
def area(width, height) :
    return width * height
#将area函数赋值给my_fun, 则my_fun可当成area使用
my_fun = area
print(my_fun(3, 4))

'''

#传入计算平方的lambda表达式作为参数
x = map(lambda x :x * x, range(8))
print([e for e in x])

#传入计算平方的lambda表达式作为参数
y = map(lambda x : x * x if x % 2 == 0 else 0, range(8))
print([e for e in y])

def get_math_func(type) :
    result = 1
    #该函数返回的是Lambda表达式
    if type == 'square' :
        return lambda n : n * n 
    elif type == 'cube' :
        return lambda n : n * n * n
    else :
        return lambda n : (1 + n) * n /2
#调用get_math_func(),程序返回一个嵌套函数
math_func = get_math_func("cube")
print(get_math_func(5))
math_func = get_math_func("square")
print(math_func(5))
math_func = get_math_func("")
print(math_func(5))

a = lambda x, y: x + y
def add(x, y): return x + y 
print(a(1, 2))

class Dog :
    #定义一个jump()方法
    def jump(self):
        print("正在执行jump方法")
    #定义一个run()方法,run()方法要借助jump()方法
    def run(self) :
        #使用self参数引用调用run()方法的对象
        self.jump()
        print("正在执行run方法")

d = Dog()
d.run()

class Person :
    '这是一个学习python定义的一个person类'
    #下面定义了一个类变量
    hair = 'black'
    def __init__(self, name = 'Charile', age = 8) :
        #下面为Person对象增加2个实例变量
        self.name = name 
        self.age = age
    #下面定义了一个say方法
    def say(self, content) :
        print(content)
help(Person)
#调用Person类的构造方法,返回一个Person对象
#将该Person对象赋给p变量
p = Person()
#输出p的name, age实例变量
print(p.name, p.age)
#访问p的name实例变量,直接为该实例变量赋值
p.name = '李刚'
#调用p的say方法,声明say()方法时定义了2个形参
#当时候第一个形参(self)是自动绑定的,因此调用该方法只需为第二个形参赋一个值
p.say('py很简单,学起来最烦')
#再次输出p的name, age实例变量
print(p.name, p.age)

#为对象增加一个skill实例变量
p.skills = ['programming', 'swimming']
print(p.skills)
#删除p对象的name实例变量
del p.name
#再次访问p的name实例变量
#print(p.name)

#先定义一个函数
def info(self) :
    print("---info函数---", self)
#使用info对p的foo方法赋值(动态绑定方法)
p.foo = info
#py不会自动将调用者绑定到第一个参数,
#因此程序需要手动将调用者绑定为第一个参数
p.foo(p)

def intro_func(self, content) :
    print("我是一个人,信息为 : %s" % content)
#导入methodtype
from types import MethodType
#使用MethType对intro_func进行包装,将该函数的第一个参数进行绑定
p.intro = MethodType(intro_func, p)
#第一个参数已经绑定,无需传入
p.intro("生活在别处")

class ReturnSelf :
    def grow(self) :
        if hasattr(self, 'age') :
            self.age += 1
        else :
            self.age = 1
        #return self返回调用该方法的对象
        return self
rs = ReturnSelf()
#可以连续调用同一个方法
rs.grow().grow().grow()
print("rs的age属性值是:", rs.age)

class InConstructor :
    def __init__(self) :
        #在构造方法里定义一个foo变量(局部变量)
        foo = 0
        #使用self代表该构造方法正在初始化的对象
        #使用下面的代码会把该构造方法的对象的foo实例变量设为6
        self.foo = 6
#所有使用In创建的对象的foo实例变量都将被设为6
print(InConstructor().foo)   #6


class User:
    def test(self) :
        print('self参数: ', self)

u = User()
#以方法形式调用test()方法
u.test()
#将User对象的test方法赋值给test()方法.
foo = u.test
#把方法赋值给变量有什么用

#通过foo变量(函数形式)调用test()方法
foo()  

#因为上面把对象的方法赋给了这个变量,所以这里可以使用这个方法是同一个

'6.2'

def auth(fn) :
    def auth_fn(*args) :
        #用一条语句模拟执行权限检查
        print("------模拟执行权限检查------")
        #回调要修饰的目标函数
        fn(*args)
    return auth_fn
@auth
def  test(a, b) :
    print("执行test函数,参数a: %s ,参数b: %s" % (a, b))
#调用test()函数,其实是调用装饰之后返回的auth_fn函数
test(20, 16)


class User :
    def walk (self) :
        print(self, '正在慢慢的走')
#通过类调用这类实例方法
#User.walk()
u = User()
#显示未方法的第一个参数绑定参数值
User.walk(u)

#显示为方法的第一个参数绑定fkit字符串参数值
User.walk('fkit')

#定义全局空间的foo函数
def foo() :
    print("全局空间的foo方法")
#全局空间的bar变量
bar = 20
class Bird :
    #定义Bird空间的foo函数
    def foo() :
        print("Bord空间的foo方法")
        #定义Bird空间的bar变量
    bar = 200
foo()
print(bar)
#调用Bird空间的函数和变量
Bird.foo()
print(Bird.bar)

class Bird :
    #classmethod修饰的是类方法
    @classmethod
    def fly(cls) :
        print('类方法fly: ', cls)
    #staticmethod修饰的是静态方法
    @staticmethod
    def info(p) :
        print('静态方法info : ', p)
#调用类方法,Bird类会自动绑定到第一个参数
Bird.fly()
#调用静态方法,不会自动绑定,因此程序必须手动绑定第一个参数
Bird.info('crazyit')
#创建Bird对象
b = Bird()
#使用对象调用fly()类方法,其实依然还是使用类方法
#因此第一个参数依旧被自动绑定到Bird类
b.fly()
#使用对象调用info()静态方法, 其实依然还是使用类调用
#因此程序必须为第一个参数执行绑定
b. info('fkit')

def funA(fn) :
    print('A')
    fn()  #执行传入的fn参数
    return 'fkit'

'''
下面的修饰效果相当于: funA(funB),
funB将会替换(装饰)成该语句的返回值:
由于funA()函数返回fkit,因此funB就是fkit
'''
@funA
def funB():
    print('B')
print(funB)

@funA
def funB() :
    print('B')
print(funB)   #fkit

def foo(fn) :
    #定义一个嵌套函数
    def bar(*args) :
        print("===1===", args)
        n = args[0]
        print('===2===', n * (n - 1))
        #查看传给foo函数的fn函数
        print(fn.__name__)
        fn(n * (n - 1))
        print(" * " * 16)
        return fn(n * (n - 1))
    return bar

'''
下面的装饰效果相关于: foo(my_test),
my_test将会替换(装饰)成该语句的返回值
由于foo()函数返回bar函数,因此funB就是bar
'''
@foo
def my_test(a) :
    print("===my_test函数===", a)
#打印my_test函数,将看到实际上是bar函数
print(my_test)
#下面代码看上去是调用my_test()函数, 其实是调用bar()函数
my_test(10)
my_test(6, 5)

class Item :
    #  直接在类空间放置执行性质代码
    print('正在定义Item类')
    for a in range(10) :
        if a % 2 == 0 :
            print('这个是偶数: ', a)
        else :
            print('这个是奇数: ', a)

















