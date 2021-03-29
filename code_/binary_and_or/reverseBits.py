"""
颠倒给定的 32 位无符号整数的二进制位。
"""
class Solution:
    def reverseBits(self, n: int) -> int:
        ans = '%0.32d' % int(bin(n)[2:])
        return int(ans[::-1], 2)


if __name__ == '__main__':
    n =  6
    solution = Solution()
    print(solution.reverseBits(n))