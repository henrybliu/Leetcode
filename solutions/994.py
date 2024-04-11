from collections import deque


class Solution:
    """
    We first count the  number of fresh oranges. We then do bfs from the rotten
    oranges either until the queue is empty or that there are no more fresh
    oranges. The queue being emtpy can indicate that all fresh oranges that can
    be reached have been infected but not all of the fresh oranges that exist
    within the grid.

    Time: O(n*m)
    Space: O(n*m)
    """

    def orangesRotting(self, grid: List[List[int]]) -> int:
        # count the number of fresh oranges
        fresh = 0
        rotten = 0

        rows = len(grid)
        cols = len(grid[0])
        q = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    rotten += 1
                    q.append((i, j))

        time = 0

        # perform bfs
        while q and fresh > 0:
            time += 1
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            # loop through the directions and check if fresh -- turn it into rotten
            for i in range(len(q)):
                curr = q.popleft()
                currR, currC = curr
                for v, h in directions:
                    newR = currR + v
                    newC = currC + h

                    # if it is in bounds, is fresh, add it to the q and update the value on the grid
                    if (
                        newR < 0
                        or newR >= rows
                        or newC < 0
                        or newC >= cols
                        or grid[newR][newC] != 1
                    ):
                        continue

                    grid[newR][newC] = 2
                    q.append((newR, newC))
                    fresh -= 1

        if fresh == 0:
            return time
        else:
            return -1
