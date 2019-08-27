class Employee :
    def __init__ (self, salary) :
        self.salary = salary
    def work (self) :
        print('普通员工正在写代码,工资是 :', self.salary)
class Customer :
    def __init__ (self, favorite, adress) :
        self.favorite = favorite
        self.adress = adress
    def info (self) :
        print('我是一个顾客,我的爱好是: %s,地址是%s' %(self.favorite,self.adress))
#Manager继承了Employ,CuSTOMER
class Manager(Employee, Customer) :
    #重写父类的构造方法
    def __init__ (self, salary, favorite, adress) :
        print('---Manager的构造方法---')
        #通过super()函数调用父类的构造方法
        super().__init__(salary)
        #使用未绑定方法调用父类的构造方法
        Customer.__init__(self, favorite, adress)
#创建Manager对象
m = Manager(2500, 'IT产品', '广州')
m.work()
m.info()
