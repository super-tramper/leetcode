class Solution:
    def prefixesDivBy5(self, A):
        pre = 0
        ans = []
        for i in A:
            pre = ((pre << 1) + i) % 5
            ans.append(not pre)
        return ans


if __name__ == '__main__':
    A = [0,1,1]
    solution = Solution()
    print(solution.prefixesDivBy5(A))