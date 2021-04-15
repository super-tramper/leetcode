"""
你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。

给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，能够偷窃到的最高金额。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/house-robber-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
输入：nums = [2,3,2]
输出：3
解释：你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        def robRange(start:int, end:int) -> int:
            first = nums[start]
            second = max(nums[start], nums[start+1])
            for i in range(start+2, end +1):
                first, second = second, max(first+nums[i], second)
            return second
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        return max(robRange(0, len(nums)-2), robRange(1, len(nums)-1))
        

if __name__ == '__main__':
    nums = [2,3,2]
    solution = Solution()
    print(solution.rob(nums))
