# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Use post-order traversal to count the distances to leaf nodes. If the
    distance between the leaf nodes is less than or equal to distance,
    increment the result. Pass up an array of the distance to get to the leaf
    node.

    Time: O(V^2) -- when visiting a node, we are summing leaf node distances
    Space: O(V)
    """

    def countPairs(self, root: TreeNode, distance: int) -> int:
        res = [0]

        def dfs(root):
            if not root:
                return []
            if not root.left and not root.right:
                return [1]

            leftDistances = dfs(root.left)
            rightDistances = dfs(root.right)

            for leftDist in leftDistances:
                if leftDist >= distance:
                    continue
                for rightDist in rightDistances:
                    if leftDist + rightDist <= distance:
                        res[0] += 1

            return [leftDist + 1 for leftDist in leftDistances] + [
                rightDist + 1 for rightDist in rightDistances
            ]

        dfs(root)
        return res[0]
