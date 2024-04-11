from collections import defaultdict


class Solution:
    """
    Use two hashmaps to store the number of 1s per row and column. The
    number of zeros can then be computed by the length of the row/column
    minus the number of 1s (sum).

    Time: O(m*n)
    Space: O(m*n)

    """

    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:

        rows = len(grid)
        cols = len(grid[0])

        # store the counts for 1s in a row/column
        rowCount = defaultdict(int)
        colCount = defaultdict(int)

        # count number of 1s per row
        for r in range(rows):
            rowCount[r] = sum(grid[r])

        # count number of 1s per column
        for c in range(cols):
            summ = 0
            for r in range(rows):
                summ += grid[r][c]
            colCount[c] = summ

        # for each index just calculate and return the original grid
        for r in range(rows):
            for c in range(cols):
                onesRow = rowCount[r]
                onesCol = colCount[c]
                zerosRow = rows - onesRow
                zerosCol = cols - onesCol

                grid[r][c] = onesRow + onesCol - zerosRow - zerosCol

        return grid
