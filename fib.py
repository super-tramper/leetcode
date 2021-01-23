def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    p = 0
    q = 1
    for i in range(2, n+1):
        p, q = q, p+q
    return q


if __name__ == '__main__':
    print(fib(2))
