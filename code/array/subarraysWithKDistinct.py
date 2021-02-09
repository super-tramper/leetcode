class Solution:
    def subarraysWithKDistinct(self, A, K: int) -> int:
        return self.atMostwithKDistinct(A, K) - self.atMostwithKDistinct(A, K - 1)

    def atMostwithKDistinct(self, A, K):
        l, r = 0, 0
        n, ans = len(A), 0
        freq = [0] * (n + 1)
        count = 0
        while r < n:
            if freq[A[r]] == 0:
                count += 1
            freq[A[r]] += 1
            r += 1

            while count > K:
                freq[A[l]] -= 1
                if freq[A[l]] == 0:
                    count -= 1
                l += 1

            ans += r - l
        return ans


if __name__ == '__main__':
    nums = [2, 1, 2, 1, 2]
    k = 2
    solution = Solution()
    print(solution.subarraysWithKDistinct(nums, k))
