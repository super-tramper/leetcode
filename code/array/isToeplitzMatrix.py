from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        length, hight = len(matrix[0]), len(matrix)
        for i in range(hight - 1):
            for j in range(length - 1):
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False
        return True


if __name__ == '__main__':
    matrix = [[1, 2], [2, 2]]
    solution = Solution()
    print(solution.isToeplitzMatrix(matrix))
