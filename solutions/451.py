from collections import Counter
import heapq
class Solution:
    '''
    Find the number of occurrences per letter. Then we want to sort by the
    number of occurrences, which can be done using a max heap. Finally, just
    create the final string by popping from the heap.

    Time: O(nlogn)
    Space: O(n)

    '''
    def frequencySort(self, s: str) -> str:
        counts = Counter(s)

        h = []
        for k,v in counts.items():
            heapq.heappush(h,(-v, k))

        res = ""

        while h:
            count, letter = heapq.heappop(h)
            res += letter * (-count)

        return res
