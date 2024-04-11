class Solution:
    """
    Can use binary search to solve this problem after realizing that for an
    arithmetic sequence, the sum of integers that are stricly in an increasing
    order by 1 can be computed by the average value multiplied by the length of
    the sequence.

    For example:
    1 2 3 4 5

    1 + 2 + 3 + 4 + 5 = 15

    ((1 + 5)//2) * 5 = 15

    We can use this fact to binary search to find the solution.

    Time: O(logn)
    Space: O(1)
    """

    def pivotInteger(self, n: int) -> int:
        l = 1
        r = n

        while l <= r:
            mid = l + (r - l) // 2

            leftSum = ((1 + mid) / 2) * (mid - 1 + 1)
            rightSum = ((mid + n) / 2) * (n - mid + 1)

            if leftSum == rightSum:
                return mid
            elif leftSum > rightSum:
                r = mid - 1
            else:
                l = mid + 1

        return -1
