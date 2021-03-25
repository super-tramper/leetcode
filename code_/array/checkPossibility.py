class Solution:
    def checkPossibility(self, nums) -> bool:
        reverses = 0
        n = len(nums)
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                reverses += 1
                if reverses > 1:
                    return False
                if i > 0 and nums[i-1] > nums[i+1]:
                    nums[i+1] = nums[i]
        return True


if __name__ == '__main__':
    nums = [4,2,1]
    solution = Solution()
    print(solution.checkPossibility(nums))
