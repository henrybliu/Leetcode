# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    At each node we want to try taking the max sum of the current node and its
    two children. We also pass up the greater of the paths - either the left or
    the right including the current node.

    Time: O(n)
    Space: O(n) - recursive stack
    """

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [float("-inf")]

        def dfs(root):
            if not root:
                return 0
            # at each node, want to add the left and the right
            # then pass up the longest path going either down or right
            left = dfs(root.left)
            right = dfs(root.right)

            if left < 0:
                left = 0
            if right < 0:
                right = 0

            res[0] = max(res[0], root.val + left + right)
            return max(root.val + left, root.val + right)

        dfs(root)
        return res[0]
