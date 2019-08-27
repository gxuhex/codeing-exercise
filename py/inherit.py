class Fruit :
    def info(self) :
        print("我是一个水果!重%g克" % self.weight)

class Food :
    def taste(self) :
        print("不同食物的口感不同")

#定义Apple类, 继承了Fruit和Food类
class Apple(Fruit, Food) :
    pass

#创建Apple对象
a = Apple()
a.weight = 5.6
#调用Apple对象的info()方法
a.info()
#调用Apple对象的taste()方法
a.taste()


class BaseClass :
    def foo(self) :
        print('父类中定义的foo方法')
class SubClass(BaseClass) :
    #重写父类的foo方法
    def foo(self) :
        print('子类中重写父类的foo方法')
    def bar(self) :
        print('执行bar方法')
        #直接执行foo方法,将会调用子类重写的foo()方法
        self.foo()
        #使用类名调用实例方法(未绑定的方法)调用父类被重写的方法
        BaseClass.foo(self)
sc = SubClass()
sc.bar()

class Item :
    def info(self) :
        print("Item中方法:", "这是一个商品")
class Product :
    def info(self) :
        print("Product中方法: ", '这是一个工业产品')
#class Mouse(Item, Product)
class Mouse(Product, Item) :
    pass
m = Mouse()
m.info()

class Bird :
    #Bird类的fly()方法
    def fly(self) :
        print("我在天空里自由自在的飞行...")
class Ostrich(Bird) :
    #重写Bird的fly()方法
    def fly(self) :
        print("我只能在地上奔跑...")

#创建Ostrich对象
os = Ostrich()
#执行Ostrich对象的fly()方法,将输出"地上奔跑"
os.fly()

class Employee :
    def __init__ (self,salary) :
        self.salary = salary
    def work (self) :
        print('普通员工正在写代码,工资是 :',self.salary)
class Customer :
    def __init__ (self, favorite, adress) :
        self.favorite = favorite
        self.adress = adress
    def info (self) :
        print('我是一个顾客,我的爱好是: %s,地址是%s' %(self.favorite, self.adress))
#Mangeager继承了Employee\Customer
#class Manger(mployee, Customer)
class Manger(Customer, Employee) :
    pass
m = Manger('IT产品', '广州')
m.info()

















