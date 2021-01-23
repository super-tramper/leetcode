class Solution:
    def makeConnected(self, n, connections) -> int:
        def dfs(x):
            if visited[x]: return
            visited[x] = 1
            for j in adj[x]:
                dfs(j)
        if len(connections) < n - 1:
            return -1
        adj = [[] for _ in range(n)]
        visited = [0] * n
        for x, y in connections:
            adj[x].append(y)
            adj[y].append(x)
        count = 0
        for i in range(n):
            if visited[i]: continue
            count += 1
            dfs(i)
        return count - 1


if __name__ == '__main__':
    n = 5
    connections = [[0, 1], [0, 2], [3, 4], [2, 3]]
    solution = Solution()
    print(solution.makeConnected(n, connections))