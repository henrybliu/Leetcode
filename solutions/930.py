class Solution:
    '''
    Use prefix sum to keep track of the number of subarrays that can be created
    at each prefix sum. When we have encountered a currSum - goal that we have
    already seen, it basically means that we already surpassed the goal
    (because counts would only have non-negative key values) and that we are
    basically counting the prefix sums to remove to create a sum of goal.

    For example:

    1 0 1 0 1

    When at the last index, the currSum is 3. Therefore, we can remove the
    prefix sums of 1 to get the goal and why we add the number of subarrays of
    prefix sum 1. In other words, some where along the way, we had increased
    the currSum to 3, and there are 2 more subarrays that could be created if
    these 2 subarrays were removed.
    '''
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        counts = {0:1}
        currSum = 0
        res = 0

        for num in nums:
            currSum += num

            if currSum-goal in counts:
                res += counts[currSum - goal]

            counts[currSum] = counts.get(currSum, 0)+1  

        return res