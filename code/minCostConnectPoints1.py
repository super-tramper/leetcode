import heapq
import numpy as np


class Solution:
    def minCostConnectPoints(self, points) -> int:
        n = len(points)
        dist = np.zeros((n, n), dtype=int)
        minDist = [float('inf')] * n
        v = [0] * n
        start = 0
        for i in range(n):
            for j in range(n):
                d = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                dist[i][j], dist[j][i] = d, d
        hq = []
        heapq.heappush(hq, [0, start])
        ans = 0
        while len(hq):
            val, i = heapq.heappop(hq)
            if v[i]: continue
            v[i] = 1
            ans += val

            for j in range(n):
                if not v[j] and minDist[j] > dist[i][j]:
                    minDist[j] = dist[i][j]
                    heapq.heappush(hq, [minDist[j], j])
        return ans


if __name__ == '__main__':
    points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
    solution = Solution()
    print(solution.minCostConnectPoints(points))
