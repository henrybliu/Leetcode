# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Perform dfs to find and test if the sum of the left and right depths are
    the largest path sum. Pass back up the sum of going through the current
    node and the larger path of going throught the left or right child.

    Time: O(n)
    Space: O(n) - recursive stack
    """

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]

        def dfs(root):
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            res[0] = max(res[0], left + right)

            return 1 + max(left, right)

        dfs(root)
        return res[0]
