from typing import List


def _quickSort(nums: List[int], start: int, end: int) -> List[int]:
    if start >= end:
        return
    low, high = start, end
    pivot = nums[low]
    while low < high:
        while low < high and nums[high] >= pivot:
            high -= 1
        nums[low] = nums[high]
        while low < high and nums[low] < pivot:
            low += 1
        nums[high] = nums[low]
    nums[low] = pivot
    _quickSort(nums, start, low-1)
    _quickSort(nums, low+1, end)
    return nums


def quickSort(nums: List[int]) -> List[int]:
    _quickSort(nums, 0, len(nums)-1)
    return nums

if __name__ == '__main__':
    nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(quickSort(nums))