class Solution:
    """
    Can do this in one pass by keeping track of the maximum number encountered
    so far.

    Time: O(n)
    Space: O(1)
    """

    def maxProduct(self, nums: List[int]) -> int:
        res = 0
        currMax = nums[0]

        for i in range(1, len(nums)):
            res = max(res, (currMax - 1) * (nums[i] - 1))
            currMax = max(currMax, nums[i])

        return res
