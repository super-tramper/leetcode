# 300. 最长递增子序列
def lengthOfLIS(nums) -> int:
    n = len(nums)
    if n < 2:
        return n
    ans = [1]
    for i in range(1, n):
        ans.append(max([ans[j] for j in range(i) if nums[i] > nums[j]], default=0) + 1)
    return max(ans)


if __name__ == '__main__':
    nums = [4, 10, 4, 3, 8, 9]
    print(lengthOfLIS(nums))
