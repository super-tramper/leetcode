import re


def reverse(x: int) -> int:
    ret = re.match(r'(\D?)(\d+)', str(x))
    if ret:
        symbol, num = ret.group(1), ret.group(2)
        rev = int(symbol+str(int(num[::-1])))
        if rev < 0:
            return abs(rev)-1
        if -2**31 < rev < 2**31 -1:
            return int(symbol+str(int(num[::-1])))
        else:
            return 0


if __name__ == '__main__':
    print(reverse(1534236469))