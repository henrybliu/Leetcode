class Solution:
    """
    Idea is to keep track of the previous iteration's minimum and maximum
    values. That way we can try to mulitply to those values and find an even
    larger value.

    We want to keep the most minimum value for when we encounter a negative
    value.

    We should also consider the current value itself to be a start of a new
    subarray.

    Time: O(n)
    Space: O(1)
    """

    def maxProduct(self, nums: List[int]) -> int:
        currMin = nums[0]
        currMax = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            # need to save currMax and currMin to prevent them from being overwritten
            prevMax = currMax
            prevMin = currMin

            currMax = max(nums[i], max(nums[i] * prevMax, nums[i] * prevMin))
            currMin = min(nums[i], min(nums[i] * prevMax, nums[i] * prevMin))
            res = max(res, max(currMax, currMin))

        return res
