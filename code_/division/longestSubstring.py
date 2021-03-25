class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if not s:
            return 0
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)


if __name__ == '__main__':
    s = "ababacb"
    k = 3
    solution = Solution()
    print(solution.longestSubstring(s, k))
