class Solution:
    """
    Use a merge intervals approach. If there is overlap, we can shoot the same
    arrow.

    Time: O(nlogn)
    Space: O(n)
    """

    def findMinArrowShots(self, points: List[List[int]]) -> int:
        stack = []

        points.sort()

        stack.append((points[0][0], points[0][1]))

        for i in range(1, len(points)):
            currL = points[i][0]
            currR = points[i][1]

            l = stack[-1][0]
            r = stack[-1][1]

            if currL <= r:
                stack.pop()
                stack.append((max(currL, l), min(r, currR)))
            else:
                stack.append((currL, currR))

        return len(stack)
