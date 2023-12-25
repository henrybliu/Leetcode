from collections import deque
class Solution:
    '''
    First identify all of the parts of one island and add those coordinates to
    a queue. Perform BFS to find the fewest number of flips needed to get from
    the first island to any point on the second island.
    
    Time: O(m*n)
    Space: O(m*n)
    '''
    def shortestBridge(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 1:
                return
            q.append((r, c))
            grid[r][c] = -1
            for v,h in directions:
                dfs(r + v, c + h)

        def bfs():
            flips = 0
            while q:
                for i in range(len(q)):
                    r, c = q.popleft()
                    for v, h in directions:
                        newR = r + v
                        newC = c + h
                        if newR < 0 or newC < 0 or newR >= rows or newC >= cols or grid[newR][newC] == -1:
                            continue
                        if grid[newR][newC]:
                            return flips
                        
                        q.append((newR, newC))
                        grid[newR][newC] = -1
                flips += 1
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    dfs(r, c)
                    return bfs()
          