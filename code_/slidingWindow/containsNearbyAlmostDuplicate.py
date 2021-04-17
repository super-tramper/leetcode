"""
给你一个整数数组 nums 和两个整数 k 和 t 。请你判断是否存在 两个不同下标 i 和 j，使得 abs(nums[i] - nums[j]) <= t ，同时又满足 abs(i - j) <= k 。
如果存在则返回 true，不存在返回 false。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/contains-duplicate-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from sortedcontainers import SortedList
import bisect
from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        window = SortedList()
        for i in range(len(nums)):
            if i > k:
                window.remove(nums[i-1-k])
            window.add(nums[i])
            idx = bisect.bisect_left(window, nums[i])
            if idx > 0 and abs(window[idx]-window[idx-1])<=t:
                return True
            if idx < len(window) - 1 and abs(window[idx]-window[idx+1]) <=t:
                return True
        return False


if __name__ == '__main__':
    nums = [1,5,9,1,5,9]
    k = 2
    t = 3
    solution = Solution()
    print(solution.containsNearbyAlmostDuplicate(nums, k, t))