# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    '''
    Want to move left if the current node is greater than both p and q. Want to
    move left if the current node is less than p and q. Otherwise, we have
    found the node that we want to return.
    
    Time: O(n)
    Space: O(1) - even though we use a queue, we only ever store one node there at a time
    '''
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        queue = deque()
        queue.append(root)
        res = None

        while queue:
            #can keep trying to test if this node is the solution
            res = queue.popleft()

            #if greater than both, want to try going left
            if res.val > p.val and res.val > q.val:
                if res.left:
                    queue.append(res.left)

            #if less than both, want to try going right
            if res.val < p.val and res.val < q.val:
                if res.right:
                    queue.append(res.right)
        
        return res