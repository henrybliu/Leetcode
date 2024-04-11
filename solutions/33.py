class Solution:
    """
    There are 4 cases to that can occur when performing this type of binary
    search:
    1. if the left half is sorted in ascending order and the target is greater
    than the midpoint
    2. if the left half is sorted in ascending order and the target is less
    than or equal to the midpoint
    3. if the right half is sorted in ascending order and the target is is not
    within the right half's range
    4. if the right half is sorted in ascending order and the target falls
    within the range of the right half

    Time: O(logn)
    Space: O(1)
    """

    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2
            # which half is mid in?
            # if we are in the left half
            if nums[l] <= nums[mid]:
                if target < nums[l] or target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid
            else:
                if target <= nums[mid] or target > nums[r]:
                    r = mid
                else:
                    l = mid + 1

        if nums[l] == target:
            return l
        else:
            return -1
