class Solution:
    """'
    Use two pointers and work inwards to create the outer 'walls'.

    Time: O(n)
    Space: O(1)
    """

    def trap(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1
        # have two maxes to only take add trapped water from the lower max height
        lMax, rMax = height[l], height[r]

        while l < r:
            if lMax < rMax:
                l += 1
                lMax = max(lMax, height[l])
                res += lMax - height[l]

            else:
                r -= 1
                rMax = max(rMax, height[r])
                res += rMax - height[r]

        return res
