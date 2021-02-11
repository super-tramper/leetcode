import heapq


class KthLargest:

    def __init__(self, k: int, nums):
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        self.hq = nums
        self.p = k

    def add(self, val: int) -> int:
        heapq.heappush(self.hq, val)
        while len(self.hq) > self.p:
            heapq.heappop(self.hq)
        return self.hq[0]




# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)