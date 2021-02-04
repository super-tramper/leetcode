def maxProfit(prices):
    buy1, sell1 = -prices[0], 0
    buy2, sell2 = -prices[0], 0
    n = len(prices)
    for i in range(1, n):
        buy1 = max(buy1, -prices[i])
        sell1 = max(sell1, buy1 + prices[i])
        buy2 = max(buy2, sell1 - prices[i])
        sell2 = max(sell2, buy2 + prices[i])
    return sell2


if __name__ == '__main__':
    prices = [1, 2, 3, 4, 5]
    print(maxProfit(prices))
