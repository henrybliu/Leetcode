from collections import defaultdict


class Solution:
    """
    We need to compute the slopes between each pair of points and then the
    y-intercept that forms the line between the two points. We then store the
    slope and y-interncept of pairs of points in a hashmap to count the number
    of points have the same formula or line. In the case that there is a
    vertical line, we instead store an infinite slope and the x intercept.

    Time: O(n^2)
    Space: O(n^2)
    """

    def maxPoints(self, points: List[List[int]]) -> int:
        def calcSlopeY(x1, y1, x2, y2):
            slope = float("inf")
            y = None

            if x2 - x1:
                slope = (y2 - y1) / (x2 - x1)
                y = -x1 * slope + y1
            # if there is an infinite slope, just store the x intercepts instead
            else:
                y = x1

            return (slope, y)

        if len(points) == 1:
            return 1

        slopes = defaultdict(set)
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                slopes[calcSlopeY(x1, y1, x2, y2)].add((x1, y1))
                slopes[calcSlopeY(x1, y1, x2, y2)].add((x2, y2))

        length = 0
        for v in slopes.values():
            length = max(length, len(v))
        return length
