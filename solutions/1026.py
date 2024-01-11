# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    We realize that we only need to pass down the minimum and maximum values of
    parent values -- any value that is not the min/max at an upper level will
    not yield as a large of a difference in calculating |a.val - b.val|.
    Therefore, we only need to pass down the minimum and largest values
    encountered in parent nodes.

    Time: O(n)
    Space: O(n) because of a recursive stack
    '''
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(root, minVal, maxVal):
            if not root:
                return 0

            left = dfs(root.left, min(minVal, root.val), max(maxVal, root.val))
            right = dfs(root.right, min(minVal, root.val), max(maxVal, root.val))
            
            # we can return the calculation of ancestor nodes, or the current node that we are on
            return max(left, max(right, max(abs(root.val - minVal), abs(root.val - maxVal))))

        return dfs(root, root.val, root.val)