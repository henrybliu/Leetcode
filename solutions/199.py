# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    """
    Perform a level-order tree traversal and only saving the right-most node.

    Time: O(n)
    Space: O(n)
    """

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # base case
        if not root:
            return []

        res = []

        q = deque()
        q.append(root)

        while q:
            # create each level
            level = []
            for i in range(len(q)):
                curr = q.popleft()
                level.append(curr.val)

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

            # save the last value of each level
            res.append(level[-1])

        return res
