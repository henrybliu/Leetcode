class Solution:
    """
    Map the directions to coordinates and use a set to keep track of visited
    coordinates.

    Time: O(n)
    Space: O(n)
    """

    def isPathCrossing(self, path: str) -> bool:
        operations = {"N": [0, 1], "S": [0, -1], "E": [1, 0], "W": [-1, 0]}

        x = 0
        y = 0

        visited = set()
        visited.add((0, 0))

        for i in range(len(path)):
            op = path[i]
            x += operations[op][0]
            y += operations[op][1]

            if (x, y) in visited:
                return True

            visited.add((x, y))

        return False
