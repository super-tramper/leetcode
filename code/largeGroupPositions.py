def largeGroupPositions(s: str):
    ret = []
    n = len(s)
    count = 1
    start = 0
    for i in range(n):
        if i == n - 1 or s[i] != s[i + 1]:
            if count > 2:
                ret.append([start, i])
            count = 1
            start = i + 1
        else:
            count += 1
    return ret


if __name__ == '__main__':
    s = "aaa"
    print(largeGroupPositions(s))
