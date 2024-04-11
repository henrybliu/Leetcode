# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    """
    We can use post-order traversal to check for 3 cases:

    1.) the current node and its left child are p and q
    2.) the current node and its right child are p and q
    3.) the left child and the right child are p and q

    We can return at the first occurrence of this because post-order traversal
    would ensure that we are at the lowest level.

    Time: O(n)
    Space: O(n)
    """

    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        res = [None]

        def dfs(root):
            if not root:
                return False

            left = dfs(root.left)
            right = dfs(root.right)
            curr = root == p or root == q

            if (left and right) or (curr and left) or (curr and right):
                res[0] = root
                return

            return left or right or curr

        dfs(root)
        return res[0]
