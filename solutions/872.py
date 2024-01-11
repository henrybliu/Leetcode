# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    '''
    Use post-order traversal to add to an array the leaf nodes from left to
    right. Do this for both trees and then compare the created arrays if they
    are the same.

    Time: O(n)
    Space: O(n)
    '''
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root, leaves):
            if not root:
                return

            dfs(root.left, leaves)
            dfs(root.right, leaves)

            if not root.left and not root.right:
                leaves.append(root.val)

            return leaves
        
        leaves1 = dfs(root1, [])
        leaves2 = dfs(root2, [])

        if len(leaves1) != len(leaves2):
            return False

        for i in range(len(leaves1)):
            if leaves1[i] != leaves2[i]:
                return False

        return True
