# def summaryRanges(nums):
#     ans = []
#     if len(nums) == 0:
#         return ans
#     if len(nums) == 1:
#         ans.append("%d" % nums[0])
#         return ans
#     flag = nums[0]
#     for i in range(1, len(nums)):
#         if nums[i] - nums[i - 1] == 1:
#             continue
#         if nums[i - 1] == flag:
#             ans.append("%d" % flag)
#         else:
#             ans.append("%d->%d" % (flag, nums[i-1]))
#         flag = nums[i]
#     if nums[-1] == flag:
#         ans.append("%d" % flag)
#     else:
#         ans.append("%d->%d" % (flag, nums[-1]))
#     return ans
def summaryRanges(nums):
    ans = []
    n = len(nums)
    flag = 0
    for i in range(n):
        if i + 1 == n or nums[i + 1] != nums[i] + 1:
            ans.append("%d->%d" % (nums[flag], nums[i]) if i != flag else "%d" % nums[i])
            flag = i + 1
    return ans


if __name__ == '__main__':
    nums = [0,1,2,4,5,7]
    print(summaryRanges(nums))
