import heapq
class Solution:
    '''
    Use a max heap to keep smashing the two largest stones.
    
    Time: O(nlogn)
    Space: O(n)
    '''
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heap.append(-stone)

        heapq.heapify(heap)


        while len(heap) > 1:
            stone1 = heapq.heappop(heap)
            stone2 = heapq.heappop(heap)

            if stone1 != stone2:
                heapq.heappush(heap, -abs(abs(stone1)-abs(stone2)))

        return -heap[0] if heap else 0

