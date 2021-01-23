import collections


def removeStones0(stones) -> int:
    def union(x: int, y: int):
        parent[find(x)] = find(y)

    def find(idx: int) -> int:
        if parent[idx] != idx:
            idx = parent[idx]
        return parent[idx]

    n = len(stones)
    parent = list(range(n))
    row_map, col_map = {}, {}
    for i in range(n):
        if stones[i][0] not in row_map:
            row_map[stones[i][0]] = i
        else:
            union(i, row_map[stones[i][0]])
        if stones[i][1] not in col_map:
            col_map[stones[i][1]] = i
        else:
            union(i, col_map[stones[i][1]])
    print(row_map)
    print(col_map)
    print(parent)
    graph = set()
    for i in range(n):
        graph.add(find(i))
    return n - len(graph)


def removeStones1( stones) -> int:
    def union(x: int, y: int):
        parent[find(x)] = find(y)

    def find(idx: int) -> int:
        if parent[idx] != idx:
            parent[idx] = find(parent[idx])
        return parent[idx]

    n = len(stones)
    parent = list(range(n))
    row_map, col_map = {}, {}
    for i in range(n):
        if stones[i][0] not in row_map:
            row_map[stones[i][0]] = i
        else:
            union(i, row_map[stones[i][0]])
        if stones[i][1] not in col_map:
            col_map[stones[i][1]] = i
        else:
            union(i, col_map[stones[i][1]])
    graph = set()
    for i in range(n):
        graph.add(find(i))
    return n - len(graph)

if __name__ == '__main__':
    print(removeStones0([[2, 1], [2, 2]]))



