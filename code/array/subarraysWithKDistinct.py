class Solution:
    def subarraysWithKDistinct(self, A, K: int) -> int:
        n = len(A)
        ans = []
        # 分别测试长度为i的子数组
        for i in range(K, n+1):
            # 从位置j开始遍历
            for j in range(n - i + 1):
                if len(set(A[j:j + i])) > K:
                    continue
                elif len(set(A[j:j + i])) == K:
                    ans.append(A[j:j + i])
        # print(ans)
        return len(ans)


if __name__ == '__main__':
    nums = [2, 1, 2, 1, 2]
    k = 2
    solution = Solution()
    print(solution.subarraysWithKDistinct(nums, k))
