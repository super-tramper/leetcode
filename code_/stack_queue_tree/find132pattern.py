"""
给你一个整数数组 nums ，数组中共有 n 个整数。132 模式的子序列 由三个整数 nums[i]、nums[j] 和 nums[k] 组成，并同时满足：i < j < k 和 nums[i] < nums[k] < nums[j] 。
如果 nums 中存在 132 模式的子序列 ，返回 true ；否则，返回 false 。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/132-pattern
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# 时间复杂度O(n),单调栈
from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False

        stack = [nums[-1]]
        max_k = -float("inf")

        for j in range(n-2, -1, -1):
            if nums[j] < max_k:
                return True
            while len(stack) and stack[-1] < nums[j]:
                max_k = stack.pop()  # 此处更新max_k时，不用将原有值与当前值进行比较，因为栈内的值肯定比栈外的大
            if max_k < nums[j]:
                stack.append(nums[j])
        return False


if __name__ == '__main__':
    nums = [3,1,4,2]
    solution = Solution()
    print(solution.find132pattern(nums))