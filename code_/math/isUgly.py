"""
给你一个整数 n ，请你判断 n 是否为 丑数 。如果是，返回 true ；否则，返回 false 。
丑数 就是只包含质因数 2、3 和/或 5 的正整数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ugly-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0:
            return False
        factors = [2, 3, 5]
        for factor in factors:
            while n % factor == 0:
                n = n // factor
        return n == 1


if __name__ == '__main__':
    A = 0
    solution = Solution()
    print(solution.isUgly(A))