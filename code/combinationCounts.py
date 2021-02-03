# 1 2 5 10
# F(count, value) 用count枚硬币凑出面值为value的方案个数
# 状态转换方程为F(count, value) = F(count-1, value-1) + F(count-1, value-2) + F(count-1, value-5) + F(count-1, value-10)
import numpy as np


def combinationCount(n, m):
    coins = [1, 2, 5, 10]
    matrix = np.zeros((n + 1, m + 1), dtype=int)
    # matrix[m][n] 表示用m枚硬币凑出面值n的组合个数
    # for i in range(n + 1):
    #     matrix[i][0] = 1
    matrix[0][0] = 1
    # for i in coins:
    #     if m > i:
    #         matrix[1][i] = 1
    for v in coins:
        for i in range(1, n+1):
            for j in range(v, m+1):
                matrix[i][j] += matrix[i - 1][j - v]
    # for i in range(2, n + 1):
    #     for j in range(2, m + 1):
    #         for v in coins:
    #             if j >= v:
    #                 matrix[i][j] += matrix[i - 1][j - v]
    print(matrix)
    return matrix[-1][-1]


if __name__ == '__main__':
    print(combinationCount(4, 10))
