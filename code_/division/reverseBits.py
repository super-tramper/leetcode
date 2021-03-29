"""
颠倒给定的 32 位无符号整数的二进制位。
"""
"""python整型没有长度限制，故左移后需要去除超出32位的部分，即同M5的与操作"""
class Solution:
    def reverseBits(self, n: int) -> int:
        M1 = 0x55555555  # 01010101010101010101010101010101
        M2 = 0x33333333  # 00110011001100110011001100110011
        M3 = 0x0f0f0f0f  # 00001111000011110000111100001111
        M4 = 0x00ff00ff  # 00000000111111110000000011111111
        M5 = 0xffffffff  # 11111111111111111111111111111111
        n = (n >> 1) & M1 | (n & M1) << 1
        n = (n >> 2) & M2 | (n & M2) << 2
        n = (n >> 4) & M3 | (n & M3) << 4
        n = (n >> 8) & M4 | (n & M4) << 8
        return (n >> 16 | n << 16) & M5


if __name__ == '__main__':
    n =  1610612736
    solution = Solution()
    print(solution.reverseBits(n))