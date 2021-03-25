"""
给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。

进阶：

一个直观的解决方案是使用  O(mn) 的额外空间，但这并不是一个好的解决方案。
一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
你能想出一个仅使用常量空间的解决方案吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/set-matrix-zeroes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        cols, rows = [], []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if not matrix[i][j]:
                    cols.append(j)
                    rows.append(i)
        for col in cols:
            for i in range(len(matrix)):
                matrix[i][col] = 0
        for row in rows:
            for i in range(len(matrix[0])):
                matrix[row][i] = 0
        


if __name__ == '__main__':
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    solution = Solution()
    solution.setZeroes(matrix)
    print(matrix)
