import collections


def calcEquation(equations, values, queries):
    table = collections.defaultdict(dict)
    for (a, b), value in zip(equations, values):
        table[a][b] = value
        table[b][a] = 1.0 / value
    ans = [dfs(c, d, table, set()) if c in table and d in table else -1.0 for (c, d) in queries]
    return ans


def dfs(x, y, table, visited):
    if x == y:
        return 1.0
    visited.add(x)
    print(x, y, table, visited)
    for k in table[x]:
        if k in visited:
            continue
        visited.add(k)
        d = dfs(k, y, table, visited)
        if d > 0:
            return d * table[x][k]
    return -1.0


if __name__ == '__main__':
    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    print(calcEquation(equations, values, queries))
