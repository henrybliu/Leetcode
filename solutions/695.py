class Solution:
    '''
    For each piece of land/island we encounter and that we haven't visited, we
    can calculate its area by exploring (dfs/bfs) its connected areas. We then
    take the max of each island's area.

    Time: O(n*m)
    Space: O(n*m)
    '''
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0

        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        def dfs(i,j):
            #if out of bounds or seen before, or is water, stop the search
            if (i<0 or i >= rows or j<0 or j>= cols or (i,j) in visited or grid[i][j] ==0):
                return 0

            visited.add((i,j))

            return 1 + dfs(i-1,j)+ dfs(i+1,j) + dfs(i,j+1) +  dfs(i,j-1)


        for i in range(rows):
            for j in range(cols):
                if grid[i][j]== 1:
                    maxArea = max(maxArea,dfs(i,j))

        return maxArea