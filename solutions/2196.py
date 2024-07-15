# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Create the tree as you iterate through the parent, child, and isLeft
    values. Return the node that doesn't have a parent.

    Time: O(n)
    Space: O(n)
    """

    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        mapp = {}
        hasParent = set()

        for parent, child, isLeft in descriptions:
            if parent not in mapp:
                mapp[parent] = TreeNode(parent)

            if child not in mapp:
                mapp[child] = TreeNode(child)

            if isLeft:
                mapp[parent].left = mapp[child]
            else:
                mapp[parent].right = mapp[child]

            hasParent.add(child)

        for parent in mapp.keys():
            if parent not in hasParent:
                return mapp[parent]
