from collections import defaultdict


class Solution:
    """
    Count number of edges each node has. Want to assign the node with the most
    edges the greatest value. Finally, go back through the roads and sum up
    each of the values to return the optimal sum.

    """

    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        mapp = defaultdict(int)
        for v1, v2 in roads:
            mapp[v1] += 1
            mapp[v2] += 1

        orderedKeys = sorted(mapp.keys(), key=lambda k: mapp[k], reverse=True)

        assignedValues = defaultdict(int)
        value = n
        for key in orderedKeys:
            assignedValues[key] = value
            value -= 1

        res = 0

        for v1, v2 in roads:
            res += assignedValues[v1] + assignedValues[v2]

        return res
