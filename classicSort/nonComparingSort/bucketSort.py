from typing import List
from classicSort.comparingSort.selectSort.heapSort import heapSort


def bucketSort(nums: List[int]) -> List[int]:
    low, high = min(nums), max(nums)
    buckets = [[] for _ in range((high-low)//10+1)]
    for i in nums:
        buckets[(i-low)//10].append(i)
    ret = []
    for bucket in buckets:
        ret.extend(heapSort(bucket))
    return ret


if __name__ == '__main__':
    nums = [90, 80, 70, 6, 5, 4, 3, 2, 1, 100]
    print(bucketSort(nums))