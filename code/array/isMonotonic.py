from typing import List


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        return sorted(A) == A or sorted(A) == A[::-1]


if __name__ == '__main__':
    matrix = [6, 5, 4, 4]
    solution = Solution()
    print(solution.isMonotonic(matrix))