import heapq


class Solution:
    def medianSlidingWindow(self, nums, k: int):
        # 定义两个数组进行堆排序, left为大顶堆，right为小顶堆，则中位数为left的堆顶元素或left与right堆顶元素的平均值
        left, right = [], []
        # 两个指针分别指向当前区域的头部和尾部
        p, q = 0, 0
        n = len(nums)
        ans = []
        # 当尾指针指向数组末尾时结束计算
        while q < n:
            if q - p + 1 <= k:
                # 依次将数组中的元素加入两个堆中
                self.pushToHeaps(left, right, nums[q])
            else:
                # 从堆中删除p指向的元素
                if nums[p] <= -left[0]:
                    self.removeNum(left, -nums[p])
                else:
                    self.removeNum(right, nums[p])
                # 向右移动左指针
                p += 1
                # 调整两个堆的大小
                if len(left) < len(right):
                    heapq.heappush(left, -heapq.heappop(right))
                # 将元素加入堆中
                self.pushToHeaps(left, right, nums[q])
            if q - p + 1 == k:
                if len(left) == len(right):
                    ans.append((right[0] - left[0]) / 2)
                else:
                    ans.append(-left[0])
            q += 1
        return ans

    def pushToHeaps(self, left, right, num):
        # 针对新元素入堆，自动做平衡
        if len(left) == len(right):
            heapq.heappush(left, -heapq.heappushpop(right, num))
        else:
            heapq.heappush(right, -heapq.heappushpop(left, -num))

    def removeNum(self, q, num):
        ind = q.index(num)
        q[ind] = q[-1]
        del q[-1]
        heapq.heapify(q)


if __name__ == '__main__':
    k = 8
    nums = [5, 5, 8, 1, 4, 7, 1, 3, 8, 4]
    solution = Solution()
    print(solution.medianSlidingWindow(nums, k))
