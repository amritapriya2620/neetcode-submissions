import heapq

class Solution:
    def lastStoneWeight(self, stones):
        heap_max = [-stone for stone in stones]
        heapq.heapify(heap_max)

        while len(heap_max) > 1:
            stone1 = heapq.heappop(heap_max)
            stone2 = heapq.heappop(heap_max)

            if stone1 != stone2:
                heapq.heappush(heap_max, stone1 - stone2)

        if heap_max:
            return -heap_max[0]
        return 0