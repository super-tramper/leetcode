from collections import deque


def maxSlidingWindow(nums, k):
    q = deque()
    n = len(nums)
    for i in range(k):
        while q and nums[q[-1]] <= nums[i]:
            q.pop()
        q.append(i)
    ret = [nums[q[0]]]
    for i in range(k, n):
        while q and nums[q[-1]] <= nums[i]:
            q.pop()
        q.append(i)
        while q[0] <= i-k:
            q.popleft()
        ret.append(nums[q[0]])
    return ret


if __name__ == '__main__':
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    print(maxSlidingWindow(nums, 3))
