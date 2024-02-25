class Solution:
    '''
    At each position in nums, we can choose to either add the number to th
    running sum or to start a new subarray.

    Time: O(n)
    Space: O(1)
    '''
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = nums[0]
        maxSum = nums[0]

        for i in range(1, len(nums)):
            currSum = max(currSum + nums[i], nums[i])
            maxSum = max(maxSum, currSum)

        return maxSum