"""
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。

不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-element
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pre, work = 0, 0
        while work < len(nums):
            if nums[work] != val:
                nums[pre] = nums[work]
                pre += 1
            work += 1
        return pre


if __name__ == '__main__':
    nums = [3,2,2,3]
    val = 3
    solution = Solution()
    print(solution.removeElement(nums, val))
    print(nums)