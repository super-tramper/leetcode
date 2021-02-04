class Solution:
    def findMaxAverage(self, nums, k: int) -> float:
        n, sumn, maxn = len(nums), [nums[0]], -float('inf')
        if n == 1:
            return nums[0]
        for i in range(1, n):
            sumn.append(sumn[i - 1] + nums[i])
            if i == k - 1:
                maxn = max(maxn, sumn[i])
            elif i >= k:
                maxn = max(maxn, sumn[i] - sumn[i - k])
        return maxn/k


if __name__ == '__main__':
    nums = [3,3,4,3,0]
    k = 3
    solution = Solution()
    print(solution.findMaxAverage(nums, k))
