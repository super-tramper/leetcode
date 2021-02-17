from typing import List


class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(nums)
        n = len(nums[0]) if m > 0 else 0
        if r * c != m * n: return nums
        for i in nums[1:]:
            nums[0].extend(i)
        return [nums[0][i:i+c] for i in range(0, m*n, c)]


if __name__ == '__main__':
    ar = [[1, 2], [3, 4]]
    r = 2
    c = 4
    solution = Solution()
    print(solution.matrixReshape(ar, r, c))
