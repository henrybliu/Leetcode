class Solution:
    """
    This question can be reduced to just finding the maximum distance between
    two x coordinates.

    Time: O(nlogn)
    Space: O(n)
    """

    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        xCoords = []
        for x, y in points:
            xCoords.append(x)

        xCoords.sort()

        dist = 0
        prev = xCoords[0]

        for i in range(1, len(xCoords)):
            currDist = xCoords[i] - prev
            dist = max(dist, currDist)
            prev = xCoords[i]

        return dist
