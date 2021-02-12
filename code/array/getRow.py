class Solution:
    def getRow(self, rowIndex: int):
        ans = [[1]]
        for i in range(1, rowIndex+1):
            ans.append([])
            for j in range(i+1):
                ret1 = ans[i-1][j-1] if j > 0 else 0
                ret2 = ans[i-1][j] if j < i else 0
                ans[i].append(ret1+ret2)
        return ans[-1]


if __name__ == '__main__':
    rowIndex = 4
    solution = Solution()
    print(solution.getRow(rowIndex))
