class Solution:
    def makeConnected(self, n, connections) -> int:
        def find(x):
            if x != parents[x]:
                parents[x] = find(parents[x])
            return parents[x]
        if n - 1 > len(connections):
            return -1
        parents = list(range(n))
        for x, y in connections:
            root1 = find(x)
            root2 = find(y)
            parents[root2] = root1
        setNum = 0
        for i in range(n):
            if i == parents[i]:
                setNum += 1
        return setNum - 1


if __name__ == '__main__':
    n = 4
    connections = [[0,1],[0,2],[1,2]]
    solution = Solution()
    print(solution.makeConnected(n, connections))
