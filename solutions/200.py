class Solution:
    '''
    When encountering a '1' that we haven't visited, we want to mark all of
    that island's land as visited and increase the count for the number of
    islands.
    
    Time: O(m*n)
    Space: O(m*n)
    '''
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        #helper function to mark coordinates as visited
        def dfs(r,c):
            #return 0 if out of bounds, not on an island, or visited this coordinate already
            if (r< 0 or c<0 or r>=rows or c>=cols or grid[r][c]=='0' or (r,c) in visited):
                return 
            visited.add((r,c))

            for v,h in directions:
                dfs(r+v,c+h)

        count = 0
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c]=='1':
                    count +=1
                    dfs(r,c)

        return count