# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    """
    Can invert a binary tree by doing post-order traversal and flipping the
    left and right child nodes.

    Time: O(n)
    Space: O(n) - recursive stack
    """

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root):
            if not root:
                return

            dfs(root.left)
            dfs(root.right)

            temp = root.right
            root.right = root.left
            root.left = temp

        dfs(root)
        return root
