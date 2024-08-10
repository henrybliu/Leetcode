class Solution:
    """
    Create an enlarged matrix and then run DFS on that matrix to find the number of regions
    """

    def regionsBySlashes(self, grid: List[str]) -> int:
        largeRows = len(grid) * 3
        largeCols = len(grid[0]) * 3
        newGrid = [[" " for _ in range(largeCols)] for _ in range(largeRows)]

        def createMark(r, c, character):
            currR = r * 3
            currC = c * 3
            # creates mark from top right to bottom left
            if character == "/":
                currC += 2
                newGrid[currR][currC] = "x"
                newGrid[currR + 1][currC - 1] = "x"
                newGrid[currR + 2][currC - 2] = "x"
            # creates mark from top left to bottom right
            else:
                newGrid[currR][currC] = "x"
                newGrid[currR + 1][currC + 1] = "x"
                newGrid[currR + 2][currC + 2] = "x"

        smallRows = len(grid)
        smallCols = len(grid)

        for r in range(smallRows):
            c = 0
            while c < smallCols:
                if grid[r][c] == "/":
                    createMark(r, c, "/")
                elif grid[r][c] == "\\":
                    createMark(r, c, "\\")
                c += 1

        visited = set()

        def dfs(r, c):
            if (
                (r, c) in visited
                or r < 0
                or r >= largeRows
                or c < 0
                or c >= largeCols
                or newGrid[r][c] == "x"
            ):
                return

            visited.add((r, c))
            dfs(r + 1, c)
            dfs(r, c + 1)
            dfs(r - 1, c)
            dfs(r, c - 1)

        res = 0

        for r in range(largeRows):
            for c in range(largeCols):
                if newGrid[r][c] == " " and (r, c) not in visited:
                    res += 1
                    dfs(r, c)

        return res
