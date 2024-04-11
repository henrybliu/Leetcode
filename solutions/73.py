class Solution:
    """
    We can use the top row of the matrix to keep track of which columns need to
    be zeroed out. We can also use the leftmost column to keep track of which
    rows need to be zeroed out. However, the top left coorindate is in both the
    leftmost column and topmost row. To resolve this, we can use a boolean to
    keep track of if the leftmost column also needs to be zeroed out.

    Time: O(mn)
    Space: O(1)
    """

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        infinity = float("inf")

        leftColumn = False

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    if c == 0:
                        leftColumn = True
                    else:
                        matrix[0][c] = infinity

                    matrix[r][0] = infinity

        # zero out columns to the right of the first column
        for c in range(1, cols):
            if matrix[0][c] == infinity:
                for r in range(rows):
                    matrix[r][c] = 0

        # zero out all of the rows
        for r in range(rows):
            if matrix[r][0] == infinity:
                for c in range(cols):
                    matrix[r][c] = 0

        # zero out the left column
        if leftColumn:
            for r in range(rows):
                matrix[r][0] = 0
