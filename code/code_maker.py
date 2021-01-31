# while True:
#     try:
#         a = input()
#         b, c = int(a.split(' ')[0].strip()), int(a.split(' ')[1].strip())
#         print(b+c)
#     except EOFError:
#         break
# import sys
# for line in sys.stdin:
#     a, b = map(int,line.split())
#     print(a + b)
# while True:
#     sum = 0
#     l = input().split()
#     if int(l[0]) == 0:
#         break
#     for i in range(1,int(l[0])+1):
#         sum += int(l[i])
#     print(sum)
# import sys
# n = int(input().strip())
# for _ in range(n):
#     l = list(map(int, sys.stdin.readline().strip().split()))
#     s = sum(l[1:l[0]+1])
#     print(s)

# import sys
# for line in sys.stdin:
#     if line.strip() == '':
#         break
#     l = list(map(int,line.split()))
#     print(sum(l[1:l[l[0]]+1]))
# import sys
# for line in sys.stdin:
#     if line.strip() == '':
#         break
#     print(sum(list(map(int, line.strip().split()))))

# l = ['c', 'd', 'a', 'bb', 'e']
# l.sort()
# print(l)
# n = input()
# l = input().strip().split()
# l.sort()
# print(' '.join(l))

# import sys
# for line in sys.stdin:
#     l = line.strip().split()
#     l.sort()
#     print(' '.join(l))

# import sys
# for line in sys.stdin:
#     l = line.strip().split(',')
#     l.sort()
#     print(','.join(l))

# import sys
# for line in sys.stdin:
#     if line.strip() == '':
#         break
#     print(sum(list(map(int, line.strip().split()))))
# import sys
# n = int(input().strip())
# for i in range(n):
#     line = sys.stdin.readline()
#     print(sum(list(map(int, line.strip().split()))))
# import sys
#
# while True:
#     line = sys.stdin.readline()
#     s = sum(list(map(int, line.strip().split())))
#     if s == 0:
#         break
#     print(s)
