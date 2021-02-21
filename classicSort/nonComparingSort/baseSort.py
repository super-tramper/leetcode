from typing import List
import math


def baseSort(nums: List[int]) -> List[int]:
    mod, dev = 10, 1
    i, k = 0, math.log10(max(nums))
    while i < k:
        container = [[] for _ in range(10)]
        for num in nums:
            container[num % mod // dev].append(num)
        nums.clear()
        for c in container:
            nums.extend(c)
        i += 1
        mod *= 10
        dev *= 10
    return nums


if __name__ == '__main__':
    nums = [1, 19, 28, 37, 16, 35, 24, 43, 32, 21, 110]
    print(baseSort(nums))
