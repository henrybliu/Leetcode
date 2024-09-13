class Solution:
    """
    Simulate all possible results and memoize subproblems
    """

    def stoneGame(self, piles: List[int]) -> bool:

        # use memoization
        visited = {}

        def dfs(l, r):
            if l > r:
                return 0

            if (l, r) in visited:
                return visited[(l, r)]

            aliceTurn = True
            if l - r + 1 % 2 == 1:
                aliceTurn = False

            # we don't care what Bob's score is when it is his turn, we just
            # want to pass back up Alice's score
            left = piles[l] if aliceTurn else 0
            right = piles[r] if aliceTurn else 0

            visited[(l, r)] = max(left + dfs(l + 1, r), right + dfs(l, r - 1))

            return visited[(l, r)]

        # Alice wins if her score is greater than half the points
        return dfs(0, len(piles) - 1) > sum(piles) // 2
