def optimize(nums, k):
    n = len(nums)
    for i in range(k):
        _, maxInd = getMaxIndex(nums, n)
        # print(maxInd)
        # print(nums)
        for j in range(n):
            nums[j] = nums[j] - 3 if j == maxInd else nums[j] + 1
    return nums


def getMaxIndex(nums, n):
    maxn = max(nums)
    return maxn, nums.index(maxn)


if __name__ == '__main__':
    nums = [10, 7, 5, 4]
    optimize(nums, 120)
    print(nums)
