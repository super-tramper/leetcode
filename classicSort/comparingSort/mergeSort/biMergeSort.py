from typing import List


def biMergeSort(nums: List[int]) -> List[int]:
    if len(nums) < 2:
        return nums
    return merge(biMergeSort(nums[:len(nums) >> 1]), biMergeSort(nums[len(nums) >> 1:]))


def merge(left: List[int], right: List[int]) -> List[int]:
    ret = []
    left, right = left[::-1], right[::-1]
    while len(left) > 0 and len(right) > 0:
        if left[-1] <= right[-1]:
            ret.append(left.pop())
        else:
            ret.append(right.pop())
    if len(left) > 0:
        ret.extend(left[::-1])
    if len(right) > 0:
        ret.extend(right[::-1])
    return ret


if __name__ == '__main__':
    nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(biMergeSort(nums))
