from typing import List


class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        def dfs(x, adj, visited):
            if x in visited:
                return
            visited.add(x)
            for i in adj[x]:
                dfs(i, adj, visited)

        n = len(row) // 2
        adj = [[] for i in range(n)]
        for i in range(n):
            adj[row[i * 2] // 2].append(row[i * 2 + 1] // 2)
            adj[row[i * 2 + 1] // 2].append(row[i * 2] // 2)
        ans = 0
        visited = set()
        for x in row:
            if x//2 not in visited:
                dfs(x//2, adj, visited)
                ans += 1
        return n - ans


if __name__ == '__main__':
    row = [0, 2, 1, 3]
    solution = Solution()
    print(solution.minSwapsCouples(row))
