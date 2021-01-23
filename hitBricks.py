class UnionFind(object):
    def __init__(self):
        self.parents = {}
        self.size_of_set = {}

    def union(self, x, y):
        # 合并x,y
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return
        self.parents[root_y] = root_x
        # 更新集合大小字典
        self.size_of_set[root_x] += self.size_of_set[root_y]
        self.size_of_set.pop(root_y)

    def find(self, x):
        while x != self.parents[x]:
            x = self.parents[x]
        return x

    def is_connected(self, x, y):
        if x in self.parents and y in self.parents:
            return self.find(x) == self.find(y)

    def add(self, x):
        if x not in self.parents:
            self.parents[x] = x
            self.size_of_set[x] = 1

    def status(self):
        print(self.parents)
        print(self.size_of_set)


class Solution:
    def __init__(self):
        self.CEILING = (-1, -1)

    def mergeNeighbors(self, uf, x, y):
        x[0] == y[0] and abs(x[1] - y[1]) == 1 and uf.union(x, y)
        x[1] == y[1] and abs(x[0] - y[0]) == 1 and uf.union(x, y)

    def calcRoofBricks(self, grid, m, n):
        bricks = []
        for i in range(m):
            for j in range(n):
                grid[i][j] and bricks.append((i, j))
        l = len(bricks)
        uf = UnionFind()
        uf.add(self.CEILING)
        for i in range(l):
            uf.add(bricks[i])
        # 合并第一行到顶部到集合中
        for i in range(n):
            grid[0][i] == 1 and uf.union(self.CEILING, (0, i))
        # 合并其它砖块
        for i in range(l - 1):
            for j in range(i, l):
                self.mergeNeighbors(uf, bricks[i], bricks[j])
        return uf  # 去除加入的屋顶元素

    def hitBricks(self, grid, hits):
        ans = []
        m = len(grid)  # 高度
        n = len(grid[0])  # 宽度
        for hit in hits:
            uf1 = self.calcRoofBricks(grid, m, n)
            p1 = uf1.find(self.CEILING)
            before_hit = uf1.size_of_set[p1]
            if uf1.is_connected(tuple(hit), self.CEILING):
                grid[hit[0]][hit[1]] = 0
                uf2 = self.calcRoofBricks(grid, m, n)
                p2 = uf2.find(self.CEILING)
                after_hit = uf2.size_of_set[p2]
                ans.append(before_hit - after_hit - 1)
            else:
                ans.append(0)
        return ans


if __name__ == '__main__':
    grid = [[1, 0, 1], [0, 0, 1]]
    hits = [[1, 0], [0, 0]]
    solution = Solution()
    print(solution.hitBricks(grid, hits))
