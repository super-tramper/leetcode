from typing import List


def insertSort(nums: List[int]) -> List[int]:
    for i in range(1, len(nums)):
        temp, pre = nums[i], i-1
        while temp < nums[pre] and pre >= 0:
            nums[pre+1] = nums[pre]
            pre -= 1
        nums[pre+1] = temp
    return nums


if __name__ == '__main__':
    nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(insertSort(nums))
