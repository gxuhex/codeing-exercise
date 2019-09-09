class SelfException(Exception):pass

def main():
    firstMethond()
def firstMethond():
    secondMethod()
def secondMethod():
    thirdMethod()
def thirdMethod():
    raise SelfException("自定义异常信息")
main()