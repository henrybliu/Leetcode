from collections import defaultdict
class Solution:
    '''
    Just tedious work but an optimization that can be made is that each grid
    must have 5 in the middle. There are no other combinations that would work 
    otherwise.
    '''
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows = defaultdict(int)
        cols = defaultdict(int)
        # diag is top to bottom
        diagLeftRight = defaultdict(int)
        diagRightLeft = defaultdict(int)

        ROWS = len(grid)
        COLS = len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                rows[(r,c)] = grid[r][c] + rows[(r, c-1)]
                cols[(r,c)] = grid[r][c] + cols[(r-1,c)]
                diagLeftRight[(r,c)] = grid[r][c] + diagLeftRight[(r-1,c-1)]
                diagRightLeft[(r,c)] = grid[r][c] + diagRightLeft[(r-1,c+1)]

        res = 0 

        # calculate number of valid 3x3 grids
        for r in range(1, ROWS-1):
            for c in range(1, COLS-1):
                if grid[r][c] != 5:
                    continue
                nums = []
                validGrid = True

                for num in grid[r-1][c-1:c+2]:
                    if num < 1 or num > 9:
                        validGrid = False
                    nums.append(num)

                for num in grid[r][c-1:c+2]:
                    if num < 1 or num > 9:
                        validGrid = False
                    nums.append(num)

                for num in grid[r+1][c-1:c+2]:
                    if num < 1 or num > 9:
                        validGrid = False
                    nums.append(num)

                if not validGrid or len(set(nums))!= len(nums):
                    continue

                topRow = rows[(r-1, c+1)] - rows[(r-1,c-2)]
                midRow = rows[(r, c+1)] - rows[(r,c-2)]
                bottomRow = rows[(r+1, c+1)] - rows[(r+1,c-2)]

                leftCol = cols[(r+1, c-1)] - cols[(r-2,c-1)]
                midCol = cols[(r+1, c)] - cols[(r-2,c)]
                rightCol = cols[(r+1, c+1)] - cols[(r-2,c+1)]

                leftRight = diagLeftRight[(r+1, c+1)] - diagLeftRight[(r-2,c-2)]
                rightLeft = diagRightLeft[(r+1, c-1)] - diagRightLeft[(r-2,c+2)]
                
                if topRow == midRow == bottomRow == leftCol == midCol == rightCol == leftRight == rightLeft:
                    res += 1

        return res