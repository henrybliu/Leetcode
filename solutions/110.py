# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    Post-order traversal to pass back up the depths and whether or not the
    height for the left and right sides are valid.
    
    Time: O(n)
    Space: O(n) - recursive stack
    '''
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [0, True]
            left = dfs(root.left)
            right = dfs(root.right)

            leftHeight = left[0]
            rightHeight = right[0]
            leftBalanced = left[1]
            rightBalanced = right[1]

            #don't forget to increment by 1 to count the node that we are at
            if abs(leftHeight - rightHeight) > 1:
                return [1+max(leftHeight, rightHeight), False]
            else:
                #return if the previous subtrees were also balanced
                return [1+max(leftHeight, rightHeight), leftBalanced and rightBalanced]

        return dfs(root)[1]