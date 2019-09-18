def square_gen(val) :
    i = 0
    out_val = None
    while True:
        #使用yield语句生成值，使用out_val接受send()方法发送的参数
        out_val = (yield out_val ** 2) if out_val is None else (yield i ** 2)
