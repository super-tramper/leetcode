from typing import List
from classicSort.tools import swap


def siftDown(nums, i):
    while i * 2 + 1 < len(nums):
        child = i * 2 + 1
        if i * 2 + 2 < len(nums) and nums[i * 2 + 1] > nums[i * 2 + 2]:
            child = i * 2 + 2
        if nums[i] < nums[child]:
            break
        swap(nums, i, child)
        i = child


def heapify(nums: List[int]):
    n = len(nums)
    for i in reversed(range((n - 1) >> 1)):
        siftDown(nums, i)


def heapSort(nums: List[int]) -> List[int]:
    heapify(nums)
    out = []
    for i in range(len(nums)):
        swap(nums, 0, -1)
        out.append(nums[-1])
        nums.pop()
        siftDown(nums, 0)
    return out


if __name__ == '__main__':
    nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(heapSort(nums))
