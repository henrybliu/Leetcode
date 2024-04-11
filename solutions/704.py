class Solution:
    """
    This is the binary search template.

    Time: O(logn)
    Space: O(1)
    """

    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1

        if nums[l] != target:
            return -1
        else:
            return l
