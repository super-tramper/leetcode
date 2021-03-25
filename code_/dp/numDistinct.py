"""
给定一个字符串 s 和一个字符串 t ，计算在 s 的子序列中 t 出现的个数。

字符串的一个 子序列 是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。（例如，"ACE" 是 "ABCDE" 的一个子序列，而 "AEC" 不是）

题目数据保证答案符合 32 位带符号整数范围。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/distinct-subsequences
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

状态转移方程如下
dp[i][j] = dp[i+1][j+1]+dp[i+1][j], s[i]=t[j]
dp[i][j] = dp[i+1][j],              s[i] != t[j]
"""


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)

        if m < n:
            return 0
        # 边界条件，当t[j:]为空字符串时，比为s[i:]的子串
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][n] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] = dp[i + 1][j + 1] + dp[i + 1][j]
                else:
                    dp[i][j] = dp[i + 1][j]
        return dp[0][0]


if __name__ == '__main__':
    s = "rabbbit"
    t = "rabbit"
    solution = Solution()
    print(solution.numDistinct(s, t))
