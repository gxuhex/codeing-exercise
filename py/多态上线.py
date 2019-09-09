class Canvas :
    def draw_pic(self, shape) :
        print('----开始绘图----')
        shape.draw(self)

class Rectangle :
    def draw(self, canvas) :
        print('在%s上绘制矩形' %canvas)
class Triangle :
    def draw(self, canvas) :
        print('在%s上绘制三角形' %canvas)
class Circle :
    def draw(self, canvas) :
        print('在%s上绘制圆形' %canvas)

c = Canvas()
#传入ectangle参数，绘制矩形
c.draw_pic(Rectangle())
#传入T
c.draw_pic(Triangle())
#传入C
c.draw_pic(Circle())
print(hasattr(c, 'draw_pic'))
print(hasattr(c.draw_pic, '__call__'))
print(Circle.__dict__)









