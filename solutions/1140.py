class Solution:
    """
    Use memoization to backtrack and recorded already visited nodes. We can
    treat this like a minimax tree.

    When it is Bob's turn, we return the minimum value that Alice can achieve.

    When it is Alice's turn, we return the maximum value that she can achieve.

    Time: O(2 * n * n * n) -- this takes into account if it is alice's turn,
    the index, the value of M, and looping through 1 to 2*M

    Space: O(2 * n * n) -- this doesn't take into account the looping of 1 to
    2*M bc of the memoization
    """

    def stoneGameII(self, piles: List[int]) -> int:
        dp = {}

        def dfs(aliceTurn, idx, M):
            if idx >= len(piles):
                return 0

            if (aliceTurn, idx, M) in dp:
                return dp[(aliceTurn, idx, M)]

            # this is to keep track of the current sum of the stones that were
            # collected within the range (1, 2*M)
            total = 0
            # set to infinity when Bob's turn to always take the minimum value
            res = 0 if aliceTurn else float("inf")
            for X in range(1, 2 * M + 1):
                if idx + X > len(piles):
                    break

                # decrement by 1 to include the current index
                total += piles[idx + X - 1]

                # on alice's turn, return the max possible result that can be
                # yielded
                if aliceTurn:
                    res = max(res, total + dfs(not aliceTurn, idx + X, max(M, X)))
                # on max's turn, return the smallest possible result that Alice
                # an yield
                else:
                    res = min(res, dfs(not aliceTurn, idx + X, max(M, X)))

            dp[(aliceTurn, idx, M)] = res
            return res

        return dfs(True, 0, 1)
