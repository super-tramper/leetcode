from typing import List
from collections import deque


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        left, right = 0, 0
        dequeMax, dequeMin = deque(), deque()
        ans = 1
        while right < n:
            while dequeMax and dequeMax[-1] < nums[right]:
                dequeMax.pop()
            while dequeMin and dequeMin[-1] > nums[right]:
                dequeMin.pop()
            dequeMax.append(nums[right])
            dequeMin.append(nums[right])
            while dequeMax and dequeMin and dequeMax[0] - dequeMin[0] > limit:
                if dequeMax and dequeMax[0] == nums[left]:
                    dequeMax.popleft()
                if dequeMin and dequeMin[0] == nums[left]:
                    dequeMin.popleft()
                left += 1
            ans = max(ans, right - left + 1)
            right += 1
        return ans


if __name__ == '__main__':
    nums = [10, 1, 2, 4, 7, 2]
    limit = 5
    solution = Solution()
    print(solution.longestSubarray(nums, limit))
