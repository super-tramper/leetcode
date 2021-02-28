from typing import List


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        asc, des = True, True
        for i in range(len(A)-1):
            if A[i] < A[i+1]:
                des = False
            if A[i] > A[i+1]:
                asc = False
        return des or asc


if __name__ == '__main__':
    matrix = [6, 5, 4, 4]
    solution = Solution()
    print(solution.isMonotonic(matrix))