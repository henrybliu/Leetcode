class Solution:
    '''
    Create a helper function that will calculate the average per coordinate
    while also checking for valid coordinates.

    Time: O(n*m)
    Space: O(n*m)
    '''
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows = len(img)
        cols = len(img[0])
        res = [[0 for _ in range(cols)] for _ in range(rows)]

        directions = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,0],[0,1],[1,-1],[1,0],[1,1]]

        def calcAvg(i,j):
            summ = 0
            valid = 0

            for v,h in directions:
                newI = i + v
                newJ = j + h

                if newI >= 0 and newI < rows and newJ >= 0 and newJ < cols:
                    valid += 1
                    summ += img[newI][newJ]

            return summ//valid

        for r in range(rows):
            for c in range(cols):
                res[r][c] = calcAvg(r,c)

        return res