import heapq


def Union(x, y, parents):
    if x > y:
        x, y = y, x
    root = findParent(x, parents)
    parents[findParent(y, parents)] = root
    while y != root:
        temp = parents[y]
        parents[y] = root
        y = temp


def findParent(x, parents):
    while x != parents[x]:
        x = parents[x]
    return x


def smallestStringWithSwaps(s, pairs) -> str:
    n = len(s)
    parents = {}
    for i in range(n):
        parents[i] = i
    for pair in pairs:
        Union(pair[0], pair[1], parents)
    ans = ""
    heap = {}
    for key in parents:
        root = findParent(key, parents)
        if root in heap:
            heap[root].append(s[key])
        else:
            heap[root] = [s[key]]
    print(heap)
    for _, value in heap.items():
        heapq.heapify(value)
    for i in range(n):
        p = findParent(i, parents)
        ans += heapq.heappop(heap[p])
    return ans


if __name__ == '__main__':
    # s = "qdwyt"
    # pairs = [[2, 3], [3, 2], [0, 1], [4, 0], [3, 2]]
    # s = "cba"
    # pairs = [[0,1],[1,2]]
    s = "fqtvkfkt"
    pairs = [[2, 4], [5, 7], [1, 0], [0, 0], [4, 7], [0, 3], [4, 1], [1, 3]]
    print(smallestStringWithSwaps(s, pairs))
