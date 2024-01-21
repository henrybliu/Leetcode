class Solution:
    '''
    At each house, we can choose to either rob the house or to skip. If we
    choose to rob the house, the amount of money stolen is the current house
    plus the sum 2 houses ago. If we choose to skip, then the current amount
    of money stolen so far is the value stolen so far at the previous house.

    Time: O(n)
    Space: O(1)
    '''
    def rob(self, nums: List[int]) -> int:
        prev = 0
        prev2 = 0

        for i in range(len(nums)):
            nums[i] = max(prev, nums[i]+prev2)
            prev2 = prev
            prev = nums[i]

        return nums[-1]