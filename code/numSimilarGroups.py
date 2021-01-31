class Solution:
    def numSimilarGroups(self, strs) -> int:
        def checkSimilar(x, y):
            differ = 0
            for i in range(len(x)):
                if x[i] != y[i]:
                    differ += 1
                if differ > 2:
                    return False
            return differ == 0 or differ == 2

        def findParent(x):
            if x != parent[x]:
                parent[x] = findParent(parent[x])
            return parent[x]

        def union(x, y):
            parent[findParent(y)] = findParent(x)

        n = len(strs)
        parent = [i for i in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                if findParent(i) == findParent(j):
                    continue
                if checkSimilar(strs[i], strs[j]):
                    union(i, j)
        ans = sum(1 for i in range(n) if i == parent[i])
        return ans


if __name__ == '__main__':
    strs = ["tars", "rats", "arts", "star"]
    solution = Solution()
    print(solution.numSimilarGroups(strs))
