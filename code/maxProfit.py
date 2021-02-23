def maxProfit_slide(stocks):
    n = len(stocks)
    minPrice = float('inf')
    maxProfit = 0
    for i in range(n):
        if stocks[i] < minPrice:
            minPrice = stocks[i]
        if stocks[i] - minPrice > maxProfit:
            maxProfit = stocks[i] - minPrice
    return maxProfit


def maxProfit_dp(stocks):
    n = len(stocks)
    buy = -stocks[0]  # 第一天买入之后账户余额
    sell = 0  # 第一天买入再卖出后账户余额
    for i in range(n):
        buy = max(buy, -stocks[i])  # 前i天内发生买入，账户余额的最大值
        sell = max(sell, buy + stocks[i])  # 前i天内进行买入后卖出，账户余额的最大值（实际）
    return sell


def maxProfit_brutal(stocks):
    maxProfit = 0
    for bi, bv in enumerate(stocks):
        for si, sv in enumerate(stocks):
            if bi < si:
                maxProfit = max(maxProfit, sv - bv)
    return maxProfit


if __name__ == '__main__':
    stocks = [3, 1, 2, 5, 7, 1, 6]
    print(maxProfit_brutal(stocks))
    print(maxProfit_slide(stocks))
    print(maxProfit_dp(stocks))