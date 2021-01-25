class Solution:
    def regionsBySlashes(self, grid) -> int:
        def findParent(x):
            if x != parent[x]:
                parent[x] = findParent(parent[x])
            return parent[x]

        def unionPiece(x, y):
            root1 = findParent(x)
            root2 = findParent(y)
            if x == y:
                return
            parent[root1] = root2

        n = len(grid)
        parent = {(i, j, k): (i, j, k) for i in range(n) for j in range(n) for k in range(4)}
        for i in range(n):
            for j in range(n):
                print(grid[i][j])
                if grid[i][j] == "\\":
                    # print(findParent((i, 3)))
                    unionPiece((i, j, 0), (i, j, 3))
                    unionPiece((i, j, 1), (i, j, 2))
                elif grid[i][j] == "/":
                    unionPiece((i, j, 0), (i, j, 1))
                    unionPiece((i, j, 2), (i, j, 3))
                else:
                    unionPiece((i, j, 0), (i, j, 1))
                    unionPiece((i, j, 1), (i, j, 2))
                    unionPiece((i, j, 2), (i, j, 3))
                if j < n - 1:
                    # 将左边的2号块和右边的0号块合并
                    unionPiece((i, j, 2), (i, j + 1, 0))
                if i < n - 1:
                    # 将上边的3号块和下边的1号块合并
                    unionPiece((i, j, 3), (i + 1, j, 1))
        ans = 0
        for i in parent:
            if i == parent[i]:
                ans += 1
        return ans


if __name__ == '__main__':
    grid = [
        "\\/",
        "/\\"
    ]
    solution = Solution()
    print(solution.regionsBySlashes(grid))
