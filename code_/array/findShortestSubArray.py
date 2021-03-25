from typing import List
from collections import defaultdict


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        start, maxf, minl = {}, 1, len(nums)  # minl设置为1，规避数组的度为1的情况
        end, count = defaultdict(int), defaultdict(int)
        for i, v in enumerate(nums):
            if v in start:
                end[v] = i
            else:
                start[v] = i
            count[v] += 1
        for key in start:
            if count[key] > maxf:
                maxf = count[key]
                minl = end[key] - start[key] + 1
            if count[key] == maxf and end[key] - start[key] + 1 < minl:
                minl = end[key] - start[key] + 1
        return minl if maxf > 1 else 1


if __name__ == '__main__':
    nums = [1, 2, 2, 3, 1, 4, 2]
    solution = Solution()
    print(solution.findShortestSubArray(nums))
