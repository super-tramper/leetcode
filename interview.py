# 找出一个只包含左右括号的字符串里面复合匹配规则的最长字串

# （）
# (())
# (()()())
# ((()())()())

# ())(

def test_length(s):
    n = 0
    for i in range(len(s)):
        for j in range(i, len(s) + 1):
            if j - i > n and test_match(s[i:j]):
                n = j - i
    return n


def test_match(s):
    k = 0
    for i in s:
        k = k + 1 if i == '(' else k - 1
        if k < 0:
            return False
    return k == 0


if __name__ == '__main__':
    print(test_length(')((()())()())'))
