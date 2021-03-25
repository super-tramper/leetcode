from typing import List


class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        n = len(A)
        differs = [0] * (n + 1)
        ans, revCnt = 0, 0
        for i in range(n):
            revCnt ^= differs[i]
            if A[i] == revCnt:
                if i + K > n:
                    return -1
                revCnt ^= 1
                ans += 1
                differs[i + K] ^= 1
        return ans


if __name__ == '__main__':
    ar = [0, 0, 0, 1, 0, 1, 1, 0]
    k = 3
    solution = Solution()
    print(solution.minKBitFlips(ar, k))
