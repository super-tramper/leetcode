from typing import List


class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        tail, count = 0, 0
        n, maxl = len(A), 0
        for head in range(n):
            if not A[head]:
                count += 1
                while count > K:
                    if not A[tail]:
                        count -= 1
                    tail += 1
            maxl = max(maxl, head-tail+1)
        return maxl


if __name__ == '__main__':
    A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
    K = 3
    solution = Solution()
    print(solution.longestOnes(A, K))
