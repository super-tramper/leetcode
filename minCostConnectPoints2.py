class Solution:
    def minCostConnectPoints(self, points) -> int:
        n, ans = len(points), 0
        dist = [float('inf')] * n
        cur = 0
        seen = set()
        # 需加入n-1条边
        for i in range(n-1):
            x, y = points[cur]
            seen.add(cur)
            for j, (nx, ny) in enumerate(points):
                if j in seen: continue
                # 更新剩余节点到树上点的最小距离
                dist[j] = min(dist[j], abs(nx-x)+abs(ny-y))
            # 从剩余节点中选取距树上节点距离最小的点
            s, cur = min((d, k) for k, d in enumerate(dist))
            ans += s
            dist[cur] = float('inf')
        return ans


if __name__ == '__main__':
    points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
    solution = Solution()
    print(solution.minCostConnectPoints(points))
