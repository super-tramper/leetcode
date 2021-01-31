class Solution:
    def swimInWater(self, grid) -> int:
        def findParent(x):
            if x != parent[x]:
                parent[x] = findParent(parent[x])
            return parent[x]

        def union(x, y):
            parent[findParent(y)] = findParent(x)

        n = len(grid)
        parent = {(x, y): (x, y) for x in range(n) for y in range(n)}
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        cost_list = [[x, y, grid[x][y]] for x in range(n) for y in range(n)]
        cost_list.sort(key=lambda x: x[2])
        for x, y, c in cost_list:
            for d in directions:
                u, v = x + d[0], y+d[1]
                if 0 <= u < n and 0 <= v <n and grid[u][v] <= c:
                    union((x, y), (u, v))
            root1 = findParent((0, 0))
            root2 = findParent((n-1, n-1))
            if root1 == root2:
                return c


if __name__ == '__main__':
    grid = [[7, 11, 5, 3], [2, 14, 12, 8], [4, 13, 9, 10], [6, 0, 1, 15]]
    solution = Solution()
    print(solution.swimInWater(grid))
