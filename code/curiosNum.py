# 1 9*9 1*1 3*7
from collections import defaultdict


def findCommonTail():
    ret_dict = defaultdict(list)
    for i in range(1, 10):
        for j in range(i, 10):
            ret_dict[int(str(i*j)[-1])].append((i, j))
    return ret_dict


def curiosNum():
    ans = []
    for i in range(10, 100):
        for j in range(10, 100):
            if i % 10 == 0 or j % 10 == 0 or i == j or len(set(str(i))) == 1 or len(set(str(j))) == 1 or str(i)[
                                                                                                         ::-1] == str(
                j): continue
            if i * j == int(str(i)[::-1]) * int(str(j)[::-1]):
                ans.append((i, j))
    return ans


if __name__ == '__main__':
    # ans = curiosNum()
    # for i in ans:
    #     print(i)
    print(findCommonTail())