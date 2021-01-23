import math


def convert(s: str, numRows: int) -> str:
    if numRows == 1:
        return s
    step = 2 * numRows - 2
    ret = []
    for i in range(int(math.ceil(len(s) / step))):
        ret.append(list(s[i * step:(i + 1) * step]))

    for i in range(step - len(s) % step):
        ret[-1].append('')
    s = ''
    for i in range(numRows):
        if i in range(1,numRows-1):
            for j in ret:
                s += j[i]
                s += j[2*(numRows-1)-i]
        else:
            for j in ret:
                s += j[i]
    return s


if __name__ == '__main__':
    print(convert(s="ab", numRows=1))
