"""
给你一个整数数组 nums ，数组中共有 n 个整数。132 模式的子序列 由三个整数 nums[i]、nums[j] 和 nums[k] 组成，并同时满足：i < j < k 和 nums[i] < nums[k] < nums[j] 。
如果 nums 中存在 132 模式的子序列 ，返回 true ；否则，返回 false 。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/132-pattern
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
"""时间复杂度O(nlogn)"""
from typing import List
from sortedcollections import SortedList


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False

        left_min = nums[0]
        right_list = SortedList(nums[2:])

        for j in range(1,n-1):
            if left_min < nums[j]:
                index = right_list.bisect_right(left_min)
                if index < len(right_list) and right_list[index] < nums[j]:
                    return True
            left_min = min(left_min, nums[j])
            right_list = SortedList(nums[j+1:])
        return False


if __name__ == '__main__':
    nums = [-1,3,2,0]
    solution = Solution()
    print(solution.find132pattern(nums))