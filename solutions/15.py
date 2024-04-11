class Solution:
    """
    For a value in nums, find in the right-side of the remaining array where the other two elements will create a total sum of 0. To prevent duplicate numbers, we don't want to search while the values to the left/right are the same.

    Time: O(n^2)
    Space: O(n)
    """

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            # check for duplicates
            if i - 1 >= 0 and nums[i] == nums[i - 1]:
                continue

            # what we are searching for to add to 0
            target = -nums[i]

            l = i + 1
            r = len(nums) - 1

            while l < r:
                currSum = nums[l] + nums[r]
                if currSum == target:
                    res.append([nums[i], nums[l], nums[r]])
                    r -= 1
                    l += 1
                elif currSum > target:
                    r -= 1
                else:
                    l += 1

                while r + 1 < len(nums) and r >= 0 and nums[r] == nums[r + 1]:
                    r -= 1

                while l - 1 > i and l <= len(nums) - 1 and nums[l] == nums[l - 1]:
                    l += 1

        return res
