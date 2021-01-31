class Solution:
    def maxNumEdgesToRemove(self, n: int, edges) -> int:
        def dfs(v, adj):
            visited.add(v)
            for i in adj[v]:
                if i in visited: continue
                dfs(i, adj)

        adj_alice = [[] for _ in range(n + 1)]
        adj_bob = [[] for _ in range(n + 1)]
        visited = set()
        for x, y, z in edges:
            if x != 1:
                adj_bob[y].append(z)
                adj_bob[z].append(y)
            if x != 2:
                adj_alice[y].append(z)
                adj_alice[z].append(y)
        start = 1
        dfs(start, adj_alice)
        if len(visited) != n:
            return -1
        visited.clear()
        dfs(start, adj_bob)
        if len(visited) != n:
            return -1
        adj_common = [[] for _ in range(n + 1)]
        for x, y, z in edges:
            if x == 3:
                adj_common[y].append(z)
                adj_common[z].append(y)
        x = 0
        visited.clear()
        for i in range(1, n + 1):
            if i in visited: continue
            x += 1
            dfs(i, adj_common)
        return len(edges) - (n - 1 + x - 1)


if __name__ == '__main__':
    n = 4
    edges = [[3, 1, 2], [3, 2, 3], [1, 1, 3], [1, 2, 4], [1, 1, 2], [2, 3, 4]]
    solution = Solution()
    print(solution.maxNumEdgesToRemove(n, edges))
