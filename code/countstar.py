import sys

tcount = int(sys.stdin.readline().strip())
stars = []
inline_stars = 0
for i in range(tcount):
    values = [int(i.strip()) for i in sys.stdin.readline().strip().split(',')]
    stars.append(values)
for i in range(len(stars)):
    ret = []
    for j in range(len(stars)):
        if stars[i][0] != stars[j][0]:
            k = (stars[i][1] - stars[j][1])/(stars[i][0]-stars[j][0])
        else:
            k = None
        ret.append(k)
    for l in set(ret):
        if l is not None:
            inline_stars = ret.count(l)+1 if ret.count(l) > inline_stars else inline_stars
        else:
            inline_stars = ret.count(l) if ret.count(l) > inline_stars else inline_stars
print(inline_stars)