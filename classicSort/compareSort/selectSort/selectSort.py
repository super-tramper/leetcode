from typing import List


def selectSort(nums: List[int]) -> List[int]:
    for i in range(len(nums)):
        minindex = i
        for j in range(i, len(nums)):
            if nums[j] < nums[minindex]:
                minindex = j
            nums[i], nums[minindex] = nums[minindex], nums[i]
    return nums


if __name__ == '__main__':
    nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(selectSort(nums))
