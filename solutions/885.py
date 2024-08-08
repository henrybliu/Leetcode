class Solution:
    """Just simulate all of the possible coordinates that we can reach. Notice
    that the first spiral moves right, down, left, up 1, 1, 2, and 2 units
    respectively. Each direction increases by 2 with each spiral"""

    def spiralMatrixIII(
        self, rows: int, cols: int, rStart: int, cStart: int
    ) -> List[List[int]]:
        right = 1
        down = 1
        left = 2
        up = 2

        totalCells = rows * cols
        visitedCells = 1
        x = rStart
        y = cStart

        res = [[rStart, cStart]]

        def isValid(r, c):
            if r >= 0 and r < rows and c >= 0 and c < cols:
                return True

            return False

        while visitedCells < totalCells:
            # right
            for r in range(right):
                y += 1
                if isValid(x, y):
                    visitedCells += 1
                    res.append([x, y])
            right += 2

            # down
            for c in range(down):
                x += 1
                if isValid(x, y):
                    visitedCells += 1
                    res.append([x, y])
            down += 2

            # left
            for r in range(left):
                y -= 1
                if isValid(x, y):
                    visitedCells += 1
                    res.append([x, y])
            left += 2

            # up
            for c in range(up):
                x -= 1
                if isValid(x, y):
                    visitedCells += 1
                    res.append([x, y])
            up += 2

        return res
