# 1 9*9 1*1 3*7
from collections import defaultdict


def findCommonTail():
    """
    把1-9内的任意两个数，按相乘后的个位数字分组
    例如 [(1, 1), (3, 7), (9, 9)] 属于分组1
    """
    ret_dict = defaultdict(list)
    for i in range(1, 10):
        for j in range(i, 10):
            ret_dict[int(str(i*j)[-1])].append((i, j))
    return ret_dict


def curiosNum():
    """暴力解法"""
    ans = []
    for i in range(10, 100):
        for j in range(10, 100):
            if i % 10 == 0 or j % 10 == 0 or i == j or len(set(str(i))) == 1 or len(set(str(j))) == 1 or str(i)[
                                                                                                         ::-1] == str(
                j): continue
            if i * j == int(str(i)[::-1]) * int(str(j)[::-1]):
                ans.append((i, j))
    return ans


def curiosNum2():
    """寻找可能的组合后计算"""
    ret_dict = findCommonTail()
    ans = []
    # 用于判断类似的组合是否已经出现过，例如（12，42）（21， 24）和（42， 12）（24， 21）属于同一个解
    ans_set = set()
    for k in range(1, 10):
        for i in ret_dict[k]:
            for j in ret_dict[k]:
                if i == j: continue
                # 在同一组中计算出所有组内元素能组成的数字（同一组内的数字组合后相乘，其个位数字相同）
                a1, a2, b1, b2 = i[0]*10+j[0], i[1]*10+j[1], j[1]*10+i[1], j[0]*10+i[0]
                c1, c2, d1, d2 = i[0]*10+j[1], i[1]*10+j[0], j[0]*10+i[1], j[1]*10+i[0]
                if a1*a2 == b1*b2 and tuple(sorted([a1, a2, b1, b2])) not in ans_set:
                    ans_set.add(tuple(sorted([a1, a2, b1, b2])))
                    ans.append((a1, a2))
                if c1*c2 == d1*d2 and tuple(sorted([c1, c2, d1, d2])) not in ans_set:
                    ans_set.add(tuple(sorted([c1, c2, d1, d2])))
                    ans.append((c1, c2))
    return ans


if __name__ == '__main__':
    ans = curiosNum2()
    for i in ans:
        print(i)
    print(len(ans))
    # print(findCommonTail())