def eraseOverlapIntervals(intervals) -> int:
    n = len(intervals)
    if not n:
        return 0
    f = [1]
    intervals.sort()
    for i in range(1, n):
        f.append(max([f[j] for j in range(i) if intervals[j][1] <= intervals[i][0]], default=0) + 1)
    return n - max(f)


if __name__ == '__main__':
    intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
    print(eraseOverlapIntervals(intervals))
