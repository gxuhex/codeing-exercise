class Cat :
    def __init__ (self, name) :
        self.name = name
def walk_func(self) :
    print('%s慢慢的走过一片草地' % self.name)
d1 = Cat('Garfriend')
d2 = Cat('Kitty')
#d1.walk()#
#为Cat动态绑定walk()方法,该方法的第一个参数会自动绑定
Cat.walk = walk_func
#d1，d2调用walk方法
d1.walk()
d2.walk()


#定义ItemMetaClass, 继承type
class ItemMetaClass(type):
    #cls代表动态修改的类
    #name代表动态修改的类名
    #bases代表被动态修改类的所有父类
    #attr代表被动态修改的类的所有属性， 方法组成的字典
    def __new__(cls, name, bases, attrs) :
        #动态为该方法添加一个cal_price方法
        attrs['cal_price'] = lambda self : self.price * self.discount
        return type.__new__(cls, name, bases, attrs)
#定义book类
class Book(metaclass = ItemMetaClass):
    __slots__ = ('name', 'price', '_discount')
    def __init__(self, name, price) :
        self.name = name
        self.price = price 
    @property
    def discount(self) :
        return self._discount
    @discount.setter
    def discount(self, discount) :
        self._discount = discount
#定义Book类
class CellPhone(metaclass = ItemMetaClass):
    __slots__ = ('price', '_discount')
    def __init__(self, price) :
        self.price = price
    @property
    def discount(self) :
        return self._discount
    @discount.setter
    def discount(self, discount) :
        self._discount = discount

b = Book("疯狂Python讲义", 85)
b.discount = 0.76
#创建Book对象的cal_price()方法
print(b.cal_price())
cp = CellPhone(2399)
cp.discount = 0.85
#创建CellPhone对象的cal_price()方法
print(cp.cal_price())

#上述依旧存在问题

#这个meteclass是基础框架中应用较多的一个方法，是为了动态修改一批类的属性说设置的，继承于type






