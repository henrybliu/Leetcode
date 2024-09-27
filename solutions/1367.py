# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Create a helper function that checks if starting at the current node will
    result in a match. There is a match when there are no more linked list
    nodes to traverse
    """

    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        # helper function to check if the downward nodes are a match
        def check(llRoot, treeRoot):
            if not llRoot:
                return True

            if not llRoot or not treeRoot or llRoot.val != treeRoot.val:
                return False

            left = check(llRoot.next, treeRoot.left)
            right = check(llRoot.next, treeRoot.right)

            return True if left or right else False

        # traverse down the tree
        def dfs(root):
            if not root:
                return False

            if root.val == head.val:
                if check(head, root):
                    return True

            left = dfs(root.left)
            right = dfs(root.right)

            return True if left or right else False

        return dfs(root)
