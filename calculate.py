from queue import LifoQueue


def test(s):
    q = LifoQueue()
    temp = ''
    q.put(s[0])
    for i in s[1:]:
        if temp == '(' and i == ')':
            q.get()
            continue
        q.put(i)
        temp = i
    return len(s)-q.qsize()


if __name__ == '__main__':
    print(test('(((((((((((()())()())'))