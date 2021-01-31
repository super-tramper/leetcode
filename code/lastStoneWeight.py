import heapq


def lastStoneWeight(stones):
    heap = []
    for i in stones:
        heapq.heappush(heap, -i)
    while len(heap) > 1:
        stone_a = -heapq.heappop(heap)
        stone_b = -heapq.heappop(heap)
        heapq.heappush(heap, -abs(stone_a - stone_b))
    return -heap[0]


if __name__ == '__main__':
    stones = [2, 7, 4, 1, 8, 1]
    print(lastStoneWeight(stones))
