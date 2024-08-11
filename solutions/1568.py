class Solution:
    """
    The key realization is that it takes at most 2 days to create a separate
    island. Adding two "water" at a diagonal can create a new island. To solve
    this problem, we can try setting a land cell to be water and to keep
    checking if multiple islands are created.

    Time: O((m*n)^2)
    Space: O(m*n)
    """

    def minDays(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(r, c, visited):
            if (
                r < 0
                or r >= ROWS
                or c < 0
                or c >= COLS
                or grid[r][c] == 0
                or (r, c) in visited
            ):
                return

            visited.add((r, c))

            dfs(r + 1, c, visited)
            dfs(r, c + 1, visited)
            dfs(r - 1, c, visited)
            dfs(r, c - 1, visited)

        def countNumIslands():
            numIslands = 0
            visited = set()

            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] == 1 and (r, c) not in visited:
                        dfs(r, c, visited)
                        numIslands += 1

            return numIslands

        currNumIslands = countNumIslands()

        if currNumIslands != 1:
            return 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    grid[r][c] = 0
                    newCount = countNumIslands()
                    if newCount != 1:
                        return 1
                    grid[r][c] = 1

        return 2
