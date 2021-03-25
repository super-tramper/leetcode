from collections import defaultdict
import math


class Solution:
    def numEquivDominoPairs(self, dominoes) -> int:
        n = len(dominoes)
        dominoes_dict = defaultdict(int)
        for i in range(n):
            if dominoes[i][0] > dominoes[i][1]:
                dominoes[i][0], dominoes[i][1] = dominoes[i][1], dominoes[i][0]
            dominoes_dict[tuple(dominoes[i])] += 1
        ans = 0
        for i in dominoes_dict:
            if dominoes_dict[i] > 2:
                ans += math.factorial(dominoes_dict[i]) / (2 * math.factorial(dominoes_dict[i] - 2))
            if dominoes_dict[i] == 2:
                ans += 1
        return int(ans)


if __name__ == '__main__':
    dominoes = [[2, 1], [1, 2], [1, 2], [1, 2], [2, 1], [1, 1], [1, 2], [2, 2]]
    solution = Solution()
    print(solution.numEquivDominoPairs(dominoes))
