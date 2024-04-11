class Solution:
    """
    Compute the largest area by first maximizing the width before moving
    inwards to find the maximum height.

    Time: O(n)
    Space: O(1)
    """

    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        l = 0
        r = len(height) - 1

        while l < r:
            area = (r - l) * min(height[l], height[r])
            maxArea = max(maxArea, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return maxArea
