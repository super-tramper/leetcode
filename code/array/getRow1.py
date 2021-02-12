import math


class Solution:
    def getRow(self, rowIndex: int):
        ans = []
        for i in range(rowIndex+1):
            ans.append(int(math.factorial(rowIndex)/(math.factorial(i)*math.factorial(rowIndex-i))))
        return ans



if __name__ == '__main__':
    rowIndex = 4
    solution = Solution()
    print(solution.getRow(rowIndex))
