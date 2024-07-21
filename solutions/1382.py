# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Use in-order traversal to create a sorted list of numbers. To create a
    balanced binary tree, used the created list of sorted numbers and add the
    middle value to each subtree.
    """

    def balanceBST(self, root: TreeNode) -> TreeNode:
        nums = []

        def inOrder(root):
            if not root:
                return

            inOrder(root.left)
            nums.append(root.val)
            inOrder(root.right)

        # use indices instead of splicing to preserve time complexity
        def createTree(l, r):
            if l > r:
                return None

            mid = l + (r - l) // 2
            root = TreeNode(nums[mid])
            root.left = createTree(l, mid - 1)
            root.right = createTree(mid + 1, r)

            return root

        inOrder(root)
        return createTree(0, len(nums) - 1)
