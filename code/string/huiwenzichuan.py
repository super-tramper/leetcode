import sys


def expandString(s, l, r):
    count = 0
    while l >= 0 and r <= len(s) - 1:
        if s[l] == s[r]:
            l -= 1
            r += 1
            count += 1
        else:
            break
    return count


line = sys.stdin.readline().strip()
count = 0
k = 0
ret = ''
if len(line) == 1:
    print(1)
else:
    for i in range(len(line)):
        count += expandString(line, i, i)
    for i in range(len(line) - 1):
        count += expandString(line, i, i+1)
    print(count)

