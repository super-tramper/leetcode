def eraseOverlapIntervals(intervals) -> int:
    n = len(intervals)
    if not n:
        return 0
    intervals.sort(key=lambda x: x[1])
    right = intervals[0][1]
    ans = 1
    for i in range(1, n):
        if intervals[i][0] >= right:
            ans += 1
            right = intervals[i][1]
    return n - ans


if __name__ == '__main__':
    intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
    print(eraseOverlapIntervals(intervals))
