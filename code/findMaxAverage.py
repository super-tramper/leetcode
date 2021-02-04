class Solution:
    def findMaxAverage(self, nums, k: int) -> float:
        maxTotal = total = sum(nums[:k])
        n = len(nums)

        for i in range(k, n):
            total = total - nums[i - k] + nums[i]
            maxTotal = max(maxTotal, total)

        return maxTotal / k


if __name__ == '__main__':
    nums = [3,3,4,3,0]
    k = 3
    solution = Solution()
    print(solution.findMaxAverage(nums, k))
