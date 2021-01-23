import queue
import itertools
import collections

a = collections.defaultdict(dict)


def sortItems(n, m, group, beforeItems):
    ans = []
    for i in range(n):
        if group[i] == -1:
            group[i] = m
            m += 1
    # 初始组的化入度表和邻接表
    groupIndegree = [0] * m
    groupAdj = [[] for _ in range(m)]
    # item拓扑排序
    # 初始化项目的入度表和邻接表
    inDegree = [0] * n
    adj = [[] for _ in range(n)]

    for i in range(n):
        # item n 的group 为 group[n]
        for j in beforeItems[i]:
            # 统计group的依赖关系
            if group[j] != group[i]:
                groupAdj[group[j]].append(group[i])
            # 统计items的依赖关系
            adj[j].append(i)
    # 统计各group的入度
    for i in range(m):
        for j in groupAdj[i]:
            groupIndegree[j] += 1
    for i in range(n):
        for j in adj[i]:
            inDegree[j] += 1
    group_ans = topological(groupAdj, groupIndegree, m)
    if not len(group_ans):
        return []
    item_ans = topological(adj, inDegree, n)
    if not len(item_ans):
        return []
    # 根据组的拓扑排序结果输出item顺序
    ans_dict = {}
    for i in group_ans:
        ans_dict[i] = []
    for i in item_ans:
        ans_dict[group[i]].append(i)
    for i in group_ans:
        ans.extend(ans_dict[i])
    return ans


def topological(adj, inDegree, n):
    itemQueue = queue.Queue(maxsize=n)
    ans = []
    for i in range(n):
        if not inDegree[i]:
            itemQueue.put(i)
    while not itemQueue.empty():
        k = itemQueue.get()
        ans.append(k)
        for j in adj[k]:
            inDegree[j] -= 1
            if not inDegree[j]:
                itemQueue.put(j)
    return ans if len(ans) == n else []


if __name__ == '__main__':
    n = 8
    m = 2
    group = [-1, -1, 1, 0, 0, 1, 0, -1]
    beforeItems = [[], [6], [5], [6], [3, 6], [], [], []]
    print(sortItems(n, m, group, beforeItems))
