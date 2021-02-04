# 从中间生成的结果来看，第三次优化后，各组的人数分别为8 5 7 6，再进行4次优化后，各组人数再次变成 8 5 7 6
# 中间有 115 次优化可省略，从开始到最终结果只需5次优化
def optimize(nums, k):
    n = len(nums)
    for i in range(k):
        _, maxInd = getMaxIndex(nums, n)
        print(maxInd)
        print(nums)
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
