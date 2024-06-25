import heapq


class Solution:
    """
    The time it takes to reach the bottom right cell is the largest value that
    we have encountered so far in the path. We can implement Dijkstra's to
    solve this. We prioritize tuples of (wait time, x-coordinate, y-coordinate)
    with the lowest wait time and where wait time is the largest cell value
    encountered so far. Visited cells are only added to the priority queue
    when they are first encountered or a cheaper path (lower wait time) is
    found.
    """

    def swimInWater(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        costs = {}
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # initialize with first cell's values
        # (cost, x-coord, y-coord)
        startCost = grid[0][0]
        pq = [(startCost, 0, 0)]
        costs[(0, 0)] = startCost

        while pq:
            currCost, x, y = heapq.heappop(pq)

            if x == rows - 1 and y == cols - 1:
                return currCost

            for v, h in directions:
                newY = y + v
                newX = x + h

                # check if the adjacent cell is inbounds and if there
                # exists a cheaper path
                if (
                    newX >= 0
                    and newX < rows
                    and newY >= 0
                    and newY < cols
                    and ((newX, newY) not in costs or costs[(newX, newY)] > newCost)
                ):
                    newCost = max(currCost, grid[newX][newY])
                    costs[(newX, newY)] = newCost
                    heapq.heappush(pq, (newCost, newX, newY))
