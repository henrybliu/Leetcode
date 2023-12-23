from collections import Counter, deque
import heapq

class Solution:
    '''
    Use a max heap and a deque. The max heap is because we want to process as
    much as possible the tasks that have the most occurrences. The deque can
    be used to store the tasks that we have processed and that we need to wait
    for n time before being able to process it again.
    
    Time: O(nlogn)
    Space: O(n)
    '''
    def leastInterval(self, tasks: List[str], n: int) -> int:
        h = []
        q = deque()
        counts = Counter(tasks)
        time = 0
        
        for k,v in counts.items():
            heapq.heappush(h, (-v,k))

        while h or len(q)>0:
            if h:
                currCount, task = heapq.heappop(h)
                if currCount + 1 < 0:
                    q.append((time+n, currCount+1, task))

            # there must be n units of time between two of the same tasks - so
            # we can't process a task as soon as the time is met - needs to be
            # the next unit of time!
            while q and q[0][0] == time:
                waitTime, count, task = q.popleft()
                heapq.heappush(h, (count, task))
  
            time+=1

        return time