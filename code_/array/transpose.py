from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # ans = [[0]*len(matrix) for _ in range(len(matrix[0]))]
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         ans[j][i] = matrix[i][j]
        return list(zip(*matrix))


if __name__ == '__main__':
    matrix = [[1,2,3],[4,5,6]]
    solution = Solution()
    print(solution.transpose(matrix))