def longestPalindrome(s: str) -> str:
    def expandString(s, l, r) -> tuple:
        """
        只考虑初始状态下l和r相同或相差1的情况
        :param s:
        :param l:
        :param r:
        :return:
        """

        while (l >= 0 and r <= len(s) - 1):
            if s[l] == s[r]:
                l -= 1
                r += 1
            else:
                break
        return l + 1, r - 1

    k = 0
    ret = ''
    if len(s) == 1:
        return s
    for i in range(len(s) - 1):
        l1, r1 = expandString(s, i, i)
        if r1 - l1 + 1 > k:
            k = r1 - l1 + 1
            ret = s[l1:r1 + 1]
        l2, r2 = expandString(s, i, i + 1)
        if r2 - l2 + 1 > k:
            k = r2 - l2 + 1
            ret = s[l2:r2 + 1]
    return ret


if __name__ == '__main__':
    print(longestPalindrome('abacababa'))
