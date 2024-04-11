# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Take advantage of the fact that the tree is a BST - we can pick which
    direction to explore depending on the value of the current node. We can use
    post-order to pass back up 0, if the current node is not within the range,
    or the node's value if it is in range. At each node, we want to pass back
    up the sum of the current node and its left and right subtrees.

    Time: O(n)
    Space: O(n)
    """

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(root):
            if not root:
                return 0

            toAdd = 0
            if low <= root.val <= high:
                toAdd += root.val

            left = 0
            right = 0

            if root.val > high:
                left = dfs(root.left)
            elif root.val < low:
                right = dfs(root.right)
            else:
                left = dfs(root.left)
                right = dfs(root.right)

            return left + right + toAdd

        return dfs(root)
