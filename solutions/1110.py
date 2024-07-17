# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    """
    Mark nodes who's parents are to be deleted. Add to the result nodes that
    have parents deleted and that are also not marked to be deleted. Delete
    child nodes from the tree if they are to be deleted.

    Time: O(V+E)
    Space: O(V)
    """

    def delNodes(
        self, root: Optional[TreeNode], to_delete: List[int]
    ) -> List[TreeNode]:
        res = []
        toDelete = set(to_delete)

        q = deque()
        q.append((root, True))

        while q:
            curr, deleteParent = q.popleft()

            # return root nodes that had parent deleted and that are not to be deleted
            if curr.val not in toDelete and deleteParent:
                res.append(curr)

            # add child nodes to the queue and mark if the parent has been deleted
            if curr.val in toDelete:
                if curr.left:
                    q.append((curr.left, True))
                if curr.right:
                    q.append((curr.right, True))

            else:
                if curr.left:
                    q.append((curr.left, False))
                if curr.right:
                    q.append((curr.right, False))

            # delete the child node from the tree if it is to be deleted
            if curr.left and curr.left.val in toDelete:
                curr.left = None

            if curr.right and curr.right.val in toDelete:
                curr.right = None

        return res
