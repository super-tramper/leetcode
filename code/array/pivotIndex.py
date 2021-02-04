# class Solution:
#     def pivotIndex(self, nums) -> int:
#         n = len(nums)
#         p, q = 0, n - 1
#         sum1, sum2 = 0, 0
#         while p < q:
#             if sum1 < sum2:
#                 sum1 += nums[p]
#                 p += 1
#             else:
#                 sum2 += nums[q]
#                 q -= 1
#         if sum1 == sum2:
#             return q
#         return -1
class Solution:
    def pivotIndex(self, nums) -> int:
        l, r = 0, sum(nums)
        for i, num in enumerate(nums):
            if l + num == r - l: return i
            l += num
        return -1


if __name__ == '__main__':
    nums = [1, 7, 3, 6, 5, 6]
    solution = Solution()
    print(solution.pivotIndex(nums))

