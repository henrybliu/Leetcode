from collections import defaultdict


class Solution:
    """
    Keep track of which cities have outgoing edges, return the city that has no
    outgoing edges.

    Time: O(n)
    Space: O(n)
    """

    def destCity(self, paths: List[List[str]]) -> str:
        # just count which city has an outgoing edge
        counts = defaultdict(int)
        cities = set()
        for start, end in paths:
            counts[start] += 1
            cities.add(start)
            cities.add(end)

        # find which city that has zero outgoing edges
        for city in cities:
            if counts[city] == 0:
                return city
