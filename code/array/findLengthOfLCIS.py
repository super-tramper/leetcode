# 674. 最长连续递增序列

class Solution:
    def findLengthOfLCIS(self, nums) -> int:
        ans = 0
        n = len(nums)
        if n < 2:
            return n
        temp = 1
        for i in range(n - 1):
            if nums[i] < nums[i + 1]:
                temp += 1
            else:
                temp = 1
            ans = temp if temp > ans else ans
        return ans


if __name__ == '__main__':
    nums = [1, 3, 5, 4, 7]
    solution = Solution()
    print(solution.findLengthOfLCIS(nums))
