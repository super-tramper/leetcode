class DisjointSetUnion:
    def __init__(self):
        self.f = dict()
        self.rank = dict()

    def find(self, x: int) -> int:
        if x not in self.f:
            self.f[x] = x
            self.rank[x] = 1
            return x
        if self.f[x] == x:
            return x
        self.f[x] = self.find(self.f[x])
        return self.f[x]

    def unionSet(self, x: int, y: int):
        fx, fy = self.find(x), self.find(y)
        if fx == fy:
            return
        if self.rank[fx] < self.rank[fy]:
            fx, fy = fy, fx
        self.rank[fx] += self.rank[fy]
        self.f[fy] = fx

    def numberOfConnectedComponent(self) -> int:
        return sum(1 for x, fa in self.f.items() if x == fa)


class Solution:
    def removeStones(self, stones) -> int:
        dsu = DisjointSetUnion()
        for x, y in stones:
            dsu.unionSet(x, y + 10001)
        return len(stones) - dsu.numberOfConnectedComponent()
