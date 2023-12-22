# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    Perform in-order traversal to create an array of elements in ascending
    order. Extract the kth element.

    Time: O(n)
    Space: O(n)
    '''
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        order = []
        def dfs(root):
            if not root:
                return
            left = dfs(root.left)
            order.append(root.val)
            right = dfs(root.right)

        dfs(root)
        return order[k-1]