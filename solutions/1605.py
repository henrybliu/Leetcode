class Solution:
    """
    We want to be greedy here. Use rowSum and colSum as the remaining sum we
    need to achieve for that row and column. At each coordinate, we can place
    down the minimum of the two. After picking the value to place down, we need
    update both sums.

    Time: O(m*n)
    Space: O(m*n)
    """

    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        rows = len(rowSum)
        cols = len(colSum)
        res = [[0 for _ in range(cols)] for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                val = min(rowSum[r], colSum[c])
                rowSum[r] -= val
                colSum[c] -= val
                res[r][c] = val

        return res
