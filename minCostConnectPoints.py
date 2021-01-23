import heapq


class Solution:
    def minCostConnectPoints(self, points) -> int:
        n = len(points)
        if n < 2: return 0
        cost = []
        # 计算cost并建堆
        for i in range(n):
            for j in range(i + 1, n):
                cost.append([abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), i, j])
        heapq.heapify(cost)
        # 从堆顶取最小值，将其代表的变的端点加入结合，直到端点数与给定的points长度相等
        ans = 0
        # kruskal算法用并查集来检验是否形成圈
        parents = list(range(n))
        count = 0
        node_set = set()
        # while len(node_set) < n:
        while count < n-1:
            c, s, t = heapq.heappop(cost)
            if self.findParent(s, parents) != self.findParent(t, parents):
                self.unionNode(s, t, parents)
                count += 1
                ans += c
                # node_set.add(s)
                # node_set.add(t)
        return ans

    def findParent(self, x, parents):
        if x != parents[x]:
            parents[x] = self.findParent(parents[x], parents)
        return parents[x]

    def unionNode(self, x, y, parents):
        parents[self.findParent(y, parents)] = self.findParent(x, parents)


if __name__ == '__main__':
    points = [[2, -3], [-17, -8], [13, 8], [-17, -15]]
    solution = Solution()
    print(solution.minCostConnectPoints(points))
