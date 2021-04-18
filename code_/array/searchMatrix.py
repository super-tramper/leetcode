"""
编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-a-2d-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        low, high = 0, m*n - 1
        while low <= high:
            mid = (low+high) // 2
            midrow, midcol = mid // n, mid % n
            if target > matrix[midrow][midcol]:
                low = mid + 1
            elif target < matrix[midrow][midcol]:
                high = mid - 1
            else:
                return True
        return False
            

if __name__ == '__main__':
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    solution = Solution()
    print(solution.searchMatrix(matrix, target))
    