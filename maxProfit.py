import numpy


# 反复阅读题目后，确定买入和卖出各算一笔交易
# 状态转移方程：buy[i][j] = max(buy[i-1][j], sell[i-1][j]-prices[i])
#             sell[i][j] = max(buy[i-1][j-1]+prices[i], sell[i-1][j])
# 边界条件：buy[0][0]设置为-prices[0]，sell[0][0]设置为0，第0其它值行设置为负无穷

def maxProfit(prices, k):
    n = len(prices)
    k = min(k, n // 2)
    if n <= 1:
        return 0
    buy = numpy.zeros((n, k + 1), dtype=float)
    sell = numpy.zeros((n, k + 1), dtype=float)
    buy[0, 0] = -prices[0]
    sell[0, 0] = 0
    for i in range(1, k+1):
        buy[0][i] = -float('inf')
        sell[0][i] = -float('inf')
    for i in range(1, n):
        buy[i][0] = max(buy[i-1][0], sell[i-1][0]-prices[i])
        for j in range(1, k+1):
            buy[i][j] = max(buy[i - 1][j], sell[i - 1][j] - prices[i])
            sell[i][j] = max(buy[i - 1][j - 1] + prices[i], sell[i - 1][j])
    return int(max(sell[n-1]))


if __name__ == '__main__':
    prices = [2, 4, 1]
    print(maxProfit(prices, 2))
