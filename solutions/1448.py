# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Do post-order traversal to find the children for each node and whether
    there are any child nodes with a value larger than the original.

    Time: O(n)
    Space: O(n) - recursive stack
    """

    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root, val):
            if not root:
                return 0

            res = 0

            # if the current node value was larger than the parent node's
            if root.val >= val:
                res += 1

            # want to pass down the largest value encountered so far to the next level
            res += dfs(root.left, max(val, root.val))
            res += dfs(root.right, max(val, root.val))

            return res

        # should account for negative node values
        return dfs(root, float("-inf"))
