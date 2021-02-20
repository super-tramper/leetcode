from typing import List


def shellSort(nums: List[int]) -> List[int]:
    gap = len(nums) >> 2
    while gap > 0:
        for i in range(gap, len(nums)):
            temp, j = nums[i], i
            while j - gap >= 0 and nums[j - gap] > temp:
                nums[j], j = nums[j - gap], j - gap
            nums[j] = temp
        gap = gap >> 1
    return nums


if __name__ == '__main__':
    nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(shellSort(nums))
