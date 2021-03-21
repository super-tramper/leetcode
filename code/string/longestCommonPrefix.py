"""
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) <= 1:
            return len(strs[0])
        ans = 0
        for i, v in enumerate(strs[0]):
            if i >= len(strs[1]) or v != strs[1][i]:
                break
            ans += 1
        for item in strs[2:]:
            k, l = 0, len(item)
            while k + 1 <= min(ans, l) and item[k] == strs[0][k]:
                k += 1
            ans = k
        return strs[0][:ans]
            

if __name__ == '__main__':
    strs = ["flower","flow","flight"]
    solution = Solution()
    print(solution.longestCommonPrefix(strs))