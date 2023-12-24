class Solution:
    '''
    We can create two sets of the coordinates visited by both oceans. Then
    return the coordinates that can be visited by both oceans.

    Time: O(m*n)
    Space: O(m*n)
    '''
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #can search up from pacific and up from atlantic and then find the overlapping coordinates
        
        rows, cols = len(heights),len(heights[0])
        both = []
        pacific, atlantic = set(), set()
        
        def dfs(r,c, visit, previousHeight):
            if ((r,c) in visit or
               (r<0 or c<0 or r==rows or c==cols) or
               heights[r][c] < previousHeight):
                return
            
            visit.add((r,c))
            dfs(r-1,c, visit, heights[r][c])
            dfs(r,c+1, visit, heights[r][c])
            dfs(r+1, c, visit, heights[r][c])
            dfs(r,c-1, visit, heights[r][c])
        
        #search top and bottom rows
        for c in range(cols):
            dfs(0,c, pacific, heights[0][c])
            dfs(rows-1,c, atlantic, heights[rows-1][c])
        
        #search left and right columns
        for r in range(rows):
            dfs(r,0, pacific, heights[r][0])
            dfs(r,cols-1,atlantic, heights[r][cols-1])
            
            
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific and (r,c) in atlantic:
                    both.append([r,c])
    
        return both
                