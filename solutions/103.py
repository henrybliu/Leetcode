# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    """
    Use level order traveral where for every other level, we would add the
    reverse of the level to the result.

    Time: O(n)
    Space: O(n)
    """

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        q = deque([root])
        goingRight = True

        while q:
            level = []
            for i in range(len(q)):
                curr = q.popleft()

                level.append(curr.val)

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

            if goingRight:
                res.append(level)
                goingRight = False

            else:
                res.append(level[::-1])
                goingRight = True

        return res
