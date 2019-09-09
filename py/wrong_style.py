import sys
#定义一个字符串列表
my_list = ["Hello", "Python", "Spring"]
#使用异常处理来遍历数组的每个元素
try:
    i = 0
    while True:
        print(my_list[i])
        i += 1
except:
    pass

#上面是使用try来遍历list，推荐使用下面的这种方式来遍历list

i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1