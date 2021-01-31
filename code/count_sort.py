def count_sort(l):
    l_min = float('inf')
    l_max = -float('inf')
    ret_list = []
    # 求出列表中的最大值及最小值
    for v in l:
        if v < l_min:
            l_min = v
        if v > l_max:
            l_max = v
    # 初始化计数容器
    count_list = [0] * (l_max - l_min + 1)
    # 统计出现次数
    for i in l:
        count_list[i - l_min] += 1
    # 按顺序输出结果
    for index, value in enumerate(count_list):
        while value > 0:
            ret_list.append(index + l_min)
            value -= 1
    print(ret_list)


if __name__ == '__main__':
    l = [1, 3, 4, 5, 2, 3, 2, 5, 9, 5, 6, 8]
    count_sort(l)
