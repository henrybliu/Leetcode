import heapq

class Solution:
    '''
    Use a max heap to store the points with the shortest distance from the
    origin.

    Time: O(nlogn)
    Space: O(n)
    '''
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []

        def calculateDistance(x,y):
            xSq = x**2
            ySq = y**2
        
            return sqrt(xSq + ySq)

        for point in points:
            x = point[0]
            y = point[1]
            distance = calculateDistance(x,y)

            if len(heap) < k:
                heapq.heappush(heap, (-1*distance, x, y))
            else:
                if -1 * distance > heap[0][0]:
                    heapq.heapreplace(heap, (-1*distance, x, y))
             
        
        for distance, x, y in heap:
            res.append([x,y])
        return res

