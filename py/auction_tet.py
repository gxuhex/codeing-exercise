class AuctionException(Exception):pass
class AuctionTest:
    def __init__(self, init_price):
        self.init_price = init_price
    def bid(self, bid_price) :
        d = 0.0
        try:
            d = float(bid_price)
        except Exception as e:
            #此处简单打印异常信息
            print('转换出异常：', e)
            #再次引发自定义异常
            raise AuctionException("竞拍必须是纯数值，不能包含空格")
            raise AuctionException(e)
        if self.init_price > d:
            raise AuctionException("出价过低")
        initPrice = d
def main():
    at = AuctionTest(20.4)
    try:
        at.bid("df")
    except AuctionException as ae:
         #再次捕获bid()方法中的异常，并进行处理
        print("捕获的异常：", ae)

main()



