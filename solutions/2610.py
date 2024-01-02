from collections import defaultdict
class Solution:
    '''
    We can use a hashmap to keep track of which row that a number occurs in. To
    save space, instead of storing each row that a number should appear in
    (hashmap of lists), we can just use a count for each number. The count (c)
    indicates that a number needs to occur in all of the rows up to c-1. For
    example, if a number were to occur 4 times. It would appear in rows indexed
    at 0, 1, and 2.
    
    Time: O(n)
    Space: O(n)
    '''
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        res = []
        # this counts the maximum number of rows that each number belongs in
        rows = defaultdict(int)
        numRows = 0

        for num in nums:
            rows[num]+=1
            numRows = max(numRows, rows[num])

        # if all numbers can fit in the same row
        if numRows == 0: 
            numRows +=1

        # add the numbers to rows for up its number of occurrences
        for i in range(numRows):
            res.append([])

        for k,v in rows.items():
            for r in range(v):
                res[r].append(k)

        return res