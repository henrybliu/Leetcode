from collections import deque


class Solution:
    """
    We can use BFS to calculate the shortest path that can reach the n^2 number
    if possible. We also need to calculate the coordinate that corresponds to
    each number to check if a number is at a snake or ladder.

    Time: O(n^2)
    Space: O(1)
    """

    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        nSquared = n**2

        def findCoords(num):
            row = 0
            col = 0

            # calculate how many rows we are from the bottom left
            # every other row starting from the bottom left is a multiple of n
            if num % n == 0:
                row = (num // n) - 1
            else:
                row = num // n

            # increases from left to right
            if row % 2 == 0:
                col = num - (row * n) - 1
            # an odd number of rows from the bottom left means increasing from right to left
            else:
                col = n - (num - (row * n))

            x = n - 1 - row
            y = col
            return (x, y)

        queue = deque()
        visited = set()
        queue.append((1, 0))
        visited.add(1)

        while queue:
            added = set()
            for i in range(len(queue)):
                curr, numMoves = queue.popleft()
                if curr == nSquared:
                    return numMoves

                for newPos in range(curr + 1, min(curr + 6, nSquared) + 1):

                    x, y = findCoords(newPos)
                    if board[x][y] != -1:
                        newPos = board[x][y]
                    if newPos not in visited:
                        queue.append((newPos, numMoves + 1))
                        visited.add(newPos)

        return -1
