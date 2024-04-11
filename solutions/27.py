class Solution:
    """
    This is just removing an element from the nums input.

    Time: O(n)
    Space: O(1)
    """

    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)

        return len(nums)
