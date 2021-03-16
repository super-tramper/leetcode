"""
给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。
"""
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0]*n for _ in range(n)]
        direction = [(0,1), (1,0), (0,-1), (-1,0)]
        d, p, q = 0, 0, 0
        for i in range(n*n):
            matrix[p][q] = i + 1
            x, y = direction[d]
            tp, tq = p + x, q + y
            if tp < 0 or tp > n - 1 or tq < 0 or tq > n-1 or matrix[tp][tq] > 0:
                d = (d+1)%4
                x, y = direction[d]
            p, q = p + x, q + y
        return matrix


if __name__ == '__main__':
    n = 3
    solution = Solution()
    print(solution.generateMatrix(n))