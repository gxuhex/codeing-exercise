#导入traceback模块
import traceback
class SelfException(Exception):pass

def main():
    firstMethod()
def firstMethod():
    secondMethod()
def secondMethod():
    thirdMethod()
def thirdMethod():
    raise SelfException("自定义错误信息")
try:
    main()
except:
    #捕捉异常，将异常传播到控制台
    traceback.print_exc()
    #捕捉异常，并将异常传播到指定文件中
    traceback.print_exc(file=open('log.txt', 'a'))