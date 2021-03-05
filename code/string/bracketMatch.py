# 由于LifoQueue没有读栈顶功能，索性自己实现一个栈


def bracketsMatch(s):
    stack = []

    def s_put(a):
        stack.append(a)

    def s_get():
        if len(stack):
            return stack.pop()

    def s_peek():
        if len(stack):
            return stack[-1]

    for i in s:
        if i == ')' and s_peek() == '(':
            s_get()
        else:
            s_put(i)
    return len(s) - len(stack)


if __name__ == '__main__':
    print(bracketsMatch('((()))'))
