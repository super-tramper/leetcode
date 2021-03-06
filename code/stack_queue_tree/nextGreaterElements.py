"""
给定一个循环数组（最后一个元素的下一个元素是数组的第一个元素），输出每个元素的下一个更大元素。
数字 x 的下一个更大的元素是按数组遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。
如果不存在，则输出 -1。
"""
# 1.依次将数组下标入栈，若当前元素比栈顶元素大，则弹出栈顶元素，并将弹出元素对应的ans位置标记为当前元素；
# 2.将数组复制一遍，解决循环的问题，以空间换时间（避免取余操作）；
# 3.利用python数组可以很方便地完成栈操作。
from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack, n = [], len(nums)
        ans = [-1] * n
        nums.extend(nums)
        for i in range(2 * n - 1):
            while stack and nums[stack[-1]] < nums[i]:
                ans[stack.pop() % n] = nums[i]
            stack.append(i)
        return ans


if __name__ == '__main__':
    nums = [1, 2, 1]
    solution = Solution()
    print(solution.nextGreaterElements(nums))
