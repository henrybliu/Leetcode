class Solution:
    """
    Ex. 1

    3 4 -1 1

    3 4 0 1

    -3 4 -5 -1

    return 2 as the answer

    Ex. 2
    4 3 2 1

    4 3 2 1

    -4 -3 -2 -1

    return 5 as the answer

    The key realization is that for an array of size n, the smallest possible
    values in consideration would be [1, n+1].

    Time: O(n)
    Space: O(1)

    """

    def firstMissingPositive(self, nums: List[int]) -> int:

        # switch all negative numbers to be negative bc we don't care about them
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0

        # mark numbers that exist in the array to be negative - have this be 1 indexed
        # we only care about numbers that fall within the range [1, len(nums)]
        # for ex: the smallest possible numbers we consider in an array of size 4 is
        # [1,2,3,4] and 5 if all of them exist
        for i in range(len(nums)):
            if 1 <= abs(nums[i]) <= len(nums):
                if nums[abs(nums[i]) - 1] == 0:
                    nums[abs(nums[i]) - 1] = -(len(nums) + 1)
                elif nums[abs(nums[i]) - 1] > 0:
                    nums[abs(nums[i]) - 1] *= -1

        # find the earliest value that isn't negative
        for i in range(len(nums)):
            if nums[i] >= 0:
                return i + 1

        return len(nums) + 1
