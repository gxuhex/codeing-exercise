class User:
    def __init__ (self, name, passwd):
        self.name = name
        self.passwd = passwd
    def validLogin(self):
        print('验证%s的登录' % self.name)
u = User('crazyit', 'leegang')
#判断u.name是否包含__call__方法，即判断是否可以调用
print(hasattr(u.name, '__call__'))
#判断u.passwd是否包含__call__方法，即判断是否可调用
print(hasattr(u.passwd, '__call__'))
#判断u.validlogin是否包含__call__方法，即判断是否可以调用
print(u.validLogin, '__call__')


#定义Roll类
class Role:
    def __init__(self, name):
        self.name = name
    #定义___call__方法
    def __call__ (self):
        print('执行Role对象')
r = Role('管理员')
#直接调用Rolr对象，就是调用该对象的__call__方法
r()

def foo():
    print('__foo函数__')
#下面示范了2种方式调用foo()函数
foo()
foo.__call__()




