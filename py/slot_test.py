class Dog :
    #__slot__和__slots__是有区别的，具有限制功能的是slots
    __slots__ = ('walk', 'age', 'name')
    def __init__(self, name) :
        self.name = name
    def test() :
        print('预先定义的test方法')
d = Dog('Snoopy')
from types import MethodType
#只允许动态为实例添加walk, age, name这三个属性
#这个MethodType的用法很有意思
d.walk = MethodType(lambda self: print('%s正在慢慢走' %self.name), d)
d.age = 5
d.walk()
#d.foo = 30
#print(d.foo)
#__slots__属性不限制通过类来动态添加方法
Dog.bar = lambda self:print('abc')
d.bar()

class GunDog(Dog) :
    def __init__(self, name) :
        super().__init__(name)
    pass
gd = GunDog('Puppy')
#完全可以为Gundog实例动态添加属性
#__slots__只限制当前，对其派生的类将不再限制
gd.speed = 99
print(gd.speed)

