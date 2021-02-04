from queue import Queue


class Solution:
    def swimInWater(self, grid) -> int:
        def travelToEnd(height):
            q = Queue(maxsize=n * n)
            visited = [0] * n * n
            if grid[0][0] > height:
                return False
            q.put((0, 0))
            while not q.empty():
                platform = q.get()
                for d in directions:
                    x, y = platform[0] + d[0], platform[1] + d[1]
                    if 0 <= x < n and 0 <= y < n and not visited[x * n + y] and grid[x][y] <= height:
                        if (x, y) == (n - 1, n - 1):
                            return True
                        q.put((x, y))
                        visited[x * n + y] = 1
            return False

        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        n = len(grid)
        maxh = max([max(grid[i]) for i in range(n)])
        low, high = grid[n - 1][n - 1], maxh
        while low <= high:
            mid = (high + low) // 2
            if travelToEnd(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low


if __name__ == '__main__':
    grid = [[7, 11, 5, 3], [2, 14, 12, 8], [4, 13, 9, 10], [6, 0, 1, 15]]
    solution = Solution()
    print(solution.swimInWater(grid))
