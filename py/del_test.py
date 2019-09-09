class Item:
    def __init__ (self, name, price):
        self.name = name
        self.price = price
    #定义析构函数
    def __def__ (self):
        print('del删除对象')
#创建一个Item对象
im = Item('鼠标', 29.5)
del im
print('--------------')





    