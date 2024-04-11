class Solution:
    """
    Use binary search to find the peak element - this number will be greater
    than the right and the left

    Time: O(logn)
    Space: O(1)
    """

    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1

        return l
