import math


class Solution:
    """
    Perform binary search to test different rates at which we can eat the bananas at

    Time: O(nlogn)
    Space: O(1)
    """

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # find if we can finish all of the bananas at this speed and less than h
        def check(speed):
            time = 0
            for pile in piles:
                time += math.ceil(pile / speed)

            return time <= h

        l = 1
        r = max(piles)

        while l < r:
            mid = l + (r - l) // 2
            if check(mid):
                r = mid
            else:
                l = mid + 1

        return l
