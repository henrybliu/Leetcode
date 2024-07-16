# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Perform DFS while keeping track of the current path taken. We can use the
    same list and make a copy of it to prevent a memory limit exceeded with too
    large of a recursive stack. We create the paths for each start and
    destination node and finally remove their common prefixes. This leaves us
    with the shortest path between them. The path down to the start node will
    always be flipped to "U".

    Time: O(V+E)
    Space: O(V)
    """

    def getDirections(
        self, root: Optional[TreeNode], startValue: int, destValue: int
    ) -> str:
        startPath = [None]
        destPath = [None]

        def dfs(root, path):
            if not root:
                return

            if root.val == startValue:
                startPath[0] = path.copy()
            if root.val == destValue:
                destPath[0] = path.copy()

            path.append("R")
            dfs(root.right, path)
            path.pop()

            path.append("L")
            dfs(root.left, path)
            path.pop()

        dfs(root, [])
        startPath = startPath[0]
        destPath = destPath[0]

        i = 0
        while i < len(startPath) and i < len(destPath) and startPath[i] == destPath[i]:
            i += 1

        startPath = startPath[i:]
        destPath = destPath[i:]

        return "U" * len(startPath) + "".join(destPath)
