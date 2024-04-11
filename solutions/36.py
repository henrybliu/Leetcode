from collections import defaultdict


class Solution:
    """
    Create 3 hashmaps storing the seen numbers per column, row, and 3x3 grid.

    Time: O(m*n)
    Space: O(m*n)
    """

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        grid = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    if (
                        board[r][c] in row[r]
                        or board[r][c] in col[c]
                        or board[r][c] in grid[(r // 3, c // 3)]
                    ):
                        return False

                    row[r].add(board[r][c])
                    col[c].add(board[r][c])
                    grid[(r // 3, c // 3)].add(board[r][c])

        return True
