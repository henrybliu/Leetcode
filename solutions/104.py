# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    Perform dfs to return the largest sum. Sum being the number of levels
    visited.
    
    Time: O(n)
    Space: O(n) - recursive stack
    '''
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root, depth):
            if not root:
                return depth
            
            left = dfs(root.left, depth+1)
            right = dfs(root.right, depth+1)

            return max(left, right)

        return dfs(root, 0)