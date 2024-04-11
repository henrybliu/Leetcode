# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    """
    Recursively traverse in the same direction for both trees - returning a
    boolean if anything was violated.

    Time: O(n)
    Space: O(n) - recursive stack
    """

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(left, right):
            if not left and not right:
                return True

            if (not left or not right) or (left.val != right.val):
                return False

            return dfs(left.left, right.left) and dfs(left.right, right.right)

        return dfs(p, q)
