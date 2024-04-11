class Solution:
    """
    For diagonal movements, that is the same as either moving horizontally or
    vertically.

    Time: O(n)
    Space: O(1)
    """

    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        def dist(x1, y1, x2, y2):
            return max(abs(x1 - x2), abs(y1 - y2))

        time = 0
        for i in range(1, len(points)):
            x1 = points[i - 1][0]
            y1 = points[i - 1][1]

            x2 = points[i][0]
            y2 = points[i][1]

            time += dist(x1, y1, x2, y2)

        return time
