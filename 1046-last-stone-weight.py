import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Python has a min-heap, so negate weights for a max-heap
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            y = -heapq.heappop(heap)  # heaviest
            x = -heapq.heappop(heap)  # second heaviest

            if y != x:
                heapq.heappush(heap, -(y - x))

        return -heap[0] if heap else 0
