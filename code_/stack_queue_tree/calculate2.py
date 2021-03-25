"""
给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。
整数除法仅保留整数部分。
"""
class Solution:
    def calculate(self, s: str) -> int:
        s = s.strip()
        first, i = self.lookahead(s, 0)
        stack =[first]
        while i < len(s):
            if s[i].isspace():
                i += 1
                continue
            if s[i] == '+':
                i += 1
                while s[i].isspace():
                    i += 1
                num, i = self.lookahead(s, i)
                stack.append(num)
                continue
            if s[i] == '-':
                i+=1
                while s[i].isspace():
                    i += 1
                num, i = self.lookahead(s, i)
                stack.append(-num)
                continue
            if s[i] == '*':
                i += 1
                while s[i].isspace():
                    i += 1
                num, i = self.lookahead(s, i)
                stack.append(stack.pop()*num)
                continue
            if s[i] == '/':
                i += 1
                while s[i].isspace():
                    i += 1
                num, i = self.lookahead(s, i) 
                dividend = stack.pop()
                if dividend < 0:
                    ret = -dividend//num
                    stack.append(-ret)
                else:
                    stack.append(dividend//num)
                continue
        return sum(stack)

    def lookahead(self, s, i):
        if s[i].isnumeric():
            j = i+1
            while j < len(s) and s[j].isnumeric():
                j += 1
        return (int(s[i:j]), j)



if __name__ == '__main__':
    s = "14-3/2"
    solution = Solution()
    print(solution.calculate(s))