class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        # 起始时头指针和尾指针都指向字符串的第一个元素
        differs = [abs(ord(s[0]) - ord(t[0]))]
        sumn, head = differs[0], 0
        maxl = 1 if sumn <= maxCost else 0

        # 不断向后移动尾指针
        for tail in range(1, len(s)):
            # 记录当前尾指针位置的字符差值
            differs.append(abs(ord(s[tail]) - ord(t[tail])))
            sumn += differs[tail]

            # 若当前区间内字符总差值大于maxCost，则向后移动头指针，并更新总差值
            while sumn > maxCost and head <= tail:
                sumn -= differs[head]
                head += 1
            # 若此时字符差值总和小于maxCost，更新maxl
            if sumn <= maxCost:
                maxl = max(maxl, tail - head + 1)
        return maxl


if __name__ == '__main__':
    s = "abcd"
    t = "acde"
    cost = 0
    solution = Solution()
    print(solution.equalSubstring(s, t, cost))
