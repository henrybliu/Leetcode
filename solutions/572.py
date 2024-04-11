# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    For each node, we run a dfs on it to check if one of the original tree
    nodes is the root for the subtree.

    Time: O(n^2)
    Space: O(n) - recursive stack
    """

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # check if at a current node, the trees match
        def matches(left, right):
            if not left and not right:
                return True
            if (not left or not right) or (left.val != right.val):
                return False

            return matches(left.left, right.left) and matches(left.right, right.right)

        def dfs(root):
            if not root:
                return False
            if matches(root, subRoot):
                return True
            return dfs(root.left) or dfs(root.right)

        return dfs(root)
