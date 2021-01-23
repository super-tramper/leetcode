def findRedundantConnection(edges):
    n = len(edges)
    parents = [i for i in range(n)]
    ans = None
    for edge in edges:
        if findRoot(edge[0]-1, parents) != findRoot(edge[1]-1, parents):
            Union(edge[0]-1, edge[1]-1, parents)
        else:
            ans = edge
            break
    return ans


def Union(x, y, parents):
    root = findRoot(x, parents)
    parents[findRoot(y, parents)] = root
    while parents[y] != root:
        temp = parents[y]
        parents[y] = root
        y = temp


def findRoot(x, parents):
    while x != parents[x]:
        x = parents[x]
    return x


if __name__ == '__main__':
    edges = [[9, 10], [5, 8], [2, 6], [1, 5], [3, 8], [4, 9], [8, 10], [4, 10], [6, 8], [7, 9]]
    print(findRedundantConnection(edges))
