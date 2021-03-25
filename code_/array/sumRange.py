from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        if len(nums) == 0:
            return
        self.sums = [nums[0]]
        for i in range(1, len(nums)):
            self.sums.append(self.sums[i-1] + self.nums[i])

    def sumRange(self, i: int, j: int) -> int:
        return self.sums[j] - self.sums[i] + self.nums[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

if __name__ == '__main__':
    nums = [-2, 0, 3, -5, 2, -1]
    solution = NumArray(nums)
    for i, j in [[0, 2], [2, 5], [0, 5]]:
        print(solution.sumRange(i, j))