# 1 2 5 10
# F(count, value) 用count枚硬币凑出面值为value的方案个数
# 可分解为F(count-1, value-1) + F(count-1, value-2) + F(count-1, value-5) + F(count-1, value-10)
import numpy as np


def combinationCount(n, m):
    coins = [1, 2, 5, 10]
    matrix = np.zeros((n+1, m+1), dtype=int)
    # matrix[m][n] 表示用m枚硬币凑出面值n的组合个数
    for i in range(n):
        matrix[i][0] = 1
    for i in coins:
        matrix[1][i] = 1
    pass
