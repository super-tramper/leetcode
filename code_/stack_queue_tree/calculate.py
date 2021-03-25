"""
给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。
"""
class Solution:
    def calculate(self, s: str) -> int:
        ans, stack = 0, [1]
        i, sign = 0, 1
        while i < len(s):
            if s[i] == ' ':
                i += 1
                continue
            if s[i] == '+':
                sign = stack[-1]
                i += 1
                continue
            if s[i] == '-':
                sign = -stack[-1]
                i += 1
                continue
            if s[i] == '(':
                stack.append(sign)
                i += 1
                continue
            if s[i] == ')':
                stack.pop()
                i += 1
                continue
            if s[i].isnumeric():
                num, i = self.lookahead(s, i)
                ans += sign*num
        return ans
            
    def lookahead(self, s, i):
        if s[i].isnumeric():
            j = i+1
            while j < len(s) and s[j].isnumeric():
                j += 1
        return (int(s[i:j]), j)


if __name__ == '__main__':
    s = "(1+(4+5+2)-3)+(6+8)"
    solution = Solution()
    print(solution.calculate(s))