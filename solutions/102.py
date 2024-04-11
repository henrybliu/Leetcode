# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    """
    Use a queue to maintain the nodes at each level. Only iterate through the
    size of one level at a time when adding to the queue.

    Time: O(n)
    Space: O(n)
    """

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque()
        q.append(root)

        res = []

        while q:
            # to simulate each level
            level = []
            for i in range(len(q)):
                curr = q.popleft()
                level.append(curr.val)

                # add the current node's children
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

            res.append(level)

        return res
