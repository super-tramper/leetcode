from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        maxc, cur, const = 0, 0, 0
        p, q = 0, 0
        n = len(customers)
        while q < n:
            if not grumpy[q]:
                const += customers[q]
            if grumpy[q]:
                cur += customers[q]
            while q - p + 1 > X:
                if grumpy[p]:
                    cur -= customers[p]
                p += 1
            maxc = max(maxc, cur)
            q += 1
        return maxc + const


if __name__ == '__main__':
    customers = [1, 0, 1, 2, 1, 1, 7, 5]
    grumpy = [0, 1, 0, 1, 0, 1, 0, 1]
    X = 3
    solution = Solution()
    print(solution.maxSatisfied(customers, grumpy, X))
