from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxl, count = 0, 0
        for i in nums:
            count = (count + 1) if i else 0
            maxl = max(maxl, count)
        return maxl


if __name__ == '__main__':
    nums = [1, 1, 0, 1, 1, 1]
    solution = Solution()
    print(solution.findMaxConsecutiveOnes(nums))
