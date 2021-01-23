def lengthOfLongestSubstring(s: str) -> int:
    st = {}
    i, ans = 0, 0
    for j in range(len(s)):
        if s[j] in st:
            i = max(st[s[j]], i)
        ans = max(ans, j - i + 1)
        st[s[j]] = j + 1
    return ans


if __name__ == '__main__':
    print(lengthOfLongestSubstring('abcabcabcabc'))
