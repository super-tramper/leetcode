from typing import List


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        n = len(A[0])
        ans = map(lambda x: (x[n - i - 1] ^ 1 for i in range(n)), A)
        return [list(i) for i in ans]


if __name__ == '__main__':
    nums = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
    solution = Solution()
    print(solution.flipAndInvertImage(nums))
