class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges):
        value, ans = 0, [list(), list()]
        m = len(edges)
        for i, edge in enumerate(edges):
            edge.append(i)
        edges.sort(key=lambda x: x[2])
        uf = UnionFind(n)
        for i in range(m):
            if uf.unionNodes(edges[i][0], edges[i][1]):
                value += edges[i][2]
        for i in range(m):
            ufr = UnionFind(n)
            v = 0
            for j in range(m):
                if j == i: continue
                if ufr.unionNodes(edges[j][0], edges[j][1]):
                    v += edges[j][2]
            if ufr.setNum != 1 or (ufr.setNum == 1 and v > value):
                ans[0].append(edges[i][3])
                continue
            ufp = UnionFind(n)
            v = edges[i][2]
            ufp.unionNodes(edges[i][0], edges[i][1])
            for j in range(m):
                if j != i and ufp.unionNodes(edges[j][0], edges[j][1]):
                    v += edges[j][2]
            if v == value and ufp.setNum == 1:
                ans[1].append(edges[i][3])
        return ans


class UnionFind(object):
    def __init__(self, n):
        self.parents = list(range(n))
        self.setNum = n
        self.setSize = [1] * n

    def unionNodes(self, x, y):
        px, py = self.findParent(x), self.findParent(y)
        if px == py:
            return False
        if self.setSize[px] < self.setSize[py]:
            px, py = py, px
        self.parents[py] = px
        self.setSize[px] += self.setSize[py]
        self.setNum -= 1
        return True

    def findParent(self, x):
        while x != self.parents[x]:
            x = self.findParent(self.parents[x])
        return self.parents[x]


if __name__ == '__main__':
    n = 4
    edges = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [0, 3, 1]]
    solution = Solution()
    print(solution.findCriticalAndPseudoCriticalEdges(n, edges))
