class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        num = [0] * 26
        begin, end, maxn = 0, 0, 0
        while end < n:
            num[ord(s[end]) - ord('A')] += 1
            maxn = max(maxn, num[ord(s[end]) - ord('A')])
            if end - begin + 1 - k > maxn:
                num[ord(s[begin]) - ord('A')] -= 1
                begin += 1
            end += 1
        return end - begin


if __name__ == '__main__':
    s = "AABABBA"
    k = 1
    solution = Solution()
    print(solution.characterReplacement(s, k))
