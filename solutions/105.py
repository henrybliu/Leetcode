# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    A preorder tree traversal is visiting the root node before visiting the
    left, and then the right child nodes. An inorder tree traversal is
    visiting the left child, then the current node, and finally the right
    child.

    Together, we can then realize that the for a node x in the preorder array.
    All nodes to the left of x in the inorder array are to the left of x and
    all nodes to the right of x will be to the right of x in the resulting
    tree.

    Time: O(n)
    Space: O(n) - recursive stack
    """

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def dfs(preorder, inorder):
            if not preorder or not inorder:
                return None

            # create the new node
            root = TreeNode(preorder[0])

            # find index of the pivot point in the inorder list
            rootIndex = inorder.index(preorder[0])

            leftInorder = inorder[:rootIndex]
            rightInorder = inorder[rootIndex + 1 :]
            leftPre = preorder[1 : len(leftInorder) + 1]
            rightPre = preorder[len(leftInorder) + 1 :]

            # create the left child
            root.left = dfs(leftPre, leftInorder)
            # create the right child
            root.right = dfs(rightPre, rightInorder)

            # return the node that was created
            return root

        return dfs(preorder, inorder)
