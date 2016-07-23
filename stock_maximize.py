def main():
    T = input()
    stock_arr = [0]*T
    for i in xrange(T):
        N = map(int, raw_input().strip().split())
        stock_arr[i] = list(map(int, raw_input().strip().split()))
        print stock_arr
    for stock in stock_arr:
        profit = calprofit(stock)

#li.index("example")
def calprofit(stock):
    stocksorted = sorted(stock)
    print "stock sorted"
    print stocksorted
    print "stock"
    print stock




if __name__ == '__main__':
    main()

