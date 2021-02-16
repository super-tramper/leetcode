from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[::2])


if __name__ == '__main__':
    nums = [6,2,6,5,1,2]
    solution = Solution()
    print(solution.arrayPairSum(nums))