import heapq

class MedianFinder:
    '''
    Use two heaps to find the median. Maintain a size difference of 0 to 1.

    Time: O(logn) - the time to add to either heap
    Space: O(n)
    '''

    def __init__(self):
        #for smaller than the median
        self.maxHeap = []
        #for larger than the median
        self.minHeap = []

    def addNum(self, num: int) -> None:
        #for when there are less than 2 elements
        if not self.minHeap or not self.maxHeap:
            heapq.heappush(self.minHeap, num)

        #if the number is less than the number to the left of the median
        elif num < -1*self.maxHeap[0]:
            heapq.heappush(self.maxHeap, -1*num)
        else:
            heapq.heappush(self.minHeap, num)

        #check that neither heap exceeds the other heap by more than 1 element in size
        if len(self.minHeap) > len(self.maxHeap)+1:
            transfer = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -1*transfer)
        
        if len(self.maxHeap) > len(self.minHeap)+1:
            transfer = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, -1*transfer)

        
    def findMedian(self) -> float:
        if len(self.maxHeap) == len(self.minHeap):
            return (-1*self.maxHeap[0] + self.minHeap[0])/2
        elif len(self.maxHeap) > len(self.minHeap):
            return -1*self.maxHeap[0]
        else:
            return self.minHeap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()