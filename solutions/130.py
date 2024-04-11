class Solution:
    """
    We can perform dfs on the 'O' that lie on the edge of the matrix. These are
    the 'O' areas that cannot be surrounded by 'X' in all 4 directions. All
    other cells must then be 'X'.

    Time: O(n*m)
    Space: O(n*m)
    """

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows = len(board)
        cols = len(board[0])
        visited = set()

        # perform dfs to mark positions that we can reach from the edge
        def dfs(i, j):
            if (
                (i, j) in visited
                or i < 0
                or i >= rows
                or j < 0
                or j >= cols
                or board[i][j] == "X"
            ):
                return
            visited.add((i, j))
            for v, h in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dfs(i + v, j + h)

        # perform dfs from the edges of the matrix
        for c in range(cols):
            if board[0][c] == "O":
                dfs(0, c)

            if board[rows - 1][c] == "O":
                dfs(rows - 1, c)

        for r in range(rows):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][cols - 1] == "O":
                dfs(r, cols - 1)

        # change O to X if it cannot touch an edge
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited:
                    board[r][c] = "X"
