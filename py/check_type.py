#定义一个字符串
hello = "Hello";
#"Hello"是str类的实例， 输出Ture
print('"Hello"是否是str类的实例：', isinstance(hello, str))
#"Hello"是object类的子类实例，输出Ture
print('"Hello是否是object类的实例：', isinstance(hello, object))
# “Hello”不是tuple类及其子类的实例
print('"Hello"是否是Tuple类的实例：', isinstance(hello, tuple))
# str不是tup;e类的子类，输出False
print('str是否是tuple类的子类：', issubclass(str, tuple))

data = (20, 'fkit')
print('data是否为列表或者元组：',isinstance(data, (list, tuple)))



