def twoSum(nums, target):
    temp = []
    for i in range(len(nums)):
        if nums[i] in temp:
            return [i, temp.index(nums[i])]
        temp.append(target-nums[i])
    return False


if __name__ == '__main__':
    print(twoSum([2, 7, 11, 15], 9))