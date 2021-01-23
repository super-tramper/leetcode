class Solution:
    def maximumProduct(self, nums) -> int:
        nums.sort()
        return max(nums[0] * nums[1] * nums[-1], nums[-1] * nums[-2] * nums[-3])


if __name__ == '__main__':
    ar = [3, 2, 1, 4]
    solution = Solution()
    print(solution.maximumProduct(ar))
