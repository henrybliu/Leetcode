class Solution:
    '''
    We can use DP to help us solve the question of how many out-of-bounds
    positions will our current position yield in addition to the number of
    moves and positions we were at previously.

    Example:
    0 moves
    0 0 0

    1 moves
    3 2 3

    2 moves
    5 8 5

    3 moves
    11 12 11

    Looking at the last index at the 2nd move, we can observe that that
    position yields 3 out of bounds possibilities. Moving from the left, we
    then have 2 + 3 out of bounds paths at the coordinate (0,2).
    
    Time: O(maxMove * m * n)
    Space: O(m*n)
    '''
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:

        mod = 10**9 + 7
        rows = m
        cols = n
        grid = [[0 for _ in range(cols)] for _ in range(rows)]

        for m in range(maxMove):
            curr = [[0 for _ in range(cols)] for _ in range(rows)]
            for r in range(rows):
                for c in range(cols):
                    # check left
                    if c-1 < 0:
                        curr[r][c] = (curr[r][c] + 1) % mod
                    else:
                        curr[r][c] = (curr[r][c] + grid[r][c-1]) % mod

                    # check right
                    if c+1 >= cols:
                        curr[r][c] = (curr[r][c] + 1) % mod
                    else:
                        curr[r][c] = (curr[r][c] + grid[r][c+1]) % mod

                    # check down
                    if r+1 >= rows:
                        curr[r][c] = (curr[r][c] + 1) % mod
                    else:
                        curr[r][c] = (curr[r][c] + grid[r+1][c]) % mod

                    # check up
                    if r-1 < 0:
                        curr[r][c] = (curr[r][c] + 1) % mod
                    else:
                        curr[r][c] = (curr[r][c] + grid[r-1][c]) % mod
                    
            grid = curr

        return grid[startRow][startColumn]