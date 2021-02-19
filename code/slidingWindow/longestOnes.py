from typing import List


class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        n, tail = len(A), 0
        for head in range(n):
            if not A[head]:
                K -= 1
            if K < 0:
                if not A[tail]:
                    K += 1
                tail += 1
        return n - tail


if __name__ == '__main__':
    A = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    K = 2
    solution = Solution()
    print(solution.longestOnes(A, K))
