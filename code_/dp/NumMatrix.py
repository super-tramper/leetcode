from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.matrixSum = matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                temp1 = self.matrixSum[i - 1][j] if i - 1 >= 0 else 0
                temp2 = self.matrixSum[i][j - 1] if j - 1 >= 0 else 0
                temp3 = self.matrixSum[i - 1][j - 1] if j - 1 >= 0 and i - 1 >= 0 else 0
                self.matrixSum[i][j] = self.matrix[i][j] + temp1 + temp2 - temp3

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if col2 < 0 or row2 < 0:
            return 0
        if row1 == 0 and col1 == 0:
            return self.matrixSum[row2][col2]
        return self.sumRegion(0, 0, row2, col2) - self.sumRegion(0, 0, row2, col1 - 1) - \
               self.sumRegion(0, 0, row1 - 1, col2) + self.sumRegion(0, 0, row1 - 1, col1 - 1)


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
if __name__ == '__main__':
    matrix = [
        # [3, 0, 1, 4, 2],
        # [5, 6, 3, 2, 1],
        # [1, 2, 0, 1, 5],
        # [4, 1, 0, 1, 7],
        # [1, 0, 3, 0, 5]
        [-4, -5]
    ]
    nummatrix = NumMatrix(matrix)
    print(nummatrix.sumRegion(0, 1, 0, 1))

