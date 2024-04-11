# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict, deque


class Solution:
    """
    Create an undirected graph and perform BFS on the start root until all
    nodes are reached.

    Time: O(n)
    Space: O(n)
    """

    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        adjList = defaultdict(set)

        # perform dfs to create an undirected graph for this tree
        def dfs(root):
            if not root:
                return

            if root.left:
                adjList[root.val].add(root.left.val)
                adjList[root.left.val].add(root.val)
            if root.right:
                adjList[root.val].add(root.right.val)
                adjList[root.right.val].add(root.val)

            dfs(root.left)
            dfs(root.right)

        dfs(root)

        visited = set()
        q = deque()
        q.append(start)
        visited.add(start)

        # start at -1 because we add one per each level but we start at 0
        minutes = -1

        # perform BFS starting from the start node
        while q:
            minutes += 1
            for i in range(len(q)):
                curr = q.popleft()

                for n in adjList[curr]:
                    if n not in visited:
                        visited.add(n)
                        q.append(n)
        return minutes
