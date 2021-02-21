from typing import List


def countSort(nums: List[int]) -> List[int]:
    low, high = min(nums), max(nums)
    count = [0] * (high - low + 1)
    for num in nums:
        count[num - low] += 1
    return [i + low for i, v in enumerate(count) for _ in range(v)]


if __name__ == '__main__':
    nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 1]
    print(countSort(nums))