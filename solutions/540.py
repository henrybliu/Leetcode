class Solution:
    """
    Use binary search to check if a number is valid. Take advantage of the fact
    that only 2 instances of a number will occur at most so an the first
    occurrence should be on an even index and the second on an odd.

    Time: O(logn)
    Space: O(1)
    """

    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        # have a helper function -- want to find idx that doesn't match neighbors
        def check(idx):
            if idx == 0:
                return nums[idx] != nums[idx + 1]
            elif idx == len(nums) - 1:
                return nums[idx] != nums[idx - 1]
            else:
                return nums[idx] != nums[idx + 1] and nums[idx] != nums[idx - 1]

        # perform binary search
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                return nums[mid]
            # if at an odd index
            if mid % 2 == 1:
                if nums[mid] == nums[mid - 1]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if nums[mid] == nums[mid + 1]:
                    l = mid + 1
                else:
                    r = mid - 1
