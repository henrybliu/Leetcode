class Solution:
    """
    We can transform this problem into using prefix sums where we add 1 when we
    encounter a 1 and subtract 1 when encountering a 0. This would help us
    identify 2 things:

    1.) When the prefix sum is 0, we have encountered an equal number of 1s and
    0s.
    2.) When we see the same prefix sum, then that means after the first
    occurrence, we encountered an equal number of 1s and 0s.

    Time: O(n)
    Space: O(n)
    """

    def findMaxLength(self, nums: List[int]) -> int:
        res = 0
        currSum = 0
        sums = {}

        for i in range(len(nums)):
            currSum += 1 if nums[i] == 1 else -1
            if currSum == 0:
                res = i + 1
            elif currSum in sums:
                res = max(res, i - sums[currSum])
            else:
                sums[currSum] = i
        return res
