class Solution:
    '''
    When placing down queens, we cannot have queens on the same row, column, or
    diagonals as previously placed queens. We can work down the board, trying
    to place a queen on each row. If we are able to reach the bottom row, then
    we have successfuly placed all n queens.    

    Time: O(2^n)
    Space: O(n^2) - in the worst case we store the entire board

    where n is the number of queens to place on an nxn board
    '''
    def solveNQueens(self, n: int) -> List[List[str]]:
        ROWS = n
        COLS = n
        res = []

        board = [["." for _ in range(n)] for _ in range(n)]

        rows = set()
        cols = set()
        lr = set()
        rl = set()

        def backtrack(r):
            if r == n:
                res.append(["".join(row) for row in board])
                return

            # we go one row at a time
            for c in range(n):
                leftDiag = r+c
                rightDiag = r-c

                # try to add to a column in the current row
                if (leftDiag not in lr and rightDiag not in rl and r not in rows and c not in cols):
                    cols.add(c)
                    rows.add(r)
                    lr.add(leftDiag)
                    rl.add(rightDiag)
                    board[r][c] = 'Q'
                    backtrack(r+1)

                    # reset the board
                    cols.remove(c)
                    rows.remove(r)
                    lr.remove(leftDiag)
                    rl.remove(rightDiag)
                    board[r][c] = '.'

            return
            
        backtrack(0)
        return res