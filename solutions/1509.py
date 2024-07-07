class Solution:
    """
    Sorting the array will make identifying the 3 largest and 3 smallest values
    the easiest. Replacing a value is the same as updating its value to the
    next smallest/largest value. We do this to minimize the distance between
    the smallest and largest values.

    Time: O(nlogn)
    Space: O(1)
    """

    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0

        nums.sort()
        # remove 3 smallest
        # remove 3 largest
        # remove 2 smallest, 1 largest
        # remove 1 smallest, 2 largest
        # remove 2 largest, 1 smallest -- this is a repeat
        # remove 1 largest, 2 smallest -- this is a repeat
        return min(
            nums[-1] - nums[3],
            nums[-4] - nums[0],
            nums[-2] - nums[2],
            nums[-3] - nums[1],
        )
