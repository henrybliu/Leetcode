import heapq


class Solution:
    """
    Only store the k largest elements in the heap. Use a min heap so that we
    only store the largest values.

    Time: O(nlogn)
    Space: O(n)

    """

    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            else:
                if num > heap[0]:
                    heapq.heapreplace(heap, num)

        return heap[0]
