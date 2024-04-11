class Solution:
    """
    Brute force is O(n^2) and there is a way to use prefixSum to compute this.
    We can keep track of the ongoing currSum and subtract off prefixSums that
    would result in our currSum to be equal to k. prefixSums are the sums that
    we had previously created.

    Time: O(n)
    Space: O(n)
    """

    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0: 1}
        res = 0
        currSum = 0

        for num in nums:
            currSum += num
            diff = currSum - k

            res += prefix.get(diff, 0)
            prefix[currSum] = 1 + prefix.get(currSum, 0)

        return res
