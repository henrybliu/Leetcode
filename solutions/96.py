class Solution:
    """
    At each position, we can count the number of trees that can be formed to
    the left and right of the root. Then multiply the number of trees that can
    be formed on each side to form the total number of trees with this root.

    Example:
    0 nodes: 1 type of tree - the null tree
    1 nodes: 1 tree
    2 nodes: 2 trees

    With 3 nodes, we have roots that can be 1, 2, or 3.

    With root as 1, we can form 2 subtrees on the right using 2 and 3
    With root as 2, we can form 1 sub trees on either side
    With root as 3, we can form 2 sub trees on the left using 1 and 2

    Extending this realization, for a number of nodes in the tree, we will sum
    up the different possible tree organizations by iterating through which
    node is the root.

    Time: O(n^2)
    Space: O(n)
    """

    def numTrees(self, n: int) -> int:
        dp = [1 for _ in range(n + 1)]

        for numNodes in range(2, n + 1):
            numTrees = 0

            for i in range(1, numNodes + 1):
                numNodesLeft = i - 1
                numNodesRight = numNodes - i
                numTrees += dp[numNodesLeft] * dp[numNodesRight]

            dp[numNodes] = numTrees

        return dp[n]
