from typing import List


class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        n = len(A)
        ans = 0
        for i in range(n-K+1):
            if not A[i]:
                self.swap(A, i, K)
                ans += 1
        return ans if len(set(A[-K:])) == 1 else -1

    def swap(self, A, start, K):
        for i in range(K):
            A[start+i] = 0 if A[start+i] else 1


if __name__ == '__main__':
    ar = [1,1,0]
    k = 2
    solution = Solution()
    print(solution.minKBitFlips(ar, k))