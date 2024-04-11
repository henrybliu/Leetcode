# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    """
    Use level order traversal and update res to be the leftmost node value.

    Time: O(n)
    Space: O(n)
    """

    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        res = 0

        while q:
            for i in range(len(q)):
                curr = q.popleft()
                if i == 0:
                    res = curr.val

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

        return res
