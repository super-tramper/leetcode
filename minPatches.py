def minPatches(nums, n):
    index = 0
    x = 1
    patches = 0
    while x <= n:
        if index < len(nums) and nums[index] <= x:
            x += nums[index]
            index += 1
        else:
            x *= 2
            patches += 1
    return patches


if __name__ == '__main__':
    print(minPatches([1, 2, 2], 5))
