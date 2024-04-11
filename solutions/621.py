from collections import Counter, deque
import heapq


class Solution:
    """
    We want to start with the tasks that appear the most. We maintain this
    ordering with a max heap. We also use a queue to prevent the same task from
    being completed if an interval of n has not passed yet.

    Time: O(nlogn)
    Space: O(n)
    """

    def leastInterval(self, tasks: List[str], n: int) -> int:
        h = []
        q = deque()
        counts = Counter(tasks)
        time = 0

        for k, v in counts.items():
            heapq.heappush(h, (-v, k))

        while h or len(q) > 0:
            if h:
                currCount, task = heapq.heappop(h)
                if currCount + 1 < 0:
                    q.append((time + n, currCount + 1, task))

            while q and q[0][0] == time:
                waitTime, count, task = q.popleft()
                heapq.heappush(h, (count, task))

            time += 1

        return time
