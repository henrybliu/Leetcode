from collections import defaultdict
from typing import List
import heapq


class Solution:
    """
    Use Dijkstra's to find the cheapest path to create each letter. When runnning Dijkstra's we can also keep track of the cost between letter pairs.
    """

    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int],
    ) -> int:
        found = {}
        res = 0
        mapp = defaultdict(list)

        for orgLetter, changeLetter, price in zip(original, changed, cost):
            mapp[orgLetter].append((changeLetter, price))

        def dijkstra(start, target):
            heap = [(0, start)]
            visited = set()

            while heap:
                currCost, currLetter = heapq.heappop(heap)
                if currLetter == target:
                    return currCost

                if currLetter in visited:
                    continue

                # optimization so that Dijkstra's can potentially create the pairings that we may need to find later
                found[(start, currLetter)] = currCost

                visited.add(currLetter)

                for neighbor, neighborCost in mapp[currLetter]:
                    if neighbor not in visited:
                        newCost = currCost + neighborCost
                        heapq.heappush(heap, (newCost, neighbor))

            return -1

        for startLetter, targetLetter in zip(source, target):
            if startLetter != targetLetter:
                if (startLetter, targetLetter) not in found:
                    found[(startLetter, targetLetter)] = dijkstra(
                        startLetter, targetLetter
                    )
                if found[(startLetter, targetLetter)] == -1:
                    return -1
                res += found[(startLetter, targetLetter)]

        return res
