class Solution:
    """
    This requires knowing a niche algorithm involving fast and slow pointers.

    Time: O(logn)
    Space: O(1)
    """

    def findDuplicate(self, nums: List[int]) -> int:
        # find point of intersection
        slow = nums[0]
        fast = nums[0]
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if slow == fast:
                break

        # find the duplicate
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
