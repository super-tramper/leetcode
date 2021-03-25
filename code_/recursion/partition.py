"""
131. 分割回文串
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
返回 s 所有可能的分割方案。
输入: "aab"
输出:
[
  ["aa","b"],
  ["a","a","b"]
]
"""
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if len(s) == 0:
            return [[]]
        if len(s) == 1:
            return [[s]]
        ans = []
        for i in range(1, len(s)+1):
            left = s[:i]
            right = s[i:]
            if left == left[::-1]:
                right = self.partition(right)
                for j in range(len(right)):
                    ans.append([left] + right[j])
        return ans


if __name__ == '__main__':
    s = "aab"
    solution = Solution()
    print(solution.partition(s))