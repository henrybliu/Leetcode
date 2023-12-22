# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    Take advantage of the the tree being a BST, a BST has properties of the
    max/min values that node can have relative to the parent.

    Time: O(n)
    Space: O(n) - recursive stack
    '''
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, small, large):
            if not root:
                return True

            if root.val <= small or root.val >= large:
                return False

            #search left
            left = dfs(root.left, small, root.val)

            #search right
            right = dfs(root.right, root.val, large)

            return left and right

        return dfs(root, float('-inf'), float('inf'))