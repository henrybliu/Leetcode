# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    We can have a set that keeps track of the pairs that we can form at each
    child node. If a pair can be formed, we remove it from the pairs set. This
    helps maintain the number of odd (unpaired) occurrences for any number.
    Then, when encountering a leaf node, we check if the number if the set is
    of length 1 or less. This signifies that there is only 1 or 0 occurences of
    a number that couldn't be paired.

    Time: O(n)
    Space: O(n^2)
    """

    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        def dfs(root, pairs):
            if not root:
                return 0

            if root.val in pairs:
                pairs.remove(root.val)
            else:
                pairs.add(root.val)

            # we can add to the count if there is only 1 or 0 occurrences of a
            # number that doesn't have a pair
            if not root.left and not root.right:
                if len(pairs) <= 1:
                    return 1
                else:
                    return 0

            # need to create new copies of pairs
            left = dfs(root.left, set(pairs))
            right = dfs(root.right, set(pairs))

            return left + right

        return dfs(root, set())
