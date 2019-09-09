def test():
    try:
        #由于finall块中包含return语句
        #所以下面的return失效
        return True
    finally:
        return False
a = test()
print(a)