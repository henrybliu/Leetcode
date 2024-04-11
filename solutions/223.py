class Solution:
    """
    Calculating the area of the different rectangles is straightforward.
    Calculating the amount of overlap is a little more tricky.

    This latter steps involves finding where the overlap occurrs on the x and y
    axes.

    On the x-axis, the overlap is always:
    - the leftmost right-side
    - the rightmost left-side

    On the y-axis, the overlap is always:
    - the bottommost top-side
    - the topmost bottom-side

    Of course, there is still the case when there is no overlap. In this case,
    the amount of overlap would be negative.

    Time: O(1)
    Space: O(1)
    """

    def computeArea(
        self,
        ax1: int,
        ay1: int,
        ax2: int,
        ay2: int,
        bx1: int,
        by1: int,
        bx2: int,
        by2: int,
    ) -> int:
        area1 = abs(ax1 - ax2) * abs(ay1 - ay2)
        area2 = abs(bx1 - bx2) * abs(by1 - by2)

        overlapY = min(ay2, by2) - max(ay1, by1)
        overlapX = min(ax2, bx2) - max(ax1, bx1)

        if overlapY < 0 or overlapX < 0:
            return area1 + area2
        else:
            diffArea = overlapY * overlapX
            return area1 + area2 - diffArea
