# 输入为一列表，列表中每个元素描述相应位置椅子的占用情况,0代表空座，1代表非空
# 返回值为满足题目要求的最后一个座位的位置（从1开始计数），此处不考虑多个符合要求的结果和满/空座的情况
# 思路：正序求出该座位距上一个非空座位之间的空座个数，结果存在数组中，将输入逆置后求出相同数组，把数组逆置，然后比较两个数组中对应位置数字的大小，
# 将较小值存入结果数组中，记录并更新结果的最大值为max，记录max出现的位置，遍历完成后，返回max最后出现的位置+1
def FindSeat(p: list) -> int:
    def getLastDistance(q: list) -> list:
        temp = - len(q)
        d = []
        dist = 0
        for i in range(len(q)):
            if q[i]:
                d.append(-1)
                temp = i
            else:
                dist = i - temp - 1
                d.append(dist)
        return d

    l1 = getLastDistance(p)
    l2 = getLastDistance(p[::-1])[::-1]
    ret = []
    max = 0
    pos = 0
    for i in range(len(l1)):
        temp = min(l1[i], l2[i])
        if temp >= max:
            max = temp
            pos = i
        ret.append(temp)
    return pos + 1


if __name__ == '__main__':
    print(FindSeat([1, 1, 0, 1, 1, 1]))
