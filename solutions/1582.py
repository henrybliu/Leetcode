from collections import defaultdict

class Solution:
    '''
    Can use two hashmaps to keep track of the number of zeros/ones per row/column
    
    Time: O(m*n)
    Space: O(m*n)
    '''
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])

        # best time complexity is O(m*n)
        # store the counts of 1s in cols and rows
        rowCount = defaultdict(int)
        colCount = defaultdict(int)

        # count 1s in row
        for r in range(rows):
            rowCount[r] = sum(mat[r])

        # count 1s in col
        for c in range(cols):
            summ = 0
            for r in range(rows):
                summ += mat[r][c]
            colCount[c]=summ

        res = 0

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 1 and colCount[c]-1==0 and rowCount[r]-1==0:
                    res+=1

        return res

        