class Solution:
    def fairCandySwap(self, A, B):
        sum1 = sum(A)
        sum2 = sum(B)
        margin = (sum1 - sum2) // 2
        ans = []
        b = set(B)
        for i in A:
            j = i - margin
            if j in b:
                ans.append(i)
                ans.append(j)
                break
        return ans


if __name__ == '__main__':
    A = [1, 1]
    B = [2, 2]
    solution = Solution()
    print(solution.fairCandySwap(A, B))
