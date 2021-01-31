def calcEquation(equations, values, queries):
    parents = {}
    weights = {}
    # 初始化
    for (a, b), value in zip(equations, values):
        if a not in parents:
            parents[a] = a
            weights[a] = 1.0
        if b not in parents:
            parents[b] = b
            weights[b] = 1.0
        Union(a, b, value, parents, weights)
    ans = []
    for c, d in queries:
        root1, weight1 = Find(c, parents, weights)
        root2, weight2 = Find(d, parents, weights)
        # root1 != root2 或者其中一个为""，即不在同一集合中
        if root1 != root2 or root1 == "" or root2 == "":
            ans.append(-1.0)
        else:
            ans.append(weight1 / weight2)
    return ans

def Find(x, parents, weights):
    if x not in parents:
        return "", -1.0
    weight = 1.0
    while x != parents[x]:
        weight *= weights[x]
        x = parents[x]
    return x, weight

def Union(x, y, value, parents, weights):
    root1, weight1 = Find(x, parents, weights)
    root2, weight2 = Find(y, parents, weights)
    if root1 == root2:
        return
    parents[root1] = root2
    weights[root1] = 1.0 / weight1 * value * weight2


if __name__ == '__main__':
    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    print(calcEquation(equations, values, queries))
