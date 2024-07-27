from collections import defaultdict
import heapq


class Solution:
    """
    Use Dijkstra's to find the maximum number of nodes that can be reached
    starting from each node while being below the threshold distance. Use a
    minDistance dictionary to only add nodes to the heap when a "cheaper" path
    to it exists.

    Time: O(n^3logn) bc in the worst case, we all nodes have edges to all other
    nodes for each exploration.
    Space: O(n)
    """

    def findTheCity(
        self, n: int, edges: List[List[int]], distanceThreshold: int
    ) -> int:
        # Create an adjacency list
        undirectedMap = defaultdict(list)
        for v1, v2, weight in edges:
            undirectedMap[v1].append((v2, weight))
            undirectedMap[v2].append((v1, weight))

        def dijkstra(root):
            minDistance = {i: float("inf") for i in range(n)}
            minDistance[root] = 0
            heap = [(0, root)]

            while heap:
                currWeight, currNode = heapq.heappop(heap)

                if currWeight > minDistance[currNode]:
                    continue

                for neighbor, weight in undirectedMap[currNode]:
                    newWeight = currWeight + weight
                    if (
                        newWeight < minDistance[neighbor]
                        and newWeight <= distanceThreshold
                    ):
                        minDistance[neighbor] = newWeight
                        heapq.heappush(heap, (newWeight, neighbor))

            return (
                sum(
                    1
                    for distance in minDistance.values()
                    if distance <= distanceThreshold
                )
                - 1
            )

        minCities = float("inf")
        res = -1
        for root in range(n):
            citiesReached = dijkstra(root)
            if citiesReached <= minCities:
                res = root
                minCities = citiesReached

        return res
