from typing import List
from collections import defaultdict


class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row)//2
        parents = list(range(n))
        # 将位置相邻的两个元素合并到一个集合中
        for x in range(n):
            self.unionNodes(row[x*2]//2, row[x*2+1]//2, parents)
        # 记录连通分量个数
        count_dict = defaultdict(int)
        ans = 0
        for x in parents:
            p = self.findParent(x, parents)
            count_dict[p] += 1
        for key in count_dict:
            ans += count_dict[key] - 1
        return ans

    def unionNodes(self, x, y, parents):
        px, py = self.findParent(x, parents), self.findParent(y, parents)
        if px != py:
            parents[py] = px

    def findParent(self, x, parents):
        if x != parents[x]:
            parents[x] = self.findParent(parents[x], parents)
        return parents[x]


if __name__ == '__main__':
    row = [3, 2, 0, 1]
    solution = Solution()
    print(solution.minSwapsCouples(row))
