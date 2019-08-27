global_fn = lambda p :print('执行lambda表达式, P参数: ', p)
class Category :
    cate_fn = lambda p :print('执行lambda表达式, p参数: ', p)
# 调用全局范围内的global_fn, 为参数p传入参数值
global_fn('fkit')
c = Category()
#调用类命名空间的cate_fn, Python 自动绑定第一个参数
c.cate_fn()

class Adress :
    detail = '广州'
    post_code = '510660'
    def info (self) :
        #尝试直接访问类变量
        #print(detail) #报错
        #通过类来访问类变量
        print(Adress.detail)
        print(Adress.post_code)
#通过类来访问Adress类的类变量
print(Adress.detail)
addr = Adress()
addr.info()
#修改Adress类的类变量
Adress.detail = '佛山'
Adress.post_code = '460110'
addr.info()

class Record :
    #定义两个类变量
    item = '鼠标'
    data = '2016-06-16'
    def iofo (self) :
        print('info方法中: ', self.item)
        print('info方法中: ', self.data)

re = Record()
print(re.item)
print(re.data)
re.iofo()

#修改Record类的两个类变量
Record.item = '键盘'
Record.data = '2016-06-16'
#调用info()方法
re.iofo()


'modifify'

class Inventory :
    #定义两个类变量
    item = '鼠标'
    quantity = 2000
    #定义实例方法
    def change(self, item, quantity) :
        #下面赋值语句不是对类变量赋值, 而是定义新的实例变量
        self.item = item 
        self.quantity = quantity
#创建Inventory()
iv = Inventory()
iv.change('显示器', 500)
#访问iv的item和quantity类变量
print(iv.item)  #显示器
print(iv.quantity) #500
#访问Inventory的item和quantity类变量
print(Inventory.item)
print(Inventory.quantity)


Inventory.item = '类变量实例item'
Inventory.quantity = '类变量quantity'
#访问iv的item和quantity实例变量
print(iv.item)
print(iv.quantity)

iv.item = '实例变量item'
iv.quantity = '实例变量quantity'
print(Inventory.item)
print(Inventory.quantity)

class Rectangle :
    #定义构造方法
    def __init__(self, width, height):
        self.width = width
        self.height = height
    #定义setsize()函数
    def setsize(self, size) :
        self.width, self.height = size
    #定义getsize()函数
    def getsize(self) :
        return self.width, self.height
    #定义delsize()函数
    def delsize(self) :
        self.width, self.height = 0, 0
    #使用property定义属性
    size = property(getsize, setsize, delsize, '用于描述矩形大小的属性')
#访问size属性的说明文档
print(Rectangle.size.__doc__)
#通过内置的help()函数查看Rectangle.size的说明文档
help(Rectangle.size)
rect = Rectangle(4, 3)
#访问rect的size属性
print(rect.size)
#对rect的size属性赋值
rect.size = 9, 7
#访问rect的width,heght实例变量
print(rect.width)
print(rect.height)
#删除rect的size属性
del rect.size
#访问rect的width, height实例变量
print(rect.width)
print(rect.height)
print(dir(Rectangle))










