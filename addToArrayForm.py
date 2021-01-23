class Solution:
    def addToArrayForm(self, A, K):
        return list(map(int, list(str(int(''.join(map(str, A)))+K))))


if __name__ == '__main__':
    A = [1, 2, 0, 0]
    K = 34
    solution = Solution()
    print(solution.addToArrayForm(A, K))