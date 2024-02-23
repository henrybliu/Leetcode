from collections import defaultdict
import heapq

class Solution:
    '''
    Djikstra's will prioritize cheaper paths. However, these paths may be
    longer than k stops. So when adding edges to the priority queue, we should
    check that we either have never visited this node before or that we have
    found a path with shorter stops to it.

    When would we visit a node again? 

    We visit a node again when an intial cheapest path will yield a path that
    exceeds the number of allowed stops. So, we would only want to visit this
    node again if there was a fewwer number of steps that can arrive at this
    node. Otherwise, we would run into the same issue again where we exceed k
    stops.

    
    Time: O(ElogV)
    Space: O(E)
    '''
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        mapp = defaultdict(list)
        visited = {}

        for f,t,p in flights:
            mapp[f].append((t,p))

        # (cost, dist, city)
        h = []
        heapq.heappush(h, (0, 0, src))

        while h:
            currCost, currStops, currCity = heapq.heappop(h)

            if currCity == dst and currStops <= k+1:
                return currCost
            
            if currCity not in visited or visited[currCity] > currStops:
                for neighbor, cost in mapp[currCity]:
                    heapq.heappush(h, (currCost + cost, currStops + 1, neighbor))

                visited[currCity] = currStops
            
        return -1

        