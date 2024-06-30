from collections import defaultdict


class Solution:
    """

    For each node value, we want to add it to all of its children before adding
    the next greater node value. This will ensure that all node values are
    appended in ascending order. For example, in the original example, we want
    to add the node value 0 to its children 3, 5, 6, and 7 before adding the
    node value of 1 to the same children nodes.

    Time: O(V*E)
    Space: O(V*E)
    """

    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        directChildren = defaultdict(list)
        res = [[] for _ in range(n)]
        for v1, v2 in edges:
            directChildren[v1].append(v2)

        def dfs(orgVal, currVal):
            for neighbor in directChildren[currVal]:
                # check that value was not already added
                if not res[neighbor] or res[neighbor][-1] != orgVal:
                    res[neighbor].append(orgVal)
                    dfs(orgVal, neighbor)

        for i in range(n):
            dfs(i, i)

        return res
